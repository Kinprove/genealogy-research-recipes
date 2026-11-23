---
id: "tax-roll-observation-workflow"
title: "Read tax rolls as a liability-bounded annual series"
summary: "Read town, township or county tax lists as a liability-bounded annual series for each jurisdiction and tax type."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "TAX-ROLL-OBSERVATION-WORKFLOW-01", "text": "Check each year against the liability rules in force then, and record every change as a bounded interval."}]
handoff: []
checked: "2026-10-21"
checked_basis: "checked on 2026-10-21"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Record types in any country", "group": "Burials, directories, land and probate", "order": 209}
---

# Read tax rolls as a liability-bounded annual series

Use this when a person turns up in, or goes missing from, annual town, township or county tax lists, and someone wants to read a first appearance, last appearance or gap as a birth, coming of age, move or death. Read the lists as a series for each jurisdiction and each tax type. Check each year against the liability rules in force then, and record every change as a bounded interval. For the general rule that absence is not proof, use the [negative-evidence gate](evidence-proof-judgment.md). That recipe also covers Jr./Sr. namesake separation and every proof ruling. For judging directory gaps against a list's inclusion rule, use the [city-directory workflow](city-directory-observation-workflow.md). For using local lists to bridge 1890, use [census workflows](us-census-practical-workflows.md). For AI abstracts that call amounts "wealth", use [AI for documentary records](ai-for-documentary-records.md).

## Contents

- 1\. Build the series register before reading any entry
- 2\. Record the liability scope for each year before interpreting
- 3\. Search each tax series separately
- 4\. Learn how the volume is arranged before browsing
- 5\. Extract one row per entry
- 6\. Turn appearances into intervals, then test them
- 7\. Close with a tax-series packet

## 1. Build the series register before reading any entry

Make one row for each combination of jurisdiction (town, township or county), tax type (land, personal property, poll/tithable, other) and year. Give every cell one status:

- **inspected – hit**
- **inspected – no hit**
- **list not surviving**
- **not inspected**

Compare the years in the online set with the archive's series guide. A search in New Garden, Chester County, jumped from 1838 to 1875 [S15]. Mark 1839–1874 uninspected in that set. The county archive's digital guide lists provincial taxes as early as 1715 and includes 1871–1900 under County Taxes, RG2040.003 [S60]. Check the township in those additional rolls before logging a miss. Even an inspected tax list covers only the people liable in that place and year [S9].

A name index is also a finding aid, not an inspection. FamilySearch's "Texas, County Tax Rolls, 1837–1910" indexes only selected years: the first year before 1845, then 1845, 1855, 1865, 1875, 1885, 1890, 1895 and 1905. It covers 231 of 254 counties and is about 13% complete. A miss in an index like that is "not inspected" for the year and county concerned. It becomes "inspected – no hit" only after you have read the images. Treat a list you find through a county guide or an abstract card the same way: record it as a finding aid, not as the inspected list [S16].

Use MyHeritage's *England and Wales, Hearth Tax, 1662–1674* index for household-head names and residence dates and places [S47 @2026-11-18], [S49 @2026-11-18]. Check the collection's county list before searching. Pembrokeshire is the only Welsh county listed [S49 @2026-11-18].

Use MyHeritage's Chester County septennial census index for name and residence leads from 1793 to 1863 [S50 @2026-11-18], [S52 @2026-11-18]. Consult the Chester County Archives' missing-township list for the target township and enumeration year before interpreting an index miss [S51 @2026-11-18], [S58 @2026-11-18].

If MyHeritage's *Pennsylvania, Chester County Tax Registrations, 1715–1890* opens in the user's account, use it for the name, year, place and property size when indexed [S70 @2026-11-21]. Check the township and year against the county's tax series. Use the Chester County Archives' 18th-century tax indexes and 19th-century assessment guide as alternate routes [S71 @2026-11-21], [S72 @2026-11-21]. Keep this search separate from the septennial census and leave gaps open until the underlying rolls are inspected.

