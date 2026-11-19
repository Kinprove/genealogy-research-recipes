"""Source sidecars carry no heading that dates when sources were added; that history belongs in the PR.

A dated recheck heading ("Platform recheck, 2026-11-12") records a check, which is evidence, and stays.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "skills/genealogy-research-recipes/sources"
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
DATE = re.compile(rf"\b(?:\d{{4}}-\d{{2}}-\d{{2}}|\d{{1,2}} (?:{MONTHS}) \d{{4}})\b")
ADDITION = re.compile(r"\b(?:added|additions?|additional)\b", re.IGNORECASE)


def history_headings(text):
    """Return the headings that date an addition of sources."""
    return [line for line in text.splitlines()
            if line.startswith("#") and DATE.search(line) and ADDITION.search(line)]


class HistoryHeadingTests(unittest.TestCase):
    def test_rule_rejects_addition_dates_and_keeps_rechecks(self):
        self.assertEqual(history_headings("### Sources added 2026-11-20"), ["### Sources added 2026-11-20"])
        self.assertEqual(history_headings("## Additional sources checked 2 November 2026"),
                         ["## Additional sources checked 2 November 2026"])
        self.assertEqual(history_headings("### Sources for the 2026-11-12 additions"),
                         ["### Sources for the 2026-11-12 additions"])
        self.assertEqual(history_headings("### Platform recheck, 2026-11-12"), [])
        self.assertEqual(history_headings("### Additions and recheck, 2026-11-16"),
                         ["### Additions and recheck, 2026-11-16"])
        self.assertEqual(history_headings("### Additional sources"), [])
        self.assertEqual(history_headings("Sources added 2026-11-20 in prose is not a heading"), [])

    def test_sources_files_have_no_history_headings(self):
        files = sorted(SOURCES.glob("*.md"))
        self.assertGreater(len(files), 100)
        found = {path.name: history_headings(path.read_text(encoding="utf-8")) for path in files}
        self.assertEqual({name: lines for name, lines in found.items() if lines}, {})


if __name__ == "__main__":
    unittest.main()
