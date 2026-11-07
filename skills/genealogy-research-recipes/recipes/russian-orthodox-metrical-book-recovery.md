---
id: "russian-orthodox-metrical-book-recovery"
title: "Recover a Russian Orthodox metrical-book entry through the period parish, the consistory copy and its margin notes"
summary: "Locate and read a Russian Orthodox metrical entry through the period parish, the consistory copy and its margin notes."
kind: "records"
scope: {"platforms": [], "tasks": ["Locate and read a Russian Orthodox metrical entry through the period parish, the consistory copy and its margin notes."]}
triggers: ["Locate and read a Russian Orthodox metrical entry through the period parish", "the consistory copy and its margin notes"]
privacy: "none"
gates: []
guardrails: [{"id": "RUSSIAN-ORTHODOX-METRICAL-BOOK-RECOVERY-01", "text": "margin decrees are separate dated events, and names and patronymics are hypotheses, not proof of descent."}]
handoff: ["bessarabia-moldova-record-routing", "catholic-parish-diocesan-record-recovery", "corpus-seeded-name-search", "evidence-proof-judgment", "galicia-bukovina-habsburg-record-routing"]
checked: "2026-11-02"
checked_basis: "opened 2026-11-02"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "pointer", "group": "Russian Empire and Soviet records", "order": 1083}
---

# Recover a Russian Orthodox metrical-book entry through the period parish, the consistory copy and its margin notes

Use this recipe when a Russian Orthodox baptism, marriage or burial in the metrical books (метрические книги) is missing, contradicts other records, or carries formulae and margin notes you need to interpret.

It covers two jobs:

- **Locating the entry.** Work out which parish served the village in the event year, which consistory held the second copy, and where the parish copy went. Then find the delo and the leaf span inside a multi-parish volume.
- **Reading the entry.** Read marriage-count formulae literally, treat margin decrees as separate dated events, and treat names and patronymics as hypotheses rather than proof of descent.

The worked material comes almost entirely from the Perm, Ekaterinburg and Tobolsk sees. The routing logic carries over to other dioceses. The fond, opis and inventory structures do not: confirm them in the local archive's own guide.

Other recipes cover the overlapping steps:

- **Locality coverage.** For planning the next searches from a locality's record coverage, use [research documentation: turn locality coverage into the next searches](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/research-documentation.md).
- **Composite files and book ledgers.** For composite-file headings and a per-year book ledger of pages × targets, use [archival image coverage verification](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/archival-image-coverage-verification.md).
- **Locators.** For leaf, side and sequence locators, use [source citation](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/source-citation.md).
- **Cancellations and AI transcription.** For bracketed cancellations and AI transcription, use [AI for documentary records](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/ai-for-documentary-records.md).
- **Kinship rulings.** For legitimacy labels, separation versus divorce, and the final kinship ruling, use [evidence/proof judgment](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md).
- **Jewish records.** For Jewish rabbinate books and registration (приписка), use [Russian-Empire Jewish identity attribution](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/russian-empire-jewish-identity-attribution.md).
- **Bessarabian books.** For Bessarabian metrical books of 1811–1923, which the National Archives Agency of Moldova (ANA) keeps in fond 211 by district opis (its op. 23 covers Tiraspol uezd of Kherson guberniya), use [Route a Bessarabian or Moldovan record by date, district and bank of the Dniester](bessarabia-moldova-record-routing.md).
- **Galician and Bukovinian books.** For Galician Greek Catholic and Roman Catholic books, Bukovinian Orthodox books and the archives that hold them, use [Route a Galician or Bukovinian record by date, confession and custodian](galicia-bukovina-habsburg-record-routing.md).

## Contents

