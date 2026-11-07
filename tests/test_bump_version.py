"""Exercise the release command and date gates in disposable Git repositories."""

import datetime as dt
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("bump_version", ROOT / "scripts/bump_version.py")
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)
FILES = (*release.JSON_MANIFESTS, "plugin.yaml", release.SKILL,
         "tests/test_manifest_versions.py", release.CHANGELOG)


class ReleaseCommandTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        for name in (*FILES, "scripts/bump_version.py", ".gitignore"):
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)
        self.git("init", "--quiet")
        self.git("config", "user.name", "Release test")
        self.git("config", "user.email", "release@example.invalid")
        self.commit()
        self.old_version, self.old_day = release.STAMP.findall((self.root / release.SKILL).read_text())[0]
        self.version = f"{release.version_key(self.old_version)[0] + 1}.0.0"
        self.today = dt.datetime.now(dt.timezone.utc).date()

    def git(self, *args, env=None):
        return subprocess.run(["git", *args], cwd=self.root, env=env, text=True,
                              capture_output=True, check=True).stdout

    def commit(self):
        self.git("add", ".")
        self.git("commit", "--quiet", "-m", "Fixture")

    def command(self, version=None, day=None):
        # Invoke by absolute path from elsewhere, as maintainers may do.
        return subprocess.run(
            [sys.executable, "-B", str(self.root / "scripts/bump_version.py"),
             version or self.version, str(day or self.today)],
            cwd=self.root / "tests", text=True, capture_output=True, check=False,
        )

    def snapshot(self):
        return {name: (self.root / name).read_bytes() for name in FILES}

    def assert_refused(self, message, **args):
        before = self.snapshot()
        result = self.command(**args)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(message, result.stderr)
        self.assertEqual(self.snapshot(), before, "a refused bump must not partially update files")

    def test_one_command_updates_every_release_field_and_preserves_history(self):
        old_history = (self.root / release.CHANGELOG).read_text()
        result = self.command()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("8 files", result.stdout)
        self.assertEqual(set(self.git("diff", "--name-only").splitlines()), set(FILES))
        for name in release.JSON_MANIFESTS:
            self.assertEqual(json.loads((self.root / name).read_text())["version"], self.version)
        self.assertIn(f"version: {self.version}\n", (self.root / "plugin.yaml").read_text())
        self.assertEqual(release.STAMP.findall((self.root / release.SKILL).read_text()),
                         [(self.version, str(self.today))])
        self.assertIn(f'EXPECTED_VERSION = "{self.version}"',
                      (self.root / "tests/test_manifest_versions.py").read_text())
        history = (self.root / release.CHANGELOG).read_text()
        rows = release.HISTORY_ROW.findall(history)
        self.assertEqual(rows[0][:2], (self.version, str(self.today)))
        self.assertEqual(history.replace(f"| {' | '.join(rows[0])} |\n", "", 1), old_history)
        check = subprocess.run([sys.executable, "-B", "tests/test_manifest_versions.py"],
                               cwd=self.root, capture_output=True, text=True)
        self.assertEqual(check.returncode, 0, check.stderr)

    def test_staged_unstaged_and_untracked_changes_are_refused(self):
        target = self.root / "package.json"
        original = target.read_bytes()
        for kind in ("unstaged", "staged", "untracked"):
            with self.subTest(kind=kind):
                if kind == "untracked":
                    (self.root / "notes.txt").write_text("unfinished")
                else:
                    target.write_bytes(original + b"\n")
                    if kind == "staged":
                        self.git("add", "package.json")
                self.assert_refused("working tree is dirty")
                if kind == "untracked":
                    (self.root / "notes.txt").unlink()
                else:
                    target.write_bytes(original)
                    self.git("add", "package.json")

    def test_same_day_release_and_ignored_build_outputs_are_allowed(self):
        (self.root / "dist").mkdir()
        (self.root / "dist/package.zip").write_bytes(b"build output")
        result = self.command(day=self.old_day)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_invalid_versions_and_dates_leave_all_files_unchanged(self):
        for version in ("2.0", "v2.0.0", "2.0.0-rc.1", "02.0.0", self.old_version, "0.0.1"):
            with self.subTest(version=version):
                self.assert_refused("version", version=version)
        for day in ("2026-02-30", "20261107", "2026-1-07", str(self.today + dt.timedelta(days=1))):
            with self.subTest(day=day):
                self.assert_refused("date", day=day)
        self.assert_refused("before the previous release",
                            day=dt.date.fromisoformat(self.old_day) - dt.timedelta(days=1))

    def test_late_validation_failure_does_not_write_earlier_manifests(self):
        path = self.root / release.CHANGELOG
        path.write_text(path.read_text().replace(f"| {self.old_version} |", "| 0.0.0 |", 1))
        self.commit()
        self.assert_refused("CHANGELOG.md must start")

    def test_manifest_drift_is_refused_before_any_write(self):
        path = self.root / "plugin.json"
        path.write_text(path.read_text().replace(self.old_version, "0.0.0"))
        self.commit()
        self.assert_refused("plugin.json: version disagrees")

    def test_preceding_tag_uses_version_order_and_utc_day(self):
        for tag, timestamp in (("v1.0.0", "2026-11-05T12:00:00+00:00"),
                               ("v1.1.0", "2026-11-05T23:30:00-02:00"),
                               ("v2.0.0", "2026-11-07T12:00:00+00:00"),
                               ("other", "2026-11-07T12:00:00+00:00")):
            self.git("tag", "-a", tag, "-m", tag, env={**os.environ, "GIT_COMMITTER_DATE": timestamp})
        self.assertEqual(release.previous_tag_date(self.root, "2.0.0"), dt.date(2026, 11, 6))
        self.assertIsNone(release.previous_tag_date(self.root, "0.1.0"))

    def test_lightweight_tag_uses_commit_date_and_source_archive_has_no_tag_bound(self):
        self.git("tag", "v0.0.1")
        timestamp = self.git("show", "-s", "--format=%cI", "HEAD").strip()
        self.assertEqual(release.previous_tag_date(self.root, self.version),
                         dt.datetime.fromisoformat(timestamp).astimezone(dt.timezone.utc).date())
        with tempfile.TemporaryDirectory() as archive:
            self.assertIsNone(release.previous_tag_date(Path(archive), self.version))

    def test_tag_bound_is_enforced_by_both_command_and_manifest_test(self):
        day = dt.date.fromisoformat(self.old_day) + dt.timedelta(days=1)
        self.git("tag", "-a", "v0.0.1", "-m", "Fixture", env={
            **os.environ, "GIT_COMMITTER_DATE": f"{day}T00:00:00+00:00"})
        self.assert_refused("before the previous release", day=self.old_day)
        check = subprocess.run([sys.executable, "-B", "tests/test_manifest_versions.py", "ManifestVersionTests"],
                               cwd=self.root, capture_output=True, text=True)
        self.assertNotEqual(check.returncode, 0)
        self.assertIn("before the previous release", check.stderr)

    def test_manifest_test_rejects_future_date_and_malformed_version_without_tags(self):
        self.assertIsNone(release.previous_tag_date(self.root, self.version))
        path = self.root / release.SKILL
        original = path.read_text()
        for stamp, message in ((f"This copy is version {self.old_version}, released {self.today + dt.timedelta(days=1)}.",
                                "after today"),
                               (f"This copy is version 1.2, released {self.old_day}.", "invalid version")):
            with self.subTest(stamp=stamp):
                path.write_text(release.STAMP.sub(stamp, original))
                check = subprocess.run([sys.executable, "-B", "tests/test_manifest_versions.py", "ManifestVersionTests"],
                                       cwd=self.root, capture_output=True, text=True)
                self.assertNotEqual(check.returncode, 0)
                self.assertIn(message, check.stderr)

    def test_reported_november_typo_fails_on_release_day(self):
        with self.assertRaisesRegex(ValueError, "after today"):
            release.validate_release_date(dt.date(2026, 11, 30), today=dt.date(2026, 11, 3))


if __name__ == "__main__":
    unittest.main()
