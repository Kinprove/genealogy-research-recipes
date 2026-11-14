---
id: "probate-case-document-inventory"
title: "Inventory the documents of a probate case"
summary: "Recover the documents behind a probate index, will or administrator's bond as a case inventory with unresolved leads."
kind: "records"
scope: {"platforms": [], "tasks": ["probate record series, references to other documents, later actions, non-will proceedings, Swedish court-copy versus heirs-original and poverty-certificate checks, reverse searches from a guardian to wards, or an estate search that stopped at the first useful document."]}
privacy: "none"
gates: []
guardrails: [{"id": "PROBATE-CASE-DOCUMENT-INVENTORY-01", "text": "Keep a case inventory and a queue of unresolved references, so finding one useful document does not silently finish the estate search."}]
handoff: ["court-case-file-recovery", "evidence-proof-judgment", "land-index-book-series-recovery"]
checked: null
checked_basis: null
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "full", "group": "Featured workflows", "order": 12}
---

# Recipe: Inventory the documents of a probate case

## Contents

- Goal
- Before starting
- 1\. Establish the case and its record-series scope
- 2\. Resolve every discovered reference into its own inventory row
- 3\. Search for later and non-will parts of the proceeding
- 4\. Reconcile retrieval coverage and hand off interpretation
- Optional: recover a reported opinion about the estate
- Optional: recover copied proceedings from an appeal
- Prompt pattern

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

Do not expect a pre-1900 U.S. probate file to give the death date: the court needed to know that the person was dead, not when, so the record may give no date or only "on or about" a date [S68]. Probate records are inconsistent about death dates, and an index can carry a date that the record itself lacks [S69]. Enter a stated date with its wording. Otherwise bound the death by the earliest court action that requires it, such as the petition to open the estate or the will's proving, and not by the witnesses' testimony, which in some areas was taken when the will was written [S69].

