---
id: "periodical-index-search-retrieval"
title: "Search a genealogical periodical index and retrieve the article"
summary: "Search a genealogical periodical index such as PERSI and retrieve the article."
kind: "records"
scope: {"platforms": [], "tasks": ["Full-text search of Russian newspapers, and provincial gazettes (губернские ведомости) on paper or microfilm."]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "PERIODICAL-INDEX-SEARCH-RETRIEVAL-01", "text": "A personal-name miss therefore usually means the article text was never searched, and a hit is only a citation."}, {"id": "PERIODICAL-INDEX-SEARCH-RETRIEVAL-02", "text": "Until the gate is answered, keep the request as an unsent draft on the user's device."}]
handoff: []
checked: "2026-11-07"
checked_basis: "checked 2026-11-07"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": ["contact"]}
router: {"section": "Record websites, libraries and maps", "group": "Books, periodicals and manuscripts", "order": 42}
---

# Search a genealogical periodical index and retrieve the article

Use this recipe when an ancestor's surname, place or event might appear in a genealogical or historical society periodical, and you are searching an article index such as PERSI or the German indexes Der Schlüssel, Familiengeschichtliche Quellen and Quellenschau für Familienforscher. None of these is a full-text index. Most of what they record comes from article titles, plus authors and subjects that indexers assign. A personal-name miss therefore usually means the article text was never searched, and a hit is only a citation. The same logic applies to book searches that cover only metadata, which are handled in [HebrewBooks search recovery](hebrewbooks-search-recovery.md). To audit FamilySearch Catalog holdings for a locality, use [FamilySearch practical workflows § 2](familysearch-practical-record-workflows.md). For wording negative-search statements in a report, use the [standards audit](genealogy-standards-audit.md).

## Contents

- Record each index's depth and coverage before searching
- Build the query set from place, jurisdiction and event
- Carry every hit to the article
- When a Russian periodical has no index: full text or the paper run
- Report bounded results

## Record each index's depth and coverage before searching

- **PERSI only matches what the indexers recorded.** PERSI was developed by the Allen County Public Library (ACPL). It is not an every-name or every-word index. A searched word has to be in the article title, or in a subject, place or surname keyword the indexers assigned, to be found. Presenters add two points:
  - S2 says authors are indexed along with titles.
  - ACPL staff in S8 say that when an author gives an article an oblique title (their example is "bones"), indexers add a plain subject such as cemetery records.

  [S2], [S7], [S8]
- **Search PERSI where it is hosted now.** Start with ACPL's own free PERSI search on the Genealogy Center website. ACPL staff compile PERSI, and this copy is the larger one. Findmypast still carries PERSI, with fewer entries but images of some articles, so use it as a second search and for those images. [S18], [S19] Talks recorded before 2022 (S3, S7, S14) describe older Findmypast or HeritageQuest interfaces, so don't rely on their screen or access details.
- **German indexes: each one indexes to a different depth.** One presenter describes the three indexes the same way across four talks:
  - **Der Schlüssel:** nine volumes, each with locality, subject and surname indexes. All three are drawn only from article titles. He adds that the surname index also covers authors and compilers. A surname that appears only inside an article, such as a name in an extracted town census, is not indexed. [S4], [S10], [S11]
  - **Familiengeschichtliche Quellen:** a surname index only. He says it covers every surname in every article. [S4], [S13]
  - **Quellenschau für Familienforscher:** separate town and district locality indexes, plus subject and surname indexes. He says that for the years it covers, it indexes surnames, places and subjects throughout the articles, not just in titles. [S4], [S13]
- **Record which periodicals and years each index covers, and search every index that overlaps.** The presenter's worked comparison for one periodical shows the three indexes overlapping for some years. Because each index works to a different depth, a miss in Der Schlüssel says nothing about what Quellenschau or Familiengeschichtliche Quellen hold for the same years. Search all of them. [S13]
- **Look up each numbered entry.** In Der Schlüssel, a locality entry does not list the surnames or subjects in the article, and a surname or subject entry does not give the places. The presenter shows item numbers that lead to the full entry. Looking up each number is the only way to see what the article covers. [S10], [S11]

