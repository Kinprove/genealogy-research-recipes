---
id: "irish-1901-1911-census-returns"
title: "Search, retrieve and read the Irish 1901 and 1911 census returns"
summary: "Search, retrieve and read the Irish 1901 and 1911 census returns."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "IRISH-1901-1911-CENSUS-RETURNS-01", "text": "Only a townland that has returns, searched by all the routes in steps 1–2 and browsed house by house, supports \"not found in [townland], [year]\"."}]
handoff: ["evidence-proof-judgment", "irish-civil-registration-jurisdiction-recovery", "irish-emigrant-origin-locality", "irish-land-valuation-occupancy-series", "uk-census-and-1939-register-interpretation"]
checked: "2026-11-06"
checked_basis: "opened 2026-11-06"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "pointer", "group": "Irish and British records", "order": 1074}
---

# Search, retrieve and read the Irish 1901 and 1911 census returns

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

## Inputs to gather first

- every name form known for the person: formal, pet, short and Irish-language forms, plus the names and rough ages of other likely household members
- the county, and any townland, street, parish or DED (District Electoral Division) already seen
- religion, occupation and county of birth if known from other records
- whether the person may have been in a workhouse, hospital, asylum, prison, barracks, school or on a ship on census night

## 1. Search the current NAI system and use every field it offers

- **Search at nationalarchives.ie/collections/search-the-census/.** The old census.nationalarchives.ie system was replaced in February 2025, with no redirects from old links [S22], [S27]. Links in older guides and gazetteers still point there (townlands.ie does [S32]) and no longer work. Re-run such a search on the new site instead of reporting the dead link.
- **Use the extra fields, not only the name.** Beyond year, surname, first name, county, townland/street, DED, age (searched as ±5 years) and sex, "More search options" offers relation to head, religion, literacy, occupation, marital status, county or country of origin, Irish language, specified illnesses, and the 1911 married-women counts. An "Exact matches only" box switches off variant matching [S17].
- **Search by county of birth across every county of residence.** In one presenter's case, the man of the right name and age found in the expected county was a Presbyterian farmer, not the Catholic sought. A search with no residence county and "county of origin" set to that county found a Catholic born there, of the right age, living in Cork [S7].
- **Search a household companion.** If the target's own entry is garbled, search a spouse or child with a rarer forename, then open the household view [S18].
- **Do not trust the variant matching to cover spellings.** The new system matches variant spellings unless "Exact matches only" is ticked, and Soundex was added for surnames. A March 2025 test found one woman under O'Brien, Brien and Obrien but not under O Brien, O'Brian, O Briain or Bryan [S27]. Run each prefix form, each spelling and each wildcard pattern (`*` or `?`) as a separate search [S18], [S27].
- **Search NAI for Ulster too.** The NAI site holds the returns for all 32 counties, and PRONI's own guide sends researchers there [S24].

## 2. Recover names the index holds in another form

- **Swap the fields.** Names are transcribed as written and spellings were not corrected. Some households wrote the whole name in one column or reversed forename and surname. NAI's own advice is to put the surname in the forename box [S22]. Do this for every 1901 and 1911 miss. For 1901, John Grenham's rebuilt search (johngrenham.com/1901/) identified about 4,000 returns with reversed names and made them findable without changing the transcript [S1].
- **Run forename variants yourself on NAI.** NAI's guide answers forename variation with wildcards, not variant lists [S18]. Its own examples of short forms in the returns are Maggie, Annie, Jno and Mick [S22]. Search pet forms (Jack, Johnny, Mick), abbreviations (Jno) and compound forms (John Joe) as separate searches. Grenham's 1901 search has forename variant families (3,135 families, 72,635 forenames) and surname variant families (12,545 families, 83,399 surnames); "John" with variants returns Jack, Jno, John Joe, John Michael and Johnny [S1].
- **Pair English names with Irish-derived ones.** A man known as Thady is named Timothy on his gravestone [S3]. Search the formal English equivalent of a pet or Irish-derived name, and the reverse.
- **Search Irish-language forms.** Some households wrote names in Irish, some in Gaelic script. NAI lists these in modern script without translating them. The head's name was usually also written in English on the back of the form and is indexed with the household [S22]. In Irish-speaking districts, expect Seán for John and Irish surname forms [S8]. NAI's own example: `Mich*` can return Michael and Micheál [S18]. Many Irish-language returns were only partly transcribed, especially in 1911 [S21]. Where the household's language column says Irish, browse the townland and read the images (step 3).
- **Expect transcription errors and gaps.** In one presenter's case the index read Isaac where the image read Grace [S8]. Unclear text was once transcribed as "?". NAI has replaced many of those with codes such as `[illegible]`, `[page torn]` and `[text struck through]` [S21]. Treat a coded or "?" field as unread, not as a different person.

## 3. Prove the townland has an online return before you call a miss

