---
id: "canadian-provincial-record-routing"
title: "Route a Canadian vital, estate, military or Indigenous-series record to its province, custodian and access category"
summary: "Route a Canadian vital or estate record, war personnel file, Métis or First Nations record, or Home Child to its province, custodian and access category."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "CANADIAN-PROVINCIAL-RECORD-ROUTING-01", "text": "Vital registration is provincial. Each province has its own start date, gaps and archive cut-off, so build one coverage row per province before you search."}]
handoff: ["canadian-census-interpretation", "catholic-parish-diocesan-record-recovery", "evidence-proof-judgment", "french-canadian-register-recovery", "historical-place-name-resolution", "us-vital-registration-coverage", "usa-immigration-search-recovery"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request", "third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Canada, Latin America, Asia and Oceania", "order": 224}
---

# Route a Canadian vital, estate, military or Indigenous-series record to its province, custodian and access category

Use this recipe before you search for a Canadian birth, marriage or death registration, a First or Second World War personnel file, a Métis or First Nations record, or a British Home Child. It sends each record to the custodian and access category of its own province, date and series. It prevents five failures: treating Canadian vital records as one national system, reading a miss past an archive's release cut-off or inside a registration gap as an absence, calling a Second World War file unavailable without checking whether it is open or closed, searching treaty paylists and scrip by surname alone, and searching for a Home Child with the family instead of inside the agency party.

Link out for the shared steps:

- **A Quebec Catholic register, a post or Montréal entry, or a notarial act:** [French-Canadian register recovery](french-canadian-register-recovery.md).
- **A Canadian census line or a census name-search miss:** [Canadian census interpretation](canadian-census-interpretation.md).
- **A church register that substitutes for a missing civil registration:** [Catholic parish and diocesan record recovery](catholic-parish-diocesan-record-recovery.md).
- **A crossing between Canada and the United States:** [U.S. immigration search recovery](usa-immigration-search-recovery.md), step 4.
- **The same coverage-register idea for U.S. states:** [U.S. vital-registration coverage](us-vital-registration-coverage.md).
- **A locality you cannot place in its province or county on the event date:** [historical place-name resolution](historical-place-name-resolution.md).
- **Identity rulings:** [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- Inputs to gather first
- 1\. Fix the province and its coverage row for the event
- 2\. Read a miss against the coverage row
- 3\. Route a military personnel file by war and access category
- 4\. Search Métis and First Nations series by series, not by name index
- 5\. Trace a British Home Child through the party and the agency
- 6\. Recover Ontario estate files through their indexes
- Close with a routing packet

## Inputs to gather first

Gather these before searching:

- the event type and approximate year
- the province or colony on the event date, and the locality as each record writes it
- for a soldier: the war, the force (for example the Canadian Expeditionary Force) and whether the person died in service
- for an Indigenous line: the band, treaty or Métis community named in any record, and any band or ticket number seen
- for a Home Child: the sending agency, the approximate arrival year and port
- every index, database or image set already searched, with the date

- for an Ontario estate: the approximate probate year and any known court or district

## 1. Fix the province and its coverage row for the event

- **Route by province, not by "Canada".** Vital registration is provincial. Each province has its own start date, gaps and archive cut-off, so build one coverage row per province before you search.
- **Use these rows for the three provinces checked.** The cut-offs are the holdings as published on 2026-11-04. Re-read the custodian's page before you rely on a cut-off; cut-offs move forward as registries release years.

  | Province | Registration coverage | Archive holdings (read 2026-11-04) | Later years |
  | --- | --- | --- | --- |
  | Ontario | From 1 July 1869 [S12]; not widely followed for some years after [S1] | Archives of Ontario: registrations from 1869 up to a cut-off for each event type [S2]; ask the Archives before ServiceOntario | ServiceOntario [S2] |
  | British Columbia | BC Archives index: births 1854–1904, marriages 1871–1950, deaths 1872–2005 [S3] | Royal BC Museum / BC Archives genealogy search [S3] | BC Vital Statistics Agency, which releases years to the BC Archives annually [S3] |
  | Nova Scotia | Births and deaths 1864–1877, then none until October 1908; marriages continuous [S4] | Nova Scotia Archives, online as of July 2025: births 1864–1877 and 1908–1924, delayed births 1830–1924, marriage bonds 1763–1864, marriage registrations 1864–1949, deaths 1864–1877 and 1908–1974; 1925 birth registrations transferred to the Archives but not yet online [S4] | Vital Statistics, Service Nova Scotia (as of March 2026): births from 1926, marriages from 1951, deaths from 1976 [S4] |

- **For any other province, build the row from that province's custodian page** before you read a result: start date, gaps, archive cut-off per event type, and the office that holds later years.

## 2. Read a miss against the coverage row

**Privacy gate:** <!-- privacy-gate: request --> A request to a provincial archive or registry for a birth, marriage or death registration can send event details and identity or eligibility documents for the applicant and people named in the record. For a Québec civil act the recipient is the Directeur de l’état civil. If anyone named may be living, answer the privacy gate in `SKILL.md` before sending the request.

- **Past the archive cut-off, route to the provincial registry.** Ask the Archives of Ontario first for an Ontario birth, marriage or death; a registration it does not hold is with ServiceOntario [S2], not missing. A Nova Scotia birth of 1925 is at the Nova Scotia Archives although it is not yet online; request it there [S4]. A BC birth after 1904 is outside the BC Archives index, not absent [S3].
- **Inside Nova Scotia's 1877–1908 gap, do not search for a birth or death registration.** The province did not record them [S4]. Search instead:
  - marriage registrations, which run straight through the gap [S4];
  - delayed birth registrations, which cover births from 1830 [S4];
  - City of Halifax death registers, 1890–1908, for a Halifax death [S4];
  - church registers, through the parish recipe.
- **In Ontario's first years, do not read a missing registration as an absence.** Registration began on 1 July 1869 but was not widely followed for some years [S1]. Search church and census substitutes before you call the event unrecorded.
- **Write the row on every negative.** Record the province, the series, the years it covers and the cut-off date you read. A miss without that row is not a negative search.

**Request an official Québec civil-status document through the Directeur de l’état civil.** Check that the event is entered in the Québec register and confirm eligibility before applying. The applicant must be named in the act or establish an interest in obtaining it. For a deceased subject, a qualifying spouse, child or sibling can establish eligibility by documenting that relationship. Apply the proof rule for the act and applicant. An age threshold alone does not determine the request route [S39 @2026-11-22] [S40 @2026-11-22] [S64 @2026-11-22].

**Use Library and Archives Canada for named historical series.** Open LAC's *Birth, marriage, death and divorce records* guide and choose the series listed for the place and event. For an early Upper or Lower Canada marriage, search the marriage bonds in Collection Search and use a bond as a lead to the ceremony record. A miss in LAC's selected collections leaves the provincial or parish search open [S37 @2026-11-22] [S38 @2026-11-22].

**Find the Newfoundland and Labrador death registration for 1950–1968.** Search The Rooms' *Vital Statistics Database – Deaths (1950–68)* by the deceased person's name, death date or death place [S44 @2026-11-22] [S45 @2026-11-22]. Open the attached registration and check for a birth year and birthplace to carry into the birth search [S43 @2026-11-22] [S45 @2026-11-22].

Establish the denomination and actual register holder before selecting an archive. Anglican historical parish registers are with the diocese, sometimes housed in a university or provincial archive [S14 @2026-11-16]. Follow the parish-record recipe for the chosen denomination. Only a transcript excerpt was inspected for the video’s custody suggestion [S19 @2026-11-16].

### Search supplementary vital indexes

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Submitting a MyHeritage search sends the subject's or relatives' names, dates and places entered in the query to MyHeritage. If any of those people may be living, answer the privacy gate in `SKILL.md` before submitting it.

Search the named collection for the province, event and year. Log its range separately from the province's official coverage row. Use the [French-Canadian register recovery](french-canadian-register-recovery.md) route to follow up Québec register leads.

**Check Nova Scotia birth hits for baptism evidence.** Use MyHeritage's *Canada, Nova Scotia Births, 1836–1921* as a second index and open the image behind the hit. Copy the birth date, place and any registration number [S23 @2026-11-21]. A birth hit can open on a baptism certificate [S22 @2026-11-21]. If it does, record birth and baptism separately, and transcribe the child's given names, parents, their residence and the officiating priest where stated. For a delayed birth registration at Nova Scotia Archives, open the supporting pages for copies of church-register entries [S24 @2026-11-21].

**Include stillbirths in a Québec birth search.** Search MyHeritage's *Canada, Quebec Births, 1820–1917* for the birth date and place and the parents' names. Use the parent fields if the child's name is unavailable. Check a stillbirth entry for a death date too [S29 @2026-11-21] [S30 @2026-11-21].

**Use Québec death entries from 1825–1917 for birth and kinship leads.** Search MyHeritage's *Canada, Quebec Deaths, 1825–1917* for the death date and place. Check the entry for the deceased person's birth date and the names of parents and spouse [S29 @2026-11-21] [S31 @2026-11-21].

**Check Québec marriage entries for each spouse's birth details.** Search MyHeritage's *Canada, Quebec Marriages, 1820–1917* for the spouses and their parents. Check for a separate birth date and birthplace for each spouse, alongside the marriage date and place [S29 @2026-11-21] [S32 @2026-11-21].

**Choose the Québec index for the event and date.** Search MyHeritage's *Canada, People of Quebec* for birth, baptism, death or burial and the parents' names [S25 @2026-11-21] [S26 @2026-11-21]. For a Québec death from 1926 through 1997, choose the distinct *Canada, Quebec Civil Deaths, 1926–1997* index [S27 @2026-11-21] [S28 @2026-11-21]. Read the deceased person's birth date, residence, parents and spouse where recorded [S27 @2026-11-21].

**Search the Montréal synagogue index for Jewish vital events.** Use MyHeritage's *Canada, Montréal Jewish Synagogue Vital Records*, 1828–2007, for births, marriages and deaths. Include outlying entries when the locality fits, such as Québec City, Sherbrooke, Lachine or La Macaza. Read the image where available and check death entries for age, spouse and both parents' names [S41 @2026-11-22] [S42 @2026-11-22].

**Use Prince Edward Island's event-specific indexes.** Check the Public Archives and Records Office service notice before counting an archive lookup. If its database is offline, log the access problem and use the MyHeritage indexes as leads [S47 @2026-11-22]. In *Canada, Prince Edward Island Births and Baptisms* (from 1702), record the birth and baptism separately and use the parents, church and officiant to locate the register [S46 @2026-11-22] [S48 @2026-11-22]. In *Canada, Prince Edward Island Deaths and Burials* (from 1779), use residence to distinguish namesakes and record death and any burial date separately [S46 @2026-11-22] [S49 @2026-11-22]. In *Canada, Prince Edward Island Marriages* (1827–1920), match the couple and residence. Use any officiant as a lead and distinguish the ceremony from the licence and registration dates [S50 @2026-11-22] [S51 @2026-11-22].

**Separate British Columbia births from baptisms.** Search MyHeritage's *Canada, British Columbia Births and Baptisms* (from 1773) using the child and any known parent. Copy birth and baptism dates and places into separate fields [S50 @2026-11-22] [S52 @2026-11-22] [S53 @2026-11-22]. Record any BC Archives (BCA) and Genealogical Society of Utah (GSU) microfilm numbers and any registration number. Use the church-register route for a baptism and the civil registration route for a birth registration. A BCA reel number on a baptism hit does not establish that BC Archives holds that reel [S50 @2026-11-22] [S53 @2026-11-22] [S54 @2026-11-22].

**Carry British Columbia marriage and death locators to the archive.** Search MyHeritage's *Canada, British Columbia Marriages* (1800–1946) for both spouses and the marriage date and place [S56 @2026-11-22] [S57 @2026-11-22]. Search *Canada, British Columbia Deaths* (from 1872) for the death date, place and age [S50 @2026-11-22] [S55 @2026-11-22]. Check any linked image. When following a civil registration to BC Archives, use the event date, registration number and BCA reel where supplied. Keep the GSU number as a separate locator [S54 @2026-11-22].

**Verify Alberta marriage index hits against the provincial locator.** Search MyHeritage's *Canada, Alberta Marriage Index, 1877–1950* for both spouses and use the year, place and any residence to narrow the match. The entries were extracted from index cards with AI. Check the hit in the Provincial Archives of Alberta marriage indexes and copy the registration number, place and year for retrieval [S58 @2026-11-22] [S59 @2026-11-22] [S60 @2026-11-22].

## 3. Route a military personnel file by war and access category

**Privacy gate:** <!-- privacy-gate: request --> An ATIP request for the file of a veteran who survived the war sends the veteran's identity, and the veteran may be living; answer the privacy gate in `SKILL.md` before you send it.

- **First World War: open the Canadian Expeditionary Force file in LAC Collection Search.** Library and Archives Canada (LAC) digitised more than 600,000 CEF service files and put them in Collection Search [S5]. Almost all are online [S6] and free to view there. Treat a CEF file that is not found as a search problem first, not as a lost file.
- **Second World War: decide the access category before calling a file unavailable.**
  - **Died in service, 1939–1947:** the file is open. Download it from Collection Search with the download arrow [S7]. Expect a "genealogy package" of selected documents for most entries; only about 1,600 are complete or partial digitised files [S7].
  - **Survived the war:** the file is closed. Request it through an ATIP (access to information or privacy) request. LAC requires proof of death, or the consent of the person if still alive [S7].
- **Record the category and the request route** in the packet. "Not online" for a survivor's file is the access rule, not a loss.

- **Open the LAC entry even when you already hold an attestation paper.** The service file of a man who served holds one copy of his attestation paper, and most entries have two digitised items: the service file as a PDF and the attestation paper as a JPEG [S6 @2026-11-16]. An attestation paper from another site is one document of the file, not the file.

- **For an American volunteer, search under other names and birthplaces.** Search for the Canadian Expeditionary Force attestation paper under the names the family used [S13]. Library and Archives Canada warns that some American volunteers supplied both a different name and a different birthplace [S6]. If a search restricted to a U.S. birthplace fails, remove that filter and try the aliases separately. Compare next of kin, date of birth and residence on the candidate's attestation with independent records before attaching the file.

**Carry a Canadian Great War Project hit into the file search.** Follow the suggestion from the available excerpt [S33 @2026-11-21] and copy the name, unit and enlistment date from the hit [S34 @2026-11-21]. Search LAC's *Personnel Records of the First World War* by name or regimental number [S35 @2026-11-21]. Compare the unit and enlistment date in the digitised papers with the project's entry.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A personnel-index query sends the service member's name and any birth or enlistment details entered to MyHeritage. Use only the service member's details and answer the privacy gate in `SKILL.md` before submitting data about anyone who may be living.

**Use enlistment details to narrow a First World War name search.** If a LAC name search leaves several candidates, use the birth or enlistment date and place fields in MyHeritage's *Canada, World War I Personnel Files*. Take any regimental number and unit back to LAC to locate and compare the service file [S61 @2026-11-22] [S63 @2026-11-22].

**Trace what happened on leaving the Canadian unit.** For a U.S.-born volunteer, check whether the record supports discharge home or onward service in a U.S. unit, the alternatives from the available excerpt [S33]. Read the service file's record of service and casualty forms and record the action, its effective date and any stated destination [S36]. Treat an entry that only records departure as an unresolved destination.

## 4. Search Métis and First Nations series by series, not by name index

- **Métis scrip: read the application for parents and birth details.** Scrip applications give dates and places of birth and the names of parents, children and spouses, and are filed alphabetically within several Department of the Interior (RG 15) series [S12]. Search the scrip series directly rather than relying on a name-index miss.
- **Treaty annuity paylists: search by band, list by list, not by surname.** They are Indian Affairs records in LAC RG 10, reached through finding aids FA 10-91, 10-109 and 10-116 [S8]. The government identified band members by a band number or "ticket" given to a family or to an adult living alone [S8]. Record any band or ticket number you find.
- **Expect a privacy restriction on paylists after 1909** [S8]. Record a later list as restricted, not as missing.
- **Hudson's Bay Company servants and posts: search the Hudson's Bay Company Archives at the Archives of Manitoba.** The HBCA is part of the Archives of Manitoba and holds servants' contracts and pre-1870 records from almost five hundred HBC posts [S9].

For possible HBC or North West Company employment, browse HBCA’s alphabetical biographical sheets, a partial set of employee summaries. Copy the references and employment dates, then check the original records [S15 @2026-11-16]. A missing sheet does not exclude employment [S20 @2026-11-16].

## 5. Trace a British Home Child through the party and the agency

**Privacy gate:** <!-- privacy-gate: request --> A request for a home child's agency case records sends the child's identity and a descendant's consent, and the records can name people who are still living; answer the privacy gate in `SKILL.md` before you send it.

- **Date the movement correctly.** More than 100,000 children were sent from the British Isles between 1869 and the late 1930s. The Fairbridge Society brought some Middlemore children to a farm school in British Columbia between 1936 and 1948 [S10].
- **Search LAC's Home Children index in Collection Search.** It is built mainly from passenger lists. Where lists were missing or unreadable, LAC filled gaps from other immigration records, and it added a Boards of Guardians register [S10].
- **Search the party, not the family.** The child usually travelled in an agency party, not with relatives. LAC gave each group of children travelling together a code [S10]. Search by that code to see the whole party and its arrival.
- **Request the agency's own case records.** Barnardo's holds the records of its child migrants and also those of the Marchmont, Annie Macpherson and Liverpool Sheltering Homes. It releases them through its Family History Service, with the signed consent of the nearest surviving descendant [S11].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A Home Child index query sends the child's name and any birth, travel and destination details entered to MyHeritage. If the child may be living, answer the privacy gate in `SKILL.md` before submitting the query.

**Narrow a Home Child lookup by birth date or destination.** If the name search leaves several candidates, use those fields in MyHeritage's *Canada, Home Children Immigration Index, 1869–1932*. Copy the departure and arrival dates and ports and the Canadian destination where stated. Use a placement note as a lead for the agency search and verify the party in LAC. Keep the index's date range separate from the span of the migration [S61 @2026-11-22] [S62 @2026-11-22].

## 6. Recover Ontario estate files through their indexes

For an Ontario estate before 1859, search the Archives’ name catalogue and copy the court, file and microfilm references [S17 @2026-11-16]. The Court of Probate handled estates valued at £5 or more **in two or more districts**; other estates went to district Surrogate Courts [S16 @2026-11-16]. Distinguish the probate date from the death date and follow the file or register locator [S21 @2026-11-16].

For Ontario estates from 1859, find the estate-file number in the index, then retrieve the file [S18 @2026-11-16]. If the court is unknown, consult the *Application to Probate Book*, 1859–1982, as a courthouse finder [S18 @2026-11-16] [S21 @2026-11-16].

## Close with a routing packet

Return:

- **Coverage rows:** for each province searched, the start date, gaps, archive cut-off per event type with the date read, and the office for later years.
- **Search rows:** each index, series or image set searched, the years it covers, the result (found, not found, outside coverage, restricted) and the locator.
- **Military rows:** the war, the force, the access category (CEF online, WWII open war dead, WWII closed survivor) and, for a closed file, the ATIP request and the proof of death or consent it needs. For an American CEF volunteer, add every name and birthplace searched.
- **Indigenous-series rows:** the series and finding aid searched, the band, any band or ticket number found, and any restricted years.
- **Home Child rows:** the agency, the party code, the ship and arrival date, and the agency record request.
- **Gaps:** registration gaps such as Nova Scotia 1877–1908, years past a cut-off, and restricted series.

- **Ontario estate rows:** the court, index coverage, estate-file number and the file or register locator.

The model assembles this packet. The researcher decides identity and kinship.
