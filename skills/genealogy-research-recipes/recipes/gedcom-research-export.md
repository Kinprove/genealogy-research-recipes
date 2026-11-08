---
id: "gedcom-research-export"
title: "Export research findings to a GEDCOM file without changing what they prove"
summary: "Export research findings to a GEDCOM file, or bring a supplied one into research, without changing what they prove."
kind: "judgment"
scope: {"platforms": [], "tasks": ["Export research findings to a GEDCOM file, or bring a supplied one into research, without changing what they prove."]}
triggers: ["Export research findings to a GEDCOM file", "or bring a supplied one into research", "without changing what they prove"]
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "GEDCOM-RESEARCH-EXPORT-01", "text": "a header version change is not a conversion, each parent link needs its own evidence, and QUAY or a format change neither confirms nor culls a claim."}, {"id": "GED-01", "text": "**Never mark anyone deceased from a birth-year cutoff or a missing death date** in order to export, share or publish them."}, {"id": "GED-02", "text": "**Apply the living-person rules to a copy prepared for sharing.**"}, {"id": "GED-03", "text": "**Never map QUAY to or from a research status.**"}, {"id": "GED-04", "text": "For an online destination, identify living or possibly living people and state the redaction and destination-specific permission still required before upload."}, {"id": "GED-05", "text": "A supplied `QUAY 3` and a source title or research note saying \"unverified\" are not contradictory merely because of that research-status wording."}]
handoff: ["descendancy-gap-worklist", "evidence-proof-judgment", "familysearch-practical-record-workflows", "geni-practical-research-workflows", "research-documentation", "rootsmagic-tree-reconciliation-workflow", "source-citation"]
checked: "2026-11-02"
checked_basis: "opened 2026-11-02"
capabilities: {"browse": [], "local_script": [], "extensions": [], "data_transfer": ["export", "upload"], "contact": []}
router: {"tier": "pointer", "group": "DNA workflows and research planning", "order": 1132}
---

# Export research findings to a GEDCOM file without changing what they prove

Use this recipe when a user asks you to build, export or convert a GEDCOM (`.ged`) file from research findings, or to bring a supplied GEDCOM into existing research. GEDCOM is a format for transmitting and storing genealogical data [S1]. It is not an application, a tree service or a place to publish. The recipe prevents seven failures: changing the header version and calling the file converted, attaching a child to the father's wife because she shares his family record, turning a shared patronymic and surname into a parent link, reading QUAY as a research status, silently converting an Old Style date or padding an approximate year, culling or confirming a supplied tree's claims during a format change, and marking people deceased so that they can go into a shared file.

Link out for the shared steps:

- **Identity rulings, source independence, working statuses and revising a rejected premise:** [evidence/proof judgment § Techniques that work and § Using working hypotheses without inheriting their assumptions](evidence-proof-judgment.md).
- **Old Style offsets by century, the pre-1752 25 March year start and the 1918 switch:** [evidence/proof judgment § Follow record versions and test disputed dates](evidence-proof-judgment.md).
- **Building a citation and its locator:** [source citation § Preserve the locator](source-citation.md).
- **The research log and report, which a GEDCOM does not replace:** [research log and report](research-documentation.md).
- **Moving facts between RootsMagic, Ancestry and FamilySearch, and checking what arrived:** [RootsMagic tree reconciliation § 4](rootsmagic-tree-reconciliation-workflow.md).
- **Inherited GEDCOMs on FamilySearch as compiled claims, and people who may still be living:** [FamilySearch practical workflows § 15 and § 14](familysearch-practical-record-workflows.md).
- **Exporting a GEDCOM from Geni:** [Geni practical workflows § 8](geni-practical-research-workflows.md).
- **A blank death, spouse or child field:** [descendancy gap worklist § Do not read a blank as a finding](descendancy-gap-worklist.md).

## Contents

- Inputs to gather first
- 1\. Choose the destination and the version
- 2\. Put only evaluated findings in the file
- 3\. Export each parent link on its own evidence
- 4\. Cite the source, and carry the status in a NOTE, not in QUAY
- 5\. Keep names, dates and calendars as the records give them
- 6\. Convert a supplied tree without culling or confirming it
- 7\. Bring a supplied tree into existing research
- 8\. Check the written file before handing it over
- 9\. When the destination rejects the file or replaces a tree
- Close with an export packet

## Inputs to gather first

Gather these before writing:

- the destination: the program or service the user named, or none
- the GEDCOM version that program imports, if the user knows it
- for a conversion or an import: the supplied file, and the version and character set its header declares
- the research notes: each evaluated person, event and link with its status, source and locator, plus the hypotheses, open conflicts and rejected identifications
- who in the data may be living, and whether the file is for the user's own use or for sharing

