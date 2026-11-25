---
id: "us-vital-registration-coverage"
title: "Build a U.S. vital-registration coverage register before calling a birth or death record missing"
summary: "List every U.S. birth and death registration authority and series before calling a record missing."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "US-VITAL-REGISTRATION-COVERAGE-01", "text": "The usual mistake is to treat the statewide mandate year as the first year of coverage, search one certificate index for one county, and report a negative. Before any absence statement, build a register with one row for each registration authority and each separate series."}]
handoff: []
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request", "third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "United States: people, vital and church records", "order": 238}
---

# Build a U.S. vital-registration coverage register before calling a birth or death record missing

Use this recipe when a U.S. birth or death search has failed and someone is about to write "no record exists". The usual mistake is to treat the statewide mandate year as the first year of coverage, search one certificate index for one county, and report a negative. Before any absence statement, build a register with one row for each registration authority and each separate series.

General negative-evidence rules are in [evidence/proof judgment § Negative-evidence gate](evidence-proof-judgment.md). How to weigh a delayed certificate as a late claim is in the same evidence/proof judgment recipe. Locality-wide search lines are in [research documentation](research-documentation.md). For browsing catalogued film that has no index, see [FamilySearch record workflows](familysearch-practical-record-workflows.md). A delayed certificate's filing date is not the birth date.

## Contents

- List every authority that could have registered the event
- Split each authority into its separate series
- Record custodians, access and copy fidelity for each series
- Widen the places searched before recording a miss
- Retry a birth search without the expected given name
- Treat a delayed certificate as a set of leads
- Report coverage as a table, not a verdict

## List every authority that could have registered the event

For the event date and every candidate place, make one row for each body that may have registered births or deaths. Give each row its own start date.

- **City boards or bureaus of health.** Cities often registered during years when their county or state did not. In Pennsylvania, counties registered births and deaths through the Register of Wills from about 1852 to 1854/55 and again from 1893 to 1905. Several city bureaus of health registered in the gap between those two periods [S7], [S6]. Pittsburgh's Bureau of Health has separate series: death indexes for 1851–1857 and 1870–1899, birth registers for 1870–1905 and death registers for 1870–1897 (Pennsylvania State Archives). Give each series its own row. The presenter gives Reading as 1874 and Allentown and Scranton as about 1873–1874 [S7], [S6]. Allentown 1873 is supported elsewhere. For Reading, a published research plan lists deaths from 1873 and births from 1876, so give its two series separate start dates. For Scranton, the only date found is deaths from 1878, so treat the presenter's Scranton date as unconfirmed. In North Carolina, Raleigh kept city records from 1885 and Wilmington from 1903, both before statewide registration began in October 1913 [S4].
- **New York City.** The state does not file births and deaths that occurred in New York City, so New York State statewide indexes do not cover the five boroughs as part of the city. The state does hold some pre-1898 records from Queens and Richmond towns, for example 1881–1897 [S12]. Historical city certificates are at the NYC Municipal Archives, with images online at a860-historicalvitalrecords.nyc.gov. Take each borough series' date range from the Archives' list of holdings [S11]. Bronx, Queens and Richmond borough series start in 1898. For Bronx areas annexed earlier (1874 and 1895), search the Manhattan records. For pre-1898 Queens and Richmond events, search the separate town and village series (1847–1849 and 1881–1897) and Long Island City (1871–1897) [S11]. Give city, state and each borough series their own rows and start years.
- **Independent cities.** These sit outside any county and often have their own courthouse. Their records may be held in the city or at a county courthouse [S4]. Virginia has 38 independent cities.
- **The county.** The register of deeds, the courthouse or the county archives may hold births and deaths from before the state level began [S4]. Some counties, like Pennsylvania's, registered in separate periods with gaps between them. Give each period its own row.
- **The state mandate.** Treat this as the start of one series, not the start of all coverage. Mandate years differ from state to state, and some states had an earlier state series that stopped. Virginia's state registers cover 1853–1896, and statewide registration started again in 1912 [S4]. Utah's statewide registration began in 1905 [S1]. Illinois statewide registration began on 1 January 1916 [S3].
- **Mandate is not compliance.** Many births in the years just after a mandate were never registered. In Cook County, many people born in the late 19th century and the first two decades of the 20th never had a certificate and later filed delayed births [S3]. Treat the first years after a mandate as partial coverage and always add a delayed-birth row for them [S2]. Record, as a separate coverage marker, the year the state was admitted to the federal Death Registration Area (formally set up in 1900) or Birth Registration Area (set up in 1915). Admission required registration to be about 90% complete, and both areas covered every state by 1933 [S13].

