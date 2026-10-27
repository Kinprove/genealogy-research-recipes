# Recover manuscript and archival collections that may mention an ancestor

Use this when an ancestor's letters, diaries, activities, employment, membership or locality may survive in personal papers, family papers or organisational records held by a special-collections library, historical society or archive. This recipe covers union-catalogue querying by context, tracing a hit to its holding repository and finding aid, and keeping catalogue, requested and inspected states apart. For single-vendor catalogue keyword behaviour, use [Ancestry catalogue searching](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/ancestry-record-search-recovery.md), [FamilySearch holdings audits](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/familysearch-practical-record-workflows.md) or [MyHeritage collection search](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/myheritage-historical-record-search.md). For Ukrainian archival lists, use [Jewish archival list triage](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/jewish-archival-list-triage.md). For logging and citation format, use [research documentation](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/research-documentation.md) and [source citation](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/source-citation.md). Identity and kinship rulings belong in [evidence/proof judgment](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md).

## Do not start with the ancestor's name

Archives arrange papers by creator or donor. They describe holdings by collection, series, extent and a brief summary, so they seldom index the people named inside the papers [S1], [S17], [S19]. A personal-name search that finds nothing is therefore not a finding. Never report "no manuscripts exist" or "not in this archive" because a name search failed [S1], [S3], [S21]. You may run the ancestor's name as one facet. Collection-level cataloguing gives name access mainly to creators, donors and prominent subjects, so a name search finds people who were famous or who created or donated a collection, and seldom anyone else [S3].

Before you query, build two registers.

- **Context register.** Record the ancestor's town, county and state (from smallest to largest); the record types sought, such as tax lists, account books, church records, Bibles or family papers; events the ancestor took part in; religion, ethnicity and occupation; and any agency the ancestor dealt with. Turn each life event into the body that would have made a record. For example, a sharp drop in census-reported wealth between two censuses points to a federal bankruptcy search for that state [S2], [S4], [S18].
- **Creator register.** List everyone whose papers might hold the ancestor's material:
  - correspondents, collateral relatives and neighbours;
  - prominent local people the ancestor lived near;
  - employers;
  - congregations and societies the ancestor belonged to;
  - relatives who moved away and may have kept letters;
  - the compiler of any published family or local history. The compiler's research papers are a separate target from the book and can hold far more than the book printed [S5], [S9], [S10], [S12], [S15].

For a congregation or similar unit, first fix the specific unit from a dated source. Then search for that unit's records instead of the person. The Church History Library example searches a named ward for the period, which turns up material that a name search misses [S21].

## Query by context, and log what each portal actually covers

Run batches that combine place with a creating body, record type, religion, occupation, ethnicity or event. The presenters' examples include:

- a Methodist church plus county and state, instead of a baptism plus a name [S2];
- "Chinese exclusion", which returned more than 300 collections in the presenter's 2025 demonstration, where a name search would have found little [S1];
- a county plus "tax", which surfaced a county tax-office account book [S4];
- "bible", narrowed by a family facet [S6];
- "Crown Point expedition" for a 1755 participant [S24].

If a town search is thin, widen it to the county and then the state [S4].

For a store or professional ledger, also try `account book`, `journal`, `daybook`, `business papers` and `business records` with the supported creator or place. These are alternate finding-aid labels, not a promise that every business-paper hit contains a ledger; check the description for the dated volume [S28].

Do not limit the search to repositories near the ancestor. Papers move with descendants, migrants, donors and collectors. The George S. Tanner papers on northern Arizona are held at the University of Utah. The presenters also report Biltmore Hotel material at a different university than expected, and migrants' letters donated in the state where descendants settled [S3], [S5], [S9], [S14], [S15]. Do not apply a portal's map or repository filter before the keyword search [S3], [S7].

If a result set is large, switch ArchiveGrid to its summary view and narrow by people/family, place, archive location or topic. Write down the facet state with the result count [S3], [S6], [S7].

For each search, record which layer it ran against:

- **ArchiveGrid** draws on two inputs: MARC records from WorldCat, and finding aids (EAD, HTML or PDF) harvested from contributing institutions. Any institution can contribute, so OCLC membership is not a condition of inclusion. It is still a mainly United States, non-exhaustive collection-level index, so a miss there says nothing about repositories that have not contributed [S12], [S16].
- **PAARP**, the Philadelphia-area portal (now branded as the PACSCL finding aids site), includes only finding aids that are electronic and encoded in EAD. Older or unencoded finding aids are absent [S12].
- **DPLA** holds item metadata and sends you to the contributor's site for the object. A DPLA search matches that metadata; do not count on it to match words inside a document's OCR text. Use its contributing-institution facets, then always repeat the search in each institution's own digital library and finding-aid portal (Archives West in the example) [S13].
- **Minimally processed collections** are described at folder, series or family level, without lists of the individuals inside. An unlisted name there is "uninspected", not "negative" [S11].
- **Regional state-archive catalogues still being filled in.** Forum participants report that Schleswig-Holstein's Arcinsys catalogue does not yet cover every district, so a miss there may be a gap in coverage. To see which record classes the archive holds, check a printed guide to its holdings arranged district by district. For Schleswig-Holstein, the thread names Harry Kunz's *Wegweiser zu den Quellen der Landwirtschaftsgeschichte Schleswig-Holsteins*, published by the Nordfriisk Instituut. A guide shows only that a record class exists, not what it says about anyone [S26].

A zero result applies only to that portal, its layer and the query. If a repository plausibly connects to the family's places, or to the places where children lived and died, contact it even if no portal shows anything [S12].

## Read the hit as a description, not as contents

