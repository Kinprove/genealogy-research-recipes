---
id: "russian-orthodox-metrical-book-recovery"
title: "Recover a Russian Orthodox metrical-book entry through the period parish, the consistory copy and its margin notes"
summary: "Locate and read a Russian Orthodox metrical entry through the period parish, the consistory copy and its margin notes."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "RUSSIAN-ORTHODOX-METRICAL-BOOK-RECOVERY-01", "text": "Read marriage-count formulae literally, treat margin decrees as separate dated events, and treat names and patronymics as hypotheses rather than proof of descent."}]
handoff: ["bessarabia-moldova-record-routing", "catholic-parish-diocesan-record-recovery", "corpus-seeded-name-search", "evidence-proof-judgment", "galicia-bukovina-habsburg-record-routing", "russian-orthodox-confession-list-reading", "russian-village-family-reconstitution"]
checked: "2026-11-02"
checked_basis: "opened 2026-11-02"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Russian Empire and Soviet Union", "order": 75}
---

# Recover a Russian Orthodox metrical-book entry through the period parish, the consistory copy and its margin notes

Use this recipe when a Russian Orthodox baptism, marriage or burial in the metrical books (метрические книги) is missing, contradicts other records, or carries formulae and margin notes you need to interpret.

It covers two jobs:

- **Locating the entry.** Work out which parish served the village in the event year, which consistory held the second copy, and where the parish copy went. Then find the delo and the leaf span inside a multi-parish volume.
- **Reading the entry.** Read marriage-count formulae literally, treat margin decrees as separate dated events, and treat names and patronymics as hypotheses rather than proof of descent.

Most of the worked material comes from the Perm, Ekaterinburg and Tobolsk sees, with Tula and Moscow cases from genealogy blogs. The routing logic carries over to other dioceses. The fond, opis and inventory structures do not: confirm them in the local archive's own guide.

Other recipes cover the overlapping steps:

- **Locality coverage.** For planning the next searches from a locality's record coverage, use [research documentation: turn locality coverage into the next searches](research-documentation.md).
- **Composite files and book ledgers.** For composite-file headings and a per-year book ledger of pages × targets, use [archival image coverage verification](archival-image-coverage-verification.md).
- **Locators.** For leaf, side and sequence locators, use [source citation](source-citation.md).
- **Cancellations and AI transcription.** For bracketed cancellations and AI transcription, use [AI for documentary records](ai-for-documentary-records.md).
- **Kinship rulings.** For legitimacy labels, separation versus divorce, and the final kinship ruling, use [evidence/proof judgment](evidence-proof-judgment.md).
- **Jewish records.** For Jewish rabbinate books and registration (приписка), use [Russian-Empire Jewish identity attribution](russian-empire-jewish-identity-attribution.md).
- **Bessarabian books.** For Bessarabian metrical books of 1811–1923, which the National Archives Agency of Moldova (ANA) keeps in fond 211 by district opis (its op. 23 covers Tiraspol uezd of Kherson guberniya), use [Route a Bessarabian or Moldovan record by date, district and bank of the Dniester](bessarabia-moldova-record-routing.md).
- **Galician and Bukovinian books.** For Galician Greek Catholic and Roman Catholic books, Bukovinian Orthodox books and the archives that hold them, use [Route a Galician or Bukovinian record by date, confession and custodian](galicia-bukovina-habsburg-record-routing.md).

When the target's own entry does not survive and a generation has to be rebuilt from the whole village, use [village family reconstitution](russian-village-family-reconstitution.md).

## Contents

- 1\. Route by the period uezd, guberniya and see, never by the modern oblast
- 2\. List every parish that could have served the village in that year
- 3\. Route each parish-year to both custodians
- 4\. Inside a consistory fond, record the delo and the leaf span, and check every delo for the year
- 5\. When an entry conflicts with other records, read the other exemplar
- 6\. Recover a missing marriage
- 7\. Read the formulae literally first
- Reading the page
- 8\. Copy every margin note as its own dated event and follow it
- 9\. Treat names and patronymics as hypotheses
- 10\. Use machine-read full-text search for leads, never for a negative
- Output

## 1. Route by the period uezd, guberniya and see, never by the modern oblast

- **Start from the period jurisdiction.** Place the village in its uezd, guberniya and see for the event year. A modern oblast may include districts from different guberniyas. [S10]
- **Confirm the village, then the parish.** Locate the village in a period list of populated places. In a dated diocesan directory (Справочная книга … епархии), check the villages assigned to its parish, their distances and the nearest other church before choosing a fond, opis and delo. [S7]
- **Route each period separately when the see changed.** For Turinsk uezd, check the Tobolsk f. 156 op. 20 inventory for the earlier run. Confirm date ranges and access in the archive’s own catalogue. An older report of reading-room restrictions for GASO f. 6 [S7] would miss the scans listed in its viewer in November 2026 [S31].
- **Route by today's custodian of the territory as well as the historic guberniya archive.** When a historic uezd now lies in another oblast, check both today's oblast archive and the historic guberniya archive before you report "not found". An inventory may be titled by present-day district rather than by the historic uezd.
- **Before a consistory existed, check its predecessors and the parish fonds.** For the Ekaterinburg area, trace the earlier Perm and Tobolsk jurisdictions. An apparent gap in early Katai books overlooked a parish run (Kurgan Ф. 243 Оп. 1 Д. 1) and a metrical book bound with confession lists (Shadrinsk Ф. 328 Оп. 1 Д. 2), according to the forum inventory leads [S10]. Record the specific parish-years still unlocated.

## 2. List every parish that could have served the village in that year

Build a dated list of candidate parishes. One village need not mean one church for every year or every resident.

