---
id: "criminal-court-prison-record-recovery"
title: "Trace a U.S. arrest or imprisonment to its trying court, prison and clemency records, with England/Wales and Swedish routes"
summary: "From an arrest, prison or census-institution lead, find the court that tried the case and recover U.S. prison, inmate, clemency and pardon records; a state or local court's case file belongs to court case-file recovery, a federal one to federal court recovery. Its England/Wales and Swedish sections cover only no-fixed-abode leads and Swedish prison, police-gazette and court-copy searches."
kind: "records"
scope: {"platforms": [], "tasks": ["Sing Sing name indexes"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "CRIMINAL-COURT-PRISON-RECORD-RECOVERY-01", "text": "Before choosing where to search for court files, establish which court tried the case and who holds the records now."}]
handoff: ["convict-transportation-record-chain", "court-case-file-recovery", "english-nonregister-record-recovery", "uk-census-and-1939-register-interpretation", "us-federal-court-case-file-recovery"]
checked: "2026-11-06"
checked_basis: "opened 2026-11-06"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request", "third-party-tool"], "contact": []}
router: {"tier": "pointer", "group": "Courts, legislatures, prisons and institutions", "order": 1105}
---

# Trace a U.S. arrest or imprisonment to its trying court, prison and clemency records, with England/Wales and Swedish routes

Use this recipe when an ancestor disappears from records and you suspect arrest, trial or imprisonment. It also applies when a census institution entry, newspaper report or family story names a prison. Before choosing where to search for court files, establish which court tried the case and who holds the records now. For U.S. cases distinguish federal, territorial and state jurisdiction; use the separate England and Wales branch for a no-fixed-abode lead in those jurisdictions. If the prison is already known, open that prison's admission record first to find the trying court: the Idaho convict description in S4 records the county (Washington County) and the court term (May 1896) [S4]. Then work out which prison series survive and what access rules apply to them. Use [newspaper search recovery](newspapers-com-search-recovery.md) to find the arrest or trial report, and [census workflows](us-census-practical-workflows.md) to recover the institution enumeration. Identity and conflict rulings belong in [evidence/proof judgment](evidence-proof-judgment.md).

The detailed jurisdiction, inmate-file and request routes below are **U.S. routes**; the
England/Wales and Swedish sections cover the specific retrieval problems they name, not all
British or European criminal records. This recipe finds which court tried the case and recovers
the prison, inmate, clemency and pardon records. For a state or local court's case file itself (its
pointer records, loose papers and stage-by-stage inventory), use
[court case-file recovery](court-case-file-recovery.md); for U.S. federal court case files, use
[U.S. federal court recovery](us-federal-court-case-file-recovery.md). For a British conviction
followed by overseas transportation, use [the convict transportation chain](convict-transportation-record-chain.md).

## Contents

- Choose available name indexes before browsing chronological registers
- Determine the trying court and its present custodian
- Route the request and log it
- Inventory surviving series and access rules
- England and Wales: follow a no-fixed-abode incident beyond a census miss
- Swedish monthly prison rolls: follow the annotations beyond the index
- Swedish police gazette: follow back-references beyond the register hit list
- Swedish court books: recover a separately surviving copy
- Weigh an inmate-list miss against other evidence
- Extract admission fields as self-reported leads
- Output

## Choose available name indexes before browsing chronological registers

**Privacy gate:** <!-- privacy-gate: third-party-tool, request --> A name search or register
request can disclose an inmate's identity and alleged criminal history to Ancestry or an
archive, including someone who may be living. Answer the privacy gate in `SKILL.md` before
entering identifying search terms or sending a record request.

