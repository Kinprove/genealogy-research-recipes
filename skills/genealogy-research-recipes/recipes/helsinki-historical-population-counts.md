---
id: "helsinki-historical-population-counts"
title: "Interpret historical Helsinki population counts and yearbooks"
summary: "Choose the correct Helsinki census or yearbook denominator before comparing historical districts, residents, subjecthood, birthplace or other population measures."
kind: "records"
scope: {"platforms": [], "tasks": ["Helsingfors population figures", "Töölö yearbook tables", "Aluesarjat historical series", "todellinen väestö"]}
privacy: "none"
gates: []
guardrails: [{"id": "HELSINKI-HISTORICAL-POPULATION-COUNTS-01", "text": "Use the denominator printed for the population, date and area you are comparing."}]
handoff: ["helsinki-household-record-recovery", "tax-roll-observation-workflow", "historical-map-record-recovery"]
checked: null
checked_basis: null
capabilities: {"browse": ["historical city yearbooks, census reports and statistical metadata"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 239}
---

# Interpret historical Helsinki population counts and yearbooks

Use this recipe to establish the population represented by a count when explaining a historical household’s neighborhood or comparing Helsinki districts and communities. For individual names and addresses, use [Helsinki household record recovery](helsinki-household-record-recovery.md).

## Choose the source and population definition

Use the denominator printed for the population, date and area you are comparing. For historical city figures, open the Aluesarjat historical series and read its own notes with the City’s Working Papers 2016:1. Distinguish *henkikirjoitettu väestö* from counts based on church registers and from census presence. The working paper’s national-register use of *läsnäoleva väestö* refers to permanent residents, including foreign nationals, and *poissaoleva väestö* includes Finnish citizens transferred to that category on moving abroad. Apply the city table’s own definition when reading the same terms in a municipal census. [S1 @2026-11-22] [S2 @2026-11-22] [S3 @2026-11-22]

Read exemptions and inclusions against the table and year. For 1870 the published report describes omissions from the parish and poll-tax figures, including Russian troops and foreigners residing on passports. The cited Aluesarjat age series notes inclusion of foreign nationals in the poll-tax population from 1951. Treat exceptional years separately and require a note for the exact series before inferring who was counted. [S4] [S2] [S3]

Use Statistics Finland’s urban census guide for the published report or the archive of original household schedules. For an unpublished schedule, identify the enumeration district from the locality and year before choosing the folders. Check the actual delivery location and reading-room availability in the current order for the exact series before planning a visit. A 2024 account found the district list was a separately ordered item and the apparent catalogue location differed from the order location. [S5] [S6]

## Read the 1870 census categories

For 1 March 1870, use the Helsinki report’s *todellinen väestö* total, 32,113, for the whole city on census day. It includes visitors present and excludes residents temporarily away. Open Helsinki table 7, *Kaupungissa olevia epäsuomalaisia alamaisia*, for non-Finnish subjects. Calculate their share with the published total as denominator because these people are already included in it. Compare the table’s subjecthood with the report’s birthplace categories as independent classifications, and use the matching area and sex columns where relevant. [S4] [S3]

## Read the yearbook by table and observation date

Open the City’s digitized statistical yearbook for the edition needed, for example the 1910 volume. Record the observation year in each table and keep the edition or publication date in the citation. Check the table heading, district key and footnotes before comparing rows. If a topic is tabulated for the city or a combined area, keep the figures at that level and look for a separate district series. [S7 @2026-11-22] [S1 @2026-11-22] [S8 @2026-11-22]

Start a birthplace or language comparison with each table’s population basis. Keep census-day totals apart from registered population and carry unknown birthplace or distinct language categories through the comparison. For a time series, test changes in boundaries and categories before joining successive editions. The Aluesarjat age series uses presence for the 1900–1920 censuses and city residence for 1930 and 1950, so the similar-looking rows do not answer the same question. [S2] [S1] [S8]

## Return the measure and its denominator

For each figure give the publication, edition and table, reference date, geographic unit, unit counted, population basis, inclusions and exclusions. For a derived share, give the numerator, denominator and both locators. Mark an unmatched geography or changed definition before making a comparison.