- **Search GPAI as well for English-language periodicals of 1962–2001.** The Genealogical Periodical Annual Index is a separate printed index, published yearly from 1962 to 2001 and indexed by surname, location or topic [S36]. A Library of Congress guide, read in its 2009 capture, shows the depth changing by volume. Volumes 1–4 (1962–65) are arranged by broad subject, article title, principal surname, author and place. Volumes 5–8 (1966–69) are arranged by male personal name, place, subject and author. Volumes 13–30 (1974–91) are arranged by personal name (surname and given name), locality and topic. The guide lists volumes 9–12 as not yet published [S35]. A PERSI miss for those years says nothing about GPAI. Record which volumes you searched and how each was arranged, and don't treat a woman's name missing from volumes 5–8 as a negative. One presenter recommends GPAI for articles about the research area but calls it hard to use (partial read: transcript excerpts only) [S37].

## Build the query set from place, jurisdiction and event

- **Write the locality list first.** Before searching, list the ancestral place's jurisdictions: civil, parish, court or district, and region. Use the list for locality searches and when scanning tables of contents. [S12]
- **Search the surname, then the place with event terms.** Start with a surname search for articles about the family. Then search the place combined with record-type or topic terms. For a death, try death, died, burial, probate, will and cemetery. An article is filed under whatever title its author chose. [S8]
- **Don't search an individual's full name; search the topic.** This does not contradict the surname search above. Articles rarely name a particular ancestor in the title, so a query for one individual's name mostly returns nothing. Presenters give two worked examples: a county with "churches" or "ministers", and a town with "probate". [S9], [S14], [S15]
- **Keep queries short.** Each extra keyword narrows the results. A 2016 presenter said PERSI accepts asterisk wildcards. That describes an earlier interface, so test whether wildcards work in the current ACPL search before relying on them. [S7]
- **Don't search only the target place's own journals.** Material about one place can be printed in an unrelated region's periodical, for example as filler pages. Use a cross-periodical index. [S1], [S2]
- **Follow cross-references,** such as a region pointing to its sub-regions, through to further entry numbers. [S13]
- **Copy any qualifier printed after a place name exactly.** Examples are Kr. (Kreis, district) or an abbreviation for a cultural or topographical region. Resolve the qualifier in the Meyers gazetteer, which separates same-named places by Kreis, before tying the article to one place. In the teaching example, four places shared a name and the district qualifier identified which one was meant. [S11]
- **Treat an entry marked Rez. (Rezension) as a book review.** It points to a separately published book. Look for holdings of that book, for example in WorldCat. [S11]
- **Track authors.** Note the author of any relevant article and add that name to later surname searches. Authors often write more than one article about the same family or area. [S10], [S12]

- **Scan short PERSI surname hit lists before filtering.** Read the unfiltered titles for an unusual surname when the list is short. For a long list, put the place in the **Search Article Title** box under the **Article Title** column. Clear that filter and check the unfiltered list again when a relevant title could omit the place. [S38 @2026-11-18], [S39 @2026-11-18]

- **Browse PERSI's subjects within the locality.** For an English locality, open **British Isles**, choose England under **Country**, and enter the place in **County or City/Town** [S38 @2026-11-18], [S40 @2026-11-18]. For a U.S. county, open **United States**, choose the state, then choose the county [S38 @2026-11-18], [S41 @2026-11-18]. Open each relevant subject in the results. A county search starts from the articles indexed to that county, so follow it with a title-keyword pass for a distinctive town name. [S39 @2026-11-18]

- **Add PERSI's record types to place searches.** ACPL's PERSI handout lists the subject categories and record types PERSI uses: biographies, cemeteries, census, church, court records, deeds, directories, history, institutions, land, maps, military, naturalization, obituaries, passenger lists, school records, tax lists, vital records, voter lists, wills and other. Pair the place with each type that could record the event. Before narrowing, read the wording of the titles already in the results and take your next keywords from it, as the handout advises. [S31 @2026-11-16]

- **Use PERSI's Research Techniques to find how-to articles.** Start with the broad record type and narrow to the method or topic you need. Keep this search separate from a locality search for published records. [S38 @2026-11-18], [S39 @2026-11-18]

- **Use Article Title Keyword for distinctive places or events.** Enter a distinctive town name of at least five characters and scan the titles for the right town [S38 @2026-11-18], [S39 @2026-11-18], [S42 @2026-11-18]. When an event name brings up several occurrences, filter the **Article Title** column by the event year. Leave **Publication Year** alone and check the unfiltered titles for articles that omit the year. [S38 @2026-11-18], [S39 @2026-11-18]