For a deceased person in Finland, search the matching MyHeritage *Finland, Population Tax Lists* collection for 1890 [S78 @2026-11-21], 1900 [S79 @2026-11-21] or 1910 [S80 @2026-11-21]. Record the name, birth year, household relationships and residence when given [S77 @2026-11-21], [S78 @2026-11-21], [S79 @2026-11-21], [S80 @2026-11-21]. For intervening years or a missed index entry, look up the *henkikirjat* by province and year in the National Archives of Finland's Astia catalogue [S81 @2026-11-21]. Leave the interval open until the relevant annual rolls have been inspected.

Search MyHeritage's *Hungary, Property Tax Census, 1828 From JewishGen* by given name, surname and place [S64 @2026-11-20]. Search with the 1828 Hungarian place names and record both town and county from the hit [S63 @2026-11-20], [S64 @2026-11-20].

Leave residence unresolved after a miss in this index. JewishGen extracted entries identified as Jewish or judged likely to be Jewish from a census limited to people with taxable property [S65]. Use the town and county to locate the original return. For a JewishGen hit, use its microfilm and entry numbers to find the census line [S65].

For a place now in Highland County, Virginia, identify which county covered it before Highland was formed in 1847, then search the personal-property tax lists for Pendleton (now in West Virginia) or Bath accordingly [S69].

For Highland County's 1847–1850 personal-property tax lists, open FamilySearch Catalog entry 776302 (film 2024589, DGS 8707155) [S67 @2026-11-20]. Check **Film/Digital Notes** in the user's signed-in account and use the camera if it opens the images [S66 @2026-11-20], [S67 @2026-11-20]. If the images are unavailable, use Library of Virginia reel 177 for those years [S68 @2026-11-20].

Treat 1850 as the end of that catalog entry and continue with the Library of Virginia's Highland County microfilm, starting with reel 574 for 1851–1854 [S67 @2026-11-20], [S68 @2026-11-20].

### The 1787 Census of Virginia: index to tax lists

Use volume 3 of *The 1787 Census of Virginia* as the index to the compiled personal-property tax lists [S82], [S83]. For a search in one county, look for its separately published edition, including under the county's historical Virginia name if it is now in West Virginia [S82], [S84]. Cite the underlying personal-property tax list and its actual year. Read the county edition's introduction and headings before assigning a year. The Monongalia County edition contains lists for 1786 and 1788 alongside a partial 1787 list [S84]. Keep each list in its own year in the series register.

For Loudoun County, check the separately published editions for 1787, 1788 and 1789 [S82 @2026-11-21], [S85 @2026-11-21], [S98 @2026-11-21]. For the original rolls for all three years, use Library of Virginia reel 208 (1787–1797) [S86 @2026-11-21].

## 2. Record the liability scope for each year before interpreting

For each jurisdiction and year, write down who was liable and for what:

- the tax types
- the age band
- sex, race or status categories
- property thresholds
- named exemptions (for example ministers, or men above an upper age limit)

Take this from, in order of preference:

1. the list's preamble or column headings, which can state who and what was taxed and the age range [S1]
2. the session statutes in force for that place and year, for taxable ages, taxable property, exemptions and form layout [S2], [S3]
3. a published tax-law summary for that jurisdiction, used to identify the legislation for the list's year [S3]
4. an archivist at the state archives [S6]

If the statute book gives no assessment rate, search contemporary newspapers for it [S2]. When columns or check marks have no headings, do not guess what they taxed. Find the governing law first [S3].

To test whether a Virginia county taxed males aged 16–21 after 1783, do not stop at the state statutes: read that county court's order books, where county levies can appear [S26], [S32]. Section IX of the May 1783 act left county courts free to list free male tithables of those ages and tax them for county or parish levies, but it does not require a specific order, and clerks varied [S26], [S33]. An order found shows the county levied the tax; no order found leaves the county's practice undetermined [S26], [S33].

