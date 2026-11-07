"""The U.S. records recipes keep the corrections from the expert review in issue #92.

Each test pins a fact that was wrong in a draft of the fix and the corrected fact
that replaced it, so a later edit cannot quietly bring the wrong one back.
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


class UsRecordsReviewCorrectionsTests(unittest.TestCase):
    def test_bankruptcy_files_route_to_kansas_city_and_acts_are_dated(self):
        text = recipe("us-federal-court-case-file-recovery.md")
        self.assertIn("all bankruptcy case files are at the National Archives at Kansas City", text)
        self.assertIn("Frankfort, Kentucky", text)
        for period in (
            "from 1800 to 1803",
            "from 1842 to 1843",
            "from 1867 to 1878",
            "continuously from 1898",
        ):
            self.assertIn(period, text)
        self.assertNotIn("remain in Record Group 21 at the regional NARA facility", text)

    def test_pension_fees_match_each_copy_product(self):
        text = recipe("us-military-pension-file-recovery.md")
        self.assertIn("complete pension application file, pre-Civil War: $55", text)
        self.assertIn(
            "complete pension application file, Civil War and later: $80 for up to 100 pages",
            text,
        )
        self.assertIn("Pension Documents Packet: $30", text)
        self.assertNotIn("Pension Documents Packet:** $55", text)

    def test_pension_index_table_gives_t289_its_span(self):
        text = recipe("us-military-pension-file-recovery.md")
        self.assertIn("| Service between 1861 and 1900 | T289", text)
        self.assertNotIn("1861–1917", text)

    def test_civil_war_navy_route_uses_civil_war_pension_indexes(self):
        text = recipe("us-civil-war-service-record-episodes.md")
        navy = between(text, "**Route Navy men elsewhere.**", " - **")
        for series in ("M1953", "T288", "T289", "M1279"):
            self.assertIn(series, navy)
        for series in ("T316", "T318"):
            self.assertNotIn(series, navy)

    def test_civil_war_carding_and_confederate_dates(self):
        text = recipe("us-civil-war-service-record-episodes.md")
        self.assertIn("carded medical records from 1887", text)
        self.assertIn("began compiling them in 1903", text)
        self.assertIn("M253", text)
        self.assertNotIn("Confederate volunteer service records throughout the 1890s", text)

    def test_1885_census_locators_and_dakota_custody(self):
        text = recipe("us-census-practical-workflows.md")
        self.assertIn("New Mexico Territory (M846)", text)
        self.assertNotIn("M1304", text)
        self.assertIn("Dakota Territory's schedules were never transferred to NARA", text)

    def test_marriage_search_keeps_civil_records_before_licensing(self):
        text = recipe("missing-marriage-jurisdiction-search.md")
        self.assertIn("July 1860 to December 1885", text)
        self.assertIn("issued by city and town clerks, not counties", text)
        self.assertIn("not instead of them", text)
        self.assertNotIn("courthouse searches will fail", text)
        self.assertNotIn("instead of civil courthouses", text)

    def test_persi_hosting_agrees_across_recipes(self):
        for name in ("missing-marriage-jurisdiction-search.md", "periodical-index-search-retrieval.md"):
            with self.subTest(recipe=name):
                text = recipe(name)
                self.assertIn("ACPL staff compile PERSI, and this copy is the larger one", text)
                self.assertIn("with fewer entries but images of some articles", text)
                self.assertNotIn("frozen", text)
                self.assertNotIn("partnership ended", text)
                self.assertNotIn("the move from Findmypast is complete", text)

    def test_uscis_route_drops_ar2_and_gives_current_fees(self):
        text = recipe("usa-immigration-search-recovery.md")
        route = between(
            text,
            "### 11. Route federal records by type and actual custody",
            "Alongside an A-file lead",
        )
        self.assertIn("17 May 2024", route)
        self.assertNotIn("7.5 million", route)
        uscis = route[route.index("4. For C-Files") :]
        self.assertIn("$30 online or $80 on paper", uscis)
        self.assertNotIn("AR-2", uscis)

    def test_church_custody_corrections(self):
        text = recipe("us-church-record-custody.md")
        self.assertIn("Concordia Historical Institute in St. Louis", text)
        self.assertIn("Brady says many Catholic churches did not record burials", text)
        self.assertIn("Second Plenary Council of Baltimore (1866)", text)
        self.assertIn("does not hold local church membership, baptism or marriage registers", text)

    def test_wwii_military_routes(self):
        text = recipe("us-20th-century-military-service-reconstruction.md")
        self.assertIn("vetrecs.archives.gov", text)
        self.assertIn("whatever his surname", text)
        self.assertNotIn("usarmy.knox.hrc.mbx.foia@army.mil", text)
        self.assertNotIn("Surnames A–L (and any unaccessioned files) remain", text)
        self.assertIn("31 July 1927", text)
        self.assertNotIn("1897–1928", text)
        self.assertNotIn("As of February 2025", text)

    def test_freedmens_bureau_microfilm_and_bank_index(self):
        text = recipe("us-freedpeople-record-recovery.md")
        self.assertIn("M1900–M1913, one for each state or district", text)
        self.assertNotIn("assistant commissioners and superintendents in NARA microfilm publications", text)
        self.assertIn("(M817)", text)

    def test_land_recipe_checks_public_land_state_first(self):
        text = recipe("us-federal-land-entry-file-recovery.md")
        self.assertIn("The 30 public-land states", text)
        self.assertIn("The 20 state-land states", text)
        self.assertIn("Congressional Reservation Line", text)
        self.assertNotIn("category error", text)


if __name__ == "__main__":
    unittest.main()
