---
id: "myheritage-ai-biography-source-audit"
title: "Audit a MyHeritage AI Biography through its contributing sources"
summary: "Generate a scoped MyHeritage AI Biography and trace conflicts, footnotes and photo omissions back to the underlying records and profiles."
kind: "platform"
scope: {"platforms": ["MyHeritage"], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "MYHERITAGE-AI-BIOGRAPHY-SOURCE-AUDIT-01", "text": "Use each biography statement as a lead and assign evidentiary weight to the contributing item."}]
handoff: ["ai-for-documentary-records", "myheritage-profile-hint-extraction", "evidence-proof-judgment"]
checked: "2026-11-22"
checked_basis: "Checked 2026-11-22"
capabilities: {"browse": ["MyHeritage family site and documentation"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool", "upload"], "contact": []}
router: {"section": "Research method", "group": "Family trees and research planning", "order": 22}
---

# Audit a MyHeritage AI Biography through its contributing sources

## Choose what the tool will use

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Profile facts about the deceased person and any living relatives included, plus any selected record details, go to MyHeritage AI Biographer for AI processing, including OpenAI as identified by MyHeritage.

Generate a biography for the selected deceased person after clearing the gate. Open the person’s profile (or select their card in Family View) and choose Create AI Biography. Choose Standard for a profile-only run or Enhanced to bring in matching records, trees and web material. Check the options and audience in the user’s account and record the mode and input. If starting from AI Record Finder, open the found historical record and use the biography option in its record view when available. [S1 @2026-11-22], [S2 @2026-11-22] [S3 @2026-11-22]

**Privacy gate:** <!-- privacy-gate: upload --> Documented profile fields about the deceased person and any living relatives named go to the selected MyHeritage tree.

Add documented occupation, education or immigration facts only if the biography control is disabled for a sparse profile and the additions are supported and authorized. Return to the profile and check whether generation is available. [S1 @2026-11-22], [S2 @2026-11-22]

## Trace the statements and omissions

Open Consistency Issues if the biography shows it, and put each conflicting value in its own evidence row. Follow the footnotes to the contributing historical record, tree profile or web page, then inspect what the item actually says. Use each biography statement as a lead and assign evidentiary weight to the contributing item. Keep an unresolved value open when the cited item does not support the narrative. [S1 @2026-11-22], [S2 @2026-11-22]

Check the selected person’s tagged photos in the tree when a photo is absent from the narrative. The biography shows a selection of tagged photos. The omission leaves open what is present in the photo collection. [S1 @2026-11-22]
