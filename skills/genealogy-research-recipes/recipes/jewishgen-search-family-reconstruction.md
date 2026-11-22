---
id: "jewishgen-search-family-reconstruction"
title: "JewishGen searches that recover families missed by a name-and-town query"
summary: "Recover families a JewishGen name-and-town search missed: name variants, mixed-field batches, wives' natal families and married daughters."
kind: "platform"
scope: {"platforms": ["jewishgen"], "tasks": ["JewishGen exact, partial, phonetic or fuzzy searches; double names and patronymics; conflicting ages or delayed registration; a missing marriage record, unknown maiden name or daughter who disappears under a married surname; counting result rows as distinct entries, keying households on the original record, and telling an overflow, an error or an uncovered database from a completed search with no hits."]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "JEWISHGEN-SEARCH-FAMILY-RECONSTRUCTION-01", "text": "Do not convert a phonetic, household or age match into a relationship."}]
handoff: ["bessarabia-moldova-record-routing", "evidence-proof-judgment", "russian-empire-jewish-identity-attribution"]
checked: "2026-11-12"
checked_basis: "Rechecked 2026-11-12"
capabilities: {"browse": ["jewishgen"], "local_script": [], "extensions": [], "data_transfer": [], "contact": ["contact"]}
router: {"section": "Records by country and region", "group": "Jewish records", "order": 79}
---

# Recipe: JewishGen searches that recover families missed by a name-and-town query

## Contents

- Goal
- The matching unit comes before the query
- A query ladder, with an explicit reason for every change
- Read the result set before counting it or accepting a negative
- Geography has several roles
- Ages: choose the observation date before choosing the search window
- Double names and ambiguous patronymics
- A wife's natal family when the marriage entry is unavailable
- A daughter's married household when neither husband nor married surname is known
- Further pivots that a single person search misses
- From a missing-husband notice to an agency case file
- Prompt-craft and output contract

## Goal

Turn an unsuccessful JewishGen search into a sequence of discriminating queries. Recover competing family candidates without assuming a fixed surname, a literal name match, one town, one birth year or a known husband. This recipe owns retrieval and comparison; identity and relationship rulings belong to [evidence-proof-judgment](evidence-proof-judgment.md) and [Russian-Empire identity attribution](russian-empire-jewish-identity-attribution.md).

## The matching unit comes before the query

Read the target collection's instructions: what is searchable, whose name each field represents, whether matching returns individuals or households, which years and populations are included, and how to reach the original. JewishGen [Global Search](https://www.jewishgen.org/search/Global_Search.php), which replaced Unified Search, is an entry point; preserve the collection name behind each result.

Three documented traps change how a result must be read:

- **Exact does not always mean literal.** JewishGen's Search Guide says that Is Exactly "still expands JewishGen's standard given-name synonym groups, so it is not literally letter-for-letter": a search for one form also returns the other names in its group, for example Jankel, Jakob, Jacob and Jack. [N17 @2026-11-12] Record both the submitted form and the returned form.
- **AND does not always mean the same person.** In Belarus Revision Lists, surname and given-name conditions can be satisfied by different members of one household, and the whole household is then returned. [N18 @2026-11-12] Inspect individual rows before treating the conjunction as a person's identity. [Belarus search instructions](https://www.jewishgen.org/databases/Belarus/BelarusRevisionLists.htm).
- **A participant is not necessarily the record subject.** A birth's father field ordinarily describes the child's father; it is not automatically the mother's father. To find a woman as a mother, use the collection's maternal fields or inspect a broader extract. Verify labels before composing the query.

## A query ladder, with an explicit reason for every change

Save the broad results first. Apply one new constraint at a time and compare what disappeared; retain that rejected set for checking filter effects. These are query plans, not universal UI or CLI commands. Use only methods offered and documented for the selected database.

| Problem | Next search | What it tests |
| --- | --- | --- |
| Known surname, uncertain spelling | Exact; Phonetically Like; Sounds Like in separate passes | Literal/synonym behavior versus two phonetic candidate sets |
| Stable beginning, changing ending | Starts With on the bare stem | Suffix and transliteration variants; do not append an invented wildcard |
| Uncertain beginning, stable internal fragment | Contains when supported, or a documented wildcard query | Prefix loss or an internal spelling fragment |
| One or two suspect letters | Fuzzy Match, then Fuzzier Match and Fuzziest Match, then plausible transcription variants | Edit-distance errors versus a different naming form |
| Double given name | Both components separately; full forms in both orders | An omitted component or reversed order |
| Two words might be given name plus patronymic | Search both parses separately | A compound name misread as two generations |
| Father known, surname unknown | Given-name variants plus the collection's father/patronymic field; omit surname | Alternative family surnames or missing surnames |
| Expected town produces nothing | Remove Town; search the town in Any Field where available | Origin, residence or transfer recorded outside the indexed Town field |
| No reliable surname, one small community | Bounded town/collection extract, then local name/age/household filtering | Records inaccessible through the expected name field |
| Woman disappears after childhood | Search her as mother in children's births and as wife in household lists | A married household under an unknown surname |

