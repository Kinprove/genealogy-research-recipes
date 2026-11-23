---
id: "irish-1901-1911-census-returns"
title: "Search, retrieve and read the Irish 1901, 1911 and 1926 census returns"
summary: "Search, retrieve and read the Irish 1901, 1911 and 1926 census returns."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "IRISH-1901-1911-CENSUS-RETURNS-01", "text": "Only a townland that has returns, searched by all the routes in steps 1–2 and browsed house by house, supports \"not found in [townland], [year]\"."}]
handoff: ["evidence-proof-judgment", "irish-civil-registration-jurisdiction-recovery", "irish-emigrant-origin-locality", "irish-land-valuation-occupancy-series", "uk-census-and-1939-register-interpretation"]
checked: "2026-11-06"
checked_basis: "opened 2026-11-06"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Britain and Ireland", "order": 128}
---

# Search, retrieve and read the Irish 1901, 1911 and 1926 census returns

Use this recipe when a person or household should appear in the 1901 or 1911 census of Ireland, or when a return you found is about to be used as evidence of age, birthplace, kinship, religion or residence. It covers all 32 counties, including today's Northern Ireland: both censuses were taken for the whole island and are searched on the National Archives of Ireland (NAI) site [S23], [S24]. It prevents these failures:

- treating a name-search miss as absence, when the index holds the name in the wrong field, as written, in Irish, or in a townland that was never put online
- reading Form A alone and missing the house, landholder and townland summaries on Forms B1, B2 and N, and the neighbours
- looking for an absent family member only at home, not in an institution (often entered under initials only) or in the England and Wales census of the same night
- reading a 1911 age of an older person as true, or rejecting a correct 1901–1911 match because that person aged more than ten years
- reading the "Where born" county as a birthplace townland, or a blank column as a missing answer

Link out for the shared steps:

- **Which census years survive, the 1841/1851 census search forms, and using the surname and religion profile to choose a parish:** [Irish emigrant origin locality](irish-emigrant-origin-locality.md).
- **Tying a household to a Griffith's or revision-book lot:** [Irish land valuation occupancy series](irish-land-valuation-occupancy-series.md).
- **Reading "present marriage" child counts and suspecting stepchildren:** [UK census interpretation](uk-census-and-1939-register-interpretation.md), whose 1911 rules apply to the Irish married-women columns too.
- **Turning a birth year or a marriage-duration clue into a certificate:** [Irish civil registration recovery](irish-civil-registration-jurisdiction-recovery.md).
- **Identity rulings:** [evidence/proof judgment](evidence-proof-judgment.md).

Use section 9 for 1926: that return set covers the Irish Free State [S36 @2026-11-16]. Keep its fields separate from the 1901 and 1911 forms.

## Contents

- Inputs to gather first
- 1\. Search the current NAI system and use every field it offers
- 2\. Recover names the index holds in another form
- 3\. Prove the townland has an online return before you call a miss
- 4\. Look for absent people where they slept that night
- 5\. Collect the whole form set and the neighbours
- 6\. Read ages under each year's rules
- 7\. Read each column under its printed instruction
- 8\. Choose between same-named households on more than the name
- 9\. Use the 1926 return under its own questions
- Close with a census packet

## Inputs to gather first

- every name form known for the person: formal, pet, short and Irish-language forms, plus the names and rough ages of other likely household members
- the county, and any townland, street, parish or DED (District Electoral Division) already seen
- religion, occupation and county of birth if known from other records
- whether the person may have been in a workhouse, hospital, asylum, prison, barracks, school or on a ship on census night

## 1. Search the current NAI system and use every field it offers

- **Search at nationalarchives.ie/collections/search-the-census/.** The old census.nationalarchives.ie system was replaced in February 2025, with no redirects from old links [S22 @2026-11-19], [S27 @2026-11-19]. Links in older guides and gazetteers still point there (townlands.ie does [S32 @2026-11-19]) and no longer work. Re-run such a search on the new site instead of reporting the dead link.
- **Use the extra fields, not only the name.** Beyond year, surname, first name, county, townland/street, DED, age (searched as ±5 years) and sex, "More search options" offers relation to head, religion, literacy, occupation, marital status, county or country of origin, Irish language, specified illnesses, and the 1911 married-women counts. An "Exact matches only" box switches off variant matching [S17 @2026-11-19].
- **Search by birthplace across counties of residence.** Leave residence county blank and set county of origin to the known birthplace. For Hugh Kelly, the Tyrone resident of roughly the right age was a Presbyterian farmer. The wider search found a 43-year-old Catholic in Cork whose birthplace was Tyrone [S7 @2026-11-19]. Test the candidate's household and occupation before linking him.
- **Search a household companion.** If the target's own entry is garbled, search a spouse or child with a rarer forename, then open the household view [S18 @2026-11-19].
- **Test surname variants separately.** Compare the results with and without “Exact matches only,” then try the prefix with and without a space or apostrophe. In a March 2025 test for Mary O'Brien of Acres, Castlehyde, County Cork, O'Brien, Brien and Obrien found her. O Brien, O'Brian, O Briain and Bryan missed her [S27 @2026-11-19]. Record the individual spellings and wildcard patterns tried [S18 @2026-11-19].
- **Search NAI for Ulster too.** The NAI site holds the returns for all 32 counties, and PRONI's own guide sends researchers there [S24 @2026-11-19].

