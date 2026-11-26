---
id: "uk-ireland-passenger-list-recovery"
title: "Trace a ship journey through British and Irish passenger lists"
summary: "Choose Board of Trade passenger lists for a British or Irish port call, recover missing voyage entries and distinguish transit from settlement."
kind: "records"
scope: {"platforms": [], "tasks": ["BT 26", "BT 27", "BT 32", "British and alien passenger sheets"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "UK-IRELAND-PASSENGER-LIST-RECOVERY-01", "text": "A port call is evidence for one leg of a journey."}]
handoff: ["irish-emigrant-origin-locality", "usa-immigration-search-recovery", "canadian-arrival-record-routing", "evidence-proof-judgment"]
checked: null
checked_basis: null
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Britain and Ireland", "order": 173}
---

# Trace a ship journey through British and Irish passenger lists

Use this recipe to recover an overseas ship arrival, departure or transit through a British or Irish
port. A port call is evidence for one leg of a journey. Start with the direction, date window, vessel
and ports if known.

## Contents

- Choose the list by direction and voyage
- Recover a missing list or entry
- Read the voyage and residence fields separately
- Find relatives and other companions
- Test the itinerary and report your findings
- Handoffs
- Sources

## Choose the list by direction and voyage

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A name or itinerary query sends the passenger’s historical details to MyHeritage. Apply the [privacy gate](../SKILL.md#privacy-gate) before submitting names, birth details or other information that can identify anyone who may be living. Browse by ship, port and date when those fields suffice.

Search MyHeritage’s United Kingdom and Ireland, Incoming Passenger Lists, 1878–1960 for arrivals
and its United Kingdom and Ireland, Outgoing Passenger Lists, 1890–1960 for departures
[S1 @2026-11-22]. The National Archives catalogues the Board of Trade lists as BT 26 inward and
BT 27 outward [S2 @2026-11-22] [S3 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A name query sends the passenger’s name and any entered birth or voyage details to FamilySearch. Apply the privacy gate for this destination before submitting information that can identify anyone who may be living.

Search the FamilySearch outward index as a second way to locate a BT 27 entry [S5 @2026-11-22].

## Recover a missing list or entry

Check the whole ship itinerary before logging a miss. Use BT 26 for arrivals from beyond Europe
and the Mediterranean and BT 27 for sailings whose final destination lay beyond those waters.
Check intermediate ports on a qualifying itinerary, including passengers who left outward ships
at those ports [S2] [S8].

Apply MyHeritage’s Irish-port cutoff at independence in 1922 to both collections [S1]. A miss for
an 1878–1888 inward voyage may reflect sparse survival. The Board of Trade destroyed many of those
early lists in 1900 [S1] [S2].

When a name search misses and the ship or port is known, use the port arrangement and BT 32 registers for 1906–1951 to locate a candidate list. For dates before 1908, the registers cover only Southampton, Bristol and Weymouth. Use the month before 1920 and check the sailing date where the register gives one [S2].

When the British series starts too late or the list does not survive, use the ship, port and
approximate date to check passenger records at the overseas end of the voyage. A list there may
survive independently [S4] [S6].

## Read the voyage and residence fields separately

Confirm the ship and sailing against the original list header. Use the image’s column labels to
record the vessel, departure and arrival dates, embarkation and disembarkation ports as supplied.
Copy the passenger’s name, age or birth date, occupation, marital status and residence fields where
the form gives them [S1] [S2] [S3] [S4] [S5].

Check later typed forms for a full birth date, address and marital status when those details are
missing from other records. MyHeritage’s 1957 inward example shows all three fields [S4].

Keep current or permanent residence separate from the proposed address and intended residence.
A proposed address and intended length of stay describe plans for this voyage. Look for a later
historical record showing where the passenger actually lived [S3] [S4] [S5].

For an inward list, test a visit, return or onward journey before inferring settlement. MyHeritage
describes lists filed at each U.K. stop on qualifying voyages, so an entry can record a transit
passenger [S1] [S2].

For an outward list, treat the British embarkation port as the start of the recorded leg.
Check for earlier continental travel, such as a Scandinavian passenger traveling via a British
port en route to the United States or Canada, and compare the destination country’s arrival
record [S1] [S2].

Keep the last U.K. address on an outward list separate from declared permanent residence.
MyHeritage’s 1949 and 1955 Alfred Hitchcock examples give different London hotels and separately
record his U.S. residence [S1].

## Find relatives and other companions

On an inward voyage with separate British/Commonwealth and *alien* sheets, check both for the same
ship and date when relatives or companions may have held different nationalities. In MyHeritage’s
November 1935 example, foreign-born travelers appear on a separate *alien* sheet. Treat the heading
as the officials’ classification on that list and transcribe nationality and birthplace separately
[S4] [S7].

When an occupation column gives *wife* or *child*, record the wording and compare nearby entries
and ages to identify a candidate family group. If a household member is missing, look for them on
later departures or arrivals. Allow for separate crossings several years apart [S4].

Compare names and occupations elsewhere on the list for possible work companions. Use an independent
employment record or contemporary report before assigning a professional connection [S4].

## Test the itinerary and report your findings

Compare dates, routes, occupations, addresses, stated residences and companions across repeat
sailings before linking them to the same person. Set the dated legs beside gaps in home-country
records to test whether travel or relocation could account for those gaps [S1] [S4].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A name query sends the passenger’s name and any age or voyage details entered to the service hosting the destination passenger index or census. Apply the [privacy gate](../SKILL.md#privacy-gate) before entering identifying details about anyone who may be living. Browse by place, ship or date when those fields suffice.

Search the destination’s arrival records and next relevant census using the stated destination as a
lead. Search contemporary newspapers by ship and sailing date for evidence of the trip’s purpose
[S4] [S6].

Report each leg’s direction, vessel, date, ports, archive series and page or image locator. Include
the literal field labels, stated travel plans, candidate companions and any missing sheets or
voyages. Record which lists you checked and which gaps reflect coverage or survival. Leave
identity, residence or travel purpose open where corroboration is missing [S1] [S2] [S4] [S6].

## Handoffs

- [Irish emigrant origin locality](irish-emigrant-origin-locality.md)
- [U.S. immigration records](usa-immigration-search-recovery.md)
- [Canadian arrivals](canadian-arrival-record-routing.md)
- [Evidence judgment for identity conflicts](evidence-proof-judgment.md)

## Sources

[Source bibliography and credits](https://github.com/Kinprove/genealogy-research-recipes/blob/2b4157d8449d36b2a0e62fb1f75fe9f581deb15a/skills/genealogy-research-recipes/sources/uk-ireland-passenger-list-recovery.md).
