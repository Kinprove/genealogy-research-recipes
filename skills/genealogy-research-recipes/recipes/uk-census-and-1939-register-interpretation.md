---
id: "uk-census-and-1939-register-interpretation"
title: "Read England and Wales censuses and the 1939 Register under each year's own rules"
summary: "Read England and Wales censuses from 1841 to 1921 and the 1939 Register under each year's own rules."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "UK-CENSUS-AND-1939-REGISTER-INTERPRETATION-01", "text": "Before reading any value, settle what that year's image is, who wrote the value, what night or day it refers to and what the year covers."}]
handoff: []
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request", "third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Britain and Ireland", "order": 133}
---

# Read England and Wales censuses and the 1939 Register under each year's own rules

Use this recipe when an England and Wales census return from 1841 to 1921, or a 1939 Register entry, is about to be used as evidence of presence, absence, age, place, marital status, family composition or a later event. Before reading any value, settle what that year's image is, who wrote the value, what night or day it refers to and what the year covers. To carry piece and folio locators beyond Ancestry, use [Ancestry record-search recovery](ancestry-record-search-recovery.md). For the general rule that a stated status is a statement and not an event, and for every proof ruling, use [evidence/proof judgment](evidence-proof-judgment.md). For keeping a filing date apart from an event date, use [AI for documentary records](ai-for-documentary-records.md). The U.S. equivalents are in [U.S. census workflows](us-census-practical-workflows.md).

## Contents

- Fix the year's rules before reading a value
- Retrieve the whole 1921 return, not one side
- Treat census night as a headcount of who slept where
- Read marital status, ages and child counts within their limits
- Read sex, occupation, status, health and origin from their columns
- Check birthplaces against the image
- Match an address by its neighbours, not its number
- Read the 1939 Register as a registration list, not a census
- Check what the year covers before reading an absence
- Return the observation record

## Fix the year's rules before reading a value

Open one observation record for each year, with these fields: observation date, image type (copy or schedule), writer of the values, place role, coverage note and access gaps. Fill them in from the rules below.

- **Census nights.** 6 June 1841, 30 March 1851, 7 April 1861, 2 April 1871, 3 April 1881, 5 April 1891, 31 March 1901 and 2 April 1911 [S16]. For 1921, see its own bullet below. Enter the year's census night as the observation date, and calculate ages and residence from it.
- **1841–1901: the enumerator's copy.** The surviving returns up to 1901 are enumeration books that the enumerator copied from the household schedules. Most of those schedules were destroyed [S9]. Treat the books as a derivative source. Lines can be dropped, misread from poor handwriting or entered on the wrong line [S9]. Do not call such an entry the household's own statement.
- **1841 ages.** Ages of people aged 15 and over were rounded down to a multiple of five, so a stated 35 means 35–39. Ages under 15 were to be exact, though some enumerators rounded children's ages too [S6], [S9]. Always carry an 1841 birth year as a range. **Do not extend the rounding to 1851.** One presenter says the 1851 instructions also called for rounding [S8], but that is wrong. From 1851 ages were recorded as age at last birthday, and rounding applied only in 1841.
- **1841 birthplace and household columns.** The birthplace column says only whether the person was born in the county of enumeration (Y, N or NK for not known), or marks S, I or F for Scotland, Ireland or foreign parts [S17]. Read F as foreign parts; where TNA's guide prints P, treat it as the same mark [S16]. It names no parish and no other county [S16], [S17]. An index value such as "1841 birthplace: Lancashire" is derived from that answer, not stated. 1841 also has no relationship-to-head or marital-status column; both start in 1851 [S16]. Do not label a wife or child from their position in the household. Take the birthplace and relationships from 1851 or later returns.
- **1911 ages.** The household's original schedule survives [S9]. A presenter observed ages ending in zero in 1911 [S8]. Record the age as written and compare it with earlier returns or a birth record before treating it as exact. The 1841 rounding instruction does not govern a 1911 entry.
- **1921: the household schedule plus later coding.** The householder usually filled in the form. Sometimes another family member, a neighbour or, rarely, the enumerator wrote it [S8], [S15]. Record the writer as unknown unless the form shows who wrote it. Green-ink annotations, including the occupation and industry codes, were added afterwards for statistical processing, not by the household [S12]. Findmypast's 1921 occupation-codes guide attributes them to the Census Office, while the S12 presenter calls them the enumerator's coding. Either way, keep them separate from the household's entries.
- **1921 census night: 19 June.** The census was planned for Sunday 24 April 1921 and postponed to Sunday 19 June 1921 [S8], [S13]. The schedules had already been printed and were reused rather than reprinted, so they still carry the April date [S12], [S13]. Calculate ages and residence from 19 June. One presenter gives the planned date as 25 April [S12]. That was the Monday when forms were to be collected, not a rival census night. The official reason for the postponement was industrial unrest. Presenters tie it to coal and mining strikes [S12], [S13] and to a transport-linked strike threat [S8]. These describe the same unrest, not competing explanations. Record the printed date exactly as it reads on the form.

