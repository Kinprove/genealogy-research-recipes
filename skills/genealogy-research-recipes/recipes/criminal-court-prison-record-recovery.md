---
id: "criminal-court-prison-record-recovery"
title: "Trace a U.S. arrest or imprisonment to its trying court, prison and clemency records, with England/Wales and Swedish routes"
summary: "Trace a U.S., English, Welsh or Swedish arrest or imprisonment to its court, prison and pardon records; a state or local court's case file belongs to court case-file recovery."
kind: "records"
scope: {"platforms": [], "tasks": ["Sing Sing name indexes"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "CRIMINAL-COURT-PRISON-RECORD-RECOVERY-01", "text": "Before choosing where to search for court files, establish which court tried the case and who holds the records now."}]
handoff: ["convict-transportation-record-chain", "court-case-file-recovery", "english-nonregister-record-recovery", "uk-census-and-1939-register-interpretation", "us-federal-court-case-file-recovery"]
checked: "2026-11-06"
checked_basis: "opened 2026-11-06"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request", "third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "United States: military, land, courts and law", "order": 142}
---

# Trace a U.S. arrest or imprisonment to its trying court, prison and clemency records, with England/Wales and Swedish routes

Use this recipe when an ancestor disappears from records and you suspect arrest, trial or imprisonment. It also applies when a census institution entry, newspaper report or family story names a prison. Before choosing where to search for court files, establish which court tried the case and who holds the records now. For U.S. cases distinguish federal, territorial and state jurisdiction; use the separate England and Wales branch for a no-fixed-abode lead in those jurisdictions. If the prison is already known, start with its admission record and copy the county and court term into the court-file search [S4]. Then work out which prison series survive and what access rules apply to them. Use [newspaper search recovery](newspapers-com-search-recovery.md) to find the arrest or trial report, and [census workflows](us-census-practical-workflows.md) to recover the institution enumeration. Identity and conflict rulings belong in [evidence/proof judgment](evidence-proof-judgment.md).

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
- England and Wales: search trial reports, wanted notices and charges
- Swedish monthly prison rolls: follow the annotations beyond the index
- Swedish police gazette: follow back-references beyond the register hit list
- Swedish court books: recover a separately surviving copy
- Weigh an inmate-list miss against other evidence
- Extract admission fields as self-reported leads
- New South Wales: search gaol photograph books and read the full card
- Output

## Choose available name indexes before browsing chronological registers

**Privacy gate:** <!-- privacy-gate: third-party-tool, request --> A name search or register
request can disclose an inmate's identity and alleged criminal history to Ancestry or an
archive, including someone who may be living. Answer the privacy gate in `SKILL.md` before
entering identifying search terms or sending a record request.

- Gather the triggers: a census line in a prison or asylum [S1], newspaper arrest, trial or incarceration reports [S1], [S3], and family accounts. Keep every family kernel, even ones that later prove wrong, and test each one [S3]. Some families avoid the subject, so a family's silence is not a negative [S1], [S3].

- The New York State Library lists the Ancestry collection *New York, U.S., Sing Sing Prison Admission Registers, 1865–1939* [S14 @2026-11-19]. The provider’s listing was partially read [S48 @2026-11-19]. The partnership offers eligible New York residents access with a free account [S47 @2026-11-19]. Check your subscription or library’s access if using another route.

- Start with the approximate period and check available **name indexes before requiring a date or inmate number**. Verify the result on the B0143 register image. For foreign-born prisoners, also search the Archives' name index to B0146 (1919–1944) for a date and consecutive number [S14], [S15].
- For later volumes without a name index, obtain a conviction/admission date window or inmate number before chronological browsing or a staff search. The 1940 census can supply prisoner numbers [S49]. Record the register, years and pages checked. A miss in the earlier online index does not cover later admissions [S14], [S15].
- Check the basis for confinement in the order or admission record. A prison could hold a debtor as well as a person convicted of an offence [S1].
- Do not assume jurisdiction from the offence label either. The same conduct (for example, liquor selling) could be prosecuted under state or federal law. Take the jurisdiction from the court of conviction, not from the type of crime.

A man missing from his family's household in a census is also a trigger: he may have been in prison that year [S22]. Look for him in that census's enumeration of institutions, where the institution's name heads the return; not everyone listed there as an inmate was a prisoner, because orphanages and hospitals also listed inmates [S23]. If he was imprisoned, search the county court records for a divorce filed during or after the sentence [S22]: early in the 20th century, imprisonment was a legal ground for divorce in 39 of the 49 U.S. divorce jurisdictions [S24]. Use [court case-file recovery](court-case-file-recovery.md) for that file.

