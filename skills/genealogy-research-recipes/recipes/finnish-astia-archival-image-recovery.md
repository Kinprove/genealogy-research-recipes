---
id: "finnish-astia-archival-image-recovery"
title: "Recover a Finnish archival image through Astia and Digihakemisto"
summary: "Find a Finnish register image after an Astia miss by checking the series tree, contributor indexes and item access separately."
kind: "platform"
scope: {"platforms":["Astia","Digihakemisto"],"tasks":["repair a Finnish Digital Archive locator","find an unindexed henkikirja volume"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id":"FINNISH-ASTIA-ARCHIVAL-IMAGE-RECOVERY-01","text":"An empty search leaves the volume unresolved. Check the series, index coverage and image access separately."}]
handoff: ["archival-image-coverage-verification","scandinavian-parish-record-recovery"]
checked: "2026-11-22"
checked_basis: "read 2026-11-22"
capabilities: {"browse":["record catalogues and original images"],"local_script":[],"extensions":[],"data_transfer":["third-party-tool"],"contact":[]}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 184}
---

# Recover a Finnish archival image through Astia and Digihakemisto

Use this recipe for a known Finnish locality, court, parish, military unit or archive when
a catalogue search, contributor index or old bookmark fails to reach a historical record image.
Use public catalogue terms and deceased subjects in the open searches. Keep any living
person's details local until the privacy gate for the service has been answered.

An empty search leaves the volume unresolved. Check the series, index coverage and image access separately.

## Browse the creator and series

In Astia, open **Selaa aineistoja** and find the archive under the first letter of its
catalogue name. Use the browser's Find within that list, then open the series and the
unit for the target year. Check the unit card's description and open **Tarkastele
digitaalisena** when offered. Search the card metadata by creator, record type and
year, using the catalogue wording or a truncated stem if the exact term fails
[S1 @2026-11-22] [S2 @2026-11-22] [S3 @2026-11-22] [S8 @2026-11-22].

If a search limited to digital material misses the target, remove the digital restriction,
find the series and check the item card for a digital view. A researcher reported
recovering the digitized Narva court books in 2022 by removing this filter. Check the same
filter and item in your own session before drawing a coverage conclusion
[S3 @2026-11-22] [S4 @2026-11-22].

## Search the contributor index and browse the volumes

Use Digihakemisto's text search for a surname, place or property in the contributed page
descriptions. Search within the known archive when possible. For an estate inventory,
start with the surname in the court's archive. For a poll-tax roll, try the place or
property and collect the candidate volume locators. If the index misses, use the archive
tree and browse the volume at the village, property or street block. Check the applicable
contributor indexes for the settlement register (SAY), court books and poll-tax rolls
before turning to the volumes themselves [S3 @2026-11-22] [S4 @2026-11-22] [S5 @2026-11-22]
[S6 @2026-11-22] [S13 @2026-11-22].

For a Finnish poll-tax roll (*henkikirja*), look up the parish's period province and
district in *pitäjähakemisto* 120:1 and use the province and year to choose the series.
For a town, identify its own listing by town and year. For Swedish-period rolls, start
with *voudintilit* for 1634 or *läänintilit* for 1635–1808 [S7 @2026-11-22].

## Verify the image and repair an old link

Read the official item's contents note as well as the series and volume titles. For
Pori burials in 1768, check I C1:3 alongside the town burial listing I F1:4 because
the official description of I C1:3 lists burials for both the town and rural parishes
under a title for births and baptisms [S10 @2026-11-22] [S11 @2026-11-22] [S12 @2026-11-22].

Recover the archive, series, year and archival reference from the old citation before
building a new locator. If a Sotasampo war-diary link fails, search Astia by military
unit and the diary's dates. Open the candidate card and image, checking that the unit,
dates and reference match. A numeric suffix from the retired Digital Archive is only a
clue [S4 @2026-11-22] [S8 @2026-11-22].

## Check restricted search visibility

If Astia shows a purpose declaration after a public search, record that the public
results may omit descriptions containing personal information. A visible catalogue
description and clearance to view the record are separate findings
[S1 @2026-11-22] [S2 @2026-11-22] [S9 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Astia receives the researcher's verified identity, declared purpose and any personal search terms for this session. Check permission for anyone whose details would be sent.

Have the user complete Astia's sign-in and purpose declaration when needed for the
permitted query. Rerun it in their authorized session and check access on the
item card [S2 @2026-11-22] [S9 @2026-11-22].

## Return

Return the creator, series, unit reference, year and folio or image locator. State
which index and volume you checked and whether the image was seen. If the gap
remains, use [archival image coverage](archival-image-coverage-verification.md) to
bound it. Use [parish record recovery](scandinavian-parish-record-recovery.md) for
the household chain.