- 1\. Route by the period uezd, guberniya and see, never by the modern oblast
- 2\. List every parish that could have served the village in that year
- 3\. Route each parish-year to both custodians
- 4\. Inside a consistory fond, record the delo and the leaf span, and check every delo for the year
- 5\. When an entry conflicts with other records, read the other exemplar
- 6\. Recover a missing marriage
- 7\. Read the formulae literally first
- 8\. Copy every margin note as its own dated event and follow it
- 9\. Treat names and patronymics as hypotheses
- 10\. Use machine-read full-text search for leads, never for a negative
- Output

## 1. Route by the period uezd, guberniya and see, never by the modern oblast

- **Start from the pre-1917 units, not today's oblast.** Place the village in its pre-1917 uezd and guberniya, then find the see that held its parish in the event year. Today's oblast boundaries say nothing about where the books accumulated.
  - Kurgan oblast was created in the Soviet period. Before 1917 Kurgan uezd belonged to Tobolsk guberniya and Shadrinsk uezd to Perm guberniya.
  - A participant concluded that records for one Shadrinsk-area locality therefore accumulated in Kamyshlov, Ekaterinburg and Perm, not in Kurgan or Chelyabinsk. [S10]
- **Confirm the village, then the parish, then choose the archive.** First confirm the village in a period list of populated places. Then find its parish in a dated diocesan reference book (Справочная книга … епархии). That book lists the villages of each parish with their distances and names the nearest other church. Only then choose fond/opis/delo. A participant demonstrated the chain with:
  - the list of populated places of Tobolsk guberniya compiled from 1868–1869 data (St Petersburg, 1871)
  - the Справочная книга Тобольской епархии к 1 сентября 1913 года (Tobolsk, 1913)
  - GASO f. 6 op. 10, dela 13, 26, 45, 63, 77, 94, 99, 119, 140 and 170, for the parish's books for 1871–1914. [S7]
- **Route each period separately when the see changed.** In the same thread, the earlier run for that uezd was given as Tobolsk state archive f. 156 op. 20 (Turinsk uezd metrical books, 1765–1875). [S7] The same participant also reported reading-room restrictions on other opisi of GASO f. 6, but a current online catalogue lists those books as digitised, so that report is out of date. Take the current date ranges and access terms from the archive's present catalogue, not from the thread.
- **Route by today's custodian of the territory as well as the historic guberniya archive.** When a historic uezd now lies in another oblast, check both today's oblast archive and the historic guberniya archive before you report "not found". An inventory may be titled by present-day district rather than by the historic uezd.
- **Before a consistory existed, look in the earlier see.** For years before an Ekaterinburg consistory existed, search Perm for the second copies, and Tobolsk for earlier years. Participants had found none in either place for that territory. Only a few pre-1799 books were known, filed by chance in GASO fond 24 (Ural Mining Administration). [S10] That early assessment was incomplete. Later in the same thread another participant reported, from his own work with the delo, the books of one Katai church for 1780–1790 without gaps in the Kurgan state archive (Ф. 243 Оп. 1 Д. 1), with 1791–1801 not found. He also listed the 1798–1812 confession lists of another Katai church, with an 1800 metrical book bound in, in the Shadrinsk archive (Ф. 328 Оп. 1 Д. 2). [S10] Search the parish-level fonds before declaring a gap, and record only the parish-years still unlocated as a coverage gap, not as "no books were kept".

## 2. List every parish that could have served the village in that year

Build a dated list of candidate parishes. One village need not mean one church for every year or every resident.