A catalogue hit tells you that a collection exists and who holds it. It does not tell you what is inside [S6], [S8], [S22]. From each hit, record:

- holding repository and collection title;
- creator or donor;
- date span and extent (linear or cubic feet, leaves or items);
- place covered;
- surnames listed;
- any typescript or transcript note;
- related or digital links;
- whether the holding is the original or a copy [S6], [S7], [S8], [S15], [S24].

Do not assume a personal name in a collection title is the creator or donor. A collection can be titled for its subject: DACS rule 2.3.23 gives the example of a collection on Isadora Duncan that she did not collect. Take the named person's role from the finding aid's creator, acquisition and scope notes. Either way, the title does not index the people inside. The presenter in [S3] shows the Miriam Matthews collection of Los Angeles newspapers on African Americans at UCLA, where the description shows that she assembled and donated it.

Watch for copies held elsewhere. The University of Utah holds the original George S. Tanner papers, 21.25 linear feet. The presenter in [S15] worked from a copy set at Northern Arizona University. Record the original holder separately from any copy holder, and take each holder's extent from its own current description.

An extent is not a count of people, and custody moves. In 2022 Tanner read NARA Atlanta's notice that it had received about 54,000 cubic feet of Railroad Retirement Board inactive claims folders from the Great Lakes region, with indexing unknown [S20]. That custody has changed again: NARA Boston now states that it holds about 54,000 cubic feet of these folders (Storages 8–20), transferred from Atlanta. Storages 8–15 left Atlanta in April 2026, and Boston now handles all reference requests for them. NARA Atlanta's page still carries the older wording. Do not assume a series sits near where the person worked, that it is indexed by name, or that the first custody notice you find is current. For an agency series, follow every documented transfer to the current custodian and confirm on that custodian's own page [S20], [S22].

Exclude a collection only when its dates or material types cannot hold the target, and write down the reason. A matching surname, county or hometown is a lead. It is not evidence of kinship.

## Trace the hit to the repository's own finding aid

Use the union portal mainly to learn the repository's name. Then follow its contact link, or search for the repository's own site, and open its catalogue record or finding aid [S1], [S6], [S7], [S25]. There, read the arrangement, container list and folder or correspondent entries. Navigating finding aids is often not intuitive, so ask the archivist or reference librarian how the collection is arranged [S9].

Some finding aids use an unexpected sort key. The Record of Members collection (call number CR 375 8) is arranged alphabetically by unit name. Spell out ward numbers when you browse it: Rasmussen's tip is that a 15th Ward files under F [S23].

A series may be filed under a unit with a different title, so a search on the series name alone can miss it. Widen the search in three ways. First, search the contents notes of other units, and read hits in the search view, not only in the browse tree. For the Nürnberg council decrees (Ratsverlässe), a series-name search returned nothing, yet the decrees for 1520–1604 were listed, with folio numbers, in the "Enthält/Darin" contents note of a copybook (Kopialbuch); in that case the note surfaced in a search of the Bavarian state archives' finding-aid database but not in its archive-structure (tectonics) browse view [S27]. Second, search the parent bodies; for these decrees, look under the chancery and council records, the council minutes and the inner council [S27]. Third, check every custodian that may hold part of a series: the Nürnberg Fünfergericht court files, for example, are divided among the city archive, the state archive and special collections [S27]. The Bavarian state archives state that only a small part of their holdings is described online, so a miss there does not establish that the records are absent [S27].

Record each finding-aid entry exactly as written, with its date and its series/box/folder position. That entry stays an unread lead until someone inspects the item.

## Form a bounded request and keep three states

Before you request or travel, ask the repository:

- whether the material is stored off site and how long retrieval takes;
- how much relevant material there actually is, from one folder to many feet [S3];
- hours, researcher registration, permission or fee requirements, and copy or camera rules. Stacks are closed, so items arrive only by request; NARA, for example, requires a researcher card and pulls records for you [S16], [S19], [S20].

The presenters describe items that are digital but sit behind a sign-in, and others that can be viewed only on site, or only after an access or digitisation request [S21], [S23]. Record of Members is also being indexed on FamilySearch (collection 3714676), which changes what a name search can reach for that collection. NEHGS holds the April 1755 list of payments to New Hampshire officers for the Crown Point expedition (Mss C 2051). The item is also listed in the free Digital Commonwealth portal. Check every free access route before you pay for a membership or a copy.

Request items by the repository's own locator (collection or call number, box, folder or item), not by a surname. If staff say a collection is not held, ask again using the repository's own catalogue record. In the presenter's account in [S15], the front desk first denied a holding that was in fact there.

For a ledger copy request, include the account heading and any linked continuation pages. The article in [S28] describes debit amounts that can continue on another page and a separate payment column. Check the actual volume's labels and page links before treating a partial page as the complete account; no particular debit/credit layout is assumed.

Keep every candidate in exactly one of three states: **catalogue hit**, **requested**, or **inspected**. Record which boxes or volumes were actually read. Anything unread stays unread, not negative [S17], [S19].

## Close with a collection packet

Return the following:

1. A dated query register showing portal, layer, terms, facet state and result counts.
2. The creator register, with where each creator was searched.
3. A candidate table: repository, title, creator/donor, dates, extent, place, listed surnames, digital link, original or copy status, and reasons for any exclusion.
4. Locators for finding-aid entries, with the literal text and dates.
5. Access conditions and request status, including the current custodian for any transferred series.
6. A list of uninspected boxes and unrequested leads.

What an inspected item states stays separate from any identity or kinship hypothesis. Hand those to evidence/proof judgment.
