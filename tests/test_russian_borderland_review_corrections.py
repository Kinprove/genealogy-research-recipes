"""The Russian Empire, Soviet and borderland recipes keep the corrections from the review in issue #88.

Each test pins corrected facts. Where the review or a draft of the fix had a claim that the sources
did not support, the test also checks, inside the relevant passage, that the claim is gone, so a
later edit cannot quietly bring it back.
"""

import re
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


class PolishCustodyTests(unittest.TestCase):
    TEXT = recipe("polish-index-original-record-recovery.md")

    def test_transfer_rule_cites_article_128_for_books_kept_before_2015(self):
        rule = between(self.TEXT, "The Civil Status Records Act", "**Privacy gate:**")
        for phrase in (
            "kept before 1 March 2015",
            "100 years after the birth book was closed",
            "80 years after the marriage or death book was closed",
            "(art. 128(1))",
            "(art. 128(1a)–(1b))",
            "issues no certificate (odpis)",
        ):
            self.assertIn(phrase, rule)
        self.assertNotIn("art. 28", rule)  # art. 28 governs the post-2015 electronic register
        self.assertNotIn("states no transfer threshold", self.TEXT)

    def test_pradziad_is_searched_inside_szukaj_without_a_closure_year(self):
        passage = between(self.TEXT, "Treat PRADZIAD as a finding aid.", "**List of files**")
        self.assertIn("It is searched inside Szukaj w Archiwach", passage)
        # A window, not a sentence: dots inside domain names would end a sentence pattern early.
        self.assertIsNone(re.search(r"PRADZIAD.{0,200}\b2019\b|\b2019\b.{0,200}PRADZIAD", self.TEXT))


class GaliciaHoldersTests(unittest.TestCase):
    TEXT = recipe("galicia-bukovina-habsburg-record-routing.md")

    def test_step_4_names_the_fonds_and_the_other_holders(self):
        step = between(self.TEXT, "## 4. Find who holds the books", "## 5.")
        for phrase in (
            "fond 201, opys 4a",
            "fond 618, opys 2",
            "most of its metrical books are copies",
            "fond 56/142",
            "consistory copies of metrical books by deanery",
            "fond 487",
            "FamilySearch collection 1910265",
            "Geneteka's **Ukraina** territory",
            "Archbishop Eugeniusz Baziak Archive",
        ):
            self.assertIn(phrase, step)
        # No source showed parish books at the Lviv oblast archive; its books went to TsDIAL.
        self.assertNotIn("ДАЛО", step)
        self.assertNotIn("DALO", step)
        self.assertNotIn("parish originals", step)

    def test_cadastre_fonds_are_both_named(self):
        self.assertIn("Josephine (TsDIAL fond 19) and Franciscan (TsDIAL fond 20)", self.TEXT)
        self.assertNotIn("pre-1784 gap", self.TEXT)

    def test_jewish_books_are_not_sought_in_catholic_registers(self):
        step = between(self.TEXT, "## 2. Choose the books by confession", "## 3.")
        self.assertIn("supervised the Jewish books, which the communities kept from 1789", step)
        self.assertIn("no formal regulations or consistency until 1877", step)
        self.assertIsNone(
            re.search(r"(search|look)[^.]*(Roman Catholic|RC|Catholic) (parish )?register", step, re.IGNORECASE)
        )

    def test_khotin_villages_are_sent_to_the_bessarabia_recipe(self):
        self.assertIn("that was in Khotin uezd of Bessarabia before 1918", self.TEXT)
        self.assertIn("(bessarabia-moldova-record-routing.md)", self.TEXT)


class SovietRepressionTests(unittest.TestCase):
    TEXT = recipe("russian-military-repression-record-episodes.md")

    def test_access_rule_counts_75_years_from_the_documents(self):
        step = between(self.TEXT, "## Recover the next document", "3. Identify the present custodian")
        for phrase in (
            "No. 375/584/352 of 25 July 2006",
            "either the person's written consent or proof of death",
            "or, after death, of the heirs",
            "75 years after the documents were created",
            "Rosarkhiv order No. 38 of 2025",
            "ask for the file itself",
        ):
            self.assertIn(phrase, step)
        self.assertNotIn("after the case was closed", self.TEXT)
        self.assertNotIn("legal successors", self.TEXT)

    def test_memorial_sites_are_offline_and_open_list_is_separate(self):
        self.assertIn("were offline on 7 November 2026", self.TEXT)
        self.assertIn("declared the international public movement Memorial extremist", self.TEXT)
        self.assertIn("not a copy of it", self.TEXT)
        self.assertNotIn("updates stopped", self.TEXT)
        for unsupported in ("mirror", "foreign IP", "foreign-IP"):
            self.assertNotIn(unsupported, self.TEXT)


class ChechenIngushCustodianTests(unittest.TestCase):
    TEXT = recipe("chechen-ingush-1944-deportation-records.md")

    def test_kazakhstan_routing_keeps_the_archive_of_the_president_first(self):
        step = between(self.TEXT, "## 6. Search the place of settlement", "## 7.")
        self.assertIn("In Kazakhstan, ask the Archive of the President first.", step)
        self.assertIn("251,000 special-settler files", step)
        self.assertIn("(КПСиСУ)", step)
        for unsupported in ("ИЦ ДП", "ДКНБ", "police information centre", "oblast state archive"):
            self.assertNotIn(unsupported, step)

    def test_garf_fonds_are_administrative_series(self):
        step = between(self.TEXT, "## 5. Ask the Chechen Republic's custodians", "## 6.")
        self.assertIn("f. Р-9479", step)
        self.assertIn("f. Р-9401", step)
        self.assertIn("The guide describes no personal files of deportees in either fond", step)
        self.assertNotIn("echelon lists", step)


