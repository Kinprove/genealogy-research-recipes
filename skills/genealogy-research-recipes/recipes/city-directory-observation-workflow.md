---
id: "city-directory-observation-workflow"
title: "Build a checked city-directory observation series"
summary: "Build a comparable series of city-directory names, addresses and occupations from checked editions and sections."
kind: "records"
scope: {"platforms": [], "tasks": ["a known address with unknown names, surrounding locality sections, abbreviation keys, index errors, address/occupation changes or a person missing from one directory edition."]}
privacy: "none"
gates: []
guardrails: [{"id": "CITY-DIRECTORY-OBSERVATION-WORKFLOW-01", "text": "A gap in a database's editions and an absent entry on inspected pages are different results. Neither alone establishes why the person is missing."}]
handoff: ["land-index-book-series-recovery"]
checked: "2026-10-07"
checked_basis: "checked 7 October 2026"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Record types in any country", "group": "Burials, directories, land and probate", "order": 206}
---

# Recipe: Build a checked city-directory observation series

## Contents

- Goal
- Before starting
- 1\. Audit the editions and their internal sections
- 2\. Extract comparable rows without importing the index's mistakes
- 3\. Sort the series into questions you can investigate
- 4\. Describe gaps before assigning events to them
- Prompt pattern

## Goal

Turn city-directory entries into a comparable series of names, addresses and occupations.
Preserve which editions and locality sections you inspected, so a missing result does not
silently become a move, death or identity conclusion.

## Before starting

Choose a person or bounded surname group, locality and edition-year range. Keep an image
locator with every extracted entry. Use the directory's own wording for names and addresses;
put expanded abbreviations and proposed identity groups in separate fields.
The worksheets below work with manually read images or copied index rows.

## 1. Audit the editions and their internal sections

1. List the editions actually available at each repository. Record individual years and gaps,
   rather than treating a collection's broad date range as uninterrupted coverage.
2. Open a volume's title page, contents and section headings. A directory named for one city
   can include separate alphabetic sections for surrounding communities or a county taxpayer list.
