"""The historical map recipe keeps the corrections from the review in issue #217.

Each test pins a corrected fact in its passage and checks that the old wording is gone,
so a later edit cannot quietly bring it back.
"""

import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / "skills/genealogy-research-recipes"
SLUG = "historical-map-record-recovery"


def text(folder: str) -> str:
    """Return the recipe or its sources file with each run of whitespace folded to one space."""
    return " ".join((SKILL / folder / f"{SLUG}.md").read_text(encoding="utf-8").split())


def between(value: str, start: str, end: str) -> str:
    """Return the part of value from start up to (not including) the next end."""
    begin = value.index(start)
    return value[begin : value.index(end, begin + len(start))]


class HistoricalMapReviewTests(unittest.TestCase):
    def test_cassini_map_is_routed_to_cartes_gouv_fr(self):
        france = between(text("recipes"), "- **France:**", "- **France, Napoleonic cadastre:**")
        self.assertIn("cartes.gouv.fr shows the Cassini map [S54 @2026-11-13]", france)
        self.assertIn("It replaced Géoportail (geoportail.gouv.fr), whose pages redirect to cartes.gouv.fr "
                      "from 30 September 2026 [S53 @2026-11-13]", france)
        self.assertNotIn("Géoportail (geoportail.gouv.fr) shows the Cassini map", france)

    def test_topotijdreis_cites_only_what_its_sources_show(self):
        netherlands = between(text("recipes"), "- **Netherlands:**", "- **Norway:**")
        self.assertIn("choose the year on the slider [S43 @2026-11-13]", netherlands)
        self.assertIn("record the sheet's edition year, not the slider year [S42 @2026-11-13]", netherlands)
        self.assertNotIn("1816–1819", netherlands)
        self.assertNotIn("grouped slider years", between(text("sources"), "- **S42:**", "- **S43:**"))


if __name__ == "__main__":
    unittest.main()
