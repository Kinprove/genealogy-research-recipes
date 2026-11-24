---
id: "romanian-historical-census-household-recovery"
title: "Find a household in Romania’s 1930, 1941 or 1948 census"
summary: "Locate Romanian census household records by census-year jurisdiction and distinguish original household schedules from surviving summaries and archive extracts."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "ROMANIAN-HISTORICAL-CENSUS-HOUSEHOLD-RECOVERY-01", "text": "Classify a 1948 borderou as a summary and an extras from it as an extract."}]
handoff: ["bessarabia-moldova-record-routing", "galicia-bukovina-habsburg-record-routing", "historical-place-name-resolution"]
checked: null
checked_basis: null
capabilities: {"browse": ["catalogues and historical records"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"section": "Records by country and region", "group": "Central and Eastern Europe by period state", "order": 101}
---

# Find a household in Romania’s 1930, 1941 or 1948 census

Use this recipe to look for a named household in an original Romanian census record or a surviving summary. Start with the year and the place’s jurisdiction on the census date.

## Find the census material that survives for the place

For 1930, use the historic village, commune and interwar county to look for a household schedule, then check which office holds the relevant volume. For 1941, look for the household return and any agricultural schedule separately. For 1948, look for the population, property and agricultural summaries. The archival study records a decision in 1974 to discard completed 1948 schedules and retain the summary lists [S1] [S2].

Classify a 1948 borderou as a summary and an extras from it as an extract. Record the exact heading, archive reference, census year and later date of the extract. Check which household or holding details are actually present before treating an omitted field as evidence [S1] [S2].

According to the supplied excerpt from the community article, one archive response carries the heading *Extras din borderoul populației, proprietăților și exploatațiilor agricole* [S5†].

## Prepare a specific request

Draft a request giving the census year and the locality under its census-date name. Specify the household or holding sought, distinguishing name variants from separate people. Confirm the current holder, the available record type and the terms of access before submitting [S2 @2026-11-22] [S3 @2026-11-22] [S4 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: request --> Apply the [privacy gate](../SKILL.md#privacy-gate) to the household names, historical locality and required eligibility evidence before sending a request about anyone who may be living to the archival office.

Send a census copy request through the confirmed office’s official service once the permitted details and any evidence of eligibility are in place [S4 @2026-11-22].
