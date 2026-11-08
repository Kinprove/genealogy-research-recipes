---
id: "court-case-file-recovery"
title: "Recover a U.S. court case file from its pointer records"
summary: "Recover a U.S. state or local civil, chancery, divorce, criminal or incapacity case file through the records that point to it, then inventory its loose papers."
kind: "records"
scope: {"platforms": [], "tasks": ["Recover a U.S. state or local civil, chancery, divorce, criminal or incapacity case file through the records that point to it, then inventory its loose papers."]}
triggers: ["U.S. state or local court case file", "civil, chancery, divorce, criminal or incapacity proceeding", "court pointer records and loose papers"]
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "COURT-CASE-FILE-RECOVERY-01", "text": "captions, arrests, index entries and case-law searches stay bounded leads."}]
handoff: ["criminal-court-prison-record-recovery", "us-federal-court-case-file-recovery"]
checked: "2026-11-07"
checked_basis: "checked 2026-11-07"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"tier": "pointer", "group": "Courts, legislatures, prisons and institutions", "order": 1102}
---

# Recover a U.S. court case file from its pointer records

Use this recipe when a U.S. civil, chancery, divorce, criminal or incapacity proceeding may involve the person. Treat the proceeding as a case file. Recover it through the records that point to it, then inventory its loose papers. Captions, arrests, index entries and case-law searches stay bounded leads.

For federal jurisdiction, record groups and NARA custody, use
[U.S. federal court case-file recovery](us-federal-court-case-file-recovery.md).

Start here for a case file from any U.S. state, county or local court, criminal cases included.
When the lead is an arrest, a prison or a census institution entry and you still need to find which
court tried the case, or when you need the prison, inmate, clemency or pardon records that follow a
sentence, use [criminal court and prison records](criminal-court-prison-record-recovery.md), then
return here for the case file.

For the rule that an indictment or presentment is only an allegation, use [evidence/proof judgment](evidence-proof-judgment.md). Estate files, including reported probate opinions and probate appeal packets, belong to [probate case inventory](probate-case-document-inventory.md). Naturalization proceedings belong to [U.S. immigration § 9](usa-immigration-search-recovery.md). To recover a recorded judgment or a sheriff's deed in the land books, use [land index recovery](land-index-book-series-recovery.md).

## Contents

- Classify the proceeding before reading it
- Collect locators from every pointer series
- Request the loose papers as their own series
- Inventory the file by procedural stage
- Bound the published case-law search
- Set the window and close with a case register

## Classify the proceeding before reading it

- **Treat a "State v." caption as a clue, not as a crime.** A criminal case is always brought by a government and can lead to criminal penalties such as jail, probation or fines. Governments also sue civilly, for example over damage to government property or a broken contract. Classify the case as criminal when the docket labels it criminal or an indictment, information or criminal charge is on file. If you have the caption and a jail census entry, log it as probably criminal, pending the file. If you have only the caption, record the proceeding type as unresolved and get the file. [S2]
- **Treat an arrest, charge or newspaper arrest report as the start of a case.** It is not a finding about conduct. An arrest is a detention and does not mean the person committed a crime. Follow the case to a dismissal, plea, acquittal or sentence before stating what happened. [S2]
- **Treat a census entry in a jail or prison as a strong pointer to a criminal case.** First check that the entry lists the person as an inmate, not as the keeper or a member of the keeper's household. Tanner reads such an entry as meaning there was probably a criminal case. Search for that case. Do not state the charge or the outcome until the file shows them. [S1], [S2]
- **Do not read a missing newspaper report as no arrest.** Tanner says newspapers reliably reported visible or major arrests, but minor arrests such as shoplifting often went unreported outside small communities. [S2]
- **Separate locators from flags.** A recorded judgment or satisfaction of judgment identifies the case, the court and the parties. An appellate citation shows that a lower-court case was filed. Treat both as locators and go to the file. A divorce is a lead to the granting authority's records, which may be a court or, in some early periods, a legislature. A claimed injury makes a lawsuit likely. Log divorces and injuries as reasons to search, not as findings. [S1]

## Collect locators from every pointer series

Build a crosswalk from each pointer to the file it implies. Keep these parts separate:

- the pointer's literal text and locator
- the court, caption and party roles
- the case number
- the proceeding type

**Recorded judgment or satisfaction of judgment in land records.** This identifies the court, the case and the parties. Copy those details and use them to request the lawsuit file. [S1]

**Sheriff's sale, foreclosure or lien notice.** Tanner describes a chain: judgment, application and notice of sale, sale, a possible redemption period, then a sheriff's deed or a payment of the proceeds to the creditor. If real property was involved, the later documents are in the recorder's office with the land records. The sale notice was sometimes only posted at the courthouse, so it may be missing from the court file. Expect papers after the sale. Search the court file and the recorder's land records for each step of this chain. Tanner says the procedure differed by county and state, so read each document against the local procedure rather than expecting a fixed sequence. [S10]

**Bound minute books.** A minute entry is a pointer, not the case. Where an every-name minute-book index exists, search it for non-party roles as well as plaintiff and defendant: juror, attorney, solicitor general, security, and court officers such as a bailiff. Follow each volume and page reference to the minute entry. In S6, the Archive Lady shows a Stewart County circuit court minute-book index that she describes as covering the book from 1821 to 1834, with volume and page references and those roles. She calls this kind of every-name indexing rare, so do not expect it elsewhere. Published listings for the Stewart County indexes give other spans, so check the span and structure against the archive's own index before you cite it. [S6]