- **Hawaiʻi birth records.** Do not turn the Department of Health's 1896 start into the beginning of all birth records. Reporting laws began in 1842 and earlier records survive unevenly by island; give those series separate rows. Also search delayed-certificate applications made in 1911–1972 for births before 1911 [S22 @2026-11-17].

- **Utah deaths.** Search county-clerk death registers from 1898 separately from statewide certificates from 1905. Some Utah cities registered deaths before 1898 [S23], [S24].

For New York City before 1898, the Municipal Archives' list of holdings adds two points to the New York City item above. For a Bronx area annexed before 1898, search the Manhattan records only for events from the date of annexation through 1897. The Archives also holds separate marriage and death records for Kings County towns: Flatbush, 1847–1851 and 1880–1894; Flatlands, 1880–1895; Gravesend, 1880–1894; New Lots, 1881–1886; and New Utrecht, 1880–1894 [S11 @2026-11-13]. Give each town's series its own row.

For a birth near the Arizona statehood transition, start the territorial registration row in 1909 and check county coverage for the event year. For an early New Mexico death, give FamilySearch’s *New Mexico, Deaths, 1889–1945* its own index row and identify the county, church or other source behind any entry from before statewide registration. In western New Mexico or eastern Arizona, check the New Mexico State Records Center & Archives’ guide to the Diocese of Gallup’s sacramental microfilm for the locality and year [S80 @2026-11-22], [S81 @2026-11-22], [S82 @2026-11-22], [S83 @2026-11-22].

Mark each start date as either `verified` (and name the authority you checked) or `presenter-reported`. Re-check any presenter-reported date with the state archives or the vital-records office before you rely on it. Do not extend one state's arrangement to another state.

Consolidations change what a name refers to. The city and county of Philadelphia merged under the Act of 2 February 1854, and the city took over the county's boundaries [S7], [S6]. A "Philadelphia" record from before 1854 may therefore come from the old small city, a borough or a township. Set the authority to match the event date, not today's map.

For a pre-1800 U.S. birth or death, check surviving town records for the jurisdiction at the time. If no town series covers the event, add separate rows for the family's church or synagogue registers and check the relevant birth, baptism or burial entries. Use published genealogies to identify the town, congregation or record to search [S78], [S79].

**California.** For births and deaths before 1 July 1905, start with the county recorder for the place of the event. Check that county's dates in FamilySearch's *California, County Birth and Death Records, 1800–1994*. The collection omits San Francisco and its death name index covers only selected localities. Browse county images where available. Give the state filing series from July 1905 its own row [S39 @2026-11-20], [S40 @2026-11-20], [S41 @2026-11-20].

**San Francisco.** Mark the April 1906 earthquake and fire as a loss of local coverage. For a death before the fire, check the California Genealogical Society's list of surviving death ledgers against the event month and year. For a birth or death from July 1905 to the fire, give the state series its own search. Add newspaper notices and, for deaths, surviving cemetery and mortuary records as separate leads [S39 @2026-11-20], [S44 @2026-11-20], [S40 @2026-11-20].

**Ohio.** Give the county probate court ledgers from 1867 through 19 December 1908 and the state-format certificates from 20 December 1908 separate rows. The 1867 law required county recording, and some births and deaths still went unreported. Record a ledger miss against that county and period [S47], [S48], [S49].

**Connecticut.** Check post-Revolutionary War town birth and death coverage by town and event. According to the chapter, town recording declined after the war [S62† @2026-11-20], [S65 @2026-11-20]. Log the 1848 start of the state's statistical reports as a separate marker [S70 @2026-11-20]. Check the Connecticut State Archives' *Vital Records circa 1850–1900* for the towns and years represented there [S66 @2026-11-20].

## Split each authority into its separate series

A miss in one series tells you nothing about the others. Under each authority, list:

