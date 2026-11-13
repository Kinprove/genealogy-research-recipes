"""The Scandinavian recipes keep the corrections from issue #212.

Each test pins the corrected facts inside the section where they live and, where the old wording
was wrong, checks that it is gone, so a later edit cannot quietly bring it back.
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


def from_marker(text: str, marker: str) -> str:
    """Return the part of text from marker to its end."""
    return text[text.index(marker) :]


class DanishRecordTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("scandinavian-patronymic-farm-name-record-recovery.md")

    def test_copenhagen_emigrant_registers_run_past_1934(self):
        bullet = between(self.text, "- Denmark: Rigsarkivet says the police", "- Norway:")
        self.assertIn("from 1868 to 1959", bullet)
        self.assertIn("the Copenhagen police went on keeping the emigrant registers", bullet)
        self.assertIn("run to 1952", bullet)
        self.assertIn("1953–1959", bullet)
        self.assertIn("not scanned", bullet)
        self.assertIn("[S23 @", bullet)
        self.assertNotIn("from 1868 to 1934", self.text)

    def test_levying_rolls_do_not_enrol_from_birth_after_1849(self):
        section = between(
            self.text,
            "## Denmark: go beyond the church books",
            "## Rebuild siblings and marriages from the named parents",
        )
        marker = "**Enrolment ages in the lægdsruller.**"
        self.assertLess(section.index("- Use the lægdsruller (military levying rolls)"), section.index(marker))
        note = from_marker(section, marker)
        for fact in ("0–36 for 1788–1808", "0–45 for 1808–1849", "15–38 from 1849", "19–38 from 1869",
                     "18–36 from 1912", "not entered at birth"):
            self.assertIn(fact, note)


class SwedishParishTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("scandinavian-parish-record-recovery.md")

    def test_poll_tax_ages_change_by_period_and_the_scans_are_named(self):
        section = between(
            self.text,
            "## Bridge gaps with poll-tax registers and probate",
            "## Before 1869, look for emigrants in the moving-out registers",
        )
        note = from_marker(section, "**Poll-tax ages and scans.**")
        for fact in ("held for 1652–1840", "15–63 from 1652", "17–63 from 1841", "18–60 from 1857",
                     "15–62", "1642–1820", "indexed them by parish"):
            self.assertIn(fact, note)

    def test_emigration_before_1869_names_the_summary_reports(self):
        section = between(
            self.text,
            "## Before 1869, look for emigrants in the moving-out registers",
            "## Finland: work the rippikirjat the same way",
        )
        self.assertIn("summariska folkmängdsredogörelser", section)
        self.assertIn("*Emigranter 1861–1940*", section)
        self.assertIn("only legal emigration", section)
        self.assertNotIn("recorded only in the parish moving-out registers", self.text)

    def test_finnish_russian_forms_are_scoped_to_orthodox_records(self):
        section = between(
            self.text,
            "## Finland: work the rippikirjat the same way",
            "## Close with a household chain packet",
        )
        note = from_marker(section, "**Russian forms and church-book images.**")
        for fact in ("mainly for Orthodox records", "Russian until the 1920s", "Julian calendar until 1920",
                     "Astia", "record the image as not seen"):
            self.assertIn(fact, note)


class SwedishMilitaryTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("swedish-military-record-routing.md")

    def test_army_rolls_from_1724_are_routed_for_war_years(self):
        section = between(
            self.text,
            "## 3. Work the general muster rolls as dated snapshots",
            "## 4. Before 1683 and in the Great Northern War",
        )
        note = from_marker(section, "**War years: also search *Rullor 1724–*.**")
        for fact in ("from 1724 to about 1865", "often incomplete in war years", "1808-1809"):
            self.assertIn(fact, note)

    def test_conscription_cards_are_named_by_their_archive_title(self):
        section = between(
            self.text,
            "## 2. Read a nil only against what the index actually covers",
            "## 3. Work the general muster rolls",
        )
        note = between(section, "**Conscription cards: an archive, not a database.**", "Record the index")
        self.assertIn("*Värnpliktskort. Stamkort och läkarhandlingar, avregistrerad*", note)
        self.assertIn("1888-1921", note)


class SwedishPropertyBookTests(unittest.TestCase):
    def test_lagfartsbocker_period_and_scope_come_before_step_1(self):
        text = recipe("land-index-book-series-recovery.md")
        section = between(
            text,
            "### Swedish property books: follow rooms and changed parcel identifiers",
            "### When the person used the farm or dwelling",
        )
        note = between(section, "**Check the books' period and scope first.**", "1. Establish the relevant court archive")
        for fact in ("rural properties", "about 1875 to 1933", "not complete"):
            self.assertIn(fact, note)


class WetNurseRollTests(unittest.TestCase):
    def test_the_series_is_spelled_as_the_guide_spells_it(self):
        text = recipe("illegitimacy-record-recovery.md")
        self.assertIn("*Ammrullor* D1BA (1816–1937)", text)
        self.assertNotIn("Amrullor", text)


if __name__ == "__main__":
    unittest.main()
