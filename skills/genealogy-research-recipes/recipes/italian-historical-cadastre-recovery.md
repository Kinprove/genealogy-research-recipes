---
id: "italian-historical-cadastre-recovery"
title: "Trace a historical Italian property through the cadastre and notarial acts"
summary: "Trace an Italian house or parcel from a named cadastral account to its map, successive holders and notarial transfers."
kind: "records"
scope: {"platforms": [], "tasks": ["catasto", "matricole dei possessori", "volture and trasporti"]}
privacy: "none"
gates: []
guardrails: [{"id": "ITALIAN-HISTORICAL-CADASTRE-RECOVERY-01", "text": "Keep the recorded holder, owner established by a deed and actual occupant as separate fields."}]
handoff: ["historical-place-name-resolution", "land-index-book-series-recovery", "historical-map-record-recovery", "italian-stato-civile-parish-record-recovery"]
checked: null
checked_basis: null
capabilities: {"browse": ["historical record catalogues and images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 196}
---

# Trace a historical Italian property through the cadastre and notarial acts

## Choose the cadastre by place and period

Start with a historical comune or cadastral municipality, an approximate year and either a named person or a property clue. Keep the recorded holder, owner established by a deed and actual occupant as separate fields.

Use the relevant State Archive’s guide to identify the cadastre and the dates it covers for that comune. Check the Teresian series in Austrian Lombardy, the Napoleonic or other predecessor cadastres where they applied, the Gregorian series in former Papal territory and the later Italian cadastre. Check which series has maps and which has only descriptions. In Latina, earlier Gregorian maps could be reused by the Italian cadastre, so match the date and series on the register and the map before joining them. [S1 @2026-11-22] [S2 @2026-11-22] [S3 @2026-11-22] [S4 @2026-11-22]

## Link a named holder or parcel to the map

From a name, use the holder’s index or matricola for that series, then follow the account or partita to the listed properties. From a known location, use the correct cadastral map and its parcel number in the corresponding parcel book. Record map sheet, parcel number, place, type of property, assessed yield where given, and the literal holder name. Match the number on the map and in the book before locating the house or field. [S1] [S2] [S3] [S4] [S5]

## Follow the parcel across transfers

Trace the parcel through the volture, trasporti or successor account. Follow changes in map sheet, parcel, ownership shares or parcel subdivisions. Preserve the cadastral change date and any separately recorded instrument date. Use the notary and act reference where stated to retrieve the instrument and determine whether the transfer was by sale, inheritance or another mechanism. [S1] [S3] [S5]

To decide whether a documented occupier owned or rented, compare separately dated evidence of occupation with the recorded holder, the underlying deed or a lease. A missing holder entry leaves tenure open. Use verified tenure and the recorded assessment as separate clues when describing economic circumstances. [S1] [S3]

Return a dated property chain with the cadastral series, folio and parcel for each entry, the map sheet, and the notarial instrument or other basis for each transfer and tenure claim.
