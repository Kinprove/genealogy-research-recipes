---
id: "ancestry-record-search-recovery"
title: "Ancestry record-search recovery"
summary: "Recover Ancestry records a search missed by checking collection scope and coverage before loosening dates, places or names."
kind: "platform"
scope: {"platforms": ["ancestry"], "tasks": ["an attached census disappearing from results, narrow Card Catalog matches, birthplace/residence confusion, conservative wildcard batches, name-free searches, book page versus image numbers, enumeration-district browsing, or index-only records."]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "ANCESTRY-RECORD-SEARCH-RECOVERY-01", "text": "Keep three observations separate: no indexed candidate; no matching images in the available inventory; and documented absence in the original surviving records."}]
handoff: ["ai-for-documentary-records", "dna-match-outreach-staging", "evidence-proof-judgment"]
checked: "2026-11-12"
checked_basis: "Rechecked 2026-11-12"
capabilities: {"browse": ["ancestry"], "local_script": [], "extensions": [], "data_transfer": ["publish", "request"], "contact": []}
router: {"section": "Record websites, libraries and maps", "group": "Record websites", "order": 37}
---

# Ancestry record-search recovery

## Contents

- Goal
- Thirteen recovery methods
- Check the saved record on each intended person
- Find a researcher or locality helper
- Prompt-craft and search log

## Goal

Recover an archival record when Ancestry's hints, person search or name index fails.
Choose the recovery that addresses the actual failure: hidden search settings,
catalog discovery, an overconstrained query, a transcription error, an image-only
volume or a record held elsewhere. Do not keep repeating the same name search.

This recipe owns Ancestry retrieval. For identity and negative-evidence judgments,
read [evidence-proof-judgment.md](evidence-proof-judgment.md); for AI transcription
and full-text finding aids, read [ai-for-documentary-records.md](ai-for-documentary-records.md).

## Thirteen recovery methods

### 1. Reset the search state before changing the ancestor

**Trigger:** expected records disappear after research in another country or category.

