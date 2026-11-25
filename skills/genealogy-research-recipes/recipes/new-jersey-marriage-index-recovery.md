---
id: "new-jersey-marriage-index-recovery"
title: "Follow a New Jersey marriage index entry to the underlying record"
summary: "Decode New Jersey marriage index numbers and place fields, then route the underlying certificate by marriage year."
kind: "records"
scope: {"platforms": ["myheritage"], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "NEW-JERSEY-MARRIAGE-INDEX-RECOVERY-01", "text": "Keep the application date separate from the date of the marriage."}]
handoff: ["missing-marriage-jurisdiction-search", "us-vital-registration-coverage", "myheritage-historical-record-search"]
checked: null
checked_basis: null
capabilities: {"browse": ["public finding aids and record catalogues"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool", "request"], "contact": []}
router: {"section": "Records by country and region", "group": "United States: people, vital and church records", "order": 247}
---

# Follow a New Jersey marriage index entry to the underlying record

Use this recipe when a New Jersey marriage from 1915 onward has an index hit or a probable year. Keep the application date separate from the date of the marriage. For a search that still lacks a candidate jurisdiction, use [missing marriage jurisdiction search](missing-marriage-jurisdiction-search.md). For collection filters and failed searches in MyHeritage, use [MyHeritage historical record search](myheritage-historical-record-search.md).

## Check both spouse indexes

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Names and approximate marriage years of the spouses go to MyHeritage.

Search the New Jersey Marriage Licenses index in MyHeritage for each spouse separately if a combined search fails or only one person is shown. Compare the underlying bride and groom index images where they survive. Keep variant-spelling rows together as possible duplicates until the year, file number and original record settle whether they describe one marriage [S1], [S2].

Transcribe each date under its own field label. If MyHeritage shows a license application date, use it as an application date. Establish the ceremony date from the underlying record [S1], [S2].

## Decode the image by period

For 1915–1919, retain the whole State File Number with the marriage year. Read its first two digits as the volume and the last three as the certificate number. Keep the year because the certificate number resets. Those index images omit the place code. Confirm the place in the underlying record [S1], [S3], [S4].

For 1920–1929, read the two-digit place code as a county code. For 1930–1964, keep the original code and take its first four digits for the place key. For 1965–1984, use the four digits as printed. MyHeritage’s collection announcement identifies a key for some codes. If the code is unresolved, leave the place provisional until you read the original. From 1985, read the field as an abbreviated place name [S1].

## Route the underlying record

For 1915–1929, start with the marriage year and groom’s surname in the State Archives reel guides. For marriages through 1950 use the New Jersey State Archives holdings route. From 1951, use the Department of Health as custodian. For 1951–1957 also check the State Archives’ in-person microfilm and available bride indexes [S1 @2026-11-22], [S3 @2026-11-22], [S4 @2026-11-22], [S5 @2026-11-22], [S6 @2026-11-22], [S7 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: request --> The spouses’ identifying details and any required proof from the applicant go to the New Jersey office selected in the preceding step.

Prepare a copy request for the underlying marriage record using the receiving office’s instructions. For a recent state record check the exact ceremony date, city and both names before submitting, and check identity and eligibility requirements for the kind of copy sought [S6 @2026-11-22], [S7 @2026-11-22], [S8 @2026-11-22], [S9 @2026-11-22].

Read the marriage record for the marriage date and place, spouses’ residences, birth details, occupations, prior marital status and any recorded details of their parents. Mark any missing fields individually [S1].

## Return packet

Return the index and image locator, each spouse search, literal and interpreted codes, dates by event, receiving office, and original or outstanding access step.
