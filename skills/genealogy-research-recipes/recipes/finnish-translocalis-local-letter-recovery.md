---
id: "finnish-translocalis-local-letter-recovery"
title: "Recover Finnish newspaper local letters in Translocalis"
summary: "Find local letters by parish or byline in Translocalis and test the collection's coverage and author identifications against the original issues."
kind: "platform"
scope: {"platforms": ["Translocalis", "National Library of Finland Digi"], "tasks": ["paikalliskirje", "clipping keywords", "nineteenth-century Finnish correspondents"]}
privacy: "none"
gates: []
guardrails: [{"id": "FINNISH-TRANSLOCALIS-LOCAL-LETTER-RECOVERY-01", "text": "A Translocalis miss leaves the newspaper run to be searched."}]
handoff: ["historical-newspaper-section-search", "periodical-index-search-retrieval", "evidence-proof-judgment"]
checked: "2026-11-22"
checked_basis: "read 2026-11-22"
capabilities: {"browse": ["Digi clippings, article directory and historical newspaper issues", "published pseudonym indexes"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Record websites, libraries and maps", "group": "Books, periodicals and manuscripts", "order": 65}
---

# Recover Finnish newspaper local letters in Translocalis

Find local letters by parish or byline in Translocalis and test the collection's coverage and author identifications against the original issues.

## Recover the locality keyword

Start with [Translocalis](https://digi.kansalliskirjasto.fi/collections?id=742) for reader letters in digitized Finnish-language press from 1775 through 1885. If the locality is missing from keyword suggestions, look it up in the old newspaper article directory under towns, regions or parishes. Open an entry and look for its Translocalis clipping to recover the full locality keyword. Compare the directory's dated references and recurring signatures with the clipping results. [S1 @2026-11-22] [S2 @2026-11-22] [S7 @2026-11-22]

In Kyläkoski's 2023 Rautalampi search, typing the place directly after the keyword prefix missed entries tagged `translocalis_101:1860: Rautalampi` or `translocalis_102:1885: Rautalampi`. Test the complete tag, including the intervening year and space, in your own session and check both locality tags when the clipping lists them. [S3]

## Expand the clipping to the issue

A Translocalis miss leaves the newspaper run to be searched. Open the full page and scan the neighboring items. If one part of a letter is clipped, trace the other installments by title, date and issue number in the directly browsed run. Search other titles if a printed notice points to a reprint. Check the full text for genre and keep the collection label and published heading separate. The heading *Lähetetty* alone is insufficient to classify a local letter. [S1] [S4]

## Check the signature and named writer

Copy the printed signature and any identified-author metadata into separate fields. Follow a recurrent signature across issues and compare names in the printed items with the clipping descriptions. Use occupation and place metadata as leads for testing a proposed attribution. [S1] [S4] Kyläkoski's 2023 search showed the identified writer under `translocalis_105:`. Inspect a clipping's tags in your own session before using that prefix to group writers. [S3]

For a pen-named contribution, look up the signature or writer in Kallio's *Fennica-kirjallisuuden salanimiä ja nimimerkkejä vuoteen 1885*, starting from the National Library's catalogue entry. Carry the attributed signature into the clipping and newspaper text searches. [S1 @2026-11-22] [S5 @2026-11-22] [S6 @2026-11-22] [S8 @2026-11-22] [S9 @2026-11-22]

Read the work's full credit to distinguish a translator or adapter from the original author. Seek a named attribution in contributor memoirs or coverage of a court case when those leads are available. Keep the credit attached to the specific work or issue it identifies. [S5] [S9]

Verify a byline advertised for a forthcoming volume by opening its published issues. If a dated objection identifies competing use of a byline, record the objection as a claim and require issue-specific support before assigning later contributions. [S9]

## Return the issue trail

List the locality tags and byline forms searched, directory references, full issues inspected, and any unrecovered installment. For each item record the printed title, issue, page, dispatch date when given, printed signature and basis for the proposed attribution. Use [historical newspaper section search](historical-newspaper-section-search.md) for issue searches outside this collection and [evidence judgment](evidence-proof-judgment.md) to resolve conflicting attributions.
