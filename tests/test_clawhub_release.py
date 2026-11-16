"""Exercise release guards against the pinned ClawHub CLI's JSON contracts."""

import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/check_clawhub_release.py"
SPEC = importlib.util.spec_from_file_location("clawhub_release", SCRIPT)
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)
SHA = "a" * 40


def preview():
    return {
        "source": "github:Kinprove/genealogy-research-recipes@v9.8.7",
        "name": "@kinprove/genealogy-research-recipes", "family": "code-plugin",
        "version": "9.8.7", "commit": SHA, "files": 298, "totalBytes": 2143103,
    }


def inspection():
    # Shape observed from the real 1.19.0 inspection on 2026-11-16. Identity values
    # are synthetic; a different latestVersion exercises version-specific checks.
    return {
        "package": {"name": "@kinprove/genealogy-research-recipes", "latestVersion": "10.0.0"},
        "owner": {"handle": "kinprove"},
        "version": {"version": "9.8.7", "verification": {
            "sourceRepo": "Kinprove/genealogy-research-recipes",
            "sourceCommit": SHA, "sourceTag": "v9.8.7", "hasProvenance": False,
        }},
    }


def run_workflow_step(workflow, step_name, data, cli_exit=0):
    step = workflow.split(f"      - name: {step_name}\n", 1)[1].split("\n      - ", 1)[0]
    command = textwrap.dedent(step.split("        run: |\n", 1)[1])
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "scripts").mkdir()
        shutil.copy2(SCRIPT, root / "scripts" / SCRIPT.name)
        (root / "package.json").write_text(json.dumps({"name": "@kinprove/genealogy-research-recipes", "version": "9.8.7"}))
        cli = root / "ci-tools/node_modules/.bin/clawhub"
        cli.parent.mkdir(parents=True)
        cli.write_text(f"#!{sys.executable}\nimport sys\nprint({json.dumps(data)!r})\nsys.exit({cli_exit})\n")
        cli.chmod(0o755)
        # setup-python supplies this command on the runner; macOS may only have python3.
        cli.with_name("python").symlink_to(sys.executable)
        return subprocess.run(
            ["bash", "-e", "-c", command], cwd=root, capture_output=True, text=True, check=False,
            env={**os.environ, "GITHUB_REF": "refs/tags/v9.8.7", "GITHUB_SHA": SHA,
                 "GITHUB_REF_NAME": "v9.8.7", "GITHUB_REPOSITORY": "Kinprove/genealogy-research-recipes",
                 "PATH": str(cli.parent) + os.pathsep + os.environ["PATH"],
                 "VERSION": "9.8.7", "PACKAGE_NAME": "@kinprove/genealogy-research-recipes",
                 "RUNNER_TEMP": str(root), "GITHUB_STEP_SUMMARY": str(root / "summary.md")},
        )


