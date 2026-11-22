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
router: {"section": "Records by country and region", "group": "United States: people, vital and church records", "order": 126}
---

# Find and interpret obituaries in U.S. newspapers

Use this recipe when you need a U.S. newspaper obituary or death notice for a person, when a search for one has failed, or when you are reading one for names, dates and relationships. It sets what kind of notice to expect, adds the relatives' notices and family papers that can stand in for a missing one, and reads the notice as an informant's account. For search mechanics, including "Mrs." with the husband's given name or initials, OCR misreadings, issue coverage, neighbouring titles and estate notices, use [newspaper search recovery](newspapers-com-search-recovery.md). For kinship rulings, use [evidence/proof judgment](evidence-proof-judgment.md). For the grave and the cemetery's records, use [burial evidence packet](burial-evidence-packet.md).

## Contents

- What goes wrong
- 1\. Set the expectation before you search
- 2\. Search the relatives' obituaries
- 3\. Search past the week of death
- Find the original issue through an obituary index
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

## Find the original issue through an obituary index

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The query sends the deceased subject's public name or the paper title and issue date to MyHeritage, JewishGen, Ancestry, the Kansas Historical Society, the relevant library index, or the newspaper archive.

Search the index by the confirmed deceased person's public name after answering the privacy gate in `SKILL.md`. Limit outbound searches to that name and, for the issue lookup, the newspaper title and publication date. Keep survivors' details and private research notes local.

Use the newspaper title and publication date from the hit to open that issue, even when the date of death differs. If the hit gives a page or column, go straight there. Read the notice and any accompanying caption on the original page, and record what the text actually attributes. Keep the index entry as a locator [S13], [S14], [S29].

Search Ancestry's *Web: Obituary Daily Times Index, 1995–2016* for notices in that date range. If the hit gives a publication place and date without a title, check the papers serving that place on that date. For a later notice, go to the relevant local index or newspaper issues [S39 @2026-11-21], [S40 @2026-11-21].

Choose the index for the paper and locality. Use indexed dates, places and family names to sort candidates in the private log.

- **Alabama, Tuscaloosa County.** MyHeritage's county index points to *Tuscaloosa News* notices from 1942 onward. Use age at death and death date to distinguish candidates, then use the publication date to retrieve the issue [S14 @2026-11-18], [S15 @2026-11-18].

- **Colorado, Pueblo County.** MyHeritage's county index points to *The Pueblo Chieftain* notices from 1868 onward. Carry the publication date into the newspaper search [S14 @2026-11-18], [S16 @2026-11-18].

- **Connecticut, Fairfield County.** MyHeritage's county index lists records from 1830 onward and typically gives the deceased's name and publication date. If the hit gives a date alone, use it to check the likely titles and leave the paper unidentified until you find the notice [S13 @2026-11-18], [S17 @2026-11-18].

- **Idaho, Boise.** MyHeritage's Boise index starts in 1957 and points to the *Idaho Statesman* and *Idaho Daily Statesman*. Use the title on the hit [S13 @2026-11-18], [S18 @2026-11-18]. Boise Public Library's *Idaho Statesman* index supplies publication dates for 1957–2017 [S19 @2026-11-18].

- **Illinois, statewide.** MyHeritage's *Illinois Obituaries* index starts in 1831, with entries concentrated in the *Chicago Daily News*, *Illinois State Journal*, *Chicago Tribune* and *Denni Hlasatel*. Use the publication place and date to narrow the issue search, checking which papers actually served that place [S46 @2026-11-21], [S47 @2026-11-21].

- **Illinois, Kane County.** MyHeritage's county index lists entries from 1850. Use the publication date to pick the issue. Check the Illinois Newspaper Project's Aurora holdings for the title in use that year, including the *Aurora Beacon* for early dates [S46 @2026-11-21], [S48 @2026-11-21], [S49 @2026-11-21].

- **Indiana, Hendricks County.** Use MyHeritage's county index for entries from 1872 onward. Compare the burial place and spouse when supplied, then use the paper and publication date on the hit [S14 @2026-11-18], [S20 @2026-11-18].

- **Indiana, Lake County.** Look for the *Post Tribune*, *Lake County Star* and *Crown Point Register* [S13 @2026-11-18] in Lake County Public Library's title-specific indexes and corresponding microfilm. Check the *Post Tribune* issues directly for 1987–1989, when its online index is incomplete [S21 @2026-11-18].

- **Indiana, Porter County.** MyHeritage's county index includes *The Northwest Indiana Times* and *The Valparaiso Vidette Messenger* notices from 1913 onward. Compare the death date in the private log, then open the title and issue dated on the hit [S41 @2026-11-21], [S42 @2026-11-21].

- **Indiana, Wells County.** Compare birth and death details, cemetery, parents, spouse and marriage date when present on a MyHeritage county index hit. Use its publication date to locate the notice [S46 @2026-11-21]. Search Wells County Public Library's downloadable Cem-Obit spreadsheet locally for marriage or plot details and whether a notice was scanned [S50 @2026-11-21].

- **Kansas, fraternal notices.** For a lodge lead, compare residence and death date in MyHeritage's *Kansas, Fraternal Order Death Notices* index, dated 1860–1969 [S58 @2026-11-21], [S59 @2026-11-21]. Search the Kansas Historical Society's fraternal order index by the deceased person's public name for the order and lodge. Use its coverage by order and proceedings call numbers to locate the original notice in the order's proceedings [S60 @2026-11-21].

