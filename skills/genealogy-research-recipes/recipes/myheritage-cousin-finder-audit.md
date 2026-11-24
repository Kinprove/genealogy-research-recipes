---
id: "myheritage-cousin-finder-audit"
title: "Audit MyHeritage Cousin Finder relationships against both trees"
summary: "Use Cousin Finder to find and audit tree-derived relationships, separate DNA matches from profile matches, and act on documented links."
kind: "platform"
scope: {"platforms": ["MyHeritage"], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "MYHERITAGE-COUSIN-FINDER-AUDIT-01", "text": "Treat each Cousin Finder relationship as a hypothesis based on the two trees."}]
handoff: ["myheritage-profile-hint-extraction", "cousin-relationship-paths", "myheritage-dna-match-investigation", "dna-match-outreach-staging", "gedcom-research-export"]
checked: "2026-11-22"
checked_basis: "Checked 2026-11-22"
capabilities: {"browse": ["MyHeritage family site and documentation"], "local_script": [], "extensions": [], "data_transfer": ["link", "upload"], "contact": ["contact"]}
router: {"section": "Research method", "group": "Family trees and research planning", "order": 23}
---

# Audit MyHeritage Cousin Finder relationships against both trees

## Check the starting profile and matching scope

Open Discoveries → Cousin Finder in the MyHeritage website and identify the tree and starting profile. For another individual, look for Cousin Finder under More actions on that profile. A result requires a Smart Match that connects the starting profile and another tree-linked member through a shared direct ancestor. An omitted relative leaves the relationship open; check whether a suitable tree, linked member, direct-ancestor match or matching setting is missing. [S1 @2026-11-22], [S2 @2026-11-22]

**Privacy gate:** <!-- privacy-gate: link --> Tree profiles and relationships of the people included become eligible for MyHeritage matching with other family sites.

Enable Smart Matching for the chosen tree only after clearing the gate. Reopen Discoveries → Cousin Finder and record the tree and date shown in the account. [S1 @2026-11-22], [S2 @2026-11-22], [S4 @2026-11-22]

**Privacy gate:** <!-- privacy-gate: upload --> The selected relatives’ GEDCOM profiles, events and relationship fields go to the named MyHeritage family site.

Import a reviewed GEDCOM into the intended family site only if the relevant tree does not already exist there. Use Family Tree → Import GEDCOM, after reviewing the [GEDCOM export](gedcom-research-export.md) and clearing the gate. [S1 @2026-11-22], [S3 @2026-11-22]

**Privacy gate:** <!-- privacy-gate: upload --> New documented profiles and vital events for the relatives concerned go to the named MyHeritage tree.

Add supported profiles or events to the chosen tree only after clearing the gate. When few matches appear, identify the documented people, dates or places missing on the branch before adding any new tree detail. [S1], [S2]

## Audit the proposed connection

Treat each Cousin Finder relationship as a hypothesis based on the two trees. Under View relationship, identify which nodes the other tree supplied by their dashed borders and tree icons. Open those nodes and check each parent-child link across the proposed path, including a possible closer path. A Smart Match compares profiles. Use the separate DNA Match label to find an available genetic comparison and follow [DNA match investigation](myheritage-dna-match-investigation.md) for what it can support. [S1 @2026-11-22], [S2 @2026-11-22]

Open More details on the card and follow the pending or confirmed match count to the relevant match list. Check the underlying evidence with [profile Hint extraction](myheritage-profile-hint-extraction.md). Reject matches only where the evidence supports rejection and the user authorized that change, then use Recalculate and compare the path before and after. [S1 @2026-11-22], [S2 @2026-11-22]

## Filter the existing leads

Filter to the target family branch and read each card’s shared ancestors and both relationships. Include spouses of cousins when weighing relatives by marriage as possible leads. Clear Show members of your site when the worklist should exclude people already on it. [S1 @2026-11-22], [S2 @2026-11-22]

**Privacy gate:** <!-- privacy-gate: contact --> The sender’s identity, the recipient’s own data and a minimal first question go to the selected recipient through the MyHeritage inbox.

Use Contact on a displayed result only for authorized outreach through the route already available in the user’s account. Follow the [Living people rule](../SKILL.md#living-people) and use [outreach staging](dna-match-outreach-staging.md) for the consent, disclosure and log. Keep unverified relationship details out of the first message. [S1 @2026-11-22], [S2 @2026-11-22]