- **Browse the place in both years.** Go from county to DED to townland or street, then open the residents [S17]. If the townland lists households in one year and none in the other, check that year's spellings of the townland and DED, and the published population figures, before you call it a gap in the online return [S2]. An empty townland can be genuine: in 1911 an uninhabited townland was returned on a Form N marked nil [S25].
- **Known gaps exist.** Missing microfilm left whole townlands and DEDs out of the online returns. Blank townland or DED fields made other returns unsearchable by place. Since 2023, NAI has added more than 6,000 such rows back to place searches and corrected 6,331 entries in 1901 and 23,067 in 1911 [S21]. PRONI notes that most absent townlands were never microfilmed [S24]. Grenham compared NAI's 1901 data with the published DED totals. He found 16 complete or part DEDs, covering 201 townlands, missing from the 1901 database, with no untranscribed images that he could find online [S2]. He keeps a separate list of 1911 gaps: returns filmed but not transcribed, returns never filmed, and returns lost (johngrenham.com/browse/missing_1911.php) [S2]. One Cork area, Kilmartin, was missing from the online 1911 [S3].
- **Allow for changed place spellings.** One DED is Coonogue in the 1901 data and Coonague in 1911 [S2]. One townland is Rathcarbery in the census and Racabry in the valuation books [S15]. Search a fragment of the name with a wildcard before you decide a place is missing.
- **Report the result accurately.** A townland classified as a gap gives "no online return for [year]". A nil Form N gives "uninhabited in [year]". Only a townland that has returns, searched by all the routes in steps 1–2 and browsed house by house, supports "not found in [townland], [year]".

## 4. Look for absent people where they slept that night

