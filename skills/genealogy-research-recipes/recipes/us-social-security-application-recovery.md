---
id: "us-social-security-application-recovery"
title: "Recover a U.S. Social Security application for a birthplace or parent clue"
summary: "Choose between a Social Security death index, Numident extract and original SS-5 when researching a deceased person’s birth or parents."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "US-SOCIAL-SECURITY-APPLICATION-RECOVERY-01", "text": "A miss in a Social Security death index leaves the person's death and application history open."}]
handoff: ["usa-immigration-search-recovery", "historical-place-name-resolution", "maiden-name-recovery"]
checked: null
checked_basis: null
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request", "third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "United States: people, vital and church records", "order": 141}
---

# Recover a U.S. Social Security application for a birthplace or parent clue

A miss in a Social Security death index leaves the person's death and application history open.

## Identify which record you found

Distinguish a death extract from an application or claim entry. The National Archives' 1936–2007 NUMIDENT series describes a selection based on verified death or the age the applicant would have reached at the cutoff. SSA death information depends on reports reaching the agency. Record which series you searched and pursue other death evidence after a miss [S3 @2026-11-20] [S4 @2026-11-20].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Identify the name and dates that would go to MyHeritage. Answer the privacy gate in `SKILL.md` before submitting the search. Confirm the subject is deceased and send only the terms needed for the lookup.

For a confirmed deceased person, search the [U.S. Social Security Death Index (SSDI) on MyHeritage](https://www.myheritage.com/research/collection/us-social-security-death-index-ssdi/colid-10002) and open any candidate entry in the free collection before considering a paid subscription [S5 @2026-11-21] [S6 @2026-11-21].

## Recover a missing birthplace

Use the original SS-5 for a deceased immigrant if the extract gives no birthplace or only a broad label. Read the exact locality wording and the application's date and compare it with passenger, naturalization or civil records before assigning a village. An application can identify a place to test, including when there is no death-index hit [S1] [S2] [S3].

## Request the document

**Privacy gate:** <!-- privacy-gate: request --> Identify the subject’s name, dates, any Social Security number and proof of death that would go to SSA. Identify and minimize any living relatives’ details. Keep identifiers and returned copies in the user's private research files.

Request the original SS-5 from SSA for the confirmed deceased applicant through its deceased-person FOIA route. Select the original application rather than the Numident extract when the original fields are needed. Check SSA’s current requirements for proof of death and release of parent names before submitting the minimum identifiers [S2 @2026-11-20].

## Handoffs

- [usa immigration search recovery](usa-immigration-search-recovery.md)
- [historical place name resolution](historical-place-name-resolution.md)
- [maiden name recovery](maiden-name-recovery.md)
