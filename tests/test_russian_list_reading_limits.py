"""The Russian list recipes keep the reading limits from issue #293.

A male-only family list, an age column reckoned at another year than the file's label, and the
numeric columns of a fiscal list were each misread in field use. Each test pins the rule in the
step where a reader meets that list, and checks that the rule is its own paragraph, so it does
not change the text of a neighbouring paragraph that has a provenance record.
"""

import unittest
from pathlib import Path

RECIPES = Path(__file__).resolve().parents[1] / "skills/genealogy-research-recipes/recipes"


def raw(slug: str) -> str:
    """Return a recipe's text exactly as stored."""
    return (RECIPES / f"{slug}.md").read_text(encoding="utf-8")


def text(slug: str) -> str:
    """Return a recipe with each run of whitespace folded to one space."""
    return " ".join(raw(slug).split())


def between(value: str, start: str, end: str) -> str:
    """Return the part of value from start up to (not including) the next end."""
    begin = value.index(start)
    return value[begin : value.index(end, begin + len(start))]


class RussianListReadingLimitTests(unittest.TestCase):
    def assertOwnParagraph(self, slug: str, opening: str, after: str):
        """The paragraph that starts with opening follows a blank line and the given text."""
        self.assertIn(f"{after}\n\n{opening}", raw(slug))

    def test_volost_step_six_reads_coverage_age_dates_and_columns(self):
        slug = "russian-volost-town-administration-records"
        step = between(text(slug), "## 6. Record inspected entries", "## Output")
        self.assertIn("Write down whom the list covers before you read anyone's absence.", step)
        self.assertIn("women, children, men below or above an age limit, people registered in another "
                      "society, or everyone except the payer", step)
        self.assertIn("A family list made for the call-up can be a list of males only", step)
        self.assertIn("says nothing about whether the women were alive, or about who the sons' mother was",
                      step)
        self.assertIn("Take each age's reference date from its column heading, not from the year on the "
                      "file's label.", step)
        self.assertIn("If the headings leave the reference date open, copy the ages as written and record "
                      "no birth year derived from them.", step)
        self.assertIn("name every column from its heading before you read a number", step)
        self.assertIn("Do not read a figure as an age until a heading says it is one.", step)
        self.assertIn("so it is not a household census", step)
        # The rules come before the step's existing list, as paragraphs of their own.
        self.assertLess(step.index("Write down whom the list covers"), step.index("Copy house, plot"))
        self.assertOwnParagraph(slug, "**Write down whom the list covers",
                                "## 6. Record inspected entries as household observations")
        self.assertIn("so it is not a household census.\n\n- Copy house, plot", raw(slug))

    def test_volost_output_records_coverage_and_headings(self):
        slug = "russian-volost-town-administration-records"
        output = text(slug)[text(slug).index("## Output"):]
        self.assertIn("For each inspected list, also record whom it covers and what it leaves out by "
                      "construction, the reference date of each age column (or \"not resolved\"), and the "
                      "heading of each numeric column (step 6).", output)
        self.assertOwnParagraph(slug, "For each inspected list, also record",
                                "missing sheet counts).")

    def test_estate_substitute_lists_carry_the_limits(self):
        slug = "russian-estate-registration-status"
        step = between(text(slug), "## 4. Choose the record series", "## 5.")
        self.assertIn("Read a substitute list's coverage and columns before you read an absence or an age.",
                      step)
        self.assertIn("A family list made for the call-up can list males only, and a tax list names only "
                      "the people liable", step)
        self.assertIn("if the headings leave an age's reference date open, record no birth year from it",
                      step)
        self.assertIn("(russian-volost-town-administration-records.md#6-record-inspected-entries-as-"
                      "household-observations)", step)
        self.assertOwnParagraph(slug, "**Read a substitute list's coverage",
                                "Do not promise family detail from them. [S1]")

    def test_revision_ages_take_their_date_from_the_heading(self):
        slug = "russian-revision-list-household-chaining"
        step = between(text(slug), "## 5. Test formulas", "## 6.")
        self.assertIn("Take each age column's reference date from its heading, not from the year on the "
                      "file's label or cover.", step)
        self.assertIn("If the headings leave the reference date open, copy the ages as written and derive "
                      "no birth year from them.", step)
        self.assertLess(step.index("reference date from its heading"), step.index("**Compilation date.**"))
        self.assertOwnParagraph(slug, "**Take each age column's reference date",
                                "## 5. Test formulas, placements and ages before using them")

    def test_revision_absence_starts_from_coverage(self):
        slug = "russian-revision-list-household-chaining"
        step = between(text(slug), "## 7. Bound every absence", "## 8.")
        self.assertIn("Start with the list's own coverage.", step)
        self.assertIn("women in a male-only revision (step 3) or in a male-only family list made for the "
                      "call-up", step)
        self.assertIn("so her absence is no evidence of her death or of who the mother was", step)
        self.assertLess(step.index("Start with the list's own coverage."),
                        step.index("A person, household or village that is not found"))
        self.assertOwnParagraph(slug, "Start with the list's own coverage.", "## 7. Bound every absence")

    def test_tax_roll_columns_are_named_before_values_are_read(self):
        slug = "tax-roll-observation-workflow"
        step = between(text(slug), "## 5. Extract one row per entry", "## 6.")
        self.assertIn("Name every column from its heading before you read its values", step)
        self.assertIn("A number beside a name is not an age until a heading says it is one", step)
        self.assertIn("if the heading leaves that date open, record no birth year from those ages", step)
        self.assertLess(step.index("Name every column"), step.index("For each entry, keep:"))
        self.assertOwnParagraph(slug, "Name every column from its heading", "## 5. Extract one row per entry")


if __name__ == "__main__":
    unittest.main()