- **Church founding dates.** If the birth predates the nearest church, search the older parishes [S24]. When a neighbouring church opened in 1911, only some Orthodox villagers began attending it, so search both churches’ books for that village [S6].
- **Edinoverie and Old Believer residents.** Check for an edinoverie church in another village [S6]. Use clergy registers (клировые ведомости, e.g. GASO f. 37 op. 4 d. 89 for Shadrinsk in 1870–1871) and dated diocesan directories to list the edinoverie parish, its predecessors and the overlapping Orthodox parishes. Distinguish the parish’s founding date from the first surviving book. For earlier years, check revision lists and the Orthodox churches’ confession lists [S12], [S8].
- **Conflicting assignments.** Keep both parishes and their archives on the list until an entry resolves the conflict [S6]. Include town and neighbouring churches in searches for baptisms and weddings [S8].
- **Foreign subjects and other confessions.** Check Orthodox books for a non-Orthodox spouse, parents at a child’s baptism, godparents, marriage guarantors and hospital-church deaths. Copy subjecthood, confession and home town only as the entry gives them [S20].

- **Institution churches.** For a birth or death in a town hospital, check the hospital church and the home parish’s loose papers for a notice from its priest [S44], [S45]. For the Tula zemstvo hospital’s Alexander Nevsky church in 1898, consult the combined city volume, GATO f. 93 op. 1 d. 69 [S100].

- **Moscow maternity shelters and the Foundling Home.** TsGA Moscow f. 179 op. 69 holds the books of mothers and births of the city maternity shelters (родильные приюты), by shelter and date, for 1880–1908 [S101 @2026-11-15]. When a Moscow birth entry names a shelter, search that shelter's book by the date of admission: a researcher reports that the entries run by admission, not alphabetically, and give the mother's estate, origin, age and the number of the pregnancy [S46 @2026-11-15]. A village child with no birth entry in the home parish may have been a ward (питомец, питомка) of the Imperial Moscow Foundling Home placed with a peasant foster family [S47 @2026-11-15]. Wards were sent to village wet nurses and often stayed with their carers; a carer found reliable had first claim to adopt a ward, but adoption was rare [S47 @2026-11-15], [S102 @2026-11-15]. The Foundling Home's fond is TsGA Moscow f. 108 [S103 @2026-11-15].

- **Regimental churches and an officer’s station.** Find the father’s unit and its station at the event date, then check regimental and garrison books for weddings and baptisms missing from city parishes [S48]. A baptismal extract placed an officer’s son at his father’s station in Ostrog although his Soviet service card gave Tula as his birthplace [S49].
- **A church known by a second name.** A church can be called after the saint of a side altar (придел) or of its lower church as well as after its main dedication. In Tula the Vladimir church za Valom, whose lower church has St Nicholas as its main altar, is known as Николо-Завальская [S104]. When a revision tale names a Nicholas church, list every church known by that name, strike those that the same revision lists separately, and remember that a monastery church was not a parish church [S50].
- **A non-Orthodox spouse.** Apart from native Finns marrying in Finland, a non-Orthodox person marrying an Orthodox one signed a pledge (подписка) before the wedding not to revile the spouse for Orthodoxy or draw the spouse to another faith, and to have the children baptised and raised Orthodox. After the wedding the priest sent the pledge to the diocesan bishop [S105], [S106]. In the Baltic provinces, local natives marrying across the Orthodox and Protestant confessions were excused the pledge from 19 March 1865 until it was restored on 8 August 1885, and in those years could have the children baptised in either church [S106]. So search the Orthodox books for a Catholic or Lutheran father's children, and the diocesan files for the pledge. Read the pledge for the parties’ confession, rank, occupation and named relatives [S51], [S52].
- **A later «оба православные».** Look for the parents’ marriage and any intervening reception (присоединение) by chrismation [S107]. A reported child’s entry calls both parents Orthodox although the marriage names the mother as Lutheran and the reception entry gives her new name [S53]. Check earlier names, including the father’s given name behind a Russian patronymic.

- **A non-Christian or Old Believer spouse joined the Church first.** The law counted a marriage of an Orthodox person with a non-Christian as invalid [S105], and an Orthodox priest could not marry an Orthodox person to an Old Believer in an Orthodox church [S166]. Look for the spouse’s baptism or reception before the wedding and check both original and baptismal names in the children’s entries [S167], [S168].

- **A first list of nearby churches.** Familio's 2021 guide says that each place page has a «Приходы» tab listing the religious communities and buildings in and around the settlement, and that a parish page sometimes lists that parish's confession lists under «Источники» [S108 @2026-11-15]. Use it to start the candidate list [S54 @2026-11-15]. Confirm each candidate in a dated diocesan reference book (step 1).

## 3. Route each parish-year to both custodians

Every parish-year has two possible copies: the parish copy stayed at the church, and the second copy went to the consistory. [S24], [S10] Give each copy its own row:

- **Consistory copy.** Search the consistory fond of the see for the event year and trace any transferred files [S10].
- **Parish copy.** Trace the church fond through ZAGS and district or oblast archives. Inventory transfer notes can name the receiving district ZAGS [S8], [S10].

- **Late nineteenth-century Orthodox Pińsk.** Start from a known cathedral baptism. Use the parents’ recorded names to search for siblings in the births and deaths parts and to look for the parents’ wedding [S195 @2026-11-22]. At the National Historical Archive of Belarus in Minsk (НИАБ), check f. 968 for the St Theodore Cathedral (Пинский Федоровский собор), f. 598 for the Leszcze Dormition parish (Лещенская Успенская церковь) and f. 136 for the Minsk Orthodox Consistory [S196 @2026-11-22], [S197 @2026-11-22]. Verify each parish, year and record part in the inventories before choosing a file.

- **Check the Minsk archive’s request status.** The archive suspended intake for genealogical and thematic research on 2 April 2026 [S198 @2026-11-22]. Check the archive’s Requests and Services page for reopening. While intake is suspended, identify files in the inventories and plan a reading-room search.