1. **The chronological register and the individual certificates as separate rows.** Cook County has register books with entries in date order (1871–1915) and individually issued certificates (from 1871). FamilySearch indexes them as separate collections. Some people appear in both, and others in only one [S3]. State-level registration in Illinois began in 1916, and many births before then have no certificate [S3]. A miss in the certificate index before 1916 is weak evidence until the register and the delayed births have also been searched [S3].
2. **Delayed-birth filings.** These cover people born before the mandate, and also people born just after it whose birth was never registered at the time. Ask the county to search for an application rather than assuming none was made [S9], [S2]. The Cook County presenter says its delayed births have been digitized but are usually not online, and puts this down to a county restriction she could not explain [S3]. This has not been confirmed. Ask the Cook County Clerk, and read the FamilySearch collection description for what it includes.
3. **Midwives' and physicians' registers.** These are not government-produced records and may be the only record of a birth or death. For Utah, the presenter says many were filmed and catalogued at the Family History Library under Utah, then the county, then Vital Records [S1]. Check the same catalog heading for whatever state you are working in.
4. **Institutional and supplemental series.** A Philadelphia City Archives representative says the Archives holds births from the almshouse and from Philadelphia General Hospital alongside the official city births [S8]. The Archives' record-group list includes Blockley Almshouse and Philadelphia General Hospital, but it has not been confirmed that a separate births series exists within them.
5. **Ledgers and group registers.** Some original city records are weekly group lists of who was born or buried, not individual certificates [S8]. Philadelphia deaths before July 1860 survive as cemetery (burial) returns, and death records are filed by cemetery [S8], [S10]. Search these as registers, not as certificate indexes.

For Nebraska births in 1904–1911, look for the ledger entry under the father's name. The state usually filed these births under his name alone and omitted the child's name. Give birth certificates their own row starting in 1912 [S30 @2026-11-18]. Use the Father fields in MyHeritage's Nebraska Births index for this period and check the ledger image if it accompanies the hit [S27 @2026-11-18], [S29 @2026-11-18].

## Record custodians, access and copy fidelity for each series

For each series, list every possible holder:

- city hall or a city archive
- county office or courthouse
- a local library
- state archives, state library or state historical society
- a county or local genealogical or historical society, which may have compiled the only index [S7]
- FamilySearch, Ancestry, Findmypast and MyHeritage. The presenter says each has contracts with archives and often carries different collections, so check all four [S4], [S7].

If municipal registers precede statewide registration, search the city and the state catalogue levels and compare their series and coverage. In Raleigh, a call to the city pointed Lefler to a local library and the state archives; the FamilySearch state-level catalogue also identified city records [S4 @2026-11-19]. Wake County's catalogue lists microfilm at the Olivia Raney Local History Library for Raleigh births, 1890–1938 [S36 @2026-11-19], and deaths, 1887–1937 [S37 @2026-11-19]. Use the register for the event year and log each copy's holder.

For each holder, record:

- **Index status:** indexed, or browse-only. Unindexed film under the county catalog listing can still be browsed image by image, and a society index can point you to the right frame [S7].
- **Access limits:** check the current rule with the vital-records office. Utah's Office of Vital Records page, checked 2026-11-07, makes birth records public after 100 years and death records after 50 years. [S19] Those are the correcting source's limits; do not repeat the presenter's 75-year figure [S1] for births or deaths. For Cook County delayed births, the only report of a restriction comes from the presenter [S3].
- **Whether the online copy matches the custodian's originals.** The Philadelphia City Archives holds births and deaths from July 1860 to June 1915, marriages only from July 1860 to December 1885, and cemetery returns from 1803 to June 1860. Marriages after 1885 are with the Orphans' Court / Register of Wills. The presenter and the Archives representative gave marriages through 1915 and "deaths" from 1803 [S8], [S10]. Correct both before you build the rows. The representative also said she could not confirm which of these holdings appear on FamilySearch or Ancestry [S8]. In Utah, most county registers have been transferred to the Utah State Archives and some remain with the counties [S1]. For example, Salt Lake County's hard copy went back to its county archives.

If the ordering office is unclear, use the National Center for Health Statistics’ *Where to Write for Vital Records*. Select the jurisdiction where the event occurred, then check the office’s own guidance for the record type, year and copy you need [S84 @2026-11-22], [S85 @2026-11-22].

A search of a filmed copy is not a search of the original holding. Record which one you searched.

