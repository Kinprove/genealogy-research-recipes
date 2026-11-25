---
id: "us-obituary-search-and-interpretation"
title: "Find and interpret obituaries in U.S. newspapers"
summary: "Judge whether a U.S. obituary should exist, find it through relatives' notices, cards of thanks and funeral cards, and read it as an informant's account."
kind: "records"
scope: {"platforms": [], "tasks": ["death notice", "survivors list", "sibling's or child's obituary", "remarried woman's later surname", "incomplete or embellished obituary"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "US-OBITUARY-SEARCH-AND-INTERPRETATION-01", "text": "Read every name, date and relationship in an obituary as the informant's statement, not as a verified fact."}, {"id": "US-OBITUARY-SEARCH-AND-INTERPRETATION-02", "text": "A missing spouse, child, sibling, employer or military service is not evidence that none existed."}, {"id": "US-OBITUARY-SEARCH-AND-INTERPRETATION-03", "text": "Do not use it to look up a survivor's current address, phone, email, workplace or accounts, and do not trace a minor named in it."}]
handoff: ["newspapers-com-search-recovery", "evidence-proof-judgment", "burial-evidence-packet", "dna-match-outreach-staging"]
checked: "2026-11-16"
checked_basis: "read 2026-11-16"
capabilities: {"browse": ["newspaper archives, obituary indexes and original page images"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool"], "contact": ["contact"]}
router: {"section": "Records by country and region", "group": "United States: people, vital and church records", "order": 230}
---

# Find and interpret obituaries in U.S. newspapers

Use this recipe when you need a U.S. newspaper obituary or death notice for a person, when a search for one has failed, or when you are reading one for names, dates and relationships. It sets what kind of notice to expect, adds the relatives' notices and family papers that can stand in for a missing one, and reads the notice as an informant's account. For search mechanics, including "Mrs." with the husband's given name or initials, OCR misreadings, issue coverage, neighbouring titles and estate notices, use [newspaper search recovery](newspapers-com-search-recovery.md). For kinship rulings, use [evidence/proof judgment](evidence-proof-judgment.md). For the grave and the cemetery's records, use [burial evidence packet](burial-evidence-packet.md).

## Contents

- What goes wrong
- 1\. Set the expectation before you search
- 2\. Search the relatives' obituaries
- 3\. Search past the week of death
- Find the original issue through an obituary index
- Ask the holding library for an issue
- 4\. Ask about funeral and memorial cards
- 5\. Read the notice as the informant's account
- 6\. Keep living survivors to the family question
- Return packet

## What goes wrong

- Calling a search negative when no full obituary should be expected. Early-1800s death notices seldom gave more than the name, age and residence, and large nineteenth-century city papers carried less on fewer residents than rural and small-city papers. [S2] Not everyone had an obituary. [S3]
- Searching only for the person's own notice. A sibling's or child's obituary can name the parents, the mother's maiden name and a woman's later married surname. [S1], [S4], [S5]
- Stopping at the week of death. A card of thanks can appear right after the funeral or much later. [S6]
- Taking stated relationships as verified. Most obituaries are not checked for accuracy, and survivors lists can mislabel or leave out relatives. [S1], [S3], [S7], [S8]
- Reading praise as a balanced biography, or a missing detail as proof that it never existed. [S1], [S9], [S10]

## 1. Set the expectation before you search

Before you search, write down what kind of notice the date and place make likely, so that a miss is read correctly.

- **An early death.** Allow for there being no obituary at all [S1]. Early-1800s death notices seldom gave more than the name, age and residence, and the biographical obituary developed mainly after the Civil War [S2]. In the nineteenth century, prominent citizens received long tributes while working-class notices stayed brief [S9].
- **A large city.** Expect less on an everyday resident. Nineteenth-century papers in cities such as New York, Chicago and St. Louis carried less information on fewer residents than papers in rural communities and small cities [S2], and small-town papers often gave obituaries considerable space [S9]. Add the papers of neighbouring smaller communities before you call the search negative [S1], choosing them as [newspaper search recovery](newspapers-com-search-recovery.md) directs.
- **Any date.** Not everyone had an obituary [S3]. Record a miss as "no notice found" in the titles and issues you checked, not as "no obituary".

Browse death columns in papers from the person's documented former residences as well as the place of death. Include a former hometown even when it is outside the region where the person died [S34], [S35].

Include nearby titles across the state line when a search around the place of death comes up empty. A researcher reported finding a New Jersey decedent's obituary in a nearby Pennsylvania paper [S62].

When testing a claim of Boston Tea Party participation, browse nineteenth-century death columns, including those headed `DIED`, for wording that ties the person to the destruction of the tea [S36], [S37]. Record what role the notice claims, including whether the person took part or witnessed the event, and check that role against an independent account [S37].

## 2. Search the relatives' obituaries

When the person's own notice is missing or thin, or names a woman only through her husband, search the obituaries of every sibling, child and spouse, not only those of direct ancestors [S1], [S3].

- **A woman missing under her own name.** If a pre-1850 federal population schedule names only the head of household, a wife may appear only in a tally [S11]. Look for her in her children's obituaries [S1]. Search by the full name of a surviving child or sibling, or by her married surname with a daughter's or sister's married surname. Her married and maiden names together can find notices that list her parents or surviving brothers [S4].
- **An unknown remarriage.** If the expected surname fails, look for the surname she had at death [S5]. Allow for a remarriage you do not know about, and take her later surname from a child's or sibling's survivors list [S1]. A survivors list can give daughters' and sisters' married surnames [S5].
- **Parents and the mother's maiden name.** Search siblings' obituaries for the mother's name [S1]. In one notice Neill found that the surname attributed to the mother appeared to belong to the grandmother, possibly as her middle name [S7]. Keep the printed name under the stated generation and test both generations against marriage and birth records.
- **Full and half siblings.** Compare each parent's children across marriages with the people named in the notice. In Neill's case the four listed siblings were three full siblings and one maternal half-sibling. Six paternal half-siblings were omitted [S8]. Record the relationship each notice actually gives and check parentage separately for every sibling.

For a first cousin who is hard to place in historical records, check the survivors lists in the obituaries of the cousin's deceased parents and grandparents [S61]. Treat the printed relationship as a lead. Use the gated index search below if you need to retrieve a notice, and apply §6 to any living survivor.

## 3. Search past the week of death

Search the death notices and obituaries in the issues around the week of death [S1], then widen the window and record its limits in the search log. An obituary could take time to be written and submitted [S2], and a card of thanks, in which the family thanked the community, may appear right after the funeral or much later [S6]. Cards of thanks tied to deaths appear from the later nineteenth century; the earliest that the GenealogyBank author found is from 1879 [S6].

Read a card of thanks for relationships and leads. It may describe the deceased as a wife and mother, or a survivor as a widow, which helps date a husband's death. It may give a wife's maiden name, a minister and church, or an employer and lodges [S6]. Relatives may appear only by initials or by relationship, so search for those forms too [S6].

Keep comparing notices after a one-line hit. Copy the birthplace, church and date wording from each notice that supplies them [S62]. Resolve “the 5th inst.” as the fifth of the month in the dated notice and record the resolved date as an inference. If the item was reprinted from an earlier issue, establish the original notice's date before resolving it [S63].

## Find the original issue through an obituary index

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The query sends the deceased subject's public name or the paper title and issue date to MyHeritage, JewishGen, Ancestry, the Kansas Historical Society, the relevant library index, OldNews, Chronicling America, or another newspaper archive.

Search the index by the confirmed deceased person's public name after answering the privacy gate in `SKILL.md`. Limit outbound searches to that name and, for the issue lookup, the newspaper title and publication date. Keep survivors' details and private research notes local.

Use the newspaper title and publication date from the hit to open that issue, even when the date of death differs. If the hit gives a page or column, go straight there. Read the notice and any accompanying caption on the original page, and record what the text actually attributes. Keep the index entry as a locator [S13], [S14], [S29].

Search Ancestry's *Web: Obituary Daily Times Index, 1995–2016* for notices in that date range. If the hit gives a publication place and date without a title, check the papers serving that place on that date. For a later notice, go to the relevant local index or newspaper issues [S39 @2026-11-21], [S40 @2026-11-21].

When an index supplies an inferred death year, label it as an inference and copy the exact publication date into its own field [S71]. Check the dated notice for an explicit death date [S102].

For a U.S. issue lookup on OldNews.com, check the U.S. title list for the publication's place and name, then check whether the issue date is available. Open the dated issue and read the notice on the page [S64 @2026-11-22], [S65 @2026-11-22].

Check Chronicling America for the U.S. title and issue date. If the issue is absent from the digitized pages, check the Library of Congress's Directory of U.S. Newspapers in American Libraries for a holding library [S66 @2026-11-22], [S67 @2026-11-22].

Choose the index for the paper and locality. Use indexed dates, places and family names to sort candidates in the private log.

- **Alabama, Madison County.** Use the Huntsville-Madison County Public Library Obituary Index. Compare any cemetery or newspaper supplied by the hit, then take its newspaper citation to the issue [S71 @2026-11-22], [S72 @2026-11-22].

- **Alabama, Tuscaloosa County.** MyHeritage's county index points to *Tuscaloosa News* notices from 1942 onward. Use age at death and death date to distinguish candidates, then use the publication date to retrieve the issue [S14 @2026-11-18], [S15 @2026-11-18].

- **California, Berkeley.** Use Berkeley Public Library's *Berkeley Daily Gazette* obituary index. Check its listed years before treating a miss as evidence about the paper, and browse the dated issues directly for years the list omits [S73 @2026-11-22], [S74 @2026-11-22].

- **Colorado, Mesa County.** Use the Mesa County Libraries catalog's obituary results. Compare birth and death dates, then use the listed publication date and page to pull the *Daily Sentinel* page on microfilm [S75 @2026-11-22], [S76 @2026-11-22].

- **Colorado, Pueblo County.** MyHeritage's county index points to *The Pueblo Chieftain* notices from 1868 onward. Carry the publication date into the newspaper search [S14 @2026-11-18], [S16 @2026-11-18].

- **Connecticut, Fairfield County.** MyHeritage's county index lists records from 1830 onward and typically gives the deceased's name and publication date. If the hit gives a date alone, use it to check the likely titles and leave the paper unidentified until you find the notice [S13 @2026-11-18], [S17 @2026-11-18].

- **Florida, Sarasota County.** For a *Sarasota Herald-Tribune* notice, use the library's text archive to locate a dated issue when it covers the period. For the original page, check Selby Public Library's microfilm dates and issue gaps [S77 @2026-11-22], [S78 @2026-11-22].

- **Idaho, Boise.** MyHeritage's Boise index starts in 1957 and points to the *Idaho Statesman* and *Idaho Daily Statesman*. Use the title on the hit [S13 @2026-11-18], [S18 @2026-11-18]. Boise Public Library's *Idaho Statesman* index supplies publication dates for 1957–2017 [S19 @2026-11-18].

- **Illinois, statewide.** MyHeritage's *Illinois Obituaries* index starts in 1831, with entries concentrated in the *Chicago Daily News*, *Illinois State Journal*, *Chicago Tribune* and *Denni Hlasatel*. Use the publication place and date to narrow the issue search, checking which papers actually served that place [S46 @2026-11-21], [S47 @2026-11-21].

- **Illinois, Cook County.** Use Oak Lawn Public Library's Local History Obituary Index for coverage from 1985, including the *Oak Lawn Independent* and *Southtown*. Use the title returned by the index to select the dated issue [S79 @2026-11-22], [S80 @2026-11-22].

- **Illinois, Kane County.** MyHeritage's county index lists entries from 1850. Use the publication date to pick the issue. Check the Illinois Newspaper Project's Aurora holdings for the title in use that year, including the *Aurora Beacon* for early dates [S46 @2026-11-21], [S48 @2026-11-21], [S49 @2026-11-21].

- **Illinois, Kankakee County.** Use Kankakee Public Library's Regional Obituary Index for the *Kankakee Daily Journal* and its predecessors. Use the page number with the publication date. Before about 1950, expect scattered entries and check the issue directly [S77 @2026-11-22], [S81 @2026-11-22].

- **Indiana, Hendricks County.** Use MyHeritage's county index for entries from 1872 onward. Compare the burial place and spouse when supplied, then use the paper and publication date on the hit [S14 @2026-11-18], [S20 @2026-11-18].

- **Indiana, LaPorte County.** Use MyHeritage's *Indiana, LaPorte County Obituaries* index for entries from 1880. Take the publication date together with the title on the hit because the index draws from several newspapers [S71 @2026-11-22], [S82 @2026-11-22].

- **Indiana, Lake County.** Look for the *Post Tribune*, *Lake County Star* and *Crown Point Register* [S13 @2026-11-18] in Lake County Public Library's title-specific indexes and corresponding microfilm. Check the *Post Tribune* issues directly for 1987–1989, when its online index is incomplete [S21 @2026-11-18].

- **Indiana, Monroe County.** Use Monroe County Public Library's index for Bloomington newspapers, 1824–2019. If the entry cites *The Christian Record*, check the library's vertical file for the notice [S87 @2026-11-22], [S109 @2026-11-22].

- **Indiana, Porter County.** MyHeritage's county index includes *The Northwest Indiana Times* and *The Valparaiso Vidette Messenger* notices from 1913 onward. Compare the death date in the private log, then open the title and issue dated on the hit [S41 @2026-11-21], [S42 @2026-11-21].

- **Indiana, Wabash Valley.** Use Vigo County Public Library's Wabash Valley obituary index and keep the newspaper title with the publication date to identify the issue [S89 @2026-11-22], [S110 @2026-11-22].

- **Indiana, Wells County.** Compare birth and death details, cemetery, parents, spouse and marriage date when present on a MyHeritage county index hit. Use its publication date to locate the notice [S46 @2026-11-21]. Search Wells County Public Library's downloadable Cem-Obit spreadsheet locally for marriage or plot details and whether a notice was scanned [S50 @2026-11-21].

- **Iowa, Pottawattamie County.** Use the Council Bluffs and Pottawattamie County Obituary Index at Council Bluffs Public Library for Council Bluffs and other southwest Iowa newspapers. Carry any title and publication date into the issue search [S77 @2026-11-22], [S83 @2026-11-22].

- **Kansas, Johnson County.** Use the JoCoHistory Obituary Index. Keep each entry for the same death as a separate newspaper locator and use the title, issue date and page to pull the notice on microfilm [S75 @2026-11-22], [S84 @2026-11-22].

- **Kansas, McPherson County.** Use MyHeritage's county index for its newspaper title and issue date. McPherson Public Library's local newspaper microfilm starts in 1872. Base the issue search on the cited paper and issue date, since the collection's stated 1841 start predates the county's first newspaper [S13 @2026-11-18], [S22 @2026-11-18], [S23 @2026-11-18], [S24 @2026-11-18].

- **Kansas, Shawnee County.** Use Topeka & Shawnee County Public Library's Obituary Index for Topeka newspapers from 1906. For an earlier death, go to the dated issues of the relevant title [S85 @2026-11-22], [S86 @2026-11-22].

- **Kansas, fraternal notices.** For a lodge lead, compare residence and death date in MyHeritage's *Kansas, Fraternal Order Death Notices* index, dated 1860–1969 [S58 @2026-11-21], [S59 @2026-11-21]. Search the Kansas Historical Society's fraternal order index by the deceased person's public name for the order and lodge. Use its coverage by order and proceedings call numbers to locate the original notice in the order's proceedings [S60 @2026-11-21].

- **Kentucky, Boyd County.** Use Boyd County Public Library's obituary index to find the dated *Ashland Daily Independent* issue. In 1998–2005, the index took the first appearance of a name, so browse nearby issues for later notices [S87 @2026-11-22], [S88 @2026-11-22].

- **Kentucky, Daviess County.** Use the Daviess County Public Library's Owensboro Area Obituary Index for Owensboro papers. Use the indexed obituary date and expand the source code before looking up the issue. MI identifies the *Owensboro Messenger & Inquirer*, OM the *Owensboro Messenger*, and OI the *Owensboro Inquirer* [S13 @2026-11-18], [S25 @2026-11-18].

- **Kentucky, Henderson County.** Use Henderson County Public Library's *Henderson Gleaner* obituary index for coverage from 1956. For earlier notices, check the library's newspaper holdings for the dates and titles needed [S87 @2026-11-22], [S111 @2026-11-22].

- **Louisiana, statewide.** MyHeritage's Louisiana index starts in 1809 and includes the *Times-Picayune*, *The Advocate* and the *Lake Charles American Press*. Compare residence, death date, age and spouse in the private log. Use the exact paper on the hit with the publication date, including when the hit names the *New Orleans States* or the *New Orleans Item-Tribune* [S46 @2026-11-21], [S51 @2026-11-21].

- **Louisiana, Ouachita Parish.** Use Ouachita Parish Public Library's Obituary Index for Monroe-area newspapers. Take the paper and issue date, plus any page and column supplied, to the original microfilm [S89 @2026-11-22], [S90 @2026-11-22].

- **Maryland, Washington County.** MyHeritage's county index lists entries from 1790. Use the paper title and publication date to locate the issue [S41 @2026-11-21], [S43 @2026-11-21]. For Hagerstown notices, also check the Washington County Free Library's Obituary Locator [S44 @2026-11-21].

- **Massachusetts, Boston.** MyHeritage's Boston index starts in 1932 and includes the *Boston Globe*, *Boston Herald* and *Boston Evening Transcript*. Compare residence and death date in the private log. Use the indexed paper and publication date to choose the issue [S41 @2026-11-21], [S45 @2026-11-21].

- **Michigan, statewide.** Use MyHeritage's *Michigan Obituaries, 1850–2006* for a statewide lead. Compare the birth and death details and any named relatives in the private log. Use the date and place of the obituary to identify the issue [S91 @2026-11-22], [S92 @2026-11-22].

- **Michigan, Genesee County.** Use MyHeritage's county index for *Flint Journal* notices from 1920 onward. Use the death date to distinguish hits and the publication date to pull the issue [S46 @2026-11-21], [S52 @2026-11-21].

- **Michigan, Macomb County.** Use Mount Clemens Public Library's Macomb County Obituary Index for coverage from 1941 with some earlier entries. For a miss in an earlier year, browse the relevant newspaper issues [S71 @2026-11-22], [S93 @2026-11-22].

- **Michigan, Monroe County.** Use the Monroe County Library System's Obituary Search. For the *Monroe Commercial*, also check the library's separate year-by-year obituary lists for 1870–1879 [S85 @2026-11-22], [S94 @2026-11-22].

- **Michigan, Saginaw County.** Use the Public Libraries of Saginaw Obituary Index for a newspaper citation, then open the dated notice before recording relationships [S87 @2026-11-22], [S113 @2026-11-22].

- **Minnesota, St. Louis County.** Use Duluth Public Library's obituary index for *Duluth News Tribune* notices from 1942. Follow the cited publication date into the microfilm [S87 @2026-11-22], [S95 @2026-11-22].

- **New Hampshire, Merrimack County.** Use Concord Public Library's *Concord Monitor* obituary index for 1948 through January 2015 and check its coverage before relying on a miss. Use the publication date to locate the notice [S73 @2026-11-22], [S97 @2026-11-22].

- **New Hampshire, Strafford County.** Check the dated microfilm at Dover Public Library for both *Foster's Daily Democrat* and *Foster's Weekly Democrat*. Start with the weekly run in 1894. The daily run resumes in 1895 after a gap [S75 @2026-11-22], [S96 @2026-11-22].

- **New York, Chemung County.** MyHeritage's 1900–1968 county index draws chiefly from the *Elmira Star-Gazette*. Compare the death date and use the publication date to check the paper. Check other local titles if the hit leaves the title unclear and the notice is missing from the dated *Star-Gazette* issue [S46 @2026-11-21], [S53 @2026-11-21].

- **New York, Herkimer County.** Use MyHeritage's county index for *Herkimer Evening Telegram* notices from 1924 onward. Compare the recorded death place and take the publication date to the original issue [S46 @2026-11-21], [S54 @2026-11-21].

- **New York, Monroe County.** Use Rochester Public Library's Life Records death and obituary indexes for Rochester newspapers. Check its title-specific dates and keep the newspaper locator with the hit [S71 @2026-11-22], [S98 @2026-11-22].

- **New York, Steuben County.** MyHeritage's county index lists entries from 1860. Compare the birth and death years and burial place. If the hit leaves the paper or issue date unknown, check the county historian's published obituary list locally or use the death year to narrow a search of local issues [S46 @2026-11-21], [S55 @2026-11-21], [S56 @2026-11-21].

- **North Carolina, Johnston County.** Use the Johnston County Heritage Center obituary index for selected regional newspapers from 1801. Expand the title code where given and use the publication date to pull the issue [S77 @2026-11-22], [S99 @2026-11-22].

- **North Carolina, Randolph County.** Use the Randolph Room's index for the *Courier* and *Courier-Tribune* from 1903 onward. Find the deceased's name within the relevant year list, then use the newspaper date and page to locate the notice in the corresponding microfilm [S46 @2026-11-21], [S57 @2026-11-21].

- **Ohio, Columbiana County.** MyHeritage's county index points to the *Salem News*, with entries dated from 1934 and occasional parent and spouse names. Use the publication date to locate the issue [S13 @2026-11-18], [S26 @2026-11-18]. Check the Salem Public Library's gap list before relying on a miss in its local index [S27 @2026-11-18].

- **Ohio, Lucas County.** Use Toledo Lucas County Public Library's Obituary Index for Toledo-area papers, including *The Blade*. Start with the deceased person's public first and last name and use the newspaper citation to locate the issue [S89 @2026-11-22], [S100 @2026-11-22].

- **Ohio, Montgomery County.** Use Dayton Metro Library's Dayton Obituary and Genealogy Database for death notices and obituaries. Check the listed year ranges before relying on a miss, then take the newspaper locator from the hit to the original [S79 @2026-11-22], [S101 @2026-11-22].

- **Ohio, Williams County.** Use MyHeritage's county index for entries from 1863 onward. Keep the paper title with the publication date so you open the right issue [S14 @2026-11-18], [S28 @2026-11-18].

- **Pennsylvania, Allentown.** Search Allentown Public Library's *Morning Call* obituary spreadsheets locally for 1895–1983. Use the publication date and page to pull the microfilm. Use the library's linked searchable archive for 1984 onward [S71 @2026-11-22], [S102 @2026-11-22].

- **Pennsylvania, Butler County.** Use Butler Area Public Library's newspaper index for 1818–2019. Check the item type on the hit because the database includes notices and other newspaper articles. Use its citation to find the issue [S85 @2026-11-22], [S112 @2026-11-22].

- **Pennsylvania, Centre County.** Use the *Centre Daily Times* obituaries database linked by Penn State University Libraries for coverage from 1920. Use the obituary date to find the corresponding newspaper issue [S89 @2026-11-22], [S103 @2026-11-22].

- **Pennsylvania, Philadelphia.** Search the *Philadelphia Jewish Exponent* obituary index on MyHeritage or JewishGen by the deceased person's public name. Compare age at death and birthplace when supplied. The index spans 1887–2013 with gaps. On a miss, check JewishGen's coverage list and go directly to issues in the gaps [S30 @2026-11-20], [S31 @2026-11-20], [S32 @2026-11-20]. Use the publication date and any page number to locate the original through Temple University's *Jewish Exponent* holdings guide [S33 @2026-11-20]. If JewishGen shows `Nerc'y` in the page field, browse the necrology in the dated issue [S32 @2026-11-20].

- **Tennessee, Knox County.** Use Knox County Public Library's later Knoxville obituary index for the *Knoxville Journal* in 1991 and the *Knoxville News Sentinel* from 1991. Open the title and issue the hit identifies [S75 @2026-11-22], [S104 @2026-11-22].

- **Washington, Spokane County.** Use Spokane Public Library's obituary search for publication, date and page. For 1940–1979, also check the linked Lee Patchen index to search Spokane papers for that period [S79 @2026-11-22], [S105 @2026-11-22].

- **Washington, Tri-Cities.** Search Mid-Columbia Libraries' downloadable 1905–2020 obituary list locally. Check the named paper on the entry, which can be the *Tri-City Herald*, *Kennewick Courier Reporter* or *Pasco Herald Express* [S87 @2026-11-22], [S106 @2026-11-22].

- **Wisconsin, Outagamie County.** For Appleton papers, use Appleton Public Library's partial index and take the publication date, section and page to the original issue [S89 @2026-11-22], [S107 @2026-11-22].

- **Denominational newspapers.** For an Evangelical Association or Evangelical Church lead, use Allen County Public Library's *Evangelical Messenger Obituary Index*, January 1848 through December 1946. Compare the spouse in the private log and use the issue reference to find the notice [S73 @2026-11-22], [S108 @2026-11-22].

## Ask the holding library for an issue

If the issue is held locally and you cannot read it yourself, check whether the holding library has a dedicated obituary lookup. Confirm the title and issue coverage, what date precision the library requires, and any copying or mailing fees before preparing the request [S68 @2026-11-22], [S69 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: contact --> The request sends the deceased person's public name and the exact death date or newspaper citation, plus the user's name and reply details if required, to the holding library's staff.

After answering the privacy gate in `SKILL.md`, request an obituary lookup for the confirmed deceased person through the library's published reference channel. Give the deceased person's public name and the exact death date or newspaper citation the service asks for. If all you have is an approximate date, check whether the service will search that window before sending. Keep the draft local until the gate is answered [S68], [S69].

## 4. Ask about funeral and memorial cards

Ask the user whether family papers hold a funeral or memorial card for the person [S1]. Early cards told family and friends of the death and of the funeral and burial services; later cards were handed out at the wake, funeral and interment as keepsakes. They give birth and death dates and places and sometimes family members' names, some larger cards carry a photograph, and a card can lead to the funeral home, church and cemetery [S12]. Record what the card actually carries; do not assume that it reproduces the obituary.

**Privacy gate:** <!-- privacy-gate: contact --> A message asking about the card sends the user's name and the research question about the deceased and their family to a living relative or family friend.

Asking a relative or family friend who attended the funeral whether they kept a card [S1] contacts a living person and tells them about the user's research. Use only a route the user already has, or a relative who agrees to pass the message on. Apply the consent, disclosure and log rules of [DNA match outreach staging](dna-match-outreach-staging.md), skipping the parts that apply only to DNA tests, and answer the privacy gate in `SKILL.md` before the message is sent. Until then the message stays an unsent draft on the user's device.

## 5. Read the notice as the informant's account

Read every name, date and relationship in an obituary as the informant's statement, not as a verified fact. Note who supplied the information where the notice or the funeral home shows it, and correlate each fact with an independent record before you rely on it.

Errors can enter at each step, from the informant to the funeral home to the newspaper [S1]. Most obituaries are not checked for accuracy, stated relationships may be wrong, and a poorly edited survivors list can be read in more than one way [S3]. In the nineteenth century, many notices were written by editors or ministers rather than by the family, and names could be misspelled or abbreviated [S9].

Check the relationship label against a record that identifies the same people in another role. Eliza Bryant's Atlanta death notice listed her children as her brothers and sisters [S1]. Compare each relative's own notice as well. Neill found that the named relatives and their stated relationships could differ between notices in a family with remarriages or divorces [S7].

A missing spouse, child, sibling, employer or military service is not evidence that none existed. When a notice mentions two marriages but gives no outcome for the first, search for both a death and a divorce before assigning an end date [S10]. Record the omission with the printed wording. Space, cost and the informant's knowledge can affect what the family includes [S1], [S10].

Read praise as a portrait, not as a balanced biography. Editors sometimes embellished lives, especially those of prominent people, and left out less flattering details [S9]. The MyHeritage author finds that obituaries show the deceased in the best light and may leave negative events out [S1]. Silence in an obituary does not show that nothing adverse happened.

Record the publication place, the place of death, the person's residence and the intended burial place in separate fields. Preserve any stated reason for being away from home. In the transcribed *Työmies* notice of 4 March 1913, a Laurium resident died while visiting South Range and the notice gave Laurium as the intended burial place [S70].

If a MyHeritage Johnston County hit has a Notes field, read it for the stated place of death, family and burial clues [S77]. Keep the publication place in its own field. In the Johnston County example, the notes place the death in London while the publication locator points to North Carolina [S77]. Compare the Notes with the original notice retrieved through the Johnston County locator above [S99].

If a Civil War veteran's obituary mentions later writing or work on the war, search for the memoirs, other published work and veterans' organization records to test the reported postwar activity. Use the work's title page or catalog record to establish authorship and publication [S114], [S115].

When a family story attributes a death to an accident abroad, compare the death notice with news coverage around the death and around the reported accident. Record the date and attributed cause of death, then date the earlier episode and any reported return separately. A corroborated return and a later death notice can overturn a claim that the person died on the trip [S38]. Check whether the death coverage actually links the accident to the death [S35], [S38].

## 6. Keep living survivors to the family question

A recent obituary's survivors list names living people and often where they live. Use it only for the family question. Do not use it to look up a survivor's current address, phone, email, workplace or accounts, and do not trace a minor named in it. The Living people rule in `SKILL.md` applies. Keep living survivors' names in the private research log.

## Return packet

- An expectation note: date and place of death, the expectation set in §1, the titles and issues checked, and any miss worded as "no notice found" in those titles and issues.
- A notice table: one row per obituary, death notice or card of thanks, with whose notice it is and their relationship to the subject, newspaper or proceedings title, date and page, and the names and relationships transcribed as printed.
- The reported publication place, place of death, residence and intended burial place. Keep the source wording for any inferred event date or reason the person was away.
- Leads from each notice, labelled with that notice: parents, the mother's maiden name, women's later surnames, church, employer, lodge and funeral home.
- Conflicts and gaps: relationships that differ between notices, relatives missing from a survivors list, and siblings not marked as full or half.
- Any funeral or memorial card: who holds it and what it carries. A request to a relative stays marked as an unsent draft until the privacy gate is answered.
