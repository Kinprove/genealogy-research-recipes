---
id: "newspaper-finder-title-coverage"
title: "Find a digitized newspaper by title, place and issue date"
summary: "Use Newspaper Finder to discover alternate hosts for a historical newspaper and verify whether a host carries the target issue."
kind: "platform"
scope: {"platforms": ["Newspaper Finder"], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "NEWSPAPER-FINDER-TITLE-COVERAGE-01", "text": "A listed year range is a lead to the host. Confirm the target issue in the host's own holdings."}]
handoff: ["newspapers-com-search-recovery", "historical-newspaper-section-search", "local-repository-uncatalogued-holdings"]
checked: "2026-11-20"
checked_basis: "Read 2026-11-20"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Record websites, libraries and maps", "group": "Record websites", "order": 48}
---

# Find a digitized newspaper by title, place and issue date

Use this recipe when the target town or title is known and you need to find an online copy of a particular issue. A listed year range is a lead to the host. Confirm the target issue in the host's own holdings.

## Find titles by locality and year

Open Search in Newspaper Finder. Enter a start and end year and the publication country. Narrow by publication place or by title when known. Open the map pin for the locality and read the title, date range and database in each row. Inspect nearby towns' pins when they could have served the locality [S1 @2026-11-20] [S2 @2026-11-20] [S3 @2026-11-20].

## Compare hosts and confirm the issue

Compare rows for the same title and choose the hosts whose listed runs cross the event date. Check any free host among them. Follow the title to the host and inspect its issue list for the exact date. Determine whether that issue can be searched or must be browsed. Use the host's own holdings and issue access when deciding whether a subscription would help [S1 @2026-11-20] [S3 @2026-11-20].

## Handoffs

- [newspapers com search recovery](newspapers-com-search-recovery.md)
- [historical newspaper section search](historical-newspaper-section-search.md)
- [local repository uncatalogued holdings](local-repository-uncatalogued-holdings.md)
