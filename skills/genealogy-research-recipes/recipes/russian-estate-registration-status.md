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
router: {"section": "Records by country and region", "group": "Russian Empire and Soviet Union", "order": 50}
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
  - from the late 19th century peasants in general were called сельские обыватели, and many town residents held peasant status (about a third in Yekaterinburg, by one participant's estimate) [S4].
  A works-settlement address does not show that the family were works people. Follow a family into the works (заводские) records only when a record shows it among the former мастеровые; otherwise search the records of its documented registering community and estate category.
- **"Почетный гражданин" is an estate, like мещанин or дворянин, not an honour from a particular town.** The estate existed from 1832 to 1917, and it was either personal (личный) or hereditary (потомственный). Always record which one. [S13], [S1]
- **Formulary lists give birthplace and estate as separate facts.** For example, a man born in the city of Perm could be registered "из крестьян [X] волости [Y] уезда". Keep both fields, and search the registering community as well as the birthplace. [S12]

- **«Временнообязанный» and «крестьянин-собственник» are land statuses of one household, not a buyout date.** A temporarily obligated peasant was free but, not having redeemed his land, still owed the landowner obrok or barshchina for it [S23]; entries often name that owner beside the label. [S21] On redemption the state paid the landowner, and the peasants became peasant-proprietors who repaid the state over 49½ years, until the payments ended on 1 January 1907. [S24] So «крестьянин-собственник» in an entry of 1868 or 1872 shows that the household's land had gone over to redemption, not that it was paid off, as the bloggers citing such entries assume. [S21], [S22] Redemption was compulsory from 1 January 1883, and by the end of the century the category survived only in Transcaucasia. [S23]
- **A peasant who shares the village nobles' surname: test an odnodvorets origin before illegitimacy or a landowner-given surname.** Odnodvortsy descended from frontier service men, boyar scions among them [S28]; in the 19th century they came to be treated as state peasants, and they passed fully into that estate in 1866. [S29] A Tula researcher found the 1795 revision-tale formula «положенные из дворян в однодворческий подушный оклад» in such a village and has never met a landowner-given surname in Tula guberniya. [S25] Another Tula family, odnodvortsy in the revisions of 1782–1834, is among the state peasants from the 1850 revision, so read the state-peasant lists before you call such a family absent. [S26] Treat a common ancestor with the nobles as a hypothesis until a revision tale or a nobility file joins the lines, and the odnodvortsy habit of marrying daughters of odnodvortsy, clergy and nobles as a lead for a wife's origin. [S26], [S27]
- **Read пахотные солдаты, крестьяне казённого ведомства and государственные крестьяне as one household.** Казённые and государственные крестьяне are one estate [S32]; ploughing soldiers became state peasants [S31], as ямщики did, in the first third of the 19th century. [S33] One Tula family carries the three labels in the revisions of 1816, 1834 and 1850. [S30] Do not split such a household, read «солдаты» as army service, or carry one family's change years to another.
- **A passport places its holder away from the society that issued it.** Under the 1894 regulation none was needed for an absence of up to six months within the uezd or up to 50 versts beyond it; мещане and сельские обыватели received passports of three months to a year, or five-year booklets, from the мещанская управа or through the volost elder. [S43] Copy a metrical entry's passport note in full, with its issuer, date and number, as Moscow entries of 1907 and 1908 give it [S42], and search the issuing town's or volost's society next. Passports of 1901 name a town elder or a volost board as issuer. [S41]

## 2. Test each status against its chronology

Test every status before you search for it:

- **3rd guild.** The 3rd merchant guild was abolished in 1863. After that, a former 3rd-guild merchant either declared capital in the 2nd guild or became a мещанин, even if he went on trading. [S2], [S8] A "3rd-guild merchant" born in the 1880s is an anachronism. Look for 2nd-guild or мещанин registration instead, or move the claim to a parent's or grandparent's generation. [S2] People also moved between estates before 1863, so a record can show someone as мещанин who was earlier a 3rd-guild merchant. [S7]
- **"Почетный житель" or a translated "Honorary Citizen" with a place.** "Почетный житель" of a town or shtetl was not a status. For a translated "Honorary Citizen", record the status and the locality in separate fields, get the original-language wording, and only then map it to потомственный or личный почетный гражданин and test both possibilities (§4). [S1]
- **First guild.** When a 1st-guild merchant disappears from a city, look for a move or a transfer between merchant societies before you assume a death. A participant cited a 1914 transfer of a Jewish merchant from one town's 1st-guild society to another's. [S2] Do not assume that 1st-guild status gave an unconditional right to live anywhere. For Jewish merchants, the law of 16 March 1859 allowed registration in guilds outside the Pale only after a period of years in the 1st guild inside the Pale (Jewish Encyclopedia, "Pale of Settlement"). The right to stay outside became permanent only after 10 years of continuous 1st-guild membership. A merchant who left the guild before then had to return to the Pale. Moscow was the exception: a Jew could join the Moscow merchant guild only with the permission of the minister of finance and the governor-general of Moscow, and the right to live in Moscow ended on leaving the guild, whatever the years (same article). So check the guild years and the city as well as the guild.

## 3. Date when the person acquired the status

A status in one record does not show the status at birth, the status of siblings, or the status of the father.

- **Service (formulary) records.** These record grants. The wording in participants' extracts includes "пожалован в звание личного почетного гражданина", "утвержден в звании потомственного почетного гражданина" and "за выслугу 10 лет в гражданской службе утвержден в звании личного почетного гражданина". They give the estate of origin separately, as "из мещан", "из солдатских детей", "из заводских детей" or "сын личного почетного гражданина". One extracted record runs: from soldiers' children; discharged from the military department in 1859; enrolled in the Perm мещане later that year; made a personal honorary citizen in 1871. Record each of these as its own dated status. [S9]
- **Revision-list remarks.** These date entry into an estate and transfers out of it. Examples from the threads:
  - "в 1852 г. причислен из крепостных людей [province]" (1858 revision, GAPK f. 111, op. 1, d. 1890, as cited);
  - "в 1849 г. записался в мещанское звание … из господских людей" (cited from the 1850 revision, ГАШ f. И-605, op. 1, d. 8);
  - "выбыл в Екатеринбургское купечество в 1831-м году" and "перешел из Екатеринбургского купечества в 1843 году";
  - a father and son "выбыли в Екатеринбургские мещане в 1818-м году".
  Record the year exactly as the remark gives it. [S7], [S11]
- **Witness and godparent entries.** These bracket a transfer between societies. In one case a man appears in the 1858 revision list and marries in 1861 in his earlier settlement. He is then a witness in 1892 as an Alapaevsk мещанин, and his son appears the same way in 1901. Search the parishes where the family lived, and use the latest entry under the old registration and the earliest under the new one as the bracket. [S6] A godparent or witness role shows the event place, not residence: a merchant's son registered in one town can appear as a godparent in another city's parish without any residence wording. Fill the residence field only from residence wording or separate residence evidence. [S7]
- **Later administrative lists.** These can supply the registration when nothing else does. A participant used a 1908 criminal-record list (Ведомость справок о судимости) giving "мещанин г. Белебей" to establish the registration and direct the next searches. [S2]

  To reach the printed Ведомость справок о судимости when the year is unknown, search the Russian State Library catalogue (search.rsl.ru) for the annual alphabetical index of names (Алфавитный указатель имен и фамилий лиц, помещенных в Ведомости справок о судимости) for the right part (часть) and year. The catalogue lists such an index by part, for example 1886, ч. 2 (general courts), with a free online scan. [S14] Read the surname's entry number in the scan, then open that year's issues of the same part, which are split into numbered books (кн.). [S15] The index for a year can be printed the next year (the 1886 index appeared in 1887), so do not cite the publication year as the conviction year. [S14] The entry number is not a page or book number. An empty catalogue or OCR search is not a negative for the scan.

  Familio's surname index to the Ведомости, 1870–1927, describes an entry as the convicted person's name, age, estate and place, the conviction and the sentence, sometimes with a trade, and reads «М» after an article as the statute on penalties imposed by justices of the peace and «У» as the Уложение. [S40] A Tula researcher adds the court, the dates of the sentence and of its execution, and any earlier conviction. [S39] Search the index before you page the volumes, and read the place by §1 as the society of registration; a hit in the right town can still be a namesake, as his search for a man convicted in 1900–1905 showed. [S39]

- **A transfer into a town estate is decided in the treasury chamber's journals.** A family's 1850 revision entry cites a Moscow Treasury Chamber decree of 30 March 1840 moving the family, ямщики of a volost, from the state peasants into a town's 3rd-guild merchants. Most such decrees are lost, but the decision survives in the chamber's journal of meetings, TsGA Moscow f. 51, op. 1, d. 373, where the Moscow Chamber of State Properties asks for the enrolment and the treasury chamber orders the town duma and the uezd treasury to carry it out. [S34] F. 51 is the Moscow Treasury Chamber, 1775–1918. [S35] Town duma fonds hold the petitions and the chamber's decrees, as an Orenburg duma file on enrolment into the мещане, 1851–1867 (OGAOO f. 368, op. 1, d. 535), shows. [S36] For a state peasant, ямщики included, search the treasury and state-property chambers, not a landowner's papers.
- **A merchant list can date the enrolment, even in an «Р» fond.** Tula's annual merchant family lists of 1890–1916 give the date each head joined the merchants; in one case that date led to the father's petition, which named his former estate and village. The lists are in GATO f. Р-1905, op. 5, a collection formed in the 1930s–40s from files of the Tula treasury chamber, the town administration and other fonds. [S37], [S38] An «Р» prefix marks a Soviet-period fond [S37]; read such a fond's historical note before you skip it for pre-1917 lists.
- **A Part 2 entry in a noble genealogy book is nobility acquired by rank.** Part 2 held the families of military nobility. [S46] Military service gave hereditary nobility with the first ober-officer rank, passing only to children born after it; from 11 June 1845 it needed a staff-officer rank (8th class) or the 5th civil class, and from 9 December 1856 the rank of colonel or the 4th civil class. [S47] A law of 5 March 1874 extended nobility acquired by rank or order to children born before it. [S55] A serf taken as a recruit in 1815 reached an ober-officer rank and was entered in Part 2 of the Vladimir guberniya book in 1838. [S44] Date the rank from the service record, find the birth estate there or in the parish books, and record each child's birth date against the rank's date, since before the 1874 law that decided whether the child shared the nobility.

If the bracket is open, record it as open. Do not fill the gap by assuming the status was inherited.

## 4. Choose the record series by the acquisition date

The 10th revision (1857–1859) was the last; later revision-list files also survive. [S16] Town lists of that revision are usually dated 1858 and are called the 1858 revision below. Compare the acquisition date or bracket with that revision before you send anyone to a revision list. [S10] For an Orenburg Cossack household after 1834, check the holding archive's inventory for which revisions exist; see [revision-list household chaining, step 10](russian-revision-list-household-chaining.md#10-for-an-orenburg-cossack-household-confirm-which-later-revisions-exist).

**Honorary citizens, whatever the acquisition date.** Go first to the honorary-citizen grant files and formulary lists under the post-1858 branch below; RGIA f. 1343, op. 39 starts in 1830. Do not let the revision cutoff decide their series. [S1], [S9]

**Status held by the 1858 revision.**

- Use the registering society's revision lists. A participant reported that the Irbit 1858 мещане list groups registered families wherever they lived but does not state residence, so expect household composition and no address from such a list. [S8] Copy any residence remark a revision entry does give, such as a daughter who "имеет жительство у отца своего" (1816 Yekaterinburg revision, GASO f. 8, op. 1, d. 453, as cited). [S11]
- Check every sub-series. A participant listed how Yekaterinburg 1858 is split in the GASO catalogue: f. 8, op. 1, d. 1776 (цеховые мещане), d. 1777 (мещане), d. 1778 and 1778а (частные сказки), and d. 1779 (newly admitted мещане). [S3]
- Merchants and мещане of one town and one revision are often in separate дела. Participants cite GAPK f. 111, op. 1, d. 2461 (1834 мещане) and d. 2463 (1834 купцы), while d. 2471 (1850) covers купцы, мещане and цеховые together. If a family is missing from one list, check its remarks and then the other estate's list. [S11]
- A participant cited digitised Yekaterinburg revision lists for купцы, мещане and цеховые on "Поколения Пермского края" (GAPK f. 111, op. 1, d. 2413, 2415, 2416). [S3]
- Read the confession note at the foot of the page for each person. A household can mix Orthodox and Old Believer members. [S3]

**Status acquired after the 1858 revision.**

Revision lists will not contain the person under the new status. [S10] Use instead:

- **Admission (причисление) and transfer files.** Participants cited GASO f. 8, op. 1, d. 1922 and 1922а (1864, works people discharged into the town мещанство) and d. 1935а (1867, an enrolment file for the мещанское общество). [S3] For a man shown as a serf works employee in 1858 and a Kungur мещанин by 1867, participants pointed to the Kungur city archive, fund 585, which they described as holding lists, a revision list and petitions after 1864. [S10]
- **1874 conscription family lists and later call-up lists in the city administration (городская управа) fund.** These substitute for revision lists at household level. A participant cited GASO f. 62, op. 1, d. 27а (Yekaterinburg мещане family list, 1874) and d. 28 (call-up lists 1878–79). [S3]
- **Honorary-citizen grant files.** RGIA f. 1343 (Department of Heraldry), op. 39, covers hereditary honorary citizenship for 1830–1890. A participant added op. 40 for hereditary and op. 41 and 47 for personal honorary citizens. He judged the personal-citizen inventories to be outside the date range in his case and said the inventories are online at RGIA. Check each inventory's date range, and also look for a grant file in the provincial archive. [S1] Provincial formulary lists record the grant itself, for example GAPK f. 36 and f. 111, op. 1, d. 1030–1034 as cited in participants' extracts. [S9], [S12]
- **For merchants of any date**, a participant listed these series:
  - guild-certificate cases and registers of trade certificates;
  - family lists of the мещанское and купеческое общества;
  - declarations of people who wished to join a merchant society;
  - lists of property owners;
  - alphabetical lists of a province's merchants.
  Find more through the footnotes of scholarly work on local merchants. [S2] A participant cited a personal file in RGIA f. 573 (op. 13) for a transfer between two towns' 1st-guild societies in the 1910s. [S2]

- **Moscow мещане: find the sloboda, then the family number.** Catalogue data of the Central State Archive of Moscow (TsGA Moscow), as listed by NashiPredki, give f. 5 as the Moscow мещанская управа with one inventory [S17 @2026-11-08] and title the 1782 revision books of Moscow merchants and мещане («купцов и мещан») by sloboda, for example Taganskaya (f. 51, op. 18) [S18 @2026-11-08]. A genealogist's 2024 account says that metrical books, revision lists and confession lists name a family's sloboda, that f. 5, op. 1 holds alphabetical lists of мещане by sloboda and sloboda books in which each family has its own number, and that the sloboda's alphabetical list should be ordered first when the number is unknown [S19 @2026-11-08]. Record the sloboda in the registering-society field (§1), not as an address. Citations from before 2013 may name the Central Historical Archive of Moscow (TsIAM), which Russian Wikipedia says became part of TsGA Moscow in April 2013 [S20 @2026-11-08]; check file numbers in TsGA Moscow's own inventory before citing them.

- **Moscow sloboda books: use the revision-number and admission columns.** A sloboda book gives the family's numbers in the 9th (1850) and 10th (1858) revisions, when and from which estate a man entered the мещане, «Какое имеет звание и чем занимается», «Кто был под судом и чем дело кончено» and remarks; in one family's entry the distinguishing-marks column recorded passports issued and the addresses at the time. [S19] Go from the revision numbers straight to the 1850 and 1858 revisions, date an admission after 1858 from the entry column (§3), and look for addresses in the occupation, marks and remarks columns. [S19], [S50]
- **A foreign subject: find his petition for Russian subjecthood.** The Heraldry handled admission to Russian subjecthood from 1832. [S54] A study of the First World War petitions of enemy subjects draws on Ministry of Internal Affairs and Council of Ministers papers in RGIA, GARF and the Central State Historical Archive of St Petersburg [S53], and other ministries held such cases too, for example a 1914 Department of Public Education file, RGIA f. 733, op. 201, d. 499. [S52] One 1914 petition gave an Austrian-subject estate manager's education, birth date and birthplace, godfather, wife and daughters; it names Jersey as his birthplace, while his parish entries of 1885 and 1886 call him a native of an Austrian town. [S51] Record the petition's birthplace and a parish entry's «родом из» as separate testimony.
- **Old noble families: prove each generation from the assembly's files.** A guberniya's noble genealogy book was compiled by the deputies' assembly from the evidence submitted for each family. [S46] A Tula researcher worked from such genealogy files together with Novikov's «Родословная книга князей и дворян российских и выезжих» (1787) and Dolgorukov's «Российская родословная книга» (1854–1857). [S45], [S48], [S49] Novikov printed the Бархатная книга from copies, not from the original [S48], so take the printed books as leads to the files, not as proof.

**Limits on substitute lists.** A participant expected community tax-allocation (раскладка) files to list at most heads of household, not full families. Do not promise family detail from them. [S1]

**Read a substitute list's coverage and columns before you read an absence or an age.** A family list made for the call-up can list males only, and a tax list names only the people liable, so a wife or daughter missing from either says nothing about her death or about who the mother was. Take each age's reference date and each figure's meaning from the column headings, not from the year on the file's label; if the headings leave an age's reference date open, record no birth year from it. The full checks are in [volost and town administration records, step 6](russian-volost-town-administration-records.md#6-record-inspected-entries-as-household-observations).

## 5. Search where the family actually lived

- Search the metrical books of the works, village and town parishes where the person lived or traded, not only the registering town. The threads document "[town] мещанин", "временно проживающий" and "[town] купецкий сын" entries for births, marriages, deaths and godparents in Nevyansk, Shuralinsky, Rezh, Polevskoy and other works parishes (GASO f. 6, various inventories). [S3], [S6], [S7]
- If the registering town's parish books seem lost, check the catalogue before you accept the gap. In one thread, a participant pointed to surviving books for 1891–1895 (GASO f. 6, op. 9, d. 860, the Holy Trinity Edinoverie church in Yekaterinburg), against the belief that the church's books began only in 1905. [S3]
- An age or date mismatch between a candidate and the expected person lowers the candidate's rank but never excludes the candidate.

## 6. Treat catalogue annotations and absences as leads

- Before you rely on a case title taken from a catalogue annotation, check its years and, where relevant, its geography. [S2]
- Absence from one society's revision list does not disprove the status or the identification. In one case a merchant was missing from his town's 1850 revision. A participant took this to mean he probably enrolled later and traded elsewhere. [S7] Check the later revision, the other estate's list (§4), the admission files, and the possibility of a transfer between societies. Record an unresolved absence as a gap.

## Output: status timeline and series worklist

For each person, give:

- **Status timeline:** one row per observation, with status as written, registering society, residence wording, occupation, origin estate, and acquisition date or bracket. Each row carries its locator.
- **Chronology check:** for each claimed status, the result (consistent, anachronistic, or untranslatable back to a real estate) and the reason.
- **Series worklist chosen by date:** revision-list sub-series, admission and petition files, 1874 family lists and call-up lists, grant files, merchant series, and residence-parish metrical books. Each row gives the fund and the coverage as a participant reported it, and is marked inspected or uninspected.
- **Gaps:** open brackets, missing books and unchecked inventories, kept as gaps.
