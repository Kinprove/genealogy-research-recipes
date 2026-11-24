---
id: "finnish-farm-subdivision-record-recovery"
title: "Recover Finnish farm subdivision minutes under the parent holding"
summary: "Find the survey map and minutes behind a named Finnish farm share and separate the recorded subdivision from any earlier inheritance division."
kind: "records"
scope: {"platforms": [], "tasks": ["Maanmittaushallituksen uudistusarkisto", "halkominen", "lohkominen"]}
privacy: "none"
gates: []
guardrails: [{"id": "FINNISH-FARM-SUBDIVISION-RECORD-RECOVERY-01", "text": "A missing share name in the survey index leaves the subdivision unresolved."}]
handoff: ["historical-place-name-resolution", "scandinavian-parish-record-recovery", "historical-map-record-recovery"]
checked: null
checked_basis: null
capabilities: {"browse": ["Finnish parish images and historical survey records"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 169}
---

# Recover Finnish farm subdivision minutes under the parent holding

Use this recipe when a historical Finnish source names part of a farm and you need the recorded land division and the parties it affected.

## Find the parent holding and case

Check the communion books for the share under its parent holding. Copy the share name and any manttaali figure with the page and register span. Keep the manttaali figure separate from any ownership fraction stated in a division document [S1].

In Astia, browse *Maanmittaushallituksen uudistusarkisto* → *Uudistuskartat ja -asiakirjat* by historical province, municipality and village. A missing share name in the survey index leaves the subdivision unresolved. Check the land register by village and parent holding, then browse the parent holding’s survey map and associated papers for the division minutes [S1 @2026-11-22], [S2 @2026-11-22], [S3 @2026-11-22], [S4 @2026-11-22].

Kyläkoski reports following Kokemäki to the papers for its parent holding at `A25:1/61-65 Alahonkajoki, N:o 13 Ristiluoma`, where a copy of the minutes accompanied the map [S1].

## Separate the division events

If the survey minutes recite an earlier inheritance division, extract its date, parties and fractions received or retained. Keep the recited event separate from the date, parties and parcel identifiers of the survey proceeding. Record whether you inspected a copy or the original minutes [S1], [S2], [S3].

## Handoffs

- [Resolve same-named historical places](historical-place-name-resolution.md)
- [Reconstruct the parish household by farm](scandinavian-parish-record-recovery.md)
- [Read and date the survey map](historical-map-record-recovery.md)
