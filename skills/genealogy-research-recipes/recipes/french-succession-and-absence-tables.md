---
id: "french-succession-and-absence-tables"
title: "Follow a French succession or absence table to its declaration"
summary: "Use a French registration-office index to distinguish a recorded death from declared absence and retrieve the referenced succession declaration."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "FRENCH-SUCCESSION-AND-ABSENCE-TABLES-01", "text": "Read the event field before assigning a death date from a succession or absence table."}]
handoff: ["french-departmental-record-routing", "french-belgian-civil-act-extraction", "probate-case-document-inventory"]
checked: null
checked_basis: null
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 179}
---

# Follow a French succession or absence table to its declaration

Read the event field before assigning a death date from a succession or absence table.

## Identify the person and registration office

Start with the département’s succession and absence tables or the *France, Tables of Successions and Absences, 1890–1970* index. Identify the registration office and locality on the source image. Copy the stated residence, age, spouse and event place and date when present. Read the table's column headings to distinguish death from formally established absence. Keep the tax registration date separate from the event date [S1 @2026-11-20] [S2 @2026-11-20] [S3 @2026-11-20].

Before interpreting a MyHeritage miss, check whether the collection covers the target département and years [S4 @2026-11-21] [S5 @2026-11-21]. If coverage is missing or uncertain, record the gap or uncertainty and look for the relevant office and years in the departmental archive’s table inventory [S6 @2026-11-21].

MyHeritage allows searching without a subscription, and full record access may require one [S4 @2026-11-21] [S7 @2026-11-21]. Check whether the user’s account can open the scan. If it shows only the index hit, look for the corresponding departmental table image [S5 @2026-11-21] [S6 @2026-11-21]. On the image, copy the birth date, birthplace and parents’ names when given [S4 @2026-11-21] [S5 @2026-11-21].

If the civil death act is out of reach or the death date or commune is uncertain, look for the stated death date and commune in the succession table. Carry both details to the civil register when it is available [S4 @2026-11-21] [S8 @2026-11-21]. For a possible death in 1970, also check Insee’s named death files [S9 @2026-11-21].

Use the registration office on a hit to narrow the possible communes of residence or death [S4] [S5]. Check which communes the office served at the time of the event before assigning a place from the office name. If the residence and death communes fall under different offices, check both tables and follow any *renvoi* to the office it names [S6].

## Use the reference to find the declaration

Copy the registration office, declaration date and entry or volume reference when supplied. Browse that office's chronological succession declaration register for the reference on the table. Check the declaration for named heirs, relationships and any notarial act. When the table has no usable reference, record the limit and check the civil act separately [S1] [S2] [S3].

## Handoffs

- [french departmental record routing](french-departmental-record-routing.md)
- [french belgian civil act extraction](french-belgian-civil-act-extraction.md)
- [probate case document inventory](probate-case-document-inventory.md)
