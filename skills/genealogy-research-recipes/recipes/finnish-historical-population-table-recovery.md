---
id: "finnish-historical-population-table-recovery"
title: "Find Finnish historical parish population tables"
summary: "Recover Finnish parish or municipal population tables and read the observation date, geography and population categories before comparing figures."
kind: "records"
scope: {"platforms": [], "tasks": ["Finnish official historical population statistics", "SVT VI population tables"]}
privacy: "none"
gates: []
guardrails: [{"id": "FINNISH-HISTORICAL-POPULATION-TABLE-RECOVERY-01", "text": "Use the table’s observation date for the count."}]
handoff: ["historical-place-name-resolution"]
checked: null
checked_basis: null
capabilities: {"browse": ["Statistics Finland historical statistical publications and guides"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 178}
---

# Find Finnish historical parish population tables

Use this recipe when a Finnish family history needs a historical parish or municipal population figure or a count of local demographic events.

## Choose the table by area, date and measure

Start with Statistics Finland’s *Historiallisen tilastotiedon opas*. Use the parish population and change references to find nineteenth-century tables, or use StatFin table 11re for modern municipal figures. Select the municipality and year and use the total age and sex rows for the full count. Check the table’s geographic classification against the boundary and administrative unit for the year you are using [S1 @2026-11-22], [S2 @2026-11-22], [S3 @2026-11-22], [S7 @2026-11-22].

Use the table’s observation date for the count. Keep the edition or publication date in its own field. Before appending a row to a series, compare the unit, observation date and category with the earlier row [S1], [S2], [S3].

For language figures around 1880, open the first booklet of *Suomen väkiluku 31. p:nä joulukuuta 1880* and read the headings for the geographic unit. For a comparison of parish totals for 1880 and 1890, open *Suomen väestö 31:nä p:nä Joulukuuta 1890* and read the year above the column you extract [S1], [S4], [S5].

## Check edition and subgroup coverage

For the 1865 parish figures, open Table I of *Suomen väestö joulukuun 31 p:nä 1865*. Check the denomination and date in the heading or note attached to the figure you extract. Carry the Greek Orthodox figure dated 1860 as an 1860 observation when the 1865 volume uses it [S1], [S8].

For counts in the categories used for disability in the 1880 statistics, switch to the second booklet, *Jälkimäinen vihko*. Check the locality or parish heading and keep the printed classification with the count. Use the figures as local context [S1], [S9].

## Use the change series for counts over a period

For local births, marriages or deaths over a period, search for the *väkiluvunmuutokset* publication covering those years. Consult *Yleinen katsaus väkiluvunmuutoksiin Suomessa vuonna 1890* for the separate retrospective covering 1881–1890. Record the event interval with the count [S1], [S2], [S6].

## Handoffs

- [Resolve a historical locality and jurisdiction](historical-place-name-resolution.md)
