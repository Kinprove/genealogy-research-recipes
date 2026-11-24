---
id: "myheritage-tree-event-and-place-audit"
title: "Audit a MyHeritage tree with consistency checks, timelines and maps"
summary: "Use MyHeritage profiles, consistency flags, timelines and PedigreeMap to turn date and location anomalies into an evidence worklist."
kind: "platform"
scope: {"platforms": ["MyHeritage"], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "MYHERITAGE-TREE-EVENT-AND-PLACE-AUDIT-01", "text": "Treat a flag, plotted event or unusual age as a lead to inspect the underlying entry."}]
handoff: ["myheritage-country-coding-place-audit", "evidence-proof-judgment", "historical-place-name-resolution"]
checked: "2026-11-22"
checked_basis: "Checked 2026-11-22"
capabilities: {"browse": ["MyHeritage family site and documentation"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Research method", "group": "Family trees and research planning", "order": 26}
---

# Audit a MyHeritage tree with consistency checks, timelines and maps

## Choose a tree and inspect its date flags

In Family Tree → Consistency Checker, choose the intended tree. Review flags for children born before a parent or long after a parent’s death, unusually young parents and large spouse age gaps. For a profile flagged at advanced age, verify the birth date and check for evidence of death before proposing a change to living status. Treat a flag, plotted event or unusual age as a lead to inspect the underlying entry. [S1 @2026-11-22], [S2 @2026-11-22]

Open Family Tree Timeline for the target profile and compare a parent’s age at each recorded birth against the family events shown. Use historical events as timeline context and trace a surprising date or a gap back to the supporting record. [S1 @2026-11-22], [S4 @2026-11-22]

## Turn the map into a place worklist

Open PedigreeMap from the Family Tree menu, using More if your account groups it there. Choose the tree, anchor person and proximity filter. Select a country or locality and open the events at that location to get the involved profiles. Use event and time filters before interpreting a cluster. [S1 @2026-11-22], [S3 @2026-11-22]

Review available place warnings and trace each spelling, misplaced pin or ambiguous locality to its source. Open the [Country Coding audit](myheritage-country-coding-place-audit.md) for uncoded place names and misleading modern flags. [S1 @2026-11-22], [S3 @2026-11-22], [S4 @2026-11-22]

## Pick a view suited to the check

Use List view to sort or narrow the set of profiles for review. Use Pedigree view to follow direct ancestors compactly, or Fan view to compare how far their branches extend and which generation has a gap. Verify the fields available for sorting and filtering in the account. [S4 @2026-11-22], [S5 @2026-11-22]
