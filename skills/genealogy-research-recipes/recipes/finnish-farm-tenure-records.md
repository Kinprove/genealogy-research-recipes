---
id: "finnish-farm-tenure-records"
title: "Reconstruct a historical Finnish farm’s tenure and transfers"
summary: "Identify a Finnish holding and reconstruct title, cultivation and transfers using farm histories, tax rolls and district court minutes."
kind: "records"
scope: {"platforms":[],"tasks":["maakirja","lainhuuto","syytinki","Suomen maatilat","Crown farm occupancy"]}
privacy: "none"
gates: []
guardrails: [{"id":"FINNISH-FARM-TENURE-RECORDS-01","text":"Identify the holding and the role attached to each name. Cultivation, residence and title are separate observations."}]
handoff: ["finnish-court-book-recovery","tax-roll-observation-workflow","scandinavian-parish-record-recovery","deed-content-relationship-clues"]
checked: null
checked_basis: null
capabilities: {"browse":["catalogues and public historical records"],"local_script":[],"extensions":[],"data_transfer":[],"contact":[]}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 236}
---

# Reconstruct a historical Finnish farm’s tenure and transfers

Use this recipe when a historical Finnish farm has several names, more than one household or a change of holder. Gather the historical village and parish, the farm’s names and numbers, and the years of the reported changes.

Identify the holding and the role attached to each name. Cultivation, residence and title are separate observations.

For related work, use [Finnish court-book recovery](finnish-court-book-recovery.md), [tax-roll observations](tax-roll-observation-workflow.md), [parish household reconstruction](scandinavian-parish-record-recovery.md), [deed relationship clues](deed-content-relationship-clues.md).

## Distinguish the holdings

Find candidate entries by village and read each farm’s account separately. When a newspaper history and Suomen maatilat use different farm labels, compare the sequence of family names in each candidate entry. Use a matching sequence to choose which holding to test in the court records [S1] [S2].

Copy the reporting or submission year from the compiled farm account. Give earlier ownership, construction and renovation dates their own fields. Preserve the stated production period and keep it separate from the reporting year [S11] [S2].

Keep separate rows for each holding in the poll-tax roll (*henkikirja*) and land register (*maakirja*). Copy the village, holding number or name, mantal share, tenure label and the role the record attaches to the person. Compare the rows before treating a second cultivator as a formally divided property [S4] [S5].

Check the named holder’s death date before using a land register to date ownership. A reported Pyhänkorva entry carries a deceased holder’s name forward. A single cultivator in the roll supplies a dated listing. Seek a lease or other instrument before assigning the entire estate to that cultivator [S10] [S4] [S5].

If the relevant communion-book pages are missing, use Iso-Iivari’s farmholder compilation to shortlist the farm, holder and possible year of arrival. Carry those leads into the tax and court series [S7] [S8].

For Crown-tax payments, look up the farm, village and use period in the National Library of Finland’s digitized receipt books. Follow the cited Digi binding number. Keep the printed year apart from the years when the book was used and leave a missing farm unresolved [S12 @2026-11-23] [S13 @2026-11-23].

## Recover the terms and dates of the transfer

Search for the farm and the outgoing owner when a search for the buyer under a later surname fails. Copy both parties as the minutes name them. Use later surnames with given names to find subsequent issues rather than backdating those surnames to the sale [S1] [S3].

In the reported Paimela example, the seller’s name led to the sale in Iitti court district, KO a:27 (1857), page 1163, where the buyers appear without their later surname [S1].

In the title registration minutes, record the sale or deed date separately from the date it was presented in court. Copy the holding and shares conveyed, the price, any relationship wording and any retained rights. For a Crown farm, check the inspection proceedings for the prior occupancy grant and any transfer document cited there [S3] [S6].

## Interpret advertisements as dated offers

Find repeat notices for the farm. If a later offer refers to an earlier listing, record its claims about the outcome as the seller’s statement on the later publication date. Keep rental and purchase clauses separate, and align the two issues by beneficiary, tax obligations, payment rate and term, and livestock upkeep [S9].

Carry the amount mentioned in each advertisement as an offered or reported amount. Use the completed-sale instrument to establish the buyer, date and price for that transfer. Read any reserved maintenance (*syytinki*) clauses for rights to buildings as well as for upkeep obligations [S9] [S3].

Transcribe the mantal share separately from field area. Keep each field-area estimate with its own measurement basis and record any explicitly excluded slash-burn cultivation (*kytö*) separately. For harvest figures, separate the amount already threshed from the expected yield still to be threshed and retain the seller’s time window and qualifications. Enter potential livestock capacity separately from the stock reported on hand [S9].

## Return packet

Return one row per holding and one per dated source observation. Label the person’s role, stated date and date type, farm identifier, exact locator and any unresolved name, subdivision, title or agreement.
