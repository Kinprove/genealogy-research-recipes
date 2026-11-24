---
id: "institutional-patient-record-recovery"
title: "Recover an asylum or state-hospital patient through custodians, courts and newspapers"
summary: "Find asylum or state-hospital patient records through custodians, courts and newspapers, including Dutch admission correspondence."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "INSTITUTIONAL-PATIENT-RECORD-RECOVERY-01", "text": "Never treat a refusal, a form letter or a court-order requirement as evidence that no file exists. Log it as an access outcome and switch to the court and newspaper routes below."}]
handoff: []
checked: "2026-11-07"
checked_basis: "checked 2026-11-07"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request", "third-party-tool"], "contact": []}
router: {"section": "Record types in any country", "group": "Births outside marriage and institutions", "order": 288}
---

# Recover an asylum or state-hospital patient through custodians, courts and newspapers

Use when an ancestor's asylum, state-hospital or similar institutional file is closed, lost or
only partly released. Three routes recover the patient: the institution's current custodian,
the committing court, and newspaper court reports. This recipe covers the access route, the
copy product that came back, the commitment search and the admission estimate.
For complete-file versus abbreviated copy handling in pension files, use
[pension file recovery § 3](us-military-pension-file-recovery.md).
For the documents in a probate court case, use
[probate case inventory](probate-case-document-inventory.md).
For newspaper coverage and OCR problems, use
[newspaper search recovery](newspapers-com-search-recovery.md).
For identity rulings, use
[evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- Do not answer "sealed, nothing can be done"
- 1\. Identify the current custodian and its access rules
- 2\. Ask for the complete file and record what actually came back
- 3\. Search the committing court and newspaper court recaps
- 4\. Estimate admission from an in-institution death certificate
- 5\. Use annual reports only as context
- Close with a patient-record packet

## Do not answer "sealed, nothing can be done"

A general privacy concern is not a search result. Access depends on the custodian and on the
state, and the presenters' own outcomes show how far apart states are [S2], [S6]:

- **Connecticut:** The state archives released a grandmother’s Norwich State Hospital file after her granddaughter documented her descent [S2 @2026-11-19], [S10 @2026-11-19].
- **New York:** The same researcher received a refusal letter from a New York state hospital after the patient’s death [S2 @2026-11-19]. The Office of Mental Health says it does not provide copies for genealogy searches and cites Mental Hygiene Law §33.13 for confidentiality [S9 @2026-11-19]. Record the custodian’s wording and the purpose of the request.
- **Privacy gate:** <!-- privacy-gate: request --> A court petition or direct request for a
  patient file sends the requester's proof of descent and can open records naming possibly
  living relatives; answer the privacy gate in `SKILL.md` before you petition or request.
- **Illinois:** A judge’s order was required for Crow’s search for a relative who died at the state hospital in Kankakee in 1899 [S6 @2026-11-19]. Check the present custodian’s eligibility rules and which group your requester is in before you go to court.
- **Ohio:** Crow says access "depends on the time period" [S6 @2026-11-19]. Confirm the current
  eligibility and documentation requirements with the custodian; do not infer them from
  family closeness or a death date alone.

Crow warns against assuming the records are closed, because a handful of states have open
records [S6]. Find out the actual rule before you advise the user. Never treat a refusal, a
form letter or a court-order requirement as evidence that no file exists. Log it as an access
outcome and switch to the court and newspaper routes below.

In Dutch research, a child's marriage supplements are a possible source for a parent's
reported inability to consent. Inspect the actual papers for the wording and any named
institution, place, date or reference; carry a supplied locator into the institutional search
below. Hoitink suggests this discovery route. An incapacity statement alone does not establish
a diagnosis or admission, and the supplement may name no institution. [S7]

## 1. Identify the current custodian and its access rules

- Search for the hospital name with the words *patient records*. Mangin found the Norwich State Hospital collection in the Connecticut State Archives. Her 2018 article cites RG 021:008 for 1904–1996 [S2 @2026-11-19], [S10 @2026-11-19]. The state library’s archival guide describes Norwich patient records for 1904–1966 under RG 021 [S13 @2026-11-19]. Check the patient series for the date you need.
- For Columbus State Hospital, Crow names Ohio History Connection [S6 @2026-11-19]. The search-result excerpt from the repository’s older guide describes transferred hospital collections and identifies confidentiality under Ohio Revised Code 5122.31. [S11† @2026-11-19] The statute allows Ohio History Connection to release records to the deceased patient’s closest living relative on request. Under §5122.31(A)(14), records and reports concerning a person dead at least 50 years are no longer confidential under that section [S14 @2026-11-19]. Check which collection covers the patient.
- Write down every access condition the custodian states, kept as separate entries:
  - **Who may request.** Mangin documented the Norwich patient’s death and linked each generation to herself with birth certificates [S2 @2026-11-19], [S10 @2026-11-19]. Record which documents the custodian accepted in your case.
  - **Years since death or record age.** Pennsylvania processes research requests if the patient has been dead at least 50 years or the record is at least 75 years old. [S12 @2026-11-19] Check the proof required before using the mail-in request below.
  - **Mixed-date volumes.** The Pennsylvania archivist measured the age of a register from its latest entries [S3 @2026-11-19], [S4 @2026-11-19]. Identify the patient’s entry date and the closing date of the volume before planning a visit.
  - **Court-order requirements**, and who is exempt from them (see Illinois above) [S6 @2026-11-19].
- Record the order of deaths and the estate representative’s authority. Luxenberg’s mother survived her sister, the patient. He reports that he first became his mother’s personal representative, then could open his aunt’s estate; being the surviving nephew did not establish standing [S1 @2026-11-19]. Check which authority the custodian recognizes for this patient.
- **Privacy gate:** <!-- privacy-gate: request --> A mail-in request for patient files and
  register entries sends family proof and can return pages naming possibly living relatives;
  answer the privacy gate in `SKILL.md` before you send it.
- Plan for mixed-date registers at the Pennsylvania State Archives. Patient entries sit in
  registers covering many years. If the page with your patient also carries entries that are
  still restricted, or the volume runs past the 75-year mark, the archivist says staff may not
  bring the original out, and it depends on the record [S3 @2026-11-19], [S4 @2026-11-19]. The archivist calls a mail-in
  request "the safest way": staff copy the original or, if the page can't be copied, abstract
  the entry, and send everything they hold for the patient [S3 @2026-11-19], [S4 @2026-11-19]. Make a mail-in request
  first. Don't travel on the assumption that the volume will be produced.
- These thresholds are the Pennsylvania State Archives' own. Do not carry them to another
  custodian.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Patient index searches send the
deceased patient's name and any search dates or places to MyHeritage or Scottish Indexes.
Answer the privacy gate in `SKILL.md` before searching. Keep case papers and details about
anyone who may be living local.

**Scotland.** Search for the deceased patient in MyHeritage's *Scotland, Mental Health Records,
1858–1921* or the Scottish Indexes *Mental Health Records* index. Record the admission date,
asylum and location, and any birth or in-asylum death date shown.
[S15 @2026-11-22] [S16 @2026-11-22] [S17 @2026-11-22] [S18 @2026-11-22] [S21 @2026-11-22]

Use the admission date and asylum to locate the entry in the National Records of Scotland's
*General Register of Lunatics in Asylum* (MC7). Save the volume and entry number. Check the
register's outcome columns before reading a date as a death. If no death date is given, leave
it open and seek a death registration or other independent death record.
[S17 @2026-11-22] [S19 @2026-11-22] [S21 @2026-11-22]

For a possible pre-1858 admission, search the opening entries of MC7/1 for people already
resident on 1 January 1858. If the search misses, look for surviving records of the individual
asylum and the relevant sheriff court. A patient who left before that date falls outside the
opening list.
[S15] [S16] [S17] [S20] [S21]

**Adelaide.** For a deceased patient's 1902–1925 admission, search MyHeritage's *Australia,
South Australia, Royal Adelaide Hospital Admissions*. Record admission date, residence, birth
year and birthplace, and any discharge date, death date or arrival ship shown.
[S22 @2026-11-22] [S23 @2026-11-22]

Check State Records of South Australia's GRG 78/49 admission registers for the underlying
entry and for dates outside the MyHeritage index. Use the volume, year and admission number
from the archive's index to locate the entry. If the online index misses the patient, check
the original indexes in GRG 78/46. [S24 @2026-11-22]

If the entry gives a length of residence in South Australia, count back from admission to
estimate an arrival window. Search passenger lists by the recorded ship name and likely year.
Compare the passenger entry with the admission details before identifying the traveler. [S25] [S26]

## 2. Ask for the complete file and record what actually came back

- **Privacy gate:** <!-- privacy-gate: request --> Asking for a complete patient file, or for
  other relatives' files, can bring back interviews, photographs and health details about
  possibly living family members; answer the privacy gate in `SKILL.md` before each request.
- Ask for everything the custodian holds for the patient. Compare the prices for selected pages and a full copy. When her great-grandfather’s file exceeded the standard fee, Allen chose the full copy and received his admission photograph and an interview with his wife [S3], [S4].
- Give each item received one product label: **copy of original**, **staff abstract**,
  **staff-selected highlights**, or **refusal/no response**. Don't treat an abstract or a set
  of highlights as the whole file. Write down what the product leaves out, if the custodian
  said.
- Transcribe the record group, file and roll from the archive’s packet so you can locate or cite each item again [S3], [S4]. Keep a separate entry for each relative.
- Ask whether other relatives were patients too. Norwich staff identified three additional relatives whose files Mangin subsequently obtained [S2]. Apply the checkpoint above to each separate request.
- Check dated visits and correspondence against the family account. The family said a husband had abandoned his wife; her Norwich file recorded his visits and letters to the superintendent after her 1908 admission [S2]. Those entries document contact. His motives remain unknown.

Check the case papers, including loose sheets, and admission forms for sibling and child counts. Preserve the
field wording, especially when it counts only living children. Use differences between the
recorded counts and the working family group to look for missing relatives. [S27]

Use a child's stated age at death to narrow the death-record search. If the age survives as
an uncertain recollection, as in the account from the available excerpt [S28], carry forward
the possible ages until the case papers or a death record resolves them.

## 3. Search the committing court and newspaper court recaps

- Work out which county the patient was committed from. Search that county's court records for
  a commitment or sanity proceeding. Depending on the jurisdiction, the court may be probate or
  civil [S6]. For a reported voluntary admission in Detroit in 1940, Luxenberg searched for a legal proceeding in Wayne County Probate Court [S1]. Search its docket even if the family described the admission as voluntary.
- Check retention, the docket and the underlying case file separately. Log a sealed or redacted file as an access outcome. An unavailable hospital file does not establish whether a court file survives [S1], [S6].
- Search local newspapers for weekly court summaries around the likely commitment date. Crow
  says most newspapers ran a recap of the court's rulings, sometimes only a line or two per
  matter [S6].
- Keep a search register. For each search, record the court and record series, the date span,
  the name forms used, and the result (hit, no hit, unavailable or not searched). For
  newspapers, record the title and issue range. A missing court entry is bounded by what you
  actually searched.

For a Dutch case, also check the relevant municipality's archival descriptions for
admission-related correspondence. Hoitink identifies municipal correspondence about forced
admission as a possible source. Add a separate search target only where the local description
supports the series and period, retaining its own locator. This is not evidence that
notification was required or that a notice survives for the person. [S7]

Where clues suggest municipal funding, check whether the municipality's archival
descriptions include registers of decisions or resolutions for the period. From a
relevant entry, copy the decision date and any court or authorization reference. Hoitink traced a death in Deventer to a Leeuwarden resolution abstract dated 6 November 1841. It describes a court order, the city’s decision to pay and its request for permission to place the patient in Deventer [S8]. Use those references to seek the resolution and order.

## 4. Estimate admission from an in-institution death certificate

- When the patient died in the institution, check the death certificate for a stated length of
  residence. Many certificate forms had a hospitals-and-institutions section asking how long
  the person had been at the place of death [S5]. Count back from the death date to get an
  **estimated admission interval**. Make it a range, because the figure usually comes from an
  informant and may be rounded.
- Compare the interval with opening dates, new wards and transfer records. At Exeter, Rhode Island, the school first admitted boys in 1908; the girls’ dormitory opened in 1913. The residence length on a death certificate pointed Mangin to 1913 and a possible transfer from the state almshouse [S5]. Look for the individual transfer or admission entry to test that inference.
- Label the result as an inference. It doesn't replace an admission register, a court order or
  a transfer list. Use it to narrow the court, newspaper and register searches.

## 5. Use annual reports only as context

- Find the institution's annual reports to the legislature or governor. Presenters describe
  looking in the Library of Congress catalogue and WorldCat [S5], and finding them on Google
  Books and Internet Archive or filed at a state library, archive or historical society [S6].
- Annual reports rarely name patients. Crow notes they often cover fires, outbreaks, reasons
  for commitment, menus and activities [S6]. The Exeter presenter treats them as self-serving
  and sets newspaper coverage of the institution against them [S5].
- Keep notes from annual reports and general newspaper coverage in a context section. Never
  turn a report's description of wards, treatment or conditions into a statement about the
  individual patient.

## Close with a patient-record packet

Return the following:

- the custodian and access log, with the requester's documented line of descent and proof of
  death;
- each product received, with its label and locators;
- the court and newspaper search register;
- the estimated admission interval, labelled as an inference, with the institutional history
  used to test it;
- context notes, kept apart from facts about the person;
- the next step for each remaining gap, such as an authorized requester, a court order, another
  county, or a newspaper title.