- **Kansas, McPherson County.** Use MyHeritage's county index for its newspaper title and issue date. McPherson Public Library's local newspaper microfilm starts in 1872. Base the issue search on the cited paper and issue date, since the collection's stated 1841 start predates the county's first newspaper [S13 @2026-11-18], [S22 @2026-11-18], [S23 @2026-11-18], [S24 @2026-11-18].

- **Kentucky, Daviess County.** Use the Daviess County Public Library's Owensboro Area Obituary Index for Owensboro papers. Use the indexed obituary date and expand the source code before looking up the issue. MI identifies the *Owensboro Messenger & Inquirer*, OM the *Owensboro Messenger*, and OI the *Owensboro Inquirer* [S13 @2026-11-18], [S25 @2026-11-18].

- **Louisiana, statewide.** MyHeritage's Louisiana index starts in 1809 and includes the *Times-Picayune*, *The Advocate* and the *Lake Charles American Press*. Compare residence, death date, age and spouse in the private log. Use the exact paper on the hit with the publication date, including when the hit names the *New Orleans States* or the *New Orleans Item-Tribune* [S46 @2026-11-21], [S51 @2026-11-21].

- **Maryland, Washington County.** MyHeritage's county index lists entries from 1790. Use the paper title and publication date to locate the issue [S41 @2026-11-21], [S43 @2026-11-21]. For Hagerstown notices, also check the Washington County Free Library's Obituary Locator [S44 @2026-11-21].

- **Massachusetts, Boston.** MyHeritage's Boston index starts in 1932 and includes the *Boston Globe*, *Boston Herald* and *Boston Evening Transcript*. Compare residence and death date in the private log. Use the indexed paper and publication date to choose the issue [S41 @2026-11-21], [S45 @2026-11-21].

- **Michigan, Genesee County.** Use MyHeritage's county index for *Flint Journal* notices from 1920 onward. Use the death date to distinguish hits and the publication date to pull the issue [S46 @2026-11-21], [S52 @2026-11-21].

- **New York, Chemung County.** MyHeritage's 1900–1968 county index draws chiefly from the *Elmira Star-Gazette*. Compare the death date and use the publication date to check the paper. Check other local titles if the hit leaves the title unclear and the notice is missing from the dated *Star-Gazette* issue [S46 @2026-11-21], [S53 @2026-11-21].

- **New York, Herkimer County.** Use MyHeritage's county index for *Herkimer Evening Telegram* notices from 1924 onward. Compare the recorded death place and take the publication date to the original issue [S46 @2026-11-21], [S54 @2026-11-21].

- **New York, Steuben County.** MyHeritage's county index lists entries from 1860. Compare the birth and death years and burial place. If the hit leaves the paper or issue date unknown, check the county historian's published obituary list locally or use the death year to narrow a search of local issues [S46 @2026-11-21], [S55 @2026-11-21], [S56 @2026-11-21].

- **North Carolina, Randolph County.** Use the Randolph Room's index for the *Courier* and *Courier-Tribune* from 1903 onward. Find the deceased's name within the relevant year list, then use the newspaper date and page to locate the notice in the corresponding microfilm [S46 @2026-11-21], [S57 @2026-11-21].

- **Ohio, Columbiana County.** MyHeritage's county index points to the *Salem News*, with entries dated from 1934 and occasional parent and spouse names. Use the publication date to locate the issue [S13 @2026-11-18], [S26 @2026-11-18]. Check the Salem Public Library's gap list before relying on a miss in its local index [S27 @2026-11-18].

- **Ohio, Williams County.** Use MyHeritage's county index for entries from 1863 onward. Keep the paper title with the publication date so you open the right issue [S14 @2026-11-18], [S28 @2026-11-18].

- **Pennsylvania, Philadelphia.** Search the *Philadelphia Jewish Exponent* obituary index on MyHeritage or JewishGen by the deceased person's public name. Compare age at death and birthplace when supplied. The index spans 1887–2013 with gaps. On a miss, check JewishGen's coverage list and go directly to issues in the gaps [S30 @2026-11-20], [S31 @2026-11-20], [S32 @2026-11-20]. Use the publication date and any page number to locate the original through Temple University's *Jewish Exponent* holdings guide [S33 @2026-11-20]. If JewishGen shows `Nerc'y` in the page field, browse the necrology in the dated issue [S32 @2026-11-20].

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

When a family story attributes a death to an accident abroad, compare the death notice with news coverage around the death and around the reported accident. Record the date and attributed cause of death, then date the earlier episode and any reported return separately. A corroborated return and a later death notice can overturn a claim that the person died on the trip [S38]. Check whether the death coverage actually links the accident to the death [S35], [S38].

## 6. Keep living survivors to the family question

A recent obituary's survivors list names living people and often where they live. Use it only for the family question. Do not use it to look up a survivor's current address, phone, email, workplace or accounts, and do not trace a minor named in it. The Living people rule in `SKILL.md` applies. Keep living survivors' names in the private research log.

## Return packet

- An expectation note: date and place of death, the expectation set in §1, the titles and issues checked, and any miss worded as "no notice found" in those titles and issues.
- A notice table: one row per obituary, death notice or card of thanks, with whose notice it is and their relationship to the subject, newspaper or proceedings title, date and page, and the names and relationships transcribed as printed.
- Leads from each notice, labelled with that notice: parents, the mother's maiden name, women's later surnames, church, employer, lodge and funeral home.
- Conflicts and gaps: relationships that differ between notices, relatives missing from a survivors list, and siblings not marked as full or half.
- Any funeral or memorial card: who holds it and what it carries. A request to a relative stays marked as an unsent draft until the privacy gate is answered.
