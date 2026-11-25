---
id: "finnish-prison-custody-records"
title: "Trace custody through historical Finnish prison records"
summary: "Trace a Finnish prisoner from a wanted notice or court sentence through custody, transfers and the receiving institution’s records."
kind: "records"
scope: {"platforms":[],"tasks":["vankiluettelot","kruununvankila","kehruuhuone","Prokuraattorin toimituskunta"]}
privacy: "none"
gates: []
guardrails: [{"id":"FINNISH-PRISON-CUSTODY-RECORDS-01","text":"A sentence names the punishment ordered. Follow the prison registers to establish where the prisoner actually went."}]
handoff: ["finnish-court-book-recovery","criminal-court-prison-record-recovery"]
checked: null
checked_basis: null
capabilities: {"browse":["catalogues and public historical records"],"local_script":[],"extensions":[],"data_transfer":[],"contact":[]}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 237}
---

# Trace custody through historical Finnish prison records

Use this recipe for historical Finnish notices and prison records about deceased people. Start with the date, court or institution and the name the record used at the time.

A sentence names the punishment ordered. Follow the prison registers to establish where the prisoner actually went.

For related work, use [Finnish court-book recovery](finnish-court-book-recovery.md), [criminal court and prison recovery for other jurisdictions](criminal-court-prison-record-recovery.md).

## Find the custody series for the period

For the Swedish period, search the Swedish archive by the issuing authority and prison. For the 1799–1800 Turku Castle and Häme Castle lists, carry *Justitiekanslern, Huvudarkivet* EIIIcc:261 and EIIIcc:269 into the catalogue. For each admission or release copy the date, sending official and stated reason when present [S1] [S2].

For autonomy-era Crown-prison lists, search Astia for *vankiluettelot* under *Prokuraattorin toimituskunnan arkisto*. In Eoa follow the date and the sending prison to the list that covers that institution. Then search the receiving prison’s or spinning house’s own archive for its admission [S1 @2026-11-23] [S3 @2026-11-23].

If the order specifies Lappeenranta spinning house, check its admission register by arrival window for the date and the recorded age. For the March 1873 example, the community post locates the admission in I Ba:11 [S3] [S1].

## Separate orders from movements

Use a wanted notice to locate the sentencing court and describe the escape or alleged offense as the notice reports it. Keep the penal destination as an order and follow dated prison admissions and departures to test whether it was reached. A prisoner assigned to Viapori in the reported 1799 case instead returned to Turku Castle to await another hearing [S2].

If a provincial wanted notice names a village and farm, take those locators into the communion book. Compare the name and marital status before using the preceding volume to recover the earlier household [S4].

Give pretrial admission, dispatch to court, hearing or sentence, return to custody, penal dispatch and arrival one row each. Pair each dispatch with a dated receipt or admission at the destination. Leave the departure date open if the only later date is receipt of an appellate decision [S2] [S3].

Start with the admission name even if a later report uses a different one. Read annotations beside the original entry for a recorded identification and carry both names into the next custody search [S3].

Keep a later omission separate from an earlier documented arrival. The reported Viipuri-to-Kuopio case has a March arrival and no entry found in the April list [S3].

If the person disappears from the sequence, check prison-list remarks and departures for an escape even if the newspapers yield no report. Use the date in the prison record for the escape and retain the newspaper search as a separate observation [S3] [S2].

## Return packet

Return a chain of dated entries with the prison, court and case, name as entered, source locator and role of each date. Label the expected destination and the last observed whereabouts separately. Keep a missing receiving entry or release unresolved.
