"""The Irish, Australian and English recipes keep the corrections from issue #214.

Each test pins a corrected rule inside the section where it lives and, where the old wording was
wrong, checks that it is gone, so a later edit cannot quietly bring it back. The last test checks
that every new or rewritten paragraph is a reviewed claim in its recipe's provenance ledger.
"""

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES = ROOT / "skills/genealogy-research-recipes/recipes"
SPEC = importlib.util.spec_from_file_location("provenance", ROOT / "scripts/provenance.py")
provenance = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(provenance)


def recipe(name: str) -> str:
    """Return a recipe's text with each run of whitespace folded to one space."""
    return " ".join((RECIPES / f"{name}.md").read_text(encoding="utf-8").split())


def between(text: str, start: str, end: str) -> str:
    """Return the part of text from start up to (not including) the next end."""
    begin = text.index(start)
    return text[begin : text.index(end, begin + len(start))]


class IrishRecipeTests(unittest.TestCase):
    def test_tithe_step_warns_that_the_nai_site_is_offline(self):
        text = recipe("irish-land-valuation-occupancy-series")
        section = between(text, "## Do not read entry order as adjacency", "## Follow the same lot")
        note = section[section.index("**The National Archives of Ireland's tithe site named in step 2 is offline.**") :]
        self.assertIn("Tithe Applotment Books, 1823–37", note)
        self.assertIn("while its genealogy microsites are offline [S14 @", note)
        self.assertLess(section.index("3. A cluster that turns up in both series"), section.index(note))

    def test_will_calendars_1858_to_1917_point_to_the_reading_room(self):
        text = recipe("irish-probate-and-deed-recovery")
        section = between(text, "- **Read the entry as an index line, not the will.**", "## 3.")
        self.assertNotIn("Take the current online location for the earlier years from the NAI page itself", text)
        self.assertIn("names no online copy of the 1858–1917 calendars yet", section)
        self.assertIn("NAI lists the will calendars for 1858–1920", section)
        self.assertIn("[S21 @", section)

    def test_pre_1858_search_adds_nai_copies_before_the_stop_rule_applies(self):
        text = recipe("irish-probate-and-deed-recovery")
        section = between(text, "- **Stop rule:**", "## 4.")
        self.assertIn("prerogative and diocesan copies of some wills, and indexes to others, for 1595–1858", section)
        self.assertIn("before the stop rule calls a pre-1858 will lost", section)

    def test_deed_indexes_and_memorials_have_a_reading_route(self):
        text = recipe("irish-probate-and-deed-recovery")
        section = between(text, "## 4. Search the Registry of Deeds", "## 5.")
        note = section[section.index("**Where to read the deed indexes and memorials.**") :]
        self.assertIn("for 1708–1929 were microfilmed", note)
        self.assertIn("published on FamilySearch", note)
        self.assertIn("by appointment, at Tailte Éireann's Henrietta Street office [S5 @", note)

    def test_surviving_1821_to_1851_census_data_is_searched_before_a_gap_is_logged(self):
        text = recipe("irish-emigrant-origin-locality")
        section = between(text, "## 3. Test each candidate", "## 4.")
        note = section[section.index("**Search the surviving 1821–1851 census data") :]
        self.assertIn("covers 1821, 1831, 1841 and 1851 [S20 @", note)


class AustralianRecipeTests(unittest.TestCase):
    def setUp(self):
        self.text = recipe("australia-nz-record-routing")

    def test_canberra_region_events_go_to_the_new_south_wales_indexes(self):
        section = between(self.text, "## 1. Send an Australian BDM search", "## 2.")
        note = section[section.index("**The Australian Capital Territory is the exception.**") :]
        self.assertIn("births in the Canberra region before 1918, and marriages and deaths there before 1930", note)
        self.assertIn("search the New South Wales indexes", note)
        self.assertIn("Queanbeyan or Yass [S1 @", note)

    def test_western_australian_lists_after_1900_go_to_the_naa(self):
        section = between(self.text, "## 7. Route passenger lists", "## 8.")
        note = section[section.index("**Western Australian passenger lists after 1900 are the exception.**") :]
        self.assertIn("generally held by the WA Branch of the National Archives of Australia [S32 @", note)
        self.assertIn("the before-1924 rule above does not apply there", note)
        self.assertLess(section.index("- **Before 1924, search the archive"), section.index(note))


