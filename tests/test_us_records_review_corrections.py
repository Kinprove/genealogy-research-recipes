"""The U.S. records recipes keep the corrections from the expert reviews in issues #92 and #216.

Each test pins corrected facts and, where a draft of the fix had them wrong, checks
that the wrong wording is gone, so a later edit cannot quietly bring it back.
"""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES = ROOT / "skills/genealogy-research-recipes/recipes"


def folded(path: Path) -> str:
    """Return a file's text with each run of whitespace folded to one space."""
    return " ".join(path.read_text(encoding="utf-8").split())


def recipe(name: str) -> str:
    """Return a recipe's text with each run of whitespace folded to one space."""
    return folded(RECIPES / name)


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
        self.assertNotIn("Pension Documents Packet:** $55", text)  # the draft's bold label

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
        c_files_step = between(text, "4. For C-Files", "Alongside an A-file lead")
        self.assertIn("$30 online or $80 on paper", c_files_step)
        self.assertNotIn("AR-2", c_files_step)

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


class UsRecordsIssue216CorrectionsTests(unittest.TestCase):
    """Corrections from the 1.15.0 review of the U.S. recipes in issue #216."""

    def test_a_later_act_can_free_people_born_before_the_cutoff(self):
        text = recipe("us-freedpeople-record-recovery.md")
        item = between(text, "**Other gradual-abolition states.**", "**A free woman heading")
        self.assertIn('"Held for life" means only that the state\'s first act did not free', item)
        self.assertIn(
            "legislation enacted in 1817 freed the remaining enslaved people in 1827 [S57]", item
        )

    def test_manhattan_search_for_the_bronx_starts_at_annexation(self):
        text = recipe("us-vital-registration-coverage.md")
        self.assertIn(
            "search the Manhattan records only for events from the date of annexation through 1897",
            text,
        )
        for town in (
            "Flatbush, 1847–1851 and 1880–1894",
            "Flatlands, 1880–1895",
            "Gravesend, 1880–1894",
            "New Lots, 1881–1886",
            "New Utrecht, 1880–1894",
        ):
            self.assertIn(town, text)

    def test_widows_thirds_include_her_share_of_personal_estate(self):
        text = recipe("us-period-law-record-reading.md")
        row = between(text, "| `widow's thirds` |", "| `Court of Ordinary` |")
        self.assertIn("In an intestate's personal estate", row)
        self.assertIn('"one third shall go to the widow of the intestate" [S131]', row)
        self.assertNotIn("| A share she owned outright |", text)

    def test_a_judge_directory_miss_does_not_rule_out_a_territorial_judge(self):
        text = recipe("us-federal-court-case-file-recovery.md")
        item = between(text, "**A lead that names a judge but no court:**", "For a matter before 1912")
        self.assertIn("lists only judges of the Article III courts and some former federal courts", item)
        self.assertIn("a judge who sat only on a territorial court is not listed", item)

    def test_federal_pardons_before_1853_have_a_route(self):
        text = recipe("criminal-court-prison-record-recovery.md")
        paragraph = between(
            text, "**Federal pardons outside RG 204's case files:**", "## Inventory surviving series"
        )
        for words in ("pardon files, 1789–1893, in RG 59", "1793–1853", "are in RG 94"):
            self.assertIn(words, paragraph)

    def test_ohio_names_the_western_reserve_and_firelands(self):
        text = recipe("us-federal-land-entry-file-recovery.md")
        paragraph = between(text, "A further caution for Ohio:", "## 1. Route the entry by authority")
        for words in ("Connecticut Western Reserve", "the Firelands", "Connecticut State Library"):
            self.assertIn(words, paragraph)

    def test_abmc_covers_korea_vietnam_and_three_more_cemeteries(self):
        text = recipe("burial-evidence-packet.md")
        paragraph = between(text, "ABMC covers more than", "On a Soviet WWII mass grave")
        for words in (
            "Korean War",
            "Vietnam War",
            "Mexico City National Cemetery",
            "Corozal American Cemetery",
            "Clark Veterans Cemetery",
        ):
            self.assertIn(words, paragraph)

    def test_a_missing_dagger_is_not_an_access_record(self):
        text = folded(ROOT / "skills/genealogy-research-recipes/SKILL.md")
        self.assertIn("take access limits from the sidecar entry, not from a missing dagger", text)

    def test_navy_veterans_own_pensions_route_to_m1469(self):
        pension = recipe("us-military-pension-file-recovery.md")
        self.assertIn("| Navy veterans, approved claims, 1861–1910 | M1469", pension)
        self.assertIn("For a Navy veteran's own approved claim, use M1469", pension)
        civil_war = recipe("us-civil-war-service-record-episodes.md")
        coverage = between(civil_war, "## Check database coverage", "## Return the episode packet")
        self.assertIn("NARA M1469", coverage)


if __name__ == "__main__":
    unittest.main()