Treat structural validity and sharing readiness as separate findings. For an online destination, identify living or possibly living people and state the redaction and destination-specific permission still required before upload. Pointing only to the privacy gate or the destination's privacy settings is not a redaction assessment.

## 1. Choose the destination and the version

- **Write a local `.ged` file unless the user chose another destination.** A connected tree service is not the destination just because it is connected. Do not read from it or write to it for this task unless the user chose it.
- **Write the version the target program imports.** If the user names none, ask. If the user cannot say, write GEDCOM 5.5.1 with `CHAR UTF-8` and the rest of the header that 5.5.1 requires: `SOUR`, a `SUBM` pointer to a submitter (SUBM) record in the same file, and `GEDC` with `VERS 5.5.1` and `FORM LINEAGE-LINKED` [S4]. The official index still lists 5.5 and 5.5.1 as in use in the marketplace [S2], a software vendor announced in 2021 that its export would default to 5.5.1 until 7.0 is in widespread use [S3], and 5.5.1 permits UTF-8 as its character set [S4], [S5]. When the user later names a program, re-export in its version.
- **Do not treat a header change as a conversion.** Between 5.5.1 and 7.0, rewrite at least these [S1]:
  - **Character set:** 7.0 uses only UTF-8.
  - **Header:** 7.0 has no `HEAD.CHAR` or `HEAD.GEDC.FORM`, and `HEAD.SUBM` is optional. A 5.5.1 file needs all three, and its SUBM pointer needs a matching SUBM record [S4].
  - **Continuation lines:** 7.0 removed `CONC` along with the old line-length limits. Join `CONC`-split values into one line.
  - **Calendars:** 7.0 writes the calendar as a keyword (`GREGORIAN`, `JULIAN`, `FRENCH_R`, `HEBREW`). Versions 4.0 to 5.5.1 used an `@#D…@` escape instead.
  - **BC years:** 5.5.1 writes `B.C.` after the year [S4]; 7.0 writes the epoch `BCE` after the date [S1].
  - **Extension tags:** 7.0 maps documented extension tags to their URIs in `HEAD.SCHMA`.
- **Check the syntax against the official specification of the target version,** linked from the gedcom.io index [S2]. Do not invent a dialect.
- **For a conversion, keep the original file unchanged** and write the result as a separate derivative file.
- **Keep the research log, the research notes and the report.** The GEDCOM does not replace them. Do not hold the export back until every search is finished.

## 2. Put only evaluated findings in the file

- **Export only people, events and links that have been evaluated against the evidence.** Keep hypotheses, candidates and unresolved alternatives in the research notes, not as facts or links in the file.
- **If the user wants a hypothesis in the file, flag it in a NOTE** on that event or link, with its handle from the notes.

## 3. Export each parent link on its own evidence

- **Evaluate each parent–child link separately.**
- **If a record proves only the father, write a FAM with him as the only partner and the child as CHIL.** Keep the mother unresolved in the notes. HUSB and WIFE are each optional in 7.0 [S1] and in 5.5.1 [S4], [S6].
- **Never put the child into the father's existing couple family.** Being his wife does not prove she is the mother. The father then belongs to two FAM records, one with his wife and one with the child.
- **Never turn a shared patronymic and surname into a CHIL link.** Keep the candidate in the notes and go on with the search that can tell the candidates apart.
- **After an import, open each one-parent family in the destination.** A reply in a 2024 FamilySearch Community thread on its new GEDCOM upload says the system creates an "Unknown" parent when one is missing [S13]. RootsMagic shows "Unknown spouse" over an empty slot that holds no person [S14]. Do not treat such a placeholder as an identified partner or attach evidence to it; list it in the export packet.
- **Do not infer a partner's sex or role from the HUSB or WIFE pointer.** GEDCOM 7 says so explicitly [S1]; 5.5.1 still assumes HUSB is male and WIFE is female [S4], so a 5.5.1 reader may do exactly that.

## 4. Cite the source, and carry the status in a NOTE, not in QUAY

- **Keep every SOUR citation already in the data.** For each new claim, cite its source and put the specific leaf, act or entry in PAGE, the field for where in the source the material is [S1].
- **Invent no locator.** For an interview or an unpaginated source, keep the locator that exists in the citation or a NOTE. When a converted tree gives no primary source, say so in a NOTE rather than supplying one.
- **Put the research status and the claim or link handle in a NOTE,** using the labels of the evidence/proof judgment worksheet: open, supported so far, contradicted or rejected.
- **Never map QUAY to or from a research status.** QUAY uses the values 0–3 to rate the credibility of a piece of information. Per the GEDCOM 7 spec, the values "do not have numeric meaning", and QUAY is "not intended to eliminate the receivers' need to evaluate the evidence for themselves" [S1]. A QUAY of 3 does not make a link proved, and a missing QUAY does not make it doubtful.