## Determine the trying court and its present custodian

- **Identify the court that sat in the place at the time.** Tanner reports retrieving Samuel Linton’s 1887 Utah cohabitation case from NARA Denver [S1]. For the federal territorial district court, use RG 21, M1401 (1870–1896) [S53].

- NARA’s digitisation-partner list identifies the online M1401 collection [S55 @2026-11-19]. FamilySearch provides a name index and cites Fold3 for the territorial case files [S56 @2026-11-19].

- For Utah’s First District, match the division to the case files: southern Series 1521 or northern Series 1529 [S50], [S51]. The register of unlawful-cohabitation actions, Series 28377, covers 1889–1891 and cannot contain an 1887 arrest [S16], [S51]. The inventory records a January 2025 loan to the Museum of Utah. Confirm where to request it before a visit [S51].
- Trace arrest, charge or indictment, preliminary proceedings, trial or plea, sentence and place of confinement. Search for the court and prison files separately [S1].
- Do not assume the prison was in the home state. A federal prisoner could be held in any federal prison with space [S1]. Alcatraz, for example, held federal inmates convicted across the country.
- Write one routing row per lead: the court, its jurisdiction level, the evidence for that level, the current custodian of the court records, and the likely custodian of the prison records.

**Read “no bill” as the grand jury’s refusal to indict on that bill.** A grand jury could return a true bill on one count or defendant and ignore another [S28]. A history counts 1811 Monaghan no-bills as acquittals despite the absence of a trial verdict [S29]. Read the finding for each charge and defendant. The notation alone gives no reason for it, including whether witnesses were unwilling to testify [S27].

**Distinguish an execution order from evidence it was carried out.** Search the newspapers following the order, then read the issue date on the page or masthead [S26]. The account of Sarah Kirk’s 1787 Delaware case cites the *Delaware Gazette* of 19 December, indexed as 9 December [S25]. Record the issue date separately from the date reported for the event.

## Route the request and log it

- **Privacy gate:** <!-- privacy-gate: request --> A Bureau of Prisons, department of corrections or state archives request asks for a file about an inmate who may be living, and it may name living relatives. Before any request below, answer the privacy gate in `SKILL.md` first. This includes clemency or parole requests to a governor's office or parole board, and pardon-file requests to NARA or the responsible pardon office.
- **Federal conviction:** identify the penitentiary and conviction date. Check NARA’s RG 129 series descriptions and prison guide for Alcatraz, Atlanta, Leavenworth or McNeil Island [S58]. Check whether your inmate was held at one of those penitentiaries or falls in the notorious-offenders series before you file any Bureau of Prisons request. For a notorious-offender file, look for the Bureau identifier [S54]. If your date or prison falls outside the identified series, ask the Bureau about retention and referral [S2].
  - Carry the file number through each referral and record what the office actually supplied. In a reported request the Bureau’s first reply was an extract, and it later referred the researcher to NARA with a file number [S2]. Ask the custodian which proof of death, consent or redaction options apply to that file. Keep a redacted copy identified as such.
- **State conviction:** start with that state's department of corrections [S2], then check the state archives. The Old Idaho State Penitentiary’s historical records include description-of-convicts volumes (AR 42/2) [S4]. For Sing Sing in New York, use the series distinctions below [S49].
- **State clemency and parole:** check the governor's clemency papers and parole-board records as separate series, including when the prison file is missing. Establish the responsible authority, period and current custodian through the state archives or agency. New York's A0597 clemency files, for example, can contain petitions from prisoners and relatives; Utah's Series 328 pardon applications can include court and biographical material. Record an application, recommendation and actual grant or denial separately. A petition does not show that clemency or parole was granted. [S17], [S52]
- **Federal pardon or commutation:** search federal pardon applications separately in **NARA RG 204, Office of the Pardon Attorney**. Its historical guide describes pardon case files for 1853–1963, dockets and indexes, with some indexes retained by the pardon office. Use the particular series' current catalogue entry to establish custody, coverage and access before requesting a file. Do not assume the prison's NARA facility holds it, or that an application establishes a pardon. [S18]
- Record in the request log: agency, form, date sent, date answered, file number quoted, documents supplied (death certificate, kinship proof), whether you gave consent or accepted redaction, and what you actually received (extract, redacted copy or full file).
- Death status matters for access. Note whether the inmate is dead, how long ago, and whether the children are living [S2].