If the expected court yields no case, do not report "no probate". Widen the search as a logged
set of candidate courts and years. Include the residence and place-of-death courts when they
differ, adjoining counties, and a court where heirs lived. Extend the years well past the death,
because heirs might not file until something later, such as a land sale, required it. Each venue
is only a search target. A hit there still needs its own locator and identity check, and none of
these places establishes jurisdiction. The
[Tanner probate-finding segment](https://www.youtube.com/watch?v=oZiYbKNvxJY) and
[later talks](https://www.youtube.com/watch?v=Yt91gmZt8sE) motivate this list. They supply no
jurisdiction rule or fixed time span for any state or period. [S1, S14]

Search the courts of the counties a person had left as well, even after the estate where he died is found and closed. An estate could be opened in a former county years later for money or property still there: in Neill's example, an estate was opened there ten years after the death in another state, to receive a settlement from a lawsuit that had taken years [S94]. A proceeding for assets in a state other than the one where the deceased lived is an ancillary administration [S95]. Enter such an estate as its own candidate case with its own locator and identity check.

Before reporting a woman's death or estate record missing, look for a late last marriage and search under that husband's surname as well as the name she had with her children's father. Neill calls the last husband's surname crucial to finding a woman's death and estate settlement [S88]; widowed and divorced women often kept a prior husband's surname unless they remarried [S89].

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

Browse the county will book even when the person died intestate: in some U.S. areas, particularly before the Civil War, it also recorded inventories, appointments of administrators and executors, sale accounts and lists of disbursements [S84], [S86].

For a Virginia estate, search the Library of Virginia's Wills and Estate Records Index, which covers wills, inventories, sales and other estate records from 1633 to 1800 in the will books of fifty-one counties and cities, and in some cases estate records in county order books [S86 @2026-11-14]. Then search that county court's order or minute books, which record every matter brought before the court and can hold information from loose papers since lost [S87 @2026-11-14]. Do not assume a loose-paper estate file exists: Neill expects a 1760 Virginia will to leave references in the order books but probably no case file [S85 @2026-11-14]. Record which loose papers survive for that county before calling a file missing.

For a death in Russia in the late Soviet period or later, search the public notarial
inheritance-case registry by full name. Enter each hit as a candidate case row: death date, case
number and year, the opening notary or state notary office, and the notarial chamber named for
further enquiry. Keep same-name hits as separate candidates. An entry may give no birth date or
only an uncertain one, so confirm identity from independent sources before linking it. Examples in
a [descendant-search thread](https://rodgersforum.borda.ru/?1-2-0-00001643-000-0-0-1734245901=)
and a [wartime-relatives thread](https://rodgersforum.borda.ru/?1-23-0-00000042-000-0-0-1730531911=)
motivate this. An entry does not name heirs or show the file's contents. Neither thread shows the
file being opened, the registry's starting year, or what a missing entry means. [S16]

For a Dutch will whose notary or date is unknown, Hoitink describes a historical Central Last
Wills Register filed by the testator's birth year. Where the inventory confirms that register
and arrangement, take a matching entry's notary, notary's place, will date and number to the
notarial series. She also describes a death-duty file as a will locator, reached where applicable
through its contemporary `table V-bis`; follow the will's notary/date/place reference actually
given in that file. [S19]

For a Pennsylvania estate, search two sets of county series, even after a will is found. Wills, administration papers, will books, administration dockets and their indexes belong to the Register of Wills; real-estate divisions, the audit of accounts and the property and care of minor heirs belong to the Orphans' Court, which also appointed guardians and oversaw partition and distribution [S21 @2026-11-12], [S39 @2026-11-12]. In the State Archives' microfilm list, a county's will books, estate indexes and Orphans' Court dockets can sit under one office heading, the Register of Wills and Clerk of the Orphans' Court, and state law lets smaller counties consolidate these elected offices [S40 @2026-11-12]. One office can therefore hold both sets; search each series' own index or docket instead of treating the will index as covering the Orphans' Court.

When a Pennsylvania index entry gives only a book and page, take them to FamilySearch's Pennsylvania, Probate Records, 1683-1994, which is browsed by county and volume through waypoints rather than searched by name [S41 @2026-11-12], [S42 @2026-11-12]. Open the named volume, go to the cited page, and record the image number separately [S21 @2026-11-12]. Do not stop at an index entry in Ancestry's Pennsylvania, U.S., Wills and Probate Records, 1683-1993, and do not read a missing image there as a lost record: that collection has searchable indexes, and not every entry has an image [S21 @2026-11-12], [S42 @2026-11-12].

When no will survives for a colonial Maryland ancestor, search the court records [S56], and route them by date. Orphans' courts, each served by a register of wills, were first created under the Acts of 1777, so do not look for one earlier [S59]. The Provincial Court heard testamentary and guardianship cases until the Prerogative Court was established and guardianship passed to the county courts [S57]. From 1692 a deputy commissary in each county took probate, recorded each will, inventory and account in his own books and sent the papers to the Prerogative Office to be recorded again [S58]. Search both the county's books and the Prerogative Court's series.

For a New Hampshire estate before 1771, search the provincial probate records, not a county court. Probate from 1636 to 1771 was filed at Exeter and Portsmouth, and the colonial probate files are now at the New Hampshire State Archives [S60 @2026-11-14], [S61 @2026-11-14]. Counties were created in 1769, but the provincial probate period runs to 1771 [S61 @2026-11-14]. For a town near the Massachusetts border, also search the Massachusetts county probate records [S61 @2026-11-14].

For Connecticut, search by probate district, not by town or county [S60 @2026-11-14]. Look the town up in the Connecticut State Library's Probate Districts by Town guide, which gives the district or districts the town belonged to at different times [S62 @2026-11-14]. A district created later out of another does not hold the earlier estates: Colchester's district was created in 1832 out of East Haddam, so an earlier Colchester estate is in the East Haddam district [S63 @2026-11-14]. Repeat the check for the parent district's own creation date. Connecticut probate courts also handled guardianships, adoptions and conservatorships, so search the same district for them [S62 @2026-11-14].

### Swedish absent probate: separate production from surviving copies

When an expected *bouppteckning* is absent, carry the supported name forms, death date,
residence and verified court coverage into the existing case register. Keep four questions
separate: was an inventory made, was a court copy filed, does a copy survive, and does the
searched index or image set expose it? A legal expectation alone answers none of them. [S24]

- **Index and filing date:** apply the later-year search already described above, retaining
  death and filing dates separately. ArkivDigital reports an example filed decades after
  death; it supplies no universal filing interval. Where the available index supports them,
  use justified name variants or wildcards, log the actual date coverage, and retrieve the
  court document behind a candidate. Do not carry the talk's historical index-coverage claim
  forward as a guarantee about the current service.
- **Court copy and heirs' original:** the presenter distinguishes the copy filed with the
  court from the inventory delivered to heirs. If the court copy cannot be found, queue an
  heir-held original only when a family-paper inventory, citation or other evidence gives
  a specific lead. Record its private custody and provenance separately; if both versions
  are recovered, compare their text. A court-series miss does not locate a private original.
- **Poverty certificate:** for an urban case with evidence suggesting this route, ask the
  relevant custodian whether a priest's *fattigbevis* survives for that person and period,
  and obtain its actual filing reference before requesting it. Record what an inspected
  certificate says and its date; an empty probate search does not establish poverty or
  prove that no inventory was made.
- **Lifetime transfer:** if a dated instrument or reference supports a distribution during
  life, retrieve it through [land-record recovery](land-index-book-series-recovery.md)
  where applicable and link it to the estate question. Preserve the transferred property,
  parties and date. Do not infer an empty estate or nonproduction from a later probate miss.
  Poverty and lifetime distribution are possibilities mentioned in the talk, not diagnoses
  for an unlocated estate. [S24]

**Artifact:** for each branch, add its actual evidence, target/custodian, covered dates,
retrieval result and remaining production or survival question to the case register.

**Check:** report an index miss, an unavailable court copy, an inspected private original
or a dated certificate as that specific outcome. None alone establishes a general production
rule or survival rate. For the talk's unlocated 1935 estate, the reason for absence and any
later filing remain unknown.

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
workflow. A [will-versus-index comparison](https://forum.ahnenforschung.net/forum/thread/2999515/)
motivates this check. It does not explain why the index differs, and it does not show that the
will is complete. [S15]

To decide whether a will image shows an original or a clerk's copy, examine the volume instead of judging from the single image. The Legal Genealogist reports paging back to the start of the volume to identify a bound will book, looking for pins or ribbons fastening an inserted document, and comparing the dates of surrounding entries with the will's date and the testator's death. The worked example is one bound Missouri will book, and no independent source was found for this test. [S29]

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

Where an original will survives alongside the will book entry, compare each heir's name in the two instead of accepting a clear, legible entry as an accurate list of the children, because copying errors occur and the differences can be minor or important. [S30], [S31] The Legal Genealogist reports, from two Tennessee county wills, a recorded copy that carried an entirely different child's name and originals held only on microfilm at a county archive; those specific examples were not independently verified. [S32]

If an index, docket or wrapper gives a packet or file number that the filmed or digitized
collection lacks, record the result as "not in this copy" rather than a missing document, and log
a pending request to the present custodian for that number
([Huron County packet example](https://www.youtube.com/watch?v=D5weC7CmDlo)); this does not
establish that any court still holds or will retrieve an unfilmed packet. [S7]

When a will names many children, note which are grouped in the same clause with the widow and which are placed apart as already provided for, rather than extracting one sibling group of the widow or reading the split only as a difference in bequests. The Legal Genealogist reports treating such a split as a hypothesis of different mothers, to be tested against tombstone dates, family Bibles and similar sources, which belongs in the evidence workflow. The author says the grouping is not proof by itself, and the example is one North Carolina will. [S33]

Do not read "my now wife" in a will as evidence of an earlier marriage. Neill reads the phrase as naming the wife at the time the will was written, to make clear who takes a bequest, as in a farm left to "my now wife" and after her death to "our children" [S67]. Test an earlier marriage in other records.

Treat a bequest to grandchildren as a lead that their parent died before the will, not as proof: a will can leave property directly to grandchildren whose parent is alive, as current North Carolina law states [S55]. A grandchild with another surname suggests a daughter's child, and one with the testator's surname a son's child [S51], but an unmarried daughter's child can carry the testator's surname. Establish the grandchildren's parent, and whether that parent had died, from other records before placing them.

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

When the final settlement or division comes years after the death, check two ordinary causes before reading the delay as a family dispute. Common-law dower was a widow's life estate in one third of her husband's land, so the heirs' possession of that part waited until her death [S82]; a will could also give her a life estate [S80]. Property was divided once all parties agreed or all heirs had come of age [S83], and heirs could wait for the youngest to come of age rather than act through a guardian [S80]. Run the search for the final settlement or partition to the later of the widow's death and the youngest heir's majority, taking the age of majority for that place, date and sex and whether marriage ended minority there, as in the Iowa rule below, and search the land records as well as probate, because the final division can appear in either or both; in Neill's Kentucky example, the land was partitioned sixteen years after the death [S81].

Do not record the administrator of an intestate estate as the spouse or a child by default. The spouse and heirs usually had priority, but a spouse could refuse and children could decline, so another heir or a creditor could take the office [S96]; current North Carolina law, for example, ranks the spouse, then heirs, next of kin and creditors, and lets a person with priority renounce [S97]. Record the person in the role of administrator only, and research an unfamiliar administrator's relationship to the deceased, if any, in other records.

An administrator *de bonis non* was appointed to finish an administration that the earlier administrator could no longer complete [S91], [S92]. Queue the earlier appointment as its own row and look in the court's orders for why it ended; the court may state a reason or may simply relieve the earlier administrator [S91].

Search the probate index even for a person who left no property, and classify each hit by proceeding type before treating it as an estate. Probate courts could also decide a person's sanity before commitment to a state hospital: in Minnesota their records include insanity case files, in some counties numbered in one sequence with the estates, and insanity record books mostly dated before 1920 [S77]. Neill found two entries for one poor ancestor that were insanity cases, not estates [S76]. Take a commitment case to [institutional patient records](institutional-patient-record-recovery.md).

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

Inventory the final settlement or final account as its own row, and compare its heirs with those first named in the will, petition or early accounts. Heirs who died during the settlement can be replaced there by others who were not listed at first [S90]; settlement records also show heirs who died and women who married before the final settlement [S83]. Record each change as a dated event on the heir, and pass the division of the money to the evidence workflow as a clue to each heir's relationship [S90].

For a relative who vanished, list the relatives who died after the disappearance and from whom that person stood to inherit, such as a sibling who died without children or a will, and search their estate files. To settle such an estate the court had to deal with the absent heir, and its file can record when the heir was last seen, testimony about the search, a court declaration that the heir was dead, or the heir's reappearance [S64], [S65]. A probate court can declare an heir missing for years dead for probate purposes and distribute the share to that heir's own heirs [S66]. Record such a declaration as a legal finding for that estate, not as a date or place of death.

When an item in an estate appraisal is illegible, read it against its neighbors. Appraisers usually walked the property, often room by room, so an appraisal tends to group items by place or purpose, and some name the room [S78], [S79]. Ask where the surrounding items stood (kitchen, barn, field) and what the unclear word could be in that group, then record the reading as an inference with that reasoning, not as a transcription. Grouping is less likely in a list of items sold than in the appraisal [S78].

Inventory an estate sale bill or vendue list as its own row, and copy each buyer with the item and price where the list gives them. Look for it with the inventory, in the case file or in a separate sales book. Buyers likely knew the deceased and can include relatives and associates; work first through those who bought more than two items [S44]. Flag a buyer of a family keepsake such as the Bible and a buyer who was also the administrator: in one 1821 Ohio estate, the author identified both as sons of the deceased from other records [S43]. Queue each flagged buyer as a separate candidate relative for the evidence workflow; a purchase alone does not prove kinship.

Do not skip guardianship or orphans' court entries because a parent survived: if minors may have
inherited land or other property, search them in the estate's county and where the widow and
children are later found ([guardianship tip](https://www.youtube.com/watch?v=CjjD9mI_dY8),
[Pennsylvania orphans' court remarks](https://www.youtube.com/watch?v=QTASkh59sEU)). Requirements
varied by place and period; a failed guardianship search carries evidentiary weight only after
establishing the applicable requirement, the expected recording and adequate surviving coverage, and
a guardianship alone does not establish the father's death. [S10]

Read a minor's guardian in an estate as the manager of the child's property, not as the child's household. Guardianship had little to do with physical custody; its main purpose was to manage and preserve the orphan's inherited estate [S52], and the children could stay with their mother while the guardian handled their inheritances [S51]. Do not move the children into the guardian's household or infer the mother's death from the appointment. An estate guardian shows the child had property to manage, since orphans who inherited nothing did not need one [S52]. If a guardian was appointed while a parent was alive, look for that property's source, such as a grandparent's estate or a land transfer: a guardian could be appointed even when a parent was alive if the minor personally owned property [S54], and Neill asks whether such an appointment kept a parent from spending an inheritance [S53].

For a bounded ancestor, locality and period, reverse the guardianship question: look for wards
for whom that person acted, not only guardians of their own children. Inspect which roles the
actual guardianship index names. If it omits guardians, a name-search miss is not a test of
the register; inspect a bounded relevant register range where its arrangement and available
extent allow, or leave the lookup unresolved. Keep guardian, ward and parent as separate
roles, and queue each located proceeding with its own locator. Hoitink suggests this reverse
search; guardianship alone establishes no kinship. [S18]

Inventory each guardianship paper for the same minor as its own row. A court appointment and a
later nomination of the same guardian are separate events, not duplicates and not a change of
guardian. Record any stated age bracket literally, such as "under fourteen" or "above 14 years
... has chosen him", and whether the minor chose the guardian. Read the dated wording as an age bound: a
minor "above 14 years" who "has chosen" the guardian was at least 14 and still under age on that
date, because the common law let a minor of 14 or over choose a guardian. When the mother's maiden
name is unknown, a guardian with a surname other than the father's is a possible lead to her kin
for the evidence workflow; check it in that family's own probate and vital records. The
[Warham Wheeler guardianship example](https://vitabrevis.americanancestors.org/the-warham-wheeler-affair)
motivates this. [S25]

Where an annual guardian's report has narrative text, read the paragraph ahead of the line entries rather than extracting only names and sums. The Legal Genealogist reports, from one 1896-1898 Louisa County, Iowa report book, that such paragraphs can show a ward's placement, custody with relatives, schooling and marriage consents, and treats a guardian's changed surname as a marriage clue; the author also says these accounts are often only line entries. [S26] Use a ward's attached receipt on reaching majority to bound a birth date only after checking the age for that place and sex and whether the ward married: under Iowa law through the Code of 1897, minority ended at 21 for males and 18 for females, and at marriage for any minor. [S27], [S28]

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

For Illinois land with underage heirs where dower, partition or sale was at issue, look for a court case, and do not read a filing over dower or partition as proof of a family dispute. A guardian's sale of a minor's land worked through a court order, and an 1877 decision held a guardian's sale decree void for lack of notice to the heirs. [S34], [S35] A partition decree had to include and represent minors. [S36] No Illinois authority was found that division or dower assignment always needed the court, so need is established only for guardian sales. The Legal Genealogist's example is one party's allegation in an 1880 McHenry County bill, and the post cites no statute for it. [S37]

Search for a will contest outside the probate series as well as in it. A separate suit over a will may be filed with the non-probate court records of the county where the estate was administered [S45]. Which court heard a contest depends on the place and period: in Tennessee a contested probate could be filed in the chancery or circuit court [S47]; Maryland's 1777 act let the parties in contested cases file in the general court, the chancery court or the county court [S59]; in England and Wales before 1858 disputes could go to the church courts or to secular courts, most often Chancery, and from 1858 went first to the new Court of Probate, though Chancery could still hear them [S46]. Recover a U.S. suit file through [court case files](court-case-file-recovery.md). Read the probate packet even for an intestate estate: it can hold a copy of a will the court refused to probate, which still carries family clues [S45].

When a child seems to be omitted from a will, collect every probate record of the settlement, not only the will [S48], [S49]. Look for settlement deeds for property the will does not mention and note whether every heir signed, since an omitted child may still be an heir [S48]; look in the land records for a transfer between the deceased and that child [S49]; and search for a suit over the will's validity as above [S48]. Whether an omitted child took a share depends on the law of the place and date: at common law the omission was presumed deliberate, while pretermitted-heir statutes give an unintentionally omitted child the intestate share, in some states only a child born after the will [S50].

Do not read the lack of a recorded lease as evidence that land had no tenants: a rental agreement generally did not have to be recorded [S73]. Look for leases and tenants in estate and court files. A lease in force at a death can be filed in the probate case, and a dispute can bring a copy of the lease or its terms into a court case [S72]; tenants can be named in an estate partition suit because they had an interest in the land, and a landlord-tenant suit can give lease terms [S70]. For a rural renter, read the probate and estate records for leases and rented property that place the family [S71], [S74]. A lease described as recorded in a case file was filed there as evidence, not recorded like a deed [S72], but still search the county's deed and lease books: Hamilton County, Ohio, recorded leases in its deed books from 1794 to 1848 and in separate lease books from 1848 [S75].

When the court file is lost or a packet is missing, search the county or regional newspaper's
legal notices for the estate. Look for claim or creditor notices, petitions to sell land to pay
debts (which may name heirs and describe the land), estate-sale notices and final-account hearing
notices. Enter each as a dated case-event row with its newspaper locator, linked to the case, and
queue the proceeding it points to. The
[legal-notice examples](https://www.youtube.com/watch?v=Mr03rzuk2gA) motivate this substitute. A
notice shows only what was published, such as alleged heirs or a scheduled hearing. It does not
give the will's contents, the court's decision or a complete heir list. [S12]

Search newspapers for the estate even when the packet survives. Neill found newspaper items about estate papers that were never found and that the packet did not mention, and one of them reported that the deceased had been married before and had children with his first wife [S93]. Enter such an item as a dated row with its newspaper locator, and pass any family statement in it to the evidence workflow as a lead.

Do not look for probate matters only in court files: The Legal Genealogist reports finding a probate court docket printed in a local newspaper, listing the matters scheduled for a court session and naming the role of the person acting, such as administrator or guardian. The example is one Missouri docket from August 1876, it could not be independently checked, and the post does not say how commonly newspapers printed such dockets. [S38]

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
