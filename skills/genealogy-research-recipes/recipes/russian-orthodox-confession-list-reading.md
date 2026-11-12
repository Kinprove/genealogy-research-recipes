---
id: "russian-orthodox-confession-list-reading"
title: "Read Russian Orthodox confession lists household by household across years"
summary: "Read Russian Orthodox confession lists by household across years, test ages and names, and check them against revision lists and metrical books."
kind: "records"
scope: {"platforms": [], "tasks": ["исповедная ведомость, исповедная роспись or духовная роспись of the Russian Empire", "Compare исповедные ведомости across years"]}
privacy: "none"
gates: []
guardrails: [{"id": "RUSSIAN-ORTHODOX-CONFESSION-LIST-READING-01", "text": "The common errors are to read one year as a census, to turn an age into a birth year, to treat a household number as an identifier, and to treat a list entry as proof of a marriage, a parent or a death."}]
handoff: ["evidence-proof-judgment", "old-believer-sectarian-record-recovery", "orthodox-clergy-record-recovery", "russian-household-list-transcription-audit", "russian-orthodox-metrical-book-recovery", "russian-revision-list-household-chaining"]
checked: "2026-11-08"
checked_basis: "opened 2026-11-08"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "pointer", "group": "Russian Empire and Soviet records", "order": 1094}
---

# Read Russian Orthodox confession lists household by household across years

Use this recipe when you have a Russian Orthodox confession list of the 18th to early 20th century, or are looking for one, and need a household, an age or a family link from it.

The list has several names: исповедная ведомость, исповедная роспись, исповедальная ведомость, духовная роспись, великопостная роспись. [S7] Researchers often shorten it to исповедка or ИВ. [S5], [S7]

The common errors are to read one year as a census, to turn an age into a birth year, to treat a household number as an identifier, and to treat a list entry as proof of a marriage, a parent or a death. This recipe gives the checks against each error.

Other recipes cover the overlapping steps:

- **Metrical books.** For the parish and consistory copies, and for formulae and margin notes, use [Russian Orthodox metrical-book recovery](russian-orthodox-metrical-book-recovery.md).
- **Revision lists.** For chaining a household across revisions and copies, use [revision-list household chaining](russian-revision-list-household-chaining.md).
- **Clergy.** For a cleric's dated career, use [Orthodox clergy record recovery](orthodox-clergy-record-recovery.md).
- **Old Believers.** For raskol series and non-confessant registers, use [Old Believer and sectarian record recovery](old-believer-sectarian-record-recovery.md).
- **Machine-read search.** For Yandex full-text search of confession lists, use [metrical-book recovery, step 10](russian-orthodox-metrical-book-recovery.md#10-use-machine-read-full-text-search-for-leads-never-for-a-negative).
- **The final ruling.** For same-name separation and the proof argument, use [evidence/proof judgment](evidence-proof-judgment.md).
- **Auditing a transcription.** To check someone's transcription of these lists against the images, use [the household-list transcription audit](russian-household-list-transcription-audit.md).

## Contents

- 1\. Identify the list and the year it describes
- 2\. Read the layout before the names
- 3\. Read the attendance columns as an administrative mark
- 4\. Compare the household across several lists
- 5\. Check the household against revision lists and metrical books
- 6\. Find the lists
- 7\. What a confession list does not prove
- Output

## 1. Identify the list and the year it describes

- **Before 1737, expect a simpler list.** Decrees of 1716 and 1718 required lists of those who confessed, those who did not and schismatics. [S2] A Synod order of 28 February 1722 required books of parishioners of both sexes arranged by house, with space left under each house for arrivals and departures, and the Senate and Synod reissued it jointly on 16 July 1722. [S1], [S2], [S6], [S40], [S41] A separate Synod decree of 7 March 1722 told dioceses to report those who had not confessed and the schismatics, and to send the fines to the Synod; one guide dates the lists from this decree. [S8], [S41]
- **Early lists can leave out children.** A 1725 Vologda list says communion was taken "кроме малолетних, которые до десяти лет". [S3] Do not read a child's absence from such a list as a sign that the child did not exist.
- **From 1737, expect household lists with ages.** The decree of 16 April 1737 ordered lists of all ranks and both sexes, "от престарелых до сущаго младенца", arranged "по чинам и домам", with each person's age. [S1]
- **The form still changed after 1737.** Metrical tables and the priest's covering report were added within a few years. "Разночинцы" left the lists in 1841 and "дворовые" after 1861. [S2] The Synod approved a new form on 15 October 1846. [S1] Read the headings of your own list.
- **The series ends around 1917–1918.** Some priests went on keeping lists into the 1920s. [S6], [S13]
- **Record the list's year and its filing date separately.** Confession was expected in Lent, or in the Peter or Dormition fast for those who missed Lent. [S2] Lists can be filed much later than that. One list for 1822 is marked as filed on 10 January 1823. [S31] A list for 1826 is marked as filed on 10 September 1826. [S20] Compute ages from the list's own year and keep the filing date as a separate note.

## 2. Read the layout before the names

The usual columns are below. Column headings vary, so copy the headings of your own list. [S5], [S8], [S12]

| Column | Copy | Why it matters |
| --- | --- | --- |
| Number of the house or household (домов или дворов) | The number as written | It runs through the whole list, so it locates an entry but does not identify a family [S8], [S20] |
| Number of the person, male and female | Both numbers | Men and women are counted separately [S2], [S8], [S15] |
| Names | Name, patronymic, any surname, relationship and status, exactly as written | Relationships are usually stated to the head of the household [S8] |
| Age, male and female | The figure as written | Separate columns for each sex [S5], [S9] |
| "Кто были у исповеди и святаго причастия" | The mark as written | See step 3 [S5], [S12] |
| "Кто ж исповедались токмо, а не причастились и за каким винословием" | The mark and the reason | See step 3 [S5], [S12] |
| "Которые у исповеди не были" | The mark and the reason | See step 3 [S6], [S12] |

- **Estates come in a set order.** The usual order is clergy and their households, military, civil officials, merchants and townspeople, household serfs, then peasants. [S5], [S6] The clergy come first, so a cleric's family is on the first page of the parish. [S7]
- **That order was often not kept.** In the Zamoskvorechye lists of Moscow, it was followed in 7 of 28 parishes in 1741 and in 18 of 37 in 1755. [S2] Read the whole parish before you report a family as missing from its estate section.
- **Peasants are grouped by village and, before 1861, by owner.** The arrangement could vary: a village could be split among its owners, or landlords' villages could come before state villages. [S8] In one 1789 list, the section for a landlord's household serfs is headed with the landlord's name. [S15]
- **Soldiers' families sit with the military.** Retired soldiers, their wives and children, and the wives and children of men taken as recruits, appear under "Военные и их домашние". [S6] Look there before you report a recruit's family as gone.
- **Inside a household,** the head comes first, then his wife, their children, their children's spouses and children, and then more distant kin. [S7], [S10] The head could be a widowed mother, and a relationship could be stated in a chain rather than to the head. [S8]
- **One двор need not be one family.** Several families not closely related could share a двор, which could hold 20 people or more. [S8] Owners' servants, lodgers, hired workers, soldiers' wives and people living "из милости" could be listed there too. [S2]
- **Infants may be absent.** The 1737 decree reached infants [S1], but guides report that children under one were usually left out [S6], [S11], [S13], and one says the threshold in practice was about six months [S17]. Treat the absence of a child under one or so as no evidence at all.
- **Non-Orthodox people are outside the count.** Fedorets and Kopay describe the lists as covering the Orthodox only. [S2], [S10] One guide says non-Orthodox family members were entered without a number. [S6]
- **Read to the end of the parish.** A summary table of houses and souls by estate closes the list. [S2], [S10] A list of persistent non-attenders or schismatics can follow it. [S8], [S10] Metrical entries can be bound into the same delo: an Urals reference article calls this general practice in the late 18th century, and one participant found births, marriages and deaths inside an 1800 confession list. [S24], [S25]

## 3. Read the attendance columns as an administrative mark

- **Copy the reason as written.** Common reasons include:
  - "по отлучке" or "за отлучкою": away, for example on trade or military service [S3], [S5]
  - "по нерадению", "за нерачением", "по лености": neglect [S3], [S5], [S2]
  - "за малолетством" or "по малолетству": too young [S3], [S10]
  - "по совету духовника": on the confessor's advice [S2], [S3]
  - "за пьянством" [S2]
  - "по расколу" or "за расколом": schism [S5], [S10]
- **A column of "был" can be routine.** One guide reports that "был" was often written in a sweep down the page, so the exceptions carry the information. [S10] Some priests listed every household and marked no attendance at all. [S2] Freeze argues that a priest had to compile the list after the rites, from memory, and that the non-compliant had reason to avoid being recorded. [S4]
- **"Отлучка" needs a follow-up.** A person away at Lent was to confess where he was and bring a certificate back to his own priest. [S2], [S6] Kopay warns that absence could also cover a schismatic. [S10] Record it as "absent, reason given by the priest".
- **Non-confession is not Old Belief.** People who missed confession for three years running were to be written down as schismatics under the 1737 rules. [S2] So a "раскол" label is an administrative classification with a date, and a plain "не был" is not even that. Use [Old Believer and sectarian record recovery](old-believer-sectarian-record-recovery.md) before you call a family Old Believer.
- **Look for separate lists of non-confessants.** A statement drawn from confession lists about people absent in 1765–1767 (GASO f.24, op.1, d.2293) gave one man's patronymic and age, and a participant used it to link him to a family. [S29]

## 4. Compare the household across several lists

Set up one table per household, with one row per person and one column per list. Then work in this order.

1. **Start from the latest list you can reach, then step back.** Two guides advise checking earlier lists at intervals of 5–10 years, then refining the facts in metrical books. [S5], [S6]
2. **Fill in the consecutive years around each change.** The two lists on either side of a change bracket the change in the record, not the event itself. A child may have been too young to list, and a new name may be the same person.
3. **Find the family by its people.** Most peasants have no surname in these lists, so look for the father with a son of the right name and age. [S6], [S10] One guide suggests reading the whole list once, then scanning the age column for the age you expect, because each sex has its own column. [S9]

**Test the ages.**

- Work out what each age should be from the previous list. A list of 1827 and one of 1838 for the same man gave 47 and 58 years, exactly 11 apart. [S32] Do not assume every series will be so clean.
- A participant comparing 18th-century lists found ages "очень условно": often the same age in different years, and sometimes a lower age in a later list. [S21]
- A priest could set an age by eye, peasants often did not know their age, and the error grew with age and could run either way. [S7] One guide puts the spread at about ten years. [S10] A Ukrainian genealogy firm says priests could give only approximate ages, to be reconciled with the birth records. [S18]
- Give each age as a range of birth years, one for each list. Keep the whole series. In one worked case, six sources implied births from 1794 to 1808 for one woman, and the 1838 confession list gave 30 years. [S22] A mismatch lowers a candidate's rank and does not exclude the candidate.

**Do not follow the household number.**

- The numbers run through the whole list, so one added or removed household can change every number after it. That is an inference from the numbering. A guide based on Ukrainian lists says that numbers in neighbouring years roughly match but could change sharply. [S9]
- In one Urals series, a participant's extracts give the same man as entry 213 in the list for 1827 and entry 725 in the list for 1838. They do not say which numbered column that is. [S32]
- Use the number to find your place in a neighbouring year. Identify the household by its people.

**Treat agreement between years with care.**

- Lists were often recopied from the previous year, adding the newcomers and removing the dead. [S9], [S19] A later list can therefore repeat an earlier error, so two lists that agree may be one observation.
- Practice varied. One Urals moderator says the lists were written out in advance with whole families and marked during the year. [S25] Freeze says the priest compiled them afterwards from memory. [S4] BYU's guide says the details may rest on the scribe's limited knowledge or on earlier lists. [S12]

**Treat every name as a hypothesis.**

- A guide warns that these lists have more errors in names, patronymics, ages and degrees of kinship than metrical books and revision lists do. [S6]
- A woman can change given name between lists: one participant found "то Анисья, то Анна". [S30]
- Watch for scribes' corrections. A priest in 1789 wrote one daughter's name and then bracketed it in favour of another. [S15] A participant found a name scraped out in a list of 1822 and could still see that it was a different name. [S22] Transcribe the cancelled form as well.
- **Test a one-off name in the series before you create a person.** In a list of 1838, a son of one household appears as Гавриил while a brother named Гавриил heads his own household; the researcher marked the entry as an error for Григорий. [S32] Annotate such a name beside the verbatim entry. Do not correct it. Before you call it an error, search the nearest revision list for a second man of that name in that generation.

**Use the changes between lists.**

- Widowhood was stated for the surviving spouse, which can help when a death entry is missing. [S13], [S14] It dates the death only to the interval since the last list that shows the couple together.
- A different wife's name is a trigger to test three explanations: the same woman under another name, a death and a remarriage, or an error. One worked case placed a first wife's death between the lists of 1812 and 1824, then narrowed it with an 1823 baptism in which the second wife stood as godmother. [S22]
- A daughter can vanish from her parents' household while a wife of the same unusual name appears in another. That is a lead, and only the marriage entry confirms it. [S10]
- If the whole family vanishes, it may have moved. Check the revision list for the place, and if there is none, the lists of the whole uezd. [S6]

## 5. Check the household against revision lists and metrical books

- **Know what each source can add.** Confession lists cover non-taxpaying groups that the revisions do not. [S5] They list women too: the 1722 orders already required books of both sexes [S1], [S6], [S40], [S41], and Vologda books from 1718 name every member of the household, men and women. [S3] Whether a revision lists women depends on the revision: the 1st, 2nd and 6th (1811) recorded men only. [S7] For the others, use [revision-list household chaining](russian-revision-list-household-chaining.md). Revision lists give the household's official registration and the previous revision's age. Metrical books date individual events.
- **Bridge the gap between revisions.** A participant reported reconstructing Southern Trans-Urals male lines from 1850 back to the 1680s as follows: [S22]
  1. Chain the revisions with the 1774–1830 confession lists (in the Orenburg archive).
  2. Use the 1795 revision, which carries the 1782 figures as well, to link to the 1719 lists of the Iset slobodas.
  3. Go to the 1710 census.
  4. Go to the 1680s census, which gives the territory of origin.
- **Separate residence from registration.** An 1834 revision tale notes a family "проживает с давних лет" at its new place, and a confession list shows it there by 1790, at least 44 years earlier. [S23] Date residence from the lists and registration from the revisions, and report them as two facts.
- **Recover a bride from her home village.** A participant knew a great-grandmother's name, patronymic, birth date and home village, and read that village's lists family by family until one Ivan had a daughter of that name and age. A copy of her birth certificate later confirmed the match. [S28] Without that kind of confirmation, the result stays a hypothesis.
- **Test absence across every source.** A participant noted that one or two omissions could be a scribe's error or a child too young to be listed, but checked a family across confession lists of 1808, 1815 and 1822, and revision lists of 1811 and 1816, before concluding that it had no such daughter. [S22] The 1811 revision recorded men only [S7], so that return says nothing about a daughter. Count only sources that record women.
- **Be careful with Old Believer households.** One review compared a Rzhev list of 1850 with the tenth revision. It found the lists fairly reliable for the Orthodox and full of inaccuracies for Old Believer families, and it prefers revision lists for them. [S16]

## 6. Find the lists

- **Expect two copies.** One stayed in the church and the other went to the consistory, where the notebooks were bound into volumes by uezd or town. [S5 @2026-11-08], [S19 @2026-11-08] In a bound volume the churches tend to come in the same order each year. [S5 @2026-11-08]
- **Look in these fonds.** Consistories, spiritual boards (духовные правления), diocesan administrations and individual churches. [S13 @2026-11-08] Check the archive for the modern region and the archive for the old guberniya. [S6 @2026-11-08] Lists and revision tales for one place can be in different archives. [S15 @2026-11-08]
- **Lists and metrical books are usually separate.** A participant reported that they are mostly kept apart but sometimes together. [S23 @2026-11-08]
- **Urals holdings.** An Urals reference article says almost all surviving lists are in church fonds, with a few bound runs for whole uezds in GASO (f. 6, op. 2 and f. 24, op. 23, dd. 6987, 7078–7082, 7168), of up to 3,000 leaves each. [S24 @2026-11-08] Participants' extracts confirm d. 7081 (1812) and d. 7078 (1807). [S33 @2026-11-08], [S34 @2026-11-08] Other runs are GASO f. 6, op. 3, dd. 638 and 638а (1800) [S35 @2026-11-08] and a combined metrical and confession volume for 1849–1851 in the Artemovsky municipal archive (f. 13, op. 1, d. 1) [S36 @2026-11-08].
- **Moscow.** Fedorets cites the Moscow lists as TsIAM f. 203, op. 747, from 1737 to 1915, bound by sorok. [S2 @2026-11-08] Kopay places f. 203 in TsGA Moscow and also names the fonds of district spiritual boards and of individual sorok. [S10 @2026-11-08] Glavarchiv Moscow added Orthodox lists of Moscow and Moscow guberniya, from the second quarter of the 18th century to the 1860s, to its «Моя семья» service in 2021. [S11 @2026-11-08]
- **Other places.** Tver lists of 1728–1913 are cited from a FamilySearch collection. [S39 @2026-11-08] Archaeograph reports that many Ukrainian lists are online at FamilySearch and that their handwriting needs separate study. [S5 @2026-11-08]
- **Late lists are rare.** A bulletin of 25 May 1927 ordered lists from 1865 onwards to be destroyed as having no historical value, and in Moscow guberniya nearly all of them were. [S20 @2026-11-08] Guides report that lists after the 1860s are very rare. [S5 @2026-11-08], [S6 @2026-11-08]
- **Do not trust the inventory title alone.** One list of 1789 is recorded in the inventory under 1780, and the same delo contains a metrical book. [S27 @2026-11-08] Delo numbers in GASO f. 6, op. 3 were reassigned, so an inventory line can describe another file. [S37 @2026-11-08] An archive's negative reply for one church was overtaken when a participant found its 1776 list in the inventory under a later entry. [S38 @2026-11-08] Order or view the file before you report a gap.

## 7. What a confession list does not prove

- **A birth date.** It gives a stated age in a year. Report a range and look for the baptism.
- **A marriage.** The church law quoted in 1904 allowed the lists to be consulted when a marriage was in doubt. It also told deans to see that priests took special care before showing people as spouses when they had not married them and no proof was offered. [S1] A "жена" is the priest's label. Seek the marriage entry.
- **Parentage.** A child listed after a wife need not be hers, and children raised in the household can be listed there. [S8], [S10] Check each child against the baptism and against any earlier wife.
- **One family.** Sharing a двор is not kinship. [S2], [S8]
- **Presence or devotion.** The mark records what the priest wrote. Freeze notes that the figures record observance, not belief. [S4]
- **Absence, death or departure.** The lists record the people present in the parish, so someone away may simply not be listed. [S2] A moderator's advice for a missing man was to look for him in another household as a son-in-law, or in another village, because he might have been skipped or entered elsewhere. [S25] One researcher read every 1800 list of an uezd and could not find people who appear in the metrical books; the reason stayed open. [S26]
- **Old Belief.** See step 3.
- **Independent confirmation.** Successive lists can be copies of one another, and one list's agreement with the next is not a second witness. [S9], [S19] Leave the ruling to [evidence/proof judgment](evidence-proof-judgment.md).

## Output

Return three tables:

1. **Coverage register.** One row per parish-year: archive, fond, opis, delo, leaf span, the list's year, its filing date, and whether the list was read, not read or not accessible. Name the parish sections you read.
2. **Household series.** One table per household, with one row per person and one column per list. Give each entry verbatim with its household number and male or female number, the attendance mark and reason as written, and the implied birth-year range.
3. **Hypothesis register.** Give each identification, each proposed relationship and each change between lists, with the competing explanations and the revision-list and metrical-book tests applied.

Call a family or person absent only for the lists and sections you actually read.
