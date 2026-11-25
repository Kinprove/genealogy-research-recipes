---
id: "sound-toll-captain-voyage-recovery"
title: "Recover a merchant captain's voyage in the Sound Toll Registers"
summary: "Use Sound Toll passages and port notices to trace a merchant captain without treating a register miss as a missing Baltic voyage."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "SOUND-TOLL-CAPTAIN-VOYAGE-RECOVERY-01", "text": "A voyage entirely within the Baltic need not appear in the Sound Toll Registers."}]
handoff: ["swedish-military-record-routing", "historical-newspaper-section-search", "posttidningar-issue-recovery", "archival-image-coverage-verification"]
checked: null
checked_basis: null
capabilities: {"browse": ["historical record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 241}
---

# Recover a merchant captain's voyage in the Sound Toll Registers

Use when a merchant captain turns up in a parish source, port notice or newspaper item and you need to check a proposed voyage. For a military sailor, use [Swedish military records](swedish-military-record-routing.md).

## Decide whether the passage belongs in the toll accounts

Read *coopvardiekapten* as a merchant captain in the cited Swedish usage. Copy the name as printed, departure and destination ports and the best-supported date window. Before searching, decide whether the route calls for passage through the Sound between Denmark and Sweden [S1], [S2], [S3], [S4].

A voyage entirely within the Baltic need not appear in the Sound Toll Registers. The surviving toll accounts span 1497–1857 with earlier gaps. Keep an in-Baltic voyage in scope for port records and shipping notices even if no toll entry was found [S1], [S2].

## Look up a candidate passage

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The voyage query sends a deceased captain's name and any date or port terms to the Sound Toll Registers Online service. Apply the privacy gate in `SKILL.md` before submitting the search.

From the Groningen dataset description follow the link to Sound Toll Registers Online. Use Database 1 for years before 1634 and Database 2 from 1634 onward. Have the user verify which search entry point opens. Search by the historical captain's name where supported. Compare candidate passages by captain, ports and direction. Follow the register reference before relying on a detail from the database reconstruction [S1 @2026-11-22], [S2 @2026-11-22], [S3 @2026-11-22].

## Check newspaper ports and dates

Look for arrivals and departures under each likely port and compare the stated cargo, origin or destination when given. Keep the issue date separate from the sailing or arrival date. Carry same-name captains as alternatives until the route or other records support the match [S1].

## Return

Give the vessel or captain lead, route, date range, the database or newspaper runs inspected, and any passage or original-register locator.
