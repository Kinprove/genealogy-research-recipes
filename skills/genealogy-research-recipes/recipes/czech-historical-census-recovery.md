---
id: "czech-historical-census-recovery"
title: "Find and read historical Czech census schedules"
summary: "Find a Czech census schedule by year, historical district and house number, then interpret residence, home municipality and language in their own columns."
kind: "records"
scope: {"platforms":[],"tasks":[]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id":"CZECH-HISTORICAL-CENSUS-RECOVERY-01","text":"Check the actual census form before drawing an inference from a missing field."}]
handoff: ["austrian-confessional-register-routing","historical-place-name-resolution","archival-image-coverage-verification"]
checked: null
checked_basis: null
capabilities: {"browse":["record catalogues and original images"],"local_script":[],"extensions":[],"data_transfer":["request"],"contact":[]}
router: {"section": "Records by country and region", "group": "Central and Eastern Europe by period state", "order": 84}
---

# Find and read historical Czech census schedules

Start with the census year, current and historical locality names, and the house number if known. Check the actual census form before drawing an inference from a missing field.

## Find a surviving schedule

For 1921 and earlier, start with the state district archive route. Identify the locality's judicial or administrative district for the census year. Where a district court prepared the return, use that court's period jurisdiction to choose the district archive. Verify the municipality and year in its catalogue before looking for the household. [S1 @2026-11-22] [S2 @2026-11-22] [S7 @2026-11-22]

Lednická and Jáchimová's Telč example sends Telč-area returns to SOkA Jindřichův Hradec because the historical Telč judicial district fell under Jindřichův Hradec. If an archive assignment looks unexpected on a modern map, test it against the census-era jurisdiction. [S1]

Use [place-name resolution](historical-place-name-resolution.md) for competing Czech and German names. Search for *sčítací operáty* by locality and year, looking under the historical parent municipality for a small settlement. Use any name index as a pointer to the return. If the index is absent or misses the household, browse the town or district return by municipality, year and house number. [S1] [S12] [S13]

Use the Moravian Land Archives' [Sčítací operáty](https://www.mza.cz/scitacioperaty/) for the districts it lists, including in South Moravia, and the Land Archives in Opava's [Digitální badatelna](https://www.archives.cz/web/digitalni_badatelna/informace/) for its north Moravian and Silesian districts. Use Třeboň's [DigiArchiv](https://digi.ceskearchivy.cz/DA?lang=cs) for South Bohemia and the part of Vysočina it covers. Check the archive's listed districts for the specific locality. For the State Regional Archives in Hradec Králové, follow its [guide to the separate census search](https://soahradec.gov.cz/napoveda-archivu-online/jak-nalezt-scitaci-operat/) to locate dated returns. [S1 @2026-11-22] [S6 @2026-11-22] [S7 @2026-11-22] [S8 @2026-11-22] [S13 @2026-11-22]

For a deceased person in 1910, search MyHeritage's *1910 Czechia Census* by name, birth details and residence. Use the original schedule to check the birth date and place, who was listed in the household and their stated relationships. Continue with the archive for the specific locality and house when the index gives no hit. [S9 @2026-11-22] [S10 @2026-11-22]

When a year is missing online, check whether the responsible district archive lists the return for that municipality and whether the images cover the locality and house. The Moravian Land Archives' search guide covers missing years in its own application. Use [archival image coverage](archival-image-coverage-verification.md) when the catalogue and images leave survival or digitization open. [S2] [S12]

For Central Bohemia, check the responsible district archive's holdings for the individual year. The community walkthrough's report that SOA Praha schedules were undigitized describes November 2024. [S1] [S2]

For Pustina (Einöde) in 1900, Lednická reported an unavailable return and left both an unscanned return and a lost return possible. The linked western Bohemian return images could not be opened during the source check. Keep the gap open until the archive or its catalogue establishes coverage for that year. [S11]

## Route the 1930 return

For 1930, use the Czech National Archives in Prague. Its copy-request page also identifies a digital reading-room route for consulting a specified return. [S3 @2026-11-22]

The community walkthrough describes access by request in November 2024. Check the archive's own instructions for the access options. [S1]

**Privacy gate:** <!-- privacy-gate: request --> The Czech National Archives can receive the applicant's details and information identifying household members who may still be living. Answer the privacy gate before sending those details. [S3 @2026-11-22]

Prepare a request for a 1930 census copy only after matching the year and locality to the custodian and checking its current form. Supply the house number when established. [S3 @2026-11-22]

## Read the year’s own questions

Use the headings of the 1857 form in hand. It asked fewer questions than the first modern census in 1869 and later returns, so record an absent column separately from a blank answer. Earlier forms can give counts of sheep, pigs, goats or beehives. The published 1921 questions omit those counts. [S1] [S4] [S5]

Record *domovská obec* as the municipality where the person reportedly held *domovské právo* (right of domicile). Keep it separate from birthplace and residence, then use that municipality's home-affiliation records to test it. [S1] [S2] [S5]

Copy the wording of the column and the answer. Read *obcovací řeč* as the recorded language of everyday use. For 1921, transcribe the declared nationality and distinguish it from citizenship and the earlier language question. The 1921 census counted people present, so check residence separately. [S1] [S4] [S5] [S14]

Use the nationality entry when a surname suggests a different language. In Lednická's 1921 Pustina account, a household with a Czech surname declared German nationality. That example comes from the account, whose linked return images could not be opened during the source check. [S11]

## Read the house and household divisions

Read *čp.* as *číslo popisné*, the house number. Read each household division under that number and record the occupants, stated relationships, occupations and locator for each division. Keep an explicitly vacant division in the house record and count only occupied divisions in the occupied-household total. Lednická's 1921 Pustina account describes a vacant third division at čp. 145. The linked images could not be opened during the source check. [S11]

Check each resident's recorded occupation before assigning a job associated with a building. In the same 1921 Pustina account, Lednická found no resident listed as a forester at the forester's lodge, čp. 149. The linked images could not be opened during the source check. Report what the occupation column says and keep any further inference about who worked there open. [S11]

## Bracket a missing house sheet

Browse births and deaths for the same house number just before and after the census date. Use [Czech confessional and civil register routing](austrian-confessional-register-routing.md) to choose the register. Log the people, event dates, house numbers and register locators. Use the entries to assess probable occupancy while leaving the identities of census-date residents open. [S11]

For Pustina čp. 148, Lednická reported a 1919 death and a 1923 birth for different families at the house and found no 1921 house sheet. The linked census images could not be opened during the source check. Use the dates to bracket probable occupancy and leave the 1921 occupants unresolved. [S11]

## Return the household and coverage

Give the archive, creator or period district where established, series, locality as filed, census year, house number, household division, and page or image. Report names and column wording as written. Say whether the archive confirms that a schedule or sheet did not survive, a holding has no image you could find, the images omit part of the locality or house range, or the pages inspected contain no matching household. If coverage remains unknown, name the catalogue and page or image range you checked, then give any register evidence with its own dates and locators.
