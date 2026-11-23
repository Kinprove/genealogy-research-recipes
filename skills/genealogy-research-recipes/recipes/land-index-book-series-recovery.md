---
id: "land-index-book-series-recovery"
title: "Recover land instruments through indexes, book series and entry files"
summary: "Trace a land record through both index directions to the right instrument and book, or a federal patent to its entry file."
kind: "records"
scope: {"platforms": [], "tasks": ["grantor/grantee indexes, ambiguous book locators, separate book series, delayed recording, a surname search that missed the alternative index entry, Swedish property-book room/successor references and changed parcel designations, Bavarian property-protocol creators and tax-book identifier/volume handoffs, or cash-sale, bounty-land and homestead supporting packets."]}
privacy: "none"
gates: []
guardrails: [{"id": "LAND-INDEX-BOOK-SERIES-RECOVERY-01", "text": "Keep both index directions, the instrument and recording dates, and the original locator visible, so one missed surname entry or guessed book does not become a false absence."}]
handoff: ["historical-map-record-recovery", "tax-roll-observation-workflow", "us-federal-land-entry-file-recovery"]
checked: "2026-11-05"
checked_basis: "checked 5 November 2026"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Record types in any country", "group": "Burials, directories, land and probate", "order": 216}
---

# Recipe: Recover land instruments through indexes, book series and entry files

## Contents

- Goal
- Before starting
- 1\. Identify how this index actually works
- 2\. Copy the locator, then reconcile the alternative entry
- 3\. Resolve the book series instead of guessing from the number
- 4\. Preserve two dates and close the bounded retrieval audit
- 5\. Carry a U.S. federal patent lead into its separate entry file
- Prompt pattern

## Goal

Follow a land-record lead through the correct index and record-book series.
Keep both index directions, the instrument and recording dates, and the original locator
visible, so one missed surname entry or guessed book does not become a false absence.
For a U.S. federal patent lead, use the separate entry-file workflow below to recover
the supporting packet rather than treating the patent as the complete file.
For Swedish property research, keep registered title separate from use of a farm or dwelling;
follow a supported non-owner lead into the relevant duty, lease or support records.
For a Bavarian farm lead, distinguish the property-protocol creator from the landlord,
and follow the tax books' changing possession, house and parcel identifiers.

## Before starting

Choose a locality, supported name forms and a bounded period. Establish the historical
jurisdiction and present custodian from the locality's record descriptions.
Copy any supplied property description exactly, including directional letters and numbers.

For **U.S. county conveyances**, check county formation and boundary changes for the tract
before choosing index volumes. Land now in County B may have been recorded in parent County A
before B existed. Search the appropriate parent-county series for that period and verify where
those books are held today. Keep later recording dates in mind too; a modern county-only search
does not cover the tract's earlier records. [S35]

If deeds stop in a county while the family still appears on its farm, check for boundary changes even when both counties had existed for years. In one Kentucky account a boundary adjustment moved the farm into the neighbouring county [S57]. Locate the parcel on the dated boundaries in the *Atlas of Historical County Boundaries* and search the receiving county’s indexes from the effective date [S58].

Do not assume a county's older land books are still at the courthouse. Some states take in older local records that a county can no longer keep [S59 @2026-11-14]. In Texas, the State Library and Archives Commission houses such permanent local government records, deeds among them, in regional depositories; a transfer is voluntary, and once records are transferred the state holds title to them [S60 @2026-11-14]. Before reporting a county series lost, look up that state's transfer program and search the state archives' holdings of local records [S59 @2026-11-14], [S60 @2026-11-14].

