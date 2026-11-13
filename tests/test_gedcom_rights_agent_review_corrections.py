"""The GEDCOM export, family collection, photograph and agent project recipes keep the corrections from issue #221.

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


class GedcomExportTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("gedcom-research-export.md")

    def test_old_style_rule_names_the_dual_year_exception(self):
        rule = between(self.text, "- **Write an Old Style date as Julian", "- **Keep a dual year.**")
        self.assertIn("except for the 5.5.1 dual-year form below", rule)

    def test_dual_year_uses_the_551_slash_form(self):
        rule = between(self.text, "- **Keep a dual year.**", "- **Do not pad an approximate date.**")
        self.assertIn("`2 DATE 30 JAN 1648/49`", rule)
        self.assertIn("with two digits after the slash and without `@#DJULIAN@`", rule)
        self.assertIn("allows the slash only in its Gregorian date form", rule)
        self.assertIn("`2 DATE JULIAN 30 JAN 1649` with `3 PHRASE 30th of January, 1648/9`", rule)
        self.assertIn("also shows `2 DATE JULIAN 30 JAN 1648`", rule)
        self.assertIn("the PHRASE keeps the literal date", rule)
        self.assertNotIn("carry the literal dual date in a NOTE", self.text)

    def test_conformance_check_names_the_three_551_output_rules(self):
        check = between(self.text, "- **Check that the file conforms", "- **Check that every INDI")
        self.assertIn("That record needs a `NAME`", check)
        self.assertIn("write the name or label the user chooses", check)
        self.assertIn("do not invent one", check)
        self.assertIn("is at most 255 characters", check)
        self.assertIn("counting its `@` signs, is at most 22", check)
        self.assertIn("without adding a space or a line break", check)
        self.assertIn("split between two non-space characters", check)
        self.assertIn("`CONT` marks a line break inside the value", check)


class FamilyCollectionTests(unittest.TestCase):
    def test_copyright_can_pass_by_will_or_inheritance(self):
        text = recipe("family-collection-intake-and-capture.md")
        rule = between(text, "In the United States, a signed deed of gift", "## Check the hand-off")
        self.assertIn("Apart from a will, an inheritance or another transfer made by law itself", rule)
        self.assertIn("a transfer of copyright needs a signed writing", rule)
        self.assertIn("may have inherited the copyright in a relative's own letters", rule)
        self.assertNotIn("Copyright passes only by a signed written transfer", text)


class FamilyPhotographTests(unittest.TestCase):
    def test_commissioner_rule_continues_under_the_1956_act(self):
        text = recipe("family-photograph-attribution-and-dating.md")
        rule = between(text, "The commissioner rule in step 4", "## Bound the date")
        self.assertIn("did not end with Britain's 1911 Act", rule)
        self.assertIn("Copyright Act 1956", rule)
        self.assertIn("paid or agreed to pay for it, was entitled to its copyright", rule)
        self.assertIn("unless an agreement excluded that", rule)
        self.assertIn("in the course of employment unless they agreed otherwise", rule)
        self.assertIn("a commission given before the 1988 Act took effect keeps the earlier rule", rule)
        step = between(text, "4. Record each copy's holder", "5. Another copy's caption")
        self.assertIn("Britain's Copyright Act 1911 gave the copyright in a photograph", step)


class AgentProjectTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("agent-research-project.md")

    def test_only_the_researcher_rules_and_a_relative_gives_an_account(self):
        rule = between(self.text, "- Change a conclusion only when", "- Use a fixed list of written statuses")
        self.assertIn("When the researcher gives a firm ruling", rule)
        self.assertIn("the researcher rules on identity and proof", rule)
        self.assertIn("(evidence-proof-judgment.md)", rule)
        self.assertIn("Record a relative's firm statement in their exact words, as theirs, but keep it an account to assess, not a ruling or a tree fact", rule)
        self.assertIn("(family-interviews-and-oral-tradition.md)", rule)
        self.assertNotIn("a relative with family knowledge gives a firm ruling", self.text)

    def test_replaced_next_step_is_logged_first(self):
        rule = between(self.text, "- Write a status with the way to verify it.", "- Before saying something")
        self.assertIn("Record an outdated next step in the research log as done or dropped, with its result, then replace it in the status", rule)
        self.assertIn("The log keeps the record and analysis that led to the step", rule)
        self.assertIn("(research-documentation.md)", rule)

    def test_unproved_link_stays_off_the_tree_unless_already_there(self):
        rule = between(self.text, "- Do not add an unproved inferred link", "- Give uncertainty a dedicated place")
        self.assertIn("in the research notes or a separate worksheet", rule)
        self.assertIn("When the tree already holds such a link", rule)
        self.assertIn("removing it is a change to the tree that needs approval", rule)
        self.assertIn("Apply the mark only to that link", rule)
        self.assertNotIn("- Mark an unproved inferred link as tentative", self.text)

    def test_obsidian_moves_are_separated_from_tool_moves(self):
        rule = between(self.text, "Obsidian repairs links itself", "## Words the agent must earn")
        self.assertIn("Automatically update internal links setting on", rule)
        self.assertIn("moved with its `move` command", rule)
        self.assertIn("a move made by a script, a shell command or git", rule)
        self.assertIn("check every link", rule)


if __name__ == "__main__":
    unittest.main()