- **Form A lists only who slept in the house on census night.** Census nights were Sunday 31 March 1901 and Sunday 2 April 1911. Absent members were left out unless they were out at work or travelling that night and came home on the Monday [S25], [S24]. A missing son or daughter is a lead to search elsewhere. Look as a visitor, boarder or servant (use the relation field), and in institutions.
- **Institutions have their own forms:** B3 shipping, C sick at home, D lunatics and idiots not in institutions, E workhouse, F hospital, G college and boarding school, H barracks (military, Royal Irish Constabulary and Metropolitan Police), I lunatics in institutions, and K prisons, bridewells and police stations [S5], [S19], [S24].
- **Search institutions by initials.** Inmates were often entered by initials only. Search the initials with age and sex (NAI's example: "M S, 25, female"), or open the institution's return. Then confirm on its age, county of birth and previous occupation [S22], [S24]. A presenter found an ancestor's wife, absent from her home, in a Waterford asylum's 1911 return [S8]. Grenham's 1901 search lists barracks, workhouses, asylums and other institutions by county, DED and townland [S1].
- **Search England and Wales on the same night.** England and Wales took their censuses on the same nights, 31 March 1901 and 2 April 1911 [S31]. An absence from an Irish household is a lead to search there.

## 5. Collect the whole form set and the neighbours

- **Open both sides of Form A.** The front lists the people. The back carries the address block (county, poor law union, DED, barony, parish, townland, street and house number), the head's name and the house's number on Form B [S25]. The NAI record links the front and back images and the townland's other forms [S27].
- **Find the house's row on Form B1** using the number on Form B. B1, the house and building return, gives for each house the walls and roof (permanent or perishable), number of rooms, windows in front, class of house (1st to 4th), number of families, the head of each family, rooms and persons per family, and the landholder on whose holding the house stood [S26]. Presenters use it to judge living conditions and to name the landlord [S9]. Follow the holding in the valuation records under B1's landholder entry. When the landholder is not the head, the house stood on someone else's holding.
- **Read B2 and N.** B2 lists the out-offices and farm-steadings attached to each house, such as stables and coach houses [S8], [S24]. N, the enumerator's abstract, gives the townland's houses, families, males, females and persons by religion, and the enumerator's name. It lists no names [S26]; the enumerator compiled it from B1 and the household returns [S25]. The names of the heads of family are on B1 [S25], [S26]: this is the list NAI describes as a name index for each area [S20]. Read the B1 head-of-family list for a household the name search missed, and check B1's house and population totals against N.
- **Walk the neighbours.** On NAI, use the breadcrumb to go back to the street or DED and open the adjoining households [S18]. Grenham's 1901 Form A pages have Previous and Next buttons and link B1, B2 and N from the same page [S1]. For a household near a townland edge, take the bordering townlands from townlands.ie [S14], [S32] and browse them on NAI.

## 6. Read ages under each year's rules

- **Ages are age at last birthday. Infants under one were given in months** [S25], so they have no age in years. In one presenter's 1901 example the transcription showed no age for a child under one [S7]. Drop the age filter when you search for a baby.
- **Read every older person's 1911 age as possibly inflated.** The Old Age Pensions Act 1908 paid a means-tested pension from age 70, from 1 January 1909 [S28]. No one born in Ireland before 1864 had a civil birth record to check against [S28], [S29]. People aged 70 and over rose from 187,315 in 1901 to 295,027 in 1911. In England, Wales and Scotland that group grew by about a fifth over the same decade. Ó Gráda estimates that one-third to two-fifths of those who claimed to be 70 or over in 1911 had not reached that age. Some kept their census age in line with a pension claim, and others raised it in case the census was later checked against one [S28], [S30]. A study of linked 1901–1911 returns found misreporting by people trying to qualify before 70, other exaggeration unrelated to the pension, and a sharp fall in round-number ages [S29].
- **Decision rule.** Flag every 1911 age of 60 or over. For a flagged person, expect a gain of more than ten years since 1901; the inflation is heaviest among those claiming 70 or over [S28]. Decide a 1901–1911 match on the other columns (step 8); the age gap alone neither rejects nor confirms it. Calculate a provisional birth range from each census age and fix the birth year from a civil birth or baptism record. Without one, take the 1901 range as the working birth estimate for a person claiming 70 or over in 1911, and report the 1911 range beside it [S28], [S29]. The shortcut of taking ten years off a 1911 age and looking in the same place in 1901 [S12] fails for exactly these people. Record each census age as the household's statement, never as a birth year [S8], [S10].

## 7. Read each column under its printed instruction

- **"Where born" is a county, city or country.** The instruction asks for the county or city if born in Ireland, otherwise the country [S25]. It never names a townland or parish of birth. Do not copy the residence townland into a birthplace field.
- **"Farmer" means an occupier of land.** The 1901 instructions restrict "farmer" to occupiers of land. The entry they give for sons and daughters working at home or on the farm is "farmer's son" or "farmer's daughter" [S25]. Read "farmer" as the occupier and "farmer's son" or "farmer's daughter" as a non-occupier on the family farm. A man of 40 entered as "farmer's son" is not the occupier. Take the holding to follow in the valuation records from B1's landholder entry (step 5).
- **A blank occupation for a woman is by instruction.** No entry was to be made for wives, daughters or other female relatives engaged only in domestic duties at home [S25]. Do not record it as a missing answer.
- **Read the relation column against the head.** Every relationship is stated to the head of family [S25]. A brother-in-law is the wife's brother or the husband of the head's sister; a sister-in-law is the wife's sister, the wife of the head's brother, or a married sister under her husband's surname. For a male head, an in-law entered as not married whose surname differs from the head's is the wife's sibling: search her marriage and baptism under that surname, as in the presenters' cases [S7], [S16]. For a married or widowed in-law, find his or her own marriage to settle the side before you use the surname. Staff can be kin too. Grenham found a shop assistant entered as the head's "cusion", who proved to be her second cousin [S4].
- **Note who wrote the form.** The head filled in and signed Form A. A head who could not write signed with a mark witnessed by the enumerator [S19], and the enumerator was to help households that could not fill in the form [S25]. Spellings on such a form are the writer's, not the family's. Read deletions on the image. One head entered his occupation as "Gentleman" and then struck it out [S6]. NAI now marks struck-through text in its transcripts with a code [S21], so check the image before you discard a coded entry.
- **Religion.** Members of Protestant churches were asked to name their denomination, not to write "Protestant" [S25]. A bare "Protestant" is the household's own vague answer. Search every Protestant denomination's registers for it.
- **Irish language.** The column says "Irish" for people who spoke only Irish, "Irish and English" for those who spoke both, and is blank otherwise [S25]. A marked household is a reason to search Irish name forms (step 2).
- **1911 married women.** Each married woman was asked the completed years of her present marriage, the children born alive to it and the children still living [S25], [S20]. Use the gap between the two counts to look for children who died young [S13]. Widows were not asked. Read the counts with the present-marriage rules in the UK census recipe. Check the image: NAI warns that some details, such as marriage duration, may be visible only on the original [S18].

## 8. Choose between same-named households on more than the name

- **A common surname can return thousands of entries in a single county.** A presenter counted more than 4,500 McGoverns in the 1911 census, about 2,000 of them in Cavan [S11]. Never pick a household on name, county and approximate age.
- **Link 1901 and 1911 as a pair.** Accept a match only when several of these agree: townland or street, children's forenames with ages rising by about ten, religion, county of birth, occupation, and B1 house details. A mismatch in religion or birthplace county is grounds to keep searching, not to reconcile [S7]. Record a different occupation in 1911 as a dated change, not a mismatch: a head can change work or retire in ten years.
- **Cite the place chain.** Record year, county, DED, poor law union, townland or street, and house number. One published citation gives the townland, DED, poor law union, county and household number [S15]. On the new NAI site each person has a stable record URL, but households have no URL of their own, and image links no longer expire [S27]. Cite a person's record URL and the image links.

## Close with a census packet

Return:

- **Search log:** each site and form used, the name forms, wildcards and swaps run, the fields filled, and the count of hits.
- **Coverage row per year:** whether the townland has online returns, any known gap (with the list or page consulted), and the place spellings used in each year.
- **Household record:** the literal transcription and your reading of the image side by side for each person, with Form A front and back, the B1 row (house class, rooms, landholder), B2 and N, and the neighbouring households and bordering townlands searched.
- **Age table:** the 1901 and 1911 ages, the birth range derived from each, and a flag on every 1911 age of 60 or over.
- **Absence leads:** institutions, other households and the England and Wales returns searched for anyone missing on census night.
- **Citation:** year, county, DED, poor law union, townland or street, house number, person record URL and image links.

Identity and kinship rulings go to evidence/proof judgment.