Verify the poll-tax age for the jurisdiction, period and person's category [S6]. The State Library of North Carolina's table lists free men aged 21 and over in 1784, 21–50 in 1801 and 21–45 in 1817 [S61]. Section 8 of the Republic of Texas act of 12 June 1837 specified white males aged 21 to 55 [S62]. Cite the applicable rule, or mark the age range **not determined**.

For Virginia colonial tithables, do not assume a minimum age of 21 or a white-male-only rule: the March 1642/3 law set 16 for youths and also named Black women at 16, and 16 continued for white males through the October 1748 act [S26], [S27], [S28]. A state poll tax at 21 was levied by October 1777 and the November 1781 act taxed free males above 21, but the Library of Virginia says counties could still choose to tax everyone over 16 in 1782–1787 [S29], [S30], [S31].

Do not read homestead land as permanently exempt, as one community post implies [S43]. Land entered under the federal land laws could not be taxed by the state or county until the entrant had a perfect equity, at final proof and payment, or until the patent issued, so a homestead or other unpatented entry can be missing from the county land roll for years after settlement [S42]. In *Duncan v. Newcomer* (1896), the South Dakota Supreme Court held a homestead untaxable until the settler's final proof, and cited the rule that land became taxable after entry, payment and final certificate, before the patent [S42]. Check the land-office entry, final-proof and patent dates before you read a settler's absence from the land roll.

For a household missing from a hearth-tax payment list, test whether it was exempt [S47]. Look for a non-chargeable entry or an exemption certificate for the place and term. Check the grounds in force, including whether the householder was excused from church and poor rates because of limited means or met the applicable rent and property limits [S48].

For a free Black woman on a colonial Virginia tithables list, check the law in force before assigning liability. The Just Genealogy presenter reports that free women of color could be liable in Virginia [S53]. The September 1668 act confirmed that Black women who had been freed remained liable [S56].

### Virginia Specific Tax: identify the act before reading a payment

Use the list heading, levy year and payment terms to identify the act. For a Virginia payment dated 1782, check whether it belongs with the November 1781 commodity levy, a land assessment or a personal-property assessment [S88], [S94], [S96], [S97]. The personal-property tax could also be paid with receipts for specified commodities, including tobacco, hemp or flour. The land tax had its own payment terms [S96]. Keep each payment with the assessment named in the record.

Under the May 1779 act, check liability for men over 16 and enslaved women over 16. Look for a county court discharge from the levy or a tax commissioner's finding of incapacity for work due to age or infirmity [S88], [S89]. Read the payment alternatives per taxable person as 1 bushel of wheat, 2 bushels of Indian corn, rye or barley, 10 pecks of oats, 15 pounds of hemp, or transfer notes for 28 pounds of inspected tobacco. Check the deficiency account for shortfalls charged in money [S89].

Separate the original schedule, March 1780 and the four succeeding years, from the date of a receipt [S89]. Keep the 1779 tax in scope after 31 December 1780. The October 1780 act expressly spared the specific taxes from the discontinuance [S88], [S90].

For a late payment under the May 1779 act, check the extensions for delinquents to 1 October 1780 and then 1 March 1781 [S88], [S91], [S92]. In counties with grain still uncollected, check the further extension to 1 August 1781. The May 1781 act treated militia service as a cause of delayed collection [S87], [S93]. For a taxpayer away on military service, check the applicable act for an extension or exemption before treating the absence as a change in liability [S87], [S93].

For the November 1781 levy, check the grain charge on free men over 21 and enslaved people over 16, with county court exemptions for age or infirmity. Check the bacon clause separately for free persons over 21 and enslaved people over 16 [S88], [S94]. The act calls for 2 pounds of bacon plus one of the listed grain options. Use ½ bushel of wheat, 1 bushel of Indian corn, rye or barley, or 5 pecks of oats. The optional coin rates were 3 shillings per bushel of wheat and 6 pence per pound of bacon [S94].

