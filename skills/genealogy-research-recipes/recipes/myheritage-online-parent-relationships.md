---
id: "myheritage-online-parent-relationships"
title: "Manage biological, adoptive and foster parents in MyHeritage"
summary: "Inspect, correct and display multiple sets of parents on a MyHeritage online tree."
kind: "platform"
scope: {"platforms": ["MyHeritage"], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "MYHERITAGE-ONLINE-PARENT-RELATIONSHIPS-01", "text": "A dashed line alone cannot distinguish adoptive parents from foster parents."}]
handoff: ["myheritage-profile-hint-extraction", "evidence-proof-judgment"]
checked: "2026-11-22"
checked_basis: "read 2026-11-22"
capabilities: {"browse": ["MyHeritage"], "local_script": [], "extensions": [], "data_transfer": ["publish", "link"], "contact": []}
router: {"section": "Research method", "group": "Family trees and research planning", "order": 25}
---

# Manage biological, adoptive and foster parents in MyHeritage

Open the child’s profile on the MyHeritage website. A dashed line alone cannot distinguish adoptive parents from foster parents. Use the relationship shown in Manage parents and check it against the evidence before changing the tree.

## Inspect and display the recorded parent sets

Open More → Manage parents from the child’s profile. On the tree card, +1 and +2 count additional parent sets. Select the badge to open the manager and read the assigned type for each set, including either adoptive or foster for a dashed line [S1 @2026-11-22] [S3 @2026-11-22].

For a temporary view, select Show in tree on the required parent card. To make adoptive parents the default display, use the Settings cog, open Other options and enable Display adoptive parents by default. Confirm the setting in the user’s tree before relying on the display [S1 @2026-11-22] [S3 @2026-11-22].

## Add or correct a parent relationship

**Privacy gate:** <!-- privacy-gate: publish --> Saving parent names or a corrected relationship records the child’s and each parent’s data in MyHeritage, visible according to the tree settings. Apply the privacy gate before saving data about anyone who may be living.

Add a parent set from Manage parents → Add more parents, select its documented type and enter the known name or names. Leave an unknown second card empty and select Done [S1 @2026-11-22] [S3 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: publish --> A change of type shares the child’s and affected parents’ biological, adoptive or foster association with the MyHeritage tree audience. Apply the privacy gate to every affected person who may be living.

Correct the assigned parent type with the dropdown above the parent cards and select Done. If the chosen type already belonged to another set, reopen the manager and check every affected set for automatic reassignment [S1 @2026-11-22] [S3 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: link --> Linking existing profiles records the child’s and selected parent’s association on MyHeritage. Apply the privacy gate before linking if either person may be living.

Link an existing parent profile from the child’s profile panel via More → Connect to an existing person → Connect to a parent. Pick the intended profile and select OK. Reopen Manage parents to confirm the assigned type and affected sets [S1 @2026-11-22] [S2 @2026-11-22].

## Return the relationship record

Record the evidence for each assigned type, the affected profiles and the verified result. For relationship claims derived from Hints, use [profile Hint extraction](myheritage-profile-hint-extraction.md). For conflicting evidence, use [evidence and proof judgment](evidence-proof-judgment.md).

## Sources

[Bibliography and credits](https://github.com/Kinprove/genealogy-research-recipes/blob/2b4157d8449d36b2a0e62fb1f75fe9f581deb15a/skills/genealogy-research-recipes/sources/myheritage-online-parent-relationships.md).
