---
id: "familysearch-practical-record-workflows"
title: "FamilySearch record recovery and Tree maintenance"
summary: "Recover FamilySearch catalog, image-only and full-text records, cite the exact view, and repair Source Linker and Family Tree errors."
kind: "platform"
scope: {"platforms": ["familysearch"], "tasks": ["FamilySearch howtos, Catalog/film/DGS crosswalks, unindexed images, Full Text or Simple Search, Source Linker cleanup, profile repair and Source Box reuse."]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "FAMILYSEARCH-PRACTICAL-RECORD-WORKFLOWS-01", "text": "Confirm candidates from the image and context. A name appearing in text does not establish the candidate's identity."}]
handoff: ["ai-for-documentary-records", "evidence-proof-judgment", "gedcom-research-export", "research-documentation", "rootsmagic-tree-reconciliation-workflow"]
checked: "2026-11-12"
checked_basis: "Rechecked 2026-11-12"
capabilities: {"browse": ["familysearch"], "local_script": [], "extensions": ["goldie-may"], "data_transfer": ["export", "link", "publish", "third-party-tool", "upload"], "contact": ["contact"]}
router: {"section": "Record websites, libraries and maps", "group": "Record websites", "order": 37}
---

# Recipe: FamilySearch record recovery and Tree maintenance

## Contents

- Goal
- The failure to prevent
- Before starting
- Nineteen workflows
- Find and maintain Family Tree profiles
- Common working table
- Hand off interpretation

## Goal

Produce a repeatable FamilySearch research packet through missed name searches, image-only holdings,
ambiguous group labels, access restrictions and collaborative Tree corrections. Each workflow saves
an artifact and ends with a check. Start with the historical event, locality and year being researched.

## The failure to prevent

Records, Full Text, Images, Catalog, Wiki and Family Tree serve different purposes. A name-search
miss does not exhaust the holdings; an image ordinal depends on viewing scope; detaching a source
does not necessarily remove facts copied from it. Keep the search surface, identifiers and
inspection coverage with every finding or limitation.

## Before starting

For help reading a record, choose the FamilySearch Community research group for its country or language. The Library’s FAQ directs users to **Groups > Research Groups** and a group’s **Ask a Question** route [S95 @2026-11-16]. **Privacy gate:** <!-- privacy-gate: publish --> Before posting a document link, excerpt or question to FamilySearch Community, answer the privacy gate in `SKILL.md`; the material can name living people. Share only material permitted for that audience. Include the record’s existing image link, locality/date, the precise reading problem and what you have read so far. Keep the reply as an assisted reading to compare with the image [S99 @2026-11-16].

Use authorized access and keep working copies and living-person information private. Before sharing
a report, choose its audience and prepare a redacted version as needed; workflow 17 records and
checks the visibility choice. The cited tutorials date from 2014–2026; confirm the current interface
labels when running a workflow. The artifact columns and checks below are the durable procedure. Tree changes require
an established identity or correction basis; unresolved candidates stay in the working packet.

