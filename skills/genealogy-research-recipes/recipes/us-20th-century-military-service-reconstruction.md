---
id: "us-20th-century-military-service-reconstruction"
title: "Rebuild a 20th-century U.S. Army or Air Force service record after file loss or restriction"
summary: "Rebuild a 20th-century U.S. Army or Air Force service record from records held outside a burned, thin or restricted personnel file, including state WWI questionnaires and Gold Star family packets, separate court-martial trial files, discharge-gated final pay and award General Orders."
kind: "records"
scope: {"platforms": [], "tasks": ["Rebuild a 20th-century U.S. Army or Air Force service record from records held outside a burned, thin or restricted personnel file, including state WWI questionnaires and Gold Star family packets, separate court-martial trial files, discharge-gated final pay and award General Orders."]}
triggers: ["Rebuild a 20th-century U.S. Army", "Air Force service record from records held outside a burned", "thin", "restricted personnel file", "including state WWI questionnaires and Gold Star family packets", "separate court-martial trial files"]
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "US-20TH-CENTURY-MILITARY-SERVICE-RECONSTRUCTION-01", "text": "check the file's actual status before saying \"it burned\", keep trial/award references separate from retrieved files, and do not give the man his unit's events."}]
handoff: []
checked: "2026-10-26"
checked_basis: "checked 2026-10-26"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"tier": "pointer", "group": "U.S. military service", "order": 1135}
---

# Rebuild a 20th-century U.S. Army or Air Force service record after file loss or restriction

Use this when a 20th-century Army or Air Force personnel file burned, came back thin or is restricted, or when a family says a man served but he does not appear in federal lists. The task is to rebuild his service from records held separately from that file, and to log each record's custodian and scope. For older compiled service records, pension files and choosing a custodian, use [military pension file recovery § 1](us-military-pension-file-recovery.md). For the grave and cemetery-record packet, use [burial evidence packet](burial-evidence-packet.md). For naturalization C-files, use [U.S. immigration search recovery](usa-immigration-search-recovery.md). Identity and proof rulings belong in [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- Find out the file's actual status before saying "it burned"
- Request each file product by name and log what comes back
- Request records that were never part of the OMPF
- Read the headstone application as a derivative summary
- Bound a WWII Army enlistment search in AAD before reading a miss
- Test state and local routes before calling the claim unsupported
- Place him with unit records without giving him the unit's events
- Treat WWII casualty lists as incomplete
- Return a routing register

## Find out the file's actual status before saying "it burned"

