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
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 119}
---

# Follow a French succession or absence table to its declaration

Read the event field before assigning a death date from a succession or absence table.

## Identify the person and registration office

Start with the département’s succession and absence tables or the *France, Tables of Successions and Absences, 1890–1970* index. Identify the registration office and locality on the source image. Copy the stated residence, age, spouse and event place and date when present. Read the table's column headings to distinguish death from formally established absence. Keep the tax registration date separate from the event date [S1 @2026-11-20] [S2 @2026-11-20] [S3 @2026-11-20].

## Use the reference to find the declaration

Copy the registration office, declaration date and entry or volume reference when supplied. Browse that office's chronological succession declaration register for the reference on the table. Check the declaration for named heirs, relationships and any notarial act. When the table has no usable reference, record the limit and check the civil act separately [S1] [S2] [S3].

## Handoffs

- [french departmental record routing](french-departmental-record-routing.md)
- [french belgian civil act extraction](french-belgian-civil-act-extraction.md)
- [probate case document inventory](probate-case-document-inventory.md)
