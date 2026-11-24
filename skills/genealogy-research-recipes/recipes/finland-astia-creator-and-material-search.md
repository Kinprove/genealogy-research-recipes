---
id: "finland-astia-creator-and-material-search"
title: "Find Finnish archival material in Astia by creator and record type"
summary: "Find a Finnish National Archives holding by separating the record creator from the material description and checking the resulting archive hierarchy."
kind: "platform"
scope: {"platforms": ["Astia"], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "FINLAND-ASTIA-CREATOR-AND-MATERIAL-SEARCH-01", "text": "After a material-search miss, search for the creator separately."}]
handoff: ["scandinavian-parish-record-recovery", "tax-roll-observation-workflow", "archival-image-coverage-verification"]
checked: "2026-11-22"
checked_basis: "Read 2026-11-22"
capabilities: {"browse": ["public catalogues and historical record images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Record websites, libraries and maps", "group": "Record websites", "order": 56}
---

# Find Finnish archival material in Astia by creator and record type

Open this recipe when a Finnish record citation names a creator and document type, but an Astia search fails to find the holding. For parish or tax records already identified by locality, start with [parish registers](scandinavian-parish-record-recovery.md) or [annual tax rolls](tax-roll-observation-workflow.md).

## Separate creator from material

Run the institution’s name in the actor search (*toimijahaku*) and the document or series term separately in the material search (*aineistohaku*). Once the creator is identified, try it as a restriction on the material search and apply the date range. After a material-search miss, search for the creator separately. [S2 @2026-11-22].

Open each plausible same-name actor card and inspect the linked material, including results farther down the list. Match the record group by creator, title and dates before following the hierarchy to series and unit [S4 @2026-11-22].

In Kaisa Kyläkoski’s January 2023 lookup, two cards headed *Ilmatieteen laitos* led to maps, while *Ilmatieteen laitos (1918)* led to the target archive. Recheck the linked material in your own Astia session [S1].

According to the author’s Turku example, compare the exact chapter name with every plausible result [S5†].

Use the official *Turun tuomiokapituli* guide to cross-check the fonds title and follow its Astia link [S6 @2026-11-22].

## Bring a catalogue lead back to Astia

When the combined search misses, search Finna or the web for the institution plus its archive name. Use the host archive, fonds title and dates from the result to resume the Astia search. For the Finnish Meteorological Institute case, match Finna’s *Ilmatieteen laitoksen arkisto (1880–1938)* to the target title and years in Astia [S1 @2026-11-22], [S3 @2026-11-22].

If the online hierarchy lacks the cited record series, check for a separately described archival catalogue and keep the target unresolved until its coverage has been checked [S1], [S4].

## Return packet

Return both queries, the candidate creator cards, the fonds and series locators, and which units or images you actually inspected. Record any separate catalogue to check and its stated scope.
