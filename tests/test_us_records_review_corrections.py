"""Regression tests verifying corrections for U.S. records recipes per expert review (Issue #92)."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES = ROOT / "skills/genealogy-research-recipes/recipes"


class UsRecordsReviewCorrectionsTests(unittest.TestCase):
    def _read_recipe(self, filename: str) -> str:
        recipe_path = RECIPES / filename
        self.assertTrue(recipe_path.exists(), f"Recipe file not found: {recipe_path}")
        return recipe_path.read_text(encoding="utf-8")

    def test_court_case_file_recovery_bankruptcy_and_acts(self):
        content = self._read_recipe("us-federal-court-case-file-recovery.md")
        # Item 1: Kansas City modern consolidation vs regional RG 21 custody
        self.assertIn("Kansas City", content)
        self.assertIn("RG 21", content)
        # Item 6: Four federal bankruptcy acts
        self.assertIn("1800", content)
        self.assertIn("1841", content)
        self.assertIn("1867", content)
        self.assertIn("1898", content)

    def test_military_service_reconstruction(self):
        content = self._read_recipe("us-20th-century-military-service-reconstruction.md")
        # Item 2: IDPF split custody (M-Z at NARA St. Louis, A-L at Army HRC Fort Knox)
        self.assertIn("vetrecs.archives.gov", content)
        self.assertIn("Fort Knox", content)
        self.assertIn("Human Resources Command", content)
        # Surnames M-Z vs A-L
        self.assertTrue(re.search(r"M[–\-]Z", content))
        self.assertTrue(re.search(r"A[–\-]L", content))
        # Item 10: AAD Army Enlistment records ~9M serial numbers & Selective Service
        self.assertIn("serial", content.lower())
        self.assertTrue("Selective Service" in content or "draft" in content.lower())
        # Item 18: morning reports - check catalog first without hardcoded stale Feb 2025 boundary
        self.assertNotIn("As of February 2025", content)

    def test_civil_war_service_records_carding_and_navy_confederate(self):
        content = self._read_recipe("us-civil-war-service-record-episodes.md")
        # Item 3: Ainsworth carding began in 1887 (medical records) in Surgeon General's Office
        self.assertIn("1887", content)
        self.assertIn("Surgeon General", content)
        # Item 13: Navy enlistment (M1953) and Confederate CMSRs (M253)
        self.assertIn("M1953", content)
        self.assertIn("M253", content)

    def test_church_records_concordia_quakers_and_catholic_burials(self):
        content = self._read_recipe("us-church-record-custody.md")
        # Item 12: Concordia Historical Institute (LCMS)
        self.assertIn("Concordia Historical Institute", content)
        self.assertIn("Missouri Synod", content)
        # Item 11: Society of Friends / Quakers and Methodist / Episcopal
        self.assertIn("Friends", content)
        self.assertIn("Swarthmore", content)
        self.assertIn("Methodist", content)
        self.assertIn("Episcopal", content)
        # Item 4: Catholic burial registration mandatory under canon law / Baltimore councils
        self.assertIn("Liber Defunctorum", content)
        self.assertIn("Baltimore", content)

    def test_missing_marriage_civil_registration_mandates_and_persi(self):
        content = self._read_recipe("missing-marriage-jurisdiction-search.md")
        # Item 5: Mandatory civil marriage dates (Pennsylvania 1885, New York 1907/1908, South Carolina 1911)
        self.assertIn("1885", content)
        self.assertIn("Pennsylvania", content)
        self.assertTrue("1907" in content or "1908" in content)
        self.assertTrue("1911" in content)
        # Item 19: PERSI hosted by ACPL, Findmypast frozen
        self.assertIn("Allen County Public Library", content)
        self.assertIn("2021", content)

    def test_periodical_index_persi_acpl_authoritative(self):
        content = self._read_recipe("periodical-index-search-retrieval.md")
        # Item 19: ACPL sole official home, Findmypast ended in 2021
        self.assertIn("Allen County Public Library", content)
        self.assertIn("2021", content)

    def test_federal_land_entry_public_land_vs_state_land(self):
        content = self._read_recipe("us-federal-land-entry-file-recovery.md")
        # Item 7: Step 0: Confirm public-land state vs state-land state
        self.assertIn("public-land state", content.lower())
        self.assertIn("state-land state", content.lower())
        self.assertTrue(re.search(r"30\s+[Pp]ublic", content))
        self.assertTrue(re.search(r"20\s+[Ss]tate", content))

    def test_freedpeople_freedmens_bureau_and_freedmans_bank(self):
        content = self._read_recipe("us-freedpeople-record-recovery.md")
        # Item 8: Freedmen's Bureau access on FamilySearch (M1900-M1913, M1875) & Freedman's Bank (M816)
        self.assertIn("M1900", content)
        self.assertIn("M816", content)
        self.assertIn("FamilySearch", content)

    def test_pension_file_recovery_indexes_and_natf_fees(self):
        content = self._read_recipe("us-military-pension-file-recovery.md")
        # Item 9: T288 vs T289, M804, and NATF fee structure
        self.assertIn("T288", content)
        self.assertIn("T289", content)
        self.assertIn("M804", content)
        self.assertIn("NATF 85", content)
        self.assertTrue("$80" in content or "80" in content)
        self.assertTrue("$55" in content or "55" in content)

    def test_census_1885_territorial_schedules(self):
        content = self._read_recipe("us-census-practical-workflows.md")
        # Item 14: 1885 federal-state cooperative censuses (Colorado, Florida, Nebraska, New Mexico, Dakota)
        self.assertIn("1885", content)
        self.assertIn("Colorado", content)
        self.assertIn("Florida", content)
        self.assertIn("Nebraska", content)
        self.assertIn("Dakota", content)
        self.assertTrue(re.search(r"M158|M352", content))

    def test_immigration_a_files_and_uscis_fees(self):
        content = self._read_recipe("usa-immigration-search-recovery.md")
        # Item 16: A-Files custody at Kansas City and San Francisco (San Bruno)
        self.assertIn("Kansas City", content)
        self.assertTrue("San Francisco" in content or "San Bruno" in content)
        # Item 17: USCIS April 1, 2024 fee rule ($30 online index search Form G-1041 / G-1055)
        self.assertIn("2024", content)
        self.assertTrue("$30" in content or "30" in content)
        fold_content = re.sub(r"\s+", " ", content)
        self.assertIn("no additional", fold_content.lower())


if __name__ == "__main__":
    unittest.main()
