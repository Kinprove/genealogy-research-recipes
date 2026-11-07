"""Exercise the combined runner's discovery and exit status in isolated checkouts."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RUNNER = Path(__file__).with_name("run_all.py")
PASS = "import unittest\nclass Example(unittest.TestCase):\n    def test_example(self):\n        pass\n"
FAIL = PASS.replace("        pass", "        self.fail('fixture failure')")


class CombinedRunnerTests(unittest.TestCase):
    def run_fixture(self, root_test, skill_test):
        with tempfile.TemporaryDirectory(prefix="kinprove-test-runner-") as directory:
            root = Path(directory)
            tests = root / "tests"
            skill_tests = root / "skills/genealogy-research-recipes/tests"
            tests.mkdir()
            skill_tests.mkdir(parents=True)
            shutil.copy2(RUNNER, tests / "run_all.py")
            if root_test is not None:
                (tests / "test_root_fixture.py").write_text(root_test, encoding="utf-8")
            if skill_test is not None:
                (skill_tests / "test_skill_fixture.py").write_text(skill_test, encoding="utf-8")
            return subprocess.run(
                [sys.executable, "-I", "-B", str(tests / "run_all.py")],
                cwd=root.parent, capture_output=True, text=True, timeout=20, check=False,
            )

    def test_success_requires_both_suites(self):
        result = self.run_fixture(PASS, PASS)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr.count("Ran 1 test"), 2, result.stderr)

    def test_empty_root_suite_fails_but_runs_skill_suite(self):
        result = self.run_fixture(None, PASS)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no tests collected in", result.stderr)
        self.assertIn("Ran 1 test", result.stderr)

    def test_empty_skill_suite_fails_after_root_suite(self):
        result = self.run_fixture(PASS, None)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no tests collected in", result.stderr)
        self.assertIn("Ran 1 test", result.stderr)

    def test_failed_root_suite_still_runs_skill_suite(self):
        result = self.run_fixture(FAIL, PASS)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("fixture failure", result.stderr)
        self.assertEqual(result.stderr.count("Ran 1 test"), 2, result.stderr)


if __name__ == "__main__":
    unittest.main()