- **Mother parish before a new church.** Compare the person's estimated birth year with the founding date of the nearest church. A participant estimated an ancestor's birth at about 1861. She reported that the local church was built in 1866 and that its books do not survive, so she moved the search to the neighbouring older parishes. [S24]
- **A newly built neighbouring church.** A participant worked through the books, which are held in a museum in Mishkino. She found that after a church opened in a neighbouring village in 1911, part of one village's Orthodox residents went there. [S6]
- **Edinoverie and Old Believer residents.** In that village, the same participant found that many Old Believers had moved to edinoverie by 1911–1915. They were baptised, married and buried at an edinoverie church in another village. [S6] For an edinoverie baptism:
  - Get the parish's village list from the clergy registers (клировые ведомости) and diocesan directories. A participant cited GASO f. 37 op. 4 d. 89 (clergy registers of the Shadrinsk edinoverie churches, 1870–1871).
  - Separately, list the Orthodox parishes that served the same village. In that case a town church and the cathedral both included it.
  - Check the founding date. A participant quoted the 1902 reference book Приходы и церкви Екатеринбургской епархии: the town's edinoverie parish formed in 1839, and before that its people went first to the Ekaterinburg edinoverie church and then to Sosnovskoe.
  - For the years before the founding, the fallbacks are revision lists and confession lists. Those confession lists come from non-edinoverie churches.
  - Participants noted that the church's surviving metrical books in the local archive begin only in 1861. [S12] The Shadrinsk archive guide, as posted by a participant, gives that church's fond as covering 1861–1919. [S8]
- **Conflicting parish assignments.** In one thread, participants named different churches for the same village. Those churches' fonds sit in different archives (Kurgan, and probably Shadrinsk). Keep both candidates until a book settles it. [S6]
- **Town and neighbouring churches.** Baptisms and weddings were not always held in the home church. A participant found family entries in town churches as well. [S8]
- **Foreign subjects and other confessions.** Look for a Lutheran, a Catholic or a foreign subject in the local Orthodox books too. Participants quoted such people:
  - as the non-Orthodox spouse in a mixed marriage
  - as the parents of a child baptised Orthodox
  - in hospital-church death entries.

  Foreign subjects also appear as godparents and marriage guarantors. Copy the subjecthood, confession and home town as written, and record a confession only where the entry gives it. [S20]

## 3. Route each parish-year to both custodians

Every parish-year has two possible copies: the parish copy stayed at the church, and the second copy went to the consistory. [S24], [S10] Give each copy its own row:

