"""The Russian Empire and USSR recipes keep the corrections from the review in issue #220.

Each test pins a corrected fact in its passage. Where a passage had wording that a source read
later did not support, or a hedge that the read source lifted, the test also checks that the old
wording is gone from that passage, so a later edit cannot quietly bring it back.
"""

import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / "skills/genealogy-research-recipes"


def text(folder: str, slug: str) -> str:
    """Return a recipe or sources file with each run of whitespace folded to one space."""
    return " ".join((SKILL / folder / f"{slug}.md").read_text(encoding="utf-8").split())


def between(value: str, start: str, end: str) -> str:
    """Return the part of value from start up to (not including) the next end."""
    begin = value.index(start)
    return value[begin : value.index(end, begin + len(start))]


class RussianEmpireUssrReviewTests(unittest.TestCase):
    def test_old_believer_registers_name_the_guberniya_board(self):
        step = between(text("recipes", "old-believer-sectarian-record-recovery"),
                       "## 3. From 1874", "## 4.")
        self.assertIn("to the guberniya board (губернское правление) to be revised and kept", step)
        self.assertIn("chancellery. [S6]", step)
        self.assertIn("apparently in a single copy. [S7]", step)
        self.assertIn("in the fond of the body that kept it, usually the guberniya board, as well as in the police fonds", step)
        self.assertIn("In the Baltic guberniyas the uezd chiefs and the police chiefs revised and kept them", step)

    def test_emigrant_search_examples_say_what_their_sources_show(self):
        recipe = text("recipes", "russian-empire-emigrant-origin-recovery")
        spouse = between(recipe, "2. Search a spouse, child or documented fellow traveler", "3. If the database")
        self.assertIn("under the spelling Lewender for Lavender, found the passenger list", spouse)
        self.assertNotIn("recovered the family list through a child's alternative spelling", spouse)
        index = between(recipe, "4. Try another index of the same collection", "5. If the arrival record")
        self.assertIn("family members listed pages apart on one manifest", index)

    def test_hamburg_lists_cover_indirect_passengers_and_a_complete_index(self):
        step = between(text("recipes", "russian-empire-emigrant-origin-recovery"),
                       "5. If the arrival record or a family account names Hamburg", "For a Canadian route")
        self.assertIn("or the arrival record names an English, French, Belgian or Dutch port", step)
        self.assertIn("From 1870 to 1892 one third or more of the passengers went the indirect way", step)
        self.assertIn("its index covers 1850–1914 and 1920–1934 and is complete for those years", step)
        self.assertNotIn("partial index", step)

    def test_bashkir_agreement_names_all_its_uezds(self):
        recipe = text("recipes", "russian-revision-list-household-chaining")
        paragraph = between(recipe, "Conversely, the agreement of 20 March 1919", "## 8.")
        self.assertIn("volosts of eleven uezds: Orenburg, Orsk, Verkhneuralsk, Troitsk, Chelyabinsk, Shadrinsk, "
                      "Ekaterinburg, Krasnoufimsk, Zlatoust, Ufa and Sterlitamak, and one volost of Buzuluk uezd. [S46]",
                      paragraph)
        self.assertIn("belonged to Perm guberniya. [S56]", paragraph)
        # The 1919 sentence is its own paragraph, so the custody claim keeps its 2026-11-08 check.
        raw = (SKILL / "recipes/russian-revision-list-household-chaining.md").read_text(encoding="utf-8")
        self.assertIn("means the Bashkortostan archive.\n\nConversely, the agreement of 20 March 1919", raw)

    def test_icrc_coverage_comes_from_the_read_faq(self):
        paragraph = between(text("recipes", "russian-military-repression-record-episodes"),
                            "For a WWI prisoner taken", "A miss there is not a negative either.")
        self.assertIn("mainly from the Western Front, Romania and Serbia", paragraph)
        self.assertIn("collected by the Danish Red Cross in Copenhagen", paragraph)
        self.assertIn("[H19 @2026-11-12]", paragraph)
        self.assertNotIn("was not read", paragraph)
        self.assertNotIn("search-engine extract", paragraph)

    def test_deportation_start_date_is_no_longer_hedged(self):
        recipe = text("recipes", "chechen-ingush-1944-deportation-records")
        gather = between(recipe, "- each event's date", "- the home village")
        units = between(recipe, "**Until 7 March 1944:**", "**7–22 March 1944:**")
        for passage in (gather, units):
            self.assertIn("23 February 1944 [S5], [S6]", passage)
            self.assertNotIn("not read", passage)
            self.assertNotIn("search-result", passage.lower())
        self.assertIn("of the RSFSR [S3], formed by decree of 22 March 1944 [S24]", recipe)

    def test_balti_seat_comes_from_the_read_entry(self):
        recipe = text("recipes", "bessarabia-moldova-record-routing")
        passage = between(recipe, "**Read Ясский уезд", "**For the south in 1856–1878")
        self.assertIn("Bălți had been its uezd town since the Bessarabian oblast was formed in 1818 [S5]", passage)
        self.assertNotIn("could not be read", passage)
        self.assertIn("divided into цинуты (ținuturi)", recipe)
        self.assertIn("Romanian rule ended on 25 August 1944 [S4]", recipe)

    def test_redirect_title_is_marked_as_the_same_source(self):
        sources = text("sources", "russian-household-list-transcription-audit")
        entry = between(sources, "- **S24:**", "- **S25:**")
        self.assertIn("redirect to the S13 article «Исповедная роспись»", entry)
        self.assertIn("S24 and S13 are one source, not two", entry)

    def test_confession_lists_name_the_1722_acts_and_include_women(self):
        recipe = text("recipes", "russian-orthodox-confession-list-reading")
        early = between(recipe, "**Before 1737, expect a simpler list.**", "**Early lists can leave out children.**")
        self.assertIn("A Synod order of 28 February 1722", early)
        self.assertIn("reissued it jointly on 16 July 1722", early)
        self.assertIn("A separate Synod decree of 7 March 1722", early)
        self.assertNotIn("Guides date that decree differently", early)
        sources = between(recipe, "**Know what each source can add.**", "**Bridge the gap between revisions.**")
        self.assertIn("the 1722 orders already required books of both sexes", sources)
        self.assertNotIn("women from 1737", sources)

    def test_read_sources_no_longer_say_they_were_only_seen_in_extracts(self):
        h19 = between(text("sources", "russian-military-repression-record-episodes"), "- **H19:**", "- **H20:**")
        self.assertIn("the PDF was opened and read in full on 2026-11-12", h19)
        chechen = text("sources", "chechen-ingush-1944-deportation-records")
        for start, end in (("- **S5:**", "- **S6:**"), ("- **S6:**", "- **S7:**")):
            self.assertIn("read in full on 2026-11-12", between(chechen, start, end))
        balti = between(text("sources", "bessarabia-moldova-record-routing"), "- **S5:**", "- **S6:**")
        self.assertIn("opened and read on 2026-11-12", balti)


if __name__ == "__main__":
    unittest.main()
