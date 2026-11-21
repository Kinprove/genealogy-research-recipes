---
id: "myheritage-country-coding-place-audit"
title: "Audit a MyHeritage tree with Country Coding"
summary: "Use MyHeritage Country Coding to review uncoded locality names and modern flags that can misrepresent historical jurisdictions."
kind: "platform"
scope: {"platforms": ["MyHeritage"], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "MYHERITAGE-COUNTRY-CODING-PLACE-AUDIT-01", "text": "Use display flags as review leads. Preserve the place recorded for the event and establish the historical jurisdiction separately."}]
handoff: ["historical-place-name-resolution", "evidence-proof-judgment"]
checked: "2026-11-20"
checked_basis: "Read 2026-11-20"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Research method", "group": "Family trees and research planning", "order": 19}
---

# Audit a MyHeritage tree with Country Coding

Open this recipe when a place in a MyHeritage tree is uncoded or carries an unexpected flag.

## Review Country Coding

Use display flags as review leads. Preserve the place recorded for the event and establish the historical jurisdiction separately.

Enable Country Coding with the globe control for each tree under review. Check whether Settings use birth and baptism or death and burial before comparing flags. The flags represent modern countries and may reflect the country written in the place field or the system's geolocation [S1 @2026-11-20] [S2 @2026-11-20] [S3 @2026-11-20].

Open the right-hand Country Coding panel and review uncoded entries for missing, ambiguous or historical place strings. Where offered, switch between country grouping and subdivisions such as U.S. states or Canadian provinces and territories. Review the underlying place wording before deciding whether an edit is justified [S1 @2026-11-20] [S2 @2026-11-20] [S3 @2026-11-20].

## Handoffs

- [historical place name resolution](historical-place-name-resolution.md)
- [evidence proof judgment](evidence-proof-judgment.md)