- **Consistory copy.** Look in the consistory fond of the see that held the parish at the event date. A participant said the books for one locality were concentrated in the Ekaterinburg consistory fond, with some later dela transferred to the Kurgan archive. [S10]
- **Parish copy.** Participants said parish copies passed through ZAGS offices into district or oblast archives (Shadrinsk or Kurgan in that case). Expect pre-1917 parish copies in the oblast archive, not the district one. A participant said it is pointless to look for pre-revolutionary files in Kamyshlov, because a Soviet-era instruction moved such files from district to oblast archives, and that any transfer should be marked in the inventory. [S10]
- **Read the inventory for transfer notes.** A participant transcribed the inventory of one Shadrinsk-archive church fond (Ф. И-264). It marks several metrical-book dela as handed over to a district ZAGS (Батуринский ЗАГС), so treat that ZAGS as a separate holder. Another participant said a 1913 book for one parish might be in the Kurgan archive or in the district ZAGS. [S8]
- **Books after 1917.** The decree of 18 (31) December 1917 recognised only civil marriage, set up civil registration offices and ordered church registers sent to the city, uezd and volost zemstvo boards. From the decree of 20 January (2 February) 1918, only civil offices kept acts of civil status. [S38], [S39] Church books continued in places: the Irkutsk archive holds Orthodox metrical books of Irkutsk diocese for 1911–1922, and a 1924 circular dealt with church marriages concluded after 20 December 1917 in territory held by the Whites. [S41], [S42] Give a post-1917 parish-year three rows: the ZAGS archive, the oblast archive (consistory and church fonds), and any transfer the inventory notes. ZAGS act books stay with ZAGS for 100 years from each entry and then go to the state archive (Federal Law 143-FZ, art. 77). [S40] A book's place can still differ from what that term predicts: the Irkutsk archive received the 1911–1922 church books from the oblast ZAGS archive in 2008. [S42] Search all three rows whatever the book's age.
- **Do not trust inventory titles.** Order the delo and check its contents:
  - A participant found dates in a delo that differed from its inventory entry, and leaves that clearly came from other documents. [S8]
  - Another said that in Perm many documents are hidden in inventories under other names. [S10]
  - The 1776 confession list participants cited is catalogued under a church name and a see that differ from today's. [S10]
  - A file titled by dedication ("книга Дмитриевской церкви", "Никольской церкви") may belong to a church of that dedication in another village, not to a village called Dmitrievka or Nikolskoe. Fix the parish and village from the full file title, the inventory and the entries before you use the book, or its empty search, for the similarly named village. For dedication names that repeat, see [Catholic parish and diocesan record recovery, step 1](catholic-parish-diocesan-record-recovery.md#1-find-the-parish-that-kept-the-register-not-just-a-church-name).
- **The diocesan office.** A participant reported that the present Perm diocesan administration answers queries by referring people to the Perm state archive (ГАПК). [S24]
- **Open the custodian's own online viewer before ordering.** Some archives publish their books as images:
  - Moscow Glavarchiv publishes metrical books (cgamos.ru/metric-books/) and confession lists (cgamos.ru/ispovedalnye_vedomosti/) as online images in its «Моя семья» service. [S29], [S30] Have the user open it in their browser.
  - The Sverdlovsk oblast archive (GASO) runs a metrical-book viewer at metriki.gaso-ural.ru. On 2026-11-02 it held only f. 6, the Ekaterinburg consistory, so it reaches the GASO f. 6 dela this recipe cites. Search it with the prefixes "фонд:", "опись:", "дело:" (for example "дело: 01_6_15_100") and "скан:". [S31]
  - The Rostov oblast archive (GARO) arranges Don metrical books by settlement and okrug at donarch.ru/metrikbooks/, with scan previews on each settlement page. [S32]

  Years missing from an online list are not proof of loss. Browse at a human pace and never fetch in bulk.
- **Before asking a Russian regional state archive to search,** read its current requests page and record the URL and the date you read it. Many of these archives have stopped or limited thematic genealogical searches. Some take a prepayment that is not refunded when nothing is found, and some send users to search the reading room themselves. [S33], [S34], [S35] Route the user to self-search or remote viewing, and order copies by cipher and leaf.

## 4. Inside a consistory fond, record the delo and the leaf span, and check every delo for the year

- **Cite the leaf span, not just the delo.** A consistory delo is often an annual volume that binds many parishes together.
  - Participants' transcriptions of the GASO f. 6 op. 1 inventory show single dela listing dozens of churches for one year, with the starting leaf (л.) given for some sections. [S2]
  - A participant's transcription of the GASO f. 6 op. 3 inventory (Ekaterinburg consistory, 1746–1913) lists each parish as "year – delo, pages". Record both numbers: "1870 – 592, 244–285" is a different citation from "delo 592". [S3]
- **Check every row for the year.**
  - Two dela can cover the same year and the same list of parishes, as d. 60 and d. 61 do for 1824 in op. 1. [S2]
  - In op. 3, one parish has two rows for 1811 (299 and 301). Another has its 1846 births in d. 180 and its marriages and deaths in d. 181. [S3]
  - A parish can appear under two uezds ("Ирбитский / Верхотурский уезды"). Delo numbers also jump between ranges as the parish's grouping changes. [S3]

  Report a parish-year as missing only after you have opened every delo row for it.
- **Copy the page string exactly as the inventory gives it,** including oddities such as "226об.243", "218об.-236", "32-96а" or reversed spans like "572-408". These are what the inventory says, not corrected readings. [S3]
- **Log what you inspected.** Use [archival image coverage verification](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/archival-image-coverage-verification.md) to record which parts (births, marriages, deaths) and which leaves you actually inspected.

## 5. When an entry conflicts with other records, read the other exemplar

Order the other copy of the same year as a separate delo. Keep both readings, each with its own locator.

In one worked case, an 1825 marriage entry named the bride as the daughter of a family that never had a daughter of that name in any confession or revision list.

- **The two exemplars.** GASO f. 6 op. 1 d. 63 and d. 62 gave two forms of the same wrong surname. The participant concluded that the error was in the parish copy. [S19]
- **Testing the bride against households.** Her identity was then tested against households:
  - The 1816 revision list showed a daughter of that name and age in another family.
  - Her brother's wife in the 1834 revision list matched a "sister-in-law" named in an 1839 report.
  - The 1850 revision list, which in this case gave women's patronymics, confirmed that wife's patronymic.
  - A birth entry for the bride was found.
  - Later, godparent links ran between the two families.
- **The result.** The participant still called the attribution indirect. The bride's ages across six sources implied births from 1794 to 1808. Treat such a spread as a range that ranks candidates. A mismatch lowers a candidate's rank but does not exclude it. [S19]

An Orthodox metrical date, like other Russian dates written before 14 February 1918, is normally Old Style; check the document's own calendar note. [S43] A Soviet, ZAGS or émigré document may restate the same event in New Style, so a difference of 12 or 13 days is not by itself a conflict. Record both dates with their calendar. For the offsets and the 1918 switch, use [evidence/proof judgment: follow record versions and test disputed dates](evidence-proof-judgment.md#follow-record-versions-and-test-disputed-dates).

## 6. Recover a missing marriage

A participant gave this search order: [S1]

1. The bride's parish, then the groom's.
2. The parish where the first child was baptised. The participant said couples usually married there.
3. Work back about seven years from the first birth, in the churches nearest the residence.
4. The confession lists of those churches for the likely years.
5. Officials' personal service files, which can record a marriage.
6. A repeat marriage certificate issued in the Soviet period, for example for an inheritance or a property sale.

**Always check for marriage-inquiry books (брачные обыски).** The same participant believed they rarely survive because they were destroyed in Soviet times as personal data. That is one participant's view, and it should not stop the search:

- Another participant cited a surviving obysk book from 1927–1929 in the Dalmatovo archive (Ф. 330 Оп. 11 Д. 11). [S1]
- Archive catalogues list surviving pre-1917 obyski, for example in the Omsk regional archive (ИАОО f. 16 op. 9, Tara uezd, 1834–1845).

**If the bride's maiden name is unknown:**

- **Eliminate candidates.** A participant suggested listing every woman with the same given name, patronymic and age in the nearest revision list. Then read the births and deaths parts of the metrical books for those years. Follow each candidate forward and drop those who are accounted for. [S11]
- **Read confession lists by household.** Another participant found a bride this way in her home village, then confirmed her through a copy of her birth certificate held by a relative. [S11]
- **Search godmother entries.** Look for the bride's name among godmothers in the months before the likely marriage. A participant found brides acting as godmothers shortly before they married. [S11]

## 7. Read the formulae literally first

Apply each reading literally, then test it against the rest of the entry.

- **"вдов по втором браке"** on a groom means his second wife has died and he is entering a third marriage. "Вдова по первом браке" means the bride is entering her second. [S1]
- **"полуторный брак"** is a marriage that is the second for one spouse and the first for the other, for example a widower marrying a maiden. Search for the widowed party's earlier marriage and the first spouse's death. [S25]
- **"сводный брак"** in a 1928 birth entry: one participant read it as a ZAGS-registered union without a church wedding, unlawful under church canon, and not a step-relation. The researcher had found no church marriage for those parents. Treat this as a single participant's tentative reading for the 1920s. [S1]
- **"нзкр"** abbreviates незаконнорожденный (illegitimate).
  - The birth entry does not give the father, so do not infer one from the household the child lived in.
  - A participant advised finding the daughters' marriages, where they will probably carry the mother's married surname and be marked illegitimate again.
  - The same participant also noted that children of Old Believer marriages were often recorded as illegitimate, and that paternity may survive in non-church records. [S13]
- **"из раскола"** marks a person joining from the Old Belief. In one 1892 entry, a 21-year-old woman was marked this way, although her parents had appeared as Orthodox at their other children's baptisms. There was a gap in those baptisms around her birth.
  - A participant read this as a lapse in the parents' observance, so her birth never entered an Orthodox book.
  - The participant said five years without communion counted as falling into the schism, and that the written pledge given on returning was not recorded.
  - The participant pointed to the 1899 compendium of laws on the schism and sectarians (Сборник законов о расколе и сектантах) for the rules of the period.

  Set out the parents' other baptisms as a series and look for the gap. Do not read the label as lifelong Old Belief. [S21]
- **Several infants baptised on one date from one village** may be a visiting priest's batch. Expect different birth dates, and record the place of baptism as an inference.
  - One participant suggested weighing the infants' villages and their distance from the church, other rites held the same day, and whether the day was a Sunday or a feast.
  - Another said priests wrote in a notebook on the round and copied the entries into the book later. [S18]
- **Month headings.** A month written once at the head of a section or column belongs to the entries it heads, not to every date on the page. Take a first entry under a June heading with birth "31" and baptism "1 June": it is a 31 May birth when the previous spread and the date sequence support May. Record the month as taken from context, keep the baptism date separate, and never write "31 June".
- **Possessive name forms in Galician and Western-Ukrainian entries.** Surnames in -ів (Петрів, Михайлів) are possessive adjectives formed from a given name that became fixed surnames, and they are common in Galicia. Their female forms include Павліва and Павлова beside Павлів. [S27], [S28] So in "Іван Петрів" or "Марія Іванова" the second word may name the father or may already be a surname. Decide from the column heading, the grammar and the neighbouring entries, never from the ending alone.
- **"родомъ X" (by origin X) is not a maiden name by itself.** Treat a maiden name as established only when an explicit "урождённая" (née) or other family records state it. Otherwise keep it as a hypothesis.

## 8. Copy every margin note as its own dated event and follow it

Copy each note in full, with its issuing body, date and number, as a separate observation. Do not merge it into the entry.

- **Divorce.** Three notes show the pattern:
  - A 1908 marriage entry (Dalmatovo archive Ф. 320 Оп. 1 Д. 20) carries a side note. The marriage was dissolved by an eparchial decision of 16/17 December 1913 (№ 720), confirmed by the Synod on 19 August 1914 (№ 13729). One spouse was given a seven-year penance, and both were allowed to remarry. The note was entered under a consistory decree of 1 September 1914. [S1]
  - An 1886 entry in GAPK f. 37 op. 3 d. 136 carries a red cross-reference in one margin. The other margin records a 1908 dissolution, confirmed by Synod decree № 789 and entered under a consistory decree of 11 March 1911 (№ 4697). [S17]
  - Another note records an annulment because the husband was exiled to penal labour, entered by consistory decree № 207 of 11 January 1902. The wife's later marriage entry says her first marriage was dissolved for that reason. [S17]

  Follow each note to the consistory divorce cases. Divorce petitions went to the eparchy's spiritual consistory. As the first two notes show, the Synod confirmed the eparchial decision, and a consistory decree then ordered the note. Participants listed GASO f. 6 op. 4 (Ekaterinburg eparchy) and GAPK f. 37 op. 5 (Perm eparchy), both arranged by the couple's surname. Also read any later remarriage entry. [S17]
- **Limits on divorce notes.**
  - "Разошелся" (separated) is not a divorce.
  - A participant found no note on one marriage entry, and the thread did not settle which exemplar carried such notes, so check both copies.
  - The stated cause is the wording of the decision, not necessarily what happened. A participant read a case in which the husband agreed to a divorce only if the wife's adultery was named as the cause. [S17]
- **Legitimation.** A 1911 birth entry received a note in 1915, entered under Ufa consistory decree № 1514 of 27 January 1915 following a decision of the Elisavetgrad circuit court of 2 January 1915, that legitimated the child to a named couple. Follow the court decision in that court's records: the court and the recording consistory were in different provinces. [S17]
- **Adoption after 1917.** A participant reported a notice pasted onto a 1905 birth entry, addressed to the ZAGS office attached to the uezd-town militia; the extract does not name the sender. It recorded an adoption in 1917, the adopter, the new surname, given name and patronymic, and the number of the certificate issued. Another participant said such notes appear regularly but not for every adopted child, so their absence proves nothing. [S5]
- **"Выслано" (sent) notes.** A participant raised a birth entry marked "выслано" with the year 1951 for a soldier missing from a regional memorial book. [S9] Copy the full note with its position, and take what was sent or issued from its formula and particulars, not from the word alone. Record it as a dated event that points to post-war records. On its own it does not show who asked, where they lived, or that the person was alive. [S9]
- **Official communications in death entries.** Copy any cited "отношение" with its office, date and number. A participant transcribed two examples:
  - a factory physician's communication № 256 (GASO f. 6 op. 19 d. 422, 1908)
  - a communication № 926 of 8 July 1909 from the court investigator of the 7th district of Ekaterinburg uezd (d. 427, 1909).

  The next retrieval target is that office's own file series. [S15]

## 9. Treat names and patronymics as hypotheses

- **Missing surnames.** In early books, surnames were often not written for peasants. Search by given name, patronymic and village. Use confession lists to place whole households, and read godparent entries, where the surname may appear. In one thread, a participant found an 1812 godparent entry that carried a family's surname, which the researcher had assumed arrived later. Revision lists then dated the family's arrival to between two revisions. [S4]
- **Unstable surnames.**
  - A participant, who held that surnames were not legal objects outside the nobility, saw the same person under different surnames in one year, at a birth and a death a week apart. [S14]
  - An 1886 priest's account, quoted by a participant, describes peasants with no surname or with two or three. [S14]
  - The ending -ов/-ев/-ских varied within one family. [S7]
  - A participant traced one household head under one surname in 1710 and under a surname derived from his place of origin in 1719. [S12]
  - Expand given names deliberately (Dionisiy = Denis). [S12]
- **Who could be a godparent.** Under an 1834 decree quoted by V. Mikhailovsky, a boy's godfather and a girl's godmother had to be Orthodox. The rule bound that sponsor only, so do not infer the other sponsor's confession. Orthodox canon law, as set out by Milaš, excluded иноверцы (people of other faiths) and the child's own parents. So do not read a godparent as the child's parent; a participant gave the same answer for a girl's godfather. [S11]
- **Patronymics need not come from the father.**
  - A participant abstracted a service file (GAPK f. 36 op. 6) recording an illegitimate man whose patronymic was given from his godfather. Record any second surname as a separate name form. [S23]
  - A participant saw a godfather called simply "father" in his goddaughter's marriage entry, and her patronymic matched his name. [S11]
  - Another found that an illegitimate boy took his patronymic and surname from his mother's father. [S11]
  - A bride may be recorded under a stepfather's or a fosterer's patronymic and surname. Marriage entries can also give names that match no real woman. [S11]
- **Converts.** A convert may be listed with the surname and patronymic of a local household head. Keep three explanations open together: an illegitimate son, naming by a godfather, or adoption into the household. Participants disagreed on whether godfathers passed on patronymics, so find the conversion baptism and its sponsors. [S16]
  - In a published baptism account cited by a participant, a boy acquired by a merchant was baptised with the merchant's adult children as sponsors. He later appears in an 1816 revision list with a patronymic matching his godfather's given name. [S22]
  - His age at baptism (15 in 1806) and his revision-list age (36 in 1816) imply birth years about a decade apart. That mismatch lowers the link's rank. It does not exclude the link.
- **Adoption before 1917.** In the cases participants discussed, adoption was not recorded as a separate act in the church books. Instead the child's status shows up across their life:
  - as "приемный" to a named head in revision or confession lists
  - often in the marriage entry
  - later, when the child acts as godparent, guarantor, groom or parent.

  Another participant had seen a couple of entries recording a surname change, so do not assume the books never note it. [S14] Search under both the birth and the adoptive patronymic and surname.
  - One participant found a woman recorded under her birth names only in her marriage entry.
  - Another found an adoptee's birth family through a consolidated revision list that gave males across several revisions and their place of origin. [S14]

  These traces describe a child raised in another family. A missing church act is not proof that no formal adoption file exists, and the procedure has not been checked. For a formal adoption, search for a court or administrative file and for a matching margin note on the birth entry, and take the procedure from Свод законов vol. X.
- **Household and age tests.** A shared godparent family or co-residence is support, not identity. Test each hypothesis against:
  - confession-list households across several years
  - revision-list candidates of matching age
  - godparent patterns.

  Leave the ruling to [evidence/proof judgment](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md). [S11], [S19]

## 10. Use machine-read full-text search for leads, never for a negative

Yandex «Поиск по архивам» (yandex.ru/archive) searches machine-recognised text of 18th- to early-20th-century metrical books, revision tales and confession lists. It names archives of Moscow and of the Astrakhan, Orenburg and Irkutsk regions, among others. Viewing a document needs a login, which the user does. [S26] Its catalogue (Источники) lists the holding archives in full: 29 on 8 October 2026, against about nine in July 2023. [S37] Have the logged-in user open the catalogue and record the archives it lists, with the date, before you treat a miss as a coverage gap.

- **Search inside entries when file titles may use another village name.** A parish-book file title can use a village's second or later name, so a catalogue filter on one name can miss the file. The service searches the recognised text of the documents by surname or settlement. [S26], [S36] Search every name form of the village, group the hits by file and read the file titles before you declare a coverage gap.
- **A miss is not a negative.** Full text finds only what the machine recognised. Log the volumes, years and pages that have no recognised text: a page without text is not a blank page. An archive missing from the results is not proof that the service lacks it.
- **Take spellings from the text itself.** Run pre-reform forms (Ѳеодоръ) beside modern ones (Фёдор) until you see which the recognised text uses, and build further variants from forms you actually find, using [corpus-seeded name searches](corpus-seeded-name-search.md#diagnose-three-different-failures). Take the query syntax from the service's current help page, not from web-search habits. Confirm every near hit on the image.
- **Read the full delo title.** A composite volume (step 4) can name the target church last. In a multi-church delo, find the target parish's pages before you assign a hit to it, and limit any negative to that section and to the years and pages read.
- **Entries without surnames.** A surname query misses surnameless entries (step 9): query the given name, patronymic and village, or browse the section.
- **A snippet is not the entry.** Open the page text and the image. For a revision-tale household, check the next leaf. Read ages, death years and marriage-out remarks from their columns on the image.
- **Person lists and filters.** Treat any list of names or event filter the service offers as a lead to the image, not as a second source.
- **Locators.** Take the archive and cipher from the document description and cite the archive, not the service.
- **Images.** Never get around a file restriction. Where the original file is not served, save a viewer screenshot with the scan URL and label it as a screenshot, not the archival original.

## Output

Return three tables:

1. **Parish-candidate and custodian register.** One row per parish-year. Give the reason the parish was chosen (mother parish, edinoverie, new church, bride's parish, town church). For both the consistory copy and the parish copy, give:
   - the archive, fond/opis/delo and leaf span
   - any transfer notes (ZAGS, district archive, museum, another oblast)
   - whether it was searched, not searched or not accessible.

   Name every delo opened for that year.
2. **Literal entry transcriptions.** Put each margin note on its own row with its date, issuing body, number and follow-up series (consistory divorce case, court, ZAGS, physician or investigator).
3. **Name and parentage hypothesis register.** Give each competing explanation and the confession-list, revision-list and godparent tests applied to it. Give ages as ranges. A range mismatch lowers a candidate's rank and never removes it.

Call an entry absent only for the dela and exemplars you actually opened.