- **When the original record is lost, look for a printed transcription.** Society periodicals printed abstracts and transcriptions of local records, cemetery transcriptions among them, and PERSI indexes those articles [S33], [S34]. An ACPL staff member tells of a researcher who found a transcription of records that later burned (partial read: transcript excerpts only) [S30]. Before reporting a destroyed record's content as lost, search the place with that record type. Cite and weigh what you find as a derivative of the lost original, not as the original.

## Carry every hit to the article

- **Privacy gate:** <!-- privacy-gate: contact --> A request to a publisher or society, a library, an interlibrary-loan service or ACPL sends the user's name, contact details and wanted citations outside the user's own account. Before sending one, answer the [privacy gate](../SKILL.md#privacy-gate) in writing for that destination. Send only the citation and the requester details the holder asks for, and nothing from the user's tree or about living relatives. Until the gate is answered, keep the request as an unsent draft on the user's device.
- **Record the full citation.** For each hit, record:
  - article title
  - periodical title
  - issuing society or publisher
  - volume and issue
  - year
  - the index's entry or item number

  A hit list is a list of citations to work through, not a set of findings. [S3], [S7], [S10], [S14]
- **Try retrieval routes and log each one.** Presenters name these routes:
  - an online copy found by searching the article title
  - the publisher or society
  - other repositories, such as FamilySearch holdings or a state memory project
  - WorldCat holdings and interlibrary loan
  - a copy order from ACPL. One presenter treats this as the fallback when no other copy turns up. The presenter describes emailing the citation to ACPL for a copy quote [S2]. ACPL's contact page, checked 2026-11-07, confirms <genealogy@acpl.info> for the Genealogy Center. [S20] Ask for the current article-order procedure and quote rather than treating the old form or fee as current.

  [S2], [S3], [S6], [S7], [S8], [S9]
- **Confirm ACPL's current order terms before relying on them.** Presenters in 2021–22 mentioned these terms, and none has been confirmed as current:
  - a fee per order form (S14)
  - about four to six weeks' turnaround (S8)
  - staff sometimes checking whether the person is named (S14)

  [S8], [S14]
- **Check each holding volume by volume.** Library and digitized runs often have gaps. A digitized run only shows the copies one repository held, and Google Books results do not list volumes in order. Record which volumes and issues each holding actually has. [S5]
- **Check the volume itself.** Once you have the volume, also check its table of contents and any surname index for the volume or issue. [S12]

- **Try retrieval routes in this order and log each one.** ACPL's PERSI handout puts the publisher first, a library that holds the periodical second and an ACPL order last, and says ordering from ACPL is not the fastest route [S31].
  - an online copy found by searching the article title, or a digitized issue on the publisher's or society's own website
  - **Privacy gate:** <!-- privacy-gate: contact --> A copy request to the publisher or society sends the user's name, contact details and the wanted citations to that publisher or society.
  - the publisher or society, at the contact details PERSI lists for the publisher in its results; ACPL calls a request to the publisher typically the fastest way to a copy [S31 @2026-11-16]. If the society has dissolved, go to the library routes; do not trace a former editor or member.
  - other repositories, such as FamilySearch holdings or a state memory project
  - **Privacy gate:** <!-- privacy-gate: contact --> A loan request sends the user's name, library account details and the wanted citations to the user's own library and, through it, to the lending library.
  - a library that holds the periodical. Search WorldCat for the periodical title, not the article title [S31], then visit a holding library or ask your own library for an interlibrary loan.
  - **Privacy gate:** <!-- privacy-gate: contact --> An article order sends the user's name and email address, the requested mailing address and the wanted citations to the ACPL Genealogy Center by email.
  - a copy order from ACPL, last (next bullet).

  ACPL staff add the publisher's own digitized issues and the WorldCat search by periodical title (partial read: transcript excerpts only) [S30]

- **Order from ACPL on its current article order form.** Open the [article order form](https://www.genealogycenter.info/pdf/Article-ORDER-FORM.pdf) and enter the full PERSI article and journal titles for up to six articles per form [S38 @2026-11-18], [S32 @2026-11-18]. ACPL's handout directs you to email the completed form to <genealogy@acpl.info> and lists $7.50 per order plus $0.20 per copied page, excluding the cover or title page [S31 @2026-11-18]. The posted form calls for prepayment of the $7.50, asks you to allow six to eight weeks and rules out orders by phone [S32 @2026-11-18]. Confirm payment timing in the order inquiry before sending money.

If a PERSI heading is missing from the cited issue's table of contents, first confirm the journal,
volume and issue, then inspect the complete cited issue for the indexed subject. The ACPL
presentation explains that indexers sometimes create a title for an untitled passage. Preserve
the index heading separately from the printed passage and its page locator; a TOC miss alone
does not close the enquiry. [S16]

When the citation or inspected article suggests continuation in another issue, identify the
additional parts in the copy request. If the extent is unclear, ask the holder whether it
continues and which parts the request covers. Record each supplied or still-outstanding part;
one indexed citation or one received copy does not establish that every instalment was obtained. [S17]

## When a Russian periodical has no index: full text or the paper run

For Russian newspapers and provincial gazettes, look for a full-text search of the recognised page text, or go to the paper run. Full text searches every recognised word, not only the terms an index recorded. Yandex's Поиск по архивам (yandex.ru/archive) searches text that its neural networks recognised; on 2026-11-15 its newspaper projects covered «Вечерняя Москва», the periodicals of 1941–1945 and «Советский спорт» from 1922, and viewing documents needed a signed-in account [S21 @2026-11-15]. In February 2025 it added «Известия» for 1917–2024 in full text and named diocesan gazettes and «Русский инвалид» among its other periodicals [S22 @2026-11-15]. For Siberia and the Far East, Tomsk State University's library runs PRO Сибирь, with more than 120,000 open-access sources, periodicals and manuscripts among them [S23 @2026-11-15]; a family historian recommends both services and PRO Сибирь's keyword search [S24 @2026-11-15]. Search an event, place or surname instead of reading issue by issue, and read the page image of every hit. Recognised text misreads, so a miss there is not a negative.

A provincial gazette (губернские ведомости) can name individuals. A Tula genealogist lists printed lists of conscripts, voters and candidates for elected posts, and notices of property sales, awards and incidents, in «Тульские губернские ведомости»; a newspaper run one reader needed at the Tula Regional Scientific Library was not digitised and took staff time to find on paper [S25 @2026-11-15]. The library holds the gazette, which ran until 12 April 1917, in print and on microfilm [S26 @2026-11-15]. Check which years of a gazette are digitised before searching, and plan a microfilm or paper search of the library's run for the rest.

Two library finding aids show which Russian newspapers are digitised and where. The Presidential Library's collection «Отечественная периодика в фонде Президентской библиотеки» (prlib.ru/collections/684567) listed 190 newspaper and 223 journal titles on 2026-11-16, from imperial runs such as «Правительственный вестник» (1869–1917) to Soviet ones, most of them in full text [S27 @2026-11-16]. The National Library of Russia's guide «Газеты в сети и вне её» lists digital copies of newspapers by title and by place of publication, has chronological, geographical and language sections, and points to printed newspaper bibliographies and the largest newspaper holdings for titles that are not online [S28 @2026-11-16].

A family historian who recommends both reports that digitisation is slow and that a catalogue often says an issue can be read only in the reading room [S29]. Record such an issue as held but unread, not as lost, and note the reading room that holds it.

## Report bounded results

- **No hits:** report a no-hit as no match in the named index and the sections or fields you actually searched (for example "no PERSI title/author/assigned-subject match" or "no entry in the Familiengeschichtliche Quellen surname index"). Give the index's depth, the periodical years it covers and the queries you ran. It does not mean no article mentions the person.
- **Hits:** report a hit as a lead until you have retrieved and read the article. Report what the article contains only after reading it, and say it names the ancestor only after you have found the person in it. A title, an index subject or an entry in the place's locality index does not show that the ancestor is named.
- **Deliverables:**
  - a query log for each index
  - the citation list
  - a retrieval register: route, holding, volumes held, and whether you retrieved the article
  - findings from articles you have read, kept separate from the bounded no-hit statements

  Send identity questions to [evidence/proof judgment](evidence-proof-judgment.md).
