---
id: "myheritage-photo-tag-review-and-retrieval"
title: "Retrieve and verify MyHeritage photo tags"
summary: "Find tagged MyHeritage photos, verify the identities and add supported tags by hand."
kind: "platform"
scope: {"platforms": ["MyHeritage"], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "MYHERITAGE-PHOTO-TAG-REVIEW-AND-RETRIEVAL-01", "text": "A photo tag is an attribution to verify. Add supported tags by hand."}]
handoff: ["family-photograph-attribution-and-dating", "myheritage-profile-hint-extraction", "evidence-proof-judgment"]
checked: "2026-11-22"
checked_basis: "Checked 2026-11-22"
capabilities: {"browse": ["MyHeritage family site and documentation"], "local_script": [], "extensions": [], "data_transfer": ["upload", "third-party-tool", "link"], "contact": []}
router: {"section": "Research method", "group": "Family trees and research planning", "order": 27}
---

# Retrieve and verify MyHeritage photo tags

A photo tag is an attribution to verify. Add supported tags by hand. Use [photo attribution and dating](family-photograph-attribution-and-dating.md)
to check the caption, dates and source of the identification. Keep face-recognition suggestions out of the attribution and tagging workflow.

## Prepare an authorized photo batch

**Privacy gate:** <!-- privacy-gate: upload --> Authorized family photos of the people pictured go to the selected MyHeritage family site.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> When Photo Tagger is enabled, it automatically scans new uploads for face suggestions on MyHeritage [S3 @2026-11-24]. Confirm Photo Tagger is off for the destination before uploading.

Upload a reviewed photo batch only after clearing the upload gate and confirming Photo Tagger is off.
Keep the originals, captions and provenance in the local record.

## Retrieve, verify and tag individual photos

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Opening an eligible undated image on its desktop Photo Page can trigger MyHeritage PhotoDater. Confirm PhotoDater is disabled or clear its processing gate before opening any individual photo, including an untagged upload. [S7 @2026-11-24]

On mobile, open Photos on the person’s tree profile, or use Photos → People to choose the person. On the website use My Photos → People, select the intended tree, and open the person’s tagged photos. Hover over the displayed name to locate its frame on the image. In My Photos List view use the People filter and Show photos of these people together to require every selected tag. Inspect the underlying photo before relying on the tag. [S1 @2026-11-22], [S2 @2026-11-22]

**Privacy gate:** <!-- privacy-gate: link --> A named tree profile and the selected photo become linked on the MyHeritage site. Clear the gate before applying a tag.

Apply a manual tag only to an independently supported identification. After clearing the PhotoDater gate above, open the individual photo from My Photos on desktop. On its Photo Page, choose **Tag person**, position the frame over the identified person, select the correct existing profile and choose **Done tagging** [S3 @2026-11-24], [S4 @2026-11-24]. If the correct profile is absent or the identification is uncertain, keep the proposed name in the local attribution record.

## Review photos discovered in other trees

**Privacy gate:** <!-- privacy-gate: link --> The selected image and its connection to the pictured person’s profile become visible according to the destination MyHeritage tree’s controls.

Under Discoveries, open Instant Discoveries → Photo Discoveries and compare source and destination profiles. Review each suggested image and its provenance, then add only the authorized, supported selections after clearing the gate. [S5 @2026-11-22], [S6 @2026-11-22]
