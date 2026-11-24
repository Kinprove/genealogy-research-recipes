---
id: "mehedinti-civil-register-recovery"
title: "Find Mehedinți civil registers by locality, event and year"
summary: "Use Genealogica’s Mehedinți inventory to locate the relevant civil register and check what the digitized volumes cover."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "MEHEDINTI-CIVIL-REGISTER-RECOVERY-01", "text": "Treat an omitted year as a gap in listed coverage."}]
handoff: ["archival-image-coverage-verification", "historical-place-name-resolution"]
checked: null
checked_basis: null
capabilities: {"browse": ["public catalogues and historical records"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Central and Eastern Europe by period state", "order": 93}
---

# Find Mehedinți civil registers by locality, event and year

## Find the locality under its commune

Open the Mehedinți inventory, find the commune heading and select the locality link for the event. For Crivina start under Burila Mare. If the map loads in your browser, use the county-filtered map to orient candidate localities, then return to the locality listing to get the register references. [S1 @2026-11-22], [S2 @2026-11-22]

## Test the event type and year

Check both the historical and current locality labels. The inventory lists *Pătuele* and *Pătulele* with different year ranges but sends both to the same locality page. Read both rows and verify the linked entries for the target year and event. [S1 @2026-11-22], [S3 @2026-11-22]

Treat an omitted year as a gap in listed coverage. In the locality’s external resources, identify the intended event series, inspect the title and date span of its eANR reference, and distinguish an original from a transcription. Include adoption or divorce only when the specific listing supports that event type. [S1 @2026-11-22], [S3 @2026-11-22]

## Return packet

Record the locality as named in the listing, the period place, the event series, years and any gaps, and the exact eANR locator. Use [historical place-name resolution](historical-place-name-resolution.md) for competing place identifications and [archival image coverage](archival-image-coverage-verification.md) if a volume is linked but its image boundaries are unclear.
