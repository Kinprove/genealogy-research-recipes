"""The rabbinic-literature recipe keeps the statement-class rules from issue #294.

One publication can mix a facsimile, an editor's identification and an oral chain. Each test pins
a rule inside the section an assistant reads for that step, so a later edit that drops the rule or
moves it out of its section fails here.
"""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPE = ROOT / "skills/genealogy-research-recipes/recipes/rabbinic-literature-person-search.md"
CLASSES = (
    "**facsimile**",
    "**quoted document**",
    "**editor's identification**",
    "**named oral chain**",
    "**unattributed tradition**",
    "**compiler's inference**",
)


def recipe() -> str:
    """Return the recipe's text with each run of whitespace folded to one space."""
    return " ".join(RECIPE.read_text(encoding="utf-8").split())


def between(text: str, start: str, end: str) -> str:
    """Return the part of text from start up to (not including) the next end."""
    begin = text.index(start)
    return text[begin : text.index(end, begin + len(start))]


class StatementClassTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe()
        self.section = between(self.text, "## 9. Classify what each statement rests on", "## 10. ")

    def test_contents_lists_the_new_section_in_order(self):
        contents = between(self.text, "## Contents", "## 1. ")
        self.assertIn("- 8\\. Screen every hit before it becomes a person - 9\\. Classify what each statement rests on", contents)
        self.assertIn("- 10\\. Count witnesses, not copies", contents)

    def test_every_statement_gets_one_class_that_travels_with_it(self):
        step = between(self.section, "1. Give every statement", "2. ")
        for name in CLASSES:
            self.assertIn(name, step)
        self.assertIn("carry the class with the statement into every note, ledger row and tree entry", step)

    def test_class_is_separate_from_the_compilers_certainty(self):
        step = between(self.section, "5. Keep the class apart", "6. ")
        self.assertIn("(section 10)", step)
        self.assertIn("still rests on the editor, not on a document", step)

    def test_a_later_correction_is_a_lead_not_a_report(self):
        step = between(self.section, "6. Treat a later correction as a lead to the earlier text, not as a report of it.", "7. ")
        self.assertIn("Do not paraphrase what the earlier text said, or what the correction rests on,", step)
        self.assertIn("record both as unknown and list the earlier page as the next check", step)

    def test_an_engagement_is_not_written_as_a_marriage(self):
        step = self.section[self.section.index("7. Record an engagement as an engagement.") :]
        self.assertIn("add no marriage, no spouse link and no children of the union", step)
        self.assertIn("the record ends at the engagement", step)
        self.assertIn("חתן and כלה mean a groom and a bride", step)

    def test_a_quotation_or_an_enhanced_scan_is_not_a_second_witness(self):
        witnesses = between(self.text, "## 10. Count witnesses, not copies", "## 11. ")
        self.assertIn("is the compiler's reading of it, not a second reading of the original", witnesses)
        self.assertIn("A cropped or contrast-enhanced copy of one scan is still that scan.", witnesses)

    def test_the_passage_ledger_and_failure_modes_carry_the_rule(self):
        ledger = between(self.text, "## Output: a passage ledger", "## Prompt patterns")
        self.assertIn("| Basis | Facsimile, quoted document, editor's identification", ledger)
        failures = self.text[self.text.index("## Failure modes") :]
        self.assertIn("Paraphrasing an earlier publication from a later publication's correction of it.", failures)
        self.assertIn("Writing an engagement into a tree as a marriage.", failures)


if __name__ == "__main__":
    unittest.main()
