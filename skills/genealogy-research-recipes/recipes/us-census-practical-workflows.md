---
id: "us-census-practical-workflows"
title: "Practical U.S. census workflows"
summary: "Ten practical U.S. census procedures: recover households, browse target-year districts, follow 1950 revisit sheets, compare pre-1850 age bins, bridge the 1890 gap, extract supplements and family fields, search mortality schedules, follow surname changes, and follow a farm lead into an agricultural schedule."
kind: "records"
scope: {"platforms": [], "tasks": ["a missing census household, an address without a name hit, sheet 71, tick-mark counts, substitute censuses, sample lines, marriage/children fields, competing child rosters, mortality reporting windows, or formerly enslaved families under different surnames."]}
privacy: "none"
gates: []
guardrails: [{"id": "US-CENSUS-PRACTICAL-WORKFLOWS-01", "text": "Preserve the original census locator and keep literal observations separate from calculations and proposed identities."}]
handoff: ["evidence-proof-judgment", "land-index-book-series-recovery", "us-military-pension-file-recovery"]
checked: "2026-10-20"
checked_basis: "checked 2026-10-20"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "full", "group": "Featured workflows", "order": 21}
---

# Practical U.S. census workflows

Use these procedures to recover households, browse a bounded district, extract year-specific
fields, or produce a comparison artifact. Preserve the original census locator and keep
literal observations separate from calculations and proposed identities.

Keep a wider research plan, query log and report alongside these census working records.
Use [Ancestry search recovery](ancestry-record-search-recovery.md)
or [MyHeritage record search](myheritage-historical-record-search.md)
for provider-specific search controls. This recipe supplies the census working records.
Route identity, kinship and negative-evidence rulings to
[evidence and proof judgment](evidence-proof-judgment.md).

## Contents

- Preserve the output schema
- Choose a recipe
- 1\. Recover a missing household by changing the search anchor
- 2\. Turn an address into an enumeration-district search
- 3\. Recover a 1950 household from the revisit sheets
- 4\. Use pre-1850 age bins as constraints on candidate households
- 5\. Bridge the 1890 gap with a coverage table and dated timeline
- 6\. Extract the informant, supplementary answers and enumerator notes
- 7\. Turn census marriage and child fields into targeted searches
- 8\. Use mortality schedules with the correct death window
- 9\. Track a formerly enslaved family through changing surnames
- 10\. Follow a farm lead into an agricultural schedule

## Preserve the output schema

Each procedure below produces the corresponding table. These column orders are this
recipe's proposed packaging of the source methods; the sources do not prescribe these exact
schemas. Keep a literal value alongside any interpretation. An unavailable value stays
unknown rather than becoming zero, false, or a guessed name.

Every `source_locator` or entry locator carries:
`census_year, schedule_type, state, county_as_recorded, locality_as_recorded,
enumeration_district_if_present, printed_sheet_or_page, line_numbers,
viewer_image_number, record_url_or_repository_locator, accessed_at`.
Keep fields unavailable on that schedule explicitly unknown. A viewer counter and a
printed sheet/page number are separate fields.

A schedule page, especially an early one, can carry more than one set of page numbers, such as a stamped number and a handwritten one [S99], [S101]. Write in `printed_sheet_or_page` which set you used and how it appears, as in `p. 792 (stamped at top right)` [S101]; Evidence Explained advises a parenthetical word or two for the same reason [S100]. Record the other sets too, each with its form and position on the page.

Before 1880 there is no enumeration district number to record. Early censuses were taken by the marshal's subdivision, and the term changed to enumeration district only with the 1880 census [S90]. For 1790 to 1870, leave `enumeration_district_if_present` unknown, and reject a citation template, including an AI-drafted one, that asks for an ED [S89]. Record the district, town or city named in the page heading as `locality_as_recorded`, even when the heading gives a district number [S91]. From 1850, the dwelling and family numbers, which run in the order of visitation, identify the household on the page [S91]. For Recipe 2 before 1880, look for a description of the subdivision instead: NARA's T1224 reproduces descriptions of subdivisions from 1830 on [S90].

| Procedure | Fixed column order |
| --- | --- |
| 1: query log | `search_id, census_year, collection, member_anchor, query_text, filters, searched_at, result_status, candidate_locator, image_reading, identity_conflicts, next_action` |
| 2: location and browse log | `location_id, target_year, observed_address_or_property, observation_date, location_source_locator, historical_jurisdiction, target_year_ed, map_or_description_locator, boundary_reason, browse_image_range, browse_sheet_range, gaps, outcome` |
| 3: revisit link | `district, original_locator, original_line, reference_literal, revisit_locator, revisit_line, link_evidence, result_status` |
| 4: literal counts | `candidate_id, census_year, census_reference_date, source_locator, column_label, lower_age, upper_age, upper_bound_inclusive, recorded_count, classification_literal, overlap_note` |
| 4: proposed assignments | `candidate_id, census_year, proposed_person_id, compatible_column, birth_interval, independent_person_evidence, assignment_status, conflict, next_record` |
| 5: coverage | `record_type, jurisdiction, actual_years, repository_locator, access_status, search_performed, searched_at, result, remaining_gap` |
| 5: timeline | `person_or_household, observation_date, locality_as_recorded, event_or_residence_literal, source_locator, jurisdiction_change_note, unresolved_link` |
| 6: supplement or note | `person_as_recorded, source_locator, person_line, question_heading, field_status, answer_literal, supplement_line_or_note_reference, interpretation, unresolved_subject` |
| 7: event lead | `person_as_recorded, census_year, source_locator, field_heading, reported_value, calculation, derived_search_window, proposed_event, conflict, corroborating_locator, next_search` |
| 8: mortality entry | `person_as_recorded, source_locator, death_month_literal, stated_reporting_window, inferred_death_year, inference_basis, household_reference_literal, population_locator, identity_comparison, conflict` |
| 9: identity chain | `candidate_link_id, earlier_person_literal, earlier_locator, later_person_literal, later_locator, surname_observations, household_comparison, corroborating_document_locator, enslavement_evidence_status, link_status, next_record` |
| 10: agricultural entry | `candidate_id, census_year, source_locator, operator_literal, population_candidate_locator, identity_link_basis, printed_line_and_continuation, column_heading, answer_literal, unit, land_record_question, unresolved_conflict` |

For search and coverage outcomes distinguish `not_searched`, `searched_no_candidate`,
`candidate_found`, `inaccessible`, `incomplete`, and `illegible`.
For extracted answers distinguish `answered`, `explicit_no`, `blank`, `not_asked`, and
`unreadable`. A blank is not an explicit negative.