- **Books after 1917.** The decree of 18 (31) December 1917 recognised only civil marriage, set up civil registration offices and ordered church registers sent to the city, uezd and volost zemstvo boards. From the decree of 20 January (2 February) 1918, only civil offices kept acts of civil status. [S38], [S39] Church books continued in places: the Irkutsk archive holds Orthodox metrical books of Irkutsk diocese for 1911–1922, and a 1924 circular dealt with church marriages concluded after 20 December 1917 in territory held by the Whites. [S41], [S42] Give a post-1917 parish-year three rows: the ZAGS archive, the oblast archive (consistory and church fonds), and any transfer the inventory notes.

  ZAGS act books stay with ZAGS for 100 years from each entry and then go to the state archive (Federal Law 143-FZ, art. 77). [S40 @2026-11-07] A book's place can still differ from what that term predicts: the Irkutsk archive received the 1911–1922 church books from the oblast ZAGS archive in 2008. [S42 @2026-11-07] Search all three rows whatever the book's age.

- **Check the delo against the inventory.** Verify dates and identify inserted leaves in the file itself [S8]. Search under historic dedications and sees [S10].
  - A file titled by dedication ("книга Дмитриевской церкви", "Никольской церкви") may belong to a church of that dedication in another village, not to a village called Dmitrievka or Nikolskoe. Fix the parish and village from the full file title, the inventory and the entries before you use the book, or its empty search, for the similarly named village. For dedication names that repeat, see [Catholic parish and diocesan record recovery, step 1](catholic-parish-diocesan-record-recovery.md#1-find-the-parish-that-kept-the-register-not-just-a-church-name).
- **Diocesan referrals.** If the diocesan office directs the search to a state archive, follow the referral and check the archive’s own holdings [S24].

- **Open the custodian's own online viewer before ordering.** Some archives publish their books as images:
  - Moscow Glavarchiv publishes metrical books (cgamos.ru/metric-books/) and confession lists (cgamos.ru/ispovedalnye_vedomosti/) as online images in its «Моя семья» service. [S29 @2026-11-02], [S30 @2026-11-02] Have the user open it in their browser.
  - The Sverdlovsk oblast archive (GASO) runs a metrical-book viewer at metriki.gaso-ural.ru. On 2026-11-02 it held only f. 6, the Ekaterinburg consistory, so it reaches the GASO f. 6 dela this recipe cites. Search it with the prefixes "фонд:", "опись:", "дело:" (for example "дело: 01_6_15_100") and "скан:". [S31 @2026-11-02]
  - The Rostov oblast archive (GARO) arranges Don metrical books by settlement and okrug at donarch.ru/metrikbooks/, with scan previews on each settlement page. [S32 @2026-11-02]

  Years missing from an online list are not proof of loss. Browse at a human pace and never fetch in bulk.
- **Before asking a Russian regional state archive to search,** read its current requests page and record the URL and the date you read it. Many of these archives have stopped or limited thematic genealogical searches. Some take a prepayment that is not refunded when nothing is found, and some send users to search the reading room themselves. [S33], [S34], [S35] Route the user to self-search or remote viewing, and order copies by cipher and leaf.

- **Find the delo before you open a film.** For Tula guberniya, A. G. Zaitsev's handbook gives, village by village (by parish church), the fond, opis and delo of the metrical books in GATO [S109 @2026-11-15], [S55 @2026-11-15]. The НашиПредки site (nashipredki.com) gathers FamilySearch's microfilms into catalogues by archive and by parish, settlement or uezd; each row gives the film and digital-folder numbers against fond, opis, delo and years [S110 @2026-11-15], [S111 @2026-11-15], [S56 @2026-11-15]. Take the delo from the handbook or the inventory, find its film there, and open the film at that delo's title sheet [S55 @2026-11-15]. In Tula, most metrical books up to 1920, including books that churches kept after 1917, are in GATO f. 93, the collection of metrical books of Tula and Kaluga guberniyas [S57 @2026-11-15], [S112 @2026-11-15].
- **Moscow and Moscow guberniya in «Моя семья».** Glavarchiv's January 2021 account of the service says to find a guberniya village's church in its parish index (указатель приходов) and then to search both copies: town churches in the fonds of the Moscow church «сорока» (ф. 2121–2126) and in the Moscow Spiritual Consistory's fond 203, village churches in the uezd church fonds and in f. 203 [S113 @2026-11-15]. In f. 203, op. 745 is catalogued as metrical books of Moscow and the guberniya's uezds for 1744–1920, and other opisi hold more [S114 @2026-11-15]. A researcher's walkthrough used the village's uezd to page to the uezd-and-year volume, then found the parish in that volume's list [S58 @2026-11-15]. Check every church of a settlement that had several.

- **District archives.** Include the district archive or district administration’s archive department, then trace any transfer to the krai archive. A researcher read metrical books in a Krasnodar Krai district archive before their transfer, so an oblast-only search could miss the earlier holding [S169], [S170].

- **Museums.** If the archives and ZAGS lack a book, search the State Catalogue of the Museum Fund (Госкаталог) for «метрическая книга» and check whether the holding is a complete book, a section or a single leaf [S171], [S172]. Use [the photograph-collection search procedure](repository-photograph-collection-search.md#find-the-collections-that-cover-the-town-and-period) and give the museum its own row.

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
- **Log what you inspected.** Use [archival image coverage verification](archival-image-coverage-verification.md) to record which parts (births, marriages, deaths) and which leaves you actually inspected.

## 5. When an entry conflicts with other records, read the other exemplar

Order the other copy of the same year as a separate delo. Keep both readings, each with its own locator.

- **Identify each copy.** A multi-year book of one parish suggests the parish copy, and an annual multi-parish volume suggests the consistory copy. Confirm the exemplar from the delo even if both are in the same opis [S115], [S59].
- **Compare names, omissions and corrections in both copies.** Start with the parish copy if it survives. A copyist could substitute a name or leave part of a marriage entry blank, and a correction decree might appear in only one exemplar [S59], [S60].
- **A parish on a guberniya border.** If an entry is missing, check whether the village lay across the border and whether a second consistory copy served that guberniya [S61].
- **Drafts and 1920s recopies.** Some priests kept a draft (the «нулевой» copy) with extra detail such as the parents' ages, address and occupation; in Tula such drafts are in GATO f. 93 and f. 256. In the 1920s many parishes recopied damaged books to hand over to ZAGS; in Tula these copies are also filed as «Метрические книги» in GATO f. 93. They are in post-1918 spelling, usually without the sureties, godparents and officiating clergy [S59]. Find the earlier copies before you rely on one.
- **An unknown town parish.** Search all the town’s consistory volumes and single-church files for the year. A walkthrough identified two 1905 Tula volumes, but the inventory also lists d. 9 а for four more churches [S62], [S116].

- **Check what the clergy were told.** The law prescribed no documentary check on the informant’s account of a birth [S139]. A consistory inquiry traced «законной жены его» in one disputed entry to the godmother’s statement [S173]. Check the named parents, estate and marital status against marriage, birth and family records and any consistory inquiry.

Agreement between copies can repeat an error: both exemplars of one marriage reportedly gave the bride a surname inconsistent with the household evidence [S19]. Test candidates in revision and confession lists, the bride’s birth entry, recorded in-law relationships and later godparent links. Use the range of reported ages to rank candidates and record an indirect identification as such.

An Orthodox metrical date, like other Russian dates written before 14 February 1918, is normally Old Style; check the document's own calendar note. [S43] A Soviet, ZAGS or émigré document may restate the same event in New Style, so a difference of 12 or 13 days is not by itself a conflict. Record both dates with their calendar. For the offsets and the 1918 switch, use [evidence/proof judgment: follow record versions and test disputed dates](evidence-proof-judgment.md#follow-record-versions-and-test-disputed-dates).

A Soviet service card and birth certificate agreed on the year, yet the parish entry with the same parents was in the preceding year [S63]. Check each stated locality and its parishes for the Old Style day a year or two either side.

## 6. Recover a missing marriage

Search the following records for the marriage [S1].

1. The bride's parish, then the groom's.
2. The parish where the first child was baptised.
3. The churches near the residence. An initial search can work back about seven years from the first birth [S1]. Extend it as needed and log the years covered.
4. The confession lists of those churches for the likely years, read as in [reading confession lists](russian-orthodox-confession-list-reading.md#4-compare-the-household-across-several-lists).
5. Officials' personal service files, which can record a marriage.
6. A repeat marriage certificate issued in the Soviet period, for example for an inheritance or a property sale.

**Pińsk and Leszcze.** For a late nineteenth-century Orthodox wedding missing from the Pińsk cathedral books, search the register of the Dormition parish at the former Leszcze monastery church [S199]. A reported wedding of two people recorded as Pińsk townspeople took place in the Leszcze parish on 29 September 1891 [S195].

**Check the catalogue for marriage-inquiry books (брачные обыски).** A reported Dalmatovo book from 1927–1929 (Ф. 330 Оп. 11 Д. 11) counters the claim that all such books were destroyed [S1]. The Omsk archive guide lists 1834–1845 обыски in ИАОО f. 16 op. 9 d. 1, leaves 1–157 [S191].

**Read the обыск and the papers filed with it.** They often say more than the marriage entry.

- **Search terms and dates.** From July 1765 the priest entered a pre-wedding inquiry (брачный обыск) in an обыскная книга; before that a венечная память authorised each wedding. In the late 19th and early 20th century the обыск was also called a предбрачное свидетельство [S117], [S64]. Search catalogues under all three names. A Moscow church's inventory shows the switch: венечные памяти to 15 July 1765, обыски from 24 July 1765 [S118]. Search full text for the older term as well as the catalogue. For 1721–1765, check RGADA f. 280 op. 4 by region and regional holdings such as Novgorod f. 480 op. 2 d. 311 [S65], [S119].
- **What it states.** The обыск covers each party's estate, residence and age, the absence of blood and spiritual kinship and affinity, marital status, free and parental consent, and the documents presented. The groom, the bride, at least two sureties and the clergy signed it [S117], [S120]. The priest recorded his kinship check in the обыск before the wedding [S66]. The form was set in 1765 and changed in 1837, so cite the check's wording, not its point number [S117]. A groom «вдов после первого брака» reveals a first marriage, and «родителей ... в живых нет» or «матери же в живых у неё нет» places a parent's death before the wedding [S121], [S67].
- **The documents presented.** Copy each document the обыск lists, with its issuing office, date and number: metrical extracts, passports, service records, confession certificates, a superior's permission, a merchant or meshchane board's certificate, a landowner's permission for serfs, or a non-Orthodox cleric's certificate in a mixed marriage [S120], [S121], [S122]. Follow the named office or parish for each extract, including a previous spouse’s death [S67], a military or departmental permission [S52], or a birth extract with the godparents and a confession note [S68].

- **Where the papers are.** Look beside the обыскная книга for books of copied marriage documents and for volumes «с приложением брачных документов» [S117 @2026-11-15], [S123 @2026-11-15]. Distinguish an original («в подлиннике») from a copy, even when the copy reproduces every passport field and marks the seal [S64 @2026-11-15], [S69 @2026-11-15].

- **Kinship and the bishop's permission.** Under the Synod decree of 19 January 1810, a marriage in the collateral blood line was forbidden up to the fourth degree inclusive, needed the diocesan bishop's permission in the fifth and sixth, and needed none from the seventh [S124]. Although one researcher saw no second-cousin weddings, a reported sixth-degree marriage had the bishop’s permission [S66], [S70], [S124]. Petitions went to the bishop himself, from the groom, his parents, relatives or guardians, with the parish priest's certificate of the degree and a table of the kinship [S125]. Identify the impediment on the chart: «шестой степени двухродного свойства» in a reported petition referred to affinity through an earlier marriage [S71], [S126].
- **Age.** A Synod decree of 19 July 1830 forbade marrying a groom under 18 or a bride under 16, outside the Caucasus [S120]. The diocesan bishop could permit a marriage when the groom or the bride lacked no more than half a year of that age [S105]. Start the search at the age the bishop could permit. If the birth entry is missing, check the inquiry for a volost family list or census sheet [S168]. A missing permission note leaves the dispensation unresolved [S174]. Verify an overwritten age against the birth entry before deriving a birth year [S72].
- **Soldiers on leave.** From a decree of 8 April 1871, any priest could marry a lower rank on leave with a yellow ticket on the ticket alone, noting on it when, whom and where. Men on short home leave with red tickets needed higher military permission, and the unfit on long leave with green tickets could not marry [S122]. A Tula researcher reports that before 1871 a soldier on temporary leave needed his command's permission [S73]. A soldier groom's marriage may therefore be written on his ticket as well as in the book.

- **Who consented for an orphaned bride.** The law forbade marrying without the permission of parents, guardians or trustees, and when the parents disagreed the father's consent decided [S105]. Record each signer’s stated relationship. «Ближайшие родственники» can identify consenting relatives of an orphaned bride. If the certificate states that a parent has died, it dates the death before the certificate [S175].

**If the bride's maiden name is unknown:**

- **Eliminate candidates.** List every woman with the same given name, patronymic and age in the nearest revision list. Then read the births and deaths parts of the metrical books for those years. Follow each candidate forward and drop those who are accounted for. [S11]
- **Read confession lists by household.** For finding a bride in her home village and for what confirms the result, use [reading confession lists, step 5](russian-orthodox-confession-list-reading.md#5-check-the-household-against-revision-lists-and-metrical-books).
- **Search godmother entries.** Look for the bride's name among godmothers in the months before the likely marriage. [S11]

## 7. Read the formulae literally first

Apply each reading literally, then test it against the rest of the entry.

- **"вдов по втором браке"** on a groom means his second wife has died and he is entering a third marriage. "Вдова по первом браке" means the bride is entering her second. [S1]
- **"полуторный брак"** is a marriage that is the second for one spouse and the first for the other, for example a widower marrying a maiden. Search for the widowed party's earlier marriage and the first spouse's death. [S25]
- **«Сводный брак».** For a 1920s entry, test a civil union without a church wedding against the ZAGS and parish books. That reading of the formula is tentative [S1].
- **«Нзкр».** For незаконнорожденный, keep the father unknown unless another record identifies him. Check marriage entries under the mother’s later surname, civil evidence of paternity and, for Old Believer families, the police marriage register [S13], [S182].
- **«Из раскола».** The label records reception from the Old Belief. A reported entry uses it for a woman whose siblings’ baptisms list their parents as Orthodox [S21].

  Lay out the siblings’ baptisms and look for a gap around the target birth [S21].
- **Several baptisms on one date.** Test a visiting priest’s round against the infants’ birth dates, villages and distance from church, other rites that day and the Sunday or feast calendar. Record the place as an inference [S18].
- **Month headings.** A month written once at the head of a section or column belongs to the entries it heads, not to every date on the page. Take a first entry under a June heading with birth "31" and baptism "1 June": it is a 31 May birth when the previous spread and the date sequence support May. Record the month as taken from context, keep the baptism date separate, and never write "31 June".
- **Possessive name forms in Galician and Western-Ukrainian entries.** Surnames in -ів (Петрів, Михайлів) are possessive adjectives formed from a given name that became fixed surnames, and they are common in Galicia. Their female forms include Павліва and Павлова beside Павлів. [S27], [S28] So in "Іван Петрів" or "Марія Іванова" the second word may name the father or may already be a surname. Decide from the column heading, the grammar and the neighbouring entries, never from the ending alone.
- **"родомъ X" (by origin X) is not a maiden name by itself.** Treat a maiden name as established only when an explicit "урождённая" (née) or other family records state it. Otherwise keep it as a hypothesis.

- **An ordinal wife.** «законная его 2ая жена» in a child's birth entry means the father had married before. Confirm it from his marriage entry, whose groom column states which marriage it was («вторым браком»), then search for the first marriage and the first wife's death [S74], [S127].
- **A convert in the births part.** Check for an adult convert’s baptism or reception in the births part [S75]. Read the stated age and the note before you take the date as a birth. A convert could receive a new name, but an Old Believer joining Orthodoxy could keep his («с оставлением прежнего имени») [S128], and some books record receptions in a separate part, о присоединившихся [S129].
- **A foundling.** A foundling's birth entry reads «дочь (сын) неизвестных родителей» and may say the child was «подкинута к дому» of a named man [S130], [S75]. He is where the child was left, not a parent and not necessarily the foster carer; follow the child under the household that raised it.
- **A serf's owner.** «Господина/госпожи N крестьянин» or «умершей Госпожи N крестьянин» in a parent's description names the owner, which leads to the owner's revision tales and estate papers [S75].
- **Military status labels.** «бессрочно-отпускной» marks a soldier released on indefinite leave before his term was over, «запасной» a man in the reserve and «отставной» a retired man; the entry often names his regiment [S76], [S131], [S132]. To estimate his birth year, apply the rules of his call-up year and give a range. The 1834 regulation released lower ranks of the reserve battalions on indefinite leave after 20 blameless years, liable to recall until their 25-year term ended [S132]. The 1874 statute took men at 21 for 15 years, 6 active and 9 in the reserve [S133]. Later rules set 18 years, 5 of them active, for men who had turned 20 by 1 January of the call-up year [S134]. A man on indefinite leave after 1874 could have entered service before the statute changed [S77].
- **Births are filed by baptism.** A birth entry stands under the date and month of the baptism, not of the birth [S135], [S75]. Next-day baptisms are reported [S78], but a regional researcher found an interval of a year [S135], and the priests’ manual itself distinguishes village custom from delays of two or three years (§65) [S136]. When a birth is missing from its month, search the following months and later annual books, including the second and third years after birth, and record a birth known only from its baptism as on or before that date.
- **Death-entry columns.** The last column of the death part, «Кто совершал погребение, и где погребены», gives the officiant and the burial place [S137], [S79]. «Не исповедан и не приобщен», with a cause such as «по внезапной смерти», or a blank «кто исповедовал и приобщал» column marks a death without the last rites, usually a sudden one [S138], [S80]. Read the wording against the deceased’s age [S138]. A note of the стан police officer (пристав) in that column, or a pristav's certificate filed with the entry, means the police examined the death, and burial could then come well after the usual two days [S80], [S129]. Follow it to the police file.

- **«Погружен бабкой».** In danger a midwife could baptise the newborn, and the priest completed the rites if the child lived [S136]. Read бабка here as the midwife who baptised the child and check the following days for a burial [S176].

- **Test for an earlier wife.** Work back from the known wedding and look for children whose baptisms name the same father with a different mother. Compare their death entries with the baptisms and check whether the candidate wife’s death preceded the known wedding [S195]. Use an earlier marriage entry or the later entry’s marriage-count or widowhood wording to test the sequence.

- **Deaths under the head of household.** Search a wife’s or child’s death under the husband’s or father’s name, including in indexes. Check which column names the deceased [S177], [S178].

- **Infant causes of death.** Copy the recorded cause, such as «от слабости», «от родимца» or «от младенческого» [S179]. A historical glossary can clarify a word like родимец, but the record alone cannot establish a modern diagnosis [S180].

- **«Сводная жена и незаконные дети их».** Interpret this heading in the context of the consistory’s register of Old Believers [S181]. An 1895 study reports churchmen calling such marriages unlawful unions, and notes that from the law of 19 April 1874 an Old Believer marriage counted as proved from the day it was entered in the metrical register kept for Old Believers by the police [S182]. Read the heading as the consistory's label for an Old Believer marriage, not as proof that the couple never married or that the children had another father, and look for the police register entry.

## Reading the page

Apply these checks to human and machine readings. They draw on a whole-parish transcription report. The underlying images and run outputs were not independently inspected [S164]. See [AI documentary-record verification and image-quality guidance](ai-for-documentary-records.md#the-pitfalls-worth-internalizing-the-least-obvious-most-llm-usable-part).

- **Fita in given names and patronymics.** Reading «Ѳевронія» as «Евфросія» reportedly produced a false match [S164]. Check every apparent С-/Е- name initial for the oval and crossbar of Ѳ. Compare a crop from the original with the full line, following the AI recipe's image-quality cautions, and leave an uncertain letter open. Keep the written form beside any search form; for Ѳ/Ф variants use [pre-reform spelling lanes](corpus-seeded-name-search.md#diagnose-three-different-failures).

- **Year digits in «19__» headings.** A reported reading turned a 1908 heading into 1918 [S164]. Recheck every header against neighbouring headings, entry dates, the running м./ж./№ counters and monthly totals. After reading the book, build a frame-to-year map in binding order. Check for monotonic years within each continuous parish sequence, allowing for reverse-year binding [S164]. Flag every break and investigate an uncertain digit, a misbound leaf or an inserted document; never sort the frames or force their years to fit. Counters and totals are consistency checks, not independent proof of a year. Keep the raw header reading, the assigned year and its basis, or mark the year unresolved.

- **Counters and totals.** Track the birth columns' м./ж. counters separately and the marriage №, following the page's own headings. The report uses these with monthly and annual totals such as «Итого въ Іюлѣ…» to flag missing or doubled entries and clerical numbering slips [S164]. Record the first and last counter of every parish/year/part actually read, with the frame or leaf range and any gaps. Keep the written total, the sum of its columns and your own entry count separate, as in [coverage as pages × targets](archival-image-coverage-verification.md#report-coverage-as-pages--targets) and [the book's own totals](russian-village-family-reconstitution.md#2-state-an-identity-as-an-inference-until-countable-checks-agree). Reconcile discrepancies on the images; never add, drop or reclassify an entry, or change a year, sex or status, to make a total agree. A counter jump alone does not prove a missing scan.

- **Misbound leaves and inserted sheets.** Check for reversed leaves, bound-in parishes, later extracts and police papers [S164]. Join split entries by counter within the same parish/year/part, checked against the dates, people and column continuation; retain both fragment locators. Transcribe each sheet under the parish named on that page and distinguish its document date from any event date it copies. If either is absent or unreadable, keep it unknown rather than inheriting the cover's parish or year. Record where the sheet is bound, even when it interrupts the year sequence.

- **Status and confession as written.** The reported transcription turned «оба раскольники» into «оба православные» [S164]. Copy the literal words before interpreting them under step 7. Never fill estate, military status or confession by default; preserve a blank or uncertain reading as such, including where the surrounding entries repeat a formula.

- **Later marginal notes.** Check both margins for dated extracts, conversion notes and consistory decrees [S164]. Link each note to its entry but give it its own date and wording, keeping the original event date separate. Do not assign the entry to the note's year. Follow [step 8](#8-copy-every-margin-note-as-its-own-dated-event-and-follow-it) for the issuing body, decree number and next record; leave an unstated date or recipient unknown.

## 8. Copy every margin note as its own dated event and follow it

Copy each note in full, with its issuing body, date and number, as a separate observation. Do not merge it into the entry.

- **Divorce.** Copy the eparchial decision, Synod confirmation and recording consistory decree separately, including their dates, numbers, penance and permission to remarry where stated [S1], [S17].

  Follow cross-references in both margins to the consistory divorce file and any later remarriage entry. Search by both spouses’ surnames (Ekaterinburg, GASO f. 6 op. 4; Perm, GAPK f. 37 op. 5) [S17].
- **Limits on divorce notes.** «Разошелся» means separated. A reported search found no note on the marriage entry examined, so check both copies before ruling out dissolution [S17]. One spouse reportedly made agreement conditional on naming adultery as the ground, so distinguish the decision’s wording from independently established events [S17].
- **Legitimation.** Follow the marginal consistory decree to the named court and its decision, even across provincial boundaries [S17].
- **Adoption.** Check birth entries for pasted-in notices as well as marginal text. Record the receiving ZAGS office, issuing body if stated, certificate number, adopter and all changed names [S5]. Absence of a note leaves adoption unresolved.
- **«Выслано».** A reported 1951 «выслано» on a soldier’s birth entry neither identifies the requester nor establishes that the soldier was then alive [S9]. Copy the position, wording and date, identify what was sent if stated, and follow the post-war paperwork.
- **Official communications in death entries.** Copy an «отношение» with its issuing office, date and number, then search the physician’s or court investigator’s own file series [S15].

- **Corrections by decree.** When a birth name conflicts with later records, check both copies for a later correction and its decree [S81]. Corrections needed an inquiry. A consistory without full evidence was not to restore or correct an entry, and a dispute about the facts of a birth went to the civil court [S139].
- **Grounds for divorce.** Under the 1841 Statute of Consistories, a church court could dissolve a marriage at one spouse's petition only for proven adultery, incapacity for married life, a sentence with loss of all rights of status or exile to Siberia with loss of rights, or a spouse's unknown absence. A marriage also ended when both spouses, with no young children, took monastic vows [S140], [S82]. Until 1904 the spouse guilty of adultery was condemned to lifelong celibacy; from 28 May 1904 the Synod set a seven-year penance instead [S140]. Read a dissolution note's ground against that list and its date.

## 9. Treat names and patronymics as hypotheses

- **Search the baptismal form of a given name.** The priest wrote the calendar (святцы) form at baptism, while revision tales, confession lists and family memory often keep the everyday one. Search both: Ксения for Аксинья, Гликерия for Лукерья, Иулиания for Ульяна, Агриппина for Аграфена, Евдокия for Авдотья [S83], [S141], and Георгий for a Юрий born before 1917 [S84], [S142]. A name missing from the calendar of the time, such as Светлана, was not given at baptism, because baptismal names were taken from the calendar [S85], [S143]. Search Полина as Пелагея (Пелагия) and Аполлинария [S86], [S144], [S145]. Check unfamiliar names such as Конкордия against the calendar before inferring ancestry or social rank [S87], [S143].
- **One remembered form can lead to several calendar names.** Include Дмитрий and Митрофан for Митя, Глафира for Глаша [S146], [S147] and Манефа as a lead for Маня [S88]. In Tula material, test Диомид and Дометий for Дементий, and Алипий, Филипп, Феофан and Вонифатий for Алифан [S81], [S148]. Also try Васса for Василиса [S89], [S149], Евплович and a form derived from Якуб/Иаков for Егупович [S90], [S150], and Гали as well as Галина for Галя [S91], [S151]. Include Юрий itself alongside Георгий for Юрий [S84], [S152]. Verify each lead against the household.
- **One man can appear under two forms.** One parish may write the secular form of a man's name and another the baptismal one. The son’s baptism names his father Юрий [S153], and a genealogy adds Евтихий [S154], but the proposed use of Евтихий as the Lermontov baptismal name remains unverified [S92]. A man baptised Иосиф can be Осип, the old Russian form, in later entries [S93], [S155]. Compare his patronymic, his wife and his years before you split him in two, and search his children as both Осипович and Иосифович. In southern Russian speech, which covered Tula guberniya, ф was said as хв or х, and priests sometimes wrote names as heard, such as Мархва for Марфа and Трохвим for Трофим; the same spelling in other names of the entry confirms it [S94], [S156].
- **Look-alike names can be different saints.** Check a period calendar before you merge two similar names. Ермил and Ермолай, on 13 January and 26 July Old Style, are distinct saints in the period calendar [S95], [S157], [S158]. Old editions write the day in Cyrillic numerals, with the units first for 11 to 19 (ГІ = 13) [S159]. Some books write the name-saint's day under the child's name, but one day can serve two saints: Гали and Галина of Corinth share 10 March Old Style, and Галина also has 16 April [S91], [S151], [S160]. Read the name as written and use the day only as a check. Archbishop Sergiy (Spassky)'s «Полный месяцеслов Востока», first published in 1875–1876, sets out the saints [S91], [S161].
- **The baptismal name itself can be wrong.** Errors in birth entries most often concern the name [S139]. Check the burial, confession lists and civil papers for another given name [S162], [S96]. A different name in confession lists or civil documents does not by itself exclude a baptism entry: test the date, the parents and the godparents.

- **Sound-alike names.** Search pairs such as Аксинья/Анисья or Фёдор/Федот separately. Check for everyday forms such as Авдотья for Евдокия, Лукерья for Гликерия and Аксинья for Ксения. Use patronymic, spouse and age to decide whether entries belong together [S183].

- **A name-saint gives a window, not a birth date.** By old custom the baptismal name was taken from the saints commemorated on the day of baptism, by stricter tradition from the saint of the 8th day after birth, and later parents also chose freely, for example after relatives [S184]. Check the saints for the day of birth, the 8th day and the 40th day [S185], [S186]. One reported baptism fell between the child’s birth and the namesake saint’s feast, so none of those dates was interchangeable [S187]. Use a name's feast only to rank possible birth dates within those weeks, never to fix one, and compare the dates in the same calendar style.

- **Bridge name forms in a kinship proof.** A reported ZAGS decision treated Иосифовна and Осиповна as a break in the documentary chain [S188]. An archival certificate preserves the entry’s wording and may flag a discrepancy «так в документе» [S189]. Obtain the page to check the reading and find a record linking the two forms.

- **Missing surnames.** Search by given name, patronymic and village, reconstruct the confession-list household and bracket arrivals between revisions. A surname thought to have appeared later was reported in a godparent entry [S4].
- **Unstable surnames.** Test several surnames for one person [S14], changes of ending (-ов/-ев/-ских) [S7] and names derived from a place of origin. Also search given-name variants such as Дионисий/Денис [S12].
- **Godparents.** A period manual requires an Orthodox godfather for a boy or an Orthodox godmother for a girl and excludes the child’s parents as sponsors [S190], [S136]. Record each sponsor’s role and any stated confession. A godparent entry alone cannot identify a parent [S11].
- **Patronymics.** A reported service-file abstract attributes a man’s patronymic to his godfather [S23]. A marriage entry reportedly calls a godfather «father», and a child’s names could also match the maternal grandfather [S11]. Check the stepfather and foster household, keep each surname separately and verify the relationships in other records.
- **Converts.** When a convert shares a household head’s names, test descent, naming by a godfather and adoption. Check the conversion baptism, its sponsors and later revision households [S16], [S22]. Record an age discrepancy as a reason to rank the link lower.
- **Adoption before 1917.** Follow «приемный» in revision and confession lists and check the child’s later entries as spouse, sponsor, guarantor and parent [S14].

  Search both birth and adoptive names. Check the marriage entry for birth names, marginal notes for a change of surname, and consolidated revisions for place of origin [S14].

  These traces describe a child raised in another family. A missing church act is not proof that no formal adoption file exists, and the procedure has not been checked. For a formal adoption, search for a court or administrative file and for a matching margin note on the birth entry, and take the procedure from Свод законов vol. X.
- **Household and age tests.** A shared godparent family or co-residence is support, not identity. Test each hypothesis against:
  - confession-list households across several years
  - revision-list candidates of matching age
  - godparent patterns.

  Leave the ruling to [evidence/proof judgment](evidence-proof-judgment.md). [S11], [S19]

- **Surnames in other series.** Look in revision tales for surnames omitted from parish books [S97], and in metrical books when revisions omit them [S163]. One family reportedly used three recurring surnames before the Soviet period, so a later record under one of those forms need not imply concealment [S98], [S163].
- **One full name in several roles.** If the same name repeats for different participants, check for a clerical slip and a later correction. Verify each role in other entries [S99], [S139].

- **Follow godparents and marriage guarantors.** Copy the names of baptismal sponsors (восприемники), marriage guarantors (поручители) and any separately listed witnesses. Preserve each role and any rank, title or office the entry gives [S192], [S193]. Use a recorded noble title to check the relevant guberniya’s nobility registers, or a named civil office to check that institution’s service lists (формулярные списки) [S194]. Require separate evidence before claiming kinship or descent.

- **Read and compare godparent descriptions.** Copy explicit kinship beside the godparent’s name. Use a stated paternal uncle, father’s sister or mother’s sister to search for that sibling in the corresponding parent’s family [S195]. Across sibling baptisms, compare a godmother’s given name and her father’s given name when the surnames differ. If both given names agree, keep both surnames as leads and check a marriage or another record for a link before merging the entries [S195].

- **Test a mother’s -owa form against a property notice.** When the ending could mark a patronymic or a surname, search under the family’s recorded surname variants. Look for a notice that gives the seller’s surname and spells out her father’s given name [S200]. Match the seller to the mother using other details before adopting the patronymic reading.

## 10. Use machine-read full-text search for leads, never for a negative

Yandex «Поиск по архивам» (yandex.ru/archive) searches machine-recognised text of 18th- to early-20th-century metrical books, revision tales and confession lists. It names archives of Moscow and of the Astrakhan, Orenburg and Irkutsk regions, among others. Viewing a document needs a login, which the user does. [S26] Its catalogue (Источники) lists the holding archives in full: 29 on 8 October 2026, against about nine in July 2023. [S37] Have the logged-in user open the catalogue and record the archives it lists, with the date, before you treat a miss as a coverage gap.

Yandex's 20 May 2026 announcement describes event and participant-role filters, with examples
including child, father and mother in birth records, and groom, bride and witness in marriages
[S165 @2026-11-16]. Have the logged-in user confirm which filters the current view offers.
Run a role-filtered search and an ordinary text search separately, recording the filters and
volumes actually covered. Check each candidate's name, role, place and dates in its own entry
on the image: structured machine fields are another interpretation of that image. The
announcement does not establish filters for godparents or marriage sureties; search ordinary
text and browse the relevant entries for them. A role-filter miss leaves unmarked or
misclassified entries unresolved.

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

   Name every delo opened for that year. Include the frame-to-year map in binding order, first/last counters for each parish/year/part read, inspected frame or leaf ranges and gaps, and the written totals, column sums and your own entry counts with any unresolved discrepancy.
2. **Literal entry transcriptions.** Keep the locators of every fragment of a split entry. Put each margin note on its own row with its date, issuing body, number and follow-up series (consistory divorce case, court, ZAGS, physician or investigator).
3. **Name and parentage hypothesis register.** Give each competing explanation and the confession-list, revision-list and godparent tests applied to it. Give ages as ranges. A range mismatch lowers a candidate's rank and never removes it.

Call an entry absent only for the dela, exemplars and frame/leaf and counter ranges you actually read, with unresolved gaps stated.
