---
id: "myheritage-profile-hint-extraction"
title: "Review a MyHeritage profile Hint before copying facts or relatives"
summary: "Review the evidence behind a MyHeritage Hint, compare conflicting values and save only the supported facts or relationships."
kind: "platform"
scope: {"platforms": ["MyHeritage"], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "MYHERITAGE-PROFILE-HINT-EXTRACTION-01", "text": "Decide which facts the source supports before selecting any arrows."}]
handoff: ["myheritage-historical-record-search", "evidence-proof-judgment"]
checked: "2026-11-18"
checked_basis: "Read 2026-11-18"
capabilities: {"browse": ["public catalogues, documentation and historical records"], "local_script": [], "extensions": [], "data_transfer": ["link", "publish"], "contact": ["contact"]}
router: {"section": "Research method", "group": "Family trees and research planning", "order": 18}
---

# Review a MyHeritage profile Hint before copying facts or relatives

Use this recipe from a MyHeritage tree profile with a Hint that may supply facts or relatives. Decide which facts the source supports before selecting any arrows.

## Read beyond the highlighted hint

Open the person’s **Profile**, open the **Hint** and choose **Review** on the relevant source card. Scroll through the side-by-side comparison and open the underlying source where available. Review fields beyond the yellow highlighting. Check whether the source concerns the same person. [S1 @2026-11-18]

When tracing an emigrant branch from a Smart Match, open the matching tree if you have access. Find a relative you can already place in your own tree and follow the relationships from that person toward the emigrant branch. [S3 @2026-11-20] Check the tree even when the match adds no facts about the matched person. If you cannot open the tree, inspect the Smart Match’s close-family comparison for leads. [S4 @2026-11-20] Verify each relationship before copying it.

**Privacy gate:** <!-- privacy-gate: contact --> The message shares the sender’s identity and the names or relationships needed for the question with the matching site manager through MyHeritage. Apply the [privacy gate](../SKILL.md#privacy-gate) and the [Living people contact rules](../SKILL.md#living-people) before sending.

If a relationship on the branch needs clarification, open the person’s Smart Matches list. Click or hover on the matching site manager’s name and choose **Contact** if available in your account. Ask the manager which source supports the relationship. [S5 @2026-11-20]

## Select values and relationships individually

**Privacy gate:** <!-- privacy-gate: link --> The association between the online profile and the source or matching tree would be recorded on MyHeritage. Apply the [privacy gate](../SKILL.md#privacy-gate) before linking if either side identifies a person who may be living.

Confirm the profile match only once you have established the correspondence. Then open the extraction panel for the fact review. [S1 @2026-11-18]

In **Extract information**, choose the arrows for the supported fields. Compare each selected value with the previous tree value shown beneath it. Use the revert control for an unwanted replacement. Use the pencil on a selected row to edit the value inline when the source supports the edited wording. [S1 @2026-11-18]

In **Immediate family**, open **More details** and inspect the available facts for the relative. Select the supported facts and relationship before adding the relative to the tree. [S1 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: publish --> The source facts and selected family relationships become available in the MyHeritage tree according to its visibility settings. Apply the [privacy gate](../SKILL.md#privacy-gate) before saving any data about people who may be living.

Use **Save to tree** for the selected facts and relatives after reviewing the scope of the change. Reopen the profile to check the new values and their linked citations, keeping a reference to the underlying source for anything the generated citation omits. [S1 @2026-11-18], [S2 @2026-11-18]
