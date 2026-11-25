---
id: "finnish-city-census-household-recovery"
title: "Trace a household in Finland's historical city censuses"
summary: "Check whether a Finnish city was enumerated, locate surviving household forms by city and block, and interpret gaps using the census report."
kind: "records"
scope: {"platforms":[],"tasks":["Finnish city census of 1870","historical Finnish census apartment forms"]}
privacy: "none"
gates: []
guardrails: [{"id":"FINNISH-CITY-CENSUS-HOUSEHOLD-RECOVERY-01","text":"A published block total does not establish that a named household was enumerated."}]
handoff: ["finnish-astia-archival-image-recovery","scandinavian-parish-record-recovery","city-directory-observation-workflow","historical-newspaper-section-search"]
checked: null
checked_basis: null
capabilities: {"browse":["record catalogues and original images"],"local_script":[],"extensions":[],"data_transfer":[],"contact":[]}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 235}
---

# Trace a household in Finland's historical city censuses

Use this recipe to investigate a deceased household in a Finnish city covered
by the 1870–1930 city censuses. Start with a city, census year and a period address
or block.

A published block total does not establish that a named household was enumerated.

## Confirm the city and find the forms

Check Statistics Finland's city-by-year list before opening the archive. The March 1870
census covered Helsinki, Turku, Viipuri and Oulu. The city list changed in later rounds.
Use a year that covers the target city and keep the printed report separate from the
unpublished dwelling forms [S3].

In Finna or Astia find *Tilastollisen päätoimiston kaupunkien väestönlaskennat -arkisto*
under the Statistical Office. Open the city series, then identify the year and block,
property or dwelling in the unit descriptions. In Oulu, start the 1870 search with the
catalogue description for Ou:2, property cards and associated apartment cards. Confirm
the unit covers the target address and that the forms are accessible before logging it
as searched [S3 @2026-11-22] [S4 @2026-11-22] [S5 @2026-11-22].

Where the address is uncertain, build a period street and block lead through
[city directories](city-directory-observation-workflow.md). For a unit described
without a viewable image, use [Finnish archival image recovery](finnish-astia-archival-image-recovery.md).
Keep a missing catalogue unit, an unseen form and an inspected form with no
entry as separate outcomes.

## Read a Helsinki gap against the 1870 enumeration account

Open the Helsinki section of the published *Wäenlasku maaliskuussa 1870* before drawing
a conclusion from a missing entry. Where the instructions matter, use the committee's
announcements in local newspapers to check what householders were asked to report.
For someone absent from an otherwise relevant list, keep temporary departure and
evasion within the city as separate hypotheses. The report suggests departures to
nearby villages or Wiapori and describes a special police count on the evening of
28 February that supplemented some household lists. For a boarding house or other
shared address, check who supplied the entry and whether it reflects that supplementary
count [S1] [S2].

Carry each recorded status and occupation with its date, source and informant. For
example, in the report's Katajanokka account, read *ent.* as a former status and
treat traveling and selling *spitting* as self-reported. Keep a stated livelihood
separate from a verified occupation [S1] [S2].

## Return

Return the city, year, block or address, archive and unit, plus the form and page if
seen. For an unresolved household, give the exact coverage or access gap and the
next dated record to check. Use [parish registers and poll-tax rolls](scandinavian-parish-record-recovery.md)
for a parallel household chain and [newspaper section search](historical-newspaper-section-search.md)
for local reporting.
