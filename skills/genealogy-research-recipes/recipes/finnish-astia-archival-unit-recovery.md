---
id: "finnish-astia-archival-unit-recovery"
title: "Recover a Finnish archival unit in Astia"
summary: "Find a Finnish archival unit from its call number, series or creator and determine how to consult it when Astia search or images fail."
kind: "platform"
scope: {"platforms": ["Astia"], "tasks": ["Finnish archive hierarchy", "archival call number (signum)", "digitized versus paper access"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "FINNISH-ASTIA-ARCHIVAL-UNIT-RECOVERY-01", "text": "An empty digital-only search leaves the archival unit's availability unresolved."}]
handoff: ["archival-image-coverage-verification", "scandinavian-parish-record-recovery", "local-repository-uncatalogued-holdings"]
checked: "2026-11-22"
checked_basis: "read 2026-11-22"
capabilities: {"browse": ["Astia and Arkistojen Portti catalogues", "public archival images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"section": "Record websites, libraries and maps", "group": "Record websites", "order": 55}
---

# Recover a Finnish archival unit in Astia

Find a Finnish archival unit from its call number, series or creator and determine how to consult it when Astia search or images fail.

## Start with the creator and unit

For a citation with a call number (*signum*), search Astia with the archive title and the exact call number together. If the combined query misses, try the archive title alone and verify each hit's parent collection before using it. [S1 @2026-11-22] [S3 @2026-11-22]

When the citation lacks the unit title, find the creator or collection in **Selaa aineistoja** (browse holdings). Expand the collection, series and subseries to the target unit. Check the unit card's identifier and inclusive dates before opening its images. Use the record-type finding aid in Arkistojen Portti to identify the creator or series when the archive name is uncertain. [S2 @2026-11-22] [S4 @2026-11-22]

## Recover from a digital search miss

An empty digital-only search leaves the archival unit's availability unresolved. Remove the digital and year filters, open the parent collection or creator card, and inspect the relevant series and unit cards. Use each card's date range and access information to decide what to inspect. Apply a digital filter again only after identifying the collection. [S1 @2026-11-22] [S2 @2026-11-22] [S3 @2026-11-22]

Check Digihakemisto for a contributed contents list before browsing an Astia image set. Use its entries to reach a candidate image, then cite the archive unit and the page or image you actually inspected. For parish books, distinguish a microfilm-derived scan from images made from the paper original when the description identifies the source. [S7 @2026-11-22] [S9 @2026-11-22]

## Choose a route to a known unit

On the unit card, distinguish a public image, a restricted digital image and an undigitized holding. If earlier image links fail, look up the unit again by call number. Check the archive's microfilm and microfiche lists for a surviving surrogate while replacement images are pending, and note the format and reading-room route that remain available. Use the access instructions for that unit when a permit or on-site consultation is required. Digitized or microfilmed material is generally supplied through the available surrogate. [S5 @2026-11-22] [S6 @2026-11-22] [S8 @2026-11-22] [S9 @2026-11-22]

**Privacy gate:** <!-- privacy-gate: request --> An Astia record request sends the user's account details and any subject identifiers in the request to the National Archives of Finland. For anyone who may be living, keep the draft local until the [record-request gate](../SKILL.md#record-requests) is cleared. [S5 @2026-11-22]

If a reading-room consultation or a copy is needed, submit the Astia request with the exact archival unit reference and only the details the archive requires. [S5 @2026-11-22]

## Return the locator and access status

Record the creator, collection path, series, call number, unit title, inclusive dates and stable card link. Add the page and image number when read. For a miss, record the filters tried, the collection and series browsed, and the next access route. Use [archival image coverage](archival-image-coverage-verification.md) to test a gap within an image set and [Scandinavian parish records](scandinavian-parish-record-recovery.md) to continue a household trail.