3. Record which section should contain the target and which you inspected. Inspect another
   relevant locality section when the first does not contain the expected entry.
   The contents may also show a separately printed racially segregated section; inspect it before
   recording no entry, and treat a no-hit as especially weak where a group was poorly canvassed.
   The [presenter's warning](https://www.youtube.com/watch?v=d39IOclm3wU) motivates this check
   without showing which editions used such sections.
4. Save the abbreviation key for that edition. Decode an entry with that key before expanding
   residence, boarding or occupational abbreviations.
5. Mark an inaccessible edition or uninspected section separately from an inspected section
   with no matching entry. [S2, S3, H1]
   Before marking an inspected edition 'no entry', also search its late-additions, changes,
   errata, 'removals and corrections' and necrology pages at the front and back of the volume.
   These sit apart from the main alphabetical list. Record whether each was found and inspected.
   A search of the index or main list alone is not an inspected-edition negative. An entry on
   these pages is a separate observation that may correct the main list or the previous edition.
   It shows the compiler's addition, not an arrival or move date, and gives no destination unless
   one is printed. An empty late list does not prove absence either, and such pages vary by
   edition. See the [Cleveland 1915](https://www.youtube.com/watch?v=VcsuFFgIrWw),
   [1814 Philadelphia](https://www.youtube.com/watch?v=b2O3BFQZ4mg),
   [Lisa Lisson](https://www.youtube.com/watch?v=31IdUHAYlKw),
   [removals](https://www.youtube.com/watch?v=a7aEIGoVXJw) and
   [late-update](https://www.youtube.com/watch?v=NmtuDJBE5eQ) examples.
6. For a former-resident directory, read the foreword to identify the addresses' roles.
   The 1949/50 Breslauer Adressbuch lists later addresses of former Breslau residents but
   orders entries by earlier street and house number. The ordering address is a lookup key;
   do not record it as residence in the titled city at publication. [S4]
7. From the title page, introduction or back matter, copy any stated coverage or canvass period
   (such as a directory 'for the year ending' a given month) and any stated inclusion rule (such
   as males over a stated age, widows, female heads of household or women in business),
   recording that rule with its locator beside the coverage row. If no period or rule is found,
   record that and leave the rule unknown. [S20] Judge a presence or absence against that period
   and rule, not the cover year. Someone who arrived after the canvass, or who falls outside the
   rule, is not a gap. Also check the business or classified section. Copy a firm listed under another household member's
   initials exactly, without saying whose it is. A son's first listing under an age rule gives at
   most a birth-year bound, because a move or an omission can also explain it. Rules differ by
   edition and may not have been applied consistently. See the
   [Cleveland title page](https://www.youtube.com/watch?v=VcsuFFgIrWw),
   [South Haven examples](https://www.youtube.com/watch?v=xjLPo2MMuHs),
   [front-matter tip](https://www.youtube.com/watch?v=8i1MYac23ec) and
   [Hayward firm case](https://www.youtube.com/watch?v=68DpL1IWZHc).
8. For a trade directory such as 'Вся Россия', read the inclusion rule in the volume itself. Posters in a [trade-directory discussion](https://forum.j-roots.info/viewtopic.php?f=4&t=4667) say only larger or guild-paying traders appeared, so a small trader's absence is weak. The town printed can be where the trader registered capital or traded rather than lived. A same-name hit in another town is therefore neither ruled out nor matched.
9. For a German town, search CompGen's Datenbank Historischer Adressbücher (adressbuecher.genealogy.net), a free index of transcribed address-book entries searchable by name and place. Also run CompGen's separate DES address-book search, which covers further books, and look for page images in CompGen's DigiBib. A hit is an index row: use it for yearly residence and occupation only after opening the edition, and cite the edition, place and page. [S25]

   A database no-hit is not an inspected-edition negative. Check CompGen's GenWiki address-book portal for whether that edition is listed in DigiBib but not yet transcribed, or was transcribed only partly (for example, only up to a certain surname). If so, page through the DigiBib scans. Where the volume's alphabetical name register has been broken down for navigation, as in some big-city series, jump through it to the surname. Record which layer you searched: transcribed database or page images. [S26]

   Do not skip an address book whose DES transcription is still in progress: data entered through DES can be searched by anyone at once, so a partly entered book can already return hits [S24 @2026-11-12], [S28 @2026-11-12]. A miss in such a book is the partial-transcription case above, not a negative.

Before you call an edition missing, find out which directories were published for the place and where they are held. For a U.S. place, uscitydirectories.com lists directories by state and locality with the repositories that hold them; its pages carry a 2002–2005 copyright, so a year it omits is unlisted there, not unpublished [S32 @2026-11-14], [S36 @2026-11-14], [S42 @2026-11-14]. The Library of Congress guide *United States: City and Telephone Directories* indexes the Library's own city and telephone directories by state [S36 @2026-11-14], [S43 @2026-11-14].

For an edition missing online, check the local-history holdings of the library serving the town, following the lead from the available excerpt [S65]. Search its catalogue or holdings list by directory title or by locality and year, including print and microform holdings [S66], [S67]. Record the format and catalogue locator in the coverage row. Mark the relevant section as inspected only after viewing its pages.

For Los Angeles, browse the Los Angeles Public Library's digitized city and street directories in ResCarta [S58 @2026-11-20]. If the edition is missing there, check the library's City Directories Index for paper and microform holdings [S59 @2026-11-20]. Record a holdings match with its format and mark an edition viewable online only after opening its scans. A search-result extract from Nancy Hendrickson's guide points to both routes [S57† @2026-11-20].

For Ohio, start with the LDSGenealogy.com Ohio City Directories index and open the relevant county page [S60 @2026-11-20], [S61 @2026-11-20]. Check countywide listings as well as any section for the target locality [S62 @2026-11-20]. Follow the provider's link and verify access to the specific edition before marking it accessible in the coverage row.

Identify each edition by its publisher as well as its place and year. In some cities competing publishers issued directories for the same year, and each can hold entries the other lacks, so give each its own coverage row and look for a rival before you treat a year as covered [S31], [S32], [S33].

Some U.S. directories marked Black or other non-white residents in the main list with an asterisk or an abbreviation such as `col'd`, besides or instead of printing them in a separate 'colored' section [S32], [S35]. Decode such a mark with the edition's key rather than reading it as a footnote, and copy it with the entry as the compiler's designation.

For England and Wales, search the University of Leicester's Historical Directories collection on its Special Collections Online: 689 trade and local directories from the 1760s to the 1910s, with at least one for every county, searchable by name, place and occupation and also available through Ancestry.co.uk [S37 @2026-11-14], [S38 @2026-11-14]. Then look under Directories on GENUKI's county pages for transcriptions and indexes, search Internet Archive for `directory` with the town's name, and check the county family history society's publications for transcripts [S37 @2026-11-14], [S41 @2026-11-14].

Before the 1841 census, an English trade directory can give a trader's street address and trade where the parish register gives only a village or district as the abode; place the address on a map close to the directory's date [S37], [S39]. Early directories listed only the chief inhabitants: gentry, clergy, professionals and the more substantial tradesmen. Later ones grew to cover most heads of household but still left out labourers, servants and the poor, so an absence from any of them is weak evidence [S37], [S39], [S40]. Some directories before about 1823 give only a surname and a trade, with no address [S39].

**Artifact:** One coverage row per edition and relevant section:
repository, directory title, publisher, edition year, locality/section, available/access status,
section image range, inspected range, abbreviation-key locator and result.

**Check:** The year and locality come from the volume, not only its database label. Another
repository's copy of that same volume supplies another access route, not another observation.

### Regional finding aids

For historic Belfast and Ulster, start with the Public Record Office of Northern Ireland's scanned street directories, 1819–1900 [S68 @2026-11-22], [S69 @2026-11-22]. In a Belfast volume, try the street list for an address and the alphabetical or trade list for a person or firm. For a provincial town, open its own section and check the lists of inhabitants and trades. The run has gaps and the provincial sections omit many residents [S69 @2026-11-22].

For European address and telephone directories, check the Library of Congress's country guides for holdings and format [S70 @2026-11-22], [S71 @2026-11-22]. For example, the Belgium guide separately lists uncatalogued directories. Use its inventory alongside the catalogue and verify access for the specific edition [S72 @2026-11-22].

For Central or Eastern Europe, try Genealogy Indexer for historical business, address and telephone directories [S70], [S73]. Check Kleinwaks's directory inventory for the locality. Use the edition's title and page for each observation [S73].

For a Polish locality, check **Geography & Maps** on PolishRoots for leads to specific editions, including commercial and city directories [S70 @2026-11-22], [S74 @2026-11-22]. Check which places and years the linked edition actually covers.

In MyHeritage's historical record catalogue, open **Directories, Guides & References** and narrow by region to find collections with different coverage [S76 @2026-11-22], [S77 @2026-11-22]. Check the individual collection description before using its date range on the coverage sheet.

For Greek addresses and occupations, look for MyHeritage's *Greece, City Directories, 1901-1947* and check the list of selected business and resident directories before searching [S75], [S78]. Preserve the Greek text and its Latin-script transliteration separately, with the directory title and year [S75].

In the National Library of Finland's Digi service, look under **Aikakauslehdet > Almanakat ja kalenterit**, using the collection selector and the place-of-publication filter. Check the collection name in your session and screen Helsinki results by title to remove university almanacs from the city-directory search [S83 @2026-11-22], [S85 @2026-11-22]. If the filter leaves gaps or the menu has changed, use the Genealogical Society of Finland's locality list to open the individual titles and supplements [S84 @2026-11-22].

For a nineteenth-century Helsinki student, consult the term issue of *Suomen yliopiston luettelo* for the student's reported address [S85], [S86], [S87]. Keep the term of the first address found separate from matriculation. Compare it with the street and number a relative reported in the general directories, recording the term or edition year for each row. Search across the overlapping series *Adressbok och yrkeskalender för Helsingfors* and *Adresskalender för Helsingfors stad* when the title you started with skips a year [S84], [S86].

For a historical Paris firm, look up the appropriate year of *Annuaire-almanach du commerce* through the Bibliothèque nationale de France's catalogue link to Gallica. Search the Paris listings for the firm. Record the printed partners and their roles with the edition and page before looking for separate evidence of when the partnership began or ended [S89 @2026-11-22], [S90 @2026-11-22].

## 2. Extract comparable rows without importing the index's mistakes

1. Locate the surname group or candidate entry using the volume's actual arrangement.
   If the name index fails, browse a relevant alphabetical section only when one exists,
   and compare the printed entry with its indexed name. For a former-resident list, use
   the former street/house as a lookup key only when the foreword or heading confirms
   that ordering and the former address is available. If the required key is unknown
   and no usable index supplies another route, leave the entry unlocated and record
   the lookup as unresolved. Do not invent an alphabetical or DES route. [S3, S4]

   If a long surname run looks unordered, test other sort keys before scanning every line. Within one surname, some volumes sorted entries by occupation, men before women, and filed a widow under her late husband's occupation, e.g. 'verwitwete Hauptmann'. Look for her under that word and copy the printed form. A [Berlin address-book discussion](https://forum.ahnenforschung.net/forum/thread/2950717/) states this for Berlin up to about 1925. Do not assume it for other cities or years, and treat the widow wording as status, not a death date (section 3, step 8).

   If the names listed at a dated address are unknown, no usable street or reverse
   lookup exists, and the entries print addresses, a finite pass through the relevant
   locality section or volume in its actual arrangement can recover literal
   street/house-number matches. Add each match to the existing observation table
   and record the inspected range. A page-by-page search of the 1812 Bremen directory found two occupants at house no. 16, leaving the servant’s employer unresolved [S22].

2. Copy the entry as printed, including initials, spouse wording, occupation and address when
   present. Preserve uncertain readings. Keep any normalized name in a separate column.
3. If copying a site's tabular index into a spreadsheet, take the header once, paste subsequent
   records beneath it, and add the correct edition year to every imported row.
4. Compare imported fields with the image. Information printed next to a name can be a locality
   or post office rather than another given name; retain the correction and the original index value.
   Check the source image for ditto marks before splitting an indexed name. One index combined two people whose names the directory printed separately [S11]. Create one observation per printed person, expand the ditto only from its referenced line and retain the original index row for comparison.

   In a 1913 trade listing for a Kremenchug hotel, readers interpreted «Александровск., д. Соловья» as a street and a house owner, although the first reader had taken it for a town and village [S15]. Transcribe the address literally, check the edition’s key for «д.» and keep the proposed owner separate from the hotel operator until the expansion is verified.

   Record the fields and arrangement of a volunteer extract before searching it. A German directory transcriber kept just place, name and establishment and added an alphabetical surname sort [S18]. Return to the edition for the street, district, type of establishment and owner or lessee where printed. A field omitted from an extract stays unknown.
5. Check the first and last imported entries, remove repeated headers or interface text, and
   confirm that each row still has its year and locator. Manual extraction uses the same schema.
   [S1, S3]

If the entry date matters and the volume gives no canvass dates, search contemporary newspapers for the publisher's calls for submissions and publication announcements. Apply each notice only to the main volume or supplement it describes. Use the notices to bound when the address could have been supplied, and corroborate occupancy before dating the move [S88].

Give residence, business premises and other stated address roles separate fields. Where a historical Finnish listing gives a shop address or calls someone a property owner, compare the address with the same-period *henkikirja* (population and tax roll). Record the home, shop, property owned and tenancy separately when the records distinguish them [S92], [S93], [S95], [S99]. If only a contact address is given, keep residence open and compare independent records that place the person or household, such as an appointment or a record of a family event [S100].

**Artifact:** An observation table with these columns:

| Field | Preserve |
| --- | --- |
| Observation ID | A stable identifier for this row |
| Edition and section | Directory title, year, locality and section |
| Name | Printed form, indexed form if used, normalized form separately |
| Address | Printed street/number or locality/post-office wording |
| Other entry text | Occupation, spouse or other relationship wording actually present |
| Reading status | Image checked, index only, or uncertain reading |
| Locator | Repository/collection, volume, printed page, image link/number |
| Candidate group | A provisional identifier; leave competing groups separate |

For entries in a former-resident list, add these columns only where that structure applies:

| Field | Preserve |
| --- | --- |
| Former address / ordering key | Earlier street and house number as printed in the row or its heading, with locator |
| Later address as reported | Later address/place as printed, including care-of or household wording |
| Address-role and time basis | Foreword/heading locator, dates actually stated, and unresolved roles or dates |

**Check:** Do not import an index field as printed evidence when the image says something else.
An edition year identifies the volume; it does not by itself establish a residence date for
each printed address or an exact move date. Keep an unstated time basis unknown. [S4]

## 3. Sort the series into questions you can investigate

When people with the same or similar names could be confused, search for the subject and each plausible candidate in every available directory year in the period of interest and for a few years on either side [S63]. Compare their separate timelines by address and occupation [S64]. Report when each appears and how many distinct candidates the inspected editions support, keeping unresolved entries and coverage gaps visible.

1. Append the next available edition using the same columns.
2. Sort complete rows by normalized surname and given name, then by edition year.
3. Compare occupation and address within each tentative group. Try an occupation-first or
   address-first view when repeated names remain ambiguous.
4. Keep raw spellings and initials visible while filtering variants. An initial-only filter
   may miss a spelled-out given name; inspect the records admitted and excluded by that filter.
5. When the volume has an address-arranged or reverse directory, use it to inspect the
   relevant street and nearby entries. Record those observations separately.
6. Create a question for each change or competing group, with the row IDs that caused it.
   A recurring name, occupation or address is a comparison clue, not an automatic merge. [S1, S2]
   Search the married woman’s own surname entry as well as her husband’s listing. Compare spellings, home and work addresses, occupation and employer across both entries. In a 1968 directory, Marion’s separate entry gave her occupation and workplace in Alexandria; the continuing occupation later suggested a remarriage [S10]. Record both row IDs and seek a marriage or other independent record before joining the names.

   If a business continues under one initial after a possible owner’s death, compare each edition’s name and occupation with the death and marriage records. Berlin researchers proposed that B. Fliegner could refer first to Bernhard, then to his widow Bertha in the egg trade [S16]. Keep the succession open until the dated entries support it. A different occupation on a death record merits a check against other identifiers.

   After a reported remarriage, search later editions by the earlier street address as well as by both surnames [S44], [S45]. Link the row IDs as a candidate sequence and use a marriage or other independent record to distinguish a surname change from a new occupant.

   For same-named people with different occupations at one historical Russian or Soviet address, locate the surviving house book (домовая книга) for that building and period. Its resident entries can help distinguish the people [S12], [S19]. If an authorized request is necessary, identify the volume by historical building and year. Compare the general and professional directories separately because their first listings may differ.
7. For a located former-resident entry with a reported later locality, use that place for
   one bounded follow-up, such as a later directory or a relevant civil-register search there.
   Keep it as a source-attributed lead; it does not establish a move at the edition date. [S4]

   Look for a departure note in place of a street address before closing a search. The 1891 Seattle directory printed ‘removed to S F, Cal.’ for James S. Adams [S30]. Preserve the wording, then check San Francisco’s directory for that and the following year [S29]. A same-name hit remains a candidate, and the edition dates the listing only.

   In a former-resident list, inspect other entries at the former house number for leads to later addresses. In a 1950 directory the entry ‘Post Raden über Haste’ distinguished Raden from the delivering post office [S17]. Copy ‘über’ or ‘üb.’ literally, check the destination locality’s own directory and supplement, and use a separate record to establish any household relationship.
8. Copy 'widow', 'wid of' or a printed death note exactly, as the status reported in that
   edition. When a man's run of entries ends and his wife next appears as his widow, rule out
   same-name men and record both row IDs as a death-interval clue. Propose a death-search window
   from these observations and the edition's stated coverage and publication frequency, because
   publication intervals varied; the window is conditional on their dating and accuracy, and the
   last listing is not an established alive-after bound. Some directories added the label only in the
   year after the death. Divorced or separated women sometimes reported themselves as widows, so
   look for the husband elsewhere. Record contents-listed deaths-since-last-edition or
   divorces-granted lists as separate observations. They are leads to the death or court record,
   bounded only by the stated period. A printed death date is the directory's statement and
   should be checked against the death or obituary record; widow labels and death or divorce
   lists only bound or suggest a death and do not prove one [S10], [S50], [S51], [S52], [S53], [S54], [S55], [S56].

**Artifact:** The observation table, saved sort/filter criteria, provisional groups and a
worklist such as “retrieve a record linking observations D07 and D12.”

**Check:** Sorting preserves each row's year, source and raw wording. A group assignment remains
provisional until the records support that person's identity.

For a supported same-block or building question, retain each literal building and unit number,
including fractional addresses. Compare dated street/reverse entries and stable-neighbor
context before choosing between a move, unit conversion, renumbering or error. At 530 and 530½ W. Sycamore, a researcher reported a former two-unit house later restored to a single residence [S23]. Keep both literal numbers and record the evidence for any proposed correspondence.

Before treating the present building at that address as the historical dwelling, compare its
construction date with the record date and retain the construction-date source. An unverified
listing year flags a question; a supported construction date after the record excludes that
structure, while leaving an earlier building or changed address correspondence to investigate.
An earlier construction date is only compatible with the historical observation; it proves
neither occupancy nor that today's appearance is unchanged. [S21]

If an inspected auxiliary section labels a land-register reference, preserve its heading,
locality, street/house wording and land number separately. Carry the stated reference into
the [land-index/book-series workflow](land-index-book-series-recovery.md). A directory’s Grundbuchnummer can point to a land-register entry [S24]. Copy it separately from the house or parcel number and check the land record for ownership.

If a marriage record names an officiant without identifying a congregation, check an available
directory near the event's date for a clergy listing. Preserve the printed name, denomination
and address with the edition and entry locators; keep an unstated address role unknown.
Compare the directory's church listings for a possible congregation, then establish whether
its relevant marriage register survives and who holds it before requesting a record.
Keep the affiliation provisional: matching denomination or nearby addresses do not establish
the ceremony's location or either spouse's membership. [S2]

If a census or other record gives an occupation but no employer, check a classified or business
section from a directory near the record date for the town of residence. List every business of
that trade with its edition and page locators. Propose a specific employer only when it is the only
one listed, and keep it marked as an inference until an employment or other record names it. An
employer named by a web page or AI answer is not a substitute for this check. A business section
can be incomplete, so a single listing does not prove there was no other employer. [S27]

When an entry names the employer, look the firm up in the same edition: in the business section or commercial register, often at the back and arranged by category, and among the advertisements [S34], [S35]. Copy the firm's printed address and trade with their page locators beside the employee's row.

### Address and business follow-ups

For a dated address of a deceased person in MyHeritage's U.S. city directories, open the record in your account and look for **See who else lived at this address**. If present, open the address results and verify the address, unit and overlapping edition years on the underlying listings. Use a printed street list or the bounded page search in section 2 when the control is absent. Keep co-residence and kinship provisional [S79 @2026-11-22], [S80 @2026-11-22].

Use a directory address near the census date to look for the same person on the census schedule. For a U.S. urban census with street-based enumeration districts, use the historical street and number to find the district for that census year, then inspect its pages [S81], [S82].

For a historical Helsinki ownership claim, use the city archives' property cards in Sinetti. Search for *kiinteistökortisto*, open the district and use its map to match the block and lot before opening the card's PDF. Compare the card's dated evidence with the directory wording and follow any linked land records if title is still in question [S89 @2026-11-22], [S91 @2026-11-22].

When tracking a firm's size or possible succession, tabulate distinct listed premises by edition. Keep the count tied to the inspected sections and preserve a comparable coverage row. A personal occupational title and the last firm listing are separate observations. If the listings disappear and a former employee is a plausible successor, search the same year for that employee's firm under any independently known later surname. Compare the trade and premises, then seek independent evidence of a transfer [S94], [S95]. Track the household address independently through the same editions [S99].

If a personal listing gives a title such as house owner and the person's role at an institution is in question, inspect the institution's listing in the same edition for staff names and roles [S93]. Compare the institution's listings over time, keeping each department's address and public hours with its own edition [S97]. For an old police station, use the directory's police listing to identify the branch and copy its printed street address before comparing it with other records [S101]. In the 1861 Helsinki calendar, try *Fabriker och Manufakturinrättningar* for a factory. In the 1872 calendar, look under general addresses for an address office (*adresskontor*) and compare following editions for its listed operator [S102], [S103].

Check staff contact addresses and public premises separately, and use dated notices or an institutional history to establish when the public was admitted. The 1912 Helsinki directory placed caretakers at the National Museum site four years before the museum's 1916 public opening [S97], [S98].

Treat a school's printed term dates or an institution's hours as its published schedule. Look for dated notices of actual activity before using those dates to extend its operating period [S93], [S96].

## 4. Describe gaps before assigning events to them

1. For the first or last apparent appearance, return to the coverage sheet.
2. Check whether an omitted year is absent from this repository, was not published, is
   inaccessible, or remains unlocated. Keep the unknown state when you cannot distinguish these.
3. Check whether the earlier edition included the same community or taxpayer/resident section.
4. Search another available edition or repository when that specific gap affects the question.
5. Report the actual observations and remaining gaps. For example: “Listed in the inspected 1931
   taxpayer section; not found in the inspected 1929 volume; comparable 1929 section coverage
   remains unconfirmed.” Do not replace that with a dated arrival. [S3, H1]

**Artifact:** A short timeline of observed entries plus a gap table and the next bounded search.

**Check:** A gap in a database's editions and an absent entry on inspected pages are different
results. Neither alone establishes why the person is missing.

Check whom the directory intended to list before using a household member’s absence. For a listed woman, transcribe `Witwe` as widow and record an occupation only when the entry supplies one for her [S20]. A household-head list can omit other residents.

If a census shows a recently widowed person living alone and a later directory lists them as a
lodging housekeeper, record in the gap table the hypothesis that they took in boarders during
the intervening years [S48]. Keep the reported occupation with the edition that lists it [S49].
Leave the earlier livelihood and the start date unknown unless other evidence establishes them.

When no directory covers the town for the year you need, or the person is missing from the one that does, widen to other directories before you treat the year as empty. A small town can appear in a county directory, and some states had state directories: Delaware's early directories covered the whole state [S32], [S33]. Rural-route, farm, church, club and professional directories also place people in a time and place, often yearly [S32], [S33], [S36]. Newspaper classified ads can give the home or business address of someone the directory missed; search them as in the [Newspapers.com recipe](newspapers-com-search-recovery.md) [S46], [S47]. Give each such listing its own row with its title, year and locator.

When successive listings leave a move undated, search the intervening newspaper issues for move notices. Save the stated street, building owner or lot and notice date. Compare later listings for the same building and any tenancy wording before joining the addresses [S89].

If a tradesperson drops out of a directory while an independently known property or trade gives you a lead, search same-year newspaper reports of local licensing or workshop approvals. Record the occupation, lot, decision date and any conditions. Record an approval as authorization and leave the opening date and actual operation open [S93].

## Prompt pattern

> Using these directory images, edition descriptions and earlier worksheet rows, produce the
> coverage sheet and observation table above. Preserve printed names and abbreviations, identify
> which section and year each row belongs to, and show corrections to index fields separately.
> For former-resident lists, retain the earlier/ordering and later-address roles separately.
> Group candidates provisionally, keeping alternatives. Explain each gap using the recorded
> coverage, then give one bounded next search. Do not infer a move or death from a missing row.
