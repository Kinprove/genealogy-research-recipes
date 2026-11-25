---
id: "swedish-land-title-record-recovery"
title: "Trace a Swedish property's title through the court books"
summary: "Follow a Swedish parcel through land-title books, court protocols and earlier records when a name search fails."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "SWEDISH-LAND-TITLE-RECORD-RECOVERY-01", "text": "A miss in the land-title book index leaves the earlier court search open."}]
handoff: ["land-index-book-series-recovery", "scandinavian-parish-record-recovery", "tax-roll-observation-workflow", "probate-case-document-inventory"]
checked: null
checked_basis: null
capabilities: {"browse": ["historical record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 230}
---

# Trace a Swedish property's title through the court books

Use this recipe when a Swedish deed, parish entry or farm name is the starting point and the question is who held title to the parcel. Use [parish record recovery](scandinavian-parish-record-recovery.md) to trace its occupants and [tax-roll observations](tax-roll-observation-workflow.md) to read the annual roll.

## Choose the book for the place and date

Identify the dated parish and its court, *häradsrätt* for a rural district or *rådhusrätt* where the town used one. Search the FamilySearch Catalog under that jurisdiction for Land and Property, and compare the series descriptions in Riksarkivet. Use *jordeböcker* to trace the property's tax listing [S1 @2026-11-22], [S2 @2026-11-22], [S5 @2026-11-22].

For a rural parcel around 1875–1933, use the *lagfartsböcker* database and follow the [Swedish property-book route](land-index-book-series-recovery.md#swedish-property-books-follow-rooms-and-changed-parcel-identifiers). For a town parcel, search the town court archive for the relevant year, starting with the title protocols or an older town lot book if the inventory lists one [S6 @2026-11-25].

A miss in the land-title book index leaves the earlier court search open. The orders for *lagfartsböcker* and *inteckningsböcker* date to 1875 and took effect on 1 January 1876. For an earlier transfer, browse the court's *lagfartsprotokoll*, *inteckningsprotokoll* or *småprotokoll*, and check the *dombok* when the separate series is absent [S1], [S2], [S3].

## Trace the transfer

In the older procedure, follow each *uppbud* (announcement) through the later sessions and look for the final *fasta*. Carry forward the property name, applicants, acquisition type, deed date and court date. For earlier volumes without a usable name index, scan the margins for the farm or village and verify it in the entry [S2], [S4].

Look for the prior-title document referenced in a registration from 1806 onward. Where an earlier inheritance has no registration, compare the probate inventory and parish entries and keep the transfer open until its basis is supported [S4].

## Return

List the period parcel designation, court, series, volume, folio and registration date for each step. Keep a tax listing, a dated occupant and a documented title transfer in separate fields.
