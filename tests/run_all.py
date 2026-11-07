"""Run both unit-test suites: the repository's tests/ and the skill's own tests/.

    python3 tests/run_all.py

Exits non-zero when any test fails or when a suite collects no tests.
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUITES = (ROOT / "tests", ROOT / "skills/genealogy-research-recipes/tests")


def main() -> int:
    sys.dont_write_bytecode = True
    ok = True
    for directory in SUITES:
        print(f"== {directory.relative_to(ROOT).as_posix()}", flush=True)
        suite = unittest.defaultTestLoader.discover(str(directory), pattern="test_*.py", top_level_dir=str(directory))
        if suite.countTestCases() == 0:
            print(f"no tests collected in {directory}", file=sys.stderr)
            ok = False
            continue
        result = unittest.TextTestRunner(verbosity=1).run(suite)
        ok = ok and result.wasSuccessful()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
