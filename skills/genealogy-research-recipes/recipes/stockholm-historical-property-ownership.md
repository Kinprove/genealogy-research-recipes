---
id: "stockholm-historical-property-ownership"
title: "Link a historical Stockholm household to its lot and title records"
summary: "Identify a Stockholm lot across its historical numbers and compare household residence with dated title and probate evidence."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "STOCKHOLM-HISTORICAL-PROPERTY-OWNERSHIP-01", "text": "Establish residence and ownership from their own dated records."}]
handoff: ["tax-roll-observation-workflow", "land-index-book-series-recovery", "historical-map-record-recovery", "probate-case-document-inventory"]
checked: null
checked_basis: null
capabilities: {"browse": ["public catalogues and historical record images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 221}
---

# Link a historical Stockholm household to its lot and title records

Use this route when a historical Stockholm roll or inventory names a block and number, and you need to identify the property or establish who owned it at the time.

## Identify the lot across numbering systems

Copy the ward, block, number and street wording as written. In Gamla stan, check which numbering system applies. The 1729 numbers run by district, and the 1810 numbers run within each block. Compare the two maps and keep both numbers where you find a match. Keep all candidate old lots when a newer lot combines them [S2], [S3].

According to the author’s case, carry the block and historic lot number into the *1729 och 1810 års tomtnummer* comparison to look for its street address [S4†]. Verify the result against the map and property wording [S2], [S3].

## Check title separately from residence

Use *Fastighetsregister 1675–1875* at Stockholm City Archives to identify the property’s card, then follow the card into the transaction protocol or underlying contract. Compare the acquired share and lot wording, and keep purchase, registered title and sale dates separate [S1], [S3].

Establish residence and ownership from their own dated records. Compare the probate inventory’s address and property list with the historical poll-tax roll and the dated title record. If a roll appears to show tenancy, test the tenure reading against the title date for the same lot. In the reported Stockholm case, the title predated the roll that had been read as tenancy [S1], [S3].

According to the author’s household example, compare the address in the estate inventory with the spouse’s separate entries in earlier and later population registers [S5†].

If a later sale names heirs of a much earlier owner, compare the intervening beneficiary’s death date with the earlier will. Check for a clause returning the property to the former estate. Carry the old and new lot identifiers into the title and estate documents [S1].

## Return packet

Return the block, street and both lot numbers, each dated residence observation and the locator for each title or probate document. For a missed name search, use [annual tax-roll recovery](tax-roll-observation-workflow.md). For an unresolved parcel change, use [historical map recovery](historical-map-record-recovery.md).