class EnglishRecipeTests(unittest.TestCase):
    def test_dr_williams_registry_is_not_limited_to_london_families(self):
        text = recipe("english-nonregister-record-recovery")
        section = between(text, "5. **Do not treat TNA as the home of every chapel register.**", "## 6.")
        note = section[section.index("**Dr Williams's Library registry was not only for London families.**") :]
        self.assertIn("parents from most parts of the British Isles, and even from abroad, also used it [S13]", note)
        self.assertIn("the registry's total, not a count of London families [S13]", note)
        self.assertIn("wherever the family lived", note)

    def test_isle_of_man_civil_registers_are_routed_to_douglas_behind_the_privacy_gate(self):
        text = recipe("england-wales-gro-index-recovery")
        section = between(text, "## Route Isle of Man and Channel Islands events", "## Order the certificate")
        note = section[section.index("**Isle of Man civil registers from 1878 are with the Civil Registry in Douglas.**") :]
        self.assertIn("The National Archives names the Douglas Civil Registry Office", note)
        self.assertIn("[S28 @", note)
        self.assertIn("answer the privacy gate in `SKILL.md` before you ask the Douglas office for one", note)

    def test_irish_convicts_have_a_national_archives_of_ireland_route(self):
        text = recipe("convict-transportation-record-chain")
        section = between(text, "8. A permission to marry", "Between these stages")
        self.assertIn("Transportation Registers (Ireland to Australia), 1836–1857", section)
        self.assertIn("Convict Reference Files, 1836–1856 and 1865–1868 [S12 @", section)


class LedgerRegistrationTests(unittest.TestCase):
    EXPECTED = {
        "irish-land-valuation-occupancy-series": [
            ("**The National Archives of Ireland's tithe site", "portal-availability", ["S14"]),
        ],
        "irish-probate-and-deed-recovery": [
            ("- **Read the entry as an index line, not the will.**", "portal-availability", ["S2", "S21", "S3", "S4"]),
            ("**Add NAI's own pre-1858 copies to the search.**", "portal-availability", ["S21"]),
            ("**Where to read the deed indexes and memorials.**", "portal-availability", ["S5"]),
        ],
        "australia-nz-record-routing": [
            ("**The Australian Capital Territory is the exception.**", "custody", ["S1"]),
            ("**Western Australian passenger lists after 1900", "custody", ["S32"]),
        ],
        "irish-emigrant-origin-locality": [
            ("**Search the surviving 1821–1851 census data", "portal-availability", ["S20"]),
        ],
        "english-nonregister-record-recovery": [
            ("**Dr Williams's Library registry was not only for London families.**", "historical", ["S13"]),
        ],
        "england-wales-gro-index-recovery": [
            ("**Isle of Man civil registers from 1878", "custody", ["S28"]),
        ],
        "convict-transportation-record-chain": [
            ("**For a convict tried in Ireland,", "portal-availability", ["S12"]),
        ],
    }

    def test_each_correction_is_a_reviewed_claim_with_its_sources(self):
        for slug, rows in self.EXPECTED.items():
            ledger = provenance.parse_ledger((ROOT / "provenance" / f"{slug}.yml").read_text(encoding="utf-8"))
            for prefix, kind, sources in rows:
                with self.subTest(slug=slug, block=prefix):
                    claims = [c for c in ledger["claims"] if c["anchor"].startswith(prefix)]
                    self.assertEqual(len(claims), 1)
                    self.assertEqual(claims[0]["review"], "reviewed")
                    self.assertEqual(claims[0]["kind"], kind)
                    self.assertEqual(sorted(claims[0]["sources"]), sources)


if __name__ == "__main__":
    unittest.main()
