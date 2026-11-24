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
capabilities: {"browse": ["public catalogues, documentation and historical records"], "local_script": [], "extensions": [], "data_transfer": ["publish", "request", "link", "upload"], "contact": ["contact"]}
router: {"section": "Record websites, libraries and maps", "group": "Record websites", "order": 48}
---

# Correct a Find a Grave memorial or request its management

Select the correction or management action from the memorial itself. Capture its ID and the evidence behind the proposed change before using the site workflow.

## Suggest a correction to the manager

**Privacy gate:** <!-- privacy-gate: publish --> The proposed memorial changes and any evidence included go to Find a Grave and the manager and may become public if accepted. Screen living-person details through the [privacy gate](../SKILL.md#privacy-gate) before sending.

Open **Suggest Edits** on the memorial. Fill in the affected fields and use **Save Suggestions** to send the proposed changes to the manager. Keep the proposed fact, evidence and submission status distinct from the memorial’s displayed content. [S1 @2026-11-18], [S2 @2026-11-18]

## Check a sent suggestion

Before resubmitting, open **Suggested Edits** from **Contribute** or from the pencil icon. Choose **Suggestions I’ve Sent** and locate the edit by memorial ID under **More options**. Check its status there. [S7 @2026-11-22], [S8 @2026-11-22]

The tutorial example from the available excerpt starts at **Contribute**. [S6]

## Link existing family memorials

**Privacy gate:** <!-- privacy-gate: link --> The relatives’ memorial IDs and the asserted relationship go to Find a Grave and, for suggested edits, to the memorial manager. Saved or accepted links can be visible on both memorials. Apply the [privacy gate](../SKILL.md#privacy-gate) before saving or submitting.

For a supported parent or spouse relationship, copy the destination **Memorial ID** from its burial details. On the memorial to update, open **Edit** if you manage it or **Suggest Edits** if someone else manages it. Enter that ID in the appropriate parent or spouse field under **Family Members**. Use **Save Changes** on a memorial you manage or **Save Suggestions** to send the link to the manager. [S4 @2026-11-22], [S5 @2026-11-22], [S7 @2026-11-22]

To show children on a parent’s memorial, enter the parent’s ID on each child’s memorial. Find a Grave displays the link on the parent’s memorial once the child’s memorial links to it. A single spouse link appears on both spouses’ memorials. [S5 @2026-11-22]

## Add a document image to a memorial

**Privacy gate:** <!-- privacy-gate: upload --> The document image, any caption and the contributor’s profile name go to Find a Grave and can be visible to memorial viewers. Review the image and caption for living people’s details under the [privacy gate](../SKILL.md#privacy-gate) before uploading.

For a relevant document image you have permission to publish, open **Add Photos** on the memorial. Select the image, choose **Other** as the photo type and select **Add**. [S9 @2026-11-22], [S10 @2026-11-22]

If the image supports a correction to a field on someone else’s memorial, follow the [suggestion workflow](#suggest-a-correction-to-the-manager) for that change.

## Request management of a relative’s memorial

**Privacy gate:** <!-- privacy-gate: contact --> The requester’s relationship and reason go through Find a Grave to the memorial manager. Apply the [privacy gate](../SKILL.md#privacy-gate), including the Living people rules.

For a member-managed memorial, open **Suggest Edits** and use **Contact Manager** to request transfer, after checking the site’s transfer guidelines for the relationship. Give the relationship and reason through that route. [S1 @2026-11-18], [S3 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: request --> The account and selected memorial ID go to Find a Grave. Apply the [privacy gate](../SKILL.md#privacy-gate) before submitting.

For a non-famous memorial managed by Find a Grave itself, use **Request to Manage** from **Suggest Edits**. Keep the two routes distinct when deciding where to make the request. [S3 @2026-11-18]

## Receive transfer requests as a manager

Members can use **Contact Manager** from the memorial even when your profile has neither messaging nor a displayed email address. [S12 @2026-11-22]

**Privacy gate:** <!-- privacy-gate: publish --> Profile messaging exposes a contact button to other Find a Grave members. The optional email route sends the account holder’s chosen address to Find a Grave and displays it to profile visitors. Apply the [privacy gate](../SKILL.md#privacy-gate) before changing visibility.

To offer an additional route for transfer requests, enable **Messages** under **Account Settings → Notifications** and keep **Display my Email** off in **Edit Profile** if you want to keep the address private. If you choose to list a dedicated email address, update it under **Account Settings → Email** and turn on **Display my Email** in **Edit Profile**. [S4 @2026-11-22], [S11 @2026-11-22], [S12 @2026-11-22]
