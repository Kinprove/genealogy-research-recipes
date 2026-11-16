"""Exercise release guards against the pinned ClawHub CLI's JSON contracts."""

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
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


if __name__ == "__main__":
    unittest.main()
