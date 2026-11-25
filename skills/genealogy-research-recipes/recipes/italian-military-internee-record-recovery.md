---
id: "italian-military-internee-record-recovery"
title: "Recover an Italian military internee’s captivity and death records"
summary: "Link Italian military internee records across Vatican inquiries, German camp and hospital papers, and local civil death registers."
kind: "records"
scope: {"platforms": [], "tasks": ["Inter Arma Caritas", "Stalag labour detachments", "Italian wartime captivity"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "ITALIAN-MILITARY-INTERNEE-RECORD-RECOVERY-01", "text": "Match the base camp and prisoner number together before linking spelling variants."}]
handoff: ["italian-stato-civile-parish-record-recovery", "german-register-image-recovery", "burial-evidence-packet", "evidence-proof-judgment"]
checked: null
checked_basis: null
capabilities: {"browse": ["historical record catalogues and images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 213}
---

# Recover an Italian military internee’s captivity and death records

## When to open this recipe

Use this for a documented or suspected Italian military internee in German captivity in the Second World War. Begin with a documented birth name, date and locality, a service or capture clue, and any prisoner number. Match the base camp and prisoner number together before linking spelling variants.

## Recover the captivity identifiers

Search the Vatican Information Office for prisoners of war (Inter Arma Caritas) inquiry cards by the prisoner’s name. When there is more than one card, compare the requester, historical address as recorded, camp, prisoner number, service designation and work detachment across the cards. Use any protocol number to trace the underlying correspondence. A card establishes an inquiry and the information entered on it. Read a reply or dispatch record for what the office actually communicated. [S1] [S2]

Search Arolsen for the deceased internee under the literal spellings in the Vatican and German papers. Carry differing birthplaces as recorded and test them as spelling variants or historical jurisdiction names. To link the returns, compare the Stalag designation and prisoner number as a pair and test the matching birth and death dates. Record Arbeitskommando (Arb.Kdo.) number and locality separately from the base camp and its prisoner identifier. If a card gives a different Kommando number or only a region, check both number and locality against the German detachment entry before deciding whether it is a transcription difference or a change of detachment. [S1] [S2] [S3]

Transcribe I.M.I. as Italienischer Militärinternierter when the record uses that designation, and retain Kriegsgefangener where a different document calls the same person a prisoner of war. Compare service designations across the papers. Read Sanitätssoldat as the medical-service role, and preserve Mechaniker in a profession field as a separate observation. [S1] [S3]

## Separate the hospital record from later notices

If the Arolsen file includes a Deutsches Rotes Kreuz Formblatt 5a, inspect front and reverse for the work detachment, tag, illness, relatives’ address field and burial. Distinguish the dated departure or transfer from the work detachment, admission to the military hospital and death. If a Todeszeugnis distinguishes the underlying condition from the immediate cause of death, record both fields in the order the certificate gives them. [S1] [S4]

Record the Lagerarzt death report to the Wehrmachtauskunftstelle and the Stalag’s transmission of a Personalkarte as separate administrative events. Give each its own date, sender, recipient and document identifier. If the relatives’ address is unknown on a Red Cross card, compare the camp report and war death notice for a historical address. Preserve a blank Vatican communication field as blank. Use an explicit camp statement only for whether that office notified the family. [S1] [S4]

## Recover the local registration and check for copies

Follow a war death notice to the civil register of the death locality. Search the registration year named in the notice or file, including years after the death when a later notification is documented. Give the death, notification and registration their own dates and citations. Compare differently formatted versions of a Kriegssterbefallanzeige before counting sources. In Suardi’s comparison, a handwritten Arolsen copy and a typescript held by the municipality preserved a single report. [S1] [S4]

For a Hessian death, use the state archive’s Arcinsys route to check whether a usable Standesamt duplicate covers the registration year. If the death register is absent from that route, identify the municipal archive’s death-register series and use the notice’s register reference to select the entry. [S5 @2026-11-22]

**Privacy gate:** <!-- privacy-gate: request --> The municipal archive or registrar would receive the deceased internee’s name and register locator and any requested proof that may identify living relatives. Clear the privacy gate in SKILL.md before sending.

Request the historical death entry from the archive only if consultation leaves the entry unavailable. Keep any request bearing a living person’s information as an unsent draft until the applicable access rule and permissions are confirmed.

Return a timeline from the last camp or detachment to hospital admission, death, burial and civil registration. Cite the card, docket or register entry for each event, and keep the original spellings, copy relationships and open discrepancies in the packet.