Distinguish the November 1781 act's collection and reporting dates. Commissioners were to list deficiencies on 1 May 1782 and report to the executive by 1 June. May 1782 legislation then allowed payment in commodities before 1 September [S88], [S94], [S95]. Apply the separate extension to 1 April 1782 to sheriffs' and collectors' accounts for taxes already due for 1781 [S94]. Keep the levy and the payment or return date in separate fields.

## 3. Search each tax series separately

Search the land series and the personal-property or poll series separately, and keep a separate register for each. A man without land can still appear on a personal-property list as a single taxable poll or because of a taxable item such as a horse or a watch [S5]. On Virginia lists, horses were taxed from 1782 and watches had their own columns in the 1850s.

Search the federal internal revenue assessment lists as a series of their own. The National Archives' filmed lists (Record Group 58) are mostly for 1862–1866; only Arizona, Arkansas, Colorado, Idaho, Montana, New Mexico, Oregon and Wyoming have later years, up to 1874 or beyond [S36 @2026-11-14]. Ancestry titles its collection "U.S. IRS Tax Assessment Lists, 1862-1918", so do not take the title as its coverage; the National Archives names Ancestry, by subscription or free at its own facilities, and FamilySearch, free, as hosts of the filmed lists [S36 @2026-11-14], [S37 @2026-11-14], [S38 @2026-11-14]. The lists are arranged by state, collection district and division, and a division generally corresponds to a county, so find where the person lived first [S37 @2026-11-14]. Lists from 1867 on are at the National Archives facility that holds the state's federal records; some states, such as Ohio, Wisconsin and Massachusetts, were never filmed, and their 1862–1866 lists are at the National Archives at Kansas City [S37 @2026-11-14]. Mark a year or place outside the filmed coverage "not inspected", not "inspected – no hit".

On Virginia personal-property lists, enslaved people were taxed under the enslaver. The presenter describes them as listed by first name, in age groups that varied by county [S5]. The Library of Virginia's guide narrows this. Names appear only on the 1782–1786 lists, and later lists give counts. The age categories (above or below 16, with a 12–16 band in later years) were set by state statute and changed over time; they did not vary by county. Do not expect names on lists after 1786. Record the counts and age categories exactly as the list in hand gives them.

In seventeenth- and eighteenth-century Virginia records, read "tithable" as a person who paid one of the taxes imposed by the General Assembly, or for whom someone else paid it, and do not assume each tithable paid personally; enslavers, for example, paid the taxes levied on their enslaved workers and servants [S26], [S34], [S35]. The tax was laid by law, so do not read a tithable as a voluntary church tithe-payer [S34].

In Pennsylvania township lists, "inmates" are renters or lodgers on someone else's land who were taxed on personal property. They are not prisoners. Exact definitions vary by county and period [S4], so record which section of the list each entry is in. The same presenter says Pennsylvania taxed some personal property, such as cattle and horses, up to the 1840s. Livestock appears on county lists from the 1780s and 1790s. For later years, take livestock liability from the list's column headings or the assessment law for that year, not from the 1840s date [S4].

For Chester County, compare the index's *Property holder type* with the original roll. Under the county archive's 18th-century categories, *Landholder* includes people holding land by lease or deed, *Inmate* denotes a landless contract laborer who was married or widowed, and *Nonresident Landowner* points to unoccupied land [S70], [S71]. Check for a lease before inferring deed ownership, and keep the parcel's location separate from the owner's residence. An early inmate can be listed among landholders, so check the roll's grouping before assigning a status [S71].

For a Chester County entry labelled *Freeman*, check the year and heading before inferring age or marital status. The county guide defines the 18th-century category, from 1718, as single free men at least 21 who had been out of servitude or apprenticeship for at least six months [S70], [S71]. Check the roll for the category before interpreting a miss. Assessment of freemen was uneven, and later 19th-century rolls replaced *Freeman* and *Inmate* with broader divisions [S71], [S72].

