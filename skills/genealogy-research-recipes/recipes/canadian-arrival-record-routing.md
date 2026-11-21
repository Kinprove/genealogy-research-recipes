---
id: "canadian-arrival-record-routing"
title: "Route an arrival in Canada by date and direction"
summary: "Choose a Canadian ocean or land arrival series by port and date, and seek substitutes before interpreting a missing entry."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "CANADIAN-ARRIVAL-RECORD-ROUTING-01", "text": "A miss in one passenger or border index leaves the arrival open."}]
handoff: ["usa-immigration-search-recovery", "canadian-census-interpretation", "canadian-provincial-record-routing"]
checked: null
checked_basis: null
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Canada, Latin America, Asia and Oceania", "order": 166}
---

# Route an arrival in Canada by date and direction

A miss in one passenger or border index leaves the arrival open. Record the date range, direction, likely port and how you established them.

## Crossing into Canada from the United States

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Ancestry receives the traveller's name or itinerary in a border-index search. Follow Living people in `SKILL.md` and answer its privacy gate before entering details that could identify a living person. When port and year suffice, browse the records with those fields.

According to the community guide, try Ancestry's Canada, Border Crossings from U.S. to Canada, 1908–1935 index when the direction is into Canada [S1† @2026-11-20] [S3 @2026-11-20]. Leave an earlier movement open. Canada's federal border entry series starts in April 1908 [S2 @2026-11-20].

Use the port and date to browse the 1908–1918 lists. For 1919–1924 use land Form 30, and for early 1925 check both Form 30 and the resumed lists. Inspect both sides of each form, including the household head's form for children. For the 1925–1935 lists follow the reel guidance when a surname search misses. Take travel in the opposite direction to the U.S. immigration recipe [S2 @2026-11-20].

## Ocean arrivals and early alternatives

Check the catalogue's port and year coverage for 1865–1935. For 1919–1922 look for a passenger list and an ocean Form 30A. Continue using the Form 30A route through 1924. Where the route went through a U.S. port, check the separate Canadian series for travellers who declared a direct onward journey to Canada [S4 @2026-11-20].

For earlier arrivals, use the named voyage, immigrant or quarantine series for the place and date. For a famine-era Irish arrival, use the early arrival guide for Grosse Île and other arrival evidence, then trace the family's first Canadian residence in census, land or local records. Keep the earliest documented residence distinct from the arrival date [S5 @2026-11-20] [S6 @2026-11-20].

## Handoffs

- [usa immigration search recovery](usa-immigration-search-recovery.md)
- [canadian census interpretation](canadian-census-interpretation.md)
- [canadian provincial record routing](canadian-provincial-record-routing.md)