For a supplied land lead, distinguish an original government disposition from a later
private conveyance before choosing the index. Use the stated issuing authority and
historical holdings descriptions to select the relevant grant/entry series or conveyance
records; verify present custody and index/image date coverage separately. Leave an
uncertain record class unresolved. [Historical demonstration](https://www.youtube.com/watch?v=0fFPtZb5TQw).

If a surviving sale deed has no matching acquisition in the grantee index and the tract may have come from a government grant, search the granting authority's patent or grant index by name, then verify the tract against the deed, following the advice from the available excerpt of each presentation [S154 @2026-11-22], [S155 @2026-11-22]. Use the issuing colony or state's land office series for its grants [S156 @2026-11-22]. For federal public-domain land, start with General Land Office patents and follow section 5 for entries that did not reach patent [S157 @2026-11-22].

For a miner or a mining-claim lead, start with the county recorder's mining-claim records for the
place the ancestor mined, then their filmed or archived copies, rather than relying on federal
land-patent searches [S46]. Carry each claim's location into maps and land records, and read any
miner registration for age, nationality and next of kin [S46].

Calaveras County, California, shows where such books can be found: the FamilySearch Research Wiki
lists its "Mining and Land Claims 1852-1931, and Indexes 1850-1892" with images among the county's
land records [S47 @2026-11-12], and the Calaveras Heritage Council describes the county archives in
San Andreas as holding mining claims with deeds and other county records [S48 @2026-11-12].

Record the historical land district or code separately from the parcel’s county. In Texas, a grant filed under the Robertson land district could concern land in another county [S19]. Use the period district map and the parcel description to choose the county indexes. Leave an uncertain county unresolved.

Transcribe a patent’s dated “of [place]” statement separately from the parcel’s location. Search local records in the stated place for the grantee, keeping same-name candidates open until an independent record identifies the person [S20].

Use the existing platform workflow to open an image-only index and distinguish printed page
numbers from viewer image numbers. This recipe adds land-index, book-series and entry-file controls.
It does not infer kinship, explain property law, draw plats or build a chain of title.

For an original-government grant, link the warrant, survey and patent by their own book and page references and seek any separately described application. Record the warrantee, assignee and patentee, the date of each action and the acreage at each stage. In a Pennsylvania register, the surveyed acreage differed from the quantity warranted [S21]. Resolve the parcel through the underlying records before tracing private conveyances.

Do not assume the warrant, survey and patent were completed before private sales began. A
warranted or surveyed tract may pass through county deeds before a later patent, so the patentee
can be a later holder rather than the first settler. Search county indexes for the tract between
the survey and patent dates. The [Pennsylvania discussion](https://www.youtube.com/watch?v=V0he2PdYk2k)
motivates this order check. [S7]

For a Pennsylvania original grant, search the State Archives' Land Office indexes stage by stage [S61 @2026-11-14]. The Warrant Registers (1733 to about 1957) are the basic index to warrants, surveys and patents for about 70% of the state's land. Each register covers a county as it was at the date of the warrant, so land now in a younger county is in the parent county's register, and entries run by the first letter of the warrantee's surname, then roughly by warrant date [S62 @2026-11-14]. The registers give the patentee but cannot be searched by that name; for the patentee, use the Patent Indexes (1684 to about 1957), arranged by the patentee's surname, which also give the warrantee, warrant date, patent book and page, acreage and county [S62 @2026-11-14], [S63 @2026-11-14]. Before 1733, use the Old Rights registers and the Proprietary Rights Index [S62 @2026-11-14]. Keep the stages apart: an application requests a warrant; a warrant authorizes a survey and starts title but does not convey all rights; the return of survey goes from the Surveyor General to the Secretary of the Land Office; only the patent conveys clear title [S61 @2026-11-14], [S64 @2026-11-14]. The State Archives holds only the surveys made for patenting; deeds and later surveys are with the county Recorder of Deeds [S61 @2026-11-14].

If a deed search leaves a warrant, survey or assignment unexplained, use the grant index to retrieve the original survey and any jacket. Inspect the endorsements for the assignor, assignee, requested grantee and dates. Record each change with its own locator before connecting it to a later patent [S22].

When a tax row supplies an original grantee or abstract number, copy it into the grant search. Record the taxpayer separately and queue later local conveyances. The first tax appearance alone cannot date acquisition or arrival [S23].

If a finding description identifies a related character certificate, queue it separately from
the grant and follow an abstract's ellipsis to the available full item. Keep original,
translation and compiled abstract distinct; extract only the household, origin or oath wording
actually present. Keep a missing field or an unavailable translation unresolved [S23].

When column 8 of the 1850, 1860 or 1870 U.S. population schedule gives a real-estate value, use the presenter's advice from the available excerpt and search for deeds under that person's name [S115]. The column could include property outside the enumeration locality [S116], [S117], [S118]. Search both deed-index directions in the census locality if it fits the other evidence, and follow tax rolls, probate files or deed references to other supported jurisdictions. Keep the parcel unresolved until a record locates it.

If the census places the household in the locality but the ancestor's deed is missing, use nearby census households as leads, following the presenter's advice from the available excerpt [S155]. Search their deeds for adjoining owners or descriptions that locate a candidate tract [S158]. For the 1850 U.S. census, dwelling numbers follow visitation order [S159]. Verify actual adjacency from land records before using the neighborhood to narrow the deed search.

### Tax rolls used for a land lead

Use the [tax roll observation](tax-roll-observation-workflow.md) workflow for the annual series
register and its inspection statuses, separate tax-type searches, reading a volume's arrangement,
literal capacity notations such as *administrator of* or *estate of*, and delinquent addenda.
For a roll used for a land lead, also apply the checks below.

Inventory the volumes and tax classes for each year, including any separately described nonresident or supplementary section. Record each section’s sort key, locator and inspected extent. A real-estate section may be ordered by parcel location even when another section is alphabetical by taxpayer [S16]. Recheck the arrangement in the next year. Keep a surname miss bounded by the sections actually searched.

If the taxpayer is missing, check whether the roll uses the payer’s or estate administrator’s surname. In a reported 1849 Arkansas search, John Cline was filed under W for his administrator Wiseman [S15]. Record both names and their stated roles, the sections searched and any parcel reference. Seek independent records for a death date, sale or family relationship.

### Colony, state and province routes

**Arkansas state dispositions.** Search the Arkansas State Archives' State Land Records by applicant when the tract points to a state donation, swamp-land grant or forfeiture [S163 @2026-11-22]. Carry the applicant, document type, issue date and tract from a lead in MyHeritage's *Arkansas, State Land Registries* into the archive search [S162 @2026-11-22]. Look for the application, patent, proof, forfeited deed or relinquishment separately, and keep the action each document records distinct [S163 @2026-11-22].

**Indiana land-office purchases.** Start with the Indiana Archives' *Indiana Public Lands* index and use the purchaser and tract to find the underlying tract-book or register-of-receipts entry [S165 @2026-11-22]. If starting with a *Land Office Purchases* result from MyHeritage, preserve the stated residence and date as separate fields from the purchased tract [S164 @2026-11-22].

**Connecticut conveyances.** Search the town where the tract lay when the deed was recorded, following the town-level route from the available excerpt [S119 @2026-11-20]. Use that town's deed indexes and books. The town holds the original land records, and the FamilySearch Catalog lists filmed copies by town [S120 @2026-11-20]. A county-only search leaves the town's series unsearched.

**Maryland parcel leads.** When a deed search misses a known historic site, use a modern tax map to locate a candidate parcel, following the advice from the available excerpt [S129 @2026-11-21]. Pan to the known locality in the Maryland Department of Planning's FINDER Online map and turn on Tax Maps or Parcel Boundaries [S132 @2026-11-21]. Use Parcel Boundaries in Baltimore City, which has parcel data but no state tax maps [S133 @2026-11-21]. Record the county, map and parcel numbers where shown. Verify the historic tract against deed descriptions or recorded plats before carrying a modern outline back in time [S133 @2026-11-21].

**North Carolina grants.** Follow a hit in Ancestry’s North Carolina land-grant files [S112 @2026-11-18] to the matching grant in NC Land Grant Images and Data, which includes North Carolina grants for land now in Tennessee [S113 @2026-11-18]. Match the county and file number where available. Open the grant’s Virtual Shuck and look for the survey among the loose-document images even if you already have the envelope summary or patent-book page [S114 @2026-11-18].

Record the county, file and image for the survey actually retrieved. The cross-site match reported in this livestream is known from the available excerpt and still needs confirmation against the grant and survey images [S111].

**South Carolina.** Records were kept by district for long periods, so search a place under both "X District" and "X County" [S65]. The seven judicial districts date from 1769, not 1766 as a community post gives [S65], [S66]. The 1785 act laid out counties inside the districts; in 1800 most counties became districts, and from 1 January 1800 to 16 April 1868 the districts were the principal administrative units while counties survived mostly as geographical names; the 1868 constitution renamed the districts counties [S66], [S67]. For 1769–1799, also search the district that contained the county; for 1800–1868, read "district" as the county-level unit.

For South Carolina colonial and state grants, search the Department of Archives and History's Online Records Index. Its Summary Guide marks the colonial land grants (copy series, 1675–1788), the colonial plat books (copy series, 1731–1775) and the state plat books (Charleston series, 1784–1860; Columbia series, 1796–1868) as in that index [S68 @2026-11-14]. Use a hit as the locator for the original plat or grant, and record the series and item it names.

**Hudson Valley manors, New York.** A tenant on one of the manors, such as Rensselaerswyck, Livingston Manor, Philipsburgh or Cortlandt Manor, held the farm by lease, so expect a lease and rent payments, not a deed of purchase [S64], [S69]. The lease-holding system produced rent ledgers, surveys, receipts, ejectment suits and tax records [S69]. Search those as well as the county deeds.

For Rensselaerswyck, the New York State Library holds the manor's leases, indexed by tenant name and dated 1721 to 1896, most of them from the late 1780s to the early 1800s [S71 @2026-11-14]. Its rent ledgers record dates of property transfers often not found in recorded deeds, subleases and partial interests; few surveys of the West Manor survived the 1911 Capitol fire, so use the ledgers and indexes for those farms [S70 @2026-11-14].

**Hawaii.** One office, the Bureau of Conveyances, records instruments for the whole state [S74 @2026-11-14]. For the earliest deeds, search the FamilySearch collections that the University of Hawaiʻi library guide lists as "Hawaii, Grantor and Grantee Index, 1845-1909" and "Hawaii, Registrar of Bureau of Conveyances, Deed Records, 1846-1900", and open the index image for the deed's book and page [S72 @2026-11-14], [S73 @2026-11-14]. The deed images stop at 1900. Instruments recorded from 1909 to 1991 are found through the Bureau's indexes in its Public Reference Room, in bound libers or on microfilm; those recorded from January 1992 can be searched and bought online with an account [S73 @2026-11-14]. Private land is recorded in two systems, the Regular System and the Land Court, a Torrens registration created in 1903, so find out which system holds the parcel before you close a search [S73 @2026-11-14].

**Upper Canada (Ontario) Crown grants.** Read the grant papers as stages. The settler petitioned the Executive Council; its decision, written on the petition and known as the Order of Council, was the official recommendation for the grant [S75], [S76]. The patent came only after the settlement conditions were met, which could take years, while Loyalist and military "privileged" grants were free of survey and patent fees [S76], [S77]. A petition or an Order of Council is a stage, not title: record its stage and date, and search for the patent separately. Patents are indexed by township for 1795–1850 and by surname for 1795–1825 [S77].

For later Ontario transfers, use the books of the county's Land Registry Office, not a courthouse, and find the lot and concession first [S75], [S78]. The Abstract Indexes list the instruments for a township by lot and concession; the Alphabetical Indexes list them by the parties' names; the copybooks hold the registered instruments, with wills before 1865; and the General Registers, from 1865, hold copies of wills, not deeds [S78]. Take the instrument number from the abstract entry to the copybook [S79].

W. Wesley Johnston's instructions say that FamilySearch has images of the abstract and the instrument books, while ServiceOntario's OnLand shows the abstract (parcel register) books under Historical Books for each Land Registry Office but not the instrument books [S79 @2026-11-14].

## 1. Identify how this index actually works

1. Record the index title, jurisdiction, covered dates and the record series it indexes.
2. Read its opening instructions, subdivision keys and column headings before assuming that
   surnames follow ordinary alphabetical order.
3. Determine whether it is a grantor, grantee, combined/general or tract-based index. In U.S.
   conveyance indexes, **direct = grantor** (conveying party), and **indirect**, **reverse** or
   **inverted = grantee** (receiving party). Check the actual headings and record types: these
   roles also occur in mortgages and other instruments, not just sales. [S36]
4. Where separate grantor and grantee indexes exist, include both in the search plan. Record
   the given-name subdivisions or surname-key procedure the actual volume requires.
5. For a tract-based index, copy the complete available township/range/section or other
   description and identify the volume covering it. Leave missing coordinates unresolved.
6. Record the index date's role when explained: instrument, recording or another date.
   Do not silently use a recording-year range as the transaction-year range. [S1, S2, S4]

**Artifact:** An index-audit row: index ID/title, coverage, direction/system, instructions/key
locator, supported search forms or tract, date role, pages inspected and result.

**Check:** The selected pages follow this volume's rules. A Russell-style or given-name
subdivision index can place a surname somewhere other than the page you first expected.
Russell indexes use surname initials and selected key letters, often with given-name
subdivisions, rather than a single ordinary alphabetic sequence. Single-key and double-key
versions differ. Read the key table printed at the front of the actual volume and follow its
instructions; do not substitute a Soundex code or assume a Campbell or Cott index uses the
same key. [S37]

Do not screen deed-index entries down to land sales. A county's deed books may also hold
mortgages, leases, powers of attorney, sales and manumissions of enslaved people, bills of sale,
indentures and apprentice papers, adoptions, livestock brands, wills and tax lists [S44].
Retrieve each instrument under the target name. Look for releases of siblings’ claims [S44] and divisions of land among heirs [S45]. Extract the parties and their stated interests even when the index gives only one name.

Many clerks' grantor and grantee indexes list only the first-named grantor and the first-named grantee [S80], [S81], [S82]. A co-heir, co-seller or partner named second may have no entry under their own name, and deeds that settle inheritances, estate disputes and partnerships may have several parties [S80]. When the target is missing, search the index under each relative by blood or marriage, and each partner, who could have been named first; if that also fails, read the deed books page by page for the relevant years [S80], [S82].

## 2. Copy the locator, then reconcile the alternative entry

1. For each candidate, save its index image or a permitted transcription and copy the parties,
   instrument type, book/volume, printed page(s), dates and property description actually supplied.
2. Mark unreadable characters rather than choosing the locator that is easiest to open.
3. Use the other index direction when available to compare an uncertain name, book or page
   reference. Inspect neighboring entries to understand the handwriting and column layout.
4. If the locator retrieves the wrong parties, recheck separators and continuation pages. In a reported search two consecutive pages, 4 and 5, had been read as one page number [S2].
5. Keep the first reading and correction in the ledger. When both entries describe the same
   instrument, link them to one candidate instrument rather than counting them as two sources.
   [S1, S2, S4]

**Artifact:** A locator ledger: candidate instrument ID, index-entry IDs, parties, type,
book-series label, book/page as written, tentative reading, correction basis and target status.

**Check:** The fetched document matches the indexed parties and locator. The second index entry
checks retrieval; it does not create independent evidence of the underlying transaction.

Align the entry and page or sequence in parallel registers, translations and compiled indexes. In a Texas index, bracketed notes added by the compiler identify final grants [S24]. Attribute such a locator to the compiler, then retrieve the grant. The repeated entry supplies no independent confirmation of the original statement.

**Maryland prior-deed references.** Start with the latest deed already in hand for the parcel and work backward, following the advice from the available excerpt [S129 @2026-11-21]. Read the “Being the same as” clause or its equivalent for the prior liber and page, then use that locator in the county's volumes in Maryland Land Records [S130 @2026-11-21]. Match the land description at each step. If the reference is missing or leads to a different tract, search the historical grantee index under the grantor's name to find the earlier acquisition [S130 @2026-11-21], [S131 @2026-11-21]. Preserve the locator as written and record any correction separately.

## 3. Resolve the book series instead of guessing from the number

1. Read the index's instrument-type and series columns and the repository's book descriptions.
   The same volume number can be used in different series.
2. Open the specified series and volume, then locate the printed page. Preserve the viewer's
   image locator separately.
3. If the index does not identify the series clearly, list the plausible locally held series
   and inspect the bounded targets or ask the custodian with the complete index reference.
4. Include a miscellaneous series when the index or holdings make it a candidate. A certificate
   or related instrument can be there rather than in the deed book.
5. Inspect the next page for continuation, and verify the parties, instrument type and land
   description before marking the locator resolved.
6. If a secondary lead's location conflicts with the index or document, preserve both forms.
   Compare every directional letter and coordinate; do not silently “correct” the lead to make
   a result fit. [S2, S3]

**Artifact:** A series-resolution row: candidate instrument ID, series/volume/page tested,
result, verified document extent and any conflict between the supplied and retrieved locators.

**Check:** A miss in deed volume 12 does not settle an index reference to an unspecified volume
12. Record which series was tested and what makes an alternative series plausible.

**Clay County, Minnesota.** In FamilySearch's *Minnesota, Clay County Land and Property Records, 1872-1947*, open **Browse All … Images** [S127 @2026-11-21]. Use the separate grantor and grantee index groups, deed books or tax deed book that fit the instrument and date [S128 @2026-11-21]. For a purchase, choose the grantee surname range and take the **Book/Page** reference to the matching deed-book volume [S126 @2026-11-21], [S128 @2026-11-21]. In your own viewer, use the printed page to confirm the location before citing the viewer image number [S126 @2026-11-21].

**Frederick County, Maryland.** Use the *1792–1795* abstracts for libers WR 11 through WR 13, following the lead from the available excerpt [S134 @2026-11-21], [S135 @2026-11-21]. Keep `WR` in the book reference. It identifies the books kept under clerk William Ritchie, and 11, 12 and 13 are deed-book numbers [S135 @2026-11-21], [S136 @2026-11-21]. Take the full liber and page to the Frederick County Court Land Records, Maryland State Archives series C814, where WR 11, WR 12 and WR 13 are C814-41, C814-42 and C814-43 respectively [S136 @2026-11-21]. Search WR 13 itself for 1796 entries because the archive dates that book 1794–1796 [S136 @2026-11-21].

**Belmont County, Ohio.** Follow the deed-abstract lead from the available excerpt to find the book and page [S137 @2026-11-21]. Choose by original volume and recording period. Heritage Books lists A–C (1800–1811), D–F (1811–1817), G (1817–1820) and H and J (1820–1824) [S138 @2026-11-21], with later books K and L (1824–1828) and M and N (1828–1830) [S139 @2026-11-21], [S140 @2026-11-21]. Use the Recorder's **Historic Indexes** when an abstract gives no lead, and take the volume and page to the Recorder's deed images [S141 @2026-11-21].

**Highland County, Virginia.** Follow the presenter's advice from the available excerpt to find both the general deed indexes and the deed books [S121 @2026-11-20]. Look up FamilySearch Catalog entry 533216 for deed books dated 1847–1885 and general deed indexes dated 1847–1981 [S122 @2026-11-20]. In your own account, open the access notice for the index film and the deed film separately. Use a FamilySearch center or affiliate library if the notice allows that location [S123 @2026-11-20]. Affiliate libraries have access to only some restricted films [S124 @2026-11-20]. If the needed film is inaccessible or the index points beyond the listed deed-book years, match the index or book to a reel in the Library of Virginia's Highland County microfilm inventory [S125 @2026-11-20].

**Casey County, Kentucky.** Search party names in both index directions and carry the recording date, tract description and book/page into the deed lookup [S166 @2026-11-22]. For historical deeds, check your eligibility and date coverage in the clerk's CCLIX route before using it [S167 @2026-11-22]. If the online route does not cover the search, use the Casey County deed books listed by the Kentucky Department for Libraries and Archives [S168 @2026-11-22].

**Richmond County, Virginia.** Use the *1714–1715* abstracts identified from the available excerpt as a locator for entries from Deed Book 6 [S169 @2026-11-22]. The publisher describes the volume's deed extracts as pages 194–274 through 1 September 1714 [S170 @2026-11-22]. Use reel 2 for Book 6 and check Book 7 on reel 3 for later recordings, including 1715 [S171 @2026-11-22].

**Richmond City, Virginia.** Use the *1790–1794* Hustings Court abstracts identified from the available excerpt and listed in the local bibliography [S172 @2026-11-22], [S173 @2026-11-22]. Carry the recorded book and page to the city's Hustings Deeds series at the Library of Virginia. For 1792, consult both No. 1 on reel 1 and No. 2 on reel 2 if the abstract gives no definite book reference [S174 @2026-11-22].

**Westmoreland County, Virginia.** Use Michael R. Marshall's abstracts identified from the available excerpt [S175 @2026-11-22]. Select the volume for Deed Book 12 part 3 and Book 13 [S176 @2026-11-22], Book 14 [S177 @2026-11-22] or Book 15 [S178 @2026-11-22]. Carry the book and page of the underlying entry into the Library of Virginia's Deeds & Wills series. The inventory lists all of Book 12 on reel 11, Books 13 and 14 on reel 12, and Book 15 on reel 13 [S179 @2026-11-22].

Search the recorder’s miscellaneous books by family name. In Hamilton County, Ohio, miscellaneous instruments went into deed books until 1859 and then into Miscellaneous Books, with powers of attorney and partnerships among the types given separate books. The county guide lists decrees, marriage certificates, name changes, depositions, dower, wills and patents, and places Army discharges to 1865 in Miscellaneous Book 1 [S83]. An out-of-state divorce decree or medical licence may also have been recorded locally [S84]. Check the book’s own index and the county’s coverage dates.

After you find a deed, read the deeds recorded the same day and several pages before and after it, for other transactions by the same people or for nearby land [S85]. Deeds that one grantor brought in together can be recorded one after another, and Genealogy Tip of the Day warns that some of them may not have been indexed [S86].

If a source identifies a loose or unrecorded deed, record its parties, date and parcel clues. Check the custodian’s finding aid for loose papers separately from the recorded books [S25]. Record which item was requested and which was retrieved. Leave the reason for nonrecording open.

When other records show a transaction for which no deed was recorded, look for collections of unrecorded deeds: published compilations and manuscript collections at historical societies [S87 @2026-11-14], and county archives. The Lancaster County, Pennsylvania, Archives Division keeps a grantor and grantee index of unrecorded deeds; it explains that the hardship of reaching the courthouse left some deeds never recorded and others recorded more than a century after they were drawn up [S88 @2026-11-14]. Some deeds in that collection were recorded later, so check the regular deed index for each hit too [S88 @2026-11-14].

**Loudoun County, Virginia.** If the regular deed books miss a supported transfer, check for a separate series, following the advice from the available excerpt [S155 @2026-11-22]. Search Loudoun's *Partially Proven Wills and Deeds Index*, which includes documents never entered in the regular court records [S160 @2026-11-22]. Check *Deeds Partly Proved* on Library of Virginia reel 161 [S161 @2026-11-22].

When a record-loss report covers the period, do not treat it as absence. Ask the custodian, or
check the holdings description, whether deeds were re-recorded from returned originals, and
search those books and their indexes. Record a re-recorded entry as a later copy, keeping the
instrument date, any stated earlier recording reference and the re-recording date apart. Also ask
whether an abstract or title company keeps its own tract records for the area. Record any copy
obtained as a third-party abstract or copy with its custody stated, and keep any official
book/page it cites as a retrieval lead. The [burned-county discussion](https://www.youtube.com/watch?v=zSx_9MrKP0M)
and [title-plant remark](https://www.youtube.com/watch?v=gssWfSl8JwY) motivate these routes. They
do not show that a given county re-recorded, how such entries are marked, that every original
came back, or that a plant survives, covers the period, is accessible or reaches back to the
original grant. [S5, S6]

Before accepting that "the courthouse burned", find out what was lost: some courthouses lost all their records and others only some, so establish the record types and years destroyed, office by office [S89], [S90], [S91]. Ask the county genealogical society, the public library and the courthouse; search the state archives and state library, which may hold copies of county records, and the National Archives for federal records about the same people [S89], [S90]. Then look for the records made to replace the lost ones. Texas acts of 1874 and 1876 required the re-registration of original deeds whose records had been destroyed [S92]. A North Carolina private act of 1873 provided for restoring Watauga County's burned records, and an owner could instead prove a burned deed in court by their own affidavit and other secondary evidence [S93]. Search the later recording books, the court records of such proofs, and any affidavits or depositions about ownership [S90], [S93]. Record each as a later statement about the earlier instrument, as for a re-recorded deed above.

### Danish property registers: follow the parcel and the earlier folio

For a known historical property, open **Fast ejendom** on [Tinglysning.dk](https://www.tinglysning.dk/) and use its supplied historical address or *ejerlav* and *matrikelnummer* [S142 @2026-11-22], [S180 @2026-11-22]. For pre-digital deed and encumbrance copies, look for the scanned *akt* under **Øvrige oplysninger** [S180 @2026-11-22]. For an older deed or cancelled right, look in the historical *tingbøger* [S144 @2026-11-22]. The digital register shows some historical title entries, and the scanned file can retain some cancelled documents. Other cancelled rights were withdrawn before scanning [S144 @2026-11-22], [S145 @2026-11-22].

In Rigsarkivet's Arkivalieronline, open **Ejendomme → Digitaliserede tingbøger** for 1927–2000. Choose the property's judicial district, then its cadastral district and parcel number [S142 @2026-11-22], [S143 @2026-11-22], [S146 @2026-11-22]. If the leaf is a replacement and the entry predates it, look for the earlier leaf in *omskrevne tingbogsblade*. Look separately under *skøde servitut* for historical deed or easement copies [S143 @2026-11-22]. Use the archive's separate regional guide for South Jutland [S143 @2026-11-22].

Read the opening entries in a *realregister* or *tingbog* as the registrations carried forward at that volume's opening. Read later additions, corrections and cancellations in sequence. If a *tingbog* gives a *gammel folio*, copy it and open that folio in the older *realregister* for the same parcel [S142].

For an earlier parcel search, open **Ejendomme → Realregistre, skøde- og panteprotokoller** in Arkivalieronline [S142 @2026-11-22], [S147 @2026-11-22]. Select the historical authority for the place. For 1805–1919, identify the relevant *herredsfoged*, *birkedommer* or *byfoged*. From 1919 to 1927, identify the judicial district and check which predecessor series it continued for the parcel [S143 @2026-11-22]. Within the authority, use the parish and *ejerlav* to locate the *matrikelnummer* in the *realregister*. If the parcel number is absent there, check a separate *matrikelregister* for the volume and page [S142 @2026-11-22], [S143 @2026-11-22].

Carry a register's volume and page or registration date into the *skøde- og panteprotokol* for its period. For the seller's prior title, read the later deed's recital. Use any prior registration date to search the chronological protocol, and retain the earlier instrument date separately when given. If the registration date is missing but a party name is known, search the authority's *navneregister* where available and follow it into the *realregister* or directly into the protocol [S142], [S143].

If the party's name in the deed index is uncertain, find the historical property in *Historiske Kort*. Read any named cadastral map and look up the parish protocol (*sogneprotokol*) and *hartkornsekstrakt* by parish or *herred*. Compare the names written there with the church-book name, then search each supported form in the *navneregister* [S142 @2026-11-22], [S148 @2026-11-22], [S149 @2026-11-22].

For a historical transfer, read nearby protocol folios for separately entered mortgages, declarations, parcel sales or probate extracts. Follow the *realregister's* separate references as well, including entries for leases, marital or lifetime-support agreements and any other indexed document. In the Ulfborg example the *realregister* points to a baptismal certificate at volume 45, page 115 [S142].

If a register or protocol marks an entry *udslettet*, record the cancellation against the specific registration and copy its date. Follow any separate volume and page to the cancellation entry [S142].

### Turku plot cards: follow the historical source reference

For a known nineteenth-century Turku plot, look up its historical plot number in the topographic section of Dahlström's card index in the National Archives of Finland's Astia service [S151 @2026-11-22]. Follow the plot-number approach from the available excerpt [S150 @2026-11-22]. Keep the stated share, transaction and source citation for each card so a sale of part of a share does not become a sale of the whole plot.

If the cards leave the seller's acquisition unexplained, keep it open. Follow the card's reference into the full *kiinnekirja* (historical title certificate) or the cited court proceedings, following the author's suggestion from the available excerpt [S150]. Read any prior title recital as a lead [S152].

Match the card's record creator and date to the correct holdings. The City of Turku archives hold historical magistrate and town court records [S151 @2026-11-22], [S153 @2026-11-22]. The National Archives of Finland's *Lainhuudot* guide gives separate routes into court series that contain *kiinnekirjat* [S152 @2026-11-22].

### Swedish property books: follow rooms and changed parcel identifiers

**Use when:** an identified Swedish farm lacks a purchase date or its older designation differs from the one now in use. Check the period covered by the books, then use the farm, numbered entry and any reference to a successor volume to trace it [S27].

**Check the books' period and scope first.** Riksarkivet describes its *lagfartsböcker* as books
for rural properties, kept from the 1870s, with information from about 1875 to 1933. Its index of
the books is not complete. If the indexed search misses the property, search the archive's books
directly; for that you need the property's name at the time and its parish. [S56 @2026-11-13]

1. Establish the relevant court archive and volume from the holdings description. Read the
   volume's arrangement and locate the farm and stated property designation. Preserve the
   farm number, parish and any *mantal* or fractional description exactly; do not substitute
   the current designation without a documented connection.
   If a carryover gives a book label that the catalogue does not recognize, compare the
   available spine/title images with the catalogue's series description. Keep both labels
   in a volume crosswalk, with the image that connects them. A later ownership column may refer back to an older book and room under its spine label [S28]. Verify the link against the catalogue, the farm-name alphabetic division and the period covered. The same farm may require successive volumes.
2. Copy the entry's *rum* number, the numbered space in the book, separately from the
   printed page and viewer image. In the predecessor's column, follow a supplied room
   reference backward; in the remarks, follow the reference to the next owner's room.
   Record which column supplied each direction. The
   [Riksarkivet guide](https://riksarkivet.se/resurser/guide-till-lagfartsbok)
   explains these distinct references. [S29]
3. If a margin transfers the entry into a new *lagfartsbok*, copy that book reference and
   locate the corresponding entry there. Verify the property description and any stated
   share at the destination. Keep an uncertain room reading unresolved instead of choosing
   the next plausible name. A successor book's opening year is a locator, not a purchase date.
4. For each entry, preserve applicant, transferor, acquisition type, underlying document
   and its date, application date, granted-registration date and any protocol paragraph.
   Keep a stated half-share as a half-share; do not silently make every entry a whole-farm
   sale. A will or probate reference is a target to retrieve, not permission to call the
   transfer a purchase or infer kinship. [S27, S29]
5. Carry the registration year and act/paragraph reference into the corresponding
   *lagfartsprotokoll* to seek the underlying acquisition document. Record the book entry
   and retrieved protocol/document as linked objects, retaining any conflict between them.
   If the protocol or cited will/probate is unavailable, report that exact missing target.
   Room navigation alone does not resolve the ownership chronology. [S29]

When a designation changes, resolve that break before attaching an earlier book entry to
the modern parcel. The [property-history discussion](https://www.youtube.com/watch?v=HSY904f8uPU)
describes subdivisions, mergers and numbering exceptions; number similarity is not a
parcel link. Nor does the same *mantal* alone establish an unchanged parcel. [S28]

1. Keep the older farm/parish/number and assessed *mantal* alongside the full modern
   designation. In an available register extract, copy *Tidigare fastighetsbeteckning*
   (previous designation), its date and act reference, and *Ursprung* (parent property or
   properties) as separate fields. The
   [register description](https://www.lantmateriet.se/sv/fastighet-och-mark/information-om-fastigheter/Fastighetsregistret/registrets-innehall/)
   identifies these fields; do not assume that every extract supplies the whole history. [S30]
2. Use the cited act identifier to retrieve the relevant *förrättningsakt*. Read its map
   together with the descriptions, decisions and protocol actually present to identify
   the old and new units and the change connecting them. The
   [act description](https://www.lantmateriet.se/sv/fastighet-och-mark/information-om-fastigheter/Forrattningsakter/)
   explains why the register summary and the survey file are separate retrieval targets. [S31]
3. Give each documented subdivision, merger or renumbering its own link. Retain multiple
   parent or successor units where the records show them, including an older designation
   that no longer names an active parcel. Follow supplied references in both directions
   where available; a missing parent record remains a gap. Do not derive a parent by
   deleting digits or force every historical holding into one modern unit. [S28, S30, S31]

To find a historical survey without an act reference, look for a register card under the county, parish, farm and farm number. Copy the farm identifier, act/signum, year and stated survey action. Use these to retrieve the corresponding map and act [S28]. Give each listed subdivision, partition or road division its own row. Record a card hit separately from inspection of the act.

Open the matching act and use its map with the descriptions and decisions already required
above. Compare the card's reference with the act actually retrieved, and retain any missing
text or map as an unresolved component. Date later parcel numbers or annotations separately from the original survey. Numbers added later can look as if they belonged to the original map [S28]. Use
the [map-record workflow](historical-map-record-recovery.md) for this copy's legend and
base/correction dates. An undated added label cannot date that designation or building to
the original survey, and a named feature does not identify its occupant.

**Artifact:** a linked book-entry and parcel-reference ledger:

| Link | Preserve |
| --- | --- |
| Book entry | Court/archive, volume, property wording, room, page/image and stated share |
| Book continuation | Incoming/outgoing room or successor-book reference and verified destination |
| Volume crosswalk | Spine/title label, catalogue series, alphabetic division, period and supporting image |
| Acquisition document | Type, parties, document date, application/grant dates, protocol reference and retrieval state |
| Parcel change | Old/new designations, parent/successor units, act identifier, dated map/text evidence and unresolved links |

**Check:** report which book entries, protocol documents and parcel links were actually
recovered. Keep parcel formation, the underlying acquisition and its registration separate.
This sequence supplies retrieval evidence, not a complete chain of title, a tenure-law
interpretation or proof that an occupant owned the farm.

### When the person used the farm or dwelling without a matching title entry

A *lagfartsbok* follows registered owners, not every tenant or cultivator. A named husband
does not make an unlisted wife absent from the household or settle her interest in the
property [S28]. Keep the title entry and the residence observation as separate records.
If the question concerns a user rather than the registered owner, choose a branch below
only from evidence for that farm's assignment or the dwelling's arrangement.

**A military-assigned farm:** establish the actual assignment before looking for duty-specific
papers. The lecture describes *rusthållsförändringar*, change receipts or lists for a farm
supporting the cavalry, as a route beyond the succession visible in tax rolls [S28]. Ask
for the relevant farm and period in the described *Krigsmanshuskontoret*, regimental or
county *landskansli* holdings; establish each custodian's actual series and coverage
separately. Preserve the named outgoing and incoming holder, date, farm/share, recorded
role and any explicit relationship wording. Keep a holder change distinct from a sale;
the lecture discusses both Crown and privately owned farms. Tax-list proximity does not
establish the relationship, and a narrated example does not verify the people in your case.

If the evidence instead identifies an *officersboställe* or another service holding covered
by the inspection series, seek the described *husesynsprotokoll* for a change of holder.
The lecture points to inspection records under *Krigskollegium* for building-by-building
descriptions and information about users and entry into possession [S28]. Verify the
holding, period and surviving series before requesting them. Record the inspection date,
holder and cultivator separately, the buildings actually described and any stated entry
date; do not give a cultivator the officer's role or treat an inspection as a title transfer.

**A torp or stuga on another owner's ground:** retain the parent farm and the evidence for
the small dwelling's location and use. A missing separate parcel/title entry does not show
that the dwelling did not exist. The lecture suggests *jordtorpsundersökningar* for torps
with labor-rent obligations; this is a population-specific survey, not a register of every
small house [S28]. Check the survey's actual locality, period and included categories before
using it. Record the holding, user, work obligation or payment only as the inspected entry
states them, and keep a survey miss bounded to that coverage.

For a private rental or lease, look for a specific surviving lead among the owner's or
tenant's papers; a title-book miss does not locate those papers. If a record identifies an
*undantag* support arrangement, seek its contract
and any referenced court copy. The lecture notes that copies can occur in *småprotokoll*
[S28]; establish the relevant court and surviving series before treating this as a target.
Record the people, dwelling/use terms, dated obligations and record form actually recovered.
Do not turn a lifetime support clause into ownership of the underlying land, or assume
that a private contract survives or was copied by a court.

**Return:** add the triggering assignment, residence or contract reference to the existing
ledger, with its source, selected branch, custodian/series, requested target, inspected
document and unresolved gap. Stop at the documented result. These routes can recover
statements about use, succession or relationships; they do not establish kinship, farm
tenure, parcel lineage or a complete history of an unregistered dwelling.

### Bavarian farms: select the property-record creator and the book's lookup key

**Use when:** a securely identified farm and bounded period lead to Bavarian property
protocols or tax cadastres. Preserve the farm wording and dated location before selecting
records. The presentations describe historical retrieval examples [S32–S34]; their
archive locations, catalogue screens and access statements are not current instructions.

#### Locate the farm-transfer protocol by its creating court

Keep the named *Grundherr* (landlord), recording court and subordinate *Amt* separate.
The Briefprotokolle presentation describes a landlord consenting to a transfer recorded
by another authority, and court records divided among subordinate Ämter [S32].

1. Use dated jurisdiction descriptions and the court's history to identify the lower
   court responsible for this farm's property protocol. A named monastery or landlord
   supplies a relationship to investigate, not automatically the creating court.
2. Read that creator's finding aid for the relevant *Briefprotokolle*, period and Amt.
   Preserve competing court/Amt candidates where the allegiance is unresolved; a modern
   locality does not choose between them. Take the actual shelfmark from the inventory.
3. Check the volume's beginning and end for an index before deciding how to browse.
   The presentation reports indexes at the back as well as volumes without one [S32].
   Apply the index and locator controls above to the actual arrangement; an index miss
   is bounded by its verified coverage, not a finding that the transfer never occurred.

#### Follow a documented secondary obligation to another institution's book

If a farm owed dues or an endowment to a second court, church or foundation, record that institution, the obligation, date and source. A farm may appear in the recipient’s books even when another lord held it. Check the *Salbuch* for appended copies of earlier deeds [S33].

Use the evidenced recipient to select its property-book descriptions for the farm and
period. Inspect the identified entry and any described appendices or associated deed
copies; keep each copy and its stated original date as a separate retrieval target.
A principal-series miss alone supplies no second institution to search. An entry for
dues is not a title entry, and not every Salbuch has an appended deed collection.

#### Carry the changing identifier through the cadastral books

Use the actual book headings and references at each stage. The Landshut and cadastre
presentations distinguish an initial fixed assessment from chronological changes and
later house-number-partitioned volumes [S33, S34].

1. Establish the farm's historical *Steuerdistrikt* from dated place/atlas descriptions,
   keeping it separate from the modern municipality. Locate the corresponding early
   *Häuser- und Rustikalsteuerkataster* under its actual Rentamt inventory; check later
   *Grundsteuerkataster* descriptions separately. The source's two catalogue placements
   are finding leads to verify, not a fixed present-day menu path [S34].
2. In the initial entry, copy the farm description, recorded person, house number and
   each *Besitznummer* separately. A farm can have several possession numbers. Carry
   those numbers into the matching *Umschreibebuch*: the early example follows them
   chronologically rather than arranging every change under the house number [S34].
   Record the period and extent actually inspected; keep each transfer reference.
3. Seek the corresponding *Liquidationsprotokoll* and map through their actual finding
   descriptions. Compare the text's holding description and parcel numbers with the
   map's identifiers, keeping *Flurnummer*, house number and possession number distinct.
   Use the [map-record workflow](historical-map-record-recovery.md) for the actual legend,
   map date and later annotations. A narration about a map does not establish a parcel link.
4. Follow the references into the later cadastre and its *Umschreibehefte*. Inventory all
   plausible volumes for the period: identical date spans can cover different house-number
   ranges, and the catalogue may omit those divisions [S33, S34]. Inspect their actual
   coverage or index before choosing one; the first same-dated volume may be insufficient.
5. Carry an explicitly recorded old/new house number into the next volume. When a sale
   or subdivision creates another possession number or sends parcels to another entry,
   follow each stated destination and preserve the remaining holding separately [S34].
   Keep multiple resulting units; number similarity or an unchanged farm name is not a link.
6. Copy any actual notary, instrument date and document number from the change entry,
   then use the series and full-instrument retrieval controls above. Keep the cadastral
   entry, underlying act and any later annotation as linked records with their own dates.

**Return:** extend the existing locator ledger with the historical tax district and
creator/Amt, the book and identifier used at each stage, the supporting cross-reference,
and every uninspected or uncertain destination. Report recorded succession statements,
not a verified chain of title or descent. A transfer described as an *Übernahme*, a payment
or continuity of the farm's name does not establish a family relationship.

### Austrian houses: find the owner and manorial lord first

For a house or farm lead in Upper or Lower Austria, look the house up in a regional house-history
database before choosing land books: such map layers and cadastre-based sites give farm or house
names, owners and manorial lords [S49 @2026-11-12]. Carry the named manorial lord (*Grundherrschaft*) into the
search for that lordship's land and transfer records as a lead, as for Bavarian farms above, and
verify each owner and date in those books.

In Upper Austria, open the DORIS theme "Hofnamen und Häusergeschichte". It places the houses and
farms that existed around 1830 on the Urmappe and gives each one's farm names, owner and
*Grundherrschaft*, taken from the Theresian Gültbuch of 1750, the Josephinian Lagebuch of 1786–88
and the Old Grundbuch of 1790–93 [S50 @2026-11-12]; it held about 100,000 houses and farms when
launched in 2022 [S51 @2026-11-12]. It is an ongoing project: the Hausruckviertel data are
incomplete, and houses in Linz, Wels, Schärding, Braunau, Ried and Markt Obernberg are not yet
included, so do not read a missing house as an absence [S50 @2026-11-12]. For Lower Austria, use
Wolfgang Zehetner's "Haus und Hof" at the ÖFR for house owners around 1787 (Josephinian Fassion)
and 1820 (Franciscan cadastre), historical house names and pointers to manorial records. It covers
Lower Austria only, with communities added over time, not all of Austria [S52 @2026-11-12].

### German farms: check the inheritance custom before naming the heir

Before you name a farm heir or look for a sibling's share, find out whether the place passed farms
undivided or divided them. Under *Anerbenrecht* one heir took the whole farm and the others were
paid off well below its value; by area the heir was the eldest or the youngest son, and the
youngest-son custom held, for example, in Ravensberg and the Wesermarsch [S53], [S54]. Do not
assume the eldest son: in Belm near Osnabrück, where at least two sons were living, the youngest took
over a large farm in about three of four cases, and small farms did not follow the custom [S55].
Look for the non-heirs elsewhere: in an Emsland account, sons who did not inherit sought a bride
who held a farm, often taking the farm's name, or became craftsmen, farm servants or *Heuerleute*
[S53]. In divided-inheritance (*Realteilung*) areas, which the Münster lecture lists as including
Württemberg, Baden, Hesse, the Rhineland, southern Westphalia and Lower Franconia, expect the land
to be split among all the heirs [S55]. The same lecture calls this contrast schematic, so let the
local transfer records decide [S55].

## 4. Preserve two dates and close the bounded retrieval audit

1. From the retrieved document, record the instrument's stated date and the recording date
   separately. Keep another dated action, such as acknowledgment, in its own field when present.
2. Compare the dates with the index's ordering. If registration occurred later, extend the
   index search by an explicit, recorded range when the question requires it.
3. Confirm whether you examined an original instrument, a recorded copy in a book, or only
   an index/abstract. Do not describe a book image as the original signed instrument by default.
4. Reconcile the index-audit and locator ledgers: each relevant candidate is resolved,
   uncertain, unavailable or assigned a next action.
5. Report searched index directions, date ranges, key/page coverage and book series.
   A completed bounded audit does not prove that no unrecorded or differently held instrument exists.
6. Hand retrieved documents to the established abstracting and evidence/proof workflows.
   Keep chain-of-title or kinship conclusions outside this retrieval result. [S1, S2, S4]

**Artifact:** The index audit, corrected locators and instrument inventory:

| Field | Preserve |
| --- | --- |
| Instrument ID | Linked index entries and resolved book-series reference |
| Parties and property | Exact names, roles and property description as supplied |
| Dates | Instrument, acknowledgment if present, recording; each with its wording |
| Record form | Original instrument, recorded book copy, index or abstract actually viewed |
| Document extent | Printed pages and image locators, including continuations |
| Retrieval status | Verified target, uncertain identity/locator, unavailable or next action |

**Check:** A later registration does not move the underlying transaction to that year.
Do not fill an absent date from an index column whose meaning remains unknown.

Sort sales by instrument date and record the filing date separately. Deeds entered the books as delivered to the recorder [S94], [S95]. If an instrument is missing near its date, search again around a resale, estate settlement, court case, child coming of age or surviving parent’s remarriage [S85], [S94], [S95]. For a power of attorney, also check the date the resulting deed was filed. A relinquishment could surface when the land became the subject of litigation in another state [S96].

When several deeds concern the same landowner and the expected instrument is missing, use an acquisitions-and-disposals table, following the presenter's advice from the available excerpt [S155]. Match rows by legal description first [S158]. For each side record acreage or fractional interest, date, other party, means of transfer and locator. Use an unmatched tract or share to target the next search. Check splits and conflicting descriptions before treating an acreage imbalance as evidence of a missing transfer.

Check how, where and when a deed had to be acknowledged. When acknowledgment took place in open court, the grantor had to wait for a session [S97]. In Burke County, North Carolina, the January 1807 minutes preserve an acknowledgment of a July 1805 deed even though the deed books were destroyed [S98]. Search the later sessions before interpreting a delay as absence or dispute.

Compare the opening roster with the names and roles at execution. In one reported deed a woman signed even though she was omitted from the opening list [S26]. Preserve both readings and page references. Verify the role independently before inferring widowhood, incapacity, death or kinship. Signatures copied into a recorded book may be in the clerk’s hand [S85].

Before reporting a grantor's wife absent from a sale, read the recorded instrument through its
acknowledgments for a release or separate-examination clause. If none appears, search later index
entries over an explicit, recorded range for a separately recorded release or disclaimer deed,
which may have been made years after the sale [S4], and link it to the sale's instrument ID.
Record her name as written, any date the release states, and any stated source of her interest,
such as inheritance. The [disclaimer-deed explanation](https://www.youtube.com/watch?v=Gci5qXFBtrQ)
and [release-of-dower discussion](https://www.youtube.com/watch?v=CjjD9mI_dY8) motivate this
check. Release requirements varied by state. Neither a missing release nor the witnesses' names
establish her death, marital status or kinship. [S9]

For North Carolina deeds from 1784 to about 1867, The Legal Genealogist expects formal dower relinquishments to be mostly absent, because dower then reached only land the husband owned at his death; do not read a deed without one as showing that the seller was unmarried or widowed. [S39] North Carolina case law confirms that limit on dower and says an 1867 act extended dower to land held during the marriage unless the wife joined the deed with privy examination. [S40] The 1784 starting date was not independently verified, and no independent source confirmed how often relinquishments actually appear in these deeds, so treat their absence as a lead only. [S39]

A grantor/grantee index often names only the parties to an instrument. Determine from the index
itself whether it covers only parties or also witnesses, adjoiners, heirs or other people named in
the text, and report a negative search within that verified scope. Use
[FamilySearch Full-Text Search](https://www.familysearch.org/en/search/full-text/) where it covers
the relevant deed images, including for witnesses and adjoiners omitted from party indexes.
Read instruments already in hand for those people too, and verify any search hit on the image. [S38] The
[full-text search remark](https://www.youtube.com/watch?v=kFxsAw8HHAs) motivates this
distinction. Full-text coverage and machine reading vary, so a full-text miss does not prove
absence either. [S8]

On surveys and grants, read a name marked C.C. or C.B. as a chain carrier or chain bearer, who carried the surveyor's measuring chain, and S.C.C. as a sworn chain carrier [S99], [S100]. Party indexes do not list them, so read the survey itself. Chain carriers were often relatives of the person for whom the land was surveyed, such as sons or brothers [S100], [S101]; record them as associates to test, not as kin. Do not infer legal age from the label alone: a Tennessee glossary says a plain C.C. could be under legal age while a sworn carrier would have reached it, and a Cumberland County, North Carolina, guide says male chain carriers had to be 14 or older [S100], [S101].

If other records place land with the person and both indexes miss the expected transfer, read the surviving deed books page by page for the relevant period [S41], [S42]. A Winston County researcher reported finding deeds despite a negative search in both indexes [S43]. Record the books and years actually read before reporting the result.

Before that page-by-page read, test the two routes by which land often left an owner without a deed in the owner's name.

- **Title by will or descent.** If the last recorded deed predates several later owners, search the probate records of each in turn. A series of wills can account for successive transfers without another recorded deed [S102]. Intestate descent also may leave no separate instrument of transfer [S82].
- **A forced sale.** Land sold for unpaid taxes or to satisfy a judgment was conveyed by an officer, so the deed is not under the owner's name in the grantor index [S82], [S103], [S104]. Search the grantor index under "Sheriff" and under the sheriff's own name, look for separate sheriff's or treasurer's deed books, such as the Laramie County, Wyoming, treasurer's deeds for property sold at tax sales, and look for the sale in the court records [S82], [S104], [S105].

When tracing a mortgage payoff, search the release or satisfaction index and read the original mortgage entry through its margins. Pennsylvania provides for indexing the satisfaction and annotating the mortgage, in the margin when the record format permits [S107]. Check the left-hand column where a clerk could enter payment [S104]. If no release appears, search for a foreclosure in court and for the resulting sheriff’s deed or other sale in the deed indexes [S104], [S106]. Document the missing release and leave the payment status open.

When an original deed survives outside the recorded book, read any clerk's endorsement giving
the book, page or acknowledgment date. Use it to find the recorded copy, then compare the two
texts instead of assuming the transcription is exact. Where a court ordered recording, search the
order or minute book for that entry and keep its date in its own field. The
[deed-process explanation](https://www.youtube.com/watch?v=gWPPN9DUUSc) motivates this crosswalk.
Endorsement and court-order practice varied, and the source shows no example endorsement. [S4]

## 5. Carry a U.S. federal patent lead into its separate entry file

**Use when:** the inspected patent or finding description identifies a federal land entry
whose supporting papers have not been examined, or a completed-patent search misses a
supported tract lead. Keep this route separate from later county conveyance indexes.

The [U.S. federal land entry files](us-federal-land-entry-file-recovery.md) workflow carries
the full entry route: routing the entry by its authority, the separate bounty-land application
and entry series, the party-role table, the tract-book search behind a missing patent, and the
case-file request and inventory. This step adds the locator, packet and date controls below.

Search the county deed books for the patent too. Owners could record their federal patents in the county's deed books [S109], and some counties kept a separate book of original grants, indexed by township and range, in which the United States was the grantor, as Carroll County, Iowa, did [S110]. The United States is the grantor of a patent and the patentee its grantee, so search the grantor index under "United States", not the grantee index as one community post says [S108], [S110]. Tax lists and probate records can supply the land's legal description for a tract-indexed book [S108].

1. Save the patent image/locator and its supplied state, land office, act and date,
   acreage, document/patent number and exact land description. Keep these labelled fields
   separate; an absent entry-file number is not supplied by relabelling the patent number.
   Copy the BLM land office, act year and document locator into the request worksheet, then check what the custodian requires for the particular series [S10].
2. Identify the entry class from the document or finding description. The cited cases
   include cash sales, bounty-land military warrants and homestead entries. Match the
   locator fields to the actual custodian's series description and instructions for that
   class and period before requesting the file; record unresolved class, custody or access
   separately. A patent image does not establish that its supporting packet has been
   retrieved. [S11, S12]
3. After a completed-patent search misses a supported tract lead, follow the tract-book route in
   [U.S. federal land entry files](us-federal-land-entry-file-recovery.md) to entries that did
   not reach patent, and retain the literal entry status, legal description, land office and any
   entry/file number. Queue a
   corresponding case series only when that locator and the actual holdings support it,
   keeping requested and retrieved files separate. Tract books can record entries that never reached patent [S17]. Record the entry’s historical status separately from whether its file can now be retrieved.
4. When the packet is available, compare its identifiers with the patent lead and inventory
   the actual jacket and component documents against the entry-class targets below. Inspect
   certificate and assignment reverses where present. Retain each component actually present,
   including affidavits, with its individual locator, and record the requested and retrieved
   extent; do not assume a fixed page count or a complete packet from the presence of a
   certificate. [S11]
5. In bounty-land papers, keep the named veteran, heir and assignee as separate rows of the
   party-role table in U.S. federal land entry files. An assignee is not thereby the veteran or
   a resident of the parcel. In homestead papers, keep the reported settlement, application, filing,
   improvements, testimony and patent dates distinct. Attribute claimant and witness
   statements to their actual documents; route conflicts and identity questions to the
   evidence/proof workflow. [S11]

| Entry lead | Components illustrated in the teaching account |
| --- | --- |
| Cash sale | Register and Receiver receipts, certificate, and any described agency or preemption papers |
| Bounty land warrant | Certificate and its reverse or assignment endorsements |
| Homestead | Application papers, claimant and witness testimony, and related enclosures actually present |

Use this table as an inspection checklist. Record which documents actually appear in each packet, including any endorsements on the reverse [S11].

**Artifact:** patent-to-file locator crosswalk, entry class and retrieval state, component
inventory, named roles and separately sourced event dates.
**Check:** the patent, supporting entry file and later deed remain separate record objects.
The cited cases supply no universal eligibility rule, period of residence, page count,
digitization guarantee or independently verified family conclusion.

## Prompt pattern

> Using these land-index instructions, entries and book descriptions, build the index audit
> and locator ledger. Search both named index directions where held, preserve uncertain
> book/page readings, and identify the correct series before retrieving the target.
> Compare directional letters and coordinates without silently editing them. Record instrument,
> acknowledgment and recording dates separately and state the record form actually viewed.
> Return the bounded retrieval result and unresolved targets; do not infer kinship or title.