A land-tax entry in a person's own name shows that the person had a taxable interest in land there; it does not show that they lived there [S41]. An entry that names someone as agent, guardian or administrator records that capacity for another's land, not that person's own interest: record the capacity and keep the representative apart from the assessed owner, as in the McClure entries in section 5. Many rolls listed non-residents' land separately: Texas county rolls often carry a heading for property in the county owned by non-residents, and Mississippi kept non-resident land tax lists from 1844 to 1895 [S39], [S40]. Record which section an entry is in. For an owner who may not have lived there, test the alternatives Genealogy Tip of the Day names, land speculation, a former residence, inherited land and military bounty land, before you place them in the county [S41].

Read a Pennsylvania septennial census as a seven-year enumeration of taxable inhabitants first authorized in 1779 [S50], [S51]. Look for the person's name, township and occupation in the return [S51], [S59]. Treat an absence as a residence clue only after verifying that the inclusion rule for that enumeration covered the person [S51].

## 4. Learn how the volume is arranged before browsing

Use the volume's headings and a contemporary township/range map to find the sequence before browsing. Chester Ward's 1845 Genesee County, Michigan, entry was in section 2, township 8, range 7 [S2]. Check the next headings to establish which direction this particular roll runs. For a Pennsylvania list arranged by township, locate the family's land first [S16].

Treat names next to each other as neighbour candidates only if you have shown the list follows a geographic or assessor-visit order. Alphabetical, letter-grouped or recopied lists say nothing about who lived next to whom. In a letter-grouped list, read the whole letter block before you record "inspected – no hit". Write the arrangement you found into the register.

Treat an alphabetical list as a probable recopy. Some tax lists were rewritten in alphabetical order, which loses the original order [S38], and Genealogy Tip of the Day warns that copying a list into alphabetical order could introduce transcription errors [S44]. Look for the earlier list in its original order, or a duplicate, and check doubtful entries against it.

### Swedish mantalslängder: enter by parish and year

When a parish is known from church records but the tax archive uses unfamiliar administrative divisions, look for a parish/year contents index rather than guessing the tax district. ArkivDigital's 7 February 2024 demonstration used *Innehållsförteckningar till mantalslängder* to reach the parish's section of the original roll [S25]. This is a contents index, not a person index.

1. Fix the parish and bounded years from the household research. In the demonstrated route, choose the tax-roll contents index under register search, enter the parish and year range, and inspect the returned roll references. Locate the corresponding finding aid in the current service; the demonstration does not guarantee today's menu or coverage.
2. List every roll returned for the same parish and year. An ArkivDigital contents search yielded two rolls for a single year [S25]. Keep the archive, volume, stated year and parish-section locator for each until its images establish what it covers.
3. Follow the image link to the original roll and verify its parish heading and year. Then locate the recorded farm or residence within that section. The contents hit establishes a browsing entry point; it does not establish that the household is present.
4. Check the first page for the original column key before interpreting ticks or counts [S25]. Record the heading and its locator with that year's entries. Where a label stays unreadable, leave the column unresolved.
5. Repeat for the next inspected year, retaining the same farm/residence clue alongside the names, household categories and counts actually recorded. Recheck headings and liability rules rather than carrying a column meaning or age threshold across years automatically.
6. Apply the interval and competing-explanation checks below. The presenter describes annual farm tracking and warns that a child's appearance can reflect the applicable taxable age, while an adult's disappearance can reflect exemption from tax [S25]. Neither change dates a birth or death. A missing or uninspected roll remains a gap in the chain.

**Return:** a parish/year-to-roll crosswalk with one row per candidate volume, the verified parish-section and farm locators, the heading reference, inspection status and linked annual observations. Keep an unresolved tax district or column meaning explicit. This route does not establish a universal Swedish tax age, exemption rule, complete household roster or survival of the requested years.

