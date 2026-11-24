---
id: "finnish-court-book-recovery"
title: "Recover historical Finnish court entries"
summary: "Find a Finnish district or appellate court entry through its historical jurisdiction, court-book copies, card indexes or publication registers."
kind: "records"
scope: {"platforms":[],"tasks":["Tuokko","tuomiokirjat","gifna utslag","utgifna domar"]}
privacy: "none"
gates: []
guardrails: [{"id":"FINNISH-COURT-BOOK-RECOVERY-01","text":"A full-text miss does not clear a Finnish court session. Check the court, case series and surviving copy before closing the search."}]
handoff: ["archival-image-coverage-verification","land-index-book-series-recovery"]
checked: null
checked_basis: null
capabilities: {"browse":["catalogues and public historical records"],"local_script":[],"extensions":[],"data_transfer":[],"contact":[]}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 182}
---

# Recover historical Finnish court entries

Use this recipe for a historical Finnish dispute, criminal proceeding, guardianship or registration entry. Start with the village or town, a date window, the people named and the proceeding you need.

A full-text miss does not clear a Finnish court session. Check the court, case series and surviving copy before closing the search.

For related work, use [image coverage verification](archival-image-coverage-verification.md), [land instrument retrieval](land-index-book-series-recovery.md).

## Select the court and minute series

Place the village or town in its court at the event date using the historical jurisdiction lists in Arkistojen Portti. Check exceptions for the particular village or part of a rural parish and establish when each exception applied. Search ordinary proceedings (*varsinaisasiain pöytäkirjat*) for disputes and criminal cases and registration proceedings (*ilmoitusasiain pöytäkirjat*) for matters such as title registration [S1] [S2] [S13].

For a widow arranging guardianship, include the ordinary proceedings in your search. If the minute lists minors, compare the couple’s marriage date and the children’s baptism dates with the hearing date and the period’s age of majority before treating the minute as a complete child list [S5] [S1].

Search the local court’s draft minutes (*konseptituomiokirjat* or *kantapöytäkirjat*) separately from the clean copies sent for review (*renovoidut tuomiokirjat*). For a pre-1827 gap in the clean copies for Åland, Suur-Savo or Sääksmäki, look for the local drafts. The Turku fire destroyed much of the clean-copy run for those courts [S2].

For missing southern Finnish registration proceedings before 1827, check whether the district was still operating when Turku burned and verify the actual survival of its records. Try the local draft series for the same session and case type [S13] [S2].

## Search the text and check the session

For a content search, open the National Archives’ Sisältöhaku. Enter the historical name when looking for a reference such as an occupation or burgher status, narrow by collection and year, and follow the result to the image in Astia. Compare the text hit with the image and record which collection and years the search actually covered [S11 @2026-11-23] [S12 @2026-11-23].

For a shipwreck inquiry, try the vessel’s name as the court-book search term and use the session and subject of any result to identify proceedings about the wreck [S13] [S11].

Search by the holding as well as by the people. When the locality is also the court venue, identify the references that concern the specific farm. In a boundary dispute keep the date stated for the demarcation separate from the hearing date [S3] [S4].

If the text search misses, open the draft volume for the identified session and check its judgment list (*tuomiolista*) where present. Browse the case entries in the surviving copy. Keep a missing volume, an uninspected session and an inspected session without the case as separate outcomes [S2] [S13].

## Use the Tuokko card indexes

Search Astia for *tuomiokirjakortisto* and the region, then check the catalogue unit for scan coverage. According to Kyläkoski, the regional guide flags undigitized card files, so keep those units open after an online miss [S6 @2026-11-23] [S14† @2026-11-23].

For Käkisalmi, version 2 is Zenodo record 7022629 and version 4 is record 7038077. Search `hakusanat.csv` for a subject, `ttp.csv` for a place, `tth.csv` for a member of the upper estates or `ttsl.csv` for a peasant surname. According to Kyläkoski, these are indexes to the underlying court books, so follow any surviving court-book reference to the volume [S6 @2026-11-23] [S7 @2026-11-23] [S8 @2026-11-23] [S14† @2026-11-23].

Copy the old shelfmark verbatim and use the Tuokko guide to identify the court. According to Kyläkoski, the cards retain superseded shelfmarks, so match the court, volume and page to the current catalogue [S6] [S14†].

## Use the earlier date to find a Turku appeal

For a surname lead, search the newspapers for a Court of Appeal list. Capture the court, heading, party and the date printed beside the entry. Identify the appellate case class before you choose a volume [S9] [S10].

For *gifna utslag* in the 1872 Turku run, look up the printed decision date in *Päätösten julkipanokirjat* Aha:12. Use the party and earlier date found there to browse *Päätösnide* Dbb:55 for January–June 1872 [S9].

For *utgifna domar* in the same run, take the party into *Vetoasiain diaari* Aca:46 if the publication register has no entry. Copy every labeled date and remark. Browse *Tuomionide* Dba:55 under the earlier case date when you can establish it [S9].

An early-March browse prompted by a 30-day note in the Turku docket did not locate the judgment, so keep that window and a *huutopäivä* annotation as unconfirmed locators until the name and case match in the volume [S9].

## Return packet

Return the village and historical court, case class, search window, series and copy searched, literal locator, session date and case number. Log publication, earlier docket and decision dates separately. Mark which link in the chain remains unresolved.