Check Collection Focus and result-type settings; restore the intended collections
and historical-record categories. These settings persist between searches. Record
their state before and after resetting them, then rerun the same query: this tests
the search environment without changing the person. See [Ancestry's refinement guide](https://help.ancestry.com/hc/en-us/articles/53933347318419-Refining-Your-Search-to-Improve-Results).

Also inspect any active option that suppresses records already saved or viewed.
Ancestry's April 2026 demonstration shows its smart filter hiding other records
from an already-attached census. That demonstration is a diagnostic clue; inspect
the controls actually present in the current account before attributing missing
results to this feature. Do not remove existing tree attachments to recover a hit.

### 2. Clear catalog locality terms to recover nationwide collections

**Trigger:** a town, province or county in the catalog's Title/Keywords finds very little.

Clear the town or province from the Card Catalog’s Title/Keywords fields and compare the list with a country or category search [S14 @2026-11-19]. In Ancestry’s 2026 demonstration, entering Nova Scotia hid national Canadian census collections that included the province [B1 @2026-11-19]. Open the national collection and look for the locality within its coverage.

Inspect geographic filters separately and widen any that restrict the intended
jurisdiction. Widening a filter alone does not repair a text query that still
requires the locality word. Neither search is an exhaustive inventory of records
concerning the place.

For a historically German locality now in another country, also try the present country in the catalog’s place filter [S28 @2026-11-22] [S29 @2026-11-22]. To narrow a large collection list, combine the place, record type and decade filters before adding title terms [S30 @2026-11-22] [S14 @2026-11-22]. If the catalog route misses, use **Search → All Collections → Explore by Location**, select the place and inspect its **Collections** tab [S30 @2026-11-22] [S29 @2026-11-22]. Check each candidate’s actual place and date coverage.

### 3. Search catalog titles and keywords separately

**Trigger:** the expected record category is missing from the catalog results.

Try a short title fragment, then a separate keyword search. Catalog keywords can
find descriptions that a title search misses; they do not search every name or
word in the underlying images. More keyword terms narrow the catalog: retry
distinctive terms individually instead of pasting a long imagined collection
title. Try related record vocabulary in separate passes, such as electoral
registers when searching for census-like household or residence evidence.
Open each plausible collection and inspect its actual coverage.
See [the Card Catalog guide](https://help.ancestry.com/hc/en-us/articles/53933305954579-Using-the-Card-Catalog).

Try the singular and plural separately, then clear the text and compare a category-and-place search. In the Genealogy Gems demonstration, searching for “postcard” missed titles containing “postcards” [B16]. Log the date, terms, filters and count for each attempt so you can reproduce the difference.

For M841, enter `postmasters` in the Card Catalog’s Title field to find *U.S., Appointments of U. S. Postmasters, 1832–1971* [S14 @2026-11-21], [S20 @2026-11-21]. A 2022 Title search from the available excerpt missed the collection with `post office` [S19 @2026-11-21]. Compare the terms in the current account if the collection is missing.

Do not take an empty Ancestry-wide search as proof that a newspaper item is absent. Ancestry's
global search does not include the Newspapers.com Stories and Events Index collections because
of their size, as reported in March 2024 [S1 @2026-11-12], [S2 @2026-11-12]. Run a Card
Catalog title search for Newspapers.com, open the collection for the person's state or
country, and search it directly [S2 @2026-11-12], [S3 @2026-11-12]. A hit links to the page on
Newspapers.com, which needs that site's own subscription to view [S3 @2026-11-12].

When starting a different Card Catalog lookup, clear the previous place, record type and date filters before testing the new terms [S14 @2026-11-22]. Use the **Clear All** control from the available excerpt if the current account offers it, or remove the filters individually [S32 @2026-11-22].

For U.S. Regular Army returns, start with the unit and the month of service. If an artillery or cavalry title search misses, use the Title term `non-infantry` from the available excerpt of the 2022 demonstration, then check the current collection’s browse choices for the unit [S45 @2026-11-22]. The National Archives links M727 for artillery regiments, M728 for field artillery batteries and regiments, M744 for cavalry regiments, and M665 for infantry to the same Ancestry collection (1225) [S24 @2026-11-22]. For infantry, also try the title fragment `Returns from Regular Army Infantry Regiments` from the available excerpt [S45 @2026-11-22]. Match the film series, unit and month. M665 runs from June 1821 to December 1916, so check an earlier service episode against a different series [S24 @2026-11-22].

For a Boston Pilot notice, use the Card Catalog title fragment `Missing Friends` from the available excerpt of the 2022 walkthrough, or open collection 5060 directly [S51 @2026-11-22] [S52 @2026-11-22]. Search by name. If it misses, check whether the current account exposes the volume browse route from the available excerpt and select the volume covering the target years [S51 @2026-11-22].

For a marriage announcement or obituary, open the corresponding regional index. Use the newspaper navigator’s category links or its state and territory links to match the event and region before searching the broader Stories and Events index [S3 @2026-11-22] [S36 @2026-11-22] [S37 @2026-11-22].

If a Newspapers.com index query misses, clear the subject’s birth year and search by publication date and place where those fields are offered [S3 @2026-11-22]. Check issues around the event and papers in other places tied to the people involved [S3 @2026-11-22] [S38 @2026-11-22]. For a married woman, also try `Mrs. [Husband’s Name]` alongside her own maiden and married names [S3 @2026-11-22].

Read the newspaper collection’s coverage notes and verify that the paper and issue are included before interpreting an index miss [S3 @2026-11-22]. When you know the issue is available, browse it for the notice after a keyword miss, especially if the page is faded or damaged and OCR can miss the text [S3 @2026-11-22] [S37 @2026-11-22].

From **View Record**, follow the newspaper thumbnail to the original page and read the article or caption in context [S3 @2026-11-22] [S37 @2026-11-22]. In a 1924 example, a mother’s name in the index led to a photograph whose caption identified her daughters as the people pictured [S3 @2026-11-22].

### 4. Revisit collections that changed after the failed search

**Trigger:** an old search log says the relevant collection produced no candidate.

Use the catalog's Last Updated ordering to identify collections worth revisiting.
Read what changed and rerun the saved query in the relevant collection. An update
date alone does not establish new coverage for the target: it can concern other
years, localities or data. Record the collection and the recheck date, rather than
carrying an old failure forward indefinitely.

Sort by **Date Added** to identify collections introduced since the logged search date. Use the date-updated sort to check collections you already searched [S31 @2026-11-22] [S14 @2026-11-22]. Open each relevant collection and verify its holdings for the target place and date.

### 5. Diagnose coverage inside the collection

**Trigger:** a collection title spans the right place and years, but the person is absent.

Read its Source and About sections, then inspect the available browse subdivisions
and volumes. Check the actual locality, date, record type and population covered,
including omissions or restrictions. Run a place/date query without the target
name to see what the index returns for that area. This is an **index diagnostic**:
zero results can reflect unindexed images, missing fields or restrictive settings.
Check the image inventory separately before deciding which material is absent.
See [Ancestry's collection-information guide](https://help.ancestry.com/hc/en-us/articles/53933269983507-Source-and-Collection-Information).

Compare the date spans of the listed volumes. Queue every relevant volume whose
span overlaps the target period; keep each volume's inspected
range separately. A gap in this inventory does not establish that the original
records were destroyed. Matching dates or titles do not establish that two books
are copies, or which is earlier: inspect the records and their provenance before
combining their evidence.

For a deceased U.S. person with unknown parents, search *U.S., Social Security Applications and Claims Index, 1936–2007* [S9 @2026-11-16]. Ancestry lists possible birth details, father’s name, mother’s maiden name and name/claim changes, but warns that inclusion is incomplete and parents’ names can be suppressed [S5 @2026-11-16]. Extract the fields actually shown as application/claim statements; a blank parent field or missing person is not a finding that no application existed [S5 @2026-11-16].

Keep three observations separate: no indexed candidate; no matching images in the
available inventory; and documented absence in the original surviving records.
Use the existing evidence-judgment recipe before drawing a genealogical conclusion.

For a name mentioned in a handwritten deed, probate record or other long text, check whether the account exposes **Search → Search full text** and whether the collection is included [S26 @2026-11-22] [S27 @2026-11-22]. Ancestry documents selected collections, handwriting recognition, transcription errors and beta access that can vary across All Access accounts [S27 @2026-11-22]. Use the collection’s own search or browse the relevant images after a full-text miss or when access or collection coverage is uncertain.

For a U.S. city directory, open collection 2469 and use the locality and year browse choices from the available excerpt of the 2023 walkthrough [S33 @2026-11-22] [S32 @2026-11-22]. Check the current account for the target city and edition before entering a name. If the edition is available, verify the locality and publication year on its title page [S33 @2026-11-22] [S34 @2026-11-22].

### 6. Remove tree facts that belong to another life stage

**Trigger:** a tree-launched search returns nothing useful for a different life stage,
such as childhood or a possible remarriage.

Inspect the populated query, including relationships. Remove the later spouse,
children, later residence and uncertain facts when they constrain an early-life
search; retain appropriate parents or siblings. Use the name recorded at that
life stage. Search forms differ by collection, so use only fields that this
collection actually exposes. A missing death-date control in a census search is
not evidence that the person lacks a death record.
See [How to Search](https://help.ancestry.com/hc/en-us/articles/53933305561747-How-to-Search-Ancestry)
and [Search Tips](https://help.ancestry.com/hc/en-us/articles/53933347309331-Ancestry-Search-Tips).

For a possible remarriage, search the previous married surname within the supported dates and place. Inspect prefilled parents and siblings: their surnames can keep an unwanted maiden-name constraint in a query after it has been removed from the subject. Save both queries, remove the constraint and compare the results. Test the candidate against the actual marriage record [B8].

Keep the candidate’s reported surname in the subject field. Where the collection offers a suitable field, search the hypothesized family surname as a keyword or associate, with the supported place and year. Read the recovered record for the stated roles, including any parent or stepparent, before drawing a kinship conclusion [B23].

If sitewide search gives you no dedicated arrival field, open **Immigration & Travel** and enter the supported date or date range under **Arrival** [S55 @2026-11-22]. Use the collection-specific fields from the available excerpt as a cue to check the narrower **Passenger Lists** search before adding more life events [S54 @2026-11-22] [S55 @2026-11-22].

### 7. Relax the place level and age separately

**Trigger:** an exact city or birth year eliminates otherwise plausible candidates.

Select a recognized place from Ancestry's suggestions, then widen its matching
level from city to county or adjacent counties. Exact Oakland excludes a record
that gives only Alameda County. Keep birthplace and residence in their own fields:
the place where a census household lived need not be where its members were born.

Then relax the year independently. A census age converted to a birth year can
shift by one year even without an erroneous age; an unreliable age requires a
wider interval. Preserve the reliable anchor while changing one constraint at a
time, and record which change recovered a candidate.
See [Ancestry's refinement guide](https://help.ancestry.com/hc/en-us/articles/53933347318419-Refining-Your-Search-to-Improve-Results).

When a broad historical-record search returns hits from too many places, use the record
location filter on the left of the results page [S15 @2026-11-20], [S16 @2026-11-20].
Keep the person query as entered so the comparison isolates the effect of the filter.

If an undocumented death year fails, check the last record showing the person alive and search across the surrounding years. Absence from the next census suggests another search date, but gives no upper bound on death. An Ohio example yielded a 1930 death record five years before the stated year [B17]. Test a transposition separately, such as 1762 for 1726 [B18]. Compare any hit with the image, other dated records and namesakes.

For the **1841 England and Wales census**, allow for the instruction to round
ages 15 and above down in five-year steps. Where applied, a recorded age of 30
represents ages 30–34. Inspect the original age field and retain the reported
value; an index's calculated birth year is not an exact birth date. Use the
possible age range and census date to set search bounds, checking other records
before deciding whether rounding explains a discrepancy. The instruction alone
does not prove how a particular entry was completed.
See [The National Archives census guide, section 5](https://www.nationalarchives.gov.uk/help-with-your-research/research-guides/census-records/).

Check where each identified adult child lived near the parent’s estimated death. Use those dated addresses to select other death-record jurisdictions and check each collection’s date coverage. Record the source for the child’s residence separately from the hypothesis that the parent stayed or died there [B11].

For a U.S. death search, separate the residence county from the hospital or institution’s county. The standard death certificate gives separate residence, facility/place-of-death and county-of-death fields [S6]. If a known facility was elsewhere, search its locality as well as the home locality, preserving which place belongs to which field. Do not move the person’s residence merely because the death was recorded elsewhere [S10].

### 8. Use wildcards for a specific spelling uncertainty

**Trigger:** a name has plausible transcription or spelling variants.

Search recorded alternatives, initials and abbreviations; then use a pattern
such as `Niels?n` or `Greenbla*`. Keep a stable fragment and test one uncertain
part at a time. Ancestry's help pages say wildcards do not work with Soundex, so run
a wildcard search without Soundex. A Soundex code always begins with the name's first
letter, so a wrong initial defeats a Soundex search; then try an alternative spelling
or a name-free recovery instead of repeating that search.

When handwriting could interchange **t** and **l**, search the letter alternatives directly or with the supported wildcard. Soundex assigns them different codes; a visual resemblance is not a sound-code match. The same issue affects Bowery/Bowey: retaining the R gives B600 versus B000 under the standard NARA rules [S4]. Keep the two searches separate rather than assuming phonetic matching covers both [S7] [S8].

Current Ancestry help pages state different wildcard limits:

- [Getting Started, Lesson 5](https://help.ancestry.co.uk/hc/en-gb/articles/53933301322899-Getting-Started-Lesson-5-Search-Tips):
  at least three non-wildcard letters, a letter as the first or last character, and `*`
  for zero to five letters.
- [Search Tips](https://help.ancestry.com/hc/en-us/articles/53933347309331-Ancestry-Search-Tips):
  `?` and `*` anywhere, at least one letter, and `*` for one or more letters.

Both say `?` stands for one letter. A pattern with at least three non-wildcard letters
that begins or ends with a letter, like the two above, satisfies both. Do not infer a universal short-pattern rule or require an Exact checkbox from
an old tutorial; check the current field's instructions when a pattern is rejected.
See also [Spelling Variations](https://help.ancestry.com/hc/en-us/articles/53933306665107-Searching-with-Spelling-Variations)
and [Searching with Soundex](https://help.ancestry.com/hc/en-us/articles/53933287988883-Searching-with-Soundex).

### 9. Recover an index entry without the target's name

**Trigger:** the right collection and locality exist, but variants still fail.

Remove the target name and search with a distinctive combination of residence, birth year, birthplace, sex or known relatives. Try each parent’s name or a sibling or neighbour whose name is easier to distinguish. Open the image, locate the household and check nearby pages for an entry indexed under another spelling [B2].

For the T718 payment ledgers in *U.S., Revolutionary War Pensioners, 1801–1815, 1818–1872*, retry a failed full-name search in the same account with only the surname [S18 @2026-11-21]. Inspect plausible ledger images for an obscured given name and compare the locality with known places for the pensioner. Check whether the place names the paying agency [S18 @2026-11-21]. In the 2022 example from the available excerpt, the surname-only search recovered an entry whose given name was blotted out [S17 @2026-11-21].

If a surname search in the M841 postmaster appointments fails, clear both name fields and search the collection by the post office’s locality, county and state [S20 @2026-11-21]. If that fails, browse by state and county, then turn to the office [S20 @2026-11-21], [S21 @2026-11-21]. In the 2022 example from the available excerpt, the office search recovered a candidate under a different surname [S19 @2026-11-21].

Enlarge a suspect M841 appointment entry, compare the handwriting with the rows immediately above and below, and trace any ambiguous stroke to its own row before reading the surname [S22]. In the 2022 example from the available excerpt, the presenter traced a letter in the indexed surname to a neighboring entry [S19].

**Privacy gate:** <!-- privacy-gate: publish --> An added reading becomes alternate information that
other Ancestry users can find by search. Before adding a reading that names or links someone who may
be living, answer the privacy gate in `SKILL.md`. Until each such person has given permission, keep
the reading in the user's local notes instead of adding it. A reading that concerns only people known
to be dead can be added as before.

Once the image shows a mistranscription, the user can add the correct reading using **Add or update information** in the record page’s three-dot menu. Ancestry keeps the original index entry and makes the alternate reading searchable [B33 @2026-11-19]. A hit can therefore match someone else’s reading. Compare the indexed and alternate names with the original image, and cite the wording that appears there [B34 @2026-11-19].

For births, search the parent fields alone, including a mother's-maiden-name field where the
birth index offers one; some early registers omit the child's name, so a search by the child's
name cannot reach those entries. Treat hits as candidates and match them by parents, date and
place ([Joyce Whiting](https://www.youtube.com/watch?v=1LPbDiF6fn8),
[Dave Obee](https://www.youtube.com/watch?v=14LegPypVRM)).

Use [Ancestry's horizontal-search advice](https://help.ancestry.com/hc/en-us/articles/53933305561747-How-to-Search-Ancestry)
and, for the 1950 census, [NARA's household/neighbor search guidance](https://www.archives.gov/research/census/1950/faqs).
These are retrieval pivots; route any identity decision to the evidence-judgment
recipe. Do not add a recovered household to the tree merely because it matches
the search constraints.

A person-search keyword field offers another pivot. Keep only name, birth year and place, and put
one known associated fact in the keyword field instead of a structured field. That fact can be an
address from another record, a city whose county changed, a regiment from a draft card, or an
indexed column without its own field, such as a passenger list's nationality. For a child who may
have lived in an institution, try a status term such as 'orphan' in a census keyword field, then
inspect the full institutional pages. Check that the current collection indexes that text.
Co-residents and listed inmates are leads, not relatives or identifications.
[Judy Sharp's examples](https://www.youtube.com/watch?v=VsbXLVM1-Xk), the
[Swiss keyword tip](https://www.youtube.com/watch?v=ezp_SFmMdYM) and a relayed
[adoptee-research tip](https://www.youtube.com/watch?v=KcsQHKLSjFQ) motivate this. They do not
document current keyword coverage.

### 10. Use the volume's own index and page numbering

**Trigger:** an image collection exists, but its searchable index misses the target
or the material is browse-only.

Choose the relevant locality, year and volume. Inspect the beginning and end for
a handwritten or printed index; follow its name variant and volume/page reference.
Distinguish the book's page number from the viewer's image number, and check the
volume named by the index. Maps can require direct browsing because labels are
initials or are poorly indexed. If the original book has no usable index, specify
a bounded image range and inspect it systematically.

If there is a separate probate index volume, copy its reference to the will book and printed page. Open the named book, verify its heading and locate the actual will before reporting what it says [B5].

If a general name search misses, open Ancestry collection 1268, *U.S., Index to General Correspondence of the Record and Pension Office, 1889–1904* (M686), directly [S24 @2026-11-21]. Follow the browse route from the available excerpt of the 2022 demonstration [S23 @2026-11-21], checking the controls in the current account before selecting the surname range. For a separate name search, use FamilySearch’s index to the same cards [S25 @2026-11-21].

The internal-index method is described by [Lisa Louise Cooke](https://lisalouisecooke.com/2019/11/17/browse-only-records-at-ancestry/).
Use the current viewer's available navigation; the 2019 article's screen positions
are not a current interface contract. Preserve the collection, volume, printed
page and image locator for each candidate.

When a city-directory name search misses a business or proprietor, follow the cue from the available excerpt and inspect the advertisements directly [S32]. Browse the correct edition’s business section and check for advertisements mixed in with residential entries [S34]. Record the edition and page of each hit.

### 11. Turn a census address into a bounded image search

**Trigger:** a household is expected at a known address but the name index fails.

Find a contemporary address in a directory, draft or naturalization record;
resolve it to the enumeration district for the **same census year**; browse that
district's images on Ancestry or at the archive. An earlier address is a lead to
check, and another year's district boundaries are not a substitute.
See [NARA's 1940 address-to-district method](https://www.archives.gov/research/census/1940/start-research).

For the **1950 U.S. census**, inspect sheets numbered 71 onward as well as the
ordinary sequence: these carry people enumerated out of order. The numbering jump
does not establish that images are missing. This is a year-specific convention,
not a rule for every census. Follow any "see sheet / line" reference on the
original schedule and check informant footnotes when a neighbor supplied the
household information. See [NARA's 1950 FAQ](https://www.archives.gov/research/census/1950/faqs).

### 12. Check the extent of a selected application packet

Read the collection's front matter before treating selected pension/bounty papers as a
complete application. Follow the identified applicant and packet boundary into additional
components actually offered; record which papers were inspected and what remains outside
that extent. Preserve the packet locator alongside the individual image locators.
The [selected-papers demonstration](https://www.youtube.com/watch?v=2TlWZ0KvbxU) supplies this
extent check, not a guarantee about present collection coverage or access.

### 13. Carry the original locator beyond Ancestry

**Trigger:** Ancestry has an index entry without an image, a Web Records pointer,
or a different provider finds a page that Ancestry's name search misses.

Copy the collection citation and original repository's locator. For a Web Records
entry, follow the linked source site. For an index-only collection, identify the
custodian and its image or copy-request route; an Ancestry index does not guarantee
Ancestry hosts the image. Access conditions can differ between a personal account
and a library edition. See [Ancestry's library guide](https://help.ancestry.com/hc/en-us/articles/53933331964691-Searching-on-Ancestry-at-a-Library-or-School)
and [Web Records guide](https://help.ancestry.com/hc/en-us/articles/53933331868179-Finding-Records-Online-with-Ancestry-Web-Records).

Search other catalogues for the exact collection or publication title, place and year [B22], [S11]. Record each host, edition and search attempted. Compare the cited original page, memorial identifier or source of the index before counting independent evidence. A shared 1880 census index or two Find a Grave indexes pointing to the same memorial can return the same observation twice [S12], [S13].

**Privacy gate:** <!-- privacy-gate: request --> A personnel-file inquiry sends the person's birth
and religious names to a religious community's archive, and the person or relatives named in the
file may be living; answer the privacy gate in `SKILL.md` before you send it.

If an inspected record supplies a religious name and a named community affiliation,
carry both with that record's locator into an institutional-archive inquiry. Check the
community's actual holdings and present custodian, including a documented later name or
successor archive; ask whether a personnel file is held and accessible for that person.
Keep any returned letters, obituaries or photographs separately identified and verify
their link to the researched person. The [interview with Sunny Jane Morton](https://www.youtube.com/watch?v=hUmGeEvOWbU)
supplies this possible file target. It does not guarantee survival, access or contents.
Keep a birth-name/religious-name link unresolved until supported; do not infer community
membership or parentage from a name form, initials, clothing or Catholic context alone.
The life-stage query in workflow 6 already handles supported name variants.

For England and Wales censuses **1841–1901**, carry the archive series, piece,
folio/page and, where applicable, book reference into a reference search or image
browse. Do not reuse that locator shape unaltered for the household schedules of
1911 or 1921. When a whole locality is missing, check the original archive's
coverage documentation before continuing name permutations.
See [The National Archives census guide, sections 10–11](https://www.nationalarchives.gov.uk/help-with-your-research/research-guides/census-records/).

For a **1921 household schedule**, recover the address panel and instructions as
well as the person rows. Keep the schedule's identity and each image locator;
check that the sides belong together. Findmypast's [RG 15 image guide](https://www.findmypast.com/discover/census-land-and-surveys/census/1921-census-of-england-and-wales-image-browse)
describes the address panel on the front and household details on the back, with
different sequences for longer schedules and attachments. Do not assume that a
fixed previous/next-image offset always retrieves the other side.

If a target volume is missing or blocked before you get a hit, use the collection’s **Source Information** to find the credited repository [S35 @2026-11-22]. Follow the repository pivot from the available excerpt by checking its own catalog for the same publication and adjacent volumes [S32 @2026-11-22]. Verify the edition and coverage there.

If access stops at a paywall, identify the exact collection and its scope from the Card Catalog without a paid membership [S29 @2026-11-22]. Use the signed-out route from the available excerpt if the catalog opens in that state [S53 @2026-11-22]. Carry the title and coverage into the library or repository lookup.

If you are working without a paid membership, open **Free Index Collections**. Use either route from the available excerpt to search the category or open **View all collections included in this search** and select a collection [S43 @2026-11-22] [S44 @2026-11-22]. Check image access separately if an index hit is all you can open.

If the older Ancestry VA index misses a known deceased veteran, check the newer **BIRLS Death File** at BIRLS.org and log the edition searched [S47 @2026-11-22] [S48 @2026-11-22]. The edition comparison from the available excerpt distinguishes the earlier Ancestry release from the newer VA release that covers more years [S46 @2026-11-22] [S47 @2026-11-22]. Treat a BIRLS hit as an index lead to a VA benefits file [S48 @2026-11-22].

For early U.S. Navy service, compare the service period with the muster or pay-roll collection’s date coverage, using the check from the available excerpt of the 2022 USS Constitution search [S49 @2026-11-22]. If the period is outside the collection, use the National Archives’ muster-roll guide to look up the vessel or station and year. Check microfilm T829 for pre-1860 pay rolls [S50 @2026-11-22].

## Check the saved record on each intended person

If you save a recovered record as an authorized tree attachment, list the source's named
people and their intended tree profiles first. Select the facts and people deliberately, then
open each intended profile and verify its source attachment, person-row pairing and resulting
facts against the record. A successful save to one person does not verify all intended people.
Use the current per-person attachment controls to address a missing link; do not
infer a parent-child relationship from household membership. Ancestry documents
[field and person selection](https://help.ancestry.com/hc/en-us/articles/53933314225043-Adding-Records-to-a-Tree)
and [saving a source to another person](https://help.ancestry.com/hc/en-us/articles/53933348187923-Managing-Facts-Events-and-Sources-in-Trees).

In a multi-person record, select the subject’s own row before choosing the destination profile. Check the proposed age, birthplace and parents against that row and the existing sources. Selecting another household member can offer that member’s details for the intended person [B9]. Leave conflicting facts and unrelated attachments in place while resolving the identity.

If an attached record will not open, verify the signed-in account, the collection’s country and the user’s record entitlement before changing anything in the tree. For premium records outside the U.S. Discovery scope, check World Explorer or All Access [S39 @2026-11-22] [S40 @2026-11-22]. A free account can retain the attachment after losing access to the underlying record [S41 @2026-11-22]. If Preserve My Tree is offered, check whether the attachment is in a tree the user owns and whether a partner site supplies the image [S39 @2026-11-22] [S42 @2026-11-22].

## Find a researcher or locality helper

If the next lookup needs a helper and a member directory/profile is available, distinguish
research-interest surname, ancestral place and period from the researcher's declared help
or skills; do not collect the researcher's current location or other personal details.
Check whether a period describes family presence
in a place or an individual's lifespan before using it as a search constraint.
Inspect candidate profiles and return their locators, stated interests/help and relevance
to the lookup. Label them as helper candidates; willingness and competence remain unverified.
Any contact goes through [DNA match outreach staging](dna-match-outreach-staging.md).

These field roles come from [Ancestry's 2012 member-profile demonstration](https://www.youtube.com/watch?v=KRz3hK3KZWc).
Use fields actually exposed in the available view; the demonstration does not establish
that the historical directory or its controls are available in the current account.

## Prompt-craft and search log

> Recover this Ancestry record: [person and event], [known locality and date],
> [collection URL], [queries and settings already tried]. Diagnose the next
> retrieval failure before suggesting another name search. Give three ordered
> searches, each changing a named constraint and stating what its result tests.
> Include a national-collection catalog check, a name-free query and a bounded
> image-browse route where relevant. Record the original locator. Distinguish
> documentation-supported instructions from actions you actually executed.

For each pass, record the collection URL/ID, search date, fields and matching
settings, active result scopes, result or access failure, image range inspected
and next discriminating query. A useful handoff names the next action, rather
than merely reporting that nothing was found.