- Gather the triggers: a census line in a prison or asylum [S1], newspaper arrest, trial or incarceration reports [S1], [S3], and family accounts. Keep every family kernel, even ones that later prove wrong, and test each one [S3]. Some families avoid the subject, so a family's silence is not a negative [S1], [S3].
- Start with the location and approximate period, but check available **name indexes before requiring a date or inmate number**. Sing Sing admission registers (B0143) are searchable on Ancestry as *New York, U.S., Sing Sing Prison Admission Registers, 1865–1939*. The New York partnership offers free access to New York State residents with a free account; others need an applicable subscription or library access. Verify each result on the register image. [S14]
- For foreign-born Sing Sing prisoners, also search the Archives' name index to **B0146, List of Foreign Born Prisoners, 1919–1944**. It can supply an admission date and inmate number; it is not a general index to all admissions. [S15]
- For later, unindexed registers (including the 1940–1970 period), obtain a conviction/admission date window or inmate number before chronological browsing or a staff search. The 1940 census can supply inmate numbers. One presenter's five-year browsing window is an example of that route [S3], not a prerequisite for searching the earlier online name index. Record which index and years you searched, or the window/number and pages browsed. A failed name search is not proof that the prisoner was never admitted. [S14], [S15]
- Imprisonment did not always follow a crime. The presenter's example is imprisonment for debt [S1]. Polygamy/cohabitation prisoners are a different case: the presenter notes they were convicted under the law of the time [S1]. Do not assume the offence category from the institution alone.
- Do not assume jurisdiction from the offence label either. The same conduct (for example, liquor selling) could be prosecuted under state or federal law. Take the jurisdiction from the court of conviction, not from the type of crime.

## Determine the trying court and its present custodian

- Find out which court actually tried the case before you search local county records. Tanner reports that his ancestor Samuel Linton was arrested for unlawful cohabitation in 1887 and was convicted "not in a Utah court but in the district court". He found those district court records at the National Archives branch in Denver and obtained them by a paid request [S1]. In practice this means the federally appointed territorial district court, which sat in Utah. It does not mean a court outside the territory.
- For territorial-era cases, search two custodians. Utah district court records (Record Group 21) are at NARA Denver, and the territorial case files for 1870–1896 are filmed as NARA M1401, which can be searched on FamilySearch and Fold3. For the First District's separate state-archive holdings, seek the appropriate division's **criminal case files**, Series 1521 (southern) or 1529 (northern). Series 28377 is an unlawful-cohabitation **register of actions**, not the loose case files. Confirm its current loan/access status with the Archives before planning to inspect it; an older catalogue's public designation does not guarantee reading-room availability. Check M1401 and the applicable state-archive case series independently. [S16]
- Learn the procedural stages: arrest, charge or indictment, preliminary actions, trial or plea, sentencing, place of sentence [S1]. The court case file and the prison file are separate records, and each has to be traced on its own [S1].
- Do not assume the prison was in the home state. A federal prisoner could be held in any federal prison with space [S1]. Alcatraz, for example, held federal inmates convicted across the country.
- Write one routing row per lead: the court, its jurisdiction level, the evidence for that level, the current custodian of the court records, and the likely custodian of the prison records.

## Route the request and log it

- **Privacy gate:** <!-- privacy-gate: request --> A Bureau of Prisons, department of corrections or state archives request asks for a file about an inmate who may be living, and it may name living relatives. Before any request below, answer the privacy gate in `SKILL.md` first. This includes clemency or parole requests to a governor's office or parole board, and pardon-file requests to NARA or the responsible pardon office.
- **Federal conviction:** start with the series NARA still holds. A NARA History Hub reply says most individual federal inmate case files were temporary records and are not held by NARA. The exceptions include Alcatraz, Leavenworth, Atlanta and McNeil Island, and the notorious-offenders files. Check whether your inmate was held at one of those penitentiaries or falls in the notorious-offenders series before you file any Bureau of Prisons request. If none applies, file the request anyway, log the reply and classify the series from it.
  - A listener's 2007 account shows the request route [S2]. A county society redirected her to the Oklahoma corrections department, which sent her on to the Bureau of Prisons because, she reports, "bootlegging was a federal crime" [S2].
  - The Bureau's emailed public-information reply was a bare-bones extract of the file [S2]. Do not file such a reply as the prison record.
  - Clarifying the extract required a FOIA request form and a copy of the death certificate [S2].
  - The Bureau then said it no longer held the records and referred her to NARA with a specific file number [S2]. Log that number.
  - NARA required written consent from the inmate's family, or else the copy would be redacted. She accepted a redacted copy [S2].
  - The request ran from 20 May 2007 to about mid-February the following year [S2]. The host describes the resulting packet as thick, with photographs and psychological testing [S2].
