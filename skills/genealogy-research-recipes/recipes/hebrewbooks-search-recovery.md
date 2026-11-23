---
id: "hebrewbooks-search-recovery"
title: "Recovering HebrewBooks search misses"
summary: "Recover HebrewBooks names or passages missed by OCR, catalogue spelling or a query that never reached search."
kind: "platform"
scope: {"platforms": ["hebrewbooks"], "tasks": ["Hebrew OCR letter confusions, catalogue versus full-text searches, short mobile queries, inaccessible routes, Shafeh title searches, given-name indexes, bound parts, per-part dating and viewer versus printed page numbers."]}
privacy: "none"
gates: []
guardrails: [{"id": "HEBREWBOOKS-SEARCH-RECOVERY-01", "text": "An access error, an unsubmitted query and a completed search with zero hits are different observations. Record the surface and the observation before interpreting it."}]
handoff: ["rabbinic-literature-person-search"]
checked: "2026-11-12"
checked_basis: "Rechecked 2026-11-12"
capabilities: {"browse": ["hebrewbooks"], "local_script": ["curl for a public page PDF"], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Jewish records", "order": 99}
---

# Recipe: Recovering HebrewBooks search misses

## Contents

- Goal
- Mental model
- What to look for in Hebrew books
- Decision procedure
- Bound parts and date evidence
- Prompt patterns
- Failure modes

## Goal

Recover a name or passage hidden by Hebrew OCR, catalogue spelling or a query that
never reached the search service. The useful question is **which layer failed**, before
another spelling is tried or a miss is recorded.

## Mental model

Keep these observations separate; each changes the next useful action.

| Surface | What the observation represents | Next action |
| --- | --- | --- |
| Mobile app history/empty state after a short query | A local query gate in the pinned source | Expand the intended title or name |
| Catalogue title/author result | A candidate work | Identify the edition, then investigate its contents |
| OCR text miss | A spelling or recognition probe that missed | Test the documented one-letter confusions |
| Printed name index | Entries organized by the index's own key | Establish given-name versus surname ordering |
| Viewer page pointer | A location in a particular scan | Read the printed locator and edition |
| HTTP 403 | An inaccessible route | Switch discovery route and retain the intended query |

## What to look for in Hebrew books

A person can appear in a Hebrew book without being its subject or author:

- **Subscriber lists (prenumeranten).** Many books printed the names of those who ordered a copy
  before publication, arranged by town. Berl Kagan's *Sefer HaPrenumerantn* (New York, 1975)
  indexes which books carry subscribers from which towns. It lists towns, not names, so use it
  to choose the books, then read each list.
- **Introductions and title pages.** In rabbinic books these usually give information about the
  author's family.
- **Approbations (haskamot), responsa and pedigree documents (yichus briefs)**, which JewishGen's
  rabbinic-genealogy resources list as genealogical material.

Record whether a name comes from the author, an approbation or a subscriber list, with the
part's title or edition and page as in step 6 and the part register below.

## Decision procedure

1. **Establish that a search actually ran.** An access error, an unsubmitted query and
   a completed search with zero hits are different observations. Record the surface and
   the observation before interpreting it.
   - In the published HebrewBooks mobile app source at commit `7b2443c`, the search
     screen shows history or an empty state for a raw query shorter than **three UTF-16
     code units**. The results widget also returns before its catalogue request for
     that length. A two-letter query such as `אב` therefore does not produce a catalogue
     miss through that screen. Expand it to the intended full name or title.
   - The app stores the query without trimming it. Spaces and Hebrew combining marks
     contribute to its length; padding is not a meaningful expansion. This finding belongs to the pinned
     app implementation; do not transfer its threshold to the website or API.

2. **Choose the surface that can answer the question.** Use the catalogue to locate a
   work by title or author; use full text to seek a person or passage inside it. A surname
   missing from title/author metadata has not been searched inside the book. For a
   catalogue miss, issue separately recorded plene/defective spellings and attested name
   variants. The catalogue described by Zitter in 2010–2011 lacked authority control:
   search those spellings yourself rather than expecting automatic unification. Preserve
   the spelling that identifies the edition you find.

3. **After the correct Hebrew spelling misses in OCR, try a documented confusion.**
   The 2011 Hebrew-search workaround gives these concrete probes:

   | Intended text | Retrieval probe | Changed letter |
   | --- | --- | --- |
   | `יעקב` | `ימקב` | ע to מ |
   | `תלמיד חכם` | `תלמיד מכם` | ח to מ |
   | A token containing ד or ר | Swap that letter | ד and ר |

   Test one changed letter per probe. The malformed query is a retrieval key:
   **never record `ימקב` as a historical variant of `יעקב` on this basis**.
   A 2018 study notes that HebrewBooks and similar projects used commercial OCR packages, and
   that no commercial or academic OCR then handled Rashi script, the typeface of many
   commentaries. When the passage you need is set in Rashi script, read the page image before
   recording a miss.

4. **Change discovery route when the surface has failed.** Run
   `site:hebrewbooks.org <Hebrew phrase>` in an external search engine. MacDowell's
   example used the OCR reading `ימקב` for `יעקב` [B2 @2026-11-19]. Check the
   beta search entry point identified in Brand's 2022 guide [B3 @2026-11-19] and
   record its response on the date you search. Otzar HaHochma advertises paid OCR
   full-text search in a separate collection of about 156,000 Judaic books [B12 @2026-11-19].
   **For an inaccessible catalogue, also use the [Shafeh search form](https://shafeh.org/hb/search).**
   Select the title field for a catalogue search. Author and OCR have separate fields
   [B4 @2026-11-19]. A title search for `מסילת ישרים` returned book **41768**,
   listed under Moshe Hayyim Luzzatto, alongside partial matches `מסילת הברזל` and
   `דובר ישרים` [B16 @2026-11-19]. Verify the whole title and author before saving
   the book ID. Record the intended within-book query separately until you can search
   the text or inspect the page.

5. **For a located work, use its printed index when OCR does not find the passage.**
   Read the heading and compare several entries before choosing the lookup key. In
   a J-Roots discussion, the correction identified the index starting on page 21 as
   arranged by given name. A surname search alone would miss the reader's lookup
   route [B5]. Record the sorting field, then follow the entry to the printed page.

6. **Keep the hit's coordinates separate.** Record the book ID (`req`), viewer page
   (`pgnum`), printed page or folio visible on the image, and edition from the title page.
   The viewer number is not necessarily the printed number. A link has this shape:
   `https://hebrewbooks.org/pdfpager.aspx?req=<id>&pgnum=<n>`.

   Before saving a hit, identify its part and that part's dating evidence using the
   [bound-part and date check](#bound-parts-and-date-evidence). Complete the whole-scan
   inventory before concluding that a passage is absent.

## Bound parts and date evidence

**Map the whole scan before reporting "not in this book".** Inspect it through its end
for separate title pages and changes or restarts in printed pagination. List every bound
part and the viewer page of each title page; inspect those title pages and their versos.
Searching the opening pages has not searched a later part. Record the viewer spans actually
searched or read and any missing or uninspected pages. If the inventory or coverage is
incomplete, report that limit instead of a book-wide negative [B14].

**Date the part you are citing.** Record its own title-page wording and each date with
its evidence type and exact location: title-page imprint, approbation or censor approval,
for example. Do not copy the outer title page's year into a later part's citation without
evidence that it applies there. An approbation or censor date is the date shown for that
approval in that part; it does not by itself establish the part's publication year or date
the whole bound volume. If no publication year is established for the part, leave it
unknown and retain the approval date separately [B14].

For using an approbation as dated evidence of an office, see
[rabbinic-book finding aids](rabbinic-literature-person-search.md#7-read-the-subjects-own-books-and-the-front-matter-first).
For Hebrew years and chronograms, see the **Dates** rule in
[hit screening](rabbinic-literature-person-search.md#8-screen-every-hit-before-it-becomes-a-person).

Keep a part register, then attach the hit to its part. Copy a printed page or folio and
side as shown; leave an absent or unreadable coordinate unresolved. Keep the viewer page
separate even when the printed numbering restarts.

| Record | Fields to keep separately |
| --- | --- |
| Each bound part | Part label and title/edition; title-page viewer page; printed pagination sequence; viewer span; inspected coverage and gaps |
| Each date | Part; literal date; evidence type; printed locator if present; viewer page; whether it establishes a publication year or leaves it unknown |
| Each hit | Book ID; part; that part's title-page viewer page; printed page/folio and side; hit's viewer page; part's publication year or unknown; separate dating evidence |

**Optional public-page retrieval.** Try the pagefeed URL
`https://beta.hebrewbooks.org/pagefeed/hebrewbooks_org_<id>_<N>.pdf`, replacing `<id>`
with the book ID and `<N>` with the **viewer page**, not the printed locator
[B14 @2026-11-16]. A request
for book 41768, page 23 returned a one-page PDF on 2026-11-16; this checks that one
request, not availability for every book or page [B15 @2026-11-16].

```sh
curl --fail --location --output page.pdf 'https://beta.hebrewbooks.org/pagefeed/hebrewbooks_org_<id>_<N>.pdf'
```

Check that the response is a PDF, then open it and verify the image against the intended
part and locator before citing it. A successful download alone does not verify the text.
For the citation, retain the viewer link from step 6 together with the part and printed locator.
If the request fails or returns a challenge or other non-PDF response, record the failure
and use the browser route; do not treat it as a missing page or passage.

## Prompt patterns

- **Recover a miss:** “I searched [surface] for [literal query] and observed [completed
  zero-hit search / no request / access error]. Propose the next surface or one-letter
  OCR probe. Label intended spelling separately from retrieval spelling.”
- **Inspect an index:** “Read this heading and these entries. Identify the demonstrated
  ordering key, then show where [given name and surname] should be sought.”
- **Map a volume:** “List each bound part and its title-page viewer page. Record the
  inspected spans and gaps. For each part, separate publication-year evidence from dates
  on approvals; leave an undetermined publication year unknown.”
- **Save a hit:** “Return book ID, part, that part's title-page viewer page, hit's viewer
  page, printed locator and edition separately. Give dating evidence for that part.
  Transcribe the relevant image text. Leave an unread coordinate unresolved.”

## Failure modes

- Turning an OCR-confused query into a name variant in a genealogy record.
- Reporting a mobile-app short query or an HTTP 403 as a completed zero-hit search.
- Searching a catalogue surname field and claiming that the book's text was searched.
- Assuming that every scanned name index is arranged by surname.
- Inferring current Boolean, fuzzy, wildcard or proximity syntax from historical guides.
- Treating a forum's book ID and ambiguous “page” pointer as an image-verified citation.
- Reporting a passage absent from the book after searching only the first bound part.
- Assigning the outer title-page year or an approval date as every part's publication year.
