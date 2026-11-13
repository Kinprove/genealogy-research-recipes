"""The proof-judgment recipe keeps the four thin-evidence rules from issue #291 in its hard rules.

An assistant always reads a judgment recipe's rules section, so each test pins its rule inside
that section: a later edit that moves a rule elsewhere, or drops its required action, fails here.
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


class ThinEvidenceHardRulesTests(unittest.TestCase):
    def setUp(self):
        self.rules = between(
            recipe("evidence-proof-judgment.md"),
            "## Hard rules — apply these before you rule",
            "## What the HUMAN must own",
        )

    def test_sole_surviving_candidate_needs_a_discriminating_field(self):
        rule = between(self.rules, "13. **A sole surviving candidate is still only a candidate.**", "14. ")
        self.assertIn('do not conclude "no other record exists, so this is the person"', rule)
        self.assertIn("the absence of rivals does not confirm identity", rule)
        self.assertIn("Name a field that would separate the person you are looking for from an unseen namesake", rule)
        self.assertIn("If no record gives such a field, record the identity as unresolved.", rule)

    def test_name_forms_prove_neither_identity_nor_difference(self):
        rule = between(self.rules, "14. **Possible short and full forms of one name prove neither identity nor difference.**", "15. ")
        self.assertIn("shows neither that the records describe one man nor that they describe two", rule)
        self.assertIn("state which observation would settle it", rule)
        self.assertIn("(jewish-genealogy-conditional-hypotheses.md#2-separate-the-propositions-before-combining-clues)", rule)

    def test_compiler_hedge_survives_into_derived_records(self):
        rule = between(self.rules, "15. **A compiler's hedge is evidence of uncertainty in its own right.**", "16. ")
        self.assertIn("carry that qualifier into every record you derive from it", rule)
        self.assertIn("Finding no other document either way does not remove the hedge.", rule)

    def test_plain_and_hedged_claims_are_separate_propositions(self):
        rule = self.rules[self.rules.index("16. **Split a sentence that states one link plainly and hedges another.**") :]
        self.assertIn("(#using-working-hypotheses-without-inheriting-their-assumptions)", rule)
        self.assertIn("and rule on each separately", rule)
        self.assertIn("write each as its own entry and keep the hedge on the parentage", rule)
        self.assertIn("Accepting the marriage does not accept the parentage.", rule)


if __name__ == "__main__":
    unittest.main()