**State chancery folder index.** The Library of Virginia chancery index is searched by county or city, then by surname, plaintiff or defendant. Not every listed case has linked images. If a folder is listed without images, keep its case details. Then search the FamilySearch Catalog by county, not by name, for that county's court records. [S7] For Catalog and film routes, use [FamilySearch workflows](familysearch-practical-record-workflows.md).

**Incapacity indexes.** These are filed under period terms such as "lunatics" and "drunkards". Search them under the heading the court used at the time. In the example, a man who did not serve in the Civil War was checked against such an index at the Clearfield County, Pennsylvania courthouse, and divorce files were checked at the prothonotary's office. Neither search found him. The presenter left the question open. Record such a search as a negative for that index, that court and those years only. It proves neither capacity nor absence. [S8], [S9]

**Appellate citation.** An appeal shows that a lower-court case was filed. Go to that court for the file. [S1]

## Request the loose papers as their own series

**Privacy gate:** <!-- privacy-gate: request --> A court-file request can disclose a party's
identity and allegations or family circumstances involving people who may be living. Answer
the privacy gate in `SKILL.md` before sending a request or supporting documents to the court
or archive.

Archives often bring out only the bound minute books. Ask separately for the loose papers or case file: affidavits, subpoenas and other working papers. The county archivist on S5 says these are kept apart from the minute books. Also find out where the court's files were later transferred, whether to a basement, attic, storage facility, microfilm or online images. Do not assume the files stayed at the courthouse. [S2], [S5]

For recent state/county files, start with the court clerk (called the prothonotary for some
civil courts). For older files, check the state archives' court holdings and transfer guidance
early: many older local-court series have moved there. Transfer dates vary by state and court,
so confirm custody for the named series and years rather than assuming all old files moved.
For transferred federal files, follow the NARA route above; a current federal court may still
hold recent files. [S11]

## Inventory the file by procedural stage

Read from the first document filed to the last. In Tanner's example, a Utah County probate file stayed open for 30 years, and papers later in the stack added information. [S10] Record a locator or an explicit gap for each expected stage.

**Civil, chancery and divorce cases** [S1]:

- complaint
- summons and return of service, or service by publication in a newspaper (a sign of a default route)
- answers, demurrers, motions to dismiss, counterclaims and third-party claims
- affidavits and depositions
- exhibits
- judgment
- post-trial motions
- satisfaction of judgment
- appeal

**Criminal cases** [S2]:

- investigation
- arrest
- initial appearance and bail, or release on recognizance
- information or grand-jury indictment
- pretrial proceedings
- plea or trial
- acquittal or sentence
- incarceration

Use these points to read the criminal file:

- **For a modern file, expect a plea, not a trial.** Tanner says that in today's practice most cases end in a negotiated plea and very few go to trial. Do not carry that expectation back to older files. Establish plea or trial from the docket or disposition. After a plea, no trial transcript is expected; after an established trial, an absent transcript remains a retrieval gap.
- **Ask for the grand-jury records.** Where the case went by indictment, Tanner says many courts keep the grand-jury records, which can show the evidence presented.
- **Look for the officer in the court file.** Police files often do not survive. The arresting officer usually testified about how, where and why the person was arrested, and that testimony is often preserved in the court case file with the depositions and affidavits.

A gap in the inventory is a retrieval gap. It is not evidence that a step never happened.

## Bound the published case-law search

- **Search by name with a stated scope.** Use a published case-law search, such as Google Scholar's case-law option, nationwide or limited to chosen courts. It is full-text, so counsel can also be found by name. Google Scholar's help page gives its coverage as U.S. Supreme Court opinions from 1791, lower federal opinions from 1923, including district (trial), appellate, tax and bankruptcy courts, and state appellate and supreme court opinions from 1950. It does not cover state trial or probate court files. Log the courts and date range you searched. [S2], [S3], [S4]
- **Read a no-hit narrowly.** It says nothing about state trial-court involvement, and little about state cases decided before 1950. Courts not of record do not publish their decisions, so search their surviving dockets, indices, minute books and case papers separately. [S1]
- **Follow a hit back to the trial court.** Look for the lower-court file and the testimony transcript, which Tanner says may give relationships and motives that the opinion leaves out. Record people named in the opinion who were not parties as separate leads. [S3]
- **Keep the appellate record and the original file apart.** If the trial file is lost, the appellate record and opinion may be what survives. Label them as the appellate record. Do not treat an opinion's summary of facts as the trial record. [S1]

## Set the window and close with a case register

Search across the person's whole adult life and decades past death. Tanner warns that suits involving an estate can come 10–20 years later or more. [S1]

Return:

- a case register: court, caption, party roles, case number and proceeding type
- the pointer-to-file crosswalk
- the stage inventory, with a locator or gap for each document
- a separately labelled appellate or opinion row
- non-party name leads
- a search log of the courts, indexes, years and custodians actually searched, each with its bounded negative

Route identity and conclusions to [evidence/proof judgment](evidence-proof-judgment.md). For newspaper notices, use [newspaper search recovery](newspapers-com-search-recovery.md).