**Do not substitute one phonetic pass for a variant matrix.** Hungarian census instructions distinguish Phonetically Like (Beider–Morse), Sounds Like (Daitch–Mokotoff) and fuzzy (Damerau–Levenshtein). Belarus instructions specifically warn that Chaia will not retrieve Khaika through the phonetic methods. Diminutives, religious/secular forms and double-name components need explicit passes. Build the matrix from attested name forms, preserving the source for each variant. [Hungarian methods](https://www.jewishgen.org/databases/Hungary/CensusOther.htm), [Belarus given names](https://www.jewishgen.org/databases/Belarus/BelarusRevisionLists.htm).

**Do not improvise Boolean or wildcard syntax.** JewishGen's Search Guide documents comma as OR and space as AND for every Search Type, while its How-to FAQ says the comma works with every type except Is Exactly. A multiword name is therefore not automatically a literal phrase. Wildcard availability varies: the Anglo-Jewry 1851 instructions permit `*` and `?` under Is Exactly, while Starts With uses a bare beginning. Check the chosen interface before reusing either convention. [Search Guide](https://jewishgen.org/HowToFAQ/searchguide.html), [How-to FAQ](https://jewishgen.org/HowToFAQ/howto.html), [1851 search instructions](https://www.jewishgen.org/jcr-uk/1851/How_to_use_the_Database.htm).

**Test a pinned letter in the selected search type.** JewishGen’s Search Guide uses `Sch[w]artz` to exclude Schvartz in phonetic or fuzzy searches and reserves the asterisk for Is Exactly [N17 @2026-11-19]. Its How-to FAQ assigns brackets to Is Exactly [N22 @2026-11-19]. Run the same surname with and without brackets in the same collection and mode. Compare the actual spellings returned as well as row counts. An unchanged count alone cannot establish how the engine handled the brackets.

Keep an actual query ledger: database, access path, fields, methods, Boolean relation, date, outcome state, row count, distinct-entry count, the positive control run beside it and reason for the next query. A listed query that was never executed is a plan. If using a search tool or CLI, read its current documentation, inspect the returned datasets and applied filters, and preserve partial-result or authentication errors; unsupported or ignored filters cannot certify a negative.

### Mixed-field batches to try

These combinations are retrieval plans, not results from completed searches. Each combines two fields. Global Search joins two criteria with AND for every user; a third or fourth criterion, or OR between rows, needs JewishGen's Value-Added status, which comes with a donation. [Global Search](https://www.jewishgen.org/search/Global_Search.php), [Value-Added Services](https://www.jewishgen.org/JewishGen-erosity/valueadded.html). Use separate methods per field only where the interface supports them. Without Value-Added status, or where the interface does not support it, split the plan into two-field passes and compare the remaining values locally. Begin without an age or Town restriction when those are uncertain.

| Batch | Combination with AND | Purpose |
| --- | --- | --- |
| A | Surname Phonetically Like + Given Name Starts With | Variable surname spelling and a stable beginning of the given name |
| B | Surname Starts With + Given Name Sounds Like | Stable surname stem and several given-name spellings |
| C | Surname Sounds Like + Any Field exact/text place | A spelling variant with a geographic mention outside the main locality column |
| D | Given Name Sounds Like + supported father/patronymic field Exact | Unknown surname, relatively secure paternal-name form |
| E | Given Name Exact + supported father/patronymic field Phonetically Like | Secure given-name form, variable paternal-name spelling |
| F | One component of a double name + supported father field; repeat with the other component | An omitted or misparsed component without treating the words as a literal phrase |

For D–F, verify whose father the field represents. For every batch, inspect which actual person supplied each match; the household-level AND trap still applies. Union the candidates from A–F and deduplicate by source record reference, not normalized name. Tighten a field only after checking that an already known row survives that constraint.

## Read the result set before counting it or accepting a negative

**Count distinct entries, not rows.** A result list is a list of rows, and rows are not people. A household-list database returns every member of a matching household; a birth row can match on a parent's name, so its subject is the child; and one original entry can come back from more than one database or index. Before reporting any number, remove repeated rows: two rows are one entry only when they give the same person from the same original record, with the same record locator and the same line or name in it. Then mark which person in each remaining row carries the searched name, and say what the number counts: rows per database, distinct entries, or people after identity work. A row total is never the number of people who bore a name; counting people needs the identity rulings in [evidence-proof-judgment](evidence-proof-judgment.md).

**Key a household on its original record, not on a household number in the results.** Unless the collection's instructions say that a household number in the results is copied from the original list, do not use it to join, merge or split households, and do not expect the same entry to carry the same number in another query. Key each household on the household number written in the original list or, where the list has none, on the line where the household's entry begins. Add the link to its original record, the archive reference (for example archive, fond, opis and file), the date and the image or page number to locate it. A page alone does not identify a household: several households can share one page, and one household can continue onto the next. Even a number copied from the list identifies a household only within that list; the former-number pivot below explains how to follow it.

**Give every executed query an outcome state.** A query that ran to the end and returned a complete list with hits is completed with hits: record its row and distinct-entry counts. A query that returned no hits or an incomplete list takes one of the four states below. Only the first of those can support a negative, and only after the positive control below.

- **Completed, no hits.** The search ran to the end and returned nothing. This is a NIL, as defined in [research-documentation](research-documentation.md), for that query and database version only.
- **Overflow or truncation.** The site refused the query as too broad, reported too many results, or stopped the list at a display limit. Nothing was tested, so this is not a NIL. Narrow the query to bounded variants, for example a given name with each surname form instead of a common given name alone, and log each narrowed query as its own row.
- **Error or expired session.** The search returned an error page, a login prompt, a timeout or only part of the results. Nothing was tested. Fix the cause and run the query again.
- **Not covered.** The database's places, years or roles do not include the target; use the Records Catalog check and the role-coverage pivot below. Record the gap; a query against that database cannot produce a NIL for the target.

**Run a positive control in the same batch.** Before accepting a NIL, query a person already known to be in the same database, in the same session, with the same region, database selection and search options. Prefer a person whose entry was found before through the same field. Log the control as its own row with its result. If the control fails, the empty result shows a broken session, a wrong region, a wrong database or a bad option, not an absence: fix the cause and run both queries again. A control that succeeds shows only that this field and scope worked; it does not cover other spellings, fields or databases.

## Geography has several roles

Keep separate fields for registration, residence, event place, birthplace and places in comments. The Belarus revision-list instructions distinguish the town of registration from residence [N18]. In an 1897 Odessa census result the family’s earlier town, Tulchin, appeared in comments [N2]. Compare surname + Town, surname + Any Field and surname alone. A place printed in comments can also have a hidden Other Towns index entry, so inspect the returned rows before concluding which query found it [N23].

The same indexing distinction applies to names: a surname mentioned inside free text is not automatically searchable phonetically as a surname. Hidden Other Surnames/Other GivenNames can supply that mapping. For a name in comments, compare an Any Field text query with the typed surname/name query before interpreting a negative; do not assume the collection populated those hidden fields. [Indexing guidelines](https://www.jewishgen.org/databases/%24transcription.html).

Resolve ambiguous place names with historical jurisdiction, coordinates and nearby communities before applying a geographic restriction. Communities supplies historical Jewish names and jurisdictions; Gazetteer serves a broader set of localities. For vital records, also identify the community or registration office responsible for the village: a nearby settlement can hold its registers. An administrative catchment is a different search from an arbitrary radius. [Communities/Gazetteer](https://www.jewishgen.org/Communities/), [Polish records questions](https://jewishgen.org/InfoFiles/Poland/Questions.htm).

When a record names an origin or transfer destination, pivot to that collection and its additional lists. When a family merely vanishes, leave migration, missing coverage and name changes as separate retrieval branches. Do not turn an unexecuted all-region search into a claim that the family was absent.

Before treating a region- or town-limited search as negative, open the [Records Catalog](https://www.jewishgen.org/catalog/) and filter by country, sub-region (historical gubernia) and town. Each dataset's page has an **At a Glance** block with its date range, total records and Last Updated date, as on [Ukraine Vital Records](https://www.jewishgen.org/databases/Ukraine/VitalRecs.htm). Use it to confirm that the dataset covers your years, and to choose which saved queries to re-run after a later update. For border or disputed territory, also run the search at country level, not only the sub-region. The [GeneaVlogger interview](https://www.youtube.com/watch?v=KWtdlADparw) motivates this check.

## Ages: choose the observation date before choosing the search window

For each age preserve **raw age; age-column heading; date that column describes; date of the individual entry; title year; event date; registration date; source reference**. Derive a birth interval only after choosing the correct observation date. If an age is exact in completed years but only the observation year is known, year minus age and the preceding year are candidate birth years. Approximate ages require a wider, explicitly justified retrieval window. Never turn one estimated year into an initial veto or average contradictory ages into a fictional birthday.

Check these mechanisms before proposing intentional falsification:

1. **Previous and current revision ages.** Read the original headings and compute each age against its own revision year, particularly when checking a translation [N8]. The Bessarabian schema gives the previous-revision age only for men [N24].
2. **Title year and later entries.** Check the date beside each addition. The 1874 Brest family list includes a daughter’s age entered for 1888. Subtracting that age from the year on the cover sends the birth search to the wrong decade [N7].
3. **Event and registration dates.** Preserve both dates and their labels. Two dates in a Russian-Polish record can instead represent one event under the Julian and Gregorian calendars [N25].
4. **Documentary and apparent age.** Where the form has both columns, transcribe each with its heading before assessing a discrepancy [N7].

**Search later registrations around a wedding or a sibling’s entry.** A contributor found a Kharkiv birth registered at age 22 and suggested an approaching marriage as a possible reason. Search later additions for the child and siblings, then record the stated birth date separately from the registration date [N7].

**Recruit evasion is a testable explanation, not an age correction rule.** Keep the recorded age intact, broaden candidate retrieval, then seek the relevant recruit/family list, marginal note or documented re-registration. A military-age male and an age discrepancy do not themselves establish a motive. For the historical mechanism and attribution sequence, use [Russian-Empire identity attribution](russian-empire-jewish-identity-attribution.md).

## Double names and ambiguous patronymics

For an attested double name such as Abram Moshe, create distinct retrieval lanes for Abram, Moshe, Abram Moshe and Moshe Abram. JewishGen's name guidance documents component omission and order changes. This is a search expansion, not a rule that any Abram and any Moshe are the same person. [Double-name guidance](https://www.jewishgen.org/infofiles/givennames/slide16.html).

When an index gives two name-like tokens, preserve both readings until the original identifies a compound given name or a given name and patronymic [N7]. Compare the mother’s name in all available children’s entries. In the Cherniakhiv births, Yokheved’s father was variously named Yosef, Yosef-Yitzhak and Yaakov-Moshe, so one entry could select the wrong paternal family [N9].

For Polish women, a name-like surname can represent the father's given name, a grammatical form of a surname, or an andronym identifying her through her husband. JewishGen gives Avram Moshe → Sara Abramówna or Sara Moszkówna: either component of the father's double name may supply the patronymic. Retain both component-derived Polish search lanes where the records warrant them. Preserve each raw form and check additional records before choosing its role. [Polish women's names, question 6](https://jewishgen.org/InfoFiles/Poland/Questions.htm).

If a metrical record has parallel Russian and Hebrew text, inspect the original names on both sides. J-Roots 4667 proposes this specifically when a woman's name changes between lists. A second language can supply another search form; it does not automatically resolve the identity or establish that the two halves agree. [Women's-name discussion](https://forum.j-roots.info/viewtopic.php?f=4&t=4667).

## A wife's natal family when the marriage entry is unavailable

This sequence generates competing families; it does not assign parents.

1. Collect her forms and ages from **all available children's births**, later household entries and death records. Record whether the father's name is explicitly written, inferred by an indexer, absent, or possibly another name role. One child's index entry must not dictate her patronymic. [J-Roots 3733](https://forum.j-roots.info/viewtopic.php?f=9&t=3733).
2. Search her given-name variants plus each supported paternal-name variant, without a presumed maiden surname. Use a justified age window and separate natal-place, registration-place and residence searches. If the necessary maternal/paternal fields are not searchable, retrieve a bounded collection and filter locally.
3. Search candidate fathers' households for a daughter with compatible forms and chronology. Compare siblings, mother, addresses, former household numbers and transfer notes. Search a brother's or sister's documented surname as a new candidate lane; keep the reason for the pivot.
4. Return a candidate table: raw names; father's-name source; age basis; place role; siblings/household; direct support; conflicts; missing link; next record that would separate the candidates. A common given name + patronymic + approximate age alone does not choose a natal family.

When those records do not name her natal family, pivot to siblings, residence/house books, a surviving work autobiography or an identified family file. J-Roots 5084 recommends these routes in a concrete missing-maiden-name question; the advice is not a reported successful identification. An alphabetic finding aid may show only a name while the underlying file contains family details. [Missing maiden-name discussion](https://forum.j-roots.info/viewtopic.php?f=20&t=5084), [citizenship-option dossiers](https://forum.j-roots.info/viewtopic.php?f=197&t=9279).

## A daughter's married household when neither husband nor married surname is known

Reverse the search role: **daughter → mother**. In collections with searchable maternal names, search births for her given-name and paternal-name variants over the relevant adult period, omitting the unknown husband/surname. Otherwise locally inspect a bounded extract with the relevant maternal columns.

Group candidate births by repeated parental pair, maternal name forms, residence and source series. Retain each competing group. Then retrieve the groups' household, later child, death or marriage records to connect the adult mother to the earlier daughter. The same maternal patronymic in two households is not a link; remarriage and homonyms remain candidates.

If several mothers fit, look for the father’s given name and the house number in Kraków’s patronymic records [N26]. Compare them with the names repeated in the children’s entries [N9]. Leave the marriage unresolved while the proposed households still fit equally well.

**Worked field plan, not an executed search:** suppose the earlier daughter is Sora, daughter of Abram; her married surname is unknown. The documented Belarus birth schema distinguishes Mother's Given Name and Mother's Patronymic from Father's Given Name and Father's Patronymic. Retrieve a covered, bounded birth collection using supported name/place fields, then locally select maternal given-name variants Sora/Sorka and a supported Abram patronymic. Group retained rows by the child's paternal names, maternal forms and locality. Two paternal groups remain two candidate households. A hit on Father's Patronymic=Abram identifies the child's paternal grandfather and does not satisfy the mother's paternal-name condition. A displayed maternal column is not a guarantee of a dedicated search selector. [Belarus birth schema](https://www.jewishgen.org/belarus/belarus_births.html).

Before declaring the marriage missing, inspect how the original marriage index is arranged. Polish guidance describes indexes under the groom's surname, brides in later columns and some brides omitted from the index entirely. An unsuccessful bride-name query is therefore a reason to inspect the actual register or another index, rather than invent a husband. [Polish index guidance](https://jewishgen.org/InfoFiles/Poland/Questions.htm).

When a family's births and deaths appear in its home-town registers but no marriages do, search the brides' places of residence. A [discussion of missing marriages](https://forum.j-roots.info/viewtopic.php?f=4&t=4667) reports, with several confirming posters, that the ceremony and record were usually made there, while the couple might later live with the groom's family or in a third place. Treat this as a custom, not a rule: a missing local marriage opens a retrieval branch and is not evidence of a lost register or of no marriage.

## Further pivots that a single person search misses

- **Later marginal notes are retrieval leads.** When you open a metrical image, read the full entry and margins even if the index has no annotation field. Transcribe later certificate-issue notes separately and follow [metrical-book recovery § 7](russian-empire-jewish-metrical-book-recovery.md#7-read-later-notes-as-a-separate-dated-layer) for the later-name search and holding-archive inquiry. Treat the note as a lead; it does not prove the person was alive or resident there.

- **Follow former household numbers.** Bessarabian lists can give a former registration number with its revision year. Follow the pair to the earlier entry and read the transfer or origin comments [N24].
- **Follow the image reference.** Use the film, page or archive reference in a JewishGen index to browse a FamilySearch image even if a name search there misses it [N6]. For Bessarabian metrical originals, search ANA fond 211 by district opis as set out in [Route a Bessarabian or Moldovan record by date, district and bank of the Dniester § 4](bessarabia-moldova-record-routing.md#4-search-bessarabian-metrical-books-in-ana-fond-211-by-opis).
- **Separate the original’s repository from the film holder.** Copy the archive, fond, opis and delo from an inventory entry when supplied. A Glusk discussion distinguishes an 1858 list cited as Minsk 333/9/1072 from an eighteenth-century census attributed to the Lithuanian State Historical Archive. A contributor interpreted the film code as a Jerusalem copy [N13]. Check the repository’s own inventory for the exact file. Compare fields and coverage in the regional project and each host copy. Matching rows drawn from one index supply one record reference [N1], [N5].

- **Compare versions of the same index.** As checked on 2026-11-19, JRI-Poland labels its Legacy search fully functional and NextGen a limited test dataset [N27 @2026-11-19].

- **Compare the underlying lists before counting duplicate index rows.** For men in the 1874–75 census, check registration with the townspeople’s society, place of residence and liability for military service. One file can contain overlapping lists. The reported pair of rows and the significance of a lone previous-age entry remained unresolved. Use both references to locate the full household and read the original headings [N7].
- **Check which people the index covers.** A demonstrated 1875 military list covered men [N4]. Check a memorial book’s translated chapters, full-text name index and separate necrology [N29], [N30]. For a burial search, check the cemetery inventory [N31].
- **Measure how many records the town search actually covers.** Search without a surname under historical and modern forms, such as Zaslav and Izyaslav. Total the results by collection, keeping Family Finder and submitted family trees separate from indexed vital records. If few vital entries appear, check which registers survive and which volumes the index covers [N12].
- **Compare volumes and years across fonds.** For a crown rabbi’s registers, list each fond, file, year and indexed extent. Where two copies survive, compare their coverage year by year. Indexing one fond can leave gaps covered only by another. The extent of overlap must be checked for the town in question [N13].
- **Privacy gate:** <!-- privacy-gate: contact --> Messaging a JGFF researcher or FTJP tree submitter contacts a living stranger and can reveal the user's family details and research; answer the privacy gate in `SKILL.md` first.
- **Use researcher and tree matches as leads.** JGFF records research interests [N32]. FTJP submissions are not validated by JewishGen. Ask for the underlying record only if contact is authorized. [N33]
- **Repeat a saved query after a relevant update.** Preserve the earlier date, fields and scope. If a collection has changed, rerun the search against the added years or towns and record what changed [N3], [N1]. A 2012 release notice itemized files distributed to LitvakSIG district groups before their planned public release [N14].

- **Check for a district release before accepting a public-database miss.** LitvakSIG’s district page says qualifying contributors receive the district’s new translations at least 18 months before public release in the All Lithuania Database [N28 @2026-11-19]. Check the translated-record list for the series. Record the series and its public status. Obtain authorization before joining a group.

- **Check the translated extent behind a Yizkor hit.** For a family or community lead in a memorial book, search the JewishGen Yizkor Book Database and linked community or regional translation project before starting a fresh translation. Inspect what is actually translated, including any translated contents list and linked chapter pages. The Lublin project, for example, provides a translated contents list while substantial content remains untranslated; record chapter-level coverage rather than labeling the whole book translated. [N19 @2026-11-16](https://www.beholdgenealogy.com/blog/?p=3874) [N20 @2026-11-16](https://www.jewishgen.org/Yizkor/faq.html) [N21 @2026-11-16](https://www.jewishgen.org/jewishgen-erosity/YizkorTr/YBLublin.html)

## From a missing-husband notice to an agency case file

For a supported family-separation lead in the relevant period, compare JewishGen's Gallery of
Missing Husbands entries with the separate National Desertion Bureau Card Catalog. Keep the
newspaper reference and card locator distinct; compare the named couple, dates and case context
before linking them. Retain the card's opening date, referring agency and case-file number when
present. The [project historian's interview](https://familylocket.com/rlp-378-the-jewish-boards-unique-collections-interview-with-gavin-beinart-smollan/)
describes a card-to-YIVO file route: follow the holder's actual instructions and queue a request
within the authorized research scope. A card does not guarantee a corresponding file; preserve
a missing or unavailable file separately from one inspected.

In the described catalog, the name search covers the couple, while a referring individual such
as a rabbi may appear in a separate referred-by field. Check the actual field's availability and
meaning before querying it. A newspaper entry or card is not the full file. Keep stated causes
and case outcomes attributed to their informants and record context; they do not independently
establish motives, accusations or identity. Current fees, form limits and access remain to check.

## Prompt-craft and output contract

> Build a JewishGen retrieval plan from the supplied records. Preserve raw names and dates. For every proposed query give collection, person's role, fields, match methods, Boolean logic, geography role and reason. Mark proposed versus executed queries; give each executed query its outcome state, row count, distinct-entry count and positive control. Generate competing natal/married-household candidates without assuming the unknown surname or husband. For ages identify the actual column and observation date. Return supporting rows, counterevidence, coverage gaps and the next discriminating query or original record. Do not convert a phonetic, household or age match into a relationship.

The assistant can generate variants, execute authorized bounded searches, compare extracts and prepare this table. The researcher owns name-role interpretation, any calendar conversion not checked against the document, age-falsification allegations and the final relationship ruling. Keep raw Family Finder/tree results and living-person contact details out of public artifacts.
