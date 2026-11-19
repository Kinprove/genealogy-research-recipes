---
id: "find-a-grave-memorial-corrections"
title: "Correct a Find a Grave memorial or request its management"
summary: "Send evidence-backed Find a Grave corrections and route management requests to the right recipient."
kind: "platform"
scope: {"platforms": ["Find a Grave"], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "FIND-A-GRAVE-MEMORIAL-CORRECTIONS-01", "text": "Select the correction or management action from the memorial itself."}]
handoff: ["burial-evidence-packet"]
checked: "2026-11-18"
checked_basis: "Read 2026-11-18"
capabilities: {"browse": ["public catalogues, documentation and historical records"], "local_script": [], "extensions": [], "data_transfer": ["publish", "request"], "contact": ["contact"]}
router: {"section": "Record websites, libraries and maps", "group": "Record websites", "order": 40}
---

# Correct a Find a Grave memorial or request its management

Select the correction or management action from the memorial itself. Capture its ID and the evidence behind the proposed change before using the site workflow.

## Suggest a correction to the manager

**Privacy gate:** <!-- privacy-gate: publish --> The proposed memorial changes and any evidence included go to Find a Grave and the manager and may become public if accepted. Screen living-person details through the [privacy gate](../SKILL.md#privacy-gate) before sending.

Open **Suggest Edits** on the memorial. Fill in the affected fields and use **Save Suggestions** to send the proposed changes to the manager. Keep the proposed fact, evidence and submission status distinct from the memorial’s displayed content. [S1 @2026-11-18], [S2 @2026-11-18]

## Request management of a relative’s memorial

**Privacy gate:** <!-- privacy-gate: contact --> The requester’s relationship and reason go through Find a Grave to the memorial manager. Apply the [privacy gate](../SKILL.md#privacy-gate), including the Living people rules.

For a member-managed memorial, open **Suggest Edits** and use **Contact Manager** to request transfer, after checking the site’s transfer guidelines for the relationship. Give the relationship and reason through that route. [S1 @2026-11-18], [S3 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: request --> The account and selected memorial ID go to Find a Grave. Apply the [privacy gate](../SKILL.md#privacy-gate) before submitting.

For a non-famous memorial managed by Find a Grave itself, use **Request to Manage** from **Suggest Edits**. Keep the two routes distinct when deciding where to make the request. [S3 @2026-11-18]
