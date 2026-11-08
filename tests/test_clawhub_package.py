"""Regression checks for the Kinprove native ClawHub package."""

import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tracked_files():
    """Return the repository's tracked files, so local untracked folders stay out of the pack."""
    git = shutil.which("git")
    if git and (ROOT / ".git").exists():
        result = subprocess.run(
            [git, "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True, timeout=60,
        )
        return [path for path in result.stdout.decode("utf-8").split("\0") if path]
    ignored = {".git", "node_modules", "__pycache__"}
    return [
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and not ignored.intersection(path.relative_to(ROOT).parts)
    ]


class ClawHubPackageTests(unittest.TestCase):
    def test_package_scope_matches_the_publishing_owner(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertEqual(package["name"], "@kinprove/genealogy-research-recipes")

    def test_registry_metadata_preserves_source(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertEqual(package.get("repository"), {
            "type": "git",
            "url": "https://github.com/Kinprove/genealogy-research-recipes.git",
        })

    def test_package_is_publicly_packable(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertIs(package.get("private", False), False)

    def test_compatibility_starts_at_the_tested_openclaw_release(self):
        package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertEqual(package["openclaw"].get("compat"), {"pluginApi": ">=2026.9.8"})
        self.assertEqual(package["openclaw"].get("build"), {"openclawVersion": "2026.9.8"})

    def test_npm_artifact_ships_only_native_code_and_complete_skill_resources(self):
        npm = shutil.which("npm")
        if npm is None:
            if os.environ.get("CI"):
                self.fail("npm is required in CI to exercise the real package artifact")
            self.skipTest("npm not installed")
        tracked = tracked_files()
        skill = ROOT / "skills" / "genealogy-research-recipes"
        expected = {
            "package.json", "index.js", "openclaw.plugin.json", "README.md", "LICENSE", "NOTICE",
            "skills/genealogy-research-recipes/SKILL.md",
            "skills/genealogy-research-recipes/CHANGELOG.md",
            "skills/genealogy-research-recipes/LICENSE",
            "skills/genealogy-research-recipes/NOTICE",
        }
        for directory in ("recipes", "sources", "scripts", "resources"):
            prefix = (skill / directory).relative_to(ROOT).as_posix() + "/"
            resources = {
                path for path in tracked
                if path.startswith(prefix) and "__pycache__" not in path.split("/")
                and not path.endswith(".pyc") and not path.endswith("/.DS_Store")
            }
            self.assertTrue(resources, f"Missing {directory} resources")
            expected.update(resources)

        with tempfile.TemporaryDirectory(prefix="kinprove-npm-pack-") as directory:
            temporary = Path(directory)
            source = temporary / "source"
            for relative in tracked:
                target = source / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / relative, target)
            (source / "untracked-output.txt").write_text("must not ship\n", encoding="utf-8")
            cache = source / "skills" / "genealogy-research-recipes" / "scripts" / "__pycache__"
            cache.mkdir(parents=True)
            (cache / "lookup_beider_name.pyc").write_bytes(b"must not ship")
            # Ignore the developer's own ~/.npmrc.
            userconfig = temporary / "empty-npmrc"
            userconfig.write_text("", encoding="utf-8")
            env = {**os.environ, "NPM_CONFIG_USERCONFIG": str(userconfig)}
            result = subprocess.run(
                [npm, "pack", "--ignore-scripts", "--json", "--pack-destination", str(temporary)],
                cwd=source, env=env, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=120,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            packages = json.loads(result.stdout)
            self.assertEqual(len(packages), 1, packages)
            package = packages[0]
            self.assertEqual(package["name"], "@kinprove/genealogy-research-recipes")
            with tarfile.open(temporary / package["filename"], "r:gz") as archive:
                members = archive.getmembers()
                self.assertTrue(all(member.isfile() for member in members), "Unexpected non-file tar member")
                self.assertEqual({member.name for member in members}, {"package/" + path for path in expected})
                self.assertEqual(len(members), len(expected), "Duplicate tar member")
                self.assertEqual(package["entryCount"], len(expected))
                for relative in expected:
                    with self.subTest(resource=relative):
                        resource = archive.extractfile("package/" + relative)
                        assert resource is not None, relative
                        with resource:
                            self.assertEqual(resource.read(), (ROOT / relative).read_bytes())
                # Exercise links against the actual installed artifact: a source-only
                # file must not accidentally make a packaged route look valid.
                installed = temporary / "installed"
                archive.extractall(installed, members=members)
                sys.path.insert(0, str(skill / "evals"))
                from checks import static_checks
                static_checks(installed / "package/skills/genealogy-research-recipes")


if __name__ == "__main__":
    unittest.main()
