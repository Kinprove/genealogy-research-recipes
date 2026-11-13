"""Pin the corrections from the 1.15.0 review of the German, Austrian, Czech and Hungarian recipes (issue #215).

Each test pins a corrected rule and the action it asks for inside the section where it lives and,
where the rule qualifies an older one, its place beside that rule, so a later edit cannot quietly
drop it or move it away.
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


class HistoricHungaryTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("historic-hungary-record-routing.md")
        self.custody = between(
            self.text,
            "## 3. Take custody from the successor state, not from Budapest",
            "## 4. Search both name orders",
        )

    def test_burgenland_state_registers_run_on_after_1921(self):
        section = between(self.text, "## 2. Choose civil or church books by date and territory", "## 3. Take custody")
        start = section.index("**In Burgenland, expect state civil registers after 1921 as well.**")
        rule = section[start:]
        self.assertIn("stayed in force there as special federal law", rule)
        self.assertIn("took the state registrars over as registry officials [S19]", rule)
        self.assertIn("do not stop a Burgenland search for a state register at 1921", rule)
        self.assertLess(section.index("- **Do not carry Austria's dates into Burgenland.**"), start)

    def test_holders_inside_todays_hungary_come_before_the_budapest_rule(self):
        note = between(
            self.custody,
            "**Inside today's Hungary, three holders share the registers.**",
            "- **Start with the archive of the state the village lies in today",
        )
        self.assertIn("Before 1895 the parishes kept them", note)
        self.assertIn("filmed them from 1960 to mid-1970 [S20 @", note)
        self.assertIn("Act XXIII of 1827", note)
        self.assertIn("from 1895 to 1980, and the archives keep the second copies [S21 @", note)
        self.assertIn('read "the MNL in Budapest" in the first rule below', note)
        self.assertIn("look in the county archive for a second copy", note)

    def test_a_split_county_archive_in_hungary_can_hold_a_village_now_abroad(self):
        start = self.custody.index(
            "**For a village now outside Hungary whose 1895 county the new border split, "
            "also check that county's archive in Hungary.**"
        )
        rule = self.custody[start:]
        self.assertIn("second copies of the state registers of 1895–1921", rule)
        self.assertIn("annexed to Austria in 1921 [S22 @", rule)
        self.assertIn("Look for the same kind of holding in another border county's archive", rule)
        self.assertLess(self.custody.index("- **For Croatia, Vojvodina, Transcarpathia and Burgenland"), start)


class AustrianRegisterTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("austrian-confessional-register-routing.md")
        self.law = between(
            self.text,
            "## 1. Fix which register the law used on the event date (present-day Austria)",
            "## 2. In Vienna, fix the address before choosing the parish",
        )

    def test_burgenland_is_sent_to_state_registers_and_the_hungary_recipe(self):
        note = between(self.law, "This step does not cover Burgenland", "- **Before the cutover")
        self.assertIn("Burgenland kept Hungary's state civil registers after 1921", note)
        self.assertIn("[S35]", note)
        self.assertIn(
            "Route a Burgenland event from before the 1938–1939 cutover with "
            "[historic Hungary record routing](historic-hungary-record-routing.md)",
            note,
        )

    def test_military_registers_are_with_the_state_archives(self):
        start = self.law.index("**Route a pre-1938 military-register entry to the Austrian State Archives.**")
        rule = between(self.law[start:], "**Route", "**Date a register's legal standing by confession.**")
        self.assertIn("Section 62(2) of the Personenstandsgesetz 2013", rule)
        self.assertIn("(Militär-Matriken, Heeres-Matriken) kept before 1 August 1938", rule)
        self.assertIn("to the Austrian State Archives (Österreichisches Staatsarchiv) [S37 @", rule)
        self.assertIn("is held there, not by a parish or a registry office", rule)
        self.assertLess(self.law.index("- **Search the old books at their holders"), start)

    def test_register_standing_is_dated_by_confession(self):
        rule = self.law[self.law.index("**Date a register's legal standing by confession.**") :]
        self.assertIn("allowed registers from 1782, at first without public standing", rule)
        self.assertIn("independent registers from 1830", rule)
        self.assertIn("declared legally valid in 1849", rule)
        self.assertIn("patent of 20 February 1784", rule)
        self.assertIn("legal evidentiary force in 1868 [S13]", rule)
        self.assertIn("For a Protestant event before 1830, check the Catholic parish as well.", rule)

    def test_the_protestant_convert_index_is_the_third_work(self):
        section = between(
            self.text,
            "## 4. Search a Viennese withdrawal from Judaism in both communities",
            "## 5. In the Czech lands, route by the regional archive",
        )
        note = between(section, "A third work indexes baptisms into the Protestant churches", "Do not merge")
        self.assertIn("*Jüdisch-protestantische Konvertiten in Wien 1782–1914* (Peter Lang, 2004)", note)
        self.assertIn("about 6,000 Jews who became Protestant in Vienna", note)
        self.assertIn("[S36]", note)
        self.assertIn("Do not merge the three works into one range or count.", section)
        self.assertIn("search all three works and the parish adult baptisms", section)
        self.assertNotIn("the two works", section)
        self.assertNotIn("both works", section)

    def test_moravia_and_silesia_have_their_own_cadastres(self):
        start = self.text.index("- **In Moravia and Silesia, use their own cadastres")
        rule = between(self.text[start:], "- **In Moravia", "- **To link generations, read the land books.**")
        self.assertIn("the 1651 list and the tax roll are Bohemian sources", rule)
        self.assertIn("not every Bohemian region has a surviving 1651 list", rule)
        self.assertIn("the so-called second lánové rejstříky", rule)
        self.assertIn("Carolingian cadastre of 1721–1729, revised 1733–1739 [S29]", rule)
        self.assertIn("Inside Bohemia, check that the 1651 list survives for the region", rule)
        self.assertIn("none survive in the central fond for the Slaný, Prácheň and Litoměřice regions", rule)
        self.assertIn("A miss for a region without lists says nothing.", rule)
        self.assertLess(self.text.index("- **Before the registers, use the 1651 list and the 1654 tax roll.**"), start)


class GermanMilitaryTests(unittest.TestCase):
    def test_hospital_book_enquiries_go_to_berlin_tegel(self):
        text = recipe("german-military-record-period-routing.md")
        note = between(text, "The surviving books of the Krankenbuchlager Berlin", "1. Give the archive")
        self.assertIn("Since 1 September 2025 its Abteilung Deutsches Reich in Berlin-Tegel", note)
        self.assertIn("the Prussian army's hospital books (PH 22-II) among them, move there from Freiburg [S21 @", note)
        self.assertIn("Address a hospital-book enquiry to the Abteilung Deutsches Reich, not to the Abteilung PA", note)
        self.assertIn("brought together at the Krankenbuchlager Berlin in 1964", note)
        self.assertNotIn("are in the Bundesarchiv (Abteilung PA)", text)


class GermanCensusTests(unittest.TestCase):
    def setUp(self):
        text = recipe("german-local-census-registration-recovery.md")
        self.section = between(text, "## Write locally, in order", "In each letter:")

    def test_the_danish_database_is_being_phased_out(self):
        note = between(self.section, "**For step 3's Danish database:**", "**For Mecklenburg-Schwerin after 1864")
        self.assertIn("the Danish Demographic Database (ddd.dda.dk) is being phased out", note)
        self.assertIn("Search the Collections (Søg i Samlingerne)", note)
        self.assertIn("[S10 @", note)
        self.assertIn("a dataset may not yet be in Search the Collections", note)
        self.assertIn("Record a NIL only for a completed search of a dataset you have confirmed is there", note)
        self.assertIn("log an interrupted search, not a NIL", note)
        self.assertNotIn("has also failed or returned nothing", note)
        self.assertLess(self.section.index("4. **Towns now in Poland or France"), self.section.index(note))

    def test_mecklenburg_schwerin_censuses_are_dated_to_the_2012_post(self):
        note = self.section[self.section.index("**For Mecklenburg-Schwerin after 1864") :]
        self.assertIn("for 1867, 1890 and 1900", note)
        self.assertIn("none then for 1867, which had to be browsed by town [S11]", note)
        self.assertIn("not a statement of present coverage; check each collection as it is now", note)


class AncestryProofTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("nazi-era-ancestry-proof-records.md")

    def test_federal_periods_are_not_carried_to_a_state_archive(self):
        section = between(
            self.text,
            "## 7. Compute the protection period before you ask",
            "## 8. Treat the regime's card indexes and films",
        )
        start = section.index("**The three periods above are federal and bind the Bundesarchiv.**")
        note = section[start:]
        self.assertIn("A state archive applies its own state's archive law", note)
        self.assertIn("[S42]", note)
        self.assertIn("Do not apply the federal periods in another state's archive without reading that state's law.", note)
        self.assertLess(section.index("- **Ask for earlier access on the law's two routes.**"), start)

    def test_jewish_community_registers_went_to_leipzig_in_2010(self):
        section = between(self.text, "## 8. Treat the regime's card indexes and films", "## Close with a proof packet")
        start = section.index(
            "**For a Jewish community register from central or eastern Germany, look for the original in Leipzig.**"
        )
        note = section[start:]
        self.assertIn("to Leipzig in 2010", note)
        self.assertIn("accessible in the Staatsarchiv Leipzig today [S1 @", note)
        self.assertLess(section.index("- **Read a separate card series as the indexers' reporting task.**"), start)


if __name__ == "__main__":
    unittest.main()
