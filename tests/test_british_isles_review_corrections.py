"""The British Isles, Canadian and convict recipes keep the corrections from the expert review in issue #93.

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


class EnglandAndWalesTests(unittest.TestCase):
    def setUp(self):
        self.gro = recipe("england-wales-gro-index-recovery.md")
        self.census = recipe("uk-census-and-1939-register-interpretation.md")

    def test_sibling_sweep_checks_the_gro_years_and_sex_rule(self):
        sweep = between(self.gro, "## Sweep for the full sibling group", "## Identify the wife")
        self.assertIn("inside the GRO online index's birth years", sweep)
        self.assertIn("For births from 1935 to 1983, sweep a copy of the quarterly index", sweep)
        self.assertIn("only from the September quarter of 1911", sweep)
        self.assertIn("GRO's guide lists sex as a required field", sweep)

    def test_gro_dash_means_not_captured(self):
        section = between(self.gro, "## Recover children registered", "## Treat a marriage page")
        self.assertIn("no maiden surname was captured for the entry", section)
        self.assertIn("GRO does not give that meaning", section)
        self.assertNotIn("generally means the mother's surname matches", self.gro)

    def test_index_copies_carry_dated_fields(self):
        copies = between(self.gro, "## Reconcile copies of one index", "## Route Isle of Man")
        for field in (
            "births from the September quarter of 1911",
            "age at death from the March quarter of 1866",
            "from the June quarter of 1969",
        ):
            self.assertIn(field, copies)
        self.assertIn("inside the GRO online index's years (step 5), rerun", copies)
        self.assertNotIn("FreeBMD and other copies may lack it", self.gro)

    def test_census_nights_are_listed(self):
        rules = between(self.census, "## Fix the year's rules", "## Retrieve the whole 1921 return")
        for night in (
            "6 June 1841",
            "30 March 1851",
            "7 April 1861",
            "2 April 1871",
            "3 April 1881",
            "5 April 1891",
            "31 March 1901",
            "2 April 1911",
        ):
            self.assertIn(night, rules)

    def test_1841_is_exempt_from_the_county_only_birthplace_check(self):
        section = between(self.census, "## Check birthplaces against the image", "## Read the 1939 Register")
        self.assertIn("This does not apply to 1841", section)

    def test_scottish_1921_census_routes_to_scotlandspeople(self):
        scotland = between(self.census, "- **Scotland.**", "- **Ireland and Northern Ireland, 1921.**")
        self.assertIn("search it on ScotlandsPeople", scotland)
        self.assertIn("6 credits (£1.50)", scotland)


class EnglishNonRegisterTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("english-nonregister-record-recovery.md")

    def test_interregnum_probate_routes_to_pcc_prob_11(self):
        probate = between(self.text, "## 2. Pre-1858 probate", "## 3. Father missing from a baptism")
        interregnum = between(probate, "**1653–1660 (Interregnum):**", "**Where to search.**")
        self.assertIn("Court for Probate of Wills and Granting Administrations", interregnum)
        self.assertIn("PCC series PROB 11", interregnum)
        self.assertIn("Prerogative Court of York records are at the Borthwick Institute", probate)

    def test_surrendered_registers_and_dr_williams_registry_are_named(self):
        dissent = between(self.text, "## 5. A label that says only", "## 6. Wales")
        self.assertIn("RG 5, the birth certificates of the Dr Williams's Library", dissent)
        self.assertIn("RG 6, the Quaker registers (1578–1841)", dissent)
        self.assertIn("It does not apply to a marriage of 1754–1837", dissent)

    def test_jurisdiction_map_points_to_its_current_address(self):
        jurisdictions = between(self.text, "## 1. Build the dated jurisdiction table", "## 2. Pre-1858 probate")
        self.assertIn("https://www.familysearch.org/en/mapp/", jurisdictions)
        self.assertNotIn("a new version released through FamilySearch Labs", self.text)

    def test_welsh_wills_are_free_at_nlw(self):
        wales = between(self.text, "## 6. Wales", "## Deliver")
        self.assertIn("free to search and view on its website", wales)


class ScotlandTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("scottish-parish-statutory-record-recovery.md")
        self.system = between(self.text, "## Choose the register system by date", "## Classify each OPR entry")

    def test_statutory_images_follow_the_closure_rule(self):
        self.assertIn("births over 100 years old, marriages over 75 and deaths over 50", self.system)
        self.assertIn("Its missing image is an access limit, not a register gap", self.system)
        self.assertIn("NRS consulted from 13 July to 4 October 2026", self.system)

    def test_death_index_maiden_surname_starts_in_1974(self):
        self.assertIn("mother's maiden surname from 1974", self.system)

    def test_kirk_session_price_is_dated(self):
        section = between(self.text, "## Follow corrections", "## Read Scottish census images")
        self.assertIn("2 credits (50p) as of 7 November 2026", section)


class IrelandTests(unittest.TestCase):
    def setUp(self):
        self.civil = recipe("irish-civil-registration-jurisdiction-recovery.md")

    def test_irishgenealogy_is_the_first_index_route(self):
        district = between(self.civil, "## 2. Identify the registration district", "## 3. Carry the index locator")
        first, commercial = district.index("Search IrishGenealogy.ie first"), district.index("Findmypast, Ancestry and FamilySearch")
        self.assertLess(first, commercial)
        self.assertIn("deaths before 1871 are index only", district)

    def test_film_route_is_a_fallback(self):
        locator = between(self.civil, "## 3. Carry the index locator", "## 4. Check where non-Catholic registers")
        self.assertIn("apply only to an entry it shows without an image", locator)
        self.assertLess(locator.index("Prefer the online image"), locator.index("Don't use the index film number"))

    def test_groni_charges_and_search_rooms_are_stated(self):
        groni = between(self.civil, "**Northern Ireland after 1921.**", "## 4. Check where non-Catholic registers")
        self.assertIn("free name search shows only how many matches exist", groni)
        self.assertIn("full entry or register image 5 credits", groni)
        self.assertIn("PRONI's search room also has GRONI terminals", groni)

    def test_nli_coverage_and_later_routes_are_stated(self):
        text = recipe("irish-catholic-parish-image-recovery.md")
        select = between(text, "## 1. Select the Catholic parish", "## 2. Use the external index")
        self.assertIn("baptism and marriage registers up to about 1880", select)
        self.assertIn("1850s–60s on the western seaboard", select)
        self.assertIn("ask the parish, which keeps the original registers", select)

    def test_tithe_books_and_rentals_are_routed(self):
        text = recipe("irish-land-valuation-occupancy-series.md")
        tithe = between(text, "## Do not read entry order as adjacency", "## Follow the same lot")
        self.assertIn("The six Northern Ireland counties' books are at PRONI (FIN/5/A)", tithe)
        self.assertIn("FamilySearch has both sets with images", tithe)
        rentals = between(text, "## Separate lease-era and sale-year layers", "## Close with a holding register")
        self.assertIn("Landed Estates Court Rentals 1850-1885", rentals)


class ConvictAndCanadaTests(unittest.TestCase):
    def setUp(self):
        self.convict = recipe("convict-transportation-record-chain.md")
        self.canada = recipe("canadian-census-interpretation.md")

    def test_ship_stage_names_ho_11_and_its_free_index(self):
        stage = between(self.convict, "4. The convict ship record", "5. The colonial arrival indent")
        self.assertIn("TNA HO 11, 1787–1870", stage)
        self.assertIn("British convict transportation registers 1787–1867", stage)

    def test_colonial_lists_tasmanian_registers_and_panopticon_are_routed(self):
        self.assertIn("TNA HO 10 (1787–1859)", self.convict)
        tasmania = between(self.convict, "**Van Diemen's Land (Tasmania), from 1803**", "**Western Australia")
        for series in ("(CON31)", "(CON33)", "(CON40)", "(CON41)"):
            self.assertIn(series, tasmania)
        courts = between(self.convict, "## Bound each court search", "## Treat the trial-to-colonist link")
        self.assertIn("search the Digital Panopticon", courts)

    def test_canadian_census_reference_dates_and_birth_fields(self):
        timing = between(self.canada, "## Check form wording and timing", "## Browse by title-card")
        for date in (
            "2 April 1871",
            "4 April 1881",
            "31 March 1901",
            "1 June 1921",
            "1 June 1931",
            "24 June 1906",
            "1 June 1916",
            "1 June 1926",
            "as of 5 April",
            "For 1911 use 1 June",
        ):
            self.assertIn(date, timing)
        self.assertIn("month and day of birth", timing)
        self.assertIn("1911 asks for month and year", timing)


class QuakerAndCatholicTests(unittest.TestCase):
    def setUp(self):
        self.quaker = recipe("quaker-meeting-record-recovery.md")

    def test_new_york_wilburite_division_starts_in_1847(self):
        branch = between(self.quaker, "For any entry dated after the Hicksite/Orthodox separation", "6. For an emigrant")
        self.assertIn("Scipio and several others split in 1847", branch)
        self.assertIn("Poplar Ridge was founded in 1853", branch)

    def test_hinshaw_abbreviations_are_decoded(self):
        decode = between(self.quaker, "## Decode the meeting code", "## Read both sexes'")
        self.assertIn("rocf = received on certificate from", decode)
        self.assertIn("mou = married out of unity", decode)
        self.assertIn('"dis mou" records a disownment for marrying out of unity, not a death', decode)

    def test_british_and_irish_origins_are_routed(self):
        origins = between(self.quaker, "6. For an emigrant from Britain or Ireland", "## Check meeting-related court")
        self.assertIn("TNA RG 6, 1578–1841", origins)
        self.assertIn("Friends Historical Library, Dublin", origins)

    def test_1917_code_kept_the_marriage_notation_duty(self):
        rule = between(recipe("catholic-sacramental-cross-notations.md"), "## Know the rule", "## Do not stop at the index")
        self.assertIn("The 1917 Code of Canon Law, in force from 19 May 1918", rule)
        self.assertIn("canons 470 §2 and 1103 §2", rule)


if __name__ == "__main__":
    unittest.main()