**Federal pardons outside RG 204's case files:** RG 204's pardon case files begin in 1853. From 1789 to 1853 the Secretary of State and the Attorney General shared responsibility for exercising the President's pardon power, and the State Department issued pardon warrants until 1893. Search the State Department's pardon files, 1789–1893, in RG 59, and RG 204's abstracts of State Department pardon cases, 1793–1853. Applications for amnesty, Civil War and later, are in RG 94 [S18 @2026-11-13].

## Inventory surviving series and access rules

Use the series descriptions to record what survives for Sing Sing and how it can be searched [S49].

- The New York State Archives reports holding B0143 admission registers and no general inmate case files apart from files of some executed prisoners [S49 @2026-11-19]. Its B0145 series describes case files for inmates sentenced to electrocution, 1939–1963 [S57 @2026-11-19].

- An archive’s statement about its holdings leaves destruction unresolved. Seek a disposal record before treating the presenter’s report of destroyed files as established [S3], [S49]. For an admission, check the indexes above before requesting a chronological search [S14], [S15].
- B0145 describes warrants, investigations and reports on the execution and remains [S57]. A presenter also mentions visitor lists, family letters, photographs and last-meal requests. Check the individual file for those items [S3].
- Record access by series, repository and date. Ask the holding office what is available and keep its written response [S3], [S4]. A restriction on one kind of record does not establish that the entire prison collection is closed.
- Classify each series as **inspected**, **restricted**, **destroyed**, **not held by custodian**, **referred elsewhere** or **not yet asked**. A restricted, unheld or destroyed series does not mean "no record".
- Check gaps in an index against the original cards. In a reported NYPD Bertillon-card search the index jumped from 14885 to 14889; the researcher sought an on-site check of the missing numbers [S5]. Compare the card’s arrest date and charge with contemporaneous newspaper coverage before linking it to a relative.

## England and Wales: follow a no-fixed-abode incident beyond a census miss

Use this branch for a Victorian person described as having *no fixed abode* or recorded through a criminal-justice or welfare encounter. Keep the household census search open through [UK census interpretation](uk-census-and-1939-register-interpretation.md), including the actual institution and open-air-return coverage for the census year. Do not infer exclusion from all pre-1911 censuses. GenealCymru's historical account motivates the newspaper, prisoner-calendar, police and workhouse leads below [S8]; it does not verify a person's identity or a complete life history.