Before expanding an abbreviation, interpreting a blank or category, or turning a field into a
search target, read that census year's enumerator instructions and apply the definitions then
in force ([Genealogy Gems](https://www.youtube.com/watch?v=0XVhB44U7aA),
[Lisa Lisson](https://www.youtube.com/watch?v=ZlTq5IxHCuM)). In the 1950 instructions as read by
[Family History Fanatics](https://www.youtube.com/watch?v=GNX7J94oEIE) and
[Genealogy Gems](https://www.youtube.com/watch?v=TEwTGVS88Oo), an out-of-state hospital birth is
entered under the family's state, common-law unions as married, and anyone 14 or under as never
married. A relationship entry of 'partner' is paraphrased as unrelated people sharing a
dwelling, not its modern sense ([Blandón Traiman](https://www.youtube.com/watch?v=dkkYqyBWIXc),
[earlier version](https://www.youtube.com/watch?v=HC5z95y_5ic)). Read a changed race or a health
term the same way and record it literally ([FHF 2020](https://www.youtube.com/watch?v=b6jSyhjEwuk),
[Crow](https://www.youtube.com/watch?v=D5weC7CmDlo)). Instructions show intended procedure, not
what an enumerator did. Keep the literal entry beside the interpretation, and do not reuse one
year's definitions for another.

Expand a place abbreviation by the usage of the record's own date, not by today's postal code. The Post Office's 1831 list abbreviated Indiana as `Ia.` and had no entry for Iowa; its 1874 list used `Ind.` and `Iowa` [S113]. Read an 1850 `Ia.` for a person living in Indiana as Indiana unless other records point to Iowa [S112], [S114]. The same tip reports `Ca.` for both Canada and California in some census records [S112]. Test the reading against the household's residence and the other members' birthplaces before you search that state's records.

Record each census's official reference date as `census_reference_date`, separate from the visit date written on the sheet. The Census Bureau gives the first Monday in August for 1790 to 1820 (2 August 1790, 4 August 1800, 6 August 1810, 7 August 1820), 1 June for 1830 to 1880 and for 1900, 15 April for 1910, 1 January for 1920 and 1 April from 1930 [S96]. For 1890 it gives 2 June, but the 1890 instructions list everyone whose usual home was in the district on 1 June 1890 [S96], [S127]; record 1 June and note the conflict when an age or a birth near that date matters. The person who answered may have described the household on the day of the visit instead, or mixed up the two dates [S95].

Before you read a blank occupation as 'did not work', check whom that year's question covered, and record a blank outside it as `not_asked`. The 1850 instructions asked an occupation only for each male over 15 [S106]; 1860 asked it of each person over 15 [S107]; 1870 entered women keeping house for their own families as `keeping house` [S131]; 1880 asked it of each person, male or female [S103], and of a child of any age who earned money regularly [S104]; 1900 asked it of persons 10 and over who were at work [S108]; 1940 and 1950 only of persons 14 and over [S109], [S110]. Price Genealogy's list of these scopes [S105] dates the inclusion of women to 1880; follow the instructions instead.

In 1880, also extract the months unemployed during the census year and the sickness column, which records an illness only on the day of the enumerator's visit, not over the year [S103]. A child marked as having attended school within the census year can also have an occupation; that is not a conflict [S103], [S104]. Any link between the illness, the months unemployed and the work, as in Price Genealogy's 1880 examples, is your inference [S102].

For 1950, read race, sex and marital status by the instructions, not as the household's own answers. Enumerators assumed that relatives in the household had the respondent's race unless told otherwise, and asked it only for unrelated people such as lodgers and employees. A person of mixed white and nonwhite parentage was entered with the nonwhite parent's race, and a mixture of nonwhite races with the father's race, subject to the exceptions the instructions name. The sex of a person absent at the interview was taken from name and relationship. `Sep` covered a legal separation or a parting through marital discord; couples apart for work or military service were entered as married; and a person whose only marriage had been annulled was entered `Nev` [S110]. So `Nev` does not rule out an annulled marriage. Price Genealogy's summary [S111] narrows 'separated' to legal separation and applies the father's-race rule to all mixed parentage; follow the instructions.

Before applying an age-based calculation, check that its input represents the recorded age
in the required unit. If the calculation cannot handle that value, retain the person,
literal age/unit and source locator and mark only the calculation unresolved. Do not clear
the source value or remove the person to make a formula fill. Genealogy TV's
[historical Excel demonstration](https://www.youtube.com/watch?v=eONcu9lTbYY) [S71]
motivates this safeguard; it does not validate a formula or establish a birth date.

## Choose a recipe

| Problem | Recipe | Deliverable |
| --- | --- | --- |
| A household disappears from name searches | 1. Change the search anchor | Query log and candidate households |
| You know a location but cannot find the family | 2. Address to enumeration district | Map-backed district list and browse log |
| A 1950 entry says nobody was home | 3. Follow the revisit reference | Linked original and revisit entries |
| Most household members are unnamed | 4. Reconstruct age-bin constraints | Household matrix with explicit hypotheses |
| The 1890 gap interrupts the family | 5. Build a substitute-record timeline | Coverage table and dated residence timeline |
| An index omits extra census information | 6. Read supplements and notes | Person-linked supplementary extraction |
| You need missing children or a marriage period | 7. Extract family-event leads | Event hypotheses and targeted record searches |
| Someone may have died before enumeration | 8. Search mortality schedules | Death-window and household correlation |
| A formerly enslaved family changes surnames | 9. Track the family group | Candidate identity chain across censuses |
| A population entry or other evidence suggests a farm | 10. Follow agricultural schedules | Linked entry, literal quantities and land-record question |

## 1. Recover a missing household by changing the search anchor

**Use when:** Searching the expected surname or head of household produces no plausible result.

**Inputs:** A household roster from another record; first and middle names; approximate ages; birthplaces; and independently supported locations.

1. List every expected member. Mark which names, ages, and birthplaces are best supported. Include children: their entries may be easier to recognize than the adults' entries.
2. Search each member separately in the target census. Then remove the surname from a distinctive member's query, keeping given name, age range, birthplace, and a supported search area.
3. Try a short name fragment or wildcard where the platform permits it. Change one constraint at a time and record the actual query. An unsuccessful surname search is a failed query, not evidence that the household was absent.
4. Extend the locality using relatives' marriages, residences, or other dated evidence. Do not restrict a missing household to the location where it appeared ten years earlier.
   Before recording a member as missing, moved or dead, read that year's rules on who was counted where. Keep the sheet's visit date separate from the official reference date ([Tanner 1880](https://www.youtube.com/watch?v=7Jn_XMUozo0)). Someone who died after the reference date may rightly be listed ([Genealogy Gems](https://www.youtube.com/watch?v=p4O1Zlol-2k)), and a baby born after it should be absent ([Tanner 1880](https://www.youtube.com/watch?v=7Jn_XMUozo0), [FHF](https://www.youtube.com/watch?v=GNX7J94oEIE)). As the cited presenters describe them (confirm in the 1950 enumerator instructions), the 1950 rules count college students at college and leave visitors, boarding pupils, inmates and absent servicemen out of the home household ([FHF](https://www.youtube.com/watch?v=GNX7J94oEIE), [Genealogy Gems](https://www.youtube.com/watch?v=87hGRjeZ5o4), [podcast](https://www.youtube.com/watch?v=R3Ds6GLx4es)). Lisa Lisson reports separate P-5 overseas and P8 reservation schedules, and no enumeration of other Americans abroad ([overview](https://www.youtube.com/watch?v=q7-fXZJTU7U), [preview](https://www.youtube.com/watch?v=tnaXso4LSCE)); a Family History Fanatics case shows a citizen abroad uncounted in 1930 and 1940 ([case](https://www.youtube.com/watch?v=gsbQIuilOYk)). Search where the rule points, such as an institution. Other years need their own rules, enumerators may not have complied, and an explanation stays unproven until another record places the person.
5. Open candidate images. Compare the whole roster, ages, birthplaces, and local associates. Record indexed spelling and the image reading separately. Search the apparent alternative surname locally before dismissing it as a transcription error.
   Before concluding that a household or member was omitted, check the page edges. A household at the top or bottom of a page may continue on the previous or next image, and an index may leave the parts unconnected ([Lefler](https://www.youtube.com/watch?v=7yVDky7MvO0), [FamilySearch indexing example](https://www.youtube.com/watch?v=vdpmIU_XOA4)). Record the continuation locator. Check the printed page sequence for a missing page, and look for a damaged or illegible entry. Test whether the head's surname was carried onto a wife and children living apart, whether children carry a stepfather's surname, and whether travel took the family away during enumeration ([FHF](https://www.youtube.com/watch?v=itVYbPHf_Oc), [travel example](https://www.youtube.com/watch?v=jeshnSv9xQ0)). If the surname on the image is blank or crossed out, also search under the previous household's surname, as in one 1930 indexing error ([Annie's Ghosts](https://www.youtube.com/watch?v=9OkR0D6bDyg)). Line order is not a relationship. Each explanation stays a hypothesis until a linked entry or dated record supports it.
   If an entry is hard to read, try an available image of the same entry on another host
   and the adjustment controls actually offered there. Match the schedule, printed page
   and household or line before comparing readings; viewer image numbers can differ.
   Record the host, image locator and reading in `image_reading`. A clearer presentation
   is another copy of the same record, not independent corroboration. If no usable copy
   is available, retain the legibility gap. Aimee Cross demonstrates this recovery step
   without establishing that one provider always has better images. [S69]
6. If name searches remain unproductive, use Recipe 2. A second platform can expose a different index, but two indexes of the same census entry remain one underlying record.
7. Expect that one person may appear twice in a census year. Examples: a 1950 student at a dormitory and with a military family, a married son still listed by his parents ([Brady](https://www.youtube.com/watch?v=o6d7Z_W_qhg), [Tanner](https://www.youtube.com/watch?v=xW-2PVfobaE), [Genealogy Gems](https://www.youtube.com/watch?v=dY9EV5R_6ZA)), or a servant entered days before her family's listing ([Genealogy Gems](https://www.youtube.com/watch?v=xzJUics2RDs)). A family that moved between districts during enumeration can be missed at both addresses or counted at both, so compare the dates written on the sheets ([Legacy Tree answer](https://www.youtube.com/watch?v=LwjPdTcCxMM)). Keep both entries with their dates and locators. Do not split them into two people or discard one, and do not choose a residence without other evidence. Test the double-enumeration or move hypothesis with independent records. None of these sources says how often it happens.

Before reading an early-census miss as absence from a state, check that the state's schedules survive. The Georgia Archives says the first three census schedules for Georgia, 1790 to 1810, are missing, lists an 1800 Oglethorpe County return among its state census reports, and names tax digests as the substitute [S93 @2026-11-12]. Diana Elder's Georgia case treats Oglethorpe as the only county with an extant 1800 census [S92 @2026-11-12]. Log a lost year as a coverage gap, not as `searched_no_candidate`, and search the substitute.

Check every early state and year the same way. NARA knows of no 1790 schedules for Delaware, Georgia, Kentucky, New Jersey, Tennessee or Virginia and says they were apparently destroyed in the British attack on Washington in the War of 1812 [S121 @2026-11-14]. For 1810 there are no schedules for the District of Columbia, Georgia, Mississippi, New Jersey, Ohio, most of Tennessee, or the Illinois, Indiana and Michigan territories [S120 @2026-11-14]. Do not blame every loss on the war: FamilySearch gives no cause for these 1810 losses [S120 @2026-11-14]. Search tax lists as the substitute [S115 @2026-11-14], [S120 @2026-11-14]; FamilySearch also names voter registrations [S120 @2026-11-14]. For a man thought to be in Ohio around the War of 1812, start with the 1820 census and read nothing into his absence from 1810 [S119 @2026-11-14].

Do not read a Native person's absence from an early census as absence from the place. The Constitution excluded "Indians not taxed" from the count, and in 1790 most Indians were not counted [S116]. The 1800 and 1810 schedules counted "all other free persons, except Indians, not taxed" [S137], [S120], and Price Genealogy notes that the 1790–1840 censuses are of little help for Native ancestors who did not pay taxes [S115]. For 1950, a person living on a reservation may also appear on Form P8, the Indian Reservation Schedule, which repeats the P1 name and adds other names, tribe, clan, degree of Indian blood, languages and participation in ceremonies in 1949; people on reservations in Alaska and Oklahoma, and those off reservations, are on P1 only [S117], [S118], [S154]. The form's heading names the reservation [S111]. Copy the P8 entries literally and take the tribe and any other name to [tribal enrollment records](us-tribal-enrollment-record-recovery.md).

In a household on or near Cherokee land before removal, do not read a missing wife or child as proof that there was none. The Constitution left "Indians not taxed" out of the count, and the 1860 instructions told enumerators not to enumerate them [S87]. Roberta Estes notes that a white man's Native wife or children would therefore not appear with him [S86]. Search the tribe's own enumerations, such as the 1835 Henderson Roll (NARA T496), which lists Cherokee heads of household in Alabama, Georgia and Tennessee with information on each family and its property [S88].

If a man has a middle name that could pass for a surname, also search that name as his surname. One tip reports an 1870 entry that dropped the man's surname and used his middle name in its place [S97], and a FamilySearch user reports a 1900 enumerator who entered a man's given name as the surname of his whole family [S98].

If a person cannot be found in any record before their own marriage and their mother remarried during their childhood, find her later marriage. Then search the stepfather's households, from that marriage to the person's own, for a child of the right age under his surname [S122], [S123]. Enumerators often entered all the children under the head's surname [S125], and someone else may have supplied the child's name to the enumerator, so the marriage record may be the first in which the person gave their own name [S122]. Keep the stepfather's surname as a search name for those years even after you have proved the birth surname, and expect the birth surname to turn up occasionally after the marriage [S123]. A child listed under a stepfather's surname was not thereby adopted: formal adoption was uncommon in the 19th century, and neither a later record calling the child his nor a guardianship proves an adoption [S124]. Name the stepfather an adoptive father only on a court adoption record.

When a man is missing from his family's household, also search the jails and prisons of the area: the 1890 and 1950 instructions entered prisoners and other inmates at the institution, and in 1950 every jail prisoner however short the stay [S127], [S110], and a prison term can explain the absence [S126]. Follow such a lead with [criminal court and prison records](criminal-court-prison-record-recovery.md). The tip adds that a divorce over the imprisonment can leave court records of its own [S126].

For a 1950 absence, also check the other forms. Transients at some hotels, YMCAs and other paid lodgings were counted on 'T-Night' by special enumerators [S110], [S111]. Form P2, the Individual Census Report, was used for military personnel in barracks on U.S. soil and for travelers at hotels, YMCAs and campgrounds, and Form P4 for the crews of U.S.-flag vessels in U.S. and territorial ports; both were usually copied onto Form P1, so search P1 first [S118]. Do not expect a return for an American abroad: information on most overseas personnel was not retained, though schedules survive for military personnel stationed in the territories [S118].

If an earlier census shows the person owning a home or land and the next finds the household elsewhere or not at all, compare the two places of residence and search the earlier county's deed indexes for the years between to date the sale and the move [S129], [S130]; use [land-record recovery](land-index-book-series-recovery.md) for the indexes. Treat a real-estate value that later goes blank as the same lead [S128], not as a sale: the 1850 and 1860 values covered real estate wherever it lay [S106], [S107], and in 1870 personal estate under $100 was not entered [S131]. Legacy Tree warns that a Pennsylvania deed could be recorded years after the transaction, and advises searching the indexes long after the person left [S130].

**Output:** A query log containing census year, collection, query, filters, result, candidate image citation, and identity conflicts.

**Checkpoint:** Retain a candidate only after household-level comparison. A matching child or unusual first name nominates a household; it does not establish everyone's identity or relationships.

**Example prompt:** “Using this known household roster, propose an ordered census search matrix. Include searches through children, surname-free searches, and locations supported by the attached records. Keep candidate identities separate from confirmed identities.”

**Method origin:** Family Locket's case found a household through a child's given names, age, and birthplace after searches for the parents and surname failed. It also demonstrates wildcard searching and extending the locality through siblings' records. [S1](https://familylocket.com/3-tips-for-searching-the-census-when-a-family-goes-missing/)

## 2. Turn an address into an enumeration-district search

**Use when:** The index fails, or you want to inspect the actual neighborhood.

**Inputs:** Census year; a dated address or rural location; the historical jurisdiction; and nearby streets, landmarks, or property descriptions.

1. Assemble location evidence close to the census date: city directories, draft registrations, letters, school records, vital records, or other dated documents. Keep an address from a different year as a lead until supported for the target year.
2. Identify the county and locality as they existed in that year. Check boundary changes before interpreting a different county name as a move.
   Apply the same check at state or territory level: a later state may have been enumerated under an earlier territory, as with present-day Wisconsin residents under Michigan Territory in 1820 and 1830 ([Brady](https://www.youtube.com/watch?v=kFxsAw8HHAs)). Check territorial dates against a boundary reference; a failed modern-state search is a failed query, not absence.
3. Locate enumeration-district maps and descriptions for the target census. Family Locket demonstrates using Steve Morse's One-Step resources to reach archival maps. Compare the address or property with streets and landmarks; retain every district consistent with the evidence.
4. Browse the district's population-schedule images. Record image numbers and the sheet/page numbers printed on the schedules separately. Inspect continuation pages and later sections, following any cross-references.
   Record the margin street name and the house-number column separately from dwelling, family or visitation numbers. Do not search directories by a visitation number ([Grant](https://www.youtube.com/watch?v=6aZsWQpatYA), [Genealogy Gems](https://www.youtube.com/watch?v=RIz4bAPdmWM)). A ruled line or a new street name can end a street mid-page ([Genealogy Gems](https://www.youtube.com/watch?v=RIz4bAPdmWM)). Read the prescribed urban or rural route ([Lisson](https://www.youtube.com/watch?v=tnaXso4LSCE)) and the pages before and after. Check for breaks where enumeration resumed later; in rural areas, 'next door' may mean the next farm ([Tanner](https://www.youtube.com/watch?v=UwXwt3lcp9s)). Some early lists were alphabetized ([FHF](https://www.youtube.com/watch?v=CjjD9mI_dY8), [Lisson 1790](https://www.youtube.com/watch?v=QAidkkT515s), [tips](https://www.youtube.com/watch?v=c1FM5Se8zYY)), so establish the arrangement from the pages. A new family number without a new dwelling number marks a second family in one dwelling ([Potter](https://www.youtube.com/watch?v=CXe0BbBtKME)). Page adjacency establishes neither neighbours nor kinship.
5. Keep a browse log: district, range inspected, street or landmark encountered, candidate households, and gaps. If the location lies near a district boundary, inspect the plausible neighboring district too.
6. Save the map or description citation alongside the census citation so another researcher can reproduce why this district was selected.

In a tenement or apartment house, expect one dwelling number with a family number for each occupied apartment: the 1910 instructions counted such a building as one dwelling and each occupied apartment as a separate family [S85]. For an immigrant family, read every family under that dwelling number, and log those born in the same country or speaking the same language as associate (FAN) leads [S84]. A shared building is a lead to test, not kinship.

**Output:** An address-evidence table, map-backed district list, and page-browse coverage log.

**Checkpoint:** Never carry an enumeration-district number into another census year without checking that year's map. Similar numbers do not establish identical boundaries. An image-only collection also needs a browse search; a name-search failure does not cover it.

**Example prompt:** “Given these dated addresses and this target-year district map, list all plausible districts and explain the boundary evidence. Produce a page-browse log template without assuming the family stayed at its earlier address.”

**Method origin:** Family Locket demonstrates locating an Idaho household through rivers, roads, railways, and target-year maps; Who Are You Made Of explains changing district boundaries; Genealogy TV demonstrates finding census maps in image-only holdings. [S12](https://familylocket.com/rlp-191-preparing-for-the-1950-u-s-census-release/), [S15](https://whoareyoumadeof.com/blog/what-is-an-enumeration-district-on-the-census/), [S3](https://www.youtube.com/watch?v=1ectqP9Ogys)

## 3. Recover a 1950 household from the revisit sheets

**Use when:** A 1950 entry says nobody was home or directs you to another sheet.

**Inputs:** The original entry, district, printed sheet number, line number, and any handwritten cross-reference.

1. Read the entire entry, including the margin. Transcribe its sheet-and-line reference exactly.
2. Follow that reference within the same district. Amy Johnson Crow's demonstration follows an entry to sheet 71, line 12, even though the viewer contains only 24 images. The image counter and the printed sheet number use different numbering systems.
3. If no complete reference is visible, inspect the district's later sheets for the revisit section. The demonstrated revisit numbering begins at sheet 71 even when the regular sheets end near sheet 10; that jump is not a missing-page gap. Read the printed sheet number in the page's upper right corner rather than requesting viewer image 71.
4. Compare the revisit household's address, names, and other identifiers with the original entry. Save citations to both entries and explain the link.
5. If an image is blurred, covered, or folded, inspect nearby images for a repeated exposure before recording it as unreadable. Record an access or legibility gap if no usable exposure is found.

**Output:** A linked pair of citations and the completed household extraction.

**Checkpoint:** “Nobody home on the first visit” does not establish that the household was omitted. A later entry must still be linked by its reference or other identifying evidence.

**Example prompt:** “Transcribe this entry's revisit reference. Tell me which printed sheet and line to locate, distinguish them from the viewer image number, and list what must match before linking the two entries.”

**Method origin:** Amy Johnson Crow's worked example explains revisit sheet 71, the 24-image discrepancy, and looking for repeated photographic exposures. [S18](https://www.youtube.com/watch?v=4p_afzX34Uk)

## 4. Use pre-1850 age bins as constraints on candidate households

**Use when:** The relevant schedule names a household head but leaves most other people as counts in categories.

**Inputs:** Complete schedule images and headings; the census reference date; independently known family members; and all plausible heads with the same name.

1. Transcribe every relevant column from the image, including its exact age bounds and historical classification. Keep categories separate. Do not reconstruct the household from the indexed totals alone.
   For 1820–1840, open the facing second page or image as well as the tally page; it carries different columns. Count down to the same line, check the alignment against the totals, and cite both locators ([Lisson walkthrough](https://www.youtube.com/watch?v=7kVPg63qM2g), [pre-1850 tips](https://www.youtube.com/watch?v=c1FM5Se8zYY), [Smith](https://www.youtube.com/watch?v=Gr6ZqgpehE4)). The 1840 continuation names military pensioners with ages ([Wilcox](https://www.youtube.com/watch?v=HG6sY_S-Neg), [pensioner tip](https://www.youtube.com/watch?v=JOB67IJEfPU)). A pensioner may be a widow or another resident rather than the head. For a Revolutionary War veteran or widow, also check the 1840 pensioner listing and its 1841 compilation. Record pensioner, age and head of family separately, and search the population schedule under that head ([Strauss](https://www.youtube.com/watch?v=nJsQ9ftU9iM)). A pensioner entry is a lead to pension files, not proof of service or of the relationship to the head. An age-derived birth year is an estimate.
2. Build a matrix with one row per candidate household and one column per printed category. Read the headings afresh for each census year rather than reusing another year's bins.
3. Convert age categories into possible birth-date intervals. This calculation assumes the reported category is accurate. For an inclusive age range `a` through `b` at reference date `D`, the interval is `(D minus (b + 1) years, D minus a years]`. Interpret headings such as “under” or “of ... and under ...” literally.
4. Place independently known people into compatible bins as **hypotheses**. Preserve unmatched counts. Household membership does not automatically establish parentage, marriage, or sibling relationships.
   Use stable hypothesis IDs across census years. Within each mutually exclusive category,
   proposed assignments must not exceed its recorded count; preserve the unassigned remainder.
   Keep overlapping columns separate rather than treating them as independent capacity.
5. Compare candidate heads across adjacent censuses and other records. Track recurring associates and historical jurisdictions. Reject a candidate only for an evidenced conflict, not a surname preference.
6. Investigate a missing expected adult through alternate names, adjacent locations, property records, or another enumeration. Keep error, absence, and separate residence as distinct explanations.

Check first which columns carry an age or a sex at all. The 1790 schedule counts free white females, the head of family included, with no age split, so a female tick does not show a wife or a daughter [S136], [S115]. The 1790 to 1810 schedules count "all other free persons" and slaves with no age or sex [S136], [S137], [S120]; age and sex categories for free people of color and the enslaved begin in 1820 [S138]. Do not put those people into age bins or relationships.

To test whether same-named heads in successive censuses are one household, follow the oldest male, the oldest female and the children's tallies: each person counted should be about ten years older in the next census and sit in the category that fits that age, and the places should fit the other evidence [S132], [S133]. Ages that do not progress, or sexes that do not line up, usually mean a different family [S133]. A death, a remarriage, someone moving in or out, or a misstated age can also explain a single change [S132]; record which explanation you test.

When an adult cannot be found as a head before 1850, look for an extra tick in the right sex and age column in the households of relatives who were heads: a parent or step-parent, an older brother, a brother-in-law [S134]. A widowed mother, for example, may be only a tick in a married child's household [S135]. Record a compatible tick as a hypothesis; it does not name anyone.

In 1820 and 1830, read the count of foreigners not naturalized [S139], [S140]. A tally there is a lead to passenger lists and naturalization records through [U.S. immigration search](usa-immigration-search-recovery.md) [S138], [S115]. It does not say which member of the household was the alien.

If one head's tallies hold more young men or children than a family plausibly contains,
especially near a college or academy, test a commercial or institutional household. Search
local newspapers for tavern, hotel, boarding-house or school notices that name the head,
including notices by later keepers that name him as a former proprietor. Record each notice's
date and locator, and compare the date with the census reference date, because a house can
change keepers. A notice offering student lodging at that house supports reading the excess
counts as boarders rather than the head's children. A young relative otherwise thought missed
may be one of those boarders. Keep that as a hypothesis: a compatible bin does not name him,
and it does not exclude another enumeration elsewhere. [S80]

To seek names behind household counts before 1850, consider the Pennsylvania account's reported
'Poor School Children' lists at the ends of township tax volumes. Confirm the locality, year and
surviving volume, then follow any county index to the original list. Record only the child names,
ages or family connections it states, with its date and inclusion limits; keep proposed census-bin
matches separate. Compatible ages alone do not identify an unnamed household member. [S79]

If headings are missing or unreadable, consult a legible blank form for the same census
year, jurisdiction and schedule. Compare its column sequence with the actual page's
remaining labels and layout before assigning a heading; an early handwritten schedule
need not follow the sample form's arrangement. Keep the form's locator and proposed
column interpretation separate from the literal image reading. If correspondence cannot
be established, leave the heading unresolved. The [blank-form demonstration](https://www.youtube.com/watch?v=1lrFNBWKwzo)
supplies the fallback; these alignment checks do not certify a particular original form.

**Output:** The literal count matrix, proposed person-to-bin assignments, conflicts, and next records needed to test each assignment.

**Checkpoint:** A compatible age bin supports a candidate household. It does not name the unnamed person. Check whether any columns overlap before summing totals.

**Example prompt:** “Create separate literal-count and hypothesis tables from these schedules. Use the printed age bounds, compare all same-name heads, and identify the documents needed to test each proposed assignment.”

**Method origin:** Family Locket demonstrates checking image tick marks, distinguishing same-name heads, following associates, and investigating a head found separately under another name. The interval formula and matrix schema above are analytical adaptations. [S4](https://www.youtube.com/watch?v=oBkEoVQtPcQ)

## 5. Bridge the 1890 gap with a coverage table and dated timeline

**Use when:** The missing population schedules interrupt a family between 1880 and 1900.

**Inputs:** The 1880 and 1900 households; intervening locations; historical county boundaries; and repository or collection descriptions.

1. Compare both households member by member. List people who disappeared, appeared, married, changed names, or changed recorded location. Keep each unexplained change as a separate research question.
2. Check whether surviving 1890 population fragments cover the locality. Check veterans' schedules separately when relevant; they have their own geographical and subject coverage.
   Before searching the 1890 Union veterans and widows schedules, check the state. The National Archives description quoted by [Genealogy Gems](https://www.youtube.com/watch?v=zRuGRGwNmf0) says they survive largely for Kentucky through Wyoming, with Alabama through Kansas only as miscellaneous returns. Search for widows as well as soldiers. For a veteran who died before 1890, the widow's entry may name both and give the unit and service dates ([Family History Fanatics](https://www.youtube.com/watch?v=cpulm6BuAJ8)). A widow listed under a surname different from her soldier's is a remarriage lead. Some Confederates were entered against instructions and some of those lines crossed out; record struck lines literally ([Cochran](https://www.youtube.com/watch?v=NmtuDJBE5eQ), [Lefler](https://www.youtube.com/watch?v=ygn9UBhamaI)). Coverage is fragmentary and inclusion inconsistent. An entry does not prove service, and a widow's entry must still be matched to the right soldier.

   For a relevant 1890 veterans-schedule entry, read both portions of the sheet. Use the printed line number and sheet context to match the upper service fields with the lower post-office-address, disability and remarks fields. Preserve multiple service rows and widow wording. A widow's post-office address is hers, not evidence of the deceased veteran's residence in 1890. Carry recorded unit and service dates as leads into the [pension-file workflow](us-military-pension-file-recovery.md). If the lower portion or its link is missing or illegible, record the gap instead of transferring a nearby row. [S76, H5, H6]

   Where an 1890 population fragment survives, read it as a family schedule: one sheet for each family, with each person's answers in a column rather than a row [S127], [S150]. It asks whether each person was a Civil War soldier, sailor or marine, Union or Confederate, or the widow of one, written as, for example, `Sol (U.S.)` or `W. Sol (Conf.)`; whether the person married during the census year; and, for each woman ever married, how many children she had borne and how many were living [S127]. Its race entries include mulatto, quadroon and octoroon [S127]. Record an empty answer as `blank`, as in a Price Genealogy example where the children's counts were left empty [S150].

3. Build a coverage table for state, territorial, local, and school censuses, directories, tax records, vital records, deeds, probate, newspapers, and other dated records. Record actual years and jurisdictions held rather than copying a broad database title.
   Where a census social schedule survives for the county and year, read it even though it names no one. It can list the taxes collected, the newspapers published and how often they appeared, and the churches counted by denomination. Turn these into coverage-table rows: tax series to request, newspaper titles to locate, and the congregations of the family's supported denomination whose records to seek. The [Curt Witcher interview](https://www.youtube.com/watch?v=uhOTAGepIms) motivates this step. It does not establish which years or places survive, where the schedules are held, or that a listed church's records still exist. A finite church count narrows the search; it does not identify the family's congregation.
4. Search for non-federal censuses between the two federal dates. If no state census is known, investigate municipal, township, county, or other local enumerations. Search library catalogs and finding aids when an online index is absent.
   For Colorado, Florida, Nebraska, New Mexico Territory and Dakota Territory, check the 1885 censuses, taken under an act of 3 March 1879 and paid for in part with federal funds. They are the closest in date to the lost 1890 population schedule. NARA holds Colorado (M158), Florida (M845), Nebraska (M352) and New Mexico Territory (M846). Dakota Territory's schedules were never transferred to NARA: they are at the North Dakota or South Dakota state archives, depending on the part of the territory ([NARA, the 1885 census](https://www.archives.gov/publications/prologue/2008/fall/1885-census.html); [NARA M846](https://www.archives.gov/files/research/census/nonpopulation/m846.pdf)). The State Historical Society of North Dakota holds the northern part ([State Historical Society of North Dakota, archived page](https://web.archive.org/web/20260113231006/https://www.history.nd.gov/archives/gencensus1800.html)).
   Record in each coverage row whom a list was meant to cover, not only its years. Some local lists covered only landowners, adult men for militia, citizens or school-age children. Crow describes Ohio's quadrennial county enumerations as permitted rather than required ([FHF with Amy Johnson Crow](https://www.youtube.com/watch?v=CjjD9mI_dY8)); verify the applicable law and surviving series for the county and year. For a voter list, establish who could register from the law in force at that place and date. Do not assume women were excluded before 1920 ([Lisson](https://www.youtube.com/watch?v=jgLVRtRRheM), [Cochran](https://www.youtube.com/watch?v=NmtuDJBE5eQ)). [Allen's Pennsylvania periods](https://www.youtube.com/watch?v=27z3ekBQ4qk) are not adopted as verified rules. Search registers or poll lists, which name individuals, not election returns, which name candidates, and log browses of unindexed county volumes ([Allen](https://www.youtube.com/watch?v=QSyyFuZWsA0), [California register](https://www.youtube.com/watch?v=uHn2P2ZmpyY), [Barker](https://www.youtube.com/watch?v=hWwgeBcsEQI)). A register's age, birthplace or description can separate same-named men. A 'Mrs. [husband]' entry does not say which wife. Assess each list's coverage before reading a missing name: it may fall outside the list's scope, or reflect omission or retrieval failure; it is not by itself evidence of absence.
5. Add dated residence observations to a timeline. Check whether changed county boundaries explain apparently different locations. Search married children separately under supported names.
6. Reconcile the timeline with the 1880 and 1900 households. Record searches that remain incomplete because records were inaccessible, unindexed, illegible, or outside the reviewed coverage.

**Output:** A table of record type, jurisdiction, actual years, repository, access status, search performed, and result; plus a dated family timeline.

**Checkpoint:** A missing federal census does not imply a record-free decade. A directory can provide residence evidence without listing every household member, and a veterans' schedule is not a replacement population census.

**Example prompt:** “Using these two households and collection descriptions, create an 1880–1900 coverage plan. Distinguish records searched, records known but inaccessible, and records whose survival has not been established.”

**Method origin:** Sara Cochran discusses fragments, veterans, school censuses, directories, family reconstruction, and boundary changes. James Tanner demonstrates state and local census discovery and library searches. [S20](https://www.youtube.com/watch?v=NmtuDJBE5eQ), [S21](https://www.youtube.com/watch?v=DYAVc-ih68g)

[Ancestry's demonstration](https://www.youtube.com/watch?v=UtoRoxYo2JE) follows the veterans schedule's lower fields and unit clues. The [official form image](https://www.census.gov/content/dam/Census/programs-surveys/decennial/technical-documentation/questionnaires/1890veteranscensus.jpg) shows the repeated line numbers; the [1890 instructions, printed page 45](https://www.census.gov/content/dam/Census/programs-surveys/decennial/technical-documentation/questionnaires/1890instructions.pdf), distinguish multiple service spaces and a widow's present post-office address. [S76, H5, H6]

## 6. Extract the informant, supplementary answers and enumerator notes

**Use when:** A standard index or household crop seems to contain too little information.

**Inputs:** The full 1940 or 1950 sheet, household line numbers, and adjacent images where an entry continues.

1. Read the whole sheet, including the top, bottom, margins, and any continuation. Record the form and printed headings actually present.
   A surname may be copied from the head ([FHF](https://www.youtube.com/watch?v=CC-6uGAuSiY)). An alphabetical run under an institution heading suggests an official's list ([Crow](https://www.youtube.com/watch?v=D5weC7CmDlo)). Compare the enumerator's letter forms before calling a spelling an error ([GeneaVlogger](https://www.youtube.com/watch?v=-CxvuPelZ4I)). A 1950 transient marked REG was copied from a lodging register ([Genealogy Gems 1950 preview](https://www.youtube.com/watch?v=87hGRjeZ5o4)).
2. For 1940, look for a circled X after a household member's name in column 7 ([Genealogy Gems 1950 preview](https://www.youtube.com/watch?v=87hGRjeZ5o4), [provenance episode](https://www.youtube.com/watch?v=mTyYpO_3uPs), [Episode 260](https://www.youtube.com/watch?v=R3Ds6GLx4es), [Brady](https://www.youtube.com/watch?v=o6d7Z_W_qhg)). The instructions identify that person as the household informant; information from someone outside the household should instead have that person's name in the left margin opposite the household. Preserve the actual mark or note and its locator, and record the marked person, or the written-in outside informant such as a neighbour, as the household informant. If neither is legible or present, leave the informant unknown rather than assume the household head. The mark identifies the informant; it does not establish who supplied every answer or whether they knew each fact firsthand. [S74, H2] It was not always used carefully and does not show whether the answers are accurate. Weigh each answer by what the informant was likely to know. A relationship may reflect the informant's view, such as a widow labelled 'mother' because her daughter answered ([GeneaVlogger](https://www.youtube.com/watch?v=g5aMe7oUW_A)).
3. For each household member, check whether the line is designated for supplementary questions. Match the person to the supplementary section by its printed line number.
4. Transcribe each answer with the question it answers. Do not apply a supplementary answer to every person in the household.
5. Resolve note numbers and written line references. A written reference such as “L 24” may have no number on the entry itself; a note number may sit over a caret beside the supplementary line, before a name, or inside the answer it qualifies, such as the age. Attach a note to the indicated entry or field. Notes can explain revisions, a doubted age and who gave it, employment details, visitors with no other residence whose lines belong after an earlier household, or why an entry was struck through, such as a death and its month [S8]. Keep a disputed answer beside the note's alternative.
6. Keep blanks, unreadable text, questions not asked, and explicit negative answers distinct. Record uncertainty about the note's subject instead of assigning it by proximity.

**Output:** A person-linked extraction containing question, literal answer, sheet/line, supplement or note reference, any identified informant with the mark/note locator, interpretation, and uncertainty.

**Checkpoint:** Use the markings on the actual form. Amy Johnson Crow demonstrates a 1950 sample-line-4 example, so a summary listing only other sample lines is incomplete. A crossed-out entry needs its associated note before interpretation.

When an identified WPA or CCC connection accompanies a 1940 emergency-work entry,
follow it to civilian personnel or application records. Preserve the entry's reference
week; a generic yes or program names printed in the question do not identify a program.
[Family Locket's discussion](https://www.youtube.com/watch?v=YSF4GCv61kg) [S72] points to
WPA and CCC records at NARA in St. Louis. Use that historical pointer to find the identified
program's current series, custodian and request guide before requesting. Leave other or
unknown programs unresolved; no NYA route is supplied here. CCC files may name camps;
civilian service is not military service.

In 1950, match each supplementary answer to its tier before you read a blank. Items 21 to 33, such as residence a year ago, parents' birthplaces, schooling and veteran status, were asked of the six people on each sheet's sample lines; items 34 to 38, including 'married more than once' and the number of children ever borne, only of the person on the last sample line [S110], [S154]. A blank for anyone else is `not_asked`. The children count leaves out stillbirths, adopted children and the woman's stepchildren, and includes children of earlier marriages, children who had died and children living elsewhere; the enumerator told her about adopted children only if she asked [S110], [S111]. The housing questions on the back of the sheets were not microfilmed, and the paper schedules were destroyed in 1961–1963, so no household's housing answers survive [S118], [S111].

Read a territory's 1950 schedule by its own form. Alaska's omitted the sample lines and asked many of the sample questions of everyone; the forms for American Samoa and Guam were shorter and had no sample questions; the Virgin Islands schedule had none; and Puerto Rico's was printed in Spanish [S151], [S111]. On a form without sample questions, a missing sample answer is `not_asked`.

**Example prompt:** “Extract this household, its marked supplementary questions, and every linked note. Preserve the person-to-line mapping and distinguish blank, unreadable, not asked, and explicit no.”

**Method origin:** Genealogy TV demonstrates matching a 1940 person to the bottom section. Amy Johnson Crow demonstrates a 1950 sample-line-4 entry and separately discusses locating and linking enumerator notes. The notes video's 1950 examples show a line-number note, footnote numbers beside the supplementary line, before a name and in the age column, and notes on a death, visitors with no other residence and a doubted age. [S7](https://www.youtube.com/watch?v=JJY4EKK_sVg), [S19](https://www.youtube.com/watch?v=jA10V_GJcio), [S8](https://www.youtube.com/watch?v=ZzrQQz4BIT4)

The [MyHeritage census demonstration](https://www.youtube.com/watch?v=4P8sUi-Adno) motivates extracting the 1940 informant mark. [Official paragraph 446](https://www2.census.gov/library/publications/decennial/1940/population-volume-4/33973538v4p1ch2.pdf) specifies both the circled X and the outside informant's margin note; this does not verify the demonstrated household or extend the rule to another census year.

## 7. Turn census marriage and child fields into targeted searches

**Use when:** You need a birth or marriage period, missing children, or evidence that a household combines more than one family.

**Inputs:** Full household images from multiple censuses, literal relationship fields, reported marriage duration or status, and children-born/children-living fields where present. For 1880, retain the birth-month and recent-marriage fields. For 1930, retain each person's reported age and age at first marriage separately.

1. Extract the reported fields without normalizing discrepancies. Include relationships to the head exactly as recorded. A list of co-residents in an 1850 or 1860 population schedule does not supply the relationship column introduced in 1880.

   For 1880, preserve column 7's birth-month entry and column 12's marriage mark, alongside the person's marital-status fields. The census year ran from 1 June 1879 through 31 May 1880. If the entry follows those instructions, June–December birth months suggest 1879 and January–May suggest 1880. Treat an affirmative marriage mark as a lead to that window, not an exact date or an identified spouse. Column 12 applied to married, widowed or divorced people; do not assume the mark dates a first marriage or the union shown in the household. Keep derived leads separate from literal answers and investigate conflicts. A blank does not establish that the person never married. [S75, H3]

   Read the earlier fields the same way. The 1850 and 1860 schedules mark each person married within the year before 1 June, and the 1870 schedule gives the month of a birth or a marriage within the year [S106], [S107], [S142]. Use such a month as a dated lead where no vital record survives, not as a vital record [S141]. If the 1850 instruction was followed, an unmarked couple married before 1 June 1849. One researcher used that, with no children yet in the household, only to estimate a marriage shortly before that date [S143]; the missing children are an inference, since children can die or live elsewhere. The 1900 schedule gives every person's month and year of birth [S108], [S105].

   Before 1880 the schedule states no relationships; the 1850 instructions listed the parents, then the children from the oldest at home to the youngest, then other inmates, lodgers, boarders, laborers and servants [S106]. Treat a person out of age order among the children, or an older one listed after them, as a lead to test in other records: a married child with a spouse, another relative, someone who had moved back or did not really live there, or an enumerator's error [S144].

2. Derive a marriage-period lead from reported duration. Compare multiple enumerations and retain disagreement. A subtraction such as census year minus reported married years is an approximate search lead, not an exact marriage date.
3. For 1930, use `1930 - (reported age - reported age at first marriage)` only as a first-marriage search lead for that person. Age refers to 1 April 1930; allow for birthday timing and uncertain reported ages. The estimate need not date the union shown in the household. Compare the spouses' leads ([Brady](https://www.youtube.com/watch?v=o6d7Z_W_qhg)): disagreement prompts prior-marriage or reporting-error checks, while agreement does not prove they first married each other. Column 15 applied only to people recorded as married in column 14, so a blank does not establish that the person never married. [S73, H1]
4. Inspect indications of previous marriages using the relevant form headings and instructions. Do not assume every duration or child count refers only to the couple shown together.
   Test the reported marriage duration, or the 1930 age at first marriage, against the known marriage date and the children's ages. A child born before the derived period, or a first-marriage age that predates the known wedding, is an earlier-marriage lead ([Grant 1930](https://www.youtube.com/watch?v=Dtl6pnXMiEY), [BYU 1900](https://www.youtube.com/watch?v=cZZ2IbQSyPc)). Read a 1910 code such as M2 as a second or later marriage, not necessarily the second ([Lisson](https://www.youtube.com/watch?v=7kVPg63qM2g)). Households can give stepchildren the current surname, so check birth registrations under that surname, then under the mother's earlier married surname ([Grant 1911](https://www.youtube.com/watch?v=S7NX-GnX4UU)). These are approximate leads. Ages and durations can be misreported, and parentage needs the registrations or other records.
5. Where both child counts are legible, calculate `reported children born minus reported children living`. Treat the result as a reported difference requiring investigation. Do not create named deceased children from it. A living child absent from the household may be living elsewhere.

   Adapt [Robyn N. Smith's child-count comparison](https://reclaimingkin.com/two-men-become-one-identity/)
   to test a one-child/two-child hypothesis: when two names may denote one child or two,
   build a separate child roster for each hypothesis. Record each documented child once
   per roster, its maternal-link evidence and whether it was alive on each census reference
   date; leave unknown links or survival unresolved. Compare each roster's required
   born/living totals with the mother's literal reported counts. Apply the
   [1900 question definitions, paragraphs 136–137](https://www.census.gov/programs-surveys/decennial-census/technical-documentation/questionnaires/1900/1900-instructions.html)
   and [1910 definitions, paragraphs 116–117](https://www.census.gov/programs-surveys/decennial-census/technical-documentation/questionnaires/1910/1910-instructions.html):
   these concern her own lifetime children, including living children elsewhere. Log the
   discrepancy and the maternal link, birth, death or census answer to check. Counts alone
   do not merge names or exclude a child; pass both hypotheses and linked observations to
   [evidence and proof judgment](evidence-proof-judgment.md). [S77, H7, H8]

   Record 'widowed' or 'single' as the reported status, not proof that a spouse died or never existed. A Census Bureau marriage-and-divorce report quoted by [Genealogy Gems](https://www.youtube.com/watch?v=SExmNq646NM) says divorced people often reported themselves as single or widowed. [Lisa Lisson](https://www.youtube.com/watch?v=Hi9QQZG8JoI) keeps divorce, desertion or bigamy open when there is no death record. Search for the spouse as a living person, including in that spouse's parents' household with any missing children, then for divorce records in the relevant jurisdiction. Do not derive a death date from the census year. Neither source shows how common misreporting was.
6. Search for missing people through surrounding households, marriages, deaths, cemetery records, probate, and other suitable records. Compare the resulting candidates with the original households.
7. Store literal statement, calculation, proposed event, and supporting record in separate fields. Keep immigration and naturalization statements as leads to the relevant documentary records rather than exact events established by the census alone.
   Where the form records language or mother tongue, extract it next to the country of birth as a separate observation. This matters most when the birthplace names an empire or a pre-unification label such as Austria or Germany. A language that does not fit the stated country can point to a region inside a multinational state, as when Magyar redirected Austria-born research to Hungary ([Tanner](https://www.youtube.com/watch?v=htx73TZD-bo), [Hungary](https://www.youtube.com/watch?v=PeS050cNO-A), [immigrant](https://www.youtube.com/watch?v=SxDbhOu-_1Y)). Test it together with religion. Language narrows a region. It does not identify a town or establish a birthplace or modern country, and many languages were spoken across several countries.

In 1910 and 1920, extract the parents' mother tongues as well: both years recorded the mother tongue of foreign-born parents as well as of the foreign-born person, in 1910 written into the birthplace columns and in 1920 in separate columns for the person, the father and the mother [S149], [S148]. A parent's language describes that parent even if the parent never came to the United States [S147]. Do not look for it in other years: 1930 asked only the foreign-born person's own language, 1940 the language spoken at home in earliest childhood, and 1950 asked none [S149].

When a man's wife has the same given name in successive censuses, compare her stated age and birthplace from one census to the next. A disagreement can mean two wives with the same given name; check the marriage records first [S145]. In one published case, an 1850 census wife and an 1814 marriage record that gave no middle names or initials were merged into one woman, although the man had married twice [S146].

**Output:** A family-event hypothesis table and specific follow-up searches.

**Checkpoint:** Do not infer biological relationships from co-residence or assign a woman's reported child count to the current husband without evidence. Unreadable or missing counts do not become zero.

**Example prompt:** “Compare these households. Separate literal fields from calculated marriage-period and missing-child leads. Identify prior-marriage questions and name the records needed to resolve them; do not invent relatives.”

**Method origin:** Ancestry's worked comparison produces differing approximate marriage years from successive censuses. BlackProGen discusses children-born/living fields and previous marriages. MyHeritage explains the relationship column and immigration fields. [S6](https://www.youtube.com/watch?v=cMrTbAj5YN0), [S10](https://www.youtube.com/watch?v=Ejmjf550pHc), [S13](https://education.myheritage.com/article/the-u-s-census-tracing-your-family-in-census-records/)

[Ancestry's 1930 example](https://www.youtube.com/watch?v=lvRG8tZ2eYU) supplies the separate
first-marriage-age calculation. The [official enumerator instructions](https://www.census.gov/content/dam/Census/programs-surveys/decennial/technical-documentation/questionnaires/1930instructions.pdf),
paragraphs 156–157 and 161 (printed pages 26–27), establish the reference date, possible
approximate ages and question scope. Agreement between calculated periods is retained as
a search lead, without adopting the video's conclusion that both spouses necessarily
married each other first. [S73, H1]

[Ancestry's 1880 example](https://www.youtube.com/watch?v=hhRsjcf0AQg) turns the birth-month
and recent-marriage fields into record searches. The [official question headings and notes A, D, E and G](https://www.census.gov/programs-surveys/decennial-census/technical-documentation/questionnaires.1880_Census.html)
define their interval and scope. The [instructions for Schedule 1](https://www.census.gov/programs-surveys/decennial-census/technical-documentation/questionnaires/1880/1880-instructions.html)
use 1 June as the reference date, independently of the visit date; a conflicting entry
still needs corroboration. [S75, H3, H4]

## 8. Use mortality schedules with the correct death window

**Use when:** A death may fall shortly before a census, especially where civil death registration is limited.

**Inputs:** Candidate name variants, residence, approximate death period, household information, and the schedule's stated coverage.

1. Establish that mortality schedules survive for the relevant year and locality. Inspect the collection's actual contents, not just its broad title. If online coverage excludes the locality, investigate archival holdings: schedules returned to a state are usually in its state library, archives or historical society; those the Census Bureau kept went to the DAR Library in Washington, D.C., or the National Archives [S9 @2026-11-08].
2. Read the schedule's reporting window. In Amy Johnson Crow's 1850 example, it covers 1 June 1849 through 31 May 1850. A September death in that reporting window belongs to 1849.
3. Search name and locality variants, then compare age, birthplace, occupation, and other recorded details. The 1880 schedule asks whether the person lived here but died elsewhere, or died here but lived elsewhere; one death can appear on two schedules, so search both localities [S9].
4. Where a mortality entry supplies a household or family reference, follow it into the corresponding population schedule. Compare the surviving household; do not assume an identical name identifies the deceased.
5. Preserve literal death month, inferred calendar year, stated reporting window, and identity reasoning separately. Retain any conflict with other death evidence.

Legacy Tree's discussion of 1880 mortality returns reports physician notes on the reverse of the
main form. Check whether the surviving copy includes those pages before calling an entry complete.
Keep each family answer, physician statement and enumerator addition separately attributed, with
its subject and locator; leave uncertain authorship unresolved. A later medical explanation remains
a claim to assess, rather than automatically replacing the earlier answer. [S78]

**Output:** A cited death-window extraction and any supported link to the population household.

**Checkpoint:** Do not assign the census year automatically to a reported death month. An online collection's absence of a locality is a coverage limitation, not evidence that the person did not die there.

**Example prompt:** “Interpret this mortality entry using its stated reporting window. Separate literal month from inferred year, follow any household reference, and evaluate the identity without relying on name alone.”

**Method origin:** Amy Johnson Crow demonstrates the reporting-window calculation, household-number correlation, and checking state coverage before searching, and explains the 1880 died-elsewhere questions and where the schedules ended up. [S9](https://www.youtube.com/watch?v=sZ1kgZLY1V0)

## 9. Track a formerly enslaved family through changing surnames

**Use when:** You have a post-emancipation household, but surname continuity is uncertain.

**Inputs:** A supported household, multiple census images, ages, birthplaces, associates, and named documentary records relevant to the family.

1. Extract the whole supported household and local associates. Make a separate list of literal surnames and spelling variants for each census.
2. Search other household members under given names, approximate ages, and birthplaces. Compare family-group composition across 1870, 1880, and 1900 where the people could still be living.
3. Investigate a surname change without requiring the family to use an alleged enslaver's surname. Keep each proposed link as a candidate until corroborated.
4. Use age and household continuity to generate searches in named post-emancipation records, such as voter registrations, and appropriate records that can identify enslaved people or establish family links.
5. When examining unnamed entries in slave schedules, record the literal demographic information and its context. An age/sex match does not name a person or establish a family.
6. Keep documentary enslavement evidence separate from census race, birthplace, age, and surname observations. A 1900 census profile alone does not establish enslavement or identify an enslaver.

For 1870, also search the household under the wife's maiden surname. The FamilyTreeDNA guide reports couples counted under the wife's surname in 1870 and under the husband's in 1880, and adult children, enslaved with their mother by a different enslaver than their father's, counted under their mother's maiden name in their first census [S81]. Family members did not always take the same surname, and surnames changed [S82]. Take the maiden surname from a cohabitation record where one survives: North Carolina's 1866 cohabitation bonds give the man's and the woman's names [S83], and [freedpeople record recovery](us-freedpeople-record-recovery.md) covers the registers. Keep each link a candidate until a record joins the two households.

If named post-emancipation records leave an enslaver question unresolved, define a bounded
1870 neighborhood to inspect and record neighboring households as possible research leads.
Trace each selected named person into earlier censuses, comparing identity before carrying
the lead backward. Retain the literal property fields with their year and heading; do not
use a wealth threshold to infer enslaving status. Search relevant deeds, probate inventories
and estate-sale records for named people and transactions. Add relatives to the worklist
when inspected records supply a reason to investigate a transfer or bequest through them.
Where relevant claims files survive, search both the target's and candidate's names and
inspect witness testimony. Keep the candidate, reason, earlier locator, record searched,
named-person evidence, conflicts and next action in a separate worklist. Neighborhood
proximity, recorded race or property value does not establish an enslaver or show that the
family remained in its former location. This bounded adaptation of [Aimee Cross's example](https://www.youtube.com/watch?v=12gmfLSWs70)
excludes the video's property-value heuristic and assumed residence continuity. [S68]

**Output:** A candidate identity chain, household comparisons, surname observations, and the documentary evidence needed for each unresolved link.

**Checkpoint:** Do not attach an unnamed slave-schedule entry or an enslaver to a person solely through matching surname, age, or locality. Keep free status and unknown status open where the documents do not resolve them.

**Example prompt:** “Compare these households while allowing surname changes. Rank proposed person links using the entire family group, keep slavery-status claims separate, and specify what named records would establish each link.”

**Method origin:** Family Locket explicitly discusses surname changes, family-group and age comparison, voter registrations, and the limitations of slave schedules. Its dataset announcements are not treated as currently verified access instructions. [S11](https://familylocket.com/tracing-the-enslaved-in-the-1900-u-s-census-and-enslaved-org-project/)

## 10. Follow a farm lead into an agricultural schedule

**Use when:** A population entry names a farmer/planter, or other evidence supports a farm.

1. Check survival and actual coverage of agricultural schedules for the year and locality.
   Search supported name variants and inspect the image, including ambiguous indexed initials.
   A 1950 population entry's agriculture questionnaire number points to a questionnaire destroyed
   as a temporary record; record the number literally and do not request the questionnaire.
2. Compare the named operator and locality with the population candidate. Record the identifying
   evidence and conflicts; a similar name or position in the list leaves the link unresolved.
3. Read the printed headings and follow the entry across continuation pages using the printed
   line/page references. Preserve each answer with its heading and unit, including acreage,
   values, livestock or production only where actually asked and answered.
4. Use the observations to form a specific [land-record search](land-index-book-series-recovery.md).
   Farm operation and reported value alone do not establish title, kinship or an identified parcel.

For step 1, start from NARA's Nonpopulation Census Records page. It lists, state by state, the 1850–1880 agriculture schedules on NARA microfilm and those held elsewhere, such as state archives and libraries, and sends you to the state archives for anything else [S94 @2026-11-12]. The FamilyTreeDNA guide notes that very few agricultural schedules were filmed and that many are only at state archives [S81 @2026-11-12].

In 1880, read the tenure columns: whether the operator owned the farm or rented it for a fixed money rent or for a share of the products [S152], [S153]. An owner answer supports the deed search in step 4. A renter answer makes a deed for the operator unlikely, so search for the landowner instead, and keep the tenure answer literally in the agricultural entry.

**Output:** An agricultural-entry row using the census locator above, the population candidate,
link basis, continuation references, literal quantities/units and remaining land-record question.

**Method origin:** [BYU's population-to-agricultural example](https://www.youtube.com/watch?v=CXe0BbBtKME)
demonstrates an indexed-initial error, a second-page line reference and a deed-search lead.
Its examples do not establish universal year coverage or independently verify ownership.

Amy Johnson Crow explains that the 1950 agriculture questionnaires were destroyed as temporary
records. [S18](https://www.youtube.com/watch?v=4p_afzX34Uk)
