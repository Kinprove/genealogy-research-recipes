---
id: "myheritage-country-coding-place-audit"
title: "Audit a MyHeritage tree with Country Coding"
summary: "Use MyHeritage Country Coding to review uncoded locality names and modern flags that can misrepresent historical jurisdictions."
kind: "platform"
scope: {"platforms": ["MyHeritage"], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "MYHERITAGE-COUNTRY-CODING-PLACE-AUDIT-01", "text": "Use display flags as review leads. Preserve the place recorded for the event and establish the historical jurisdiction separately."}]
handoff: ["historical-place-name-resolution", "evidence-proof-judgment"]
checked: "2026-11-21"
checked_basis: "Read 2026-11-21"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["upload", "export"], "contact": []}
router: {"section": "Research method", "group": "Family trees and research planning", "order": 20}
---

# Audit a MyHeritage tree with Country Coding

Open this recipe when a place in a MyHeritage tree is uncoded or carries an unexpected flag.

## Review Country Coding

Use display flags as review leads. Preserve the place recorded for the event and establish the historical jurisdiction separately.

On the desktop site, enable Country Coding for each tree with the globe at the lower right of Family, Pedigree or Fan view. Confirm in the first-use pop-up. The setting carries over to List view. Use Fan view in Color mode to compare direct ancestral branches [S1 @2026-11-21] [S2 @2026-11-21] [S3 @2026-11-21] [S4 @2026-11-21].

Open **Settings** from the three-dot menu at the top of the Country Coding panel. Use the default birth and baptism pair for an origins audit or switch to death and burial for an end-of-life audit. Compare flags using the same event setting [S1 @2026-11-21] [S2 @2026-11-21] [S3 @2026-11-21].

Use **Current view** in the right-hand panel for counts and country assignments in the visible part of the tree [S2 @2026-11-21]. Move to another branch to refresh that list [S3 @2026-11-21]. Switch to **Entire tree** before drawing conclusions about country assignments across the tree [S2 @2026-11-21].

Click a country in the panel to list the people assigned to it for the selected events and scope [S2 @2026-11-21] [S3 @2026-11-21]. From the **Current view** list, select a name to center Family view on that person, then click their card if the details panel is closed. In Pedigree, Fan or List view, selecting the name opens the details panel [S3 @2026-11-21].

## Interpret flags

In birth mode, hover over a flag to read the place and country in the tooltip, then check which event supplied the place. Country Coding falls back to baptism or christening only when no birthplace is listed. In death mode, it falls back to burial only when no death place is listed. Attribute the place to the supplying event [S3 @2026-11-21].

A recognized modern country at the end of the place field takes precedence when assigning the flag. When the entry lacks a country, treat any assigned country flag as a present-day geolocation estimate. A Polish flag for `Danzig` reflects that estimate, so establish the jurisdiction for the event date separately [S2 @2026-11-21] [S3 @2026-11-21].

In **Settings**, select U.S. state or Canadian provincial breakdowns when auditing places at that level. Inspect the existing wording first. With U.S. state flags enabled, `Los Angeles, CA` can supply the California flag [S2 @2026-11-21] [S3 @2026-11-21].

The default United Kingdom breakdown can show St George's Cross for `London, England` and the Union Jack for `London, United Kingdom`. Check the wording behind each flag. Clear **United Kingdom** in Settings to use the Union Jack for UK places [S2 @2026-11-21] [S3 @2026-11-21].

## Audit missing and uncoded places

In birth mode, use the dashed-circle flag to spot profiles with neither a birth nor a baptism place. Enable missing-place icons in **Settings** if needed. Treat a question mark as an unmatched place. Inspect its wording for an underspecified place such as a hospital name or a historical country that the tool cannot resolve. Keep a supported historical entry even when it has no flag [S2 @2026-11-21] [S3 @2026-11-21].

Expand the missing-birthplace count at the bottom of the panel in **Current view** to open the worklist. Hover over a name and select the icon beside it to open **Edit profile**, or start from the dashed-circle flag on the profile card [S2 @2026-11-21] [S3 @2026-11-21].

Open the empty flag to check for **Suggested places** if the account has a subscription. When a Smart Match or Record Match supplies a candidate birthplace, inspect the underlying match and corroborate the birthplace before using it [S3 @2026-11-21].

**Privacy gate:** <!-- privacy-gate: upload --> A verified birthplace goes into the person's profile on MyHeritage. Identify whose place you will enter, check who can see it there, and clear the gate for anyone who may be living before entering it.

Enter a verified birthplace in **Edit profile** after clearing the gate [S2 @2026-11-21] [S3 @2026-11-21].

## Export a fan chart

**Privacy gate:** <!-- privacy-gate: export --> The fan chart can carry names, family relationships and place flags from MyHeritage to the user's device. Check who is shown, including anyone who may be living, and keep the export on that device.

With Country Coding enabled, download the fan chart from the arrow menu in Fan view's Color mode. Check the local copy for flags before relying on it as a record of the display [S3 @2026-11-21] [S4 @2026-11-21].

## Handoffs

- [historical place name resolution](historical-place-name-resolution.md)
- [evidence proof judgment](evidence-proof-judgment.md)