**Open household members from a MyHeritage hit.** In a [1901 Ireland Census](https://www.myheritage.com/research/collection-10199/1901-ireland-census) record [S52 @2026-11-20], check whether the names under **Household** are linked in your view. Open the member’s individual entry from that list when available [S51 @2026-11-20]. If the list does not open the member’s entry, find the household on NAI and select the person in its household view [S18 @2026-11-20].

## 2. Recover names the index holds in another form

- **Swap the fields.** Householders sometimes reversed names or wrote both in one column. Search for the surname in the forename field [S22 @2026-11-19]. In October 2026 Grenham reported making about 4,000 reversed-name returns findable in his 1901 search without changing the transcript [S1 @2026-11-19].
- **Run forename variants.** Try a wildcard on NAI [S18 @2026-11-19] and search pet forms, abbreviations and compounds such as Jack, Jno and John Joe [S22 @2026-11-19]. In October 2026 Grenham reported that his rebuilt 1901 search grouped Jack, Jno, John Joe, John Michael and Johnny with John [S1 @2026-11-19].
- **Look for a documented link between an Irish-derived and an English forename.** Thady Quill's gravestone named him Timothy. The address helped connect him to an Aghinagh baptism, while another Timothy's death registration led to the wrong family [S3 @2026-11-19]. Search both forms and compare dates, relatives and place.
- **Search Irish-language forms.** Some households wrote names in Irish, some in Gaelic script. NAI lists these in modern script without translating them. The head's name was usually also written in English on the back of the form and is indexed with the household [S22 @2026-11-19]. In Irish-speaking districts, expect Seán for John and Irish surname forms [S8 @2026-11-19]. NAI's own example: `Mich*` can return Michael and Micheál [S18 @2026-11-19]. Many Irish-language returns were only partly transcribed, especially in 1911 [S21 @2026-11-19]. Where the household's language column says Irish, browse the townland and read the images (step 3).
- **Check the image for an apparently different person.** In one household a daughter's indexed name, Isaac, read Grace on the return [S8 @2026-11-19]. NAI describes codes such as `[illegible]`, `[page torn]` and `[text struck through]` replacing older question marks [S21 @2026-11-19]. Record the code and transcribe only what the image supports.

## 3. Prove the townland has an online return before you call a miss

- **Browse the place in both years.** Go from county to DED to townland or street, then open the residents [S17 @2026-11-19]. If the townland lists households in one year and none in the other, check that year's spellings of the townland and DED, and the published population figures, before you call it a gap in the online return [S2 @2026-11-19]. An empty townland can be genuine: in 1911 an uninhabited townland was returned on a Form N marked nil [S50 @2026-11-19].
- **Known gaps exist.** Missing microfilm left whole townlands and DEDs out of the online returns. Blank townland or DED fields made other returns unsearchable by place. Since 2023, NAI has added more than 6,000 such rows back to place searches and corrected 6,331 entries in 1901 and 23,067 in 1911 [S21 @2026-11-19]. PRONI notes that most absent townlands were never microfilmed [S24 @2026-11-19]. Grenham compared NAI's 1901 data with the published DED totals. He found 16 complete or part DEDs, covering 201 townlands, missing from the 1901 database, with no untranscribed images that he could find online [S2 @2026-11-19]. He keeps a separate list of 1911 gaps: returns filmed but not transcribed, returns never filmed, and returns lost (johngrenham.com/browse/missing_1911.php) [S2 @2026-11-19]. One Cork area, Kilmartin, was missing from the online 1911 [S3 @2026-11-19].
- **Use the place spelling from each source.** The County Carlow DED of Coonogue appears as Coonague in the 1911 data [S2 @2026-11-19]. In County Armagh, the McBride household's 1901 townland Rathcarbery appears as Racabry in valuation revision book VAL/12/B/10/26C, p. 112 [S15 @2026-11-19]. Search a shared fragment, then compare the DED or nearby holdings before treating two spellings as one place.
- **Report the result accurately.** A townland classified as a gap gives "no online return for [year]". A nil Form N gives "uninhabited in [year]". Only a townland that has returns, searched by all the routes in steps 1–2 and browsed house by house, supports "not found in [townland], [year]".

**Before 1901, check which returns survive.** For 1821, 1831, 1841 or 1851, check the NAI survival list by county and year, then establish whether the fragment covers the locality before you interpret a household miss. Most returns from those years were lost in the 1922 Public Record Office fire [S41]. No individual household returns survive for 1861, 1871, 1881 or 1891 [S41]. To follow a family across that gap, use [civil registration](irish-civil-registration-jurisdiction-recovery.md) where it covers the event and check the years that survive in the parish registers [S42].

## 4. Look for absent people where they slept that night

- **Form A lists only who slept in the house on census night.** Census nights were Sunday 31 March 1901 and Sunday 2 April 1911. Absent members were left out unless they were out at work or travelling that night and came home on the Monday [S48], [S49], [S24]. A missing son or daughter is a lead to search elsewhere. Look as a visitor, boarder or servant (use the relation field), and in institutions.
- **Institutions have their own forms:** B3 shipping, C sick at home, D lunatics and idiots not in institutions, E workhouse, F hospital, G college and boarding school, H barracks (military, Royal Irish Constabulary and Metropolitan Police), I lunatics in institutions, and K prisons, bridewells and police stations [S5], [S19], [S24].
- **Search institutional returns by initials.** Start with initials, age and sex, then compare birthplace and previous occupation against the household or other records [S22], [S24]. A woman missing from her household appeared in the 1911 returns for John's Hill asylum, Waterford [S8]. Search the institution's own form by locality. Grenham's October 2026 account describes a 1901 institution list arranged by county, DED and townland [S1].
- **Search England and Wales on the same night.** England and Wales took their censuses on the same nights, 31 March 1901 and 2 April 1911 [S31]. An absence from an Irish household is a lead to search there.

## 5. Collect the whole form set and the neighbours

**Open Form A from a MyHeritage hit.** Check the top right of your MyHeritage 1901 census record for an image control. Open it when present [S51 @2026-11-20] and match the National Archives scan to the household [S52 @2026-11-20]. If you cannot open the scan, find the household on NAI by county, DED and townland or street (step 3), then open the form image there [S18 @2026-11-20].

- **Open both sides of Form A.** The front lists the people. The back carries the address block (county, poor law union, DED, barony, parish, townland, street and house number), the head's name and the house's number on Form B [S25]. The NAI record links the front and back images and the townland's other forms [S27].
- **Find the house's row on Form B1** using the number on Form B. B1, the house and building return, gives for each house the walls and roof (permanent or perishable), number of rooms, windows in front, class of house (1st to 4th), number of families, the head of each family, rooms and persons per family, and the landholder on whose holding the house stood [S26]. Presenters use it to judge living conditions and to name the landlord [S9]. Follow the holding in the valuation records under B1's landholder entry. When the landholder is not the head, the house stood on someone else's holding.
- **Read B2 and N.** B2 lists the out-offices and farm-steadings attached to each house, such as stables and coach houses [S8], [S24]. N, the enumerator's abstract, gives the townland's houses, families, males, females and persons by religion, and the enumerator's name. It lists no names [S26]; the enumerator compiled it from B1 and the household returns [S25]. The names of the heads of family are on B1 [S25], [S26]: this is the list NAI describes as a name index for each area [S20]. Read the B1 head-of-family list for a household the name search missed, and check B1's house and population totals against N.
- **Walk the neighbours.** On NAI, use the breadcrumb to go back to the street or DED and open the adjoining households [S18]. Grenham's 1901 Form A pages have Previous and Next buttons and link B1, B2 and N from the same page [S1]. For a household near a townland edge, take the bordering townlands from townlands.ie [S14], [S32] and browse them on NAI.

## 6. Read ages under each year's rules

- **Drop the age filter for an infant.** The forms call for age at last birthday and months for a child under one [S48], [S49]. A 1901 transcription left an infant's age in years blank [S7]. Search with a parent or sibling and read the age in months from the image.
- **Check unusually large increases in reported age.** The Old Age Pensions Act 1908 paid a means-tested pension from age 70, from 1 January 1909 [S28]. No one born in Ireland before 1864 had a civil birth record to check against [S28]. People aged 70 and over rose from 187,315 in 1901 to 295,027 in 1911. In England, Wales and Scotland that group grew by about a fifth over the same decade. Ó Gráda estimates that one-third to two-fifths of those who claimed to be 70 or over in 1911 had not reached that age. Some kept their census age in line with a pension claim, and others raised it in case the census was later checked against one [S28], [S30]. Based on the available excerpt (the authors' abstract), a study of linked 1901–1911 returns reports misreporting by people trying to qualify before 70, other exaggeration unrelated to the pension, and a sharp fall in round-number ages [S29].
- **Decision rule.** Flag every 1911 age of 60 or over. For a flagged person, compare the ages without requiring a ten-year gain. The largest inflation was among those claiming 70 or over [S28]. Decide a 1901–1911 match on the other columns (step 8); the age gap alone neither rejects nor confirms it. Calculate a provisional birth range from each census age and fix the birth year from a civil birth or baptism record. Without one, take the 1901 range as the working birth estimate for a person claiming 70 or over in 1911, and report the 1911 range beside it [S28]. The shortcut of taking ten years off a 1911 age and looking in the same place in 1901 [S12] fails for exactly these people. Record each census age as the household's statement, never as a birth year [S8], [S10].

## 7. Read each column under its printed instruction

- **"Where born" is a county, city or country.** The instruction asks for the county or city if born in Ireland, otherwise the country [S48], [S49]. It never names a townland or parish of birth. Do not copy the residence townland into a birthplace field.
- **"Farmer" means an occupier of land.** The 1901 instructions restrict "farmer" to occupiers of land. The entry they give for sons and daughters working at home or on the farm is "farmer's son" or "farmer's daughter" [S48]. Read "farmer" as the occupier and "farmer's son" or "farmer's daughter" as a non-occupier on the family farm. A man of 40 entered as "farmer's son" is not the occupier. Take the holding to follow in the valuation records from B1's landholder entry (step 5).
- **A blank occupation for a woman is by instruction.** No entry was to be made for wives, daughters or other female relatives engaged only in domestic duties at home [S48], [S49]. Do not record it as a missing answer.
- **Read the relationship to the head independently of the occupation.** The form asks for each person's relationship to the household head [S48], [S49]. An unmarried brother- or sister-in-law with a different surname can suggest the wife's birth family. For a married or widowed in-law, trace that person's marriage and compare both spouses' families before assigning the relationship [S7], [S16]. A shop assistant described as the head's “cusion” proved to be her second cousin only after the families were traced [S4].
- **Read signatures, marks and deletions on the image.** The head signed Form A or made a witnessed mark [S19]. The enumerator could assist [S50], so check the handwriting before attributing spellings to the head. In 1901 Alfred Henry Hunter struck out “Gentleman” as his occupation [S6]. Preserve the deletion separately from his final answer, including when the transcript uses the struck-text code [S21].
- **Religion.** Members of Protestant churches were asked to name their denomination, not to write "Protestant" [S48], [S49]. A bare "Protestant" is the household's own vague answer. Search every Protestant denomination's registers for it.
- **Irish language.** The column says "Irish" for people who spoke only Irish, "Irish and English" for those who spoke both, and is blank otherwise [S48], [S49]. A marked household is a reason to search Irish name forms (step 2).
- **1911 married women.** Each married woman was asked the completed years of her present marriage, the children born alive to it and the children still living [S49], [S20]. Use the gap between the two counts to look for children who died young [S13]. Widows were not asked. Read the counts with the present-marriage rules in the UK census recipe. Check the image: NAI warns that some details, such as marriage duration, may be visible only on the original [S18].

## 8. Choose between same-named households on more than the name

- **Narrow a common surname with independent identifiers.** A search of the 1911 returns produced over 4,500 McGoverns, about 2,000 of them in Cavan [S11 @2026-11-19]. Compare townland, relatives, religion, occupation and birthplace before attaching a household to a same-named person.
- **Link 1901 and 1911 as a pair.** Accept a match only when several of these agree: townland or street, children's forenames with ages rising by about ten, religion, county of birth, occupation, and B1 house details. A mismatch in religion or birthplace county is grounds to keep searching, not to reconcile [S7 @2026-11-19]. Record a different occupation in 1911 as a dated change, not a mismatch: a head can change work or retire in ten years.
- **Cite the place chain.** Record year, county, DED, poor law union, townland or street, and house number. One published citation gives the townland, DED, poor law union, county and household number [S15 @2026-11-19]. On the new NAI site each person has a stable record URL, but households have no URL of their own, and image links no longer expire [S27 @2026-11-19]. Cite a person's record URL and the image links.

**Follow a MyHeritage household into 1911.** From a 1901 MyHeritage hit, search its [1911 Ireland Census](https://www.myheritage.com/research/collection-10198/1911-ireland-census) for the same household and apply the matching criteria above [S53 @2026-11-21], [S54 @2026-11-21]. MyHeritage credits NAI for the 1911 index and images [S54 @2026-11-21]. Count a MyHeritage result and the matching NAI return as a single 1911 return.

## 9. Use the 1926 return under its own questions

**Choose the census by jurisdiction.** For a locality in the Irish Free State, go from 1911 to the first Free State census, taken on 18 April 1926 [S40], [S45]. No census was taken in Ireland in 1921 because of the War of Independence [S40].

**For Northern Ireland, keep 1911 as the household reference.** Northern Ireland took a separate 1926 census, but its household returns are believed to have been destroyed [S43 @2026-11-18]. Use the published 1926 and 1937 tables for population and locality context only [S43 @2026-11-18], [S44 @2026-11-18].

**Open the year’s search form.** Use NAI’s [Search the Census 1926](https://nationalarchives.ie/collections/search-the-1926-census/) for 1926 and follow its separate link for 1901 and 1911 [S47 @2026-11-18].

- **Coverage and place.** The 1926 NAI returns cover the Irish Free State [S36 @2026-11-16]. For a known townland or street, use the map’s county, DED and townland/street route to browse its households [S34 @2026-11-16]. Northern Ireland is outside this return set.
- **Age.** Record years and months as asked on Form A, retaining both when comparing a birth record [S33 @2026-11-16].
- **Occupation and employer.** Read these fields on the image [S33 @2026-11-16]. Their searchable transcription is a later release phase [S35 @2026-11-16]; a keyword miss does not show the image fields were blank.
- **Video source.** Only a transcript excerpt was inspected for the video’s 1926 search suggestions in this section [S37 @2026-11-16].

**Check relatives’ returns for a missing household member.** Look for the person as a visitor, or follow evidence that work or travel took them elsewhere. Form A counted those who spent census night in the household and those received the next morning who had yet to be counted [S45].

**Read the birthplace townland or town on the image.** Form A asked for county and townland or town for an Irish birthplace [S45 @2026-11-18]. The birthplace search covers county or country [S46 @2026-11-18]. Use the locality written on the form to narrow earlier searches for a person with a common name or someone found in an institution. Keep the birthplace separate from where the person was enumerated.

**Read employment separately from occupation.** Record the trade in the occupation column and the employer's name and business, or the status “Own Account” when given, from the employment column [S45].

**Read marriage or orphanhood by age.** For a person aged 15 or over, record the marital status. For a child under 15, record whether the return says both parents were alive, the father was dead, the mother was dead, or both were dead [S45]. A parent’s absence from the household is a separate observation.

**Use orphanhood to bound a death search.** Daniel Loftus’s suggestion from the available excerpt is to use the two censuses to narrow the search for a parent’s death [S38], [S39]. If you identify the parent alive in 1911 and the child’s 1926 orphanhood entry reports that parent dead, restrict the initial civil death or burial search to the interval between census nights. Treat the interval as a search lead until a matching record confirms the death [S45].

**Keep the child counts tied to their questions.** In 1926, married women reported completed years and months of the present marriage and the children born alive to it. Keep the 1911 count of children still living with the 1911 return. In 1926, married men, widowers and widows reported one total of living children and stepchildren under 16, including those living elsewhere [S33], [S45]. Use this as a dependant count across marriages. Leave the number from any one marriage and the number of deaths unresolved by that total.

## Close with a census packet

Return:

- **Search log:** each site and form used, the name forms, wildcards and swaps run, the fields filled, and the count of hits.
- **Coverage row per year:** whether the townland has online returns, any known gap (with the list or page consulted), and the place spellings used in each year.
- **Household record:** the literal transcription and your reading of the image side by side for each person, with Form A front and back, the B1 row (house class, rooms, landholder), B2 and N, and the neighbouring households and bordering townlands searched.
- **Age table:** the 1901 and 1911 ages, the birth range derived from each, and a flag on every 1911 age of 60 or over.
- **Absence leads:** institutions, other households and the England and Wales returns searched for anyone missing on census night.
- **Citation:** year, county, DED, poor law union, townland or street, house number, person record URL and image links.

- **1926 rows:** years and months of age, birthplace as written, marriage or orphanhood answer, the exact child-count question and respondent category, and occupation/employer fields read on the image.

Identity and kinship rulings go to evidence/proof judgment.
