---
id: "published-book-catalogue-and-full-text-discovery"
title: "Find a published local history, compiled genealogy or family book across catalogues and full text"
summary: "Find a published local history, compiled genealogy or family book across catalogues and full text."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "PUBLISHED-BOOK-CATALOGUE-AND-FULL-TEXT-DISCOVERY-01", "text": "A miss is only a miss for that tool, query and range. It never establishes that the book doesn't exist or isn't held."}]
handoff: ["hebrewbooks-search-recovery"]
checked: "2026-11-02"
checked_basis: "opened 2026-11-02"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"section": "Record websites, libraries and maps", "group": "Books, periodicals and manuscripts", "order": 42}
---

# Find a published local history, compiled genealogy or family book across catalogues and full text

Use this recipe when you need a published county or local history, compiled genealogy or family book, or a mention of a family inside one. Before reporting "no book exists", "not held" or "no digital copy", work out whether each tool searches cataloguer metadata or OCR full text. Then query each tool in its own terms, check several holders and record what each check covered.

This recipe covers the cross-platform discovery of a book. Some steps overlap with sibling recipes, so use them for those steps:

- Ancestry catalogue-versus-content searches and carrying a locator off Ancestry: [Ancestry search recovery §3 and §12](ancestry-record-search-recovery.md)
- Opening and citing FamilySearch digital books: [FamilySearch workflows §2](familysearch-practical-record-workflows.md)
- MyHeritage name-index versus full-text routes: [MyHeritage record search §10](myheritage-historical-record-search.md)
- Hebrew-language book platforms: [HebrewBooks recovery](hebrewbooks-search-recovery.md), including [bound parts and per-part dates](hebrewbooks-search-recovery.md#bound-parts-and-date-evidence)
- Deciding whether a mention identifies your person: [evidence/proof judgment](evidence-proof-judgment.md)

## Contents

- 1\. Classify the target, then classify each tool
- 2\. Query catalogues the way a cataloguer would describe the item
- 3\. Browse the classification range from a relevant hit
- 4\. Search the full text inside candidate books
- 5\. Carry the confirmed title across holders
- 6\. Open the copy and cite the real host
- 7\. Search photographs and other non-text items through their descriptions
- 8\. Treat snippets, incidental mentions and transcriptions as leads
- 9\. Close with a book-discovery register

## 1. Classify the target, then classify each tool

**Decide whether the target is published or archival before choosing a catalogue.** A presenter from Library and Archives Canada called this the first decision point, because LAC is both a library and an archive and, when she spoke, used a separate catalogue for each [S4]. Those catalogues have since been replaced: Aurora searches LAC's published holdings, and Collection Search covers both archival and published records. Use the institution's current tools, but make this decision first.

**Treat a catalogue entry as holding information only.** The same presenter warned that:

- the library catalogue can show that a newspaper title is held, but it cannot find an individual obituary;
- archival descriptions do not index every file or name [S4].

**Label every tool you plan to use with its search type:**

- **Catalogue search** (WorldCat, a library OPAC) matches only the terms cataloguers assigned. WorldCat does not search a book's contents [S2], [S12]. Some records include a table of contents or a summary, and those are searched too.
- **OCR full-text search** looks for words inside scanned pages, including names absent from the catalogue record. Run a quoted name and spelling variants in Google Books and in full-text collections such as MyHeritage’s Compilation of Published Sources or HathiTrust [S6], [S12], [S15]. Google Books can return a snippet without showing all the matching pages. Record the volume and edition, then obtain the page in an accessible copy.

**Know which search each tool runs before you count a zero as a negative:**

- FamilySearch Books searches the full text of its books as well as their descriptions [S26].
- Internet Archive searches metadata (title, creator, description, subjects) by default. To search the OCR text of books, choose **Text Contents** in the search drop-down or tab (its help pages call the option "Search text contents"), or open `https://archive.org/search?query=TERM&sin=TXT`. A default search can miss a book whose pages contain the term [S27], [S28].

**Test any other tool whose search type you haven't established.** Search a distinctive phrase that you know appears only in the body text of a book the tool holds, such as a name from a page you have already read.

- One hit proves the tool searches page text.
- One miss proves nothing: OCR misreadings can keep a book out of the results for a word it contains. Test two more distinct phrases from different pages.
- If all three miss, read the platform's documentation. Until a hit or the documentation settles it, record the search type as unknown, keep running full-text surname searches there, and log each failed query as a miss for that tool and query only.

On any full-text tool, including HathiTrust, a zero result can come from an OCR misreading. Record the test result.

**Don't compare hit counts across tools.** Tools count different units: Google Books counts books, HathiTrust's full-text search lists individual volumes, and the presenter describes MyHeritage's count as word occurrences. They also search different fields and collections. A catalogue count reflects only how cataloguers described whole items [S12], [S6].

## 2. Query catalogues the way a cataloguer would describe the item

**Don't type the ancestor's name into a catalogue and stop.** A catalogue is arranged by subject categories and is not a word-for-word transcription. Searching by name and finding nothing is the failure this recipe exists to prevent [S2].

**Write the queries as subject descriptions.** For a Joseph City settler, try Arizona history, early settlement and the town or religious community [S2]. A catalogue record can describe the community while omitting the settler. Search that person's name inside the books the subject search identifies.

**Use P. William Filby's *A Bibliography of American County Histories* as another title finder.** The Family History Library's Ohio research outline recommends the 1985 bibliography for local histories [S54]. Carry a discovered title, author and edition into current catalogues, and also search regional titles covering the locality rather than limiting the query to a single-county title [S58].

**Search the catalogue of each library that serves the county, not only WorldCat and the FamilySearch Catalog.** WorldCat shows a library's copy only when the library is an OCLC member, has chosen to represent its collection in WorldCat and keeps the subscription that makes its holdings visible [S48 @2026-11-16]. The FamilySearch Catalog describes material that FamilySearch has collected [S49 @2026-11-16]. A book held only by a local library can be missing from both. Find the online catalogue of the public library or libraries serving the county and run the subject queries there too. The Just Genealogy video on county research makes this a step of its own for that reason (known here only from transcript excerpts; the video itself was not read) [S46† @2026-11-16]. Log each of these catalogues as a separate catalogue-search tool in the register.

**Record WorldCat's holding libraries for each title.** Enter a postal code or location and WorldCat lists the nearest libraries that hold the title [S2], [S6].

**Set WorldCat's location to the county before you read its holdings list.** WorldCat.org lists holding libraries within roughly 200 miles of the location it is given. It asks you to sign in with a free account to see more than the first results, and it does not display every type of library [S47 @2026-11-16]. Enter a place in the target county, not your own or the server's location, and record the location you used.

**Read WorldCat records critically:**

- Compare the full title, author, imprint, date and pagination before counting editions. Two WorldCat descriptions of the same 1964 book about Henry Martin Tanner used different title lengths [S6]. Keep both identifiers and their holdings, and use the title page to decide whether they describe the same edition.

**Expand a WorldCat result to check for a later printing.** Just Genealogy suggests this step, according to the transcript excerpt [S64† @2026-11-18]. Open **View All Formats & Editions** when offered and use the **Sign in** prompt to see the full list [S65 @2026-11-18]. A single search result can group records for different editions and formats [S66 @2026-11-18]. Compare the imprint and date, then check holdings for the printing you need.

**Read Library of Congress-style records critically:**

- Catalogue and finding-aid entries for manuscripts and archival groups describe whole groups of items, sometimes hundreds, not individual items [S3].
- Not all manuscript collections have finding aids. The presenter notes that much of the Library of Congress's manuscript material is still waiting to be catalogued [S3].
- A catalogue that finds nothing is not evidence that the library doesn't hold the material.

## 3. Browse the classification range from a relevant hit

**Use one relevant catalogue hit to find its call-number range.** Then browse that whole range:

- In person, read the shelves item by item.
- Online, use the catalogue's subject or call-number browse.
- Check each volume's index or full text for the surname.

Use a relevant catalogue hit to identify a shelf range. At BYU, a Vermont history volume led to neighbouring books in the social sciences section, where an index pointed to a transcribed probate record [S10]. Note the range and indexes inspected, then verify the transcription against the probate file.

**Repeat the browse under every other plausible classification.** The presenters give several reasons:

- the same or similar material sits in two, three or more places in one library;
- different cataloguers can classify the same item differently;
- some material is uncatalogued [S1], [S9], [S3].

Record each range you browsed and the volumes you actually opened.

## 4. Search the full text inside candidate books

**Map bound parts before recording a passage as absent.** For a HebrewBooks scan, use the
[bound-part and date check](hebrewbooks-search-recovery.md#bound-parts-and-date-evidence):
list each part's title-page viewer page, record the inspected spans and keep the printed
locator, viewer page, part and its dating evidence separately. An opening-page search
does not cover a later part; do not carry the outer title-page year into that part's citation
without evidence that it applies there.

**Within digitised county histories and compiled genealogies, run full-text searches for the surname.** Don't rely on the title, the table of contents or the printed index. The presenter found that many county-history indexes list only the main subject of each biographical sketch [S8].

**Look for people named inside someone else's sketch.** A county-history sketch named Effie Barnes as the daughter of John and Emma even though Barnes was absent from the table of contents. A separate surname hit appeared on a church membership list [S8]. Record the page and whether it names a relative or a church member, then follow the appropriate family or congregation records.

**When the ancestor has no sketch, look for each child's.** A child's biography may name a parent who has no entry [S44]. Search the index and full text for each child and each daughter's husband. A sketch indexed under the husband's name can identify his wife's parents [S8]. Treat the relationship, origin and migration reported by a county history as leads until independently verified [S45]. Follow [section 8](#8-treat-snippets-incidental-mentions-and-transcriptions-as-leads).

**If the immigrant lacks a named sketch, extend the search to documented later descendants.** The Maine examples described in the Bangor Daily News include parents' and earlier generations' origins inside descendants' biographies [S53]. Extract the literal origin statement, whose ancestor it concerns and the relationship asserted. Use it to choose an origin search; a sketch does not guarantee an exact birth town [S57].

**For a late-nineteenth- or early-twentieth-century mug book, check its subscription and biography-selection process.** Frevert describes advance subscribers buying inclusion and sometimes portraits, and subjects editing their sketches [S52]. A missing biography does not establish absence from the locality or lack of status. Treat the published sketch as a contributed account and pursue its named people, places and events in other records [S56].

**Search a compiled-genealogy collection by surname keyword.** A search inside a book titled for another family turned up several familiar names and a possible collateral relative [S5]. Record the page and the proposed relationship separately, then look for each link in independent records.

**Search Google Books for the ancestor's name across all books, not only full-view ones.** For a common name, put the full name in quotation marks and add a place or occupation qualifier [S6]. Record every query string exactly as you ran it.

**Run the same historical name-and-place query under both Books and All in Google Search.** For a deceased ancestor, quote the full name and add the locality. Crume suggests applying **Books** to find published family and local histories and also checking **All** for copies at other hosts such as Internet Archive [S59 @2026-11-18]. Google varies which filters it displays by query, so check the available filters for **Books** [S60 @2026-11-18]. Record the filter with each set of hits and misses.

**For Central and Eastern European directories, yizkor (memorial) books and military lists, search Genealogy Indexer (genealogyindexer.org).** It searches the OCR text of these publications, and its guide warns that the OCR is not fully accurate [S16], [S17]. An empty 'surname near uezd' proximity query is weaker evidence than an empty surname-only query, because an OCR error in either word blocks the match. Also try its OCR-Adjusted matching and wildcards [S17]. If the source list shows no edition for the target guberniya, look for its residents in empire-wide editions and the WWI casualty lists. The page images sit on the holders' websites, and a moved image shows the host's error page, so find the volume at another holder [S18]. Its robots.txt disallows /search/ and /words/ for all robots (checked 2026-11-02), so run searches only in the user's browser [S19].

In these sources a given name is often not spelled out. Genealogy Indexer's guide warns that some give only an initial or an abbreviated given name, and suggests searching for both forms near the surname, as `"j pytel"~3 | "joz* pytel"~3` [S38 @2026-11-12]. Vera Miller adds that in Russian and Ukrainian sources the given name and the patronymic may each be cut to about four letters, or given as initials only [S39 @2026-11-12]. Run the surname with an initial and with a short wildcard stem of the given name, and the surname with the place. Do not read a miss on the full given name and patronymic as a negative, and match an abbreviated hit to the person on the page image, not on the hit line.

**For people who lived in Latvia, search the National Library of Latvia's periodika.lv and its digitised books.** Periodika searches the OCR full text of Latvian periodicals from the 18th century to the present, with a language filter [S20]. It includes Russian-language press of the Latvian SSR, such as the Riga paper *Советская молодежь* (Sovetskaya molodezh) [S21]. Some titles still under copyright are not available in full text [S22]. The digitised books collection holds interwar telephone subscriber lists, such as Jelgava 1932/33 [S23]; use them as an address and occupation lead. OCR can merge adjacent columns into a false match, so confirm every hit on the page image.

**For Pennsylvania, search the published *Pennsylvania Archives*, which is not the Pennsylvania State Archives.** The *Pennsylvania Archives* is a printed set of transcribed records, issued 1838–1935 in ten series: the Colonial Records and the First to Ninth Series. The State Archives is the repository in Harrisburg [S40], [S41], [S42]. The transcribed lists include militia and muster rolls, tax lists, land warrantees, church marriages and baptisms, oaths of allegiance of foreigners arriving at Philadelphia, and governors' papers [S40], [S41], [S42]. The set runs from 1614 (Second Series volume V, on the Delaware colonies) to 1902 (Fourth Series, governors' papers), and the Ninth Series covers 1790–1838, so do not skip it for an event after 1780 [S41], [S42], [S43]. Search its own name indexes as a separate route: the last four volumes of the Third Series index the sixteen volumes before them, volume XV of the Sixth Series indexes the Fifth, and the Seventh Series indexes the names in the first fourteen volumes of the Sixth [S41]. Fold3's description of the set warns that names were misread in transcription, German names above all [S42]. Search spelling variants, and trace each entry you rely on to the original record, as in [section 8](#8-treat-snippets-incidental-mentions-and-transcriptions-as-leads).

Fold3 has page images of all ten series, which you can search by name or browse by series and volume, under the title "US, Pennsylvania Archives, 1660-1780"; the title understates the set's dates [S40 @2026-11-13], [S42 @2026-11-13]. The Pennsylvania Historical and Museum Commission names Ancestry and HathiTrust as other hosts, and its summary of each series helps you choose a volume [S41 @2026-11-13]. Wikipedia's volume list covers only the Colonial Records and the First to Seventh Series; it links the volumes to scans at Internet Archive, Google Books and FamilySearch [S43 @2026-11-13].

**For colonial Virginia, use the Antient Press surname index to choose which volumes to open.** Just Genealogy suggests looking under the surname's initial or using the combined index, according to the transcript excerpt [S61† @2026-11-18]. Heritage Books lists both kinds of entry under [Antient Press Indexes](https://heritagebooks.com/collections/antient-press-indexes) [S62 @2026-11-18]. If you have only a listing, locate the matching alphabetical volume of Ruth and Sam Sparacio's *Virginia County Court Records Surname Indexes* in a library catalogue [S63 @2026-11-18]. Record the surname range you searched and follow each hit into the cited volume to read the abstract.

### Follow a separate all-person index into the biography

When the book's headings or index cover only the principal subjects, look for a
separately held index of people mentioned in the text. ArkivDigital's February 2024
demonstration describes photographed Riddarhuset cards for incidental people in
Lewenhaupt's *Karl XII:s officerare. Biografiska anteckningar* [S24]. The title is
confirmed by the digitized book [S25]. This supplies a route for a woman or another
secondary person who has no officer biography of their own; an officer-name miss
has not searched that separate index.

1. Confirm the book's exact title, author and edition, and establish what its own
   index covers. Locate the separately described card index in the actual catalogue;
   the historical demonstration does not guarantee its current menu or availability.
2. Search the secondary person's supported name forms in that index. Preserve each
   card's literal name, any married-name or other cross-reference, and any stated
   family designation separately. A family reference is another lead, not an identity
   or relationship ruling.
3. Copy the card's cited principal subject, book/volume and page exactly as supplied.
   Keep the card image locator separate from the biography's printed page and viewer
   image. Leave an unreadable or absent locator unresolved instead of inventing a page.
4. Open the referenced biography in the matching edition and read the complete entry
   and its continuation. Verify that the secondary name actually appears and record
   the role and relationship wording the text supplies. Preserve a discrepancy between
   the card and book rather than silently making them agree.
5. Link the card and inspected biography as finding aid and target. A card hit alone
   is not an inspected mention, and the two objects are not independent evidence for
   the biography's statements. Pass any identity or kinship question to the evidence
   workflow.

Add the card-to-biography crosswalk and its retrieval status to the book-discovery
register. The demonstrated names and card/page references have not been independently
verified here; use the procedure to check the actual case rather than copy its example.

## 5. Carry the confirmed title across holders

**Once the exact title is confirmed, search for that title at each other holder.** Check:

- FamilySearch Books
- Internet Archive
- HathiTrust
- Google Books
- WorldCat holdings (on a Google Books page, use the "Get the book" tab and its "Search WorldCat" link under Borrow; the presenters knew it as "Find in a library" [S15])
- a general web search

- the catalogue of each library serving the county ([section 2](#2-query-catalogues-the-way-a-cataloguer-would-describe-the-item))

**Treat each platform's statement as that platform's own knowledge only:**

- **Check the book's viewing options separately from its purchase options.** Google Books showed “No eBook available” for a 1964 volume on Henry Martin Tanner of Joseph City, Arizona. A search by name and place located a complete downloadable copy at FamilySearch Books [S6], [S15]. Record the holding and the extent actually visible at each host.
- **Google Books "preview" or "snippet"** is that platform's access level only. Look up the same book at Internet Archive or HathiTrust [S11].

- **Check the HathiTrust volume's rights and download options [S67 @2026-11-19].** Anyone can read a public-domain Full View item. Visitors can download unrestricted public-domain volumes in full, including many scanned by Internet Archive and items released under Creative Commons. For vendor-restricted scans, visitors can download single pages. Users signed in through a member library can download full public-domain volumes [S67 @2026-11-19]. A member login alone does not open a search-only copyrighted volume for ordinary reading [S67 @2026-11-19].
  - Check the place and date of publication and the item's rights code. HathiTrust's 2026 guidance treats U.S. publications through 1930 and non-U.S. publications through 1900 as public domain. For non-U.S. publications from 1901 through 1930, its default full-view access applies from a U.S. IP address. For 1931 and later it generally treats the item as in copyright, subject to the individual volume's rights. Recheck the current thresholds when repeating a search [S29 @2026-11-19]. The code `pdus` restricts full view to a U.S. IP address, and `icus` to locations outside the U.S. [S30 @2026-11-19].
  - To find volumes outside the default viewable set, choose All Items under Item Viewability [S31 @2026-11-19]. The Bibliographic API documents `usRightsString` as the U.S. user's view. Check the volume page from your own location before recording access [S32 @2026-11-19].

  Google digitised most HathiTrust content, so check Google Books for a locked item, as the presenter does [S7 @2026-11-08]. Google Books also decides what a reader may view from the reader's country and IP address [S33 @2026-11-08].
- **A FamilySearch access-restriction message** (such as "not authorized to view") means the book is restricted, not missing. FamilySearch gives each book one of three access levels, shown in its search result and in the Access Level filter [S34 @2026-11-08]:
  - **Available Online:** searched and viewed online; it can be downloaded and printed [S35 @2026-11-08].
  - **Protected (search only):** searched online, generally not viewable. One current help article says it cannot be viewed; another says it can be viewed but not printed or downloaded [S34 @2026-11-08], [S35 @2026-11-08]. Do not claim that it can be viewed.
  - **Viewable in Library:** searched online and viewed only on site ("from a Family Search Center or Library", in the help's words), without printing or downloading [S34 @2026-11-08], [S35 @2026-11-08].

  Affiliate libraries do not get restricted Books images [S36]. Read the level on the book's search result and confirm that book's access with FamilySearch or the center before you plan a visit. The presenter adds that a "not authorized to view" message can also mean the book's limit on simultaneous viewers has been reached [S6]. Record the exact restriction message you saw.

**Record a view level for each holder checked:** full view or "read", snippet, preview, timed loan, restricted/on-site, or catalogue only. Note which copy and edition you actually read, and the country you searched from.

**Privacy gate:** <!-- privacy-gate: request --> A loan or page-copy request sends the book's title, call number and pages, and the name of any person it mentions, to library staff (the user's own library for a loan, the holding library for page copies). Before a request names a person or asks staff to search for one, answer the [privacy gate](../SKILL.md#privacy-gate) for that person, who may be living.

**For a book held only on paper, record whether the holding copy lends.** Read the holding library's lending rule before you list interlibrary loan as the route. Allen County Public Library, for example, excludes reference materials and rare or unique materials from interlibrary loan, and its Genealogy department lends nothing but offers copying services [S50 @2026-11-16]. Where the copy does not lend, record a request for copies of the pages you need as the follow-up route. The user sends any loan or copy request, including the interlibrary loan in [section 8](#8-treat-snippets-incidental-mentions-and-transcriptions-as-leads). Draft it with the title, call number and pages only.

## 6. Open the copy and cite the real host

**Verify a claimed digital copy.** A result advertising a free copy of the 1964 Tanner book led to advertisements [S6]. Open the title page and the relevant printed page. If neither is available, record the listing as a lead and try a library holding.

**Use an aggregator hit to find the host institution's item, then cite that host:**

- DPLA collects other institutions' metadata and does not hold the objects. Follow the hit to the host's item page for the object, its rights and download options [S7].
- On Internet Archive, compare the date range, volume and sponsor for near-identical titles. When the sponsor field names a library such as Allen County Public Library, use its catalogue or collection index to identify the right item, then match its details back to the scan [S14].

Record both the aggregator locator and the host or sponsor locator.

**Inspect an accessible library copy for handwritten annotations, corrections and inserted material even when you have read another copy of the edition.** UVA's Book Traces account documents such copy-specific additions [S51]. Cite the particular holding copy and page or insertion, and distinguish its printed text from later handwriting. Determine who wrote a note before attributing it to the donor or author [S55].

## 7. Search photographs and other non-text items through their descriptions

Photographs, plates and other items without searchable text can be found only through the descriptions written for them. Ohio Memory searches both OCR text and the descriptive metadata its partners add. A presenter from Ohio Memory gave two tips for that site [S13]:

- use keywords and place names from the item's own period;
- if the "exclude full text sources" box is on the home page, tick it so newspaper OCR hits don't bury these items.

## 8. Treat snippets, incidental mentions and transcriptions as leads

**Use a snippet for triage, not for facts.** A snippet shows only the search term in context on its page. It can tell you which book and page are worth chasing [S6], [S15]. Before you record any fact, find a complete copy and read the whole entry.

**Keep an incidental mention as a candidate.** A presenter warns against copying a surname book into a family file without first verifying that the people are actually related [S12]. Pass identity questions to evidence/proof judgment.

**Privacy gate:** <!-- privacy-gate: request --> An interlibrary loan sends the book's title and call number, and the name of any person the request mentions, to staff at the user's own library and the lending library. If it names a person, who may be living, or asks staff to search for one, answer the [privacy gate](../SKILL.md#privacy-gate) for that person before the user sends it.

**Trace a transcription back to its original record.** For example, a transcribed probate record found in a book should lead you to the original probate record. If the book itself is held only on paper elsewhere, request it through interlibrary loan [S10].

## 9. Close with a book-discovery register

Return one register containing:

- **For each tool:** its search type (catalogue, full text, or unknown if untested) and the result of any body-text test, the exact queries, the classification ranges browsed, and the hits and misses.
- **For each holder:** the title searched, the record identifiers, and the view level or restriction message.
- **For each copy read:** its edition, copy, page and image locator, plus host and aggregator locators.
- **Candidate mentions** still to verify.
- **Follow-up routes**, such as interlibrary loan or the original record behind a transcription.
- **Holders or ranges not checked**, listed separately.

A miss is only a miss for that tool, query and range. It never establishes that the book doesn't exist or isn't held.