### Stockholm mantalsregister: match the index to the annual roll

Use MyHeritage's *Sweden, Stockholm Census Registers, 1800–1884* for a name and residence lead [S70 @2026-11-21], [S73 @2026-11-21]. For a man in 1909, use *Sweden, Stockholm Census Register of Males, 1909* and record the birth date when given along with the residence [S70 @2026-11-21], [S74 @2026-11-21]. For a female target in 1909, go directly to the annual roll. Find the property in the *mantalslängd*, series G 1 BA, through the Stockholm City Archives' guide to Riksarkivet's *Mantals- och kronotaxeringslängder Stockholm stad* search [S76 @2026-11-21].

Keep the year on the household declaration (*mantalsuppgift*) separate from the year of the roll. Household heads submitted declarations to the tax authority, and Stockholm's Governor's Office used them to compile the following year's roll [S70], [S75]. Read the property entry for the household members actually listed, including people other than the declarant [S76]. Keep a person-index miss open until the roll and its inclusion rules have been checked.

## 5. Extract one row per entry

Name every column from its heading before you read its values: a sum of money, arrears, an age, a household or list number, a count of polls or animals. A number beside a name is not an age until a heading says it is one, and a column without a heading stays unread until the list's preamble or the governing law explains it (step 2). Keep the literal heading with the values. If a column gives ages, take the date they are reckoned from out of its heading, not from the year on the volume's label; if the heading leaves that date open, record no birth year from those ages.

Read *chimney money* in England and Wales as the hearth tax introduced in 1662 and assessed per hearth or stove [S47], [S48]. Its two equal installments fell due at Lady Day (25 March) and Michaelmas (29 September) [S47], [S48]. Record the stated collection term as well as the year and keep the two terms separate in the series register.

Transcribe *LF* before expanding the abbreviation. In the 1813 Charlotte County, Virginia, transcription, Peggy Bird's entry includes an explicit gloss of *Lf* as *levy free* [S54]. Where an exemption could be granted individually, check the county order book [S53]. The St. Peter's Parish vestry recorded Peter Maye presenting a court order for levy-free status [S55]. Cite the minute as evidence he produced it, and look for the order itself to establish its date and scope.

If a Virginia tithables list names an overseer, record that capacity alongside the enslaved people listed and the person charged with the levy. The Just Genealogy presenter reports that an overseer could be involved in the levy [S53]. Under Virginia's October 1748 act, an overseer could file the list for an absent or nonresident owner, who still owed the levy on tithables the overseer failed to list [S57].

For each entry, keep:

- the literal name form and any Jr./Sr. designation, as written; it describes the entry and is not a parent–child link [S14]
- the capacity, exactly as written: *agent for*, *guardian for heirs of*, *administrator of*, *estate of*, *widow* [S12], [S7], [S11]
- the parcel details: acreage, section/range or location, valuation, and any named original grantee or owner [S12], [S14]
- any paid or delinquent mark, plus the list section (land, personal, inmates, poll)
- the image or volume locator

Trace changes in capacity on the same tract back from the last identified taxpayer. In Rusk County, Texas, the 400-acre tract links entries under different names [S12]. Read the following observations in date order and keep years without an inspected roll open.

- In 1850–1852 James McClure was taxed on 400 acres. The 1850 entry names James as original owner, while 1851–1852 name James M. Johnson [S12].
- In 1853 Susan McClure appears with matching property. In 1854 S. W. McClure, administrator of “J.” McClure, appears below F. M. McClure [S12].
- In 1855 F. M. McClure is guardian for the heirs of McClure. The 1859 roll identifies Francis M. McClure as an agent and the 1860 entry names F. M. McClure [S12]. Check probate and deeds before equating the taxpayers, the decedent or their relationships.

Link the years through the repeated tract description, because the name and capacity change from year to year. Then trace an unusual acreage in deeds, where a nominal sale price is a lead and not proof of kinship [S14].