FamilySearch's Terms of Use (updated 2023-09-01) forbid using software to bulk-download, scrape or
harvest the site's content without prior written permission, and separately forbid circumventing
its controls or usage rules [S60]. So when asked to check every entry in a film, read it image by
image in the user's own session. Do not script retrieval of result lists or image ranges, and do
not use a tool that harvests in bulk. Community-built FamilySearch connectors, such as MCP servers
and API wrappers, are third-party tools. Read a connector's tool schema before relying on a filter, because a
server can drop an argument it does not support, such as a DGS, collection, date or relative,
without warning. Log an empty reply or a lone first page as an interrupted search, not as NIL (see the
[research log](research-documentation.md#research-log)). Use the website for anything the connector lacks; a connected server
does not show that a book is indexed or fully viewable. Check how a connector authenticates: one
that replays the website session may breach the terms. [S60]

**Privacy gate:** <!-- privacy-gate: export --> Syncing Family Tree data into a local file copies the
details of any living relatives in it; answer the privacy gate in `SKILL.md` first.

FamilySearch.org has no GEDCOM export of the shared Family Tree: its own export page says GEDCOM
export is no longer supported there and points to compatible tree-management apps [S71]. Never send
a user to a website "Export GEDCOM" menu. Tree data reaches a local file only through
FamilySearch-compatible software that syncs with the Tree, such as RootsMagic or Ancestral Quest:
import the tree or the ancestral lines into a local file, then match and reconcile individual
records [S74], [S75]. Then run the destination check in
[RootsMagic tree reconciliation § 4](rootsmagic-tree-reconciliation-workflow.md), and build the file
with [GEDCOM export](gedcom-research-export.md). Do not offer the API as a route either. It is
closed to the general public and is not a self-service personal key: beta and production keys need
a compatibility review and signed agreements, and apps that simply copy data out of FamilySearch may not be approved
[S72], [S73].

When a vital assertion lacks expected support in the profile’s ordinary source list, inspect the
contributor’s reason or explanation for that assertion. If that text is collapsed and an
expansion control is available, reveal it. Record any cited book title and page or census year
with the profile/assertion and available contributor/date context. Treat each reference as a
retrieval lead: obtain and inspect the cited page before using its statement, and keep unread or
unavailable pages unresolved. This check does not require changing the profile. [S76]

## Nineteen workflows

### 1. Resolve the event's historical jurisdiction

**Trigger:** You know a place and approximate year, but not which authority kept the records.

1. Follow the Research Wiki country page into the relevant state, county, city or parish.
2. Record the authority responsible in the event's year, the series' start date and the custodian.
3. Follow the locality's record-type links to candidate collections.
4. When formal recording began after the event, queue the locality's named substitutes, such as church, burial or cemetery records.

For early Canadian church or civil records, open **Search > Records > Search by Place** and choose
the standardized province [S133 @2026-11-20], [S134 @2026-11-20]. Inspect its record collections.
Use **Browse all collections** with the province and collection type if you need to narrow the list
[S135 @2026-11-20]. Check the collection's actual locality and dates before recording coverage.

When recording a Tree event, keep the church or cemetery in the place text and choose a standard whose date range covers the event [S21], [S22], [S23]. An English civil registration district such as Ormskirk contained more than the town of that name. Check the record for the parish. Use alternate spellings and nearby names as search leads [S20]. Cite the record and explain the choice before treating two place names as equivalent.

**Artifact:** An event → year → historical jurisdiction → custodian → series/substitute table.

**Check:** The target year fits the actual series. A modern county name or broad collection title does not establish coverage.

**Sources:** [S10](https://familylocket.com/using-the-familysearch-research-wiki-part-2-understanding-locality-pages/), [S11](https://familylocket.com/understanding-the-familysearch-research-wiki-part-4-case-study/).

### 2. Audit holdings after a failed name search

**Trigger:** Records search finds nothing suitable, or you need to know what remains unsearched.

1. Search the Catalog by the standardized locality of a known event.
2. Check parent and historical jurisdictions separately; expand each relevant record category.
3. Inspect each entry's creator, language, notes, dates and individual volume/film rows.
4. Record indexed search, browsable images, digital books and physical holdings as separate access routes.
5. Cross-check Images for relevant groups that have not reached the Catalog.

For the first Catalog inventory, use **Place** and leave **Availability** set to **Any**.
Switch to **Online** only for a digital-access pass, and check each result's access separately.
The **Online** filter can include items whose images are restricted at home [S141 @2026-11-20].

According to a 2022 transcript excerpt, the county inventory demonstration uses **Any** before
working out where each item can be viewed [S140†].

A Catalog place search lists items catalogued at that jurisdiction level, so town registers inside a
county, or a family history catalogued under another locality, may not appear. Also run keyword or
subject searches pairing the county or territory with a record subject (Jewish records), an
occupation term in the record's language (Schäfer) or a surname. For localities with national
letters, search native and plain-letter spellings (ø/o); a Swedish Catalog note filed å, ä and ö
after Z. Record each search in the ledger. A thin entry under one form does not show missing
holdings, a keyword hit shows co-occurring terms rather than the same family, and an extraction index
still needs its original entry. Sources: [Jewish genealogy](https://www.youtube.com/watch?v=VFT8ppcDzWA),
[German periodicals](https://www.youtube.com/watch?v=W_IeM93Lcn4),
[search function](https://www.youtube.com/watch?v=qU4k2sm3crA),
[Danish places](https://www.youtube.com/watch?v=iA8SSSgUzyc),
[Sweden](https://www.youtube.com/watch?v=T_fRRUa4lYY); their 2017–2022 search fields may differ now.

When a citation supplies a FamilySearch Catalog entry number, try the English Catalog address ending in that number. Match the title and volume range before opening a film or image group. In a December 2022 demonstration, number 660634 retrieved Stephen B. Weeks’s index to volumes I–XXV of the *Colonial and State Records of North Carolina* [S105]. The Catalog entry inspected on 18 November 2026 identified the same index [S106]. Use the index to find the volume and page of the underlying record. If direct access fails, keep the entry number and search for the full title.

Treat the coverage ledger as an inventory of FamilySearch's holdings, not of the records that survive
for the place. FamilySearch describes the Catalog as a guide to the records and resources it has
collected, covering materials available in its libraries and centers, physically or as online
digital files [S100 @2026-11-16], [S101 @2026-11-16]. Enter every series and custodian found in workflow 1.
Mark a series the Catalog does not list as not catalogued, not as not held: an image group can
reach Images before the Catalog, so search Images for it first (workflow 2, step 5), then look for
it in the custodian's own catalogue; never log it as nonexistent or as searched. A
[Just Genealogy talk](https://www.youtube.com/watch?v=H4SDdOicYjQ) builds a locality guide from this
search, according to a community reader's extracted quotations; only its title and channel were
rechecked, and its claim that the outline lists everything known to exist is narrowed here to
FamilySearch's holdings [S102† @2026-11-16].

When an inspected entry offers Locality Subject or Subject links, save the exact label and entry
URL and follow a relevant link to related items. Check each candidate's creator, place, dates,
record type and access before adding it to the coverage ledger. A subject heading describes
catalogued material; it does not show that an ancestor appears in it. A search with no useful
result does not exhaust the holdings.

For a digital-book lead, use Books search when available and record the title/edition of the volume
you actually open. Search within that volume; distinguish next-book/result navigation from page
navigation. Confirm the volume and printed page before saving a passage and attaching its citation
to supported facts. Record the item's actual viewing and downloading state in the coverage ledger.
The [Books demonstration](https://www.youtube.com/watch?v=1hPFe9IHyKQ) illustrates the handoff;
use the controls and access information actually available for the item.

If the book is restricted, record that as an access state and look for the same edition at another
holder before citing it; cite the copy you read. Sources:
[digital books 2016](https://www.youtube.com/watch?v=akqZPDs0E8w),
[500,000 books](https://www.youtube.com/watch?v=lqYLQJICzDY).

**Artifact:** A coverage ledger: jurisdiction, series, volume dates, Catalog URL, film/DGS/item, access route, index status and examined/unexamined.

**Check:** Relevant image-only holdings remain outstanding after a negative name search. Never calculate indexing coverage by dividing or subtracting record counts and image counts.

**Sources:** [S12](https://www.youtube.com/watch?v=MMe67JLgS08), [S14](https://www.youtube.com/watch?v=XOnRrT771CY), [S08](https://familylocket.com/finding-your-family-in-familysearch-images/), [S58](https://www.youtube.com/watch?v=LaqAID03XqM), [S59](https://www.familysearch.org/en/help/helpcenter/article/how-do-i-use-the-catalog-to-learn-more-about-the-collections-in-historical-records).

**Sources:** [S100](https://familysearch.org/en/help/helpcenter/familysearch-catalog-learning-center), [S101](https://articles.familysearch.org/hc/en-us/articles/40890974066971), [S102†](https://www.youtube.com/watch?v=H4SDdOicYjQ) (title and channel only; its transcript could not be retrieved).

### 3. Use a photographed index to browse an unindexed register

**Trigger:** The right material is digitized, but a usable searchable name index is missing.

1. Narrow Images by locality, then by town, parish or institution.
2. Look for a separate index group and a photographed index within the volume.
3. Check the index's covered years; carry its entry/page reference to the correct original volume.
4. Browse directly where the index is absent or incomplete, noting relevant relatives and neighboring entries.
5. Log every examined image range and the ranges still outstanding.

Sign in and open **Search > Images** after a name-search miss to find image-only collections.
Start with the standardized place and leave optional filters broad. In **Help me find a
collection**, add the standardized date range only when useful. Check and adjust it in **Filters**
on collection results or **Refine Search** on image-group results [S137 @2026-11-20],
[S138 @2026-11-20]. If a dated small-place search returns zero, rerun it with the dates cleared.
When the period must stay fixed, keep the date range and rerun the search for the surrounding
jurisdiction. Inspect each candidate group's actual creator and locality [S137 @2026-11-20],
[S138 @2026-11-20].

Use **Life Event** first when looking for an event across several kinds of records. A marriage may
be in a volume described as parish records or vital records. Add **Record Type** after identifying
the series you want [S139 @2026-11-20].

Scan thumbnails at the beginning and end of each volume for a title page, contents or index.
Enlarge the opening pages and read the headings to tell entries from an index [S104 @2026-11-20].

If the register includes both event and recording dates, sample entries to establish which date
governs the sequence [S104]. Continue beyond the target event date when entries run by recording
date, following the 2023 advice reported in a transcript excerpt [S136†].

According to Katie Merkley’s advice, determine the arrangement before browsing individual images
[S103† @2026-11-18]. Sample headings and entries to see whether the current item runs by surname,
by date, or by one within the other. Use thumbnails or the image-number field to jump near the
target, then step through the surrounding images individually. Check the ordering again after an
item break [S104 @2026-11-18].

**Artifact:** A browsing log with group/item, index coverage, original page reference, image range, names, findings and remaining work.

**Check:** Inspect the original entry. A photographed book index and FamilySearch's searchable index are different finding aids.

**Sources:** [S08](https://familylocket.com/finding-your-family-in-familysearch-images/), [S12](https://www.youtube.com/watch?v=MMe67JLgS08), [S14](https://www.youtube.com/watch?v=XOnRrT771CY).

### 4. Check the contents behind a misleading image-group label

**Trigger:** A group's title or date range looks irrelevant or ambiguous.

1. Narrow to a tractable locality and retain plausibly relevant groups with uncertain descriptions.
2. Inspect the group's identification image and internal title/divider pages.
3. Survey its image sequence for actual dates and changes of record type; record how much you inspected.
4. Map the ranges containing the target period or series.
5. Search those ranges in detail; base exclusions on inspected contents.

**Artifact:** A group-content map: image ranges, actual dates, internal titles, record types and inspection depth.

**Check:** The tutorial warns that groups labeled as births may also contain marriage or burial material. Inspect the contents before rejecting the group.

**Sources:** [S13](https://www.youtube.com/watch?v=0Qor-XLujh4).

### 5. Carry a Catalog reference into Images and Full Text

**Trigger:** You have a film reference or a known series and want to search its digital group precisely.

1. From the Catalog entry, record physical film number, item and Image Group Number/DGS separately.
2. For an Images identifier search, use the labeled DGS/Image Group Number field rather than the physical film number.
3. Check whether that particular group is available in Full Text; image availability alone does not establish this.
4. Search Full Text with the DGS and a name/keyword; the dated sources also describe comma-separated group numbers.
5. Record both item-view and complete-group image positions when they differ.

Match the external index’s archive, series, accession and file number against the Catalog description. In the Groß Lichterfelde probate search for Klara Ritter, the index specified Landesarchiv Berlin, Rep. 45, Acc. 1232, file 2567, court reference 6 IV 65. The first R volume ran from 14090 to 14135. The researcher reported finding file 2567 after switching to Catalog 286393 [S54]. Check the file’s own identifiers and record any locked images as an access limit (workflow 6).

**Artifact:** A crosswalk: Catalog URL, series/years, physical film/item, DGS, image URL, viewing scope and exact Full Text query.

**Check:** Each DGS belongs to the intended series and period. Confirm the document from its visible heading, date and original page content.

**Sources:** [S15](https://www.youtube.com/watch?v=BGu3IyZTvzU), [S07](https://www.youtube.com/watch?v=4M3h-bSiQGM), [S01](https://www.youtube.com/watch?v=mZc2-Z-TROw), [S09](https://familylocket.com/citing-digitized-records-on-familysearch/).

### 6. Diagnose restricted viewing separately from disabled downloading

For a NARA microfilm publication found through FamilySearch, do not plan a NARA rental: that programme ended 31 July 2009. NARA lists onsite viewing and purchase alternatives [S94 @2026-11-16]. Use the publication title, publication number and reel when seeking a NARA or library copy, and record the actual holder and access outcome [S98 @2026-11-16].

**Trigger:** An image is blocked at home, a restriction symbol appears, or Download is disabled.

1. Save the exact image message (the one shown when the image opens) and the film/DGS/item; distinguish blocked viewing from disabled downloading. The image messages and their access classes are listed after these steps.
2. Inspect Catalog notes and availability information for the authorized route.
3. Confirm that route for the specific item before arranging a library or center visit.
4. Reopen that same item through the permitted route and record the actual outcome.
5. If viewing works but downloading is disabled, inspect and transcribe the displayed record and preserve its citation.

FamilySearch's Help Center lists these image messages and their access classes [S86]:

- **"Images Available", at a FamilySearch center or an affiliate library:** sign in at either.
- **"Images Available", at a FamilySearch center only:** an affiliate library will not show the image.
- **"Images Available", at a third-party subscription site or the legal record custodian:** look there; fees may apply.
- **"Unable to Display Image":** FamilySearch lacks permission to share the image, usually because of the
  record's creator or custodian or privacy law; ask the custodian.
- **"Image Unavailable":** usually temporary, while permissions are updated; retry later.

The Catalog's restricted icon (a camera with an alert sign; older pages describe a key) and its hover
text only flag a restriction [S87]; plan a visit from the image message, not from the icon. Before a
trip to an affiliate library, check that the image message names affiliate libraries: by contract, FamilySearch cannot share every image with them [S88].

If the Catalog entry offers a WorldCat link for other copy locations, follow it and retain
the matching title, creator, edition/volume and listed institutions as retrieval leads.
Check the prospective holder's own catalog or item-specific response for the needed volume,
dates and permitted access before planning a visit or request. Keep an unverified listing
separate from confirmed holdings and an inspected copy. The [Catalog demonstration](https://www.youtube.com/watch?v=0mxyz1mPVpQ)
shows this alternate-copy route; it does not establish that another institution can supply
the particular record or remove the original item's restrictions. [S56]

**Artifact:** An access packet: Catalog URL, identifiers, restriction message, attempted location, permitted route and outcome.

**Check:** An access failure leaves the record unexamined. Some restrictions remain even at center/library computers, as the tutorials warn and the Help Center's classes show.

**Sources:** [S14](https://www.youtube.com/watch?v=XOnRrT771CY), [S13](https://www.youtube.com/watch?v=0Qor-XLujh4), [S86](https://articles.familysearch.org/hc/en-us/articles/41693898891931-What-are-the-image-restrictions-in-Historical-Records), [S88](https://articles.familysearch.org/hc/en-us/articles/41653513329435-Our-affiliate-library-needs-access-to-restricted-images).

### 7. Save a locator that survives item-view renumbering

**Trigger:** You save, cite, transcribe or attach a digitized image.

1. Preserve the complete image URL, including its ARK identifier and viewing query string.
2. Add the relevant people, event date, original page and docket/entry number to the supplied citation.
3. Record film/item and DGS separately.
4. Label each image ordinal with its viewing scope: individual item or complete group.
5. Reopen the saved link and compare the actual document; test both scopes when useful.

Label each saved ARK by type. A record ARK (`…/ark:/61903/1:1:…`) points to an indexed record
[S62], [S63]. An image ARK (`…/ark:/61903/3:1:…`) opens the image viewer, whose index panel can
report that no indexes are available for that image [S61]. An image ARK does not show that an
index entry exists. Never construct a record ID for a line that has no index entry.

**Artifact:** A citation with an identifier crosswalk and any permitted local image/transcription.

**Check:** Save the same document under both viewing scopes. In the Russell County, Alabama, Orphan’s Court docket, image group 005175954, the cover is item 5 image 2 of 158 and complete-group image 830 of 1,138 [S09]. Reopen the citation and match the cover or actual entry. Include the item number or the group total whenever you give an image ordinal.

**Sources:** [S09](https://familylocket.com/citing-digitized-records-on-familysearch/).

### 8. Recover a person missed by indexed Records search

**Trigger:** Records returns no useful match, although relevant material may exist.

1. Open Full Text from the main Search menu, or from the full-text icon in a Catalog entry. It has been a standard search tool since 30 August 2025; it started in FamilySearch Labs in 2024, so older tutorials may show it there [S87], [S89].
2. Start with a surname or distinctive documented name.
3. Compare keyword search with the Name field; recognized-name search can miss words present in the transcript.
4. Try documented initials, abbreviations, spelling variants and name order.
5. Temporarily remove a group restriction, then add place and time filters incrementally.

Switch from Full Text back to indexed Records for the parish and parent searches that follow. For a common surname in English parish registers, search the whole parish through the first census naming everyone. Try the observed spellings and a one-character wildcard, leaving the given name and relatives blank [S50]. Include burials when reconstructing children. A burial explicitly recorded that a child had never been baptized, explaining why a baptism-only reconstruction had missed him [S128]. Group entries provisionally by household and inspect the images before treating identical rows as twins or duplicate filming.

For a couple’s children, search indexed Records with the principal name blank. Enter the father’s name, the mother’s given name and the locality [S28], [S29]. Test place and collection filters separately [S30]. If an exact relative field produces no results, release one field at a time and inspect the indexed spellings [S31]. Compare each candidate’s dates, residence and siblings with the family. Rerun the search when an index gains parent fields [S127], and check for an existing Tree entry before adding a family [S29].

**Artifact:** A query matrix with exact query, search surface, scope, observed count, image links and rejected identities.

**Check:** Confirm candidates from the image and context. A name appearing in text does not establish the candidate's identity.

**Sources:** [S01](https://www.youtube.com/watch?v=mZc2-Z-TROw), [S03](https://www.youtube.com/watch?v=NUwBg94RXdk), [S89](https://www.familysearch.org/en/blog/full-text-search-leaves-familysearch-labs).

### 9. Test Full Text operators with a baseline

**Trigger:** A common name produces excessive results, or spelling is uncertain.

1. Save a plain-query baseline.
2. Compare a quoted name/phrase with that baseline.
3. Test every intended required keyword with its own plus prefix, for example `+John +Smith +Ohio`, as Sorensen describes.
4. Test exclusions and wildcard variants separately, such as `-Ohio` or `Jens?n`; keep wildcards outside quotation marks.
5. After each change, inspect representative hits and record what the syntax actually required.

**Artifact:** An operator comparison table: exact syntax, counts, sample image links and observed behavior.

**Check:** Compare a single required word with every intended term prefixed individually. In Cross’s demonstration, a search for George Stephenson with only `+Mary` returned records mentioning Mary alone [S01]. Sorensen demonstrated a separate plus for each required term [S07]. Inspect matching text beyond the first hits and record what the quoted and unquoted versions returned.

**Sources:** [S07](https://www.youtube.com/watch?v=4M3h-bSiQGM), [S01](https://www.youtube.com/watch?v=mZc2-Z-TROw), [S03](https://www.youtube.com/watch?v=NUwBg94RXdk).

### 10. Turn a page hit into the complete document

**Trigger:** A useful Full Text hit has difficult handwriting, a continuation or an appealing AI summary.

1. Save the original image, citation, DGS and image number before extracting text.
2. Inspect images before and after the hit for continuations and connected pages that omit the search name.
3. Mark the document's start/end and distinguish separate transactions on the same page.
4. Compare material names, dates and legal roles in the AI transcript with the image; preserve uncertain readings.
5. Build any summary from the corrected reading of that document.

Check whether the two sides of a spread were filmed in separate runs. In a baptism-register discussion, a contributor paired image 412 with images 293 and 294 for the pages before and after it. The contributor could not view the baptism itself on FamilySearch and suggested checking Archion [S55]. Use headings, written page numbers and entry sequence to verify each join. Cite each image used.

**Artifact:** An image sequence, document-boundary map, original/corrected transcript and source-linked summary.

**Check:** Every material claim traces to an image. A page summary can combine several documents, and a deed-book entry may be a clerk's copy. FamilySearch's Help Center says transcript editing is disabled while Full Text is updated and may stay unavailable afterwards [S90 @2026-11-12], so no editing button is required by this workflow.

**Sources:** [S01](https://www.youtube.com/watch?v=mZc2-Z-TROw), [S03](https://www.youtube.com/watch?v=NUwBg94RXdk), [S07](https://www.youtube.com/watch?v=4M3h-bSiQGM), [S05](https://familylocket.com/ai-and-familysearch-full-text-search-working-together-to-make-discoveries/).

### 11. Search roles, associates and property clues

**Trigger:** The principal name index omits a woman, witness or person who was not the main party.

1. Search documented name variants in relevant probate, deed and other Full Text material.
2. Record occurrences as daughter, witness, trustee, appraiser or wife releasing dower.
3. Search associated people, distinctive land descriptions, waterways and neighboring property names.
4. Expand into historically relevant adjoining jurisdictions or migration destinations.
5. Keep each person's exact role and pursue separate documents for a proposed relationship.

**Artifact:** A role/FAN table: person, documentary wording, role, date, jurisdiction, image link and next research question.

**Check:** Association is not automatically kinship. Keep stated relationships separate from inferred ones.

**Sources:** [S05](https://familylocket.com/ai-and-familysearch-full-text-search-working-together-to-make-discoveries/), [S06](https://www.legacytree.com/blog/familysearch-full-text-search-finding-hidden-records-with-ai), [S03](https://www.youtube.com/watch?v=NUwBg94RXdk).

### 12. Make Simple Search match the expected record

**Trigger:** A natural-language search is excessive, sparse or irrelevant.

1. Describe person, full geographic location, event and approximate date/range in one concise query.
2. Add relatives or distinguishing facts only when they would plausibly appear in that record.
3. For excessive results, add one relevant detail or apply a record-type filter.
4. For sparse results, remove detail; for irrelevant results, revise the query to match the document.
5. Try historical vocabulary explicitly when semantic matching fails, such as cordwainer alongside shoemaker.

**Artifact:** Query versions, filters, retained image links and a table separating same-named candidates.

**Check:** Inspect the image and compare identities. A second spouse need not occur in a first-marriage record. S02's PID-only search suggestion was untested and is excluded.

**Sources:** [S02](https://www.youtube.com/watch?v=_szy7VbYPjE), [S04](https://familylocket.com/tips-for-using-the-new-familysearch-simple-search-tool/).

### 13. Classify zero results and leave a repeatable retry

**Trigger:** Several sensible query variants still find nothing useful.

1. Check the Full Text collection list for the relevant place, series and period.
2. Cross-check Catalog holdings and separate absent holdings, images without Full Text, restricted access and recognition/query failures.
3. Use indexed Records or browse the image group when the material exists outside Full Text.
4. Save exact queries, filters, groups and a dated coverage observation.
5. Set a revisit date and rerun the saved searches when material may have been added or processed.

Full Text covers only part of FamilySearch's image collections, and more are added over time. For step 1,
use the tool's Find a Collection field or Browse all collections option [S89], [S90].

Where Full Text offers an option to include limited-access content, record its displayed
label and state with the query. The [July 2026 demonstration](https://www.youtube.com/watch?v=gX-d5Szg9XY)
shows restricted items appearing in the result list while their images remain blocked.
Compare the same query with the option changed when useful; a zero in a view excluding
those results does not establish absent holdings. This records visible result scope,
not which material the backend searched. Save any restricted hit's displayed details
and locator as an unviewed lead, then use workflow 6 to check its actual access route.
The hit does not establish the person's identity or the document's contents. Confirm
the control actually offered; the demonstration is not a current interface guarantee. [S57]

**Artifact:** A coverage/retry log: attempted surfaces and queries, available groups, access state, inspected range, outstanding work and revisit date.

**Check:** Zero hits record a query or coverage limitation. They do not establish that the person or document is absent.

**Sources:** [S02](https://www.youtube.com/watch?v=_szy7VbYPjE), [S01](https://www.youtube.com/watch?v=mZc2-Z-TROw), [S03](https://www.youtube.com/watch?v=NUwBg94RXdk), [S05](https://familylocket.com/ai-and-familysearch-full-text-search-working-together-to-make-discoveries/), [S89](https://www.familysearch.org/en/blog/full-text-search-leaves-familysearch-labs), [S90](https://articles.familysearch.org/hc/en-us/articles/41171158944667-How-do-I-use-Fulltext-Search).

### 14. Attach a family record by changing Source Linker's focus

**Trigger:** A proven relative is present in the record but absent from the displayed Tree side.

1. Compare the record image with the intended Tree IDs before accepting the alignment.
2. Align an unmatched name with the established person; do not create a duplicate merely because the person is not displayed.
3. Change the focus person to expose the relevant family: for example, from groom to bride to reach her father.
4. Compare and attach each established match, supplying a reason statement.
5. Recheck the attached people by ID; changing focus alone does not move an existing attachment.

Before using Add, or creating a profile for a name-only person (a bride's father, a tree-extending
hint, a census household member), research them: full name, birth year, a birthplace below country
level, relatives, a married woman's maiden surname and unindexed details on the image. Then search
the Tree yourself and add any existing profile by PID. An empty Possible Duplicates list is not a
negative. Matching uses only the data present. Presenters report that Source Linker checks the
indexed name and does not rerun after corrections. Sparse, married-name or misindexed profiles may
go unsuggested. Vary spouse, parents, place level and name forms. For siblings or a married
woman's children, search surname, place, birth range, father's full name and mother's given name. Log
a record already attached to relatives under other PIDs as a duplicate lead. Hits remain candidates
until records compare them. Sources: [data](https://www.youtube.com/watch?v=90K2gSBXwnI),
[duplicates](https://www.youtube.com/watch?v=I5fM1NbPnWw),
[flags](https://www.youtube.com/watch?v=6jKakuqa6iI),
[merging](https://www.youtube.com/watch?v=1T0bnDx_Ya0),
[prevention](https://www.youtube.com/watch?v=MmtHSlQ34h4),
[Source Linker](https://www.youtube.com/watch?v=48yoEQ0t0ow),
[hints](https://www.youtube.com/watch?v=cCehdMnGJgM),
[skills](https://www.youtube.com/watch?v=ShK2QJAfdN0),
[adding](https://www.youtube.com/watch?v=x270_BdSHaA),
[placeholders](https://www.youtube.com/watch?v=XZp1tyYAJc4),
[Holtby](https://www.youtube.com/watch?v=XcGpE1bxzV8),
[extraction duplicates](https://www.youtube.com/watch?v=pdqsz950wnc),
[misindexed family](https://www.youtube.com/watch?v=EQu60tXwvvA).

Before acting on an unfinished attachment, check what the indexed row represents. A lodger can be a real person outside the family, while an employer or a stray number can be indexed as a person by mistake [S43]. Leave plausible relatives unattached while their identity or living status remains unresolved. A sibling’s recent birth is a reason for caution and supplies no evidence of the other person’s death.

Never set Deceased, a birth year or another required field without evidence just to make an add or
attach succeed. A profile marked deceased normally becomes public in the shared Tree, where any user
can see and edit it [S64], [S65]. The user can set it back to living only if they created the record
and no one else has contributed: Edit → Living → Save makes it private again. Otherwise Save opens a
request form; the user explains the change and submits it, and a FamilySearch system administrator
reviews it [S85].
If the tool cannot express the record or the chosen scope, keep the change queued in the working
packet, and never switch to another tree or scope to make the write succeed.

Before any write, check which tree holds the profile. An uploaded GEDCOM becomes a separate user
tree whose people have their own person IDs; editing them does not change the shared Family Tree
[S78]. Open the person in the uploaded tree and in the shared Family Tree, for example in two tabs,
and compare the IDs. A different ID means a separate copy that changes only that tree. The shared
Family Tree's ID means the edit changes the shared tree. Person IDs distinguish records, not
visibility: check the selected tree, its privacy settings and the person's living or confidential
status before describing an edit as private. Living people in a family group tree are separate records from your own
private copies, and the two cannot be merged [S81]. [S77]

A family group tree does not shield deceased ancestors. Deceased people in it are the public
Tree's profiles, so any user can edit them and those edits show in the group tree; a deceased
ancestor cannot be moved into group-only view. The exception is confidential people copied from
your private list, who are visible only to the group [S82]. What the group adds is shared access
to living people: every member can see and edit living relatives that other members add, and
their stories, photos and recordings can be restricted to the group by setting each Memory
to Private and selecting that group [S82], [S83]. Do not use a group tree
to protect research from outside edits. [S77]

**Privacy gate:** <!-- privacy-gate: link --> Linking a Full Text result sends the record reference, any source notes and the profile association to FamilySearch and the profile’s audience. The linked record can disclose living people. Answer the privacy gate in `SKILL.md` before attaching it.

For a confirmed Full Text hit, open the result's document view and attach the image as a source to
the verified Tree PID. Use that view's attachment control without waiting for an indexed record or
a Source Linker match. Use Source Box if staging the citation for later [S129 @2026-11-20],
[S130 @2026-11-20]. Reopen the intended profile's **Sources** and verify the image and locator.

**Artifact:** An attachment checklist: record/image URL, named person, documentary role, Tree PID, attachment and reason.

**Check:** The right person is attached, not merely a same-named person on the visible screen. The transcript's focus controls are a 2024 observation.

**Sources:** [S16](https://www.youtube.com/watch?v=48yoEQ0t0ow).

For an indexed household record, distinguish the display title from each named participant's
attachment to a Tree PID. Retitling the source does not correct a wrong participant link;
use the identity and copied-fact checks below. This distinction comes from the
[person-page sources demonstration](https://www.youtube.com/watch?v=0G7cwls5N8U), without
adopting its speculation about hint algorithms or a universal source-object structure.

### 15. Detach a wrong source and inspect copied facts

For a compiled-family lead, search the title *Family Group Record Collection—Archive Section, 1942–1969*. FamilySearch’s 2013 guide describes sheets arranged by family surname and then head of family [S93]. Follow the current catalogue or collection entry to the sheets actually available and preserve the submitter and references. Keep the sheet’s family assertions separate from the records it cites [S97].

When following an older CET discussion, look for **User Trees**: the official feedback group announces the retirement of the CET terminology [S92 @2026-11-16]. Use the User Tree route and its controls described below; the older label is not a separate current tree product [S96 @2026-11-16].

**Trigger:** A historical record has been attached to the wrong Tree person.

1. Compare birthplace, parents, dates and other identifying details; save the record URL and affected PID.
2. Detach the demonstrably wrong attachment with a specific explanation of the conflicting identities.
3. Inspect Other Information and other affected fields for facts copied while the source was attached.
4. For each copied fact, check whether other evidence supports it before removing or correcting it.
5. Inspect the remaining sources, facts and change trail.

Before weighing, detaching or rejecting near-identical or legacy sources, classify each one by film,
collection, provider and contributor. City, county and state registrations, or a register and its
bishop's transcript, are separate copies that may differ. Keep distinct applicable copies; detach a
demonstrably inapplicable attachment with the identity conflict recorded, and remove a redundant copy
only after preserving the locators it carries. A double extraction, provider indexes of one image,
or parallel registrations from one informant are not independent corroboration. Treat Ancestral File,
IGI, Pedigree Resource File, Genealogies hits, inherited GEDCOMs and Legacy sources as compiled or
derived claims. Follow an extraction to its register and a submission's patron film to its informant.
Compare a GEDCOM's people with existing profiles rather than bulk-loading it. These leads verify
nothing. Sources: [history](https://www.youtube.com/watch?v=Q4YYIXVwfGE),
[descendants](https://www.youtube.com/watch?v=9Q4qYeK5DTg),
[duplicate sources](https://www.youtube.com/watch?v=IkVGqNpzDUs),
[relationships](https://www.youtube.com/watch?v=PL3LBCW5D6c),
[sources](https://www.youtube.com/watch?v=W-FMXSswYAY),
[Source Linker](https://www.youtube.com/watch?v=48yoEQ0t0ow),
[Q&A #2](https://www.youtube.com/watch?v=Ab53jSpnN6g),
[genealogies](https://www.youtube.com/watch?v=V36wK8VQhu0),
[same name](https://www.youtube.com/watch?v=dlFJ4BKQyOg),
[IGI](https://www.youtube.com/watch?v=HrQhzcfNHmY),
[compiled](https://www.youtube.com/watch?v=1E6zygUP02I),
[Tree history](https://www.youtube.com/watch?v=8Q4gESv4aJ0),
[double extraction](https://www.youtube.com/watch?v=6K9ZF5aunMs). For exporting or importing a
GEDCOM, see [Export research findings to a GEDCOM file without changing what they prove](gedcom-research-export.md).

**Privacy gate:** <!-- privacy-gate: export, upload --> Exporting a GEDCOM from Ancestry or MyHeritage
and uploading it to FamilySearch moves everyone in the tree, including anyone who may be living;
answer the privacy gate in `SKILL.md` first and record the tree's Settings visibility.

For a tree on FamilySearch that only you control, upload a GEDCOM at **Family Tree > Manage
Trees**; export it from Ancestry or MyHeritage, or build it in desktop software [S79]. The upload
becomes a User Tree in the Genealogies collection. You and the people you invite can edit it, and
the shared Family Tree stays untouched [S78], [S84]. In Settings, mark it private to keep it out
of Genealogies search; a public tree shows its deceased, non-sensitive people in search. A private
tree becomes public after two years with no activity; signing in or a contributor's edit resets
that clock [S80]. The tree is a workspace, not evidence: it holds derived claims, like any
compiled tree. Use **Review Matches** as a list of people to compare with existing Family Tree
profiles, check each match against its sources, and do not push the tree's people into the Family
Tree in bulk [S79]. [S77]

Do not use the Help Center's GEDCOM upload route (Search > Genealogies > Upload Your Individual
Tree) for this tree: it adds the file to the Pedigree Resource File, where all FamilySearch users
can search and view it and others cannot change it [S91 @2026-11-12].

Do not enter tentative facts to generate hints. Hints match the data already on the profile, so a
hint that agrees with a guess or a merged-in fact is circular confirmation. Give each reviewed hint an
explicit disposition. Attach a confirmed match. Mark a wrong-person hint not a match, with a reason
naming the PIDs and two or three conflicting facts. If you cannot decide, leave the hint rather than
attaching it. If a detach warning says the record is attached to another profile, compare both
profiles, then merge established duplicates or detach and reattach; do not dismiss an applicable hint
to clear the warning. Review dismissed hints from time to time, because any dismissal reflects the
facts known then. Sources: [merging](https://www.youtube.com/watch?v=1T0bnDx_Ya0),
[record hints](https://www.youtube.com/watch?v=uz2GFqSdOe0),
[helper resources](https://www.youtube.com/watch?v=78j4yZg2a4A),
[best practices](https://www.youtube.com/watch?v=Ry_RUrAQEzw),
[Q&A](https://www.youtube.com/watch?v=cDFvH7i36xY),
[evaluating hints](https://www.youtube.com/watch?v=F_sCTFN-c0o). Labels date from 2017–2026; do not
assume a disposition trains future suggestions.

Before keeping or counting a profile's alternate names, trace each one to a record. A stack of
alternate birth names with no separate birth sources may only reflect repeated submissions. Do not
cite them as several attested spellings, and do not choose among them before finding the birth or
christening record. Record a name the person actually used (nickname, alias, informal or legal
change) as an alternate name or name fact. Keep a clerk's phonetic renderings in a running note, not
as also-known-as names. Neither [Tanner's guide](https://www.youtube.com/watch?v=Y4vkJheOo80) nor the
[name building-blocks talk](https://www.youtube.com/watch?v=QeO_nPCPofI) gives a test for which
category a form belongs to.

**Artifact:** A correction log: record URL, PID, detachment reason, copied facts inspected, corrections and supporting evidence.

**Check:** The Source Linker webinar explicitly says detaching a source does not automatically delete a residence copied into Other Information. Detachment alone is not a complete correction.

**Sources:** [S16](https://www.youtube.com/watch?v=48yoEQ0t0ow).

### 16. Untangle a profile containing several same-named people

**Trigger:** Dates, spouses, children or places suggest that distinct people were merged.

1. Load the full change history to its earliest entries and record surviving/deleted IDs for each merge.
2. Open each deleted person's history; reconstruct its earlier relatives and facts in a comparison table.
   If a nested history is incomplete or unavailable, reconstruct dated spouse/child groups from inspected
   records in a separate comparison. Check the men's identities as well as the women's: an apparent
   duplicate-wife problem may arise from conflated husbands. Repair an established husband conflation
   without treating it as a decision on any still-unresolved wife identity.
3. Research the proposed distinct identities before choosing which IDs to restore; true duplicates stay merged.
4. Using the available restore/unmerge route, restore only the established distinct identities, then allocate facts, sources and relationships to the correct profiles.
5. Add the reasoning/report and an alert note explaining the confusion; record final PIDs in the local comparison document.

Before merging, untangling or relying on a shared profile, read its change log back to the earliest
entries. Record the intended identity: creator, name, vitals, parents and the record it came from (a
marriage-only profile suggests an extracted marriage). Compare candidates and the current profile
against that baseline. Keep the relationships that fit it, and connect detached relatives to their
correct partner. Note when each parent set was added, and look for repeated vital edits without new
sources. Such churn marks a contested profile but does not show which version is right. The cited
presenters describe a 2012 entry credited to FamilySearch as migration from new.familysearch.org
with the contributor withheld, not as verification; check the actual history entry. They also
report that old-system combinations can appear at creation and that earlier-system changes are
absent from the visible log, so verify the history actually available. This baseline method is the
presenters' own practice, and the original identity can itself be wrong. Sources: [merge experience](https://www.youtube.com/watch?v=92Psj3REPs0),
[resolving](https://www.youtube.com/watch?v=lJSDH-L86oE),
[diagnosis](https://www.youtube.com/watch?v=JP3dSfdloK4),
[intended identity](https://www.youtube.com/watch?v=RZeqgY47zdA),
[sticky problems](https://www.youtube.com/watch?v=sxEZVAooC58),
[change log](https://www.youtube.com/watch?v=ZxMCU1RJuyk),
[Hepton](https://www.youtube.com/watch?v=_KXxDk7JNrM),
[double trouble](https://www.youtube.com/watch?v=emOfJia1vuc),
[same name](https://www.youtube.com/watch?v=D-PJUgIDY-M),
[competing parents](https://www.youtube.com/watch?v=9EmwqUrVPwA),
[change frequency](https://www.youtube.com/watch?v=FJD1nd2QOWY).

Diagnose a contradiction before editing it. Any of these suggest a possible bad merge: children after
death, a christening before birth, several values for one event, or two same-year censuses linked to
one profile. One person can, however, be enumerated twice. Do not delete or re-estimate a value just
to clear a warning, because it may be right for one of the combined people. Filter the change log by
the conflicting field to find the edit or merge that introduced it. A relationship whose reason names
two PIDs probably came from a merge (an undocumented observation). In the demonstrated logs, linked
entries showed current names and dates, so reconstruct merge-time content from records, restored
profiles and text-only entries. Read an earlier 'same person' reason as the merger's belief. Cleared
warnings or a high quality score do not verify relationships. Sources:
[merge repair](https://www.youtube.com/watch?v=e3wVkWt581Y),
[diagnosis](https://www.youtube.com/watch?v=JP3dSfdloK4),
[ordinances](https://www.youtube.com/watch?v=EQu60tXwvvA),
[hinting](https://www.youtube.com/watch?v=be-zx7r_hE4),
[change log](https://www.youtube.com/watch?v=ZxMCU1RJuyk),
[conflicting dates](https://www.youtube.com/watch?v=cDFvH7i36xY),
[merge-added relationships](https://www.youtube.com/watch?v=iwYK_cO961s),
[quality score](https://www.youtube.com/watch?v=IYy1m6l8vUQ),
[change log 2020](https://www.youtube.com/watch?v=xvDgxulfroc); a newer log was said to fix the
display, so test it.

Correct known errors on both profiles first, then decide on the evidence. Merge an established
identity. Mark Not a Match only when distinct identities are proved. Otherwise cancel and leave an
alert note saying what was compared and what remains open. For complementary events, such as a birth
on one profile and a christening on the other, look for one record that states both. Write a reason
naming both full names and PIDs as they currently stand, the specific matching or distinguishing
facts, and why any flagged inconsistency is overridden. A reason that names only a data origin or an
action ('GEDCOM data', 'standardized the place', 'same person', 'minor conflicts') carries no
evidence. An automated 'no significant inconsistencies' result is not a reason either. Presenters
offer this as practice, not FamilySearch policy. Sources:
[merge experience](https://www.youtube.com/watch?v=92Psj3REPs0),
[Q&A](https://www.youtube.com/watch?v=6K9ZF5aunMs),
[change log](https://www.youtube.com/watch?v=iwYK_cO961s),
[common mistakes](https://www.youtube.com/watch?v=pbDOvdiSsjk),
[double trouble](https://www.youtube.com/watch?v=emOfJia1vuc),
[reason statements](https://www.youtube.com/watch?v=2NECPoDi-00),
[standards](https://www.youtube.com/watch?v=SjTkwLdqhXI).

The cited presenters describe undo or unmerge as offered only while nothing has changed since the
merge (check the repair route actually offered); otherwise restore the deleted person. Presenters
describe restoration as returning the deleted profile to its pre-merge state while the survivor
keeps the merged facts, sources, relationships and later edits; inspect both profiles after the
actual repair. Where a Merge Analysis link is offered, compare the before and after states. For
merges before 1 August 2016, which reportedly lack the analysis, use step 2 above. List every wrong item on both profiles, then repair in order: merges, relationships, then
facts and sources. Check the spouse, parents and children for newly exposed duplicates, and detach
wrong sources and Other Information from every affected profile. When merging, carry over relatives
whose PIDs differ. Record each affected PID. Sources:
[merge repair](https://www.youtube.com/watch?v=e3wVkWt581Y),
[integrity tools](https://www.youtube.com/watch?v=IYy1m6l8vUQ),
[merging](https://www.youtube.com/watch?v=9o6DTDhrDLo),
[merge talk](https://www.youtube.com/watch?v=1T0bnDx_Ya0),
[sticky problems](https://www.youtube.com/watch?v=sxEZVAooC58). These are 2020–2026 presenter
observations; confirm the current controls and do not assume one repair cleans both profiles.

**Artifact:** A before/after identity matrix, merge chronology, evidence links, restored PID list and correction log.

**Check:** After restoring a profile, verify names, dates, relationships and sources on both surviving and restored profiles. In the 2023 John West reconstruction the author left the Fauquier County man’s disputed birthplace blank and documented his birth-year range separately [S17]. Record the evidence for each correction. An alert note can explain the distinction to collaborators.

**Sources:** [S17](https://familylocket.com/?p=31567), [same-named wives case](https://www.youtube.com/watch?v=0tNC4c2HmQQ).

### 17. Reuse one documentary source across the people it names

**Trigger:** A deed or report belongs on several established profiles and you want a traceable attachment workflow.

1. Create a source with the original record link, citation and the relevant passage.
2. Verify that the created source is available in Source Box rather than assuming it was saved.
3. On each additional established person, use the Source Box attachment route described in the case.
4. **Privacy gate:** <!-- privacy-gate: publish --> Before adding a research report, choose who needs to read it and answer the privacy gate in `SKILL.md`, because the report and its summary may name living people. Keep the sensitive master private; prepare a shareable, redacted version when collaborators need the PDF.
5. Upload the chosen PDF to Memories, explicitly select its visibility, and verify the saved setting before selecting it through Add New Memory Source. Current upload guidance defaults Memories to private; uploading or attaching a source does not establish public visibility.
6. If the PDF stays private, put a self-contained, shareable evidence summary and underlying citations in visible source/reason fields so collaborators can assess the correction without opening the PDF.
7. Reopen each profile's source and confirm the right person and documentary role. Check access from the intended audience's perspective, with authorized access, and record whether that audience can read the PDF or the evidence summary.

**Privacy gate:** <!-- privacy-gate: upload, publish --> An image, document, title, tag or comment can disclose the identities or relationships of living people to FamilySearch or to everyone who can see the Memory. Answer the privacy gate in `SKILL.md` before adding the material or associating it with a profile.

Upload an identified photo or document from the deceased subject’s **Memories > Add Memories**.
Give it a descriptive title and record where the item came from and what supports the identification.
You can contribute to a deceased person’s profile even if they are unrelated to you [S107 @2026-11-18].
Select and verify visibility explicitly. FamilySearch documents a private default [S123 @2026-11-18].

Tag the same Memory for each additional identified subject whose profile it belongs on. Confirm the
profile for every tag, then reopen the Memory and check which people are linked. Use the tags on the
existing item so each person points to the same copy [S107 @2026-11-18], [S124 @2026-11-18].

Post a correction in the existing photo’s **Comments** when you have a basis for challenging a label.
Point to the specific figure and give the proposed name and basis. Attribute a recognition to the
person who made it. Disregard facial resemblance as evidence of identity and leave the tag unchanged
until independent evidence establishes the identification [S107 @2026-11-18], [S125 @2026-11-18].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A record page can send names, dates and relationships of living people to Goldie May and the selected AI provider. The saved source and profile association go to FamilySearch and the target tree’s audience [S131 @2026-11-20], [S132 @2026-11-20]. Answer the privacy gate in `SKILL.md` for both transfers before invoking the command.

With the authorized Goldie May extension already installed, confirm the destination tree and
person ID. Right-click the outside record page and use Goldie May's offered FamilySearch attachment
command [S129 @2026-11-20], [S131 @2026-11-20]. Check the generated citation and description against
the original, and reopen the intended PID's **Sources** to verify the saved link. If the command is
unavailable, use the source-creation route in step 1.

**Artifact:** A source-reuse map: source/image URL, cited passage, named roles, attached PIDs, report version, intended audience, saved visibility, redaction/summary version and reader-access check.

**Check:** Other Tree users can see a private Memory's source information without being able to read the Memory. Verify that the intended audience can inspect the evidence in the PDF or visible summary. Sharing a source does not imply every fact or conclusion applies to every named person. The report is an authored analysis; preserve its underlying evidence.

**Sources:** [S17](https://familylocket.com/?p=31567), [S18](https://www.familysearch.org/en/help/helpcenter/article/how-do-i-upload-photos-or-documents-to-memories), [S19](https://www.familysearch.org/en/help/helpcenter/article/what-are-private-memories).

### 18. Recover a missing Memory from an independent copy

**Privacy gate:** <!-- privacy-gate: upload --> A restored photo or story may show or name living
people; answer the privacy gate in `SKILL.md` before restoring or re-uploading it.

Preserve the affected item's references, associated profiles/albums and surviving title,
tags or text. Locate a separately preserved, authorized original or attributable earlier
copy; check the intended image or complete story before using an available restore/upload
route. Reopen the result and inspect the actual file/text and its associations separately.
Mark unrecovered content explicitly: surviving metadata cannot recreate missing content.
The [media-recovery demonstration](https://www.youtube.com/watch?v=52zi94jhRVQ) motivates this
dispatch; verify current available controls rather than assuming a restore tool, cause of
loss or lossless result.

**Artifact:** A recovery record with the item/copy references, actual file/text inspected,
associations checked and unrecovered content.

### 19. Record a supported relationship without inventing a parent

For two established PIDs and an inspected source stating their relationship, use an actually
offered Other Relationships control when appropriate. Inspect its directional role labels;
retain the exact stated relationship and citation in the reason, then check the saved
association. A generic “relative” label does not itself encode “brother.” Leave an unknown
intermediate parent or uncertain ancestral link unresolved rather than creating a fictional
parent to connect the profiles. The [Other Relationships example](https://familylocket.com/other-relationships-on-familysearch/)
motivates the task; confirm the controls actually offered before any authorized Tree change.

A parent–child link with no type set is reportedly treated as biological, but it is not a sourced
claim. Where records state adoption, step, foster or guardianship, keep each documented parent set:
add biological parents as a separate set rather than replacing adoptive ones. Set the type on each
parent's link separately, because mother and father can differ; the demonstrated edit was made from
the child's side. Give a start date only from its evidence, such as the marriage or the earliest
stating record. Mark inferred dates, cite the records in the reason and recheck both links. A census
'adopted' label does not prove legal adoption, and a census household does not show who raised a
child. Sources: [Q&A 2017](https://www.youtube.com/watch?v=9ZZpLzsGF5A),
[Q&A 2022](https://www.youtube.com/watch?v=K9iQ-kWP46c),
[relationships 2026](https://www.youtube.com/watch?v=PL3LBCW5D6c),
[relationships 2017](https://www.youtube.com/watch?v=TuEwBt1JCiw); confirm which types are
offered. The additional [relationships class video](https://www.youtube.com/watch?v=Y2S38-s3tSc)
was private when checked on 2026-10-22; its title and date were unavailable, and it does not
verify the parent-link types above [S47].

When people repeat in a pedigree or family display, compare PIDs before proposing a merge. A repeated
identical PID means an extra relationship or a loop, not a duplicate. First distinguish valid pedigree
collapse and documented multiple parent sets from erroneous links or unfinished merges, and repair only
an established error. Establish from records which parent–child or couple link is wrong. Walk back from the root person and break the first wrong link
nearest the present, with a reason naming the PIDs. Remove a wrong spouse from the side of the parent
who keeps the children. If a child and one parent repeat with the same PIDs but the other parent's PID
differs, an earlier merge may have been left unfinished, or the child may have a documented second
parent set: merge that parent only after confirming identity.
Recheck the pedigree afterwards. Sources: [Q&A #3](https://www.youtube.com/watch?v=hBeGiubTxWg),
[relationships](https://www.youtube.com/watch?v=TuEwBt1JCiw),
[editing](https://www.youtube.com/watch?v=iUYT0_CvbBU). Their controls date from 2017–2019, and the
2018 dialog removed both parents at once, so check what the current control removes. They do not
address loops created by merges.

## Find and maintain Family Tree profiles

### Find a profile and check its evidence

If the direct-line profile leaves a gap, use **Search > Family Tree > Find by Name** for a deceased
collateral relative or a documented associate such as a witness, godparent, pallbearer or neighbor.
Enter the name and the documented place and approximate birth or death year. Use the returned
profiles to queue sources and connections to verify [S107 @2026-11-18], [S108 @2026-11-18].

Use **Find by ID** when you already have the Family Tree person ID (PID), and save that PID and the
profile URL with your findings. A name search of the public Tree covers profiles listed as deceased.
Log a miss as no public profile found by that search. A living or confidential profile can be outside
that view [S107 @2026-11-18], [S108 @2026-11-18], [S126 @2026-11-18].

Open the full person page from the result. Inspect **Sources** for attachments, **Collaborate**
for notes and discussions, **Memories** for documents and photos, and **Details > Family Members**
for linked parents, siblings, spouses and children. Check those links and the attached records
before accepting the identity shown on the profile [S107 @2026-11-18], [S109 @2026-11-18].

**Privacy gate:** <!-- privacy-gate: publish --> Following exposes the user's FamilySearch account to other followers who open the selected profile’s follower list [S111 @2026-11-18]. Answer the privacy gate in `SKILL.md` before subscribing.

Click **Follow** in the identified deceased person’s page banner when you need alerts about later
changes. Verify the profile on the **Following** list and review changes before updating the working
conclusion [S107 @2026-11-18], [S109 @2026-11-18], [S110 @2026-11-18].

### Add a documented person or extend a branch

**Privacy gate:** <!-- privacy-gate: upload, publish --> Creating people or linking branches sends identifying details and kinship to FamilySearch. Living people in the bridge require permission, and shared Tree profiles and links can be visible to other users. Answer the privacy gate in `SKILL.md` for the particular data, people and audience before saving.

Add a confirmed deceased person to the shared Tree only after searching for an existing profile.
From an established parent, child or spouse, use **Details > Family Members** and the applicable
**Add Child**, **Add Parent** or **Add Spouse** control. Compare the suggested profiles against the
records and select an established match. If the identity and relationship are supported and no match
remains, create the profile through that relationship [S107 @2026-11-18], [S112 @2026-11-18],
[S113 @2026-11-18], [S114 @2026-11-18].

Create an unconnected deceased profile through **Family Tree > Tree > Recents > Add Unconnected
Person** if no supported immediate relative has a profile. Review the duplicate search before
creating the entry. Save the new PID and evidence in the working packet so you can find the profile
again and revisit the unresolved connection [S107 @2026-11-18], [S115 @2026-11-18].

Connect the user’s branch in **Family Tree > Tree** only when the research requires it. Enter the
minimum approved living-person details in the user’s private tree until the line reaches a documented
deceased relative. Link to the corresponding shared profile when the records confirm it. Extend
other supported branches for additional relationship paths and leave an unresolved link open
[S107 @2026-11-18].

### Share living profiles with a family group

**Privacy gate:** <!-- privacy-gate: publish, contact --> Copying profiles exposes the approved living relatives’ details to FamilySearch and every member of the selected group [S117 @2026-11-18]. Invitations disclose the group link to their recipients. Answer the privacy gate in `SKILL.md` for the profile data, group membership and each invitation before sharing.

Create a **Family Group Tree** from **Family Groups > Create Group** and enable its tree option.
Copy only consented living profiles to that group. The group copies have different PIDs and do not
sync edits back to the private copies [S107 @2026-11-18],
[S116 @2026-11-18], [S117 @2026-11-18].

Invite only the approved relatives through a route already permitted under
[Living people](../SKILL.md#living-people). Confirm which group and tree the invitation opens and
record the group's approved membership before relying on that audience [S117 @2026-11-18].

### Ask about a contribution

Trace an unsupported historical assertion to the specific entry under **Sources**, **Collaborate**,
**Memories**, or **Details > Latest Changes > Show All**. Record the assertion and edit date as
provenance. Apply [Living people](../SKILL.md#living-people) to any contributor who may be living
and use only a contact route the user already has [S107 @2026-11-18], [S119 @2026-11-18].

**Privacy gate:** <!-- privacy-gate: contact --> A private first message discloses the sender’s identity and the question to the known contributor through FamilySearch Chat. Follow the consent, disclosure and logging rules under Living people. Keep other living people’s data out of the message and stage any DNA question before outreach.

Draft a private FamilySearch Chat message asking for the source behind that particular contribution
if the user already has that chat route. Send it only with the user's explicit authorization and
log the reply as an attributed lead [S107 @2026-11-18], [S118 @2026-11-18].

### Check a displayed relationship path

On the deceased person’s profile, use **View Relationship** if shown in the name banner. Record
**Relationship Unknown** as no path returned within the viewer’s scope. If the control is absent,
record that it was unavailable. For a displayed path, verify each parent–child link from records
before relying on it [S107 @2026-11-18], [S120 @2026-11-18], [S121 @2026-11-18].

**Privacy gate:** <!-- privacy-gate: publish --> Enabling relationship viewing exposes the user’s relationship path and common ancestors to participating FamilySearch users [S121 @2026-11-18]. Inspect the disclosures in the setting and answer the privacy gate in `SKILL.md` for any living person whose details become visible.

Enable **Relationship Viewing** in FamilySearch settings only when the user authorizes that audience.
For a contributor whose FamilySearch connection the user already has, open the displayed relationship
to inspect the path if both users opted in and the viewer returns one. Verify each link before using it
as evidence [S107 @2026-11-18], [S121 @2026-11-18], [S122 @2026-11-18].

## Common working table

Use one row per query or inspected range. Preserve the distinction between a failed query, an
inaccessible record and an inspected negative result. Use the workflow's additional fields when
recording source attachments, image crosswalks or identity repairs.

| Date | Question | Surface | Locality/series | Catalog URL | Film/item | DGS | Query/filters | Image range inspected | Result/limitation | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | Target event/person | Records, Full Text, Images, Catalog or Tree | Historical place and years | Exact link | Physical film and item | Digital group | Literal query and active filters | Exact range or none | Finding, access block or coverage limit | Browse, compare, obtain access or retry |

## Hand off interpretation

Use your project's research-documentation and source-citation workflows for the complete
plan/log/report loop and citation forms. For transcription uncertainties, read
`genealogy-research-recipes` → `ai-for-documentary-records.md`; for contested identity,
relationship or absence conclusions, read
`evidence-proof-judgment.md`. Carry the images, locators, inspected coverage and candidate comparison
packet into that handoff.