Do not claim that the records burned and nothing survives. On July 12, 1973 a fire at the National Personnel Records Center (NPRC) in St. Louis destroyed about 16–18 million Official Military Personnel Files (OMPFs). NARA gives these losses ([NARA, 1973 fire](https://www.archives.gov/personnel-records-center/fire-1973); presenter account in [S11], [S12]):

- Army: about 80% of files lost for men discharged November 1, 1912 – January 1, 1960.
- Air Force: about 75% of files lost for discharges September 25, 1947 – January 1, 1964, but only for names alphabetically after "Hubbard, James E."
- Navy, Marine Corps and Coast Guard: NARA's fire page lists no losses for these branches. Strauss calls them largely unaffected [S11].

A discharge date inside a range means the file *may* be lost, not that it is lost. These are exactly the ranges for which NPRC keeps a burned ("B") file registry of about 6.5 million recovered records and a reconstructed ("R") file registry ([NARA](https://www.archives.gov/personnel-records-center/fire-1973)). Request the file anyway.

Then check access. OMPFs become archival and open to the public 62 years after separation, on a rolling basis. Before that, full access is limited to the veteran or next of kin ([NARA, OMPF access](https://www.archives.gov/personnel-records-center/ompf-access)). Work out the cutoff from the discharge date. Do not reuse the presenter's example year [S11].

An archival file is public, so no release is needed ([NARA, archival OMPF requests](https://www.archives.gov/personnel-records-center/military-personnel/ompf-archival-requests)). For a non-archival file, a requester who is neither the veteran nor his next of kin (for example, a grandson) must send a signed, dated authorization. If the veteran is living, it comes from him. If he is deceased, it comes from his next of kin (un-remarried spouse, son, daughter, father, mother, brother or sister), sent with proof of death ([NARA, OMPF access](https://www.archives.gov/personnel-records-center/ompf-access)). In one listener's account, a release signed by the veteran's sons turned a limited reply into the full file [S15].

**Privacy gate:** <!-- privacy-gate: request --> A personnel-file request sends the veteran's identity and, for a non-archival file, a signed authorization and any proof of death; the veteran may be living, so answer the privacy gate in `SKILL.md` first.

Request routes: NARA's online request system, eVetRecs ([vetrecs.archives.gov](https://vetrecs.archives.gov/)); Standard Form 180 (SF-180) by mail; an in-person visit to St. Louis by appointment; or an independent researcher ([NARA](https://www.archives.gov/personnel-records-center/military-personnel/morning-reports-and-unit-rosters); [S11]). eVetRecs is not limited to the family. A requester who is neither the veteran nor his next of kin chooses "Other", and every user verifies identity through ID.me ([NARA, eVetRecs help](https://www.archives.gov/veterans/military-service-records/evetrecs-help.html)).

Ignore loose fire dates. One presenter said "1979" [S16], and another was unsure of the custodian's name [S20]. Cite NARA's own description instead.

## Request each file product by name and log what comes back

**Privacy gate:** <!-- privacy-gate: request --> Each product request concerns a veteran who may be living, and a returned pay roll can name other men of his unit; answer the privacy gate in `SKILL.md` before sending it.

Name each product in the request, and log the product returned and its page count [S9], [S10]:

- **OMPF:** the personnel file itself.
- **Burnt (B) file:** a file that survived with fire or water damage, listed in NPRC's B-file registry. The presenter says the custodian may scan and email it rather than show the original [S9].
- **Reconstructed (R) file:** assembled after the fire from alternate sources: VA claim files, final pay vouchers, state records, Selective Service records, hospital records and organizational records ([NARA](https://www.archives.gov/personnel-records-center/fire-1973)). The presenter adds that veterans were asked to send in copies of their discharge papers [S9]. Expect only a few pages [S9].
- **Auxiliary file:** ask for it by name when the OMPF is lost, and expect it to be minimal. One example is a final pay voucher giving name, service number, and dates and character of service ([NARA, other records](https://www.archives.gov/st-louis/other-records)). Strauss adds rank, last duty station, last unit, pay and overseas status, all from the man's last period of service [S9]. His own WWI request returned three pages: a final pay roll naming the man with other men of his unit [S11]. Log the product under the label the custodian puts on it.

Before choosing final pay as a substitute, distinguish a discharge from an in-service
death. NARA's 2023 presentation says a final pay voucher required discharge: a person
killed in service would have one only from an earlier break before the final reenlistment
[S27]. Preserve the evidence for that earlier separation and request the voucher for its
actual period; an in-service death alone does not supply that target. Use the separate
death-file route below. A missing voucher is not evidence of non-service.

A payroll entry dates the end of service and names the last unit. It is not a full service history. The recorded unit may be a separation unit rather than the operational unit [S27]. Log "no OMPF; auxiliary returned, 3 pp." rather than "file destroyed".

## Request records that were never part of the OMPF

- **In-service deaths:** request the WWI burial case file (also called a mortuary or casualty file) or the WWII Individual Deceased Personnel File (IDPF) separately from the OMPF. Do not merge it with the OMPF in the register. Route the request by custodian:
  - WWI-era burial case files (1915–1939, RG 92) were held at the National Archives in College Park and moved to NARA St. Louis in 2012 ([NARA](https://narations.blogs.archives.gov/2012/06/26/records-heading-west-to-st-louis)).
  - WWII Army IDPFs: search the National Archives Catalog for his file first, then ask NARA St. Louis, whatever his surname. NARA St. Louis lists IDPFs for 1939–1975 among its holdings ([NARA St. Louis, frequently requested](https://www.archives.gov/st-louis/frequently-requested)) and states that WWII Army IDPFs for surnames M–Z are open ([NARA St. Louis](https://www.archives.gov/st-louis)). Its Catalog series also has digitized files for some A–L surnames ([NARA Catalog, IDPFs](https://catalog.archives.gov/id/297287480)). Older accounts split custody by surname between NARA and the Army, so do not route by surname alone. If NARA St. Louis says it does not hold the file, send a FOIA request to the U.S. Army Human Resources Command at Fort Knox, Kentucky. A 2025 History Hub reply gives the address and what to include ([History Hub](https://openhistoryhub.com/t/55151)).
  - Expect cause and date of death, temporary and permanent burial, medical records and sometimes a burial-site map [S10].
- **VA claim file (VA C-file or XC-file):** request it by FOIA. It exists only if a benefits claim was made ([birls.org](https://www.birls.org); [S18], [S20], [S21]).
  - Route: Reclaim The Records runs birls.org, which prepares faxed FOIA requests for deceased veterans' C-files. VBA no longer accepts emailed FOIA requests. Use fax, and use the appeal texts on birls.org for refusals.
  - Example contents: one file contained a DD214 and a WD AGO 53-55 enlistment/discharge form listing decorations [S18].
  - Timing: one request took about five months [S18].
  - Refusals: Reclaim The Records reports that beginning in late July 2025 the VA withheld copies of XC-files and sent only a summary of the genealogical details it deemed releasable ([birls.org updates](https://www.birls.org/updates)). Refusals the presenter received said the records had "no genealogical relevance" [S21]. Log a summary-only reply as a response with the file withheld. A refusal is an access result to appeal, not proof the file doesn't exist.
  - Name: keep the VA C-file apart from the USCIS C-file, which shares the label [S21].
- **VA Master Index card (1917–1940):** held by NARA St. Louis, not the VA. It is digitized and free to search on [FamilySearch](https://familysearch.org/search/collection/2968245). Search there first and log it as its own product [S20].
- **BIRLS entry:** BIRLS (Beneficiary Identification Records Locator Subsystem) is a VA index of veterans and beneficiaries who claimed benefits, built from the 1980s on. Death does not create a BIRLS record. The public release covers only veterans the VA has confirmed as deceased ([birls.org](https://www.birls.org); [S17]). A BIRLS hit tells you a claim file may exist. Log it as its own product.
- **Compensation file:** one presenter used a WWI "compensation file" listing company, battalion, division and dated engagements [S17]. Take the custodian from the file's own heading or citation and record it exactly as found.
- **State bonus file:** many states paid their own WWI bonus or compensation. The application files are state records with a state custodian, separate from the OMPF. Search the archives of the veteran's home state [S29]:
  - Pennsylvania State Archives, RG 19, Series 19.91, *World War I Veterans Service and Compensation File, 1917–1919, 1934–1948*. It records residence, unit, service and overseas dates, discharge, and dependents' names and addresses. Images are on Ancestry and, free to Pennsylvania residents, on Ancestry Pennsylvania ([PA State Archives, WWI records](https://www.pa.gov/en/agencies/phmc/pa-state-archives/research-online/research-guides/world-war-i-records.html); [RG 19](https://www.pa.gov/en/agencies/phmc/pa-state-archives/research-online/research-guides/wpa-and-new-deal-records/wpa-and-new-deal-records-rg-19-rg-23.html); [Ancestry Pennsylvania](https://www.pa.gov/en/agencies/phmc/pa-state-archives/research-online/collection-highlights.html)).
  - Iowa: [Iowa, World War I Bonus Applications, 1922–1954](https://www.familysearch.org/en/search/collection/5000051) (State Historical Society of Iowa; the applications are indexed on FamilySearch).
  - Washington: [Washington, World War I Veteran's Compensation Fund Application Records, 1921–1925](https://www.familysearch.org/en/search/collection/1878898) (Washington State Archives; on FamilySearch).
  - Use: the state holds these files, so they can supply a dated residence and service details when the OMPF burned in 1973. Cite the state custodian and series, not the federal one.

### A separate Army or Air Force court-martial trial file

Keep the trial record separate from personnel-file remarks. Gather the service, trial
year or bounded interval, court type, original outcome and any later appeal or discharge
upgrade. NARA's 2024 presentation describes these historical selection distinctions [S26]:

| Described Army/Air Force trial series | Selection described in the presentation |
| --- | --- |
| General and special, 1917–1938 | Included regardless of outcome |
| General, 1939–1976 | Separate trial-record series |
| Special, 1939–1976 | Proceedings resulting in a bad-conduct discharge |

**Privacy gate:** <!-- privacy-gate: request --> A trial-file request names the defendant,
who may be living, and the file can name victims and witnesses; answer the privacy gate in
`SKILL.md` before requesting it.

The presentation places surviving summary-court details in the OMPF rather than a separate
trial series. Use these distinctions to select a candidate finding description, then
verify its actual period, custodian, survival and access before requesting it. They do
not establish that an individual's file survives or was destroyed. A later discharge
upgrade alone does not settle survival; preserve the original disposition and appeal dates.

For a trial-file search without a case number:

1. Preserve any case number already supplied; otherwise use the **defendant's surname**
   as the lookup lead. The presentation describes staff card indexes arranged by service
   and surname, not by the victim or witness [S26]. Check the custodian's present finder
   and request requirements rather than assuming the 2024 index format is unchanged.
2. Supply the service, all known names and aliases, including married/maiden names, and
   the trial date or bounded interval. Keep unit and trial location as additional clues
   when the date is uncertain. For a joint trial, one known defendant can supply the
   individual card lead; the presentation does not require every defendant's name [S26].
3. Retain any separately cited appeal case number as another retrieval target. Record
   the trial file requested, the actual file or personnel-file extract returned, its
   extent and unresolved references. Personnel remarks are not the trial transcript.

## Read the headstone application as a derivative summary

Retrieve the government headstone or marker application and read **both sides**. A WWI veteran's card had his whole service history written on the back by an unnamed hand [S1], [S4], [S5]. FamilySearch holds "United States, Headstone Applications for U.S. Military Veterans, 1925–1949" (NARA M1916/M2113, RG 92) ([FamilySearch](https://www.familysearch.org/en/search/collection/1916249)), which covers many WWII-era applicants. One presenter found a full list of assignments on the reverse of a card in that series [S7].

Treat any annotation as derivative information from an unknown informant:

- Copy the unit exactly as written.
- Use it to choose unit records.
- Do not file it as the service record.

The stone itself can supply the unit when nothing else names it [S5], [S6].

Not appearing in the VA Nationwide Gravesite Locator is a non-result. Tanner says his grandfather had a VA marker but was missing from the locator [S5]. Log the search and its scope, then check the marker and the application.

## Bound a WWII Army enlistment search in AAD before reading a miss

NARA's WWII Army Enlistment Records in the Access to Archival Databases (AAD) hold about 9 million Army enlistments from 1938–1946, including the Women's Army Auxiliary Corps and the Enlisted Reserve Corps. They exclude Army officers and every other service: Navy, Marine Corps and Coast Guard ([NARA, WWII electronic records](https://www.archives.gov/research/military/ww2/electronic-records.html); [NARA press release, 2004](https://www.archives.gov/press/press-releases/2004/nr04-64.html)). The series is the Electronic Army Serial Number Merged File, RG 64 ([NARA Catalog](https://catalog.archives.gov/id/1263923)). If his OMPF burned, search AAD first to test a claimed Army enlistment. A hit gives his Army serial number for the later requests.

The file was converted from punch-card microfilm. 212 rolls holding about 1.5 million cards were too dark to scan, and 160,390 records only flag that cards at that point were unreadable ([Prologue, 2006](https://www.archives.gov/publications/prologue/2006/spring/aad-ww2.html)). An AAD miss is therefore not evidence that he did not enlist.

- Coded fields, such as residence state and county, need AAD's code lists and field notes. Read the code from the list; do not guess it ([Prologue, 2006](https://www.archives.gov/publications/prologue/2006/spring/aad-ww2.html)).
- Tell same-name men apart by state of residence and year of birth. For a common surname, narrow the query by state of residence before reading the results.
- AAD can refuse automated fetches: an automated fetch got HTTP 403 on 2026-11-04. Do not rely on web search to find its record pages. Log a 403 or an empty web search as an access failure, not a no-record finding, and search AAD in a browser session.

## Test state and local routes before calling the claim unsupported

Absence from federal service lists does not show non-service. In Tanner's repeated account, a man missing from every WWI list he searched had served in a National Guard unit [S1], [S3], [S4], [S5], [S6]:

- He enlisted in one state's Guard.
- He was transferred, attached or detailed to another state's Guard unit (Texas), which was mobilized and went overseas.

The retellings differ on details (Arizona versus New Mexico Guard). Keep the method, not the specifics. Tanner says such a man was "never in the Army", yet his family held the man's Army discharge papers [S1], [S2]. Do not read that phrase as meaning no federal record exists.

Search both states' Guard records. Search the unit's later federal designation, but keep the original designation as written [S6], [S7].

Check the county for a locally recorded discharge, even if the family holds the Army papers. Tanner found that an Apache County–recorded copy carried information missing from the Army documents [S2]. Record it as a separate source with its own custodian, and compare it field by field. Strauss also found Pennsylvania local records that were not in federal hands [S11].

Search the state archive's WWI historical-project questionnaires and Gold Star files as a
separate product from the OMPF or federal burial file. Read the collection's own inclusion
rule first: Alabama's Gold Star project collected survivors' contributions about service
members who died, so a miss is not a general test of service. Use documented state ties,
including a supported collateral soldier or next of kin living elsewhere, to choose other
collections whose scope fits. Birthplace alone need not identify the right one; a relative's
residence does not itself establish eligibility. [S23, H1]

Inventory the supplied biography, questionnaire, letters, photographs and notification papers
rather than treating the result as a service abstract. Record who supplied each family
statement, keeping apparent or unknown informants uncertain, and carry names and addresses
as attributed leads. Where both an online preview and a downloadable packet are available,
compare their page/image extents and log omissions before calling the packet inspected.
Contents and access vary by collection; these state papers do not reconstruct a complete
service history. The Reclaiming Kin examples motivate the family-file and extent checks;
their historical site controls are not current access promises. [S23]

A draft registration shows a man was present when he registered, not that he served [S5], [S14]. The 1917 card asks about prior military service, and Strauss says Guard service was often noted [S14]. Read the whole card, but don't count it as service.

For WWII, the draft records in Record Group 147 cover men only. The Fourth Registration took men born from April 1877 to 16 February 1897. Its cards no longer exist for Alabama, Florida, Georgia, Maine, Mississippi, North Carolina, South Carolina and Tennessee. The other WWII registrations took men born from 17 February 1897 to 31 July 1927 ([NARA, Fourth Registration](https://www.archives.gov/files/research/military/ww2/draft-cards-fourth-registration.pdf); [NARA St. Louis, Selective Service](https://www.archives.gov/st-louis/selective-service)). NARA St. Louis also holds *Classification Records, 1940–1947* for many but not all states. Search the Catalog for his state's series before you rely on it ([NARA Catalog, example](https://catalog.archives.gov/id/2173095)). A classification entry, like a card, is not proof of service.

## Place him with unit records without giving him the unit's events

With a service number and unit, get the morning reports and after-action reports covering his dates. Morning reports and muster rolls are unit records that were not part of the OMPF, and the fire did not touch them [S10], [S16].

Check whether the selected morning-report series and period record personnel changes rather
than a full roster. McComb describes entries for changes such as promotion, illness or
absence [S24]. Where that practice is confirmed, use an independently dated status change
to choose an initial, bounded run of the supported unit or company's reports. A name missing
on one day then does not show that the man was absent from the unit.

- **Online first:** NARA has been adding digitized WWII Army morning reports to the National Archives Catalog, in the series *Morning Reports, 1940–1946*. When checked on 2026-11-07, it had monthly reports through December 1944 only ([NARA Catalog](https://catalog.archives.gov/id/85713825)). Search the Catalog for the unit and his dates first. If his reports are not there, use the offline route. The 2023 advice that morning reports are "not online" [S16] is out of date.
- **Privacy gate:** <!-- privacy-gate: request --> Morning reports name the men of a unit, and the 1969–1974 reports may concern living people; answer the privacy gate in `SKILL.md` before requesting them or briefing a researcher.
- **Offline access:** for archival Army morning reports (1912–1968), NPRC does not take written requests. Read them in person at St. Louis by appointment, or hire an independent researcher. Mail and fax requests apply only to non-archival 1969–1974 reports ([NARA](https://www.archives.gov/personnel-records-center/military-personnel/morning-reports-and-unit-rosters)).
- **Personal entries:** promotions and furloughs, dated to the day [S16]. Log only entries that name him.
- **Unit context:** movements, incidents and after-action detail [S16]. An after-action report corrected a family memory of an incident's date (Christmas Day versus Christmas Eve) [S16]. Note that it dates the unit's incident, not his part in it.

**An award reference:** an OMPF decorations field is a lead to an order, not the order
itself. For Korean War Army records, NARA's 2023 presentation gives two search keys:
the General Order (GO) number, or the awarding unit and approximate award date [S28].
Preserve whichever is actually supplied; a surname alone does not identify the order.

1. Copy the GO number and any date or issuing unit from the referring document. With
   only unit/date evidence, identify the actual awarding unit before selecting records.
   Keep the supported interval and any unresolved command relationship explicit.
2. Search that unit's actual record descriptions. If the company or battalion search
   misses, use its documented command relationship to inspect the relevant higher-level
   regiment or other issuing formation. The presentation shows regimental records that
   cover subordinate units [S28]; do not substitute an unrelated same-numbered formation.
3. **Privacy gate:** <!-- privacy-gate: request --> The order can name other award
   recipients who may be living; answer the privacy gate in `SKILL.md` before requesting it.
   Retrieve the matching order and retain its locator and extent. Compare the actual
   name, rank, service number and organization with the independent identity anchors.
   Keep order, award and action dates in their stated roles. Some orders list only basic
   award details; record an individual action only when the inspected order states it.

Keep the order as a separate row in the routing register. A GO is not a complete personnel
roster, and neither an uninspected award reference nor a unit narrative proves the man's
action. Continue to separate personal statements from unit context in the timeline.

The presenters describe outbound and returning Army transport passenger lists [S14], [S22]. The [Ancestry database 61174 link](https://search.ancestry.com/search/db.aspx?dbid=61174) is a collection lead: its fetch returned HTTP 403, so the reported RG 92 attribution and 1910–1939 coverage were not confirmed from the collection description [H12]. Check that description before choosing the collection, then search both directions:

- Treat a 1930 census veteran answer as a lead either way: search the transport lists even when the answer is "no" [S22].
- Record the vessel, dates, service number, company/regiment and named nearest relative with the stated relationship [S14].
- Follow ditto marks up to the top of the page, or back to earlier pages, to read the unit [S22].
- Compare the relative and address with the census household and city directories before attributing a letter, postcard or identity [S14], [S22].

Unit histories, unit reports and veterans' associations supply context. One example is a group that sent books and pointers to repositories holding diaries and photographs [S17]. Another is a hospital unit's periodic reports [S19].

- Limit them to his service dates.
- Exclude later incarnations of the designation. The 97th General Hospital designation stayed in use for a postwar U.S. military hospital in Frankfurt, and that postwar role swamped search results for its WWII service [S18], [S19]. Filter results to his service dates, and confirm the unit number from his documents before searching.
- Write unit actions as unit context, never as "he fought at…". Tanner's own wording ("I assume, from the record of that unit") is an inference [S4].

## Treat WWII casualty lists as incomplete

Do not accept the National Archives WWII casualty lists as a complete roster. The presenter found people missing from them by checking newspaper casualty lists, county memorial lists and the full crew of a single crash [S13]. Cross-check all three, and record which roster supplied each name.

## Return a routing register

Deliver three things:

1. **Register:** one row per product (OMPF/B/R/auxiliary, separate court-martial trial file, burial case file/IDPF with its custodian, VA C-file, VA Master Index card, BIRLS, AAD enlistment record, compensation file, state bonus file, headstone application both sides, Guard records per state, county discharge, state WWI questionnaire/Gold Star packet, morning/after-action reports, award GO, transport lists, unit histories). Each row gives custodian, access status, release used, date requested and result (including page count, refusal, summary-only reply, appeal or pending). For a state questionnaire packet, also retain its subject, collection inclusion rule, family informants and the received page/image extent.
2. **Dated timeline:** three marked columns: personal entries, unit-level context and derivative annotations.
3. **Negative searches:** each with its scope (database, name form, branch, state, date range).

A pending or refused request stays open. Do not fill the gap with unit history.
