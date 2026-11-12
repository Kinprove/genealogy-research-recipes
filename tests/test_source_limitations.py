"""Keep issue #81's source limits with the affected claims, preserving later readings.

These are editorial regressions, not independent verification of historical facts.
A caveat elsewhere in a recipe cannot satisfy a check on the affected paragraph.
"""

import re
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / "skills/genealogy-research-recipes"


def paragraph(folder, slug, anchor):
    text = (SKILL / folder / f"{slug}.md").read_text(encoding="utf-8")
    matches = [" ".join(p.split()) for p in text.split("\n\n") if anchor in p]
    if len(matches) != 1:
        raise AssertionError(f"{slug}: expected one paragraph containing {anchor!r}")
    return matches[0]


# Each anchor identifies a particular claim, not merely a recipe with some caveat.
# Patterns pin the access limitation and the affected assertion or next action.
LIMITED_CLAIMS = (
    ("bessarabia-moldova-record-routing", "**Read a Тодор", (
        r"search-result summary.*most frequent.*full study was not read.*unconfirmed.*\[S21\]",
    )),
    ("early-new-england-town-records", "Her example is Abington", (
        r"might be with the older one \[S4\], \[S5\]",
        r"Abington, Massachusetts, established in 1712,.*Bridgewater \[S4\], \[S5\]",
        r"town report.*10 June 1712 \(o\.s\.\).*\[S7\]",
    )),
    ("early-new-england-town-records", "- For Massachusetts,", (
        r"no readable text.*fifth edition.*1997.*not confirmed.*\[S10\]",
    )),
    ("early-new-england-town-records", "Most town books", (
        r"New London.*sign-in page.*index note was not confirmed.*\[S11\]",
    )),
    ("early-new-england-town-records", "**Cut-off:**", (
        r"HSP catalog lead.*1985.*2002.*HTTP 403.*details remain unconfirmed.*\[S14\]",
    )),
    ("familysearch-practical-record-workflows", "A parent–child link", (
        r"Y2S38-s3tSc.*private when checked on 2026-10-22.*does not verify the parent-link types.*\[S47\]",
    )),
    ("23andme-match-research", "Request raw data early", (
        r"usually after about one week but sometimes up to thirty days \[O8 @2026-11-12\]",
        r"retain the request confirmation as preservation checks",
        r"Read the current delivery instructions before promising a download time",
    )),
    ("japanese-koseki-honseki-recovery", "**Map certificates", (
        r"indexed.*fee table.*500 yen.*470 yen.*440 yen",
        r"Only indexed text was checked.*HTTP 403.*full table was not read.*\[S13\]",
        r"Confirm the applicable map, parcel unit and current fee",
    )),
    ("historical-map-record-recovery", "- Retromap", (
        r"search-result title.*1804.*page could not be read.*label.*unconfirmed.*\[S38\]",
        r"1801–1804.*separately supported by S39",
    )),
    ("galicia-bukovina-habsburg-record-routing", "**Northern Bukovina:", (
        r"search-result summary.*1784–1840.*thesis itself was not read.*unconfirmed.*\[S18\]",
        r"Search-result catalogue text.*FamilySearch films.*full entries were not read.*confirm.*\[S19\]",
    )),
    ("historical-place-name-resolution", "- For Galicia, take", (
        r"2001 county history, partially read, cites.*1925.*1921 \[S41\]\. Check the edition's title page",
    )),
    ("russian-military-repression-record-episodes", "For Western-Ukrainian deportation", (
        r"archives \[H33\].*1995.*search-engine extract.*unread page.*unconfirmed \[H32\]",
        r"Депортації.*1996–2002.*PDF itself could not be fetched.*edition details remain unconfirmed \[H34\]",
    )),
    ("russian-military-repression-record-episodes", "3. Identify the present custodian", (
        r"316-VIII.*read in the reproduction on kodeksy.com.ua.*official zakon.rada.gov.ua page could not be opened",
        r"within two years \[H42\].*not a check against the official text",
    )),
    ("russian-revision-list-household-chaining", "household sheets of the 1897 census", (
        r"Search-engine summaries.*ordered destroyed.*PDF did not load.*survival remains unconfirmed.*\[S26\]",
    )),
    ("russian-revision-list-household-chaining", "1. Check the survival catalogues", (
        r"Altai.*search-result bibliography.*site refused.*contents and usability remain unconfirmed \[S28\]",
    )),
    ("usa-immigration-search-recovery", "2. Check the historical rule", (
        r"FAM link.*lead.*certificate error.*title and contents were not confirmed.*item 46",
        r"readable authoritative rule before using it to infer citizenship",
    )),
    ("state-legislative-private-act-petitions", "The legislature was not always", (
        r"publisher's store description.*web-archive copy.*1805.*1827.*\[S5\]",
        r"book itself was not consulted.*dates as leads",
    )),
    ("us-20th-century-military-service-reconstruction", "Army transport passenger lists", (
        r"presenters describe.*\[S14\], \[S22\]",
        r"61174.*HTTP 403.*RG 92.*1910–1939.*not confirmed.*\[H12\]",
    )),
    ("quaker-meeting-record-recovery", "2. Keep the printed Encyclopedia", (
        r"197 meetings in 17 states was not verified.*current collection description.*confirm coverage",
        r"presenter demonstrates.*Walnut Ridge.*\[S1\]",
    )),
    ("repository-photograph-collection-search", "**WWII participants:**", (
        r"participant-search link was a placeholder.*2026-11-02.*search was not verified",
        r"unsearched lead.*do not count an unavailable search as a name miss",
    )),
    ("russian-volost-town-administration-records", "**1917 agricultural census.**", (
        r"Поземельная перепись, 1917.*title, fond and film format came only from search results.*sign-in",
        r"not confirmed from the full entry.*before claiming.*filmed or available.*\[S13\]",
    )),
)