A supplied `QUAY 3` and a source title or research note saying "unverified" are not contradictory merely because of that research-status wording. Preserve the code and text separately. Whether the underlying information merits its credibility code is a separate source-evaluation question; do not change QUAY solely to mirror research status.

## 5. Keep names, dates and calendars as the records give them

- **Keep the original name spellings, the date uncertainty, the calendar and the historical jurisdiction.**
- **Write an Old Style date as Julian in the target syntax:** `JULIAN 3 MAY 1892` in 7.0 [S1], `@#DJULIAN@ 3 MAY 1892` in 5.5.1 [S4], [S7], [S8]. A 7.0 date without a calendar is read as Gregorian [S1], so the keyword is required. Never convert a date to New Style silently; take the offset for the date's century from evidence/proof judgment.
- **Keep a dual year.** Before 1752, England, Wales, Ireland and the British colonies began the year on 25 March; Scotland used 1 January from 1600 [S9], [S10]. A date from 1 January to 24 March may therefore belong to the next modern year; a record may write it as a dual year such as 1731/32. In 7.0 the year is a plain integer with no slash form [S1]. Put the New Style year in DATE, keep the Julian calendar keyword, and put the literal dual date in PHRASE: `2 DATE JULIAN 30 JAN 1649` with `3 PHRASE 30th of January, 1648/9`. Moving the year start does not convert the day and month to Gregorian. If the year itself is uncertain, write `2 DATE BET 1648 AND 1649` with `3 PHRASE 1648/9` [S1]. In 5.5.1, carry the literal dual date in a NOTE beside the DATE. Never drop to one year silently: that moves ages and the order of events by a year. How to read such a date: [evidence/proof judgment § Follow record versions and test disputed dates](evidence-proof-judgment.md).
- **Do not pad an approximate date.** `ABT 1890` stays `ABT 1890`, never a full day and month. Both 5.5.1 and 7.0 have `ABT`, `CAL` and `EST` for approximations, `BEF` and `AFT` for one-sided bounds, `BET … AND` for a range, and `FROM … TO` for a period [S1], [S4]. The versions differ in how they write the calendar and a BC year (section 1). If the target version cannot express a detail, keep it in a NOTE and in the notes, and say what was lost.
- **When versions conflict, keep both.** For example, a tree gives a birth year and a document gives a Julian date in another year. Keep both in the notes with their provenance, and add a NOTE in the export that names the dispute. Do not choose one silently.
- **Never re-export a disputed link as confirmed, and never overwrite the user's file** with a new conclusion.

## 6. Convert a supplied tree without culling or confirming it

- **A pure format conversion keeps every claim and link of the supplied tree,** unverified ones included, with their provenance and status. It is not an evidence cull: do not drop claims that would fail the bar for new research findings. It confirms nothing either.
- **List every custom tag, attachment and media link that was not carried over,** and carry its meaning in a standard NOTE where you can.
- **Media files do not travel inside a `.ged` file.** A 5.5.1 `OBJE` `FILE` value is a local or remote file reference [S4]. A path on the sender's computer, such as the migration guide's `d:\Media\…` example [S12], breaks after transfer when that path is not available on the receiving computer. 7.0 defines GEDZIP: a `.gdz` zip archive that holds the dataset as `gedcom.ged` together with the local media files it references [S1]. Write a GEDZIP only when the destination imports it; otherwise hand the media files over separately and list them.
- **Do not call a conversion lossless, or an import into another program successful, until you have checked it in that program.** For transfers between RootsMagic, Ancestry and FamilySearch, use the RootsMagic recipe's destination check.

## 7. Bring a supplied tree into existing research

- **Keep the file unchanged as a source.** Record where and when you received it, and its SHA-256 hash.
- **Decode before you match.** Earlier versions allowed several character encodings and defaulted to ANSEL; 7.0 uses only UTF-8 [S1]. Decode a 5.5 or 5.5.1 file with the character set its header declares. If names show stray accented capitals or symbols where letters belong, the file was decoded with the wrong character set: fix that first. Next, repair family links recorded on only one side, in the FAM record but not in the person's record or the reverse. Run duplicate detection only after both repairs. Otherwise a garbled spelling and the correct one, or a half-linked record and its fully linked twin, look like two people.
- **Map its cross-reference IDs to your own person handles** in a small table. Do not merge same-named people automatically, and do not overwrite existing candidates. Same-named children of one couple may be two children, one named after a dead sibling: run the burial and forward-trace test in [evidence/proof judgment § Techniques that work](evidence-proof-judgment.md) before you merge them.
- **Enter its links as hypotheses** until the documents behind them are evaluated. A website copy of the same tree is not a second source; test independence as evidence/proof judgment sets out.
- **Never mark anyone deceased from a birth-year cutoff or a missing death date** in order to export, share or publish them. Treat probably living people as living.
- **State partial coverage,** for example "40 of 200 people parsed", and keep the unsupported fields for review. Work on the parsed part without waiting for the rest.
- **Do not let a re-import restore an identification rejected earlier.** Keep the rejection, its reason and any justified revision, as the evidence/proof judgment worksheet does when a premise changes.

