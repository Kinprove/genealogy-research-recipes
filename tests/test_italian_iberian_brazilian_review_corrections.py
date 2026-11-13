"""The Italian, Spanish and Andorran, Portuguese and Brazilian recipes keep the corrections from issue #213.

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


class SpanishAndorranRoutingTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("spanish-civil-parish-record-routing.md")

    def test_andorra_has_no_civil_register_before_1997(self):
        section = between(self.text, "## 1. Fix the civil-registration period", "## 2.")
        self.assertIn("**Andorra had no civil register before 1997.**", section)
        self.assertIn("published on 14 August 1996", section)
        self.assertIn("from the 180th day after that, in February 1997", section)
        self.assertIn("their keepers may certify entries from them [S40]", section)

    def test_andorra_step_names_the_archive_and_why_years_are_missing(self):
        section = between(self.text, "## 4. For Andorra", "## 5.")
        self.assertIn("Arxiu Nacional d'Andorra [S42 @", section)
        self.assertNotIn("Arxius Nacionals d'Andorra", self.text)
        self.assertIn("with books of 1863–1870 only", section)
        self.assertIn("A year missing from it is not a lost book.", section)
        self.assertIn("(only the opening section was read)", section)

    def test_catastro_excludes_the_canaries_basque_provinces_and_navarre(self):
        section = between(self.text, "## 6. Search the Catastro de Ensenada", "## 7.")
        self.assertIn("and not for the Canary Islands, the Basque provinces or Navarre", section)
        self.assertIn("except the Canary Islands and the exempt territories, the Basque Country and Navarre [S41 @", section)

    def test_notarial_line_is_five_years_since_2023(self):
        section = between(self.text, "## 7. Search notarial protocols", "## 8.")
        self.assertIn("| Under 5 years |", section)
        self.assertIn("| 5 to 100 years |", section)
        self.assertIn("Since 9 November 2023 the Colegio's archive keeps protocols at least five years old", section)
        self.assertIn("From 1862 until 8 November 2023", section)
        self.assertIn("the Oviedo district's protocols over 25 years old", section)
        self.assertIn("its index lists that notary's grantors only", section)
        for gone in ("Treat the 25-year line as a regional statement", "Under about 25 years",
                     "such as Madrid's", "do not expect a client-name index"):
            self.assertNotIn(gone, section)

    def test_departure_side_names_the_pares_migration_search(self):
        section = between(self.text, "## 11. Search the Spanish departure side", "## Close with")
        self.assertIn("the PARES Movimientos Migratorios search takes a name", section)
        self.assertIn("the digitized books are on its ReCrea site", section)
        self.assertNotIn("searchable on its UC ReCrea platform", section)


class ItalianRegisterTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("italian-stato-civile-parish-record-recovery.md")
        self.step1 = between(self.text, "## 1. Date the civil record", "## 2.")

    def test_table_dates_the_south_rome_and_the_new_provinces(self):
        self.assertIn("| Mainland South (Kingdom of the Two Sicilies, roughly today's southern Italy), 1815 to 1865 |", self.step1)
        self.assertIn("| Comuni then in the Kingdom of Italy, from 1 January 1866 |", self.step1)
        self.assertIn("| Rome and its province, from 1 February 1871 |", self.step1)
        self.assertIn("R.D. 27 November 1870 n. 6030", self.step1)
        self.assertIn("R.D. 24 September 1923 n. 2013 extended the 1865 decree to the territories annexed", self.step1)
        self.assertIn("In Trieste the other officially recognised faiths kept their own registers [S5]", self.step1)
        self.assertNotIn("[S4]", self.text)
        self.assertNotIn("Venezia Giulia", self.step1)

    def test_custody_paragraph_follows_the_table(self):
        custody = between(self.step1, "**Find where the earlier registers are now.**", "- **Do not apply the 1865 decree")
        self.assertIn("Provincial Archive of Trento for nine comuni", custody)
        self.assertIn("1833–1941", custody)
        self.assertIn("from 1835 [S6 @", custody)
        self.assertIn("Italian consulate", custody)
        self.assertNotIn("now usually at the State Archive", self.step1)

    def test_antenati_has_no_legal_value_and_the_court_holds_the_second_original(self):
        section = between(self.text, "## 2. Search Antenati", "## 3.")
        self.assertIn("**Do not use an Antenati image as a certificate.**", section)
        self.assertIn("in particular citizenship requests [S24 @", section)
        self.assertIn("Each Stato civile register was kept in two originals.", section)
        self.assertIn("the court's second original, where the State Archive never received it", section)

    def test_supporting_file_names(self):
        section = between(self.text, "## 3. Read the marriage's supporting file", "## 4.")
        self.assertIn("processetti matrimoniali", section)
        self.assertIn("Allegati (attachments) series", section)
        self.assertIn("so the comune does not have it", section)

    def test_conscription_widening_and_centro_documentale(self):
        section = between(self.text, "## 5. Search conscription lists", "## 6.")
        rolls = between(section, "- **Search the ruoli matricolari", "- **Do not read a missing service roll")
        self.assertIn("search at least three classes either side before you log a miss", rolls)
        self.assertIn("comune of birth as well as the comune of residence at call-up", section)
        self.assertIn("**Ask the Army's Centro documentale for a service sheet not yet transferred.**", section)
        self.assertIn("the Navy, Air Force and Carabinieri keep theirs in other offices", section)

    def test_papal_sentence_names_frosinone_only(self):
        section = between(self.text, "## 6. Send each comune request", "## Close with")
        self.assertIn("In Frosinone, in the part of Lazio that was Papal until 1870", section)
        self.assertNotIn("Former Papal State territory", section)
        self.assertIn("describe each household as of 1 January 1865", section)


class BrazilMarriageRuleTests(unittest.TestCase):
    def setUp(self):
        text = recipe("brazilian-parish-civil-registry-recovery.md")
        self.section = between(text, "## 2. Send a civil entry", "## 3. Search forward")

    def test_civil_first_rule_follows_the_before_or_after_sentence(self):
        old = self.section.index("before or after the civil one [S12]")
        rule = self.section.index("**Read the marriage rules by date.**")
        self.assertLess(old, rule)
        tail = self.section[rule:]
        self.assertIn("Decree 521 of 26 June 1890", tail)
        self.assertIn("the civil marriage was always to come first", tail)
        self.assertIn("three days after the local judge published it [S49]", tail)

    def test_church_marriages_from_1889_have_a_civil_entry_and_1874_is_not_a_start(self):
        self.assertIn("whatever their religion, to have their marriage entered within three days", self.section)
        self.assertIn("For a church marriage of 1889 or early 1890, search the civil books too.", self.section)
        self.assertIn("25 April 1874, Decree 5.604 [S7], [S48]", self.section)
        self.assertIn("do not take 1874 as the start either", self.section)


class PortugalMarriageIndexTests(unittest.TestCase):
    def test_marriage_index_years_follow_the_collection_title(self):
        text = recipe("portuguese-parish-civil-register-recovery.md")
        section = between(text, "## 3. Use tombo.pt as a list of books", "## 4.")
        self.assertIn("Marriages 1670–1910 [S23 @", section)
        self.assertNotIn("Marriages 1760–1910", text)


if __name__ == "__main__":
    unittest.main()