- **State conviction:** start with that state's department of corrections [S2], then check the state archives. Historical state prison series often end up there: the Sing Sing admission registers are at the New York State Archives [S3], and the Old Idaho State Penitentiary records (AR 42/2, 1872–1973, including "description of convicts" volumes) are at the Idaho State Archives. Find the prison series in that state archives' finding aid.
- **State clemency and parole:** check the governor's clemency papers and parole-board records as separate series, including when the prison file is missing. Establish the responsible authority, period and current custodian through the state archives or agency. New York's A0597 clemency files, for example, can contain petitions from prisoners and relatives; Utah's Series 328 pardon applications can include court and biographical material. Record an application, recommendation and actual grant or denial separately. A petition does not show that clemency or parole was granted. [S17]
- **Federal pardon or commutation:** search federal pardon applications separately in **NARA RG 204, Office of the Pardon Attorney**. Its historical guide describes pardon case files for 1853–1963, dockets and indexes, with some indexes retained by the pardon office. Use the particular series' current catalogue entry to establish custody, coverage and access before requesting a file. Do not assume the prison's NARA facility holds it, or that an application establishes a pardon. [S18]
- Record in the request log: agency, form, date sent, date answered, file number quoted, documents supplied (death certificate, kinship proof), whether you gave consent or accepted redaction, and what you actually received (extract, redacted copy or full file).
- Death status matters for access. Note whether the inmate is dead, how long ago, and whether the children are living [S2].

**Federal pardons before 1853:** RG 204's pardon case files begin in 1853. From 1789 to 1853 the Secretary of State and the Attorney General shared responsibility for exercising the President's pardon power, and the State Department issued pardon warrants until 1893. Search the State Department's pardon files, 1789–1893, in RG 59, and RG 204's abstracts of State Department pardon cases, 1793–1853. Applications for amnesty, Civil War and later, are in RG 94 [S18 @2026-11-13].

## Inventory surviving series and access rules

- Ask the custodian which series survive. Do not assume a case file exists. For Sing Sing:
  - The presenter says the general inmate case files were destroyed years ago [S3]. The New York State Archives says only that it holds no Sing Sing inmate case files apart from some for executed inmates. Record that series as "not held by the State Archives", not as destroyed, unless you find a destruction record.
  - The admission registers survive at the State Archives in Albany [S3]. Start with the online 1865–1939 name search and the population-specific B0146 index where applicable; use a date or inmate number for unindexed chronological browsing (see above). [S14], [S15]
  - Case files for inmates sentenced to electrocution survive as series B0145 (1939–1963). The Archives' description lists warrants of execution, investigation reports and post-mortem/remains reports. The presenter says some files also include visitor lists, last-meal requests, family letters and photographs [S3]. Expect the listed contents, and treat the rest as possible.
- Check closure rules before you search. One presenter says some states open prison and jail records after a period while others say "never" [S4]. Idaho, for example, restricts some penitentiary records. Another presenter says rules vary by repository and record type, and that different federal agencies gave her conflicting access answers for the same record [S3]. Get the ruling in writing from the office that actually holds the series [S3].
- Classify each series as **inspected**, **restricted**, **destroyed**, **not held by custodian**, **referred elsewhere** or **not yet asked**. A restricted, unheld or destroyed series does not mean "no record".
- Check index numbers for gaps. The NYC Municipal Archives holds NYPD Bertillon identification cards, and the presenter used digitized cards from the city's records access website [S5]. A friend's index of the cards jumped from card 14885 to 14889, and he treated that as a possible indexing gap rather than lost cards. He arranged for someone to check the originals on site [S5]. He tied card 14885 to his relative by matching its arrest date (7 January 1908) and charge to a newspaper report dated the next day [S5].

## England and Wales: follow a no-fixed-abode incident beyond a census miss

