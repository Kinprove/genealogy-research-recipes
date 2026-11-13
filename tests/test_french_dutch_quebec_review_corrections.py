"""The French, Dutch, Québec and Belgian recipes keep the corrections from issue #211.

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


class FrenchRoutingTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("french-departmental-record-routing.md")

    def test_civil_registration_exceptions_sit_in_step_one(self):
        step = between(self.text, "## 1. Route by département", "## 2. Work out whether the act is open yet")
        self.assertIn("**Savoie and Haute-Savoie have no civil registers for 1816–1860.**", step)
        self.assertIn("took up civil registration again on 1 January 1861", step)
        self.assertIn("**A marriage of 22 September 1798 to 26 July 1800 can be in another commune's register.**", step)
        self.assertIn("From 1 vendémiaire an VII to 7 thermidor an VIII, marriages were celebrated only in the canton's chief town", step)
        self.assertIn("The communes' ten-year tables still list these marriages.", step)
        self.assertIn("the birth acts of 1 January 1870 to 25 May 1871 were also destroyed", step)

    def test_online_delays_are_separate_from_the_access_rule(self):
        step = between(self.text, "## 2. Work out whether the act is open yet", "## 3. Date a death after 1970")
        self.assertIn("a delay of 100 years for putting birth and marriage acts online, which can be cut to 75 years when the margin notes are masked [S13]", step)
        self.assertIn("can be open to the public and still be missing from the AD website", step)

    def test_succession_tables_name_the_tables_before_1825(self):
        step = between(self.text, "## 4. Find a death when the commune is unknown", "### A 1902 Saint-Pierre")
        self.assertIn("**For a death before 1825, search the older tables.**", step)
        self.assertIn("five tables abolished on that day", step)

    def test_paris_census_lists_exist_for_four_years(self):
        step = between(self.text, "## 5. Read the nominative census lists", "## 6. Follow the military record")
        self.assertIn("**In Paris, expect nominative lists for 1926, 1931, 1936 and 1946 only.**", step)
        self.assertIn("except those of 1946, which are seen only in the reading room [S59 @", step)

    def test_military_routing_drops_the_wrong_rules(self):
        step = between(self.text, "### Find a man in the registres matricules", "### Before classe 1867")
        self.assertIn("their registers can be in either département's archives", step)
        self.assertIn("the coverage page lists them for each one [S61 @2026-11-13]", step)
        self.assertIn("In the Bas-Rhin they start with the class of 1893 [S50 @2026-11-13].", step)
        self.assertNotIn("whose archives hold their registers", step)
        self.assertNotIn("about 70 départements", step)
        self.assertNotIn("classes 1878–1886 or 1922–1925", step)
        self.assertNotIn("No registres matricules were kept during the annexation.", step)

    def test_notarial_tables_cover_an_unknown_notary(self):
        rule = between(self.text, "### When the notary is not known", "### From a cadastral case")
        self.assertIn("From 1693 every notarial act had to be declared", rule)
        self.assertIn("sellers, buyers, marriage contracts, wills and others", rule)
        self.assertIn("some tables give only the registration date", rule)


class DutchRecordTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("dutch-civil-church-record-recovery.md")

    def test_an_index_miss_can_be_an_act_that_is_not_yet_public(self):
        section = between(
            self.text,
            "## When the index fails, open the ten-year tables",
            "## Once civil registration starts",
        )
        self.assertIn("birth acts become public after 100 years, marriage acts and their supplements after 75 years, and death acts after 50 years [S19]", section)

    def test_the_consent_age_follows_the_1901_majority(self):
        section = between(
            self.text,
            "## Once civil registration starts",
            "## Check separate contracts and guardian agreements",
        )
        self.assertIn("21 for 1901–1988 and 18 since 1988 [S24]", section)
        self.assertIn("So a spouse of 21 or 22 was of age after 1901", section)

    def test_the_title_no_longer_says_pre_1811(self):
        self.assertNotIn("pre-1811 church register", self.text)
        self.assertIn("# Recover Dutch civil acts and the church register kept before civil registration", self.text)


class QuebecCopyTests(unittest.TestCase):
    def test_the_drouin_folders_name_their_copy(self):
        text = recipe("french-canadian-register-recovery.md")
        section = between(
            text,
            "## Use the second copy when the parish copy fails",
            "## Search the post's own register first",
        )
        self.assertIn("The Fonds Drouin folder has the court copy.", section)
        self.assertIn("The Registres paroissiaux 1621-1876 (Parish registers 1621-1876) folder has the parish copy", section)


class BelgianAccessTests(unittest.TestCase):
    def test_belgian_death_acts_open_after_75_years(self):
        text = recipe("french-belgian-civil-act-extraction.md")
        section = between(
            text,
            "## Find Belgian register images in AGATHA",
            "## Check a Paris reconstructed-record branch",
        )
        self.assertIn("birth acts are public after 100 years and marriage and death acts after 75 years", section)
        self.assertIn("still gave 50 years for death acts when it was read on 2026-11-13 [S8]", section)


if __name__ == "__main__":
    unittest.main()