### Arkansas and Orleans Parish indexes

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Before entering names in the Arkansas or Orleans Parish indexes, clear the [privacy gate](../SKILL.md#privacy-gate) for names, event details and any parents’ names about people who may be living before sending them to MyHeritage or an archive index. Use collection descriptions and non-identifying filters while the gate is pending.

For an early Arkansas death, search *Arkansas Deaths* on MyHeritage as a compiled index. Record the death date and any notice publication date separately. Use the index’s named source to locate the underlying item in the Arkansas State Archives’ holdings. Keep the index row separate from the state death-certificate series, which began in 1914 and has gaps in early reporting [S86 @2026-11-22], [S87 @2026-11-22], [S88 @2026-11-22].

For an Orleans Parish birth, give MyHeritage’s *Louisiana, Orleans Parish Births, 1800–1921* index its own row. After a miss near the beginning of that range, check the separate Orleans Parish birth index beginning in 1790 at the New Orleans City Archives. Log a hit before 1819 as an index entry and check original availability separately. The Louisiana State Archives explains that early index hits can lack an individual certificate in its holdings [S89 @2026-11-22], [S90 @2026-11-22], [S91 @2026-11-22], [S92 @2026-11-22], [S93 @2026-11-22].

### California

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Before using the California indexes below for a name search, clear the [privacy gate](../SKILL.md#privacy-gate) for each destination that would receive names, event details or parents’ names for anyone who may be living. Treat each search site as a separate destination. Use collection coverage and non-identifying filters while the gate is pending.

Search FamilySearch's *California, Deaths and Burials, 1776–2000* as a partial index. Check its coverage table for the locality and keep this search separate from the county register and state certificate searches [S39 @2026-11-20], [S42 @2026-11-20].

For state death index coverage beginning in 1905, record the years of the specific index searched. Archives.com's *California Death Index, 1905–1939* supplies the county and death date for a certificate search [S39 @2026-11-20], [S43 @2026-11-20].

For county deaths, give MyHeritage's *California, County Death Registers, 1873–1994* its own index row and check the county and year before logging a miss. Use birth details and parents' names, where given, to distinguish same-name entries [S57 @2026-11-20], [S58 @2026-11-20].

**Privacy gate:** <!-- privacy-gate: request --> Before sending the subject's name and event details, any living parents' details, and the applicant's information to CDPH or the county office, clear the Record requests gate for anyone who may be living. Keep the application as an unsent draft until the gate is cleared.

Request a California informational birth or death copy by mail using the California Department of Public Health form when using the state route. If the county is known, compare the county recorder's copy and turnaround with the state route [S39 @2026-11-20], [S40 @2026-11-20], [S45 @2026-11-20], [S46 @2026-11-20].

### New York and Massachusetts access

For a New York State birth in the state office’s jurisdiction, check eligibility for an uncertified genealogy copy. The person named must be deceased and the record must have been on file for at least 75 years. A direct-line descendant who documents the relationship can qualify for a waiver of the filing-age requirement and still needs proof of death. Record eligibility and whether the series covers the event as separate findings [S94 @2026-11-22], [S95 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Before entering a New York death-index query at Reclaim The Records, clear the [privacy gate](../SKILL.md#privacy-gate) for names or event details about anyone who may be living that would go to the public search service. Use the coverage description while the gate is pending.

For a New York State death outside New York City, also check Reclaim The Records’ public *New York State Death Index, 1880–2017*. Give the public search its own coverage row and check the fields for the period searched before treating a missing field as evidence about the original certificate [S96 @2026-11-22], [S97 @2026-11-22].

For a 1950 New York City death, check the Municipal Archives’ 1950 holdings and which formats it offers for the borough. NYC Health stopped taking new orders for that year on 1 December 2025. Record the archive transfer and the availability of an image as separate findings [S96 @2026-11-22], [S98 @2026-11-22], [S99 @2026-11-22].

If a New York City death copy lacks cause of death, check which part of the record was supplied. NYC Health issues a standard certificate and separately controls eligibility for the confidential medical report. Record the field as absent from the copy you examined and leave its presence in the underlying record unresolved [S96 @2026-11-22], [S98 @2026-11-22].

For a Massachusetts birth or death from 1930 through 1935, check the Massachusetts Archives’ transferred vital records. Log the archive’s holdings separately from the years available as digital images. If the relevant volume is missing online, check the Archives’ individual scan route [S96 @2026-11-22], [S100 @2026-11-22].

### Ohio

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Before entering identifying details in the Ohio FamilySearch indexes, clear the [privacy gate](../SKILL.md#privacy-gate) for names, dates or parents’ names of anyone who may be living. Use county and year alone while the gate is pending.

For the Ohio county rows, search FamilySearch's *Ohio, County Births, 1841–2003* and *Ohio, County Death Records, 1840–2001* as applicable. After a name miss, browse the event county and year within the respective collection and check for gaps against the probate court's holdings [S47 @2026-11-20], [S48 @2026-11-20], [S49 @2026-11-20], [S50 @2026-11-20], [S51 @2026-11-20].

**Privacy gate:** <!-- privacy-gate: request --> Before sending an Ohio birth request with the registrant's birth details, any living parents' details, and the applicant's information to the Bureau of Vital Statistics or local health department, clear the Record requests gate for anyone who may be living. Keep the application as an unsent draft until the gate is cleared.

Use an Ohio state birth index hit to locate the certificate. Request the Ohio birth certificate for a birth from 20 December 1908 onward from the Ohio Bureau of Vital Statistics or a local health department [S47 @2026-11-20], [S48 @2026-11-20], [S56 @2026-11-20].

Check the access rule for the specific Ohio record and fields. Section 3705.23 generally permits any applicant to obtain a public vital-record copy, with exceptions including restricted medical and health fields on birth records and limits on release of Social Security numbers during the first five years after death. Apply the Record requests gate independently of the office's eligibility rule [S47 @2026-11-20], [S55 @2026-11-20].

**Privacy gate:** <!-- privacy-gate: request --> Before sending an Ohio death-copy request, clear the [privacy gate](../SKILL.md#privacy-gate) for the applicant’s identifying information and any other identifying details about people who may be living that would go to the county health department. Keep the application as an unsent draft until the gate is cleared.

For Ohio state deaths from 20 December 1908 through 1953, search FamilySearch's *Ohio, Deaths, 1908–1953* and open the certificate image where available. The Ohio History Connection holds the 1908–1970 state death certificates. Its online index has separate ranges for the main state death series, 1913–1944 and 1954–1970. For the archive copy, use its microfilm through 1953 or its on-site digital access for 1954–1970. For a certified 1954–1970 copy, use the health department for the county of death [S47 @2026-11-20], [S49 @2026-11-20], [S52 @2026-11-20], [S53 @2026-11-20].

Log the Ohio History Connection's holdings separately from the transfer thresholds. Ohio may transfer a record after 125 years for births or 50 years for deaths. Check the archive's county birth holdings and state death holdings before routing a request there. Use the state office's death series from 1971 [S47 @2026-11-20], [S48 @2026-11-20], [S49 @2026-11-20], [S54 @2026-11-20], [S56 @2026-11-20].

### Maryland death records

For a Baltimore City death from 1875 through 1972, use the Maryland State Archives’ city death index CE42. Browse the vowel index where applicable and switch to the surname Soundex sequence from 1950. Give Baltimore City and Maryland county registration their own rows, with systematic recording beginning in 1875 and 1898 respectively [S101 @2026-11-22], [S102 @2026-11-22], [S103 @2026-11-22].

For a Maryland death entry, record web index and certificate-image availability separately. Check the Maryland State Archives’ series entry and Reclaim The Records’ *Maryland Motherlode* for an off-site image before marking an index hit as requiring a visit to Annapolis [S96 @2026-11-22], [S102 @2026-11-22], [S104 @2026-11-22].

### Rock Island County, Idaho and Harris County indexes

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Before sending names, exact event dates or parents' names for anyone who may be living to MyHeritage, clear the [privacy gate](../SKILL.md#privacy-gate). Use collection descriptions and non-identifying place and year filters while the gate is pending.

For a Rock Island County birth, look for MyHeritage's *Illinois, Rock Island County Births* and search it if your account offers the event year. Record the years of the copy searched. Give the County Clerk's birth holdings their own row and use the Illinois State Archives' separate regular birth index (1877–1907) and delayed birth index (1860–1978) for the relevant year [S71 @2026-11-21], [S72 @2026-11-21], [S73 @2026-11-21].

For an Idaho birth, search MyHeritage's *Idaho Births, 1861–1940*. Open the record image when linked and record the child's birth date and place, the parents' names and any details of their births [S71 @2026-11-21], [S74 @2026-11-21].

Keep Idaho's 1907–1911 county birth holdings and the state filing series beginning in July 1911 on separate rows. Use the collection's 1861 start only for the index row. Check both authorities near the transition, since the state also holds some earlier records [S74 @2026-11-21], [S75 @2026-11-21], [S76 @2026-11-21].

For a Harris County event, look for MyHeritage's *Texas, Harris County Births* or *Texas, Harris County Deaths* and search the matching collection if your account offers the event year. Log the birth and death indexes separately and use the indexed name, event date and place to pursue the underlying record. For events within Houston's city limits at the time, add the city series for births from 1882 or deaths from 1874 [S71 @2026-11-21], [S77 @2026-11-21].

### Other state and town indexes

For an Illinois stillbirth, include the statewide death-and-stillbirth index in the coverage register. Check the years in the copy you search. MyHeritage announced a 1916–1948 index and FamilySearch describes its indexed records as 1916–1947 [S57 @2026-11-20], [S59 @2026-11-20].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Before running the New York death-index name search, clear the [privacy gate](../SKILL.md#privacy-gate) for any names or event details you would send to MyHeritage about someone who may be living. Check the collection’s years and fields while the gate is pending.

For a New York State death outside New York City, search MyHeritage's *New York State Deaths, 1880–2017* as an index. Save the death date and state file or certificate number when present. Check the field label before using an indexed place to route the certificate search, since the state data can give residence at death [S57 @2026-11-20], [S60 @2026-11-20], [S61 @2026-11-20].

For a Connecticut town birth or death through about 1850, use the Barbour statewide surname slips or the relevant town volume. Copy the town, volume and page and use them to find the town register or its film. According to the chapter, names and dates can change in transcription [S62† @2026-11-20]. Check both against the original entry. The town volumes can group different surname spellings and a slip can cite a published transcript. Check the source and years for the particular town in the State Library's *Vital Records by Town* [S63 @2026-11-20], [S64 @2026-11-20].

If the Connecticut town birth entry is missing, use the State Library's town finding aid to identify a church register and check the baptism entry [S64 @2026-11-20]. According to the chapter, a baptism date can help estimate a missing birth date [S62† @2026-11-20]. Record the baptism date separately and, if the entry gives no birth date, use it only as the latest possible birth date.

### Other examples

For Nebraska deaths, give the scanned 1904–1955 state death-index books and the searchable 1956–1968 database separate rows. After an aggregator miss in the earlier period, browse the scanned books by surname Soundex, then by given name. Log the image as an index page [S27 @2026-11-18], [S31 @2026-11-18].

For a statewide Missouri death record, use the Missouri State Archives' death certificate database (1910–1975) and open the free scan when the result links one [S33 @2026-11-18], [S35 @2026-11-18]. Record the latest year posted for the coverage row and keep it separate from the 50-year transfer rule [S32 @2026-11-18], [S33 @2026-11-18], [S34 @2026-11-18].

Read the index's matching rules before logging a failed name search. Oklahoma's OK2Explore returns exact matches, accepts an asterisk as a wildcard and treats blank fields as wildcards [S38 @2026-11-19]. Dyer found a record indexed as Margotte C. Bane by leaving the name blank and searching for a female death in Love County in February 1928. The index gave 12 February, one day later than the headstone. The desired surname was Bone [S20 @2026-11-19]. Try surname and given-name initials with wildcards as a separate search, then compare the certificate, index and headstone before resolving the spelling or date.

Oklahoma's OK2Explore death index works this way: it returns only exact matches, accepts an asterisk as a wildcard in any field, treats a blank field as a wildcard, and asks you to narrow any search that matches more than 15 records. Run the name-free search there with sex, death county and its ±1, 2 or 5-year date range [S21 @2026-11-12].

For Philadelphia City Archives death records filed by cemetery, follow the Archives' own sequence: index, then register page, then cemetery name, then original return. A known cemetery and burial date can be a shortcut into the original records [S10].

For a New York City birth, marriage or death listed in an index on FamilySearch, Ancestry or elsewhere, copy the certificate number, year and borough. Search the Municipal Archives image site by certificate number, limited to that borough and year, not by name: numbering restarts every year in each borough, and name spellings differ between indexes [S15], [S14]. The year on a certificate is the year it was filed, so if nothing comes up, check the number and borough, then try the following year [S15]. If there is still no image, record `searched – no hit` for the online lookup and order the certificate from the Municipal Archives; orders for records not yet digitized are typically filled within six weeks [S16]. Record `unavailable (not online)` only when the archive confirms the certificate is not digitized. Many indexed certificates are not yet digitized, including most corrected "S" birth certificates, and some images are mis-indexed [S17], [S18], [S15].

### Missouri birth and death indexes

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Before using either Missouri index with identifying data, clear the [privacy gate](../SKILL.md#privacy-gate) for names, birth details and any parents’ names about someone who may be living before sending them to MyHeritage or Reclaim The Records. Inspect the catalogue coverage while the gate is pending.

For a Missouri birth, use the *Missouri Births* index on MyHeritage as a locator for the underlying certificate. MyHeritage’s catalogue starts at 1910 and Reclaim The Records describes its release as starting around 1920. Check the copy’s event-year coverage and give the Missouri Bureau of Vital Records’ certificate series a separate row [S105 @2026-11-22], [S106 @2026-11-22], [S113 @2026-11-22], [S107 @2026-11-22].

For a Missouri death beyond the last year of archive certificate scans, check Reclaim The Records’ *Missouri Death Index*. Its expanded search covers 1954–2024. Give the index a separate row and check the Missouri Bureau of Vital Records’ certificate access rule for any follow-up [S105 @2026-11-22], [S108 @2026-11-22], [S107 @2026-11-22].

## Widen the places searched before recording a miss

- **A nearby city where the person worked but did not live.** People living just outside a city could register a birth or death with the city's board [S7], [S6].
- **Where the mother's female relatives lived around the birth.** Look for her mother, sisters and other close female kin. Include neighbouring counties, and cross the state line where the family lived near one [S5].

When a death is missing from the reported home county, test the death place rather than merely changing the name query. Read the burial permit, removal or transfer record for the actual death place, including a hospital or institution in another county or state. A burial permit can supply a death location that conflicts with an obituary's claim that the death occurred at home [S25], [S26].

For a death indexed as filed in Collier County, Florida, read the place-of-death field separately and use it to choose the vital-registration authority. The Collier County Clerk records certificates issued elsewhere, so a Collier filing alone leaves the death place undetermined [S27 @2026-11-18], [S28 @2026-11-18].

For a possible death from the Great Miami Hurricane, search the relevant death series for dates around and after the 18 September 1926 landfall. Test separately for a later death and for a filing after the death. Preserve both dates when the record gives them [S109], [S110].

Each added place gets its own set of authority and series rows. It does not just widen one query.

## Retry a birth search without the expected given name

**Privacy gate:** <!-- privacy-gate: request --> Clear the Record requests gate before giving the local registrar the child's birth date and any names of the child or parents who may be living. Keep the request as an unsent draft until the gate is cleared.

After a birth-record request under an expected given name comes back empty, ask the local registrar to check the known birth date and parents' names without requiring that given name [S68], [S69]. That search located a birth filed under a different given name, according to the presenter [S67†]. Keep the entry as a candidate while you resolve the name conflict.

## Treat a delayed certificate as a set of leads

Search the delayed series for an adult who needed formal proof of birth, following the advice reported in the episode to check even when the birth date is already known [S111†]. For a Utah defense-industry worker during World War II, include delayed filings from 1941 onward [S112].

Read the delayed certificate's evidence section and record each item, its date and its likely holder. It may cite a family Bible, a parent's affidavit or a child's birth certificate [S2], [S9]. One researcher reported a school record as supporting evidence [S2]. If a school is named, trace that school's records for the child's years. For a family Bible, identify the collateral branch that kept it [S9], [S5].

From the affidavits and signatures, record these points separately, and keep each affidavit's date apart from the certificate's filing date:

- an affiant was alive on the date the affidavit was executed
- an affiant's stated age, counted from the date that age applies to, gives an approximate birth year for that affiant
- the applicant's signature may show a married surname [S2], [S9]

Then ask the custodian whether the application and its exhibits were kept. Researchers have told the presenter that some counties kept only the certificate copy [S2]. The certificate alone does not establish the event; route its weight to evidence/proof judgment.

## Report coverage as a table, not a verdict

Return one row per authority and series:

| Place | Authority | Series | Start date (verified + authority / presenter-reported) | Custodian(s) | Access route | Index status | Original vs copy searched | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Use only these result values: `searched – hit`, `searched – no hit`, `not searched`, `unavailable (restricted / not filmed / not online)`. Add a separate list of delayed-certificate evidence leads and their likely holders, and a list of the retrieval requests still needed: archive look-ups, county application requests and society indexes.

Do not write "no birth/death record exists" while any row is `not searched` or `unavailable`. Even with every row searched, report only the bounded negative and hand the conclusion to the researcher.