class SourceLimitationTests(unittest.TestCase):
    def test_each_affected_claim_carries_its_own_limit(self):
        for slug, anchor, patterns in LIMITED_CLAIMS:
            with self.subTest(recipe=slug, claim=anchor):
                passage = paragraph("recipes", slug, anchor)
                for pattern in patterns:
                    self.assertRegex(passage, pattern)

    def test_presenter_wording_is_quoted_from_the_full_captions(self):
        passage = paragraph("recipes", "catholic-sacramental-cross-notations", "The papal decree")
        self.assertIn('"after Easter 1908, you may begin to see this extra column" with the marriage [S2]', passage)

    def test_fond_identity_uses_the_archive_catalogue_that_was_read(self):
        slug = "historical-map-record-recovery"
        passage = paragraph("recipes", slug, "Galicia also has two earlier land surveys")
        for value in ("fond 19", "fond 20", "[S32]", "[S35]", "[S52]"):
            self.assertIn(value, passage)
        self.assertNotIn("[S34]", passage)
        self.assertRegex(paragraph("sources", slug, "- **S52:**"), r"opened 2026-11-07.*fond 19.*fond 20")

    def test_later_readings_of_agad_and_tsdial_are_preserved(self):
        slug = "galicia-bukovina-habsburg-record-routing"
        # Historical failed fetches in these entries must not trigger a blanket caveat.
        self.assertIn("opened directly 2026-11-07", paragraph("sources", slug, "- **S8:**"))
        self.assertRegex(paragraph("sources", slug, "- **S16:**"),
                         r"Both PDFs were read on 2026-11-07 from Internet Archive captures")
        self.assertRegex(paragraph("recipes", slug, "  - AGAD ("), r"8,500.*\[S8\]")
        self.assertRegex(paragraph("recipes", slug, "  - TsDIAL ("), r"2026 \[S16\]")

    def test_unread_parcel_notice_does_not_restore_a_charging_unit(self):
        passage = paragraph("recipes", "japanese-koseki-honseki-recovery", "**Map certificates")
        self.assertNotRegex(passage, r"per.parcel|1筆|\[S14\]")


if __name__ == "__main__":
    unittest.main()