## 8. Check the written file before handing it over

- **Check that the file conforms to the declared version:** the header, the character set, the date syntax and the tags of that version. A 5.5.1 header needs `SOUR`, `SUBM`, `GEDC` with `VERS` and `FORM LINEAGE-LINKED`, and `CHAR`, and the file needs the SUBM record that `SUBM` points to [S4].
- **Check that every INDI, FAM and SOUR pointer resolves.** In 7.0, every pointer except the null pointer `@VOID@` must occur as the cross-reference identifier of a structure in the same file [S1].
- **Compare the exported links, citations and notes with the research notes.**
- **Privacy gate:** <!-- privacy-gate: export --> A copy prepared for sharing carries tree data that may include living or possibly living people out of the user's own files; answer the privacy gate in `SKILL.md` before handing it over.
- **Apply the living-person rules to a copy prepared for sharing.** Leave out or redact the living and probably living, private notes, and attachments the user did not choose to share. Writing a local export publishes nothing; do not upload the file or its attachments anywhere the user did not choose.
- **Report what was not checked.** Give the file path, the version and the material limits of the transfer.

## 9. When the destination rejects the file or replaces a tree

- **Separate conformance from importer support before you edit the file.** A file that passes a local parser can still be rejected by a program. Check the rule in the target version's specification first, then the program's own import help.
- **Check the version differences that trip importers** [S1]:
  - **`@` in a value:** 5.5.1 doubled every `@`; 7.0 doubles an `@` only when it is the first character of the line string.
  - **Cross-reference IDs:** in 7.0 an ID is any run of uppercase letters, digits and underscores between `@` signs, so a leading digit is allowed. `@VOID@` is reserved.
  - **Date phrases:** 5.5.1 put them inside the DATE value; 7.0 moved them to a PHRASE substructure.
- **Privacy gate:** <!-- privacy-gate: upload --> A test upload sends tree data, possibly about living or possibly living relatives, to an online tree service; answer the privacy gate in `SKILL.md` before uploading even a test file.
- **Never upload a reduced test file over an existing online tree.** A re-import can replace the tree. Familio's help (a Russian-language tree service; checked 2026-11-04) says a re-import always fully replaces person pages: the new file replaces the old one, and all edits made by hand on Familio are lost [S11]. Test on a separate test tree or with a small synthetic file, and only on a destination the user chose.

**Cross-reference IDs in 5.5.1:** the first character may be a letter, an underscore or a digit, and lowercase letters are allowed; the standard's own example ID is `@1234@` [S16]. A 7.0 ID takes no lowercase letters [S15]. A leading digit is valid in both versions and is no reason to rewrite IDs. If an importer still rejects the file's IDs, rename them in a derivative copy: a pointer must match a cross-reference ID in the same file [S16], so change each ID and every pointer to it in one pass, and add each old and new ID to the packet's ID map.

**Blank lines and the last line:** every 7.0 line ends with a line terminator, and 7.0 dropped the permission earlier versions gave for blank lines before a line [S15]. The 5.5.1 standard says the trailer must be followed by the terminator, and that files with extra blank lines between records are not to be used when transmitting to other systems [S16]. Remove empty lines and make sure `0 TRLR` ends with a terminator.

**A sample export from the target program is a structure reference, not a template for the content.** `HEAD.SOUR` names the software that actually wrote the file [S15], [S16]; leave it naming that software even where the sample names the target program. Keep every place, source, note and continuation line that the sample lacks: cutting them to match loses research data silently.

## Close with an export packet

Return:

- **File row:** path, version, character set, and whether it is a new export or a derivative of a supplied file kept unchanged.
- **Destination:** the user's choice, or local by default.
- **ID map:** the supplied file's cross-reference IDs against your person handles.
- **Coverage:** people parsed out of the total, and the unsupported fields kept.
- **Not carried over:** custom tags, attachments, media and details the version cannot express, each with the NOTE that carries its meaning, if any; and whether media travel in a GEDZIP or separately.
- **Placeholders:** any "Unknown" partner a destination showed or created for a one-parent family.
- **Disputes:** each conflicting version with its provenance, and the NOTE that names it in the file.
- **Checks:** version conformance, pointer resolution, agreement with the research notes, and any check in a destination program.
- **Sharing:** the living-person handling applied, or "local only".

The model writes and checks the file. The researcher decides identity and kinship.