class ImperialRecordTests(unittest.TestCase):
    def test_central_service_record_fonds(self):
        text = recipe("russian-imperial-service-record-recovery.md")
        passage = between(text, "**Also check the central series.**", "When a list ends")
        for phrase in ("RGIA f. 1349", "оп. 3 (1800–1894", "RGIA f. 1343", "f. 409", "f. 879", "f. 546"):
            self.assertIn(phrase, passage)
        self.assertIn("a miss there is not a negative", passage)
        self.assertNotIn("3–6", passage)  # the alphabetical inventories are оп. 1–3
        self.assertNotIn("first place", text)
        self.assertNotIn("St Petersburg", passage)  # RGVIA is not there; no source places the series
        self.assertNotIn("f. 400", text)  # military physicians are in f. 879 and f. 546

    def test_police_register_is_one_row_not_the_first(self):
        text = recipe("old-believer-sectarian-record-recovery.md")
        self.assertIn("only if the parents' marriage had been entered", text)
        self.assertIn("not ahead of them", text)
        self.assertNotIn("series to check first", text)
        self.assertIsNone(re.search(r"\bmost\b[^.]*never used", text, re.IGNORECASE))  # testimony, not counts

    def test_revisions_without_women_are_named(self):
        text = recipe("russian-revision-list-household-chaining.md")
        self.assertIn("The 1st (1719), 2nd (1744–1747) and 6th (1811) revisions did not record women", text)
        self.assertNotIn("The early censuses often did not record women", text)

    def test_surviving_1897_sets_are_only_the_sourced_ones(self):
        text = recipe("russian-revision-list-household-chaining.md")
        step = between(text, "## 8. Check that 1897 census sheets survive", "## 9.")
        self.assertIn("ф. И-417, оп. 2, д. 1–4175", step)
        self.assertIn("all except Berezov and Surgut", step)
        for unconfirmed in ("Arkhangelsk", "Vologda", "Rybinsk"):
            self.assertNotIn(unconfirmed, step)


class MetricalBookTests(unittest.TestCase):
    TEXT = recipe("russian-orthodox-metrical-book-recovery.md")

    def test_books_after_1917_are_dated(self):
        step = between(self.TEXT, "## 3. Route each parish-year to both custodians", "## 4.")
        for phrase in ("18 (31) December 1917", "20 January (2 February) 1918", "143-FZ, art. 77", "three rows"):
            self.assertIn(phrase, step)
        self.assertNotIn("many parishes", step)
        # Art. 77 names ZAGS act books; it is not the rule for church metrical books. Pin the one
        # sentence that cites it, with its subject, and allow no other citation of the article.
        self.assertIn(
            "ZAGS act books stay with ZAGS for 100 years from each entry and then go to the state archive"
            " (Federal Law 143-FZ, art. 77)",
            step,
        )
        self.assertEqual(step.count("art. 77"), 1)
        self.assertNotIn("article 77", step.lower())

    def test_calendar_rule_links_the_shared_offsets(self):
        for name in ("russian-orthodox-metrical-book-recovery.md", "soviet-personal-file-recovery.md"):
            text = recipe(name)
            self.assertIn("written before 14 February 1918, is normally Old Style", text)
            self.assertIn("evidence-proof-judgment.md#follow-record-versions-and-test-disputed-dates", text)

    def test_yandex_coverage_comes_from_its_catalogue(self):
        self.assertIn("29 on 8 October 2026", self.TEXT)
        self.assertIn("record the archives it lists, with the date", self.TEXT)


class BorderCustodyTests(unittest.TestCase):
    def test_hamburg_departure_lists_are_a_ladder_step(self):
        text = recipe("russian-empire-emigrant-origin-recovery.md")
        step = between(text, "5. If the arrival record or a family account names Hamburg", "For a Canadian route")
        self.assertIn("1850–1934 with a gap for 1915–1919", step)
        self.assertIn("usa-immigration-search-recovery.md#5-recover-an-arrival-through-the-departure-list", step)
        for unsupported in ("Libau", "Antwerp", "MyHeritage"):
            self.assertNotIn(unsupported, step)

    def test_bessarabia_after_fond_211_routes_by_the_100_year_term(self):
        text = recipe("bessarabia-moldova-record-routing.md")
        step = between(text, "## 4. Search Bessarabian metrical books", "## 5.")
        self.assertIn("ask ANA, then the Public Services Agency", step)
        self.assertIn("for a register still inside the 100-year term, ask ASP", step)
        self.assertIn("for a village that went to the Ukrainian SSR in 1940, follow step 1", step)
        self.assertIn("file titles found only villages now in Moldova", step)
        self.assertNotIn("After 1923, look outside fond 211", text)
        self.assertNotIn("A later Romanian-period event needs another fond", text)
        self.assertNotIn("post-1944", step.lower())  # post-1944 registers are all still with ASP

    def test_ukrainian_bound_book_exception_is_shared(self):
        self.assertIn("bound into a combined book", recipe("soviet-personal-file-recovery.md"))
        self.assertIn("bound into a combined book", recipe("galicia-bukovina-habsburg-record-routing.md"))


if __name__ == "__main__":
    unittest.main()
