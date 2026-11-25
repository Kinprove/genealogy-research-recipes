---
id: "russian-estate-registration-status"
title: "Read a Russian-Empire estate label as a dated registration status and choose the series by date"
summary: "Read a Russian-Empire estate label as a dated registration status and pick the record series by when it was acquired."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "RUSSIAN-ESTATE-REGISTRATION-STATUS-01", "text": "**A town mark on мещанин or купец names the society of registration, not the birthplace or residence.**"}]
handoff: ["russian-revision-list-household-chaining"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Russian Empire and Soviet Union", "order": 111}
---

# Read a Russian-Empire estate label as a dated registration status and choose the series by date

Use this recipe when a record gives an ancestor's estate (сословие) with a place: "Ирбитский мещанин", "Далматовский 2-й гильдии купец", "личный/потомственный почетный гражданин", "Каменского завода сельский обыватель", or a translated label such as "Honorary Citizen of [town]". These labels cause four common errors:

- reading the town as the birthplace or residence;
- reading "завод" or "сельский обыватель" as a job;
- accepting a status that did not exist on the claimed date;
- sending a person who was admitted after the last revision to the 1858 revision list.

The recipe builds a dated status timeline for each person, tests each status against its chronology, and chooses the record series by the date the person acquired the status. The method works anywhere in the Empire. The fund and дело numbers below are Ural examples (GASO, GAPK, Kungur, Shadrinsk), so for another region look up the matching series in that region's archive.

Related recipes cover the neighbouring ground:

- For registration (приписка) versus residence in Jewish families, a merchant reverting to his former estate, and naming mechanisms, use [Russian-Empire Jewish identity attribution](russian-empire-jewish-identity-attribution.md).
- For keeping registration, residence and event place in separate search columns, use [JewishGen search and family reconstruction](jewishgen-search-family-reconstruction.md).
- For choosing Ukrainian archival cases by society, use [Jewish archival list triage](jewish-archival-list-triage.md).
- For getting from an emigrant to the locality and archive, use [Russian-Empire emigrant origin recovery](russian-empire-emigrant-origin-recovery.md).
- For AI transcriptions and translations of status words, use [AI for documentary records](ai-for-documentary-records.md).
- For identity rulings, use [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- 1\. Parse the estate phrase into separate fields
- 2\. Test each status against its chronology
- 3\. Date when the person acquired the status
- 4\. Choose the record series by the acquisition date
- 5\. Search where the family actually lived
- 6\. Treat catalogue annotations and absences as leads
- Output: status timeline and series worklist

## 1. Parse the estate phrase into separate fields

For each record, copy the estate phrase exactly as written, with its date, record type and locator. Then split it into these fields:

- **Status:** мещанин, купец of a named guild, купецкий сын, личный or потомственный почетный гражданин, сельский обыватель, крестьянин, and so on.
- **Registering society:** the town, or the works settlement or volost, that the status belongs to.
- **Residence:** for example "временно проживающий в г. Ирбите", or "проживающего в Невьянском заводе [town] … купецкого сына". [S7], [S3]
- **Occupation:** teacher, clerk, trader, and so on.

Rules for reading the phrase:

- **A town mark on мещанин or купец names the society of registration, not the birthplace or residence.** A мещанин of Irbit could live anywhere and was only registered there. Factory parishes record many "[town] мещанин" families living outside the town, including some marked "временно проживающий". [S8], [S3], [S7]
- **Separate "a merchant in Petersburg" from "a Petersburg merchant".** Only the second names the merchant society whose fund you should search. [S2]
- **"X-ского завода" names a settlement, not an employer.** A завод here is a populated place, of the kind later called a посёлок. [S4]
- **"Сельский обыватель" and "крестьянин" are estate categories, not jobs.** Never record them as an occupation. Participants describe two ways the label was applied:
  - factory мастеровые were moved into this category after 1861, when they were released from compulsory works labour, for example "сельский обыватель Берёзовского завода" [S5];
  - сельский обыватель also applied to peasants, including people living in town [S4].
  A works-settlement address does not show that the family were works people. Follow a family into the works (заводские) records only when a record shows it among the former мастеровые; otherwise search the records of its documented registering community and estate category.
- **"Почетный гражданин" is an estate, like мещанин or дворянин, not an honour from a particular town.** The estate existed from 1832 to 1917, and it was either personal (личный) or hereditary (потомственный). Always record which one. [S13], [S1]
- **Formulary lists give birthplace and estate as separate facts.** For example, a man born in the city of Perm could be registered "из крестьян [X] волости [Y] уезда". Keep both fields, and search the registering community as well as the birthplace. [S12]

- **Trace the issuing society through the passport.** Copy the holder’s status, the issuing office, date and number. The authority for a мещанин or peasant might be the мещанская управа, town elder or volost board [S21], [S22]. A Moscow baptism in 1907 cites a Klin town elder’s passport, while a 1908 baptism gives separate numbers and dates for the father and mother [S23]. Search the society the document names and record residence from evidence of where the holder lived.

## 2. Test each status against its chronology

Test every status before you search for it:

- **3rd guild.** The 3rd merchant guild was abolished in 1863. After that, a former 3rd-guild merchant either declared capital in the 2nd guild or became a мещанин, even if he went on trading. [S2], [S8] A "3rd-guild merchant" born in the 1880s is an anachronism. Look for 2nd-guild or мещанин registration instead, or move the claim to a parent's or grandparent's generation. [S2] People also moved between estates before 1863, so a record can show someone as мещанин who was earlier a 3rd-guild merchant. [S7]
- **"Почетный житель" or a translated "Honorary Citizen" with a place.** "Почетный житель" of a town or shtetl was not a status. For a translated "Honorary Citizen", record the status and the locality in separate fields, get the original-language wording, and only then map it to потомственный or личный почетный гражданин and test both possibilities (§4). [S1]
- **First guild.** Check for a transfer between merchant societies before interpreting a disappearance as a death or a move (§4) [S2]. For a Jewish merchant relying on guild membership to live outside the Pale, check the city and years of membership. The 1859 law’s qualification was two years already spent in the first guild within the Pale when the law was issued on 16 March, or five years under the new rule [S54]. Remaining outside after leaving the guild generally required ten continuous years in the first guild outside the Pale. Moscow required permission from the finance minister and governor-general and residence rights under this rule lapsed on resignation [S54], [S55].

- **«Временнообязанный» and «крестьянин-собственник».** A временнообязанный peasant was personally free but had not redeemed his land and still owed the landowner obrok or barshchina for it [S24]; record the landowner an entry names beside the label [S25]. On redemption the state paid the landowner, and the peasants became крестьяне-собственники who repaid the state until the payments ended on 1 January 1907 [S26]. The 1868 birth and 1872 marriage entries mark the transition to redemption with «крестьянин-собственник». Neither dates the household’s final payment [S25], [S27]. Redemption was compulsory from 1 January 1883, and by the end of the 19th century временнообязанные remained only in Transcaucasia. [S24]

- **Find a redemption file by landowner and village.** In RGIA f. 577 (Main Redemption Institution), choose the guberniya’s inventory. Op. 46 lists 1,278 Kherson files with titles naming landowners and villages [S51 @2026-11-19]. For Tambov, the cited 1870 title combines the landowner А. М. Ратч with деревня Любезная, Kozlov uezd [S50 @2026-11-19]. Search both names.

## 3. Date when the person acquired the status

A status in one record does not show the status at birth, the status of siblings, or the status of the father.

In an Orthodox marriage entry, record each spouse’s stated мещанин or мещанка status and registering town on the marriage date [S63]. Keep a family tradition of noble descent as an open lead and test it in records of the earlier generations [S62].

- **Service (formulary) records.** These record grants. The wording in participants' extracts includes "пожалован в звание личного почетного гражданина", "утвержден в звании потомственного почетного гражданина" and "за выслугу 10 лет в гражданской службе утвержден в звании личного почетного гражданина". They give the estate of origin separately, as "из мещан", "из солдатских детей", "из заводских детей" or "сын личного почетного гражданина". Date each transition separately. An 1859 discharge from the military department and admission to the Perm мещане preceded an 1871 grant of personal honorary citizenship to the same man [S9].
- **Date a transfer from the revision remark.** Read «причислен из» and «записался … из» for the former estate and year of admission. The cited 1858 return dates a former serf’s admission to 1852 (GAPK f. 111, op. 1, d. 1890), and the 1850 return dates another admission to 1849 (ГАШ f. И-605, op. 1, d. 8) [S7]. Preserve the direction of a transfer: «выбыл в Екатеринбургское купечество» in 1831 and «перешел из Екатеринбургского купечества» in 1843 point to opposite sides of the register. Record exactly who moved when a remark names more than one person, as in the father and son admitted to the Yekaterinburg мещане in 1818 [S11].
- **Read the status of witnesses and godparents.** Bracket a transfer with the person’s latest explicit old registration and earliest explicit new one. An 1892 witness entry calls the father an Alapaevsk мещанин, and a 1901 entry does the same for his son. The father’s earlier marriage in Petrokamenskoye in 1861 establishes the event place alone unless it states his registration [S6]. Likewise, a merchant’s son serving as godparent in another town’s parish supplies no address without residence wording [S7].
- **Search printed administrative lists for a missing registration.** The 1908 Ведомость справок о судимости gives «мещанин г. Белебей», a lead to Belebey’s society records. Transcribe the estate and town separately from the place of the offence or any address [S2].

  To reach the printed Ведомость справок о судимости when the year is unknown, search the Russian State Library catalogue (search.rsl.ru) for the annual alphabetical index of names (Алфавитный указатель имен и фамилий лиц, помещенных в Ведомости справок о судимости) for the right part (часть) and year. The catalogue lists such an index by part, for example 1886, ч. 2 (general courts), with a free online scan. [S14] Read the surname's entry number in the scan, then open that year's issues of the same part, which are split into numbered books (кн.). [S15] The index for a year can be printed the next year (the 1886 index appeared in 1887), so do not cite the publication year as the conviction year. [S14] The entry number is not a page or book number. An empty catalogue or OCR search is not a negative for the scan.

- **Find a missing treasury chamber decree in its monthly meeting journal.** A date in the 1850 Klin revision led to the Moscow Treasury Chamber’s decision of 30 March 1840 admitting a family of ямщики from the state peasants to the third guild (TsGA Moscow f. 51, op. 1, d. 373) [S28], [S29]. Follow the request back to the Chamber of State Properties and the orders forward to the town duma and uezd treasury. For the town’s copy, look for enrolment files such as Orenburg’s 1851–1867 мещане file (OGAOO f. 368, op. 1, d. 535) [S28], [S30].
- **Take the year of enrolment from a merchant family list to the petition.** In Tula, search f. Р-1905, op. 5 even for pre-1917 lists: its 1890/1891 list compares the family across both years, and the enrolment year led to a petition in f. 174 naming the former estate and village, Новое Павшино, Aleksin uezd [S31], [S32]. Check the relevant year’s entry in the inventory.
- **Part 2 of a noble genealogy book identifies the military route to hereditary nobility.** [S33] Date the qualifying ancestor's rank from his service record: hereditary nobility came with the first ober-officer rank, from 11 June 1845 with a staff-officer rank received in service rather than on retirement, and from 9 December 1856 with the rank of colonel. [S34] Record each child's birth date and estate at birth against that date: children born before it in a taxable estate shared the nobility only under the law of 5 March 1874 [S35], except that a military father with no children born after his promotion could petition for the nobility of one earlier-born son [S43]. Look for such a petition before you date a son's nobility from 1874. A Vladimir Part 2 admission in 1838 followed the former serf’s recruitment in 1815 and later promotion to ober-officer [S36]. Look for the promotion date and original estate in the service record, and for the birth in the parish books.

- **Find a noble family in its guberniya's genealogy book, by part.** Under the Charter of 1785 each guberniya's noble deputy assembly kept its own genealogy book in six parts: 1 nobility granted by the sovereign's diploma, 2 military nobility, 3 nobility earned by civil rank, 4 foreign noble families, 5 titled families, 6 ancient families whose nobility went back 100 years or more. Only hereditary nobles were entered; personal nobles were not. [S33] A genealogist advises opening the book of the guberniya concerned [S44], and an index on the heraldry site goldarms.narod.ru gathers lists of the families entered in the books, guberniya by guberniya. [S45] Search the book of the guberniya where the family was registered, read the part that matches how it gained its nobility, and do not read a personal noble's absence from the book against the status.

If the bracket is open, record it as open. Do not fill the gap by assuming the status was inherited.

## 4. Choose the record series by the acquisition date

The 10th revision (1857–1859) was the last; later revision-list files also survive. [S16] Town lists of that revision are usually dated 1858 and are called the 1858 revision below. Compare the acquisition date or bracket with that revision before you send anyone to a revision list. [S10] For an Orenburg Cossack household after 1834, check the holding archive's inventory for which revisions exist; see [revision-list household chaining, step 10](russian-revision-list-household-chaining.md#10-for-an-orenburg-cossack-household-confirm-which-later-revisions-exist).

**Honorary citizens, whatever the acquisition date.** Go first to the honorary-citizen grant files and formulary lists under the post-1858 branch below; RGIA f. 1343, op. 39 starts in 1830. Do not let the revision cutoff decide their series. [S1], [S9]

**Status held by the 1858 revision.**

- Read the registering society’s revision for household composition and any explicit residence remark. The Irbit мещане revision of 1858 lists households without their addresses [S8]. In the 1816 Yekaterinburg revision, «имеет жительство у отца своего» places a daughter with her father (GASO f. 8, op. 1, d. 453). Establish the father’s address before assigning one to her [S11].
- Check every sub-series. A participant listed how Yekaterinburg 1858 is split in the GASO catalogue: f. 8, op. 1, d. 1776 (цеховые мещане), d. 1777 (мещане), d. 1778 and 1778а (частные сказки), and d. 1779 (newly admitted мещане). [S3]
- Merchants and мещане of one town and one revision are often in separate дела. Participants cite GAPK f. 111, op. 1, d. 2461 (1834 мещане) and d. 2463 (1834 купцы), while d. 2471 (1850) covers купцы, мещане and цеховые together. If a family is missing from one list, check its remarks and then the other estate's list. [S11]
- A participant cited digitised Yekaterinburg revision lists for купцы, мещане and цеховые on "Поколения Пермского края" (GAPK f. 111, op. 1, d. 2413, 2415, 2416). [S3]
- Read the confession note at the foot of the page for each person. A household can mix Orthodox and Old Believer members. [S3]

**Status acquired after the 1858 revision.**

The original 1858 return predates the new status [S10]. Check the following series.

- **Later revision tales of a single estate.** Some archives hold revision tales of one estate compiled after 1858, so read the registering society's inventory for them first. The Astrakhan treasury chamber's fond in the State Archive of Astrakhan Oblast holds revision tales of the мещане of Astrakhan and its guberniya for 1858–1877 (f. 687, op. 2, d. 2144) and for 1880 (d. 2508) [S47 @2026-11-15], [S48 @2026-11-15], and the Orenburg town duma's fond holds supplementary tales of the 10th revision for the town's мещане, 1859–1862 (OGAOO f. 368, op. 1, d. 531). [S49 @2026-11-15] A genealogist says such tales were compiled by estate in some regions from 1858 to 1897 [S46 @2026-11-15]; no file later than 1880 was checked here. Take each file's dates from the file, not from the inventory range.

- **Admission (причисление) and transfer files.** Participants cited GASO f. 8, op. 1, d. 1922 and 1922а (1864, works people discharged into the town мещанство) and d. 1935а (1867, an enrolment file for the мещанское общество). [S3] For a works serf in 1858 described as a Kungur мещанин by 1867, the reported lead is Kungur city archive f. 585. Request its inventory for lists, a revision and admission petitions after 1864 [S10].
- **1874 conscription family lists and later call-up lists in the city administration (городская управа) fund.** These substitute for revision lists at household level. A participant cited GASO f. 62, op. 1, d. 27а (Yekaterinburg мещане family list, 1874) and d. 28 (call-up lists 1878–79). [S3]
- **Honorary-citizen grant files.** Choose the inventory in RGIA f. 1343 by status and date. Op. 39 (1830–1890) and op. 40 (1890–1917) cover hereditary grants [S56], [S57]. The op. 41 heading covers personal grants from 1833–1917, although the fond summary starts that series in 1890 [S58], [S59]. Op. 47 (1897–1917) says only «почетного гражданства», and the fond summary groups it with hereditary grants. Read the individual grant before assigning a status [S59], [S60]. Also check the provincial archive [S1]. Provincial formulary lists can record the grant, including the cited GAPK f. 36 and f. 111, op. 1, d. 1030–1034 [S9], [S12].
- **For merchants of any date**, a participant listed these series:
  - guild-certificate cases and registers of trade certificates;
  - family lists of the мещанское and купеческое общества;
  - declarations of people who wished to join a merchant society;
  - lists of property owners;
  - alphabetical lists of a province's merchants.
  Follow the footnotes of local merchant studies to the relevant society and fonds. For a transfer, search both towns’ first-guild records. The reported 1914 transfer from Vasylkiv to Kyiv has a specific file reference, RGIA f. 573, op. 13, d. 15303. Verify the file for registration and look elsewhere for evidence of a residential move [S2].

- **Moscow мещане: find the sloboda, then the family number.** Catalogue data of the Central State Archive of Moscow (TsGA Moscow), as listed by NashiPredki, give f. 5 as the Moscow мещанская управа with one inventory [S17 @2026-11-08] and title the 1782 revision books of Moscow merchants and мещане («купцов и мещан») by sloboda, for example Taganskaya (f. 51, op. 18) [S18 @2026-11-08]. A genealogist's 2024 account says that metrical books, revision lists and confession lists name a family's sloboda, that f. 5, op. 1 holds alphabetical lists of мещане by sloboda and sloboda books in which each family has its own number, and that the sloboda's alphabetical list should be ordered first when the number is unknown [S19 @2026-11-08]. Record the sloboda in the registering-society field (§1), not as an address. Citations from before 2013 may name the Central Historical Archive of Moscow (TsIAM), which Russian Wikipedia says became part of TsGA Moscow in April 2013 [S20 @2026-11-08]; check file numbers in TsGA Moscow's own inventory before citing them.

- **Moscow sloboda books: go from the revision numbers to the revisions.** A sloboda book gives each family's numbers in the 9th (1850) and 10th (1858) revisions and when and from which estate each man entered the мещане. [S19] Open the 1850 and 1858 revisions by those numbers, take a post-1858 admission date from the column on entry into the мещане (§3), and read the «Приметы», occupation and remarks columns for passports and addresses. [S19], [S37]

**Limits on substitute lists.** A participant expected community tax-allocation (раскладка) files to list at most heads of household, not full families. Do not promise family detail from them. [S1]

**Read a substitute list's coverage and columns before you read an absence or an age.** A family list made for the call-up can list males only, and a tax list names only the people liable, so a wife or daughter missing from either says nothing about her death or about who the mother was. Take each age's reference date and each figure's meaning from the column headings, not from the year on the file's label; if the headings leave an age's reference date open, record no birth year from it. The full checks are in [volost and town administration records, step 6](russian-volost-town-administration-records.md#6-record-inspected-entries-as-household-observations).

For hereditary nobility, pair a provincial noble genealogy-book entry with the admission or confirmation file, preserving the province, part and date. The FEEFHS guide reports noble registers among RGIA fond 1343, inventory 51, with family members dispersed through the books; treat that as a finding-aid lead and verify the actual inventory before requesting a file. Its current archival access was not checked here. A surname match in a book does not establish descent from the registered family. [S52], [S53]

## 5. Search where the family actually lived

- Search the metrical books of the works, village and town parishes where the person lived or traded, not only the registering town. The threads document "[town] мещанин", "временно проживающий" and "[town] купецкий сын" entries for births, marriages, deaths and godparents in Nevyansk, Shuralinsky, Rezh, Polevskoy and other works parishes (GASO f. 6, various inventories). [S3], [S6], [S7]
- Check the parish name and inventory before declaring a gap. The reported 1905 start for Yekaterinburg’s Holy Trinity Edinoverie books misses GASO f. 6, op. 9, d. 860: the inventory lists Holy Trinity parish registers for 1891–1895 [S3], [S61]. Check the volume for the event and year you need.
- An age or date mismatch between a candidate and the expected person lowers the candidate's rank but never excludes the candidate.

## 6. Treat catalogue annotations and absences as leads

- Before you rely on a case title taken from a catalogue annotation, check its years and, where relevant, its geography. [S2]
- A merchant’s absence from his town’s 1850 revision cannot establish later enrolment or a trading address elsewhere [S7]. Check the other estate’s list and the next revision (§4), then look for an admission or transfer between societies. Record the missing entry until a dated record explains it.

- **Search the state-peasant lists of the same revision for однодворцы or пахотные солдаты.** A Tula household appears among the state peasants in 1850, before the 1866 reclassification, although the revisions of 1782–1834 list it among the однодворцы [S38], [S39]. For пахотные солдаты, search under both казённые and государственные крестьяне [S40], [S41]. A second Tula household is labelled пахотные солдаты in 1816, крестьяне казённого ведомства in 1834 and государственные in 1850 [S42]. Match family members across revisions and preserve the wording at each date.

## Output: status timeline and series worklist

For each person, give:

- **Status timeline:** one row per observation, with status as written, registering society, residence wording, occupation, origin estate, and acquisition date or bracket. Each row carries its locator.
- **Chronology check:** for each claimed status, the result (consistent, anachronistic, or untranslatable back to a real estate) and the reason.
- **Series worklist chosen by date:** revision-list sub-series, admission and petition files, 1874 family lists and call-up lists, grant files, merchant series, and residence-parish metrical books. Each row gives the fund and the coverage as a participant reported it, and is marked inspected or uninspected.
- **Gaps:** open brackets, missing books and unchecked inventories, kept as gaps.
