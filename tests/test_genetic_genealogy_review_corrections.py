"""The WATO, mtDNA and ethnicity recipes keep the corrections from issue #218.

Each test pins a corrected rule inside the section where it lives and, where the old wording was
wrong, checks that it is gone, so a later edit cannot quietly bring it back.
"""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES = ROOT / "skills/genealogy-research-recipes/recipes"


def recipe(name: str) -> str:
    """Return a recipe's text with each run of whitespace folded to one space."""
    return " ".join((RECIPES / name).read_text(encoding="utf-8").split())


def between(text: str, start: str, end: str) -> str:
    """Return the part of text from start up to (not including) the next end."""
    begin = text.index(start)
    return text[begin : text.index(end, begin + len(start))]


class FamilyTreeDnaTransferTests(unittest.TestCase):
    def test_match_selection_names_the_files_familytreedna_accepts(self):
        text = recipe("unknown-parentage-wato.md")
        section = between(
            text,
            "## Match selection dominates the answer",
            "## When two hypotheses survive",
        )
        rule = between(section, "**Which files FamilyTreeDNA accepts", "**Privacy gate:**")
        self.assertIn("only from AncestryDNA, 23andMe and MyHeritage", rule)
        self.assertIn("AncestryDNA test taken in 2026 or processed by Ancestry after September 2025", rule)
        self.assertIn("from May 2012 through September 2025 can be uploaded", rule)
        self.assertIn("not the date the file was downloaded", rule)
        self.assertIn("only tests run on the GSA chip", rule)
        self.assertIn("[N60 @", rule)
        self.assertLess(section.index("- **Grow the pool across databases.**"), section.index(rule))


class MitochondrialDistanceTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("ydna-mtdna-interpretation.md")

    def test_only_positions_309_and_315_are_excluded_from_the_count(self):
        section = between(
            self.text,
            "### 3 — NEVER treat mtDNA genetic distance",
            "### 4 — NEVER assert a non-paternity event",
        )
        self.assertIn("**completely excludes the poly-C insertion positions 309 and 315**", section)
        self.assertIn("only 309/315 are GD-*excluded*", section)
        self.assertIn("only 309/315 are excluded.", section)
        prompt = between(
            self.text,
            "4. **Name the positions before ranking mtDNA matches by GD.**",
            "5. **Force the alternative-explanations list",
        )
        self.assertIn("only 309/315 are excluded.", prompt)

    def test_the_522_523_exclusion_is_gone(self):
        self.assertNotIn("522/523", self.text)
        self.assertNotIn("by community/historical convention", self.text)


class AncestryReportingMinimumTests(unittest.TestCase):
    def test_the_legacy_half_percent_rule_is_not_the_current_minimum(self):
        text = recipe("ethnicity-estimate-version-comparison.md")
        section = between(
            text,
            "## 7. Apply the version's own reliability floor to small regions",
            "## 8. Keep a version log",
        )
        self.assertIn("Ancestry reports only regions above a minimum share, which it does not publish.", section)
        note = section[section.index("**An older Ancestry page's 0.5% is not this minimum.**") :]
        self.assertIn("estimate is below 0.5% and its range does not exceed 2.5% [S23]", note)
        self.assertIn("not the 2025 or 2026 method", note)
        self.assertIn("Do not record 0.5% as the reporting minimum of either version.", note)


if __name__ == "__main__":
    unittest.main()
