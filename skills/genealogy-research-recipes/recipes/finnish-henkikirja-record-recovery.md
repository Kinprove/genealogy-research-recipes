---
id: "finnish-henkikirja-record-recovery"
title: "Recover Finnish henkikirja entries from provincial accounts"
summary: "Find a Finnish henkikirja by historical parish, district, year and volume signum, and distinguish index gaps from missing roll entries."
kind: "records"
scope: {"platforms": [], "tasks": ["henkikirjamikrofilmien käyttökopiot", "Suomen asutuksen yleisluettelo", "SAY"]}
privacy: "none"
gates: []
guardrails: [{"id": "FINNISH-HENKIKIRJA-RECORD-RECOVERY-01", "text": "Treat the guide’s page as the start of the district."}]
handoff: ["tax-roll-observation-workflow", "scandinavian-parish-record-recovery"]
checked: null
checked_basis: null
capabilities: {"browse": ["Finnish National Archives catalogues and historical register images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 188}
---

# Recover Finnish henkikirja entries from provincial accounts

Use this recipe for a historical Finnish household or farm when you have a place and year but lack the fiscal register entry.

## Resolve the parish to a volume and folio

In the 1634–1808 microfilm guide, use the back index to identify the parish’s district (*kihlakunta*) and then open the relevant province’s tables. For each target year, take the volume signum and starting folio from the district row. Treat the guide’s page as the start of the district. Confirm the parish heading and browse until you reach its entry. Keep the folio and digital image number in separate fields [S1], [S2], [S3].

In Astia, match the signum with its provincial accounts series, volume title and year. For Porvoon kihlakunta in 1710, use *Uudenmaan ja Hämeen läänin tilejä*, *Tositekirja* 8123 and folio 472 as the district locator. If a detail search returns no result, go back to the series and signum [S1 @2026-11-22], [S2 @2026-11-22], [S3 @2026-11-22].

For 1634, start with the bailiffs’ accounts (*voudintilit*). For 1635–1808, follow the provincial accounts (*läänintilit*) and check its voucher books (*tositekirjat*) or separately bound rolls as appropriate to the year. For later rolls, browse the province’s henkikirja series in Astia [S2 @2026-11-22].

## Check contributed finding aids against the roll

Kyläkoski reports using contributed Digihakemisto entries in 2023 to jump to property sections for selected years. Check whether the target volume has a contributed contents entry for the place. When a year or place is missing from the index, open the volume in Astia and browse the images for that year [S5].

## Check the compiled list against the original

Open *Suomen asutuksen yleisluettelo* (SAY) by parish. Read the individual volumes’ dates before ruling in or out a year. Within the volume go from village to farm, record the source indicated by the colour key, and retrieve the cited roll or other source. Prefer the colour images for decoding the key. When the volumes skip the target years, resume with the provincial accounts [S1 @2026-11-22], [S4 @2026-11-22].

## Read absences against the roll’s coverage

Check whom the roll was meant to include that year. For a village in a seventeenth-century roll, inspect the rest of the parish before treating a missing farm as an omission. Farms from the same village can appear in different parts of the parish list [S2].

## Handoffs

- [Read dated tax-roll observations and omissions](tax-roll-observation-workflow.md)
- [Reconstruct the parish household](scandinavian-parish-record-recovery.md)
