---
id: "myheritage-gaia-research-review"
title: "Review a MyHeritage GAIA investigation and its evidence"
summary: "Check the tree GAIA is using, open the records behind its findings and approve individual MyHeritage tree changes after reviewing the evidence."
kind: "platform"
scope: {"platforms": ["MyHeritage GAIA"], "tasks": ["Research Agent and default family site", "GAIA People and Relevant sources"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "MYHERITAGE-GAIA-RESEARCH-REVIEW-01", "text": "Open and evaluate the supporting record before approving any change to a profile or relationship."}]
handoff: ["myheritage-historical-record-search", "ai-for-documentary-records", "evidence-proof-judgment"]
checked: "2026-11-22"
checked_basis: "Read 2026-11-22"
capabilities: {"browse": ["MyHeritage GAIA"], "local_script": [], "extensions": [], "data_transfer": ["publish", "third-party-tool"], "contact": []}
router: {"section": "Record websites, libraries and maps", "group": "Record websites", "order": 59}
---

# Review a MyHeritage GAIA investigation and its evidence

## Check the research context before submitting

Sign in and open Research Agent from the MyHeritage Research page. Check the default tree on the default family site, because that is the tree context GAIA’s documentation describes. If the relevant branch is in a different tree, verify the context in the user’s account before supplying any missing facts. Use Manage trees to verify the default for that site. [S1 @2026-11-22], [S2 @2026-11-22]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Submitting a question sends names, dates, places and relationships about the researched people to MyHeritage GAIA and can use details from the default tree. Answer the skill’s privacy gate before submitting anything about people who may be living.

Submit one bounded research question in Research Agent after checking the data and tree context. Include only the names, approximate dates, places, relatives and variant spellings needed for that question. Keep unconfirmed identities and relationships marked as hypotheses. [S1 @2026-11-22]

## Open the sources and work the unresolved leads

In Overview, open People to inspect each proposed person’s details, associated sources and relatives. Use Relevant sources to filter by type and, when helpful, sort by age or GAIA’s relevance confidence. Read the relevance explanation and verify what the record actually says. [S1 @2026-11-22]

Open a cited source from the response and inspect the scanned image when the source pop-up offers one. Use Review and save to your tree to reach the full record page and its arrows to navigate the sources. Hold any save until each image and identity is checked. [S1 @2026-11-22]

Treat a Lead as a locator for a manual search. Open the named repository or catalogue and check its holdings. If a source needs a separate external subscription, check access there or find another copy. A gap in GAIA’s results leaves that source unsearched. [S1 @2026-11-22]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A follow-up sends the chosen question and any added names, dates or relationships to MyHeritage GAIA. Confirm the existing gate covers that data and audience, or answer it again.

Select an in-conversation suggested search only if it tests a current hypothesis or opens a specific unsearched source. Check the suggested question before running it, and keep the result attached to the question it tests. [S1 @2026-11-22]

## Review a save or tree creation

Open and evaluate the supporting record before approving any change to a profile or relationship.

**Privacy gate:** <!-- privacy-gate: publish --> Creating or updating the online tree can send the selected people, facts, relationships and record links to MyHeritage and make them visible to the tree’s audience. Verify the destination and visibility and answer the skill’s privacy gate before authorizing the write.

Review GAIA’s proposed tree changes in Compare with your tree when offered. Save only the individually approved, verified changes. When starting without a tree, finish reviewing the connected people first and use the creation option only if offered and explicitly authorized. [S1 @2026-11-22]

Reopen edited profiles and verify the person, record link and fields actually saved in the user’s account. [S3]

Use [MyHeritage historical record search](myheritage-historical-record-search.md) for manual collection and coverage checks and [AI for documentary records](ai-for-documentary-records.md) for reviewing transcriptions and extracted claims.

See [sources and credits](../sources/myheritage-gaia-research-review.md).
