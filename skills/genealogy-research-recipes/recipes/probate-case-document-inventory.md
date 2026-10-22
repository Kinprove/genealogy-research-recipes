# Recipe: Inventory the documents of a probate case

## Goal

Recover the available documents behind a probate index, will or administrator's bond.
Keep a case inventory and a queue of unresolved references, so finding one useful document
does not silently finish the estate search.

## Before starting

Record the deceased person's supported names, approximate death date, residences and known
property locations. Keep competing same-named people separate. Determine the relevant court,
record series and present custodian from the historical locality's descriptions or finding aids;
do not assume that a death location, an heir's residence or today's court name decides jurisdiction.

Use the existing platform workflow for opening an image-only volume and distinguishing printed
pages from viewer image numbers. This recipe manages the documents and references across volumes.

## 1. Establish the case and its record-series scope

1. Save the locator and image of the starting index, will, bond or estate entry.
2. Record the name and identifying context, the court/jurisdiction stated, the case or estate
   number when supplied, and the document and recording dates actually present.
3. List the probate-related series available for that court and period. A surviving will book,
   administration docket, probate journal and loose case file are different retrieval targets.
4. Identify the present custodian for each relevant series. Records may have moved from their
   original court to an archive or another repository.
5. If the person owned property elsewhere, inspect that locality's probate descriptions for a
   related proceeding. Add a candidate case only with its own locator and identity check;
   do not presume an ancillary proceeding must exist. [S1, S2]

**Artifact:** A case register: case ID, deceased name, identifying context, court/time,
case number, candidate related cases, relevant series, coverage and present custodian.

**Check:** A collection title or same name is not a case link. Record the stated connection
between a related proceeding and the principal case, or leave that connection unresolved.