Use this branch for a Victorian person described as having *no fixed abode* or recorded through a criminal-justice or welfare encounter. Keep the household census search open through [UK census interpretation](uk-census-and-1939-register-interpretation.md), including the actual institution and open-air-return coverage for the census year. Do not infer exclusion from all pre-1911 censuses. GenealCymru's historical account motivates the newspaper, prisoner-calendar, police and workhouse leads below [S8]; it does not verify a person's identity or a complete life history.

1. From a newspaper report or police-register entry, retain the literal name and aliases, occupation, stated age or birthplace, incident date and place, named court, prison and institution. Search supported name forms in the local press, including Welsh-language papers for Welsh cases. Keep reported arrest, accusation, trial, sentence and request for relief as separate events; a report that someone asked for admission does not establish admission.
2. Use the named court and trial year to select a relevant prisoner calendar; use the named prison and date to seek its register. The National Archives describes calendars for assizes and quarter sessions and notes that prisoner records are divided between national, prison and local archives [S9]. Check each series' actual court, year and institutional coverage before searching. Copy the calendar's court/date and any references into the court-file queue; retain the calendar and retrieved proceeding separately. A calendar is not the person's whole criminal history.
3. Treat a constabulary register or police return as its own series. Establish the responsible force, period, custodian and fields actually indexed; a census-night police return is a different target from a criminal register. Follow any named court or institution with its recorded date, rather than assuming every police record implies conviction.
4. For a reported workhouse encounter after 1834, identify the dated poor-law union through [English and Welsh nonregister routing](english-nonregister-record-recovery.md#1-build-the-dated-jurisdiction-table-before-choosing-a-series). Seek surviving admission/discharge records at the local or county archive [S10]. Keep a refusal or relief request distinct from an inmate entry. Central poor-law correspondence can mention exceptional individual cases, but does not replace the workhouse's everyday records [S10]. If another institution is named, establish its own custodian and surviving admission series separately.

**Privacy gate:** <!-- privacy-gate: request --> An order for copies of assize records names the defendant, the charge and the trial, and sends them to the archive or to a record agent. A trial from the 20th century can concern a defendant or relatives who are still living. Answer the privacy gate in `SKILL.md` before ordering copies.

When the charge was too serious for quarter sessions, look for the trial at the assizes [S19 @2026-11-12]. The National Archives files assize records by circuit, each with its own ASSI series, from 1559 for England and from 1831 for Wales; take the county's series from its guide's county appendix for the trial year, not from a fixed circuit list, because the six circuits of the period up to 1876 were later regrouped [S20 @2026-11-12]. Cheshire joined the assizes only in 1830, and Durham and Lancashire in 1876: search their earlier trials in the palatinate court records, and Welsh trials of 1543–1830 in the National Library of Wales's Crime and Punishment database [S20 @2026-11-12]. Start with the crown and gaol books for the charge, plea, verdict and sentence. Expect depositions to survive mainly for capital cases such as murder and riot, and expect to use the originals at Kew or order copies, because the assize records are not online [S20 @2026-11-12]. Look for London and Middlesex trials at the Old Bailey instead: from 1834, as the Central Criminal Court, its records are in TNA's CRIM series, and the earlier London and Middlesex sessions records are at the London Archives [S21 @2026-11-12]. An entry in Ancestry's criminal registers gives the court and trial date to follow; it is not the assize record (see [the convict transportation chain](convict-transportation-record-chain.md)).

**Return:** one incident-to-record chain, retaining each source's date, descriptors, procedural stage, selected custodian/series, retrieved locator and result. Compare those fields before linking appearances, preserve conflicting namesakes, and quote punitive labels as the record's descriptions. Report missing or uninspected series explicitly; neither an institutional record nor its absence supplies a complete account of the person's life.

## Swedish monthly prison rolls: follow the annotations beyond the index

Use this branch when a Swedish prison-roll index hit gives a name or alleged offence
but leaves the court, proceeding date or next destination unclear. ArkivDigital's
September 2024 demonstration opens monthly returns sent to *Justitiekanslern* and
reads columns that its name index does not expose [S7]. The index is an entry point,
not an abstract of every procedural or movement note.

1. Open the linked original roll image and retain the prison, return month/year,
   archive, volume, printed page and image locator. Read the whole entry across its
   columns and any continuation. Copy the literal name and abbreviation, occupation,
   stated origin and custody details; leave an uncertain expansion unresolved.
   Check the actual index and volume's date and institution coverage before treating
   a miss as informative. The demonstration's index counts and coverage are historical.
2. Separate the dates and roles before choosing the next record. Keep the roll's
   reporting month apart from admission, release, hearing, order and transport dates.
   Copy each action's wording and status: awaiting a decision, undergoing proceedings,
   ordered to leave and reported sent are different observations. An offence label or
   pending proceeding does not establish conviction or the final outcome. [S7]
3. Build a separate retrieval target for each authority or destination actually named,
   using the routing rows below. Identify its historical jurisdiction, surviving series
   and current custodian before requesting records. Preserve the roll reference beside
   each target so a failed lookup does not erase the original lead.

| Annotation in the inspected roll | Next retrieval target and limit |
| --- | --- |
| Named court, proceeding date and action | Locate that court's relevant minute or case series for the stated date/term; compare the retrieved entry's person and procedural stage. A hearing court or higher-court decision still awaited is not automatically a court of conviction. |
| Governor's office or other administrative authority | Preserve the authority, locality, date and action actually attributed to it. Ask its custodian whether corresponding interrogation or administrative papers survive. A release or passport statement alone does not show that an interrogation file exists or that the governor personally questioned the prisoner. |
| Onward transport, destination and date | Retain whether transport was ordered or reported as carried out. Follow the named receiving court or institution for the bounded destination/date question; request a cited transport document separately when a reference or finding aid identifies one. Do not invent a receiving prison from a court-district name. |

The demonstration's September 1826 example supplies both a dated court proceeding and
a later transport to another district [S7]. These are separate retrieval leads. A
transport annotation does not retrieve a transport order, prove arrival or establish
what happened in the receiving court. Keep a missing date, document reference or
receiving institution unresolved rather than filling it from the next plausible hit.

1. Compare other monthly hits only as candidate observations. Record the literal name,
   descriptors, institution and event dates for each, then test a proposed connection
   against those fields and the retrieved court or administrative record. The presenter
   explicitly warns that repeated hits for the same name need not be one person [S7].
   Retain conflicting or insufficiently identified rows separately; the reporting month
   alone neither dates a new imprisonment nor proves continuous custody between returns.
2. Add each followed reference to the existing routing row and request log. Record the
   source annotation, exact court/authority/destination, dated action, target series,
   requested item, retrieved locator and comparison result. Distinguish an inspected
   no-hit from an unsearched month, unindexed field, unavailable volume or unlocated
   administrative/transport paper. Pass identity and conflict rulings to the evidence
   workflow, preserving both the allegation and the procedural stage.

**Return:** a dated roll-entry and follow-up chain with one row per observation and
one result per target. This branch supplies a way to recover court, interrogation-authority
and movement leads; it does not establish current national index completeness, applicable
passport or vagrancy law, guilt, identity, a surviving file or an actual case outcome.

## Swedish police gazette: follow back-references beyond the register hit list

Use this branch for a Swede in police contact between 1878 and 1950. Search ArkivDigital's *Polisunderrättelser* (police gazette) name register, indexed for 1878–1950, by name and its variants [S11], [S12]. Check each hit's birth date against the person.

- Open each hit's page image. Record the year, issue number, section and the literal entry. The sections are A (wanted persons), B (detained persons and cancelled notices), C (miscellaneous notices), D (released prisoners) and E (stolen and lost property) [S13].
- Follow every back-reference in the remarks column to an earlier volume and section by hand, even where ArkivDigital has linked it; it links them only as far as possible [S12]. The presenter's example points to issue 104 of 1907, section D1 [S11]. Open that year, issue and section, and record the earlier entry as a separate observation.
- Do not treat the register's hit list as complete. Indexing errors and name variants can hide appearances that the back-references reveal. Log each one found only by following a reference.
- A gazette entry is a lead to the trying court, not proof of conviction. Add the named court, conviction date or prison to the routing row.

## Swedish court books: recover a separately surviving copy

Use this branch when an identified Swedish proceeding has an incomplete *dombok* entry.
Retain the court, year, term, paragraph and inspected page/image extent from the actual
record. A missing conclusion in one volume does not establish the case's outcome. [S6]

1. Compare the book's pagination and text with the image sequence. Record whether the gap
   appears to be an omitted image, a missing leaf or an uncertain continuation. Inspect the
   available volume for displaced continuations before describing the original as lost;
   consecutive viewer images do not establish consecutive surviving leaves.
2. Ask the custodian whether a matching *renovation* (a court-book copy sent to the
   *hovrätt*) survives. ArkivDigital points to the appellate court's *advokatfiskal* archive
   for this route, while warning that a copy may be unavailable for a late-nineteenth-century
   case. Establish the appropriate appellate authority and its actual court/year coverage
   before requesting a volume; the suggested archive name is not a surviving-copy locator.
3. If a docket, judgment or other inspected record establishes an appeal, retain its higher
   authority and case reference, and request that separate file. Look for transmitted copies
   of the lower court's papers and protocols. Follow a further appeal only when the records
   supply that link; an incomplete trial entry alone does not establish any appeal.
4. Inventory each recovered copy separately from the incomplete book. Compare the case,
   dates, paragraph and surviving overlap before using it to fill the gap; preserve differences
   and any missing ending. A copied judgment is not the missing original leaf. [S6]

**Artifact:** add a copy-recovery row to the routing and series inventory: original locator,
gap evidence, proposed copying or appeal authority, matching series coverage, requested
reference, copy actually inspected and unresolved text.

**Check:** ArkivDigital's Arjeplog example supplies a retrieval route, not a verified copy
for that case. Leave the copy's survival, an appeal and the outcome unresolved until their
records establish them. This branch does not identify a civil or military authority for an
unlocated death inquiry, or establish criminality from a death or prison reference.

## Weigh an inmate-list miss against other evidence

- An archivist's statement that someone is "not on the list" describes that list, not whether the person was held. NARA San Bruno holds the Alcatraz inmate files (1934–1963). The presenter reports that Irving Wexler was missing from its Alcatraz inmate list, even though a California death certificate and a New York Times article put his death at Alcatraz [S3]. Contemporary wire reports also place his death there, in June 1952. His file turned up in the Bureau of Prisons notorious-offenders series (RG 129) at NARA College Park [S3].
- Write a conflict list: each list or index searched with its scope, and each item of contrary evidence (death certificate, newspaper report, census line). If a list misses the person while such evidence places them in the institution, search the next series whose documented coverage could include them: for a federal inmate, the institution's series at other branches, and the notorious-offenders series (RG 129, College Park) only when the inmate was a prominent offender of the kind it covers, as Wexler was [S3]. Name the next series or branch to search.

## Extract admission fields as self-reported leads

- From a convict description, keep each field literally: name as written, alias field, age at admission, birthplace, occupation, parents living or dead, age when the inmate left home, religion, literacy, prior imprisonment, and nearest relative with residence [S4].
- Mark every field as given by the inmate or an unknown informant. Birth year is calculated from admission age, so record it as a range.
- A ticked alias box with no alias written means the recorded name may itself be an alias [S4].
- In the presenter's Idaho example, a nearest relative named as the father with a residence, together with a North Carolina birthplace, pointed the search to the previous generation in another state [S4]. Use such fields to target records. They do not establish parentage by themselves. The originals of this record type are at the Idaho State Archives (AR 42/2).

## Output

Return:

- the jurisdiction-and-custodian routing row
- the request log
- the surviving-series inventory with each series' status
- the conflict list on whether the person was held
- the admission-field lead table, with the informant marked for every field
- when monthly Swedish rolls are used, the dated annotation-to-record chain, with unresolved identities and transport targets kept separate

Name the next custodian, series or on-site check for every open gap.