## Retrieve the whole 1921 return, not one side

Collect every image attached to the household return [S12]:

- the side where the address box sits, separate from the schedule side;
- the volume cover, which gives the civil parish, urban and registration districts, the parliamentary district and The National Archives (TNA) RG 15 piece reference;
- the maps, including rescans with the paper flaps lifted;
- the enumerator's instructions and boundary notes.

Cite the piece reference from the cover. Several families at one address each have their own schedule [S13], so record the schedule as well as the address.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Before sending a 1921 census search to MyHeritage, answer the privacy gate in `SKILL.md`. Confirm that the person is deceased and send only the name, dates and place needed for the lookup.

If another provider's 1921 index misses a deceased ancestor, try MyHeritage's [1921 England & Wales Census](https://www.myheritage.com/research/collection-20972/1921-england-wales-census) [S61 @2026-11-21], [S62 @2026-11-21]. If you can see the index entry but cannot open the full return, use the match to locate the schedule and its supporting images with another provider.

In 1921, read the orphanhood answer for children under 15 together with the relationship-to-head column. Do not assume the head of household is the parent who died. The child may be a nephew or cousin whose dead parent lived elsewhere [S12].

Read the schedule's other 1921 answers as well. Ages are given in years and months, so counting back from 19 June 1921 narrows a correctly stated age to a birth window of about one month [S16], [S24], [S25]. Each worker gives the name and business of the employer and the address of the place of work; someone out of work names the last employer and adds "out of work" [S16], [S24], [S26]. The schedule also records whether each person was in full-time or part-time education, and every schedule gives the number of rooms [S16], [S26]. The 1911 questions on years of marriage and children born, and the infirmity question, were dropped [S16], [S25], so a 1921 schedule has no child counts for the method below. Instead, married men, widows and widowers gave the number and ages of their living children and stepchildren under 16 [S16].

## Treat census night as a headcount of who slept where

England and Wales censuses recorded everyone present on census night, wherever they were: visitors, guests at a sleepover, hotel guests, tourists, ships in port and institutions. Presenters report that some people were listed twice, at home and where they stayed, and some were missed because each household assumed the other would list them [S8], [S14]. Prisons and asylums often give initials only [S14].

The example from the available excerpt concerns a 1921 household schedule that could list a person who spent census night there or arrived the next morning and had been counted nowhere else [S70], [S71]. Check the home and visiting schedules when both could describe the same person. Compare the piece and schedule references to distinguish two returns from two index hits for one return, then compare the names, ages and birthplaces on the images before recording a possible double enumeration.

The 1921 instructions used "Visitor" even for a relative who was present and usually lived elsewhere [S71]. Record the address as their place of enumeration and search separately for their usual home and their spouse’s return. In one published example from the 1921 returns, a married visitor appears away from her husband [S62].

When a person or household is missing from the expected address:

1. Do not record death, separation or emigration. Record "not found at expected address on [census night]."
2. For 1921, search hotels, lodgings and nearby resorts. The June census fell at the start of the summer holiday season [S7], [S8], [S10], [S13]. Parents could be away while a child remained at the home address. A reported hotel stay a few villages away left a teenage son at home [S12]. Search each family member separately.
3. Search the returns for vessels in port, children's homes and other institutions [S12]. Also search the police-collected returns for people sleeping in barns, sheds or the open air. These are placed at the end of the district's book [S12].
4. Where a person appears twice, link both entries as one possible double entry. Do not create two people.

Search an institution's return differently. A workhouse, prison or similar institution is enumerated as one household, with its master or governor as head and the inmates in adjacent entries [S27]. The head of the institution filled in the form for the inmates [S30], so the inmate did not write the entry and the form does not show who supplied each detail, and some institutions recorded inmates by initials only [S31], [S32]. Search institution returns by initials, with a wide age range and no birthplace, and confirm each candidate on the image.

Search all sections of an institution's return before looking for the rest of the household elsewhere. Poor Law workhouses separated husbands, wives and older children on admission [S28]. In the 1841 St Andrew's Workhouse return, seven-year-old Henry Herbert and his father Richard appear in different places on one page. His mother and newborn brother were outside the workhouse [S29]. Record each person's location separately. Most institution schedules lack a relationship column [S16], so use other records to test kinship.

Add refusal and absence to the reasons for a miss. In 1911 suffragettes boycotted the census: some refused to fill in the schedule or spoiled it with slogans, and others stayed away from home all night. Many were recorded all the same, and one evader was listed twice: at the place where she hid, and by her landlady at home [S32], [S33]. For a woman missing in 1911, look for her on another household's schedule and for a schedule annotated with a protest before recording a gap. A civilian abroad on business or travel that night is outside the returns, and for someone who may have been at sea, search the vessel returns as well as the home schedule (see [what the year covers](#check-what-the-year-covers-before-reading-an-absence)) [S32].

## Read marital status, ages and child counts within their limits

- **Divorce before 1921.** 1921 was the first England and Wales census to record divorce as a marital status. One presenter suspects that divorced people in earlier years called themselves single or widowed [S8]. A pre-1921 "single" or "widowed" therefore does not show that no divorce took place. Pass the status to [evidence/proof judgment](evidence-proof-judgment.md) as a statement.
- **Conflicting ages.** One presenter gives a 1921 age more weight than a 1911 age because ages became more precise by 1921 [S8]. Keep this as an attributed opinion, not a rule.
- **1911 marriage and child counts.** Copy the years of present marriage and the numbers of children born alive, still living and died, all exactly as written. These counts cover the **present marriage only** [S5].
  - **Fewer children than the counts:** set a target number of missing children. Look first in the gaps in birth order between the marriage and 1911 [S5]. Search civil birth indexes by surname and the mother's maiden surname for that window. Confirm each candidate with a baptism. For a child counted as died, also confirm a death registration before 1911 [S3]. Two births registered in the same quarter are only a twin hypothesis [S3].
  - **More children than the counts, or a marriage too recent for the older children:** suspect an earlier marriage and stepchildren. Keep one row per wife, check each wife's birthplace and age across the census years, and do not merge the children [S5].

Use the clue from the available excerpt to read "D" in the marriage or orphanhood column on a 1921 household return for a person aged 15 or over as a report that their marriage was dissolved by divorce [S70], [S71]. Use the reported status to look for a divorce record before census day.

**Reported marriage and widowhood.** Keep a census label such as "wife" or "husband" as the reported relationship to the head. A published 1891 case describes an unmarried couple appearing under one surname, with the man reported as her husband [S66]. Search the marriage index under the recorded surname and any other documented surname, then verify the event against the marriage entry [S67]. For an unexpected "widowed" entry, compare it with the condition in the known marriage entry and use it as a lead to look for an earlier marriage and a spouse’s death [S67], [S68]. Keep any earlier spouse or family tentative.

**Birth windows from conflicting ages.** Calculate a birth window from each stated age and its census date. Use the windows to estimate the age at a documented marriage and reopen a birth search narrowed by an assumed marriage age. If the windows disagree, search both and widen the range if neither yields a match. Keep the birth year unresolved. In one published case two ages for the same person advanced by one year over a decade [S68].

## Read sex, occupation, status, health and origin from their columns

**Sex.** In 1841 the age was written in one of two columns, for males or for females [S34], and the forms kept separate male and female age columns until 1921, the first census to ask for sex on its own [S35]. An entry whose forename is missing or unreadable still has a sex: take it from the column that holds the age [S36].

**Occupation shorthand.** Read abbreviations in the occupation column as census terms, not as initials or misreadings. FS and MS are female and male servant and FWK is framework knitter, all in 1841; Ag lab is agricultural labourer, Ap or App apprentice, J journeyman, and Ind or Independent of independent means [S16], [S37].

**Employment status.** In 1891, take the status from which of three columns, Employer, Employed, or Neither employer nor employed, holds the cross, not from the occupation wording. Married women assisting their husbands in a trade or industry were to be returned as employed, and the columns cover only trades and industries, not domestic service [S38]. A wife or daughter entered as a shop assistant in the family business can therefore carry an employed mark of her own [S39]. In 1901 the choices are Employer, Worker or Own account [S16].

**Work reported in 1921.** Copy the personal occupation as reported for 1921, even when earlier records give a different trade. Keep any "Retired" qualifier attached to the former occupation, and read the employer and workplace in their own columns [S73]. A published example shows a person known for writing returned as a farmer in 1921 [S62].

**Health.** From 1851 a column asks whether each person was blind, or deaf and dumb [S16], [S41]. From 1871 it adds imbecile or idiot and lunatic, in 1911 it asks the age at which the condition began, and in 1921 it is gone [S16]. Record an entry there as the household's statement. Do not read a blank as proof of good health: householders were often reluctant to admit a disability in the family [S40].

**Language and origin.** These censuses never ask for a mother tongue. For someone born in a foreign country they give the country of birth, and only from 1921 a state or province; they ask about language only in Wales from 1891 and also in the Isle of Man from 1901; and from 1911 they record the nationality of anyone born overseas [S16]. For an immigrant family settled in England or Wales, find a sibling, child or other relative who went on to the United States. The 1910 US census added mother tongue to its birthplace columns, and the 1920 census asked the mother tongue of each person born abroad and of each parent born abroad [S42], [S43], [S56]. Use relatives with independently established links to compare answers across countries. For a County Mayo family, a researcher traced ancestors of DNA matches into U.S. census and death records for clues to the family's language. A separate family's U.S. census entries named Polish and Yiddish [S44]. Record each answer against the individual, question and year before extending it to relatives in Britain. Read those returns with [U.S. census workflows](us-census-practical-workflows.md).

## Check birthplaces against the image

If an 1851 or later transcript stops at the county, compare the birthplace with the image before choosing a register. An 1851 entry omitted the parish from the transcript, while the surviving enumeration book named St Giles, Cambridge [S4]. Keep both readings. This does not apply to 1841, when the birthplace column asked whether the person was born in the county and supplied no parish [S16].

From 1851 the birthplace column asks for the parish and county for people born in England or Wales [S16]. Use a child's named parish to search for siblings who were born in the same place. An 1861 return specifying Norwich St Martin at Oak led to further children's baptisms in that parish even before its records were fully indexed [S45]. Browse the images and record the years and parish searched.

On a 1921 household schedule, copy the county and town or parish for a United Kingdom birthplace. For a birthplace outside the United Kingdom, copy the country and any state, province or district given. Use the example from the available excerpt to preserve "At Sea" as the birthplace answer when written [S70], [S73]. Keep the narrower place when choosing the next register to search.

## Match an address by its neighbours, not its number

A different house number in a later census does not show that the family moved. Towns renumbered streets, sometimes every property at once, and renamed them, so match a household by its neighbours, occupations and members rather than by its number [S47]. If several neighbouring families who stayed put all reappear at new numbers in the same order, as numbers 42, 44 and 46 becoming 58, 60 and 62, the street was renumbered [S51]. Electoral registers, produced annually since 1832 with a few exceptions, can date the change [S48], [S51]. Where a town's registers are arranged by street, as Bury's are from 1879, read them year by year [S49]. They list only voters, and the property through which a person qualified to vote is not always the home [S48].

Match a court dwelling by the court as well as the house. A court could be renamed: in Birmingham, the court built in 1802 by a silversmith was first called Willmore's Court, after him, and later Court 14 Inge Street [S46]. A court named for its builder in one record and a street-and-number court in another can be the same place; settle it by the neighbours, as above. A post on the Birmingham back-to-backs prompted this check [S50].

## Read the 1939 Register as a registration list, not a census

Open [The National Archives' 1939 Register research guide](https://www.nationalarchives.gov.uk/help-with-your-research/research-guides/1939-register) to check who was enumerated, which fields were recorded and how the books are arranged. Use the guide's access links to check what each provider lets you view and whether viewing requires payment [S58].

Use **RG 101** to locate digital copies of the enumerators' transcript books. If the person was outside England and Wales on registration day, record a coverage gap for this series [S59].

The Register was used to issue identity cards and ration books [S60], [S69]. Use it to place registered individuals between the missing censuses. On a private-household entry, record the enumerator as the copyist and the householder as the person who completed the underlying schedule [S21], [S64]. Leave the informant for an individual value unknown unless other evidence identifies them.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Before a 1939 Register search sends data to MyHeritage or Findmypast, answer the privacy gate in `SKILL.md` for that provider. Confirm the search subject is deceased and send only the name, birth date or historic address needed for the lookup. Apply the same check to any co-resident whose data you send.

For a direct Register lookup, search the [1939 Register on Findmypast](https://search.findmypast.co.uk/search-world-Records/1939-register) for the entry and its image [S60 @2026-11-22], [S72 @2026-11-22]. The guidance from the available excerpt also points to Findmypast [S70 @2026-11-22].

If the first index misses a deceased person, try the [1939 Register on MyHeritage](https://www.myheritage.com/research/collection-10678/1939-register-of-england-wales) as another finding aid [S64 @2026-11-22], [S65 @2026-11-22]. Use a candidate’s address and any register reference to locate it in the transcript book.

After a full-name miss, retry with the surname and birth date, leaving middle names out. If that misses, search by the known 1939 address or a known co-resident and examine the whole schedule on the image [S21], [S64].

If you find an entry in the FamilySearch index, follow its link to Findmypast for the image [S60 @2026-11-20]. Record any barrier to viewing the page as an access gap.

- **Registration day.** 29 September 1939. Use it as the observation date.
- **What the image is.** It is the master list the enumerator copied from numbered household schedules. Each person's sub-number matches their line on the schedule [S1]. A presenter reports that nobody knows what happened to the schedules and that they were probably destroyed after copying [S1]. Cite the schedule number and sub-number.
- **Place.** The address shows where the person was on registration day, not a permanent home. Seasonal and migrant workers, evacuees and visitors may appear away from home [S11]. The Register gives no birthplace [S3]. Never record the 1939 address as a birthplace.
- **Relationships.** None are recorded. People listed together can include visiting nieces, nephews and others [S11]. Do not file them as a family without other evidence. Institutions use a column of codes for officer, visitor, servant, patient or inmate [S1].
- **Birth dates.** Transcribe the full date from the Register [S1], [S2], [S3]. Search the civil registrations at least a year either side if the stated year gives no match [S23]. Test the month and day as well. Married twins in different households appear a month apart in entries made by different enumerators [S21]. A guide also notes that some men of conscription age reported another birth year [S22]. Use the birth registration's date, place and parents to test the identification [S3].
- **Later annotations.** A crossed-out surname with another written above it, or a date in the margin, was added after 1939. The Register was updated for National Registration until 1952, and by the National Health Service (NHS), including deaths, from 1948 to 1991 [S1]. Record each annotation as a dated update event. A changed surname is a lead for a marriage search in the same district. The new surname is also a lead for a later death search matched on the stated birth date [S1], [S2]. **Do not record the margin date as the marriage date.** Search for a separately dated marriage registration under both surnames. A register entry can still say single beside a later surname, and a reported margin date differed from the marriage registration [S1], [S11]. Record the status at registration, the later annotation and any documented marriage as three observations.

- **Closed entries.** Record a black bar as a withheld entry. The National Archives explains that Findmypast regularly opens entries as the recorded birth date reaches 100 years. A deceased person's entry can still be closed if the death went unrecorded. For a documented death, the Archives' guide describes the opening procedure [S57 @2026-11-19].

When a name search misses, check for a closed line on the expected household image. Record the closure separately from the candidate identity and repeat the search after the provider releases more entries [S60 @2026-11-22], [S64 @2026-11-22].

## Check what the year covers before reading an absence

- **Scotland.** Scotland took its own census, processed and held separately from the England and Wales returns. Its 1921 returns are not in the England and Wales collection [S8]. A presenter reports that a few forms crossed the border in each direction [S8]. Search the Scottish census for anyone who may have been north of the border. The Scottish returns from 1841 to 1921 are on ScotlandsPeople. The Scottish 1921 census is not in Ancestry's or Findmypast's 1921 collections, which cover England and Wales; search it on ScotlandsPeople. Its index is free to search with an account; each image costs 6 credits (£1.50) as of 7 November 2026 [S18], [S19], [S20].
- **Ireland and Northern Ireland, 1921.** No census was taken in Ireland in 1921, including the area that became Northern Ireland. Ireland is outside the England and Wales returns in any case. If someone was resident there in 1921, their absence from the England and Wales census is a coverage gap, not a failed search.
- **1931 and 1941.** The 1931 England and Wales returns were destroyed by fire in 1942, and no census was taken in 1941 [S8], [S11]. A gap for those years is a record gap, not a failed search. Use the 1939 Register for the period between [S11].
- **Merchant mariners at sea and other coverage limits.** The cited presentations cover vessels in port [S12], [S13] but do not establish coverage of mariners at sea. Check TNA coverage notes before reading an absence for a seafarer.

For England and Wales, 1921 is the latest census with public household returns, and the 1951 returns are due to open in 2052 [S61 @2026-11-21], [S63 @2026-11-21]. Log 1951 as an access gap while the returns are closed.

**What the series does cover.** The England and Wales returns also include the Channel Islands and the Isle of Man; vessels in English and Welsh ports and inland waterways from 1861; the British Army overseas in 1911 and 1921; and RAF bases overseas in 1921 [S16], [S25]. TNA's coverage notes answer the seafarer question: from 1861 the series includes Royal Navy and merchant ships at sea and in ports at home and abroad. In 1861 all the ship returns are at the end of the series; after that, ships in home ports are at the end of the district where they were moored, and only ships in foreign waters are at the end of the series. The shipping returns are likely to be incomplete, and none survive for Royal Navy ships in foreign waters in 1891 [S16]. Before reading an absence for an islander, a soldier or airman overseas, or a sailor or fisherman away overnight, search those parts of the series [S32]. Also read the home schedule: in 1891, for one, it was to list people out at work overnight who returned the next day and were not returned elsewhere [S38]. A miss in the shipping returns still does not show that a seafarer was ashore.

All the censuses from 1841 to 1921 are on Ancestry and Findmypast, free to search and paid to view. They are free to view on site at The National Archives in Kew, and the 1921 census also through Findmypast at Manchester Central Library and the National Library of Wales [S16 @2026-11-14].

**Privacy gate:** <!-- privacy-gate: request --> An inquiry to a county record office about a surviving listing names the parish and the family you are researching; answer the privacy gate in `SKILL.md` before you send it.

**Before 1841.** The 1801, 1811, 1821 and 1831 censuses were counts: lists of names were not collected centrally, though some survive in local record offices [S16]. Do not assume that no earlier census names anyone [S55]. Look the parish up in Richard Wall, Matthew Woollard and Beatrice Moring's guide, *Census schedules and listings, 1801–1831* (University of Essex, 2004, re-published 2012). It is arranged by county and parish and lists nearly 800 surviving English listings, most of them household listings, which often name only the head [S52], [S53], [S55]. Its authors say the guide is incomplete and many listings remain undiscovered [S52], so a parish missing from it is unresolved, not a lost return. Ask that county's record office as well.

Brigham Young University's Early British and Irish Census database (ebic.byu.edu, formerly ebc.byu.edu) is a free transcription project in progress [S54 @2026-11-14]. First look up the county alone to see which parishes have entries. In February 2025 a Middlesex search under Groves, Graves, Grove and Grave missed the target family. In a separate Yorkshire search, only the household head Thomas Cass was named [S55 @2026-11-14]. Try each spelling and record the parish, year and naming coverage before treating a miss as evidence.

## Return the observation record

For each year, return:

- the observation date: that year's census night (listed above; 19 June for 1921), or for 1939 the registration day, 29 September 1939;
- the image type (copy or schedule) and the writer of each value;
- literal values, with ages carried as ranges;
- the place role: place of enumeration, birthplace or workplace, with usual residence recorded separately when established;
- annotations recorded as dated update leads;
- locators: TNA piece, schedule and sub-number, plus viewer image;
- access and coverage gaps;
- next searches: other places the person may have slept, civil indexes, the original image.

Do not make identity, kinship or proof rulings here. Pass them to evidence/proof judgment.
