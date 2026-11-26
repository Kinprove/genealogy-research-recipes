---
id: "filae-historical-record-search"
title: "Find and verify a French historical record in Filae"
summary: "Choose the Filae collection that covers a French event, narrow by relatives and carry the result to the underlying record."
kind: "platform"
scope: {"platforms": ["Filae"], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "FILAE-HISTORICAL-RECORD-SEARCH-01", "text": "Check the collection’s place and year before interpreting a Filae miss."}]
handoff: ["french-departmental-record-routing", "french-belgian-civil-act-extraction", "french-succession-and-absence-tables"]
checked: "2026-11-22"
checked_basis: "read 2026-11-22"
capabilities: {"browse": ["Filae search forms, source descriptions and historical images"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool"], "contact": []}
router: {"section": "Record websites, libraries and maps", "group": "Record websites", "order": 57}
---

# Find and verify a French historical record in Filae

Use this recipe to recover a specific French birth, marriage, death, census or other historical entry when Filae's broad person search yields several candidates or no useful record. Check the collection’s place and year before interpreting a Filae miss.

## Choose a source before narrowing the name

According to the presenter, start with Search for a Source when you know the type of event [S1† @2026-11-22]. Use Filae’s source list to check the collection scope and choose the likely series before submitting a name [S2 @2026-11-22].

For a birth, marriage or death around the change to civil registration, check both the eighteenth-century parish collections and the civil-registration collections beginning in 1792. For a census, check the commune and the year, including the indexed 1872 and 1906 collections where applicable. [S3 @2026-11-22] [S4 @2026-11-22]

For a military or service clue, check the specific conscription, prisoner-of-war or decoration collection. For a civil pension or naturalization lead, look for the relevant entry in the Bulletin des lois holdings. Record the series searched before reading a miss. [S3 @2026-11-22] [S4 @2026-11-22]

For a departure lead, check Embarquements, Passeports, Passagers for a collection matching the port and year. Bordeaux passports and passenger lists are listed separately. Check naturalizations under their own series when the clue is acquisition of citizenship. [S2 @2026-11-22] [S4 @2026-11-22]

For a birth less than 120 years ago, check Filae’s stated birth-indexing boundary before treating an empty result as evidence. Check a death collection against its own coverage and use [departmental record routing](french-departmental-record-routing.md) to identify the correct register keeper. [S6 @2026-11-22]

## Run a person search and test the role

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Target and relative names and any date or place filters go to Filae. Complete the gate in `SKILL.md` first if the query could identify a living person.

Run a Filae person search with the target’s name and approximate place and year. If several matches remain, add one known spouse or parent and rerun. If that removes the expected hit, retry without the relative filter and inspect the indexed names and roles. Use the source filter to distinguish a civil act or census from a tree lead. [S3 @2026-11-22] [S5 @2026-11-22]

In the surname field, use `?` for one uncertain character and `*` for several. Keep the exact form as a separate run so the wildcard does not obscure which spelling produced a hit. [S7 @2026-11-22]

If the place is uncertain, inspect the map distribution and compare candidate places with the written event place in each result. Keep event and residence separate when the same indexed source shows both. [S4 @2026-11-22] [S5 @2026-11-22]

## Carry the result to the cited record

Copy Filae’s source label, person’s role, commune, event date and reference. Open the linked image when available. If the result stops at an abstract or a member tree, use the commune, series and date to locate the record through [departmental routing](french-departmental-record-routing.md). Use [civil-act extraction](french-belgian-civil-act-extraction.md) to read the act. [S3 @2026-11-22] [S5 @2026-11-22] [S6 @2026-11-22]

## Sources

[Source bibliography and credits](../sources/filae-historical-record-search.md).