1. From a newspaper report or police-register entry, retain the literal name and aliases, occupation, stated age or birthplace, incident date and place, named court, prison and institution. Search supported name forms in the local press, including Welsh-language papers for Welsh cases. Keep reported arrest, accusation, trial, sentence and request for relief as separate events; a report that someone asked for admission does not establish admission.
2. Use the named court and trial year to select a relevant prisoner calendar; use the named prison and date to seek its register. The National Archives describes calendars for assizes and quarter sessions and notes that prisoner records are divided between national, prison and local archives [S9]. Check each series' actual court, year and institutional coverage before searching. Copy the calendar's court/date and any references into the court-file queue; retain the calendar and retrieved proceeding separately. A calendar is not the person's whole criminal history.
3. Treat a constabulary register or police return as its own series. Establish the responsible force, period, custodian and fields actually indexed; a census-night police return is a different target from a criminal register. Follow any named court or institution with its recorded date, rather than assuming every police record implies conviction.
4. For a reported workhouse encounter after 1834, identify the dated poor-law union through [English and Welsh nonregister routing](english-nonregister-record-recovery.md#1-build-the-dated-jurisdiction-table-before-choosing-a-series). Seek surviving admission/discharge records at the local or county archive [S10]. Keep a refusal or relief request distinct from an inmate entry. Central poor-law correspondence can mention exceptional individual cases, but does not replace the workhouse's everyday records [S10]. If another institution is named, establish its own custodian and surviving admission series separately.

**Privacy gate:** <!-- privacy-gate: request --> An order for copies of assize records names the defendant, the charge and the trial, and sends them to the archive or to a record agent. A trial from the 20th century can concern a defendant or relatives who are still living. Answer the privacy gate in `SKILL.md` before ordering copies.

When the charge was too serious for quarter sessions, look for the trial at the assizes [S19 @2026-11-12]. The National Archives files assize records by circuit, each with its own ASSI series, from 1559 for England and from 1831 for Wales; take the county's series from its guide's county appendix for the trial year, not from a fixed circuit list, because the six circuits of the period up to 1876 were later regrouped [S20 @2026-11-12]. Cheshire joined the assizes only in 1830, and Durham and Lancashire in 1876: search their earlier trials in the palatinate court records, and Welsh trials of 1543–1830 in the National Library of Wales's Crime and Punishment database [S20 @2026-11-12]. Start with the crown and gaol books for the charge, plea, verdict and sentence. Expect depositions to survive mainly for capital cases such as murder and riot, and expect to use the originals at Kew or order copies, because the assize records are not online [S20 @2026-11-12]. Look for London and Middlesex trials at the Old Bailey instead: from 1834, as the Central Criminal Court, its records are in TNA's CRIM series, and the earlier London and Middlesex sessions records are at the London Archives [S21 @2026-11-12]. An entry in Ancestry's criminal registers gives the court and trial date to follow; it is not the assize record (see [the convict transportation chain](convict-transportation-record-chain.md)).

**Return:** one incident-to-record chain, retaining each source's date, descriptors, procedural stage, selected custodian/series, retrieved locator and result. Compare those fields before linking appearances, preserve conflicting namesakes, and quote punitive labels as the record's descriptions. Report missing or uninspected series explicitly; neither an institutional record nor its absence supplies a complete account of the person's life.

## England and Wales: search trial reports, wanted notices and charges

**Privacy gate:** <!-- privacy-gate: third-party-tool, request --> A name search on a trial-report,
newspaper or catalogue site, or a request to open a closed file, sends the person's name and the
alleged offence to that service or archive, and a 20th-century defendant, victim, witness or
relative may still be living. Answer the privacy gate in `SKILL.md` before entering a name or
sending the request.

For a trial at the Old Bailey up to 1913, search the Old Bailey Proceedings Online by the names of victims and witnesses as well as defendants. It is a full-text edition of the published accounts of trials at London's central criminal court from 1674 to 1913, with names, occupations, places and dates tagged [S34 @2026-11-14]. Extract stated kinship, addresses and occupations for victims and witnesses as well as defendants [S30 @2026-11-14]. The accounts are not verbatim transcripts: before the 1720s they hold little testimony, until the early 19th century they leave some testimony out, and the 19th-century accounts, though fuller, omit sexual details, particularly in rape and sodomy trials [S34 @2026-11-14]. Cite a quoted statement as the published account's wording, not as a transcript of what the witness said.

Search newspapers for notices about men who absconded. In the *Poor Law Unions’ Gazette*, look for descriptions of men whose families were chargeable to the union. Compare identifying marks, occupation, suspected whereabouts and companions [S35], [S30]. Repeated advertisements may refer to the same disappearance.

Also search the *Illustrated Police News* (1864–1938), including the digitised examples described by Findmypast and an independent researcher [S36], [S37], [S30]. Use its reports and illustrations as leads to the original court proceedings.

To find a prosecution of a man for sex with another man, search The National Archives' Discovery catalogue by the period's charge words, adding a name, county or court. TNA lists among them sodomy, buggery, gross indecency, indecency, importuning, soliciting, unnatural act and unnatural offences [S39 @2026-11-14]. Quarter sessions records are held in local archives: search "quarter sessions" with the county and choose the "Other archives" filter [S40 @2026-11-14]. Expect the records to concern men: female homosexuality was never explicitly criminalised, so lesbian relationships are generally absent from criminal records [S39 @2026-11-14]. Many 20th-century criminal records at TNA are still closed under the Data Protection Act; you can ask for a Freedom of Information review of a closed record [S39 @2026-11-14].

Read such a record as a record of a charge. An indictment names the accused and the offence, and depositions record the evidence; trial transcripts are very rare [S39]. A charge does not establish a relationship between men accused together, or either man's sexual orientation. A reported Kent quarter sessions certificate names two accused men but leaves their relationship unresolved [S38]. Treat the record as a sensitive finding. Keep a possibly living person's name and charge in the user's private research notes, and never publish or share them (privacy gate and Living people, in `SKILL.md`).

**Read "detained during His Majesty's pleasure" as an indefinite term.** The sentence sets no release date; under a queen, such as Victoria, the wording is "Her Majesty's pleasure" [S31 @2026-11-14]. Under the Criminal Lunatics Act 1800, a person found insane at the time of the offence was kept in custody "until His Majesty's pleasure shall be known" [S32 @2026-11-14]; today the sentence is used most often for juveniles, such as a person under 18 convicted of murder [S31 @2026-11-14]. For a person held as insane, look for the asylum rather than a prison release: TNA's guide points to HO 20 (1820–1843), HO 8 (1862–1875), HO 144 (1869–1941) and HO 145 (1882–1921) for criminals confined at Broadmoor and Bethlem after being certified insane at court or after imprisonment [S33 @2026-11-14].

## Swedish monthly prison rolls: follow the annotations beyond the index

Use this branch when a Swedish prison-roll name index leaves the court, proceeding date or next destination unclear. Open the original monthly return sent to *Justitiekanslern* and read the procedural and movement columns omitted from the index [S7].

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

A September 1826 return in the ArkivDigital demonstration records a proceeding and a later dispatch by extra prisoner transport to another court district [S7]. Follow each dated event in the corresponding court. A dispatch entry alone does not establish the receiving institution, arrival or verdict.

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
- Follow every back-reference in the remarks column to an earlier volume and section by hand, even where ArkivDigital has linked it; it links them only as far as possible [S12]. For a reference such as 1907 issue 104, section D1 [S11], open that year, issue and section and record the earlier entry as a separate observation.
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

**Check:** In the reported Arjeplog search, consecutive photographs did not settle whether the book lacked leaves; the presenter suggested checking for an appellate copy [S6]. Establish the survival of that copy, the existence of any appeal and its outcome from the corresponding records. This branch does not identify a civil or military authority for an
unlocated death inquiry, or establish criminality from a death or prison reference.

## Weigh an inmate-list miss against other evidence

- An inmate-list miss describes the list searched. A researcher reported that an Alcatraz list omitted Irving Wexler although his death certificate placed him there [S3]. The Bureau of Prisons’ released notorious-offenders list names Irving Wexler with identifiers 49345-I and 62691 and identifies NARA as the permanent custodian [S54]. Keep those identifiers with the separate file search.
- Write a conflict list: each list or index searched with its scope, and each item of contrary evidence (death certificate, newspaper report, census line). If a list misses the person while such evidence places them in the institution, search the next series whose documented coverage could include them: for a federal inmate, the institution's series at other branches, and the notorious-offenders series (RG 129, College Park) only when the inmate was a prominent offender of the kind it covers, as Wexler was [S3]. Name the next series or branch to search.

## Extract admission fields as self-reported leads

- From a convict description, keep each field literally: name as written, alias field, age at admission, birthplace, occupation, parents living or dead, age when the inmate left home, religion, literacy, prior imprisonment, and nearest relative with residence [S4].
- Mark every field as given by the inmate or an unknown informant. Birth year is calculated from admission age, so record it as a range.
- A ticked alias box with no alias written means the recorded name may itself be an alias [S4].
- Use the named relative, the relative’s stated residence and the inmate’s birthplace to search the previous generation in that place [S4]. Confirm the suggested relationship in an independent record. For the Idaho example, consult the Idaho State Archives’ inmate files and convict descriptions (AR 42/2).

If no mugshot turns up, read the prison admission register for a written physical description [S59]. For an early Sing Sing admission, check the B0143 register entry for height, complexion, hair and eye color, and other physical characteristics [S60]. Transcribe any recorded scars, tattoos and notes on teeth, and keep the admission date and register locator with the description [S61].

## New South Wales: search gaol photograph books and read the full card

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A gaol search sends the inmate's identifying details to MyHeritage and may disclose a living person's connection to a criminal record. Answer the privacy gate in `SKILL.md` before entering identifying search terms.

Search MyHeritage's *Australia, New South Wales, Gaol Inmates & Photos, 1870–1930* for an inmate held in New South Wales. It draws on photographic description books from several gaols [S42 @2026-11-18]. Check the individual gaol's coverage before drawing conclusions from a miss [S43 @2026-11-18]. Treat a hit as evidence of a gaol record and require separate evidence of transportation [S41 @2026-11-18].

Read the full card for the gaol and prisoner or portrait number, birthplace, recorded birth date or year, occupation, physical description and convictions [S41], [S42], [S44]. Establish identity from the written identifiers and corroborating records. Never use facial resemblance as identity evidence.

If the convictions field cites a previous report, record the earlier count with that reference and list each conviction itemized on the card separately. Keep the earlier convictions unresolved until you recover the earlier report or the individual conviction records [S41], [S44].

In the education field, transcribe `R & W` as written and record its meaning separately as the gaol's statement that the inmate could read and write [S41], [S45].

In the marks or special features field, transcribe the wording of tattoos, including personal names. Keep a name as a lead in the private notes and require separate evidence of the relationship [S41], [S46].

## Output

Return:

- the jurisdiction-and-custodian routing row
- the request log
- the surviving-series inventory with each series' status
- the conflict list on whether the person was held
- the admission-field lead table, with the informant marked for every field
- when monthly Swedish rolls are used, the dated annotation-to-record chain, with unresolved identities and transport targets kept separate

Name the next custodian, series or on-site check for every open gap.