class ClawHubReleaseTests(unittest.TestCase):
    def test_only_the_matching_release_tag_is_accepted(self):
        package = {"name": "@kinprove/genealogy-research-recipes", "version": "9.8.7"}
        self.assertEqual(release.release_version("refs/tags/v9.8.7", package), "9.8.7")
        for ref in ("refs/heads/main", "refs/heads/v9.8.7", "v9.8.7", "refs/tags/v9.8.6"):
            with self.subTest(ref=ref), self.assertRaises(ValueError):
                release.release_version(ref, package)
        for version in (None, 987, "09.8.7", "9.8.7-rc.1", "9.8.7\n"):
            with self.subTest(version=version), self.assertRaises(ValueError):
                release.release_version("refs/tags/v9.8.7", {**package, "version": version})
        with self.assertRaises(ValueError):
            release.release_version("refs/tags/v9.8.7", {**package, "name": "@other/package"})

    def test_preview_rejects_missing_or_wrong_release_identity(self):
        release.verify_preview(preview(), "9.8.7", SHA, "v9.8.7")
        for key, wrong in (
            ("name", "@other/package"), ("family", "bundle-plugin"), ("version", "9.8.6"),
            ("commit", "b" * 40), ("source", "github:other/repo@v9.8.7"),
            ("source", "github:Kinprove/genealogy-research-recipes@main"),
        ):
            for omit in (False, True):
                data = preview()
                data.pop(key) if omit else data.update({key: wrong})
                with self.subTest(key=key, omit=omit), self.assertRaises(ValueError):
                    release.verify_preview(data, "9.8.7", SHA, "v9.8.7")

    def test_only_definitive_publication_passes(self):
        published = {**preview(), "status": "published", "publicationStatus": "published"}
        release.verify_publication(published, "9.8.7", SHA, "v9.8.7")
        for status in (None, "pending", "blocked", "failed", "expired"):
            with self.subTest(status=status), self.assertRaises(ValueError):
                release.verify_publication({**published, "publicationStatus": status}, "9.8.7", SHA, "v9.8.7")

    def test_public_inspection_uses_the_selected_version_and_reports_provenance(self):
        data = inspection()
        self.assertIs(release.verify_inspection(data, "9.8.7", SHA, "v9.8.7"), False)
        del data["version"]["verification"]["hasProvenance"]
        self.assertIsNone(release.verify_inspection(data, "9.8.7", SHA, "v9.8.7"))

    def test_public_inspection_rejects_wrong_or_missing_source_and_owner(self):
        for path, wrong in (
            (("package", "name"), "@other/package"), (("owner", "handle"), "other"),
            (("version", "version"), "10.0.0"),
            (("version", "verification", "sourceRepo"), "other/repo"),
            (("version", "verification", "sourceCommit"), "b" * 40),
            (("version", "verification", "sourceTag"), "main"),
        ):
            for omit in (False, True):
                data = inspection()
                target = data
                for key in path[:-1]:
                    target = target[key]
                target.pop(path[-1]) if omit else target.update({path[-1]: wrong})
                with self.subTest(path=path, omit=omit), self.assertRaises(ValueError):
                    release.verify_inspection(data, "9.8.7", SHA, "v9.8.7")
        for data in (None, [], {}, {**inspection(), "version": None}):
            with self.subTest(data=data), self.assertRaises(ValueError):
                release.verify_inspection(data, "9.8.7", SHA, "v9.8.7")

    def test_context_command_fails_for_a_branch_dispatch(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory) / "package.json"
            package.write_text(json.dumps({"name": "@kinprove/genealogy-research-recipes", "version": "9.8.7"}))
            for ref, expected in (("refs/tags/v9.8.7", 0), ("refs/heads/main", 2)):
                result = subprocess.run(
                    [sys.executable, "-B", str(SCRIPT), "context", str(package)],
                    env={**os.environ, "GITHUB_REF": ref}, capture_output=True, text=True, check=False,
                )
                self.assertEqual(result.returncode, expected, result.stderr)
                if expected == 0:
                    self.assertEqual(result.stdout, "9.8.7\n")
                else:
                    self.assertIn("dispatch at refs/tags/v9.8.7", result.stderr)

    def test_public_inspection_failure_reaches_the_job(self):
        workflow = (ROOT / ".github/workflows/clawhub-publish.yml").read_text(encoding="utf-8")
        step_name = "Verify the public version and report registry provenance"
        valid = run_workflow_step(workflow, step_name, inspection())
        self.assertEqual(valid.returncode, 0, valid.stderr)
        self.assertIn("Registry hasProvenance: false", valid.stdout)
        wrong_source = inspection()
        wrong_source["version"]["verification"]["sourceCommit"] = "b" * 40
        invalid = run_workflow_step(workflow, step_name, wrong_source)
        self.assertNotEqual(invalid.returncode, 0, "The workflow hid the verifier failure behind tee")
        self.assertIn("inspect.version.verification.sourceCommit", invalid.stderr)

    def test_publish_response_is_logged_without_hiding_failures(self):
        workflow = (ROOT / ".github/workflows/clawhub-publish.yml").read_text(encoding="utf-8")
        step_name = "Publish through GitHub OIDC and wait for definitive publication"
        published = {**preview(), "status": "published", "publicationStatus": "published", "attemptId": "attempt-test"}
        valid = run_workflow_step(workflow, step_name, published)
        self.assertEqual(valid.returncode, 0, valid.stderr)
        self.assertIn('"attemptId": "attempt-test"', valid.stdout)
        invalid = run_workflow_step(workflow, step_name, {**published, "commit": "b" * 40})
        self.assertEqual(invalid.returncode, 2, invalid.stderr)
        self.assertIn("publish.commit", invalid.stderr)
        self.assertIn('"attemptId": "attempt-test"', invalid.stdout)
        uncertain = run_workflow_step(workflow, step_name, {"attemptId": "attempt-test"}, cli_exit=23)
        self.assertEqual(uncertain.returncode, 23, uncertain.stderr)
        self.assertIn('"attemptId": "attempt-test"', uncertain.stdout)


if __name__ == "__main__":
    unittest.main()