Check the end of each roll for a delinquent addendum, and check contemporary newspapers for published delinquent lists. If you find nothing there, record it as an inspected result. It is not proof of payment.

## 6. Turn appearances into intervals, then test them

Record each change for one series as **last year present → first year absent**, or **last year absent → first year present**. A single date is not an observation. Then classify each non-appearance:

- **not liable** (outside the documented scope that year)
- **scope not determined**
- **list missing or not inspected**
- **candidate move, death or exemption**

Moving away, death and ageing out of liability are competing explanations for someone dropping off a run of lists [S17], [S7], [S11], [S23]. Not appearing does not show that the person had left the area or was avoiding the tax. He may simply have met an exemption [S1], [S6], [S9].

Test the candidates against other records:

- If the family stays on the roll on the same land, favour death in place over removal [S13]. A later *widow* entry [S11], an *estate of* entry [S7], or the tract passing to an administrator or heir, as in the Rusk County sequence, strengthens that reading.
- Probate, court, jury and deed activity: buying or selling land after the gap rules out death in the gap [S7].
- Census presence [S13].
- The next jurisdiction, for a candidate move [S20], [S19].

Bound a change by the last inspected roll on one side and the first inspected roll on the other [S18], [S20]. Two consecutive inspected annual rolls give an interval of about a year. Missing or uninspected years widen it. A Rhode Island-to-New York move was reportedly narrowed using monthly town lists [S20]. Use a month-level interval only if your series register identifies the two inspected monthly rolls and their actual dates.

A son's first entry as a separate taxpayer is a bounded clue to his coming of age or to a separate household [S18]. It is not an exact birthday. If you estimate a birth year from a liability age, give a range and cite the specific rule you used [S8]. Without a documented age band, give no estimate. Same-surname men taxed next to an older householder are only candidate sons. Send them, and every identity question, to [evidence/proof judgment](evidence-proof-judgment.md).

Before treating a county hit in *The 1787 Census of Virginia* as the only candidate, use volume 3 to collect same-name entries across the compilation [S83], [S87]. Compare their county, actual roll year and entry fields. Limit any uniqueness conclusion to the lists the compilation covers.

Where a list names a head of household and counts the taxables under him, track the count as well as the names. On Virginia and North Carolina tithable lists, the person responsible for a family's tax was listed with the names or the number of the taxable persons for whom he paid, sons over 16 among them, while a free male of 21 or over was responsible for his own tax and should be listed separately [S45]. A rise in the head's count is therefore a second bounded clue that a son may have reached the lower taxable age, before his own entry appears [S43], [S45]. Record both changes as intervals against the age band documented for that place and year.

To find candidate fathers for a man whose parents are unknown, list every taxpayer with his surname or a variant in the place where he came of age, over a run of years around his first appearance [S38]. On Kentucky lists, a son who had turned 21 was usually listed with his father [S46]. Treat each older same-surname man only as a candidate, and test him in other records.

On Virginia personal-property lists from the May 1783 act (in force 1 July 1783) to the 1793 change, do not read a first listing as age 21 without checking that county's practice, because county courts could still list free male tithables aged 16–21 for county or parish levies [S26], [S33]. The Library of Virginia gives 21 as the taxable age for 1782–1787, with counties able to tax everyone over 16, and 16 as the taxable age statewide from 1793, so from that year test a first listing against 16, with no county-by-county inquiry [S31].

## 7. Close with a tax-series packet

Return:

- the series register (jurisdiction × tax type × year × status), with the arrangement you found and any index coverage limits
- the cited liability scope for each year, or "not determined"
- the per-entry rows with literal fields and capacity notations
- the interval list, with competing explanations and the records that test them
- neighbour or relative candidates, labelled with the list order they rest on
- follow-up leads: deeds, probate, delinquent lists, uninspected years, the next jurisdiction

Do not turn an interval into a death date, move date or birth date in the packet.