If the expected court yields no case, do not report "no probate". Widen the search as a logged
set of candidate courts and years. Include the residence and place-of-death courts when they
differ, adjoining counties, and a court where heirs lived. Extend the years well past the death,
because heirs might not file until something later, such as a land sale, required it. Each venue
is only a search target. A hit there still needs its own locator and identity check, and none of
these places establishes jurisdiction. The
[Tanner probate-finding segment](https://www.youtube.com/watch?v=oZiYbKNvxJY) and
[later talks](https://www.youtube.com/watch?v=Yt91gmZt8sE) motivate this list. They supply no
jurisdiction rule or fixed time span for any state or period. [S1, S14]

Treat names on a case wrapper as a finding aid, not an exhaustive person index. When
independently supported locality, family and time context justifies inspecting that case,
define the internal packet scope rather than restricting it to wrapper-name matches.
Inspect the available documents within that scope, recording the actual person/event
each concerns and the extent still uninspected. [Historical demonstration](https://www.youtube.com/watch?v=1FEjeMA41eg).

Before treating a digitized folder or first volume as the whole case, find out how that court
filed estate papers. It may have kept one file per estate, split papers by party or claimant
under a case number, or recorded documents chronologically into general books as they arrived.
In split or chronological systems, take the docket or register's document list as targets and
search later volumes across the case's active years.
[Tanner's filing-system discussion](https://www.youtube.com/watch?v=FB2SNEW3hC0) and
[court-records example](https://www.youtube.com/watch?v=JrcVzlwtnuQ) motivate this step. The
system must be established for each court and period; neither source documents the filing system
of a specific court. [S5]

For a death in Russia in the late Soviet period or later, search the public notarial
inheritance-case registry by full name. Enter each hit as a candidate case row: death date, case
number and year, the opening notary or state notary office, and the notarial chamber named for
further enquiry. Keep same-name hits as separate candidates. An entry may give no birth date or
only an uncertain one, so confirm identity from independent sources before linking it. Examples in
a [descendant-search thread](https://rodgersforum.borda.ru/?1-2-0-00001643-000-0-0-1734245901=)
and a [wartime-relatives thread](https://rodgersforum.borda.ru/?1-23-0-00000042-000-0-0-1730531911=)
motivate this. An entry does not name heirs or show the file's contents. Neither thread shows the
file being opened, the registry's starting year, or what a missing entry means. [S16]

## 2. Resolve every discovered reference into its own inventory row

If the packet has a coded document key, locate the collection's actual master legend before
decoding it. Keep both locators and compare the listed components with inspected documents;
distinguish listed-but-unseen parts from inspected parts absent from the key. The
[probate-key example](https://familylocket.com/part-6-pennsylvania-germans-probate-records/)
illustrates this check. A contents key does not certify complete survival or inspection.

Before browsing an unindexed will register or a run of original wills, record how it is actually
arranged. A series described as alphabetical may be grouped only by the first letter of the
surname and then by probate date, or by month with blank leaves between months. Scan the whole
letter group for the relevant period, and open both films when a month or letter continues onto
the next one. Record whether the filmed series includes administrations as well as wills. The
[Part 2](https://www.youtube.com/watch?v=ckpu7brPLnI) and
[Part 3](https://www.youtube.com/watch?v=Gwcf300h1sA) England and Wales examples motivate this
check. The arrangement varies by collection and county, so a reel lacking a grant is not
evidence that no grant exists. [S13]

1. Read the starting record for references to another volume, page, docket, journal or file.
2. Enter each reference in a queue exactly as written, including the record series and book number.
3. Open the referenced series and volume; locate the printed page using the viewer's available
   navigation. Save the image locator separately.
4. Confirm that the retrieved document concerns the intended case. Inspect its continuation,
   and record any further references it supplies.
5. Link the resolved row back to the document that cited it. If you cannot retrieve it, record
   the specific outcome: locator unreadable, series not held, access restricted, page not found,
   or request pending. Keep a tentative reading visibly tentative.
6. Continue until every discovered reference has a recorded result or an explicit next action.
   [S2]

**Artifact:** A reference queue plus document inventory:

| Field | Preserve |
| --- | --- |
| Document ID and case ID | Distinguish the document from the case and from its images |
| Type and creator | Will, bond, docket entry, appraisal, account, settlement or actual description |
| Dates | Document/action date and recording date, separately when given |
| Locator | Court, series, case/file number or book/page, repository and image link |
| Image extent | Start/end and continuation images inspected |
| Reference relationship | Referring document ID and wording; newly discovered targets |
| Retrieval result | Found and checked, uncertain target, unavailable or next action |

**Check:** A will can be indexed while a referenced docket or journal is not. A link to an
index entry is not a completed retrieval of the document it points to.

When an index or database abstract lists a will's heirs or beneficiaries, record that list as the
indexer's derived data, separate from the will row. Read the will image itself and compare the two
name by name. Mark any name that appears in only one of them as a discrepancy. Do not count an
index-only name as a separate person, and do not drop a will-named child because the index uses a
different name. Hand the reconciliation, for example against a household census entry, to the evidence
workflow. A [will-versus-index comparison](https://forum.ahnenforschung.net/forum/thread/2999515-auswanderung-1857-aus-hessen-%C3%BCber-bremen-nach-amerika/)
motivates this check. It does not explain why the index differs, and it does not show that the
will is complete. [S15]

Inventory a loose original and a clerk's recorded copy as separate rows with separate locators,
and record which form each image shows. A will in a will book is usually the court's recorded
copy rather than the document the testator signed. Consecutive entries in one hand indicate
copying, and signatures, marks and seals there are the copyist's renderings; do not infer the testator's
signature, literacy or handwriting from them. Where loose
originals were kept, queue the original as a separate target and record differences, such as a
clause present only on the registered copy. If a wrapper or docket points to a recorded volume
and page because the originals are missing, retrieve that copy, but do not report the original as
found. The [Maryland seal example](https://www.youtube.com/watch?v=Yt91gmZt8sE),
[Middlesex docket example](https://www.youtube.com/watch?v=1oNhIhwKA6U),
[Tanner's source-evaluation example](https://www.youtube.com/watch?v=iLEqf98ks9M),
[consecutive-handwriting check](https://www.youtube.com/watch?v=FB2SNEW3hC0) and
[Maris registered/original comparison](https://www.youtube.com/watch?v=Gwcf300h1sA) motivate
this. None of these
examples establishes routine recording or the survival of originals. [S6]

If an index, docket or wrapper gives a packet or file number that the filmed or digitized
collection lacks, record the result as "not in this copy" rather than a missing document, and log
a pending request to the present custodian for that number
([Huron County packet example](https://www.youtube.com/watch?v=D5weC7CmDlo)); this does not
establish that any court still holds or will retrieve an unfilmed packet. [S7]

## 3. Search for later and non-will parts of the proceeding

1. Review the inventory for administration, guardianship, appraisal, accounts and settlement
   material relevant to the case. Search the series actually held; not every case has every type.
2. Try supported abbreviations and administrator or executor names when the deceased's full
   name does not recover the relevant entry. Verify each candidate from its document.
3. Do not restrict every search to the death year. Use dates already found in bonds, accounts,
   dockets or settlements to extend a bounded search into later years.
4. If a deceased person appears in a land document as a boundary reference, record that role
   separately. Follow a relevant administrator/executor deed into a probate search; do not turn
   an ordinary neighbor reference into evidence of another estate proceeding.
5. Preserve an inventory of estate documents even when no will is located. An administration
   account or appraisal remains a document to retrieve and examine, rather than a failed will
   search. Do not declare intestacy solely because a will search failed. [S1, S3]

**Artifact:** Additional document rows and a search log specifying series, names, date bounds,
results and reasons for each extension.

**Check:** A later recording date is not a later death date. Finding a settlement several years
after death demonstrates the need for that case's wider search; it supplies no universal deadline.

If an inspected estate instrument defers distribution or control until a condition is met,
retain its literal terms and locator. When independent records support a potential triggering
event and date, such as a specified beneficiary's later death, add a bounded search for later
estate action to the queue. Record the condition, event evidence, selected court/series and
date bounds; verify any returned case link separately. Keep an uncertain condition or trigger
unresolved, and do not assume a universal age or automatic reopening. Judy Russell's dated
late-estate example motivates this search input without verifying the narrated case or its
governing law. [S17]

If an account or receipt describes an administrator's journey, retain the actor, role,
date, destination and stated purpose. Use that purpose to nominate a bounded related court,
land-office or transaction-record question in the existing queue, even without a book/page
citation; establish the actual series and custodian before retrieval. The [administrator-itinerary example](https://dna-explained.com/2023/07/16/new-information-about-philip-jacob-miller-c1726-1799-and-magdalena-possibly-rochette-c1730-1800-1808-52-ancestors-404/)
motivates the lead. The administrator's destination does not establish the deceased person's
residence, property, service or another estate proceeding.

When selecting pages from a packet, include vouchers and receipts, not only the will, inventory
and account summaries, and inventory each as its own row. Record each signer or payee, the share
or item receipted, and any statement that one person signs for another, such as a husband for his
wife's share. Mark payments worded as a distributive share separately from creditor payments,
especially when no final distribution survives. If a share is assigned to a deceased heir's
estate, queue that estate as a candidate related case with its own court, date bounds and
identity check. The [Broglin probate interview](https://www.youtube.com/watch?v=PzZ4fwSbjq8) and
[Abbott estate walkthrough](https://www.youtube.com/watch?v=880wgUzrmhQ) motivate this. Wording
and proxy-signing rules vary by place and period. A receipt is an heir lead for the evidence
workflow, not proof of kinship. A receipt without share wording does not prove a creditor. Do not
presume the deceased heir's case exists or was filed in the same court. [S8, S9]

Do not skip guardianship or orphans' court entries because a parent survived: if minors may have
inherited land or other property, search them in the estate's county and where the widow and
children are later found ([guardianship tip](https://www.youtube.com/watch?v=CjjD9mI_dY8),
[Pennsylvania orphans' court remarks](https://www.youtube.com/watch?v=QTASkh59sEU)). Requirements
varied by place and period; a failed guardianship search carries evidentiary weight only after
establishing the applicable requirement, the expected recording and adequate surviving coverage, and
a guardianship alone does not establish the father's death. [S10]

If land passed jointly to several heirs, or the estate papers or deeds point to a suit, add a
bounded search of the court's civil or equity series for a partition, sale or title suit. An
heir, another household member or the administrator may have brought it. Recover a U.S. suit file
through [court case files](court-case-file-recovery.md), and inventory it as a related case with
its own locator and stated link to the estate; record each heir's name and residence as stated,
including married names. Such suits could be the legal route to settlement or
clear title, so a family-versus-family caption is not evidence of a feud. The
[Family History Fanatics example](https://www.youtube.com/watch?v=CjjD9mI_dY8) and
[court-records remark](https://www.youtube.com/watch?v=KjWd4X-7o_k) motivate this lead without
supplying local law. Not every jurisdiction required such a suit; establish the period's procedure before
interpreting a suit. [S11]

When the court file is lost or a packet is missing, search the county or regional newspaper's
legal notices for the estate. Look for claim or creditor notices, petitions to sell land to pay
debts (which may name heirs and describe the land), estate-sale notices and final-account hearing
notices. Enter each as a dated case-event row with its newspaper locator, linked to the case, and
queue the proceeding it points to. The
[legal-notice examples](https://www.youtube.com/watch?v=Mr03rzuk2gA) motivate this substitute. A
notice shows only what was published, such as alleged heirs or a scheduled hearing. It does not
give the will's contents, the court's decision or a complete heir list. [S12]

## 4. Reconcile retrieval coverage and hand off interpretation

1. Sort document rows by the dates of the recorded actions while preserving the original
   image order and locators.
2. Check that each image belongs to the intended document and case. Separate a different
   person's entry sharing the same page.
3. Compare the reference queue with the inventory. Mark resolved references and retain any
   missing documents or unsearched relevant series.
4. Report what was retrieved, the holdings/series searched, and the limits of the search.
   Completion means the recorded queue was handled within that scope; it does not certify
   that every historical case document survives or has been found.
5. Hand the source-linked documents to the evidence/proof workflow for identity, kinship and
   conflicts. Keep transcript uncertainty and proposed relationships separate from retrieval
   status. [S1, S2, S3]

**Artifact:** A case-document packet, resolved/unresolved reference list and retrieval-coverage note.

**Check:** “Will found,” “document packet retrieved” and “relationship established” describe
different outcomes. State only the outcome the packet supports.

## Optional: recover a reported opinion about the estate

1. When a search or secondary account supplies an estate-related opinion lead, save the exact
   query or source locator and the context that surfaced it. Copy the case name and citation
   as supplied, preserving the stated jurisdiction, reporter, volume and page. Leave missing
   citation components unresolved.
2. Use those citation components to locate the full opinion in an available reporter or
   legal-text collection. Save its locator and the pages actually inspected. Record whether
   you have only an article, a citation/listing, a headnote/summary, or the full opinion text;
   if the full text is unavailable, retain the citation and a specific next action.
3. Read the retrieved opinion for references to wills, deeds or other estate instruments.
   Enter each reference in the existing §2 queue as a separate, initially uninspected target,
   linked to the citing opinion and its wording. Retrieve and check each instrument separately;
   discussion of a deed or will in an opinion does not retrieve that instrument. Use the
   [land-record recovery workflow](land-index-book-series-recovery.md) for queued deeds.
4. Preserve the opinion's stated court separately from the estate-record court; one does not
   establish the other. Keep the opinion-to-estate/person link and each instrument's identity
   state separate from retrieval status. Reconcile the added rows through §4 and send unresolved
   identity links to the [evidence/proof workflow](evidence-proof-judgment.md). [S4]

**Artifact:** An opinion-lead record with literal search/source context, the supplied citation,
full-text retrieval/inspection status, and separate linked instrument targets in the existing queue.

**Check:** An article, search listing, headnote or AI explanation is not inspected opinion text.
Do not fill an unseen opinion or instrument with facts from a summary.

## Optional: recover copied proceedings from an appeal

When a relevant lower-court file is missing and an appeal is evidenced, check the described
appellate archival packet as a separate target from the published opinion. Its catalogue may
use a next friend, administrator or another litigant. Inventory transmitted pleadings,
depositions or a judicially reconstructed will with their own locators and record forms;
keep them distinct from the absent original. The [Dobkins appeal-copy example](https://dna-explained.com/2022/09/26/why-was-old-man-jacob-dobkins-will-fraudulently-secreted-concealed-and-destroyed-52-ancestors-375/)
motivates this fallback, without establishing current custody, a complete packet or the
participants' final outcome after appeal or remand.

## Prompt pattern

> Using these probate images and record-series descriptions, build the case register,
> reference queue and document inventory. Preserve exact book/page and file references,
> distinguish document/action dates from recording dates, and follow every supplied reference.
> Propose bounded searches for relevant later or non-will documents. Mark missing series,
> uncertain locators and access limits. Do not infer intestacy, kinship or exhaustive survival.
