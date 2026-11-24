---
id: "merida-badajoz-parish-household-lists"
title: "Reconstruct a household from Mérida-Badajoz parish lists"
summary: "Use ecclesiastical censuses and Easter observance lists to reconstruct Mérida-Badajoz households without turning an age label or omission into a vital event."
kind: "records"
scope: {"platforms":[],"tasks":["censo eclesiástico","estadísticas de cumplimientos pascuales","párvulo and adulto by series"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id":"MERIDA-BADAJOZ-PARISH-HOUSEHOLD-LISTS-01","text":"Treat a missing person in an Easter observance list as an unresolved residence question."}]
handoff: ["spanish-civil-parish-record-routing","hispanic-catholic-register-recovery","evidence-proof-judgment"]
checked: null
checked_basis: null
capabilities: {"browse":["record catalogues and original images"],"local_script":[],"extensions":[],"data_transfer":["request"],"contact":[]}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 210}
---

# Reconstruct a household from Mérida-Badajoz parish lists

Use this when a household in the historical archdiocese of Mérida-Badajoz needs a dated roster between baptisms, marriages or deaths. Use [Spanish record routing](spanish-civil-parish-record-routing.md) to identify the historical parish and municipal padrón. Use [Hispanic Catholic registers](hispanic-catholic-register-recovery.md) to read the sacramental entries.

## 1. Find both series by parish and year

At the Archivos Eclesiásticos de Mérida-Badajoz, check the diocesan and parish fonds separately for censuses and *estadísticas de cumplimientos pascuales*. Use the parish and year to identify which list covers the household. The archive study points to diocesan Comp.19.A, caja 9, exp.54 for a worked example of the Easter series and to parish fonds for other examples [S1 @2026-11-22], [S2 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: request --> A request for a census or Easter list sends the parish, dates and any named household members to the archive. It can identify living relatives and reveal religious observance. Answer the privacy gate in `SKILL.md` before sending it.

If the list is unavailable for inspection, request the household-list file by fonds and reference. Give the parish and year and keep the request at series or file level when names are unnecessary.

## 2. Extract the census and Easter list separately

Start a row per named person. Record the date of the list, street or household grouping, relationship, recorded age band and occupation as the entry gives them. Assign an occupation to the person it qualifies. When only the parent’s occupation is entered, leave the other occupations unrecorded [S1].

Match the age bands to the series and period before estimating a birth window. The Mérida-Badajoz ecclesiastical census examples distinguish *párvulos* aged 1–7, *infante* aged 8–14 and *adultos* aged 15 or more [S1]. In the study of Alburquerque parish deaths for 1833–1855, *párvulo* runs from birth through age seven and *adulto* begins at eight [S3]. Carry the original label into the worksheet and use a baptism or birth act when the exact age matters.

For each named person in the Easter list, copy the age band, stated relationship and any explicit confession or Communion entry. Treat a missing person in an Easter observance list as an unresolved residence question. Check the list’s stated purpose, year and parish coverage before interpreting who appears there [S1].

## 3. Resolve a household change with another series

If someone drops out between two lists, compare the corresponding municipal padrón and parish burial book, especially during a period of high mortality. Start with the last dated appearance. Keep the loss of a person from the roster open until a named death, a move or other evidence accounts for it [S1], [S3].

Return the fonds and reference for each list, a row per person and date, the literal age and observance labels, any separately documented event and the unresolved gaps.
