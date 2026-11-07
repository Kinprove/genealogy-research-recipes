"""Exercise the CI entry point with the real pinned gitleaks image and disposable repos.

Run explicitly in the gitleaks job; ordinary unit tests do not require Docker.
"""

import os
from pathlib import Path
import random
import shutil
import string
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCAN = ROOT / "scripts/check_secrets.sh"


class SecretScanTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="secret-scan-")
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        # Keep local Git settings, hooks and signing out of the fixture commits.
        self.env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
        self.git("init", "--initial-branch=main")
        shutil.copyfile(ROOT / ".gitleaks.toml", self.repo / ".gitleaks.toml")
        self.commit("Clean repository")

    def git(self, *args):
        return subprocess.run(
            ["git", "-c", "core.hooksPath=/dev/null", "-c", "user.name=Secret scan test",
             "-c", "user.email=secret-scan@example.invalid", *args],
            cwd=self.repo, env=self.env, check=True, capture_output=True, text=True,
        )

    def commit(self, message):
        self.git("add", "--all")
        self.git("commit", "-m", message)

    def add_fake_key(self):
        # Construct an intentionally fake GitHub PAT without storing a token-shaped
        # literal in the test source or this project's history.
        key = "ghp_" + "".join(random.Random(67).choices(string.ascii_letters + string.digits, k=36))
        (self.repo / "credentials.txt").write_text("token=" + key + "\n", encoding="utf-8")

    def scan(self, expected):
        result = subprocess.run(
            ["bash", str(SCAN)], cwd=self.repo, env=self.env,
            capture_output=True, text=True, timeout=180,
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)

    def test_clean_repository_passes(self):
        self.scan(0)

    def test_untracked_key_fails(self):
        self.add_fake_key()
        self.scan(1)

    def test_added_then_deleted_key_fails(self):
        self.add_fake_key()
        self.commit("Add a fake key")
        (self.repo / "credentials.txt").unlink()
        self.commit("Delete the fake key")
        self.scan(1)

    def test_key_on_another_branch_fails(self):
        self.git("switch", "-c", "other")
        self.add_fake_key()
        self.commit("Add a fake key on another branch")
        self.git("switch", "main")
        self.scan(1)

    def test_missing_config_fails(self):
        (self.repo / ".gitleaks.toml").unlink()
        self.scan(1)

    def test_invalid_config_fails(self):
        (self.repo / ".gitleaks.toml").write_text("[invalid", encoding="utf-8")
        self.scan(1)

    def test_container_error_is_preserved(self):
        tools = self.repo / "bin"
        tools.mkdir()
        docker = tools / "docker"
        docker.write_text("#!/bin/sh\nexit 42\n", encoding="utf-8")
        docker.chmod(0o700)
        self.env["PATH"] = str(tools) + os.pathsep + self.env["PATH"]
        self.scan(42)


if __name__ == "__main__":
    unittest.main(verbosity=2)
