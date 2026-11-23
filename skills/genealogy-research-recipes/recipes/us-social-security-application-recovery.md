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
router: {"section": "Records by country and region", "group": "United States: people, vital and church records", "order": 151}
---

# Recover a U.S. Social Security application for a birthplace or parent clue

A miss in a Social Security death index leaves the person's death and application history open.

## Identify which record you found

Distinguish a death extract from an application or claim entry. The National Archives' 1936–2007 NUMIDENT series describes a selection based on verified death or the age the applicant would have reached at the cutoff. SSA death information depends on reports reaching the agency. Record which series you searched and pursue other death evidence after a miss [S3 @2026-11-20] [S4 @2026-11-20].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Identify the name and dates that would go to MyHeritage. Answer the privacy gate in `SKILL.md` before submitting the search. Confirm the subject is deceased and send only the terms needed for the lookup.

For a confirmed deceased person, search the [U.S. Social Security Death Index (SSDI) on MyHeritage](https://www.myheritage.com/research/collection/us-social-security-death-index-ssdi/colid-10002) and open any candidate entry in the free collection before considering a paid subscription [S5 @2026-11-21] [S6 @2026-11-21].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Identify the deceased subject’s name and any dates that would go to FamilySearch. Answer the privacy gate in `SKILL.md` before submitting only the terms needed for the lookup.

If MyHeritage yields no usable entry, try the [FamilySearch United States Social Security Death Index](https://www.familysearch.org/en/search/collection/1202535) with a free sign-in. Count matching entries derived from the same SSA Death Master File record once [S6 @2026-11-22] [S7 @2026-11-22] [S8 @2026-11-22] [S9 @2026-11-22].

When an early file is missing, check the person’s occupation and work dates, following advice from the available excerpt [S16]. Number assignment began for workers in covered employment in November 1936 [S13]. The 1950 amendments extended coverage to qualifying farm and domestic workers. If the person’s work was initially excluded, look for a later covered job and keep the application date open [S14].

## Search the National Archives’ NUMIDENT files

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Identify the deceased applicant’s name and dates or the deceased parent’s name that would go to Access to Archival Databases (AAD). Answer the privacy gate in `SKILL.md` and use only confirmed deceased people’s details. Keep full Social Security numbers in the user’s private research files.

If AAD’s fielded search is accessible and the deceased applicant’s name is uncertain, use the parent-name search from the available excerpt [S17 @2026-11-22]. In the NUMIDENT Application Files, enter a confirmed deceased parent’s name in the field for the father’s name or mother’s maiden name. Start with the file for the applicant’s likely surname, or search across the surname files if it is unknown. Compare the applicant’s birth date and birthplace with known details before using the extract as a lead to the original SS-5 [S18 @2026-11-22].

If AAD is accessible, search the NUMIDENT Death Files for the confirmed deceased subject. Compare the birth and death dates with known details and retain any Social Security number privately [S18 @2026-11-22]. Use the Residence ZIP Code to find a candidate locality for the last residence, following the example from the available excerpt [S17 @2026-11-22]. Match it against a ZIP reference for the record’s period. The Death Payment ZIP Code tracks where SSA sent the death payment. Keep the place of death open until other evidence establishes it [S18 @2026-11-22].

## Interpret the first three digits

Establish when the deceased person’s Social Security number was first assigned before reading its area number. Before centralized issuance in 1972, the first three digits generally reflected the state of issuance. From centralized issuance in 1972 through June 24, 2011, they generally reflected the state associated with the ZIP code of the application’s mailing address. Skip geographic inference for numbers assigned on or after June 25, 2011, when SSA began randomizing assignments [S10] [S11] [S12]. Treat an earlier state as a search lead and verify residence from a separate record. During initial registration, some employees received area numbers tied to their employer’s headquarters even when they worked elsewhere [S11].

## Recover a missing birthplace

Use the original SS-5 for a deceased immigrant if the extract gives no birthplace or only a broad label. Read the exact locality wording and the application's date and compare it with passenger, naturalization or civil records before assigning a village. An application can identify a place to test, including when there is no death-index hit [S1] [S2] [S3].

## Read the original application

On an early SS-5, look for the employer’s name and address when you need a workplace clue. Tie those fields to the application date and transcribe the applicant’s address separately [S13] [S15].

When a married surname or nickname could explain conflicting names, compare the original SS-5’s recorded name, birth date, parents’ names and address with the candidate records. Compare addresses as of their dates. Keep the identities open when the name difference is plausible but the other fields give insufficient or conflicting evidence [S13] [S15].

## Request the document

**Privacy gate:** <!-- privacy-gate: request --> Identify the subject’s name, dates, any Social Security number and proof of death that would go to SSA. Identify and minimize any living relatives’ details. Keep identifiers and returned copies in the user's private research files.

Request the original SS-5 from SSA for the confirmed deceased applicant through its deceased-person FOIA route. Select the original application rather than the Numident extract when the original fields are needed. Check SSA’s current requirements for proof of death and release of parent names before submitting the minimum identifiers [S2 @2026-11-20].

## Handoffs

- [usa immigration search recovery](usa-immigration-search-recovery.md)
- [historical place name resolution](historical-place-name-resolution.md)
- [maiden name recovery](maiden-name-recovery.md)
