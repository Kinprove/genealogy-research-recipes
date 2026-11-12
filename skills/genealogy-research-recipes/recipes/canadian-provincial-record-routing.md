---
id: "canadian-provincial-record-routing"
title: "Route a Canadian vital, military or Indigenous-series record to its province, custodian and access category"
summary: "Route a Canadian vital registration, world-war personnel file, Métis or First Nations record, or British Home Child to the province, custodian and access category of its date and series."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "CANADIAN-PROVINCIAL-RECORD-ROUTING-01", "text": "Vital registration is provincial. Each province has its own start date, gaps and archive cut-off, so build one coverage row per province before you search."}]
handoff: ["canadian-census-interpretation", "catholic-parish-diocesan-record-recovery", "evidence-proof-judgment", "french-canadian-register-recovery", "historical-place-name-resolution", "us-vital-registration-coverage", "usa-immigration-search-recovery"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "pointer", "group": "Country record routing", "order": 1065}
---

# Route a Canadian vital, military or Indigenous-series record to its province, custodian and access category

Use this recipe before you search for a Canadian birth, marriage or death registration, a First or Second World War personnel file, a Métis or First Nations record, or a British Home Child. It sends each record to the custodian and access category of its own province, date and series. It prevents five failures: treating Canadian vital records as one national system, reading a miss past an archive's release cut-off or inside a registration gap as an absence, calling a Second World War file unavailable without checking whether it is open or closed, searching treaty paylists and scrip by surname alone, and searching for a Home Child with the family instead of inside the agency party.

Link out for the shared steps:

- **A Quebec Catholic register, a post or Montréal entry, or a notarial act:** [French-Canadian register recovery](french-canadian-register-recovery.md).
- **A Canadian census line or a census name-search miss:** [Canadian census interpretation](canadian-census-interpretation.md).
- **A church register that substitutes for a missing civil registration:** [Catholic parish and diocesan record recovery](catholic-parish-diocesan-record-recovery.md).
- **A crossing between Canada and the United States:** [U.S. immigration search recovery](usa-immigration-search-recovery.md), step 4.
- **The same coverage-register idea for U.S. states:** [U.S. vital-registration coverage](us-vital-registration-coverage.md).
- **A locality you cannot place in its province or county on the event date:** [historical place-name resolution](historical-place-name-resolution.md).
- **Identity rulings:** [evidence/proof judgment](evidence-proof-judgment.md).

## Inputs to gather first

Gather these before searching:

- the event type and approximate year
- the province or colony on the event date, and the locality as each record writes it
- for a soldier: the war, the force (for example the Canadian Expeditionary Force) and whether the person died in service
- for an Indigenous line: the band, treaty or Métis community named in any record, and any band or ticket number seen
- for a Home Child: the sending agency, the approximate arrival year and port
- every index, database or image set already searched, with the date

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

- **Past the archive cut-off, route to the provincial registry.** Ask the Archives of Ontario first for an Ontario birth, marriage or death; a registration it does not hold is with ServiceOntario [S2], not missing. A Nova Scotia birth of 1925 is at the Nova Scotia Archives although it is not yet online; request it there [S4]. A BC birth after 1904 is outside the BC Archives index, not absent [S3].
- **Inside Nova Scotia's 1877–1908 gap, do not search for a birth or death registration.** The province did not record them [S4]. Search instead:
  - marriage registrations, which run straight through the gap [S4];
  - delayed birth registrations, which cover births from 1830 [S4];
  - City of Halifax death registers, 1890–1908, for a Halifax death [S4];
  - church registers, through the parish recipe.
- **In Ontario's first years, do not read a missing registration as an absence.** Registration began on 1 July 1869 but was not widely followed for some years [S1]. Search church and census substitutes before you call the event unrecorded.
- **Write the row on every negative.** Record the province, the series, the years it covers and the cut-off date you read. A miss without that row is not a negative search.

## 3. Route a military personnel file by war and access category

- **First World War: open the Canadian Expeditionary Force file in LAC Collection Search.** Library and Archives Canada (LAC) digitised more than 600,000 CEF service files and put them in Collection Search [S5]. Almost all are online [S6] and free to view there. Treat a CEF file that is not found as a search problem first, not as a lost file.
- **Second World War: decide the access category before calling a file unavailable.**
  - **Died in service, 1939–1947:** the file is open. Download it from Collection Search with the download arrow [S7]. Expect a "genealogy package" of selected documents for most entries; only about 1,600 are complete or partial digitised files [S7].
  - **Survived the war:** the file is closed. Request it through an ATIP (access to information or privacy) request. LAC requires proof of death, or the consent of the person if still alive [S7].
- **Record the category and the request route** in the packet. "Not online" for a survivor's file is the access rule, not a loss.

## 4. Search Métis and First Nations series by series, not by name index

- **Métis scrip: read the application for parents and birth details.** Scrip applications give dates and places of birth and the names of parents, children and spouses, and are filed alphabetically within several Department of the Interior (RG 15) series [S12]. Search the scrip series directly rather than relying on a name-index miss.
- **Treaty annuity paylists: search by band, list by list, not by surname.** They are Indian Affairs records in LAC RG 10, reached through finding aids FA 10-91, 10-109 and 10-116 [S8]. The government identified band members by a band number or "ticket" given to a family or to an adult living alone [S8]. Record any band or ticket number you find.
- **Expect a privacy restriction on paylists after 1909** [S8]. Record a later list as restricted, not as missing.
- **Hudson's Bay Company servants and posts: search the Hudson's Bay Company Archives at the Archives of Manitoba.** The HBCA is part of the Archives of Manitoba and holds servants' contracts and pre-1870 records from almost five hundred HBC posts [S9].

## 5. Trace a British Home Child through the party and the agency

- **Date the movement correctly.** More than 100,000 children were sent from the British Isles between 1869 and the late 1930s. The Fairbridge Society brought some Middlemore children to a farm school in British Columbia between 1936 and 1948 [S10].
- **Search LAC's Home Children index in Collection Search.** It is built mainly from passenger lists. Where lists were missing or unreadable, LAC filled gaps from other immigration records, and it added a Boards of Guardians register [S10].
- **Search the party, not the family.** The child usually travelled in an agency party, not with relatives. LAC gave each group of children travelling together a code [S10]. Search by that code to see the whole party and its arrival.
- **Request the agency's own case records.** Barnardo's holds the records of its child migrants and also those of the Marchmont, Annie Macpherson and Liverpool Sheltering Homes. It releases them through its Family History Service, with the signed consent of the nearest surviving descendant [S11].

## Close with a routing packet

Return:

- **Coverage rows:** for each province searched, the start date, gaps, archive cut-off per event type with the date read, and the office for later years.
- **Search rows:** each index, series or image set searched, the years it covers, the result (found, not found, outside coverage, restricted) and the locator.
- **Military rows:** the war, the force, the access category (CEF online, WWII open war dead, WWII closed survivor) and, for a closed file, the ATIP request and the proof of death or consent it needs.
- **Indigenous-series rows:** the series and finding aid searched, the band, any band or ticket number found, and any restricted years.
- **Home Child rows:** the agency, the party code, the ship and arrival date, and the agency record request.
- **Gaps:** registration gaps such as Nova Scotia 1877–1908, years past a cut-off, and restricted series.

The model assembles this packet. The researcher decides identity and kinship.
