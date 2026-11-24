---
id: "usa-immigration-search-recovery"
title: "Recover U.S. immigration and naturalization records"
summary: "Trace U.S. immigration and naturalization by sea, air or land border, and read manifests, verification marks and federal files."
kind: "records"
scope: {"platforms": [], "tasks": ["ship and aircraft passenger lists, Canada/Mexico crossing records, naturalization minute books, C-files, A-files and AR-2 records."]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "USA-IMMIGRATION-SEARCH-RECOVERY-01", "text": "The recurring mistake is treating a search miss as a missing ancestor when the failure lies in the selected port, date, recorded name, image, citizenship history or custodian."}]
handoff: ["land-index-book-series-recovery", "russian-empire-jewish-identity-attribution"]
checked: "2026-10-26"
checked_basis: "checked 26 October 2026"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request", "third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "United States: people, vital and church records", "order": 194}
---

# Recover U.S. immigration and naturalization records

## Contents

- Goal
- Recovery workflows
- Prompt-craft

## Goal

Recover the record behind a failed name-and-year search. The recurring mistake
is treating a search miss as a missing ancestor when the failure lies in the
selected port, date, recorded name, image, citizenship history or custodian.
Immigration and naturalization are separate events and produce different
records.[3]

This recipe complements `russian-empire-emigrant-origin-recovery`: use that skill
to reconstruct the origin locality, scripts and Eastern European archive
jurisdiction. Here, recover the U.S. arrival and citizenship record packet.
For vendor controls, use the Ancestry or MyHeritage search-recovery recipes;
for an identity conclusion, use `evidence-proof-judgment`.

Keep three small working sheets:

- **Journey table:** record date, event date, original name, supported travel mode,
  departure, arrival, destination, companions, citizenship/traveler category and locator.
- **Coverage table:** repository, collection/series, mode, port/airport or district,
  dates, traveler categories, index versus images, access and gaps.
- **Recovery queue:** failed query or image, proposed repair, exact locator,
  result and next stopping condition.

## Recovery workflows

### 1. Replace one immigration year with a journey sequence

**Trigger:** censuses disagree, a family story supplies one year, or a later
arrival is being treated as the first arrival.

1. Transcribe immigration and citizenship entries from each available census
   image separately; keep their record dates and reported values. Do not average
   them into a new year.[5]
2. Add naturalization arrival statements, dated residences, border entries and
   other documented trips. Separate departure, U.S. arrival and residence.
3. Search distinct arrival windows, including a return trip where the evidence
   permits it. An AR-2 form can distinguish first arrival from most recent
   arrival; extract both fields when present.

**Output:** competing journey rows with a search window for each. **Check:**
every window states which record supports it. Stop treating the years as a
contradiction once they demonstrably describe different journeys.
[NARA AR-2 guide](https://www.archives.gov/research/immigration/alien-registration-ar-2)

Read the reported immigration year in each available 1900, 1910, 1920 and 1930
U.S. population schedule. Carry the birthplace and an estimated birth year into
the passenger search. In 1920, also copy any reported year of naturalization
into the court-search table. Use the voyage date on the identified manifest for
that journey and keep the census answers as separate reports. [N73] [N152] [N156] [N165]

If dated births place the same household first abroad and then in the United
States, search the interval between them first. Verify whose location each
record fixes before using it to bound another family member's arrival. Keep
separate arrivals and return trips open. [N156] [N157]

Treat the ship and arrival date on an AR-2 as the registrant's own statement, not a verified
locator. Record them as an attributed journey claim, and confirm that the named ship made that
voyage and that the person appears on its manifest before treating it as an established journey.
If the claim conflicts with a manifest already found, record the conflict rather than inventing a
second trip. One AR-2 gave 4 July 1910 for a New York arrival; the named ship made no such voyage, while the passenger had been found on a manifest for 20 June 1907 [N13].

When an immigrant-community church admission or transfer entry names a previous parish,
retain that literal field, date and locator as a separate journey clue. It may identify a
transit or port parish rather than birthplace. Compare independent birthplace evidence and
collateral relatives' stated localities before choosing a natal family. The
[Scandinavian-immigrant example](https://familylocket.com/rlp-202-researching-scandinavian-immigrants-with-jenny-hansen/)
motivates this place-role check without guaranteeing a field or identifying the family.

For a return leg through Britain, search British inbound passenger lists and verify their route and
year coverage before recording a gap; a missing list is not evidence the person stayed. In the
[return-voyage discussion](https://forum.ahnenforschung.net/forum/thread/185403/),
a forum participant states this for an interwar return without citing a source. It does not
establish coverage by year or route, or what records the home locality kept, so check the finding
aid of the collection you choose.

### 2. Diagnose the collection before expanding the query

**Trigger:** a New York or Ellis Island search fails, or a portal's name is
being used as proof of arrival place.

1. Read the selected collection's description. Record its actual ports or airports,
   dates, series and traveler categories in the coverage table.
2. Rank other entry points from evidence: destination, a documented ship,
   relatives' routes, a citizenship file or a border entry. Residence in New
   York does not establish arrival there.[1,5]
3. Search the matching port/series directly. If the relevant period has
   incomplete passenger records, choose another record type rather than
   repeating an unsupported exact-name search.

Before 1 January 1820 there was no federal rule requiring shipmasters to submit passenger
lists. [N88] For earlier arrivals, start with published passenger-list compilations and
surviving port series such as Philadelphia (1800–1819) and New Orleans (1813–1819).
Allow for a list never having been created. Venezia raises that possibility
in his advice from the available excerpt. [N87] [N88]

Use Filby’s *Passenger and Immigration Lists Index* as a finding aid for early arrivals.
Copy its source code and page number and retrieve the cited record. Its dates
and places can come from a naturalization or another record, so establish the
event type before adding an arrival to the journey table. [N167] [N168] [N146]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A Boston index query sends the passenger's name and any birth, residence or travel details entered to MyHeritage. Apply the privacy gate in `SKILL.md` first.

For Boston arrivals in 1848–1891, search the [MyHeritage Boston manifest index](https://www.myheritage.com/research/collection-20681/massachusetts-boston-passenger-manifests-1848-1891).
Use its ship and arrival date to locate the original list. Keep any indexed age, birthplace,
residence and destination as leads until you read the corresponding fields on the image.
[N89 @2026-11-18] [N90 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A regional passenger or crew query sends the traveler's name and any entered birth or voyage details to MyHeritage. Apply the privacy gate in `SKILL.md` first.

For a ship lead at Fall River, New London or a listed Rhode Island port, search MyHeritage's
[New England passenger and crew collection](https://www.myheritage.com/research/collection-20348/new-england-passenger-crew-lists).
Record the ship and arrival date from the index, then check the image for the
recorded birthplace and departure. Check coverage by port and series before
using the site's 1829–1957 label to interpret a miss. The archive dates A3468
to August 1918–November 1954 and lists later series separately.
[N149 @2026-11-21] [N150 @2026-11-21] [N108 @2026-11-21]

For a Wilmington or Morehead City ship lead in 1908–1958, search MyHeritage's
North Carolina, Passenger and Crew Lists from its [collection guide](https://www.myheritage.com/wiki/North_Carolina_passenger_lists_index).
Use the ship and arrival date to match the indexed entry to the manifest, then
read the birth and departure fields there. If the site query misses, use the
archive's port listing to locate the 1908–1958 series by port and date.
[N149 @2026-11-21] [N151 @2026-11-21] [N108 @2026-11-21]

Use MyHeritage’s Louisiana, New Orleans, Passenger Lists for a New Orleans ship
lead in 1901–1960. Match the index hit to the manifest by ship and arrival date,
then copy the recorded embarkation and any birthplace or named relatives.
Keep New Orleans in the arrival-port field and copy the stated final destination
separately. [N186 @2026-11-22] [N187 @2026-11-22]

Use MyHeritage’s California, San Diego Passenger Lists (20779) for a San Diego
arrival from 1904. Match the ship and arrival details to the manifest, then
check any indexed birth details against the image. When the viewer presents a
joined manifest, inspect both halves and match the line across them. [N188 @2026-11-22] [N189 @2026-11-22]

If the evidence supports a flight, search the airport's passenger-arrival series,
not only ship lists for the nearest seaport. Keep any supplied airport, airline
and flight details with the date and traveler category. NARA lists airplane and
vessel series separately, sometimes with different date ranges and indexes;
check the selected series' description and access before inspecting its manifest.
A ship-list miss does not test the airplane series. The Cuban-research article
names plane manifests as a possible hometown source; it establishes neither a
particular person's route nor that a manifest supplies a birthplace.[33,34]

For a late-1950s or early-1960s New York flight, check A3998 for arrivals from
1 December 1957 and A3665 for passenger manifests from 1 May 1959. A3665
includes departures too, so confirm the direction on the document. [N108 @2026-11-22] Copy
the route and date from the form. If the image shows only an aircraft itinerary,
crew list or health declaration, find a passenger row before identifying the
traveler as a passenger. [N178 @2026-11-22]

**Output:** a coverage-backed route shortlist. **Check:** a negative result
applies only to the searched series and window. The Foundation's current
Arrival Records Collection includes entry points beyond New York; check the
selected series rather than copying old New-York-only coverage claims.
[Foundation collection guide](https://www.statueofliberty.org/discover/heritagesearch/)

For a New York arrival, set the station from the arrival date before you name it or choose a
station-named index. From 1820 ship captains gave passenger lists to customs officials.[N61]
Before 1855 there was no immigration station, and the lists were collected at whatever pier the
ship docked.[N62] Castle Garden was the port's immigration station from 1855 to 1890. The Barge
Office in the Battery was used while Ellis Island was built, and Ellis Island received
immigrants from 1 January 1892. After the June 1897 fire the Barge Office was used again until
the new main building opened on 17 December 1900.[N63] Do not write "came through Ellis Island"
for an arrival before 1892 or between June 1897 and December 1900. Do not report a list for an
arrival before June 1897 as lost in the fire: the fire burned the immigration manifests for those
entries, but the customs lists remain.[N63]

For a New York arrival near the station handover, use 3 August 1855 as Castle
Garden's opening date and 19 April 1890 as the start of federal processing at the
Barge Office. Check the arrival and inspection dates separately if they straddle
the change. Keep the New York passenger-list search open across the handover.
[N152] [N153] [N154]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A broad New York passenger or crew query sends the traveler's name and any entered birth or voyage details to MyHeritage. Apply the privacy gate in `SKILL.md` first.

Search MyHeritage's [Ellis Island and Other New York Passenger Lists, 1820–1957](https://www.myheritage.com/research/collection-10512/ellis-island-other-new-york-passenger-lists-1820-1957)
for New York arrivals across the Castle Garden, Barge Office and Ellis Island
eras. The collection draws on M237 and T715. Save the ship, arrival date and
numbered line from the manifest. [N166 @2026-11-21] Use the collection dates to
choose where to search and the station chronology to describe the arrival.
[N152 @2026-11-21] [N155 @2026-11-21]

For a Swedish migrant with a lead through Britain, test Liverpool as the
Atlantic embarkation port. If that lead fails, broaden the search without an
embarkation constraint. Keep the Swedish departure port and Atlantic
embarkation in separate journey fields. [N152] [N158]

For early New York customs lists, look first for the name, age, origin and any occupation
in the columns actually provided. Expect fewer details than on later immigration forms.
Kathryn Marks points to that difference in her advice from the available excerpt. [N91]
Use the form heading and date to judge whether a missing detail was ever asked. [N92]

For a New York arrival, record the port and leave the inspection site open until a
source identifies it. This follows Marks's advice from the available excerpt. [N91]
Most arrivals after mid-1924 did not go to Ellis Island. If the question is whether
someone went ashore there, look for a detention or other record that places them on
the island. [N92]

If the person may have worked aboard a ship, check the crew schedule for the known
voyage. Looking for crew manifests is part of Marks's advice from the available excerpt. [N91]
For New York vessel arrivals in 1897–1957, use the T715 ship and date locator to find
the crew list. Keep employment aboard separate from immigrant passenger status. [N94]

For nineteenth-century arrivals that fit the Balch Institute's passenger data,
check the Russian, German, Italian or New York Irish Famine series in NARA's
[electronic-records guide](https://www.archives.gov/research/genealogy/electronic-records).
[N102 @2026-11-18] Reuse the manifest ID to match the passenger and vessel files and
retrieve the original by ship, port and date. Series labels do not restrict every
passenger to the named nationality [N103 @2026-11-18]. The account from the available excerpt identifies all four series [N101 @2026-11-18].

Use the port encoded in the Balch manifest ID to choose the arrival series.
Read the ship, departure port and arrival date in the linked header and use
them with the decoded arrival port to retrieve the original list. [N103]
The Just Genealogy example from the available excerpt illustrates the
passenger-to-header lookup. [N183]

For an 1846–1851 New York lead, check the Irish Famine series even if the
traveler's origin was elsewhere. Use the dates listed for each of the German,
Italian and Russian series when searching those files. The Irish Famine window
applies to that series. [N152] [N102]

For a Spanish cigar worker who settled in Tampa around the turn of the twentieth
century, include sailings from Cuba when browsing the Tampa arrival lists (M1844).
Use the recorded embarkation port to test for a separate Spain-to-Cuba leg.
[N135] [N136] [N108]

For a Spanish immigrant linked to a Hawaiʻi sugar plantation, start with the
1907–1913 window in the Honolulu vessel manifests (A3422 or A4156).
For the 1907 S.S. Heliopolis sailing from Málaga, use the separate Hawaiʻi State
Archives passenger index and MFL 50, reel 17. For other sailings, use the
ship and date to browse; the state archive's general 1900–1921 index is to ships.
[N135] [N137] [N108]

For a Chinese traveler under the exclusion laws, a passenger-list search is not the only arrival
route. Check the exclusion registers kept at the port of entry for the recorded status category
(for example laborer, merchant or son of a native) and the admission result. Then look for the
person's exclusion or immigration case file. These files can include departure statements,
photographs, signatures, letters and witness interview transcripts. Treat status claims and
testimony as statements made to win admission, not as independent proof of kinship. The
[My China Roots demonstration](https://www.youtube.com/watch?v=x5P9fKp25lw) shows these record
types through one vendor's images. Confirm the custodian and the file locator separately.

For a San Francisco arrival, require a record that places the traveler at
Angel Island before naming the station. In late 1940, look for the inspection
site and any detention or transfer date in the case file. The administration
building burned on 12 August 1940 and the station moved to mainland San Francisco
on 5 November. A detainee's file can span both sites. [N169] [N170]

For a Chinese arrival at San Francisco, use M1414 (1882–1914) to check the
separate Chinese passenger lists and M1476 (1903–1947) for the admission or
denial in the indexed registers. For a returning Chinese laborer in 1882–1888,
use M1413 to connect the recorded departure and return ships and dates and to
look for the stated original arrival. [N169] [N171]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A Chinese arrival index query sends the traveler's name and any entered birth or arrival details to Ancestry. Apply the privacy gate in `SKILL.md` first.

For the San Francisco arrival lead from the available excerpt, search Ancestry's Chinese Arrival Case Files Index (1884–1940). [N120 @2026-11-20]
Record the indexed name, age, gender, birth date and place, arrival date and ship
where supplied. Save the case and box numbers for the corresponding San Francisco
investigation file, NAID 296445 (1884–1944). The index dates extend beyond Angel
Island's 1910–1940 station years. [N121 @2026-11-20] [N122 @2026-11-20]

**Privacy gate:** <!-- privacy-gate: request --> An arrival case-file request sends the traveler's name and case locator to NARA at San Francisco. Apply the privacy gate in `SKILL.md` first.

Request the original investigation file by case number from NARA at San Francisco
in San Bruno. If the index misses, use the San Francisco vessel manifest M1410
to reconstruct the case locator from the ship's arrival number and the ticket
number or, after 1910, the manifest page and line. [N121 @2026-11-20] [N122 @2026-11-20]

For a return through San Francisco, rebuild the case locator from that
arrival’s manifest and retain it beside the earlier locator. [N169] If the
arrival leads to a file gap, check the series for the most recent port or the
INS office near the last documented residence for a consolidated case. [N172]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A Riverside catalog query sends the traveler’s name and any entered travel details to NARA. Apply the privacy gate in `SKILL.md` first.

Search the Riverside series in the NARA Catalog for a Chinese exclusion case
with a Los Angeles, Calexico, Nogales or San Diego office lead. Use the office
series and retain its case locator. [N172 @2026-11-22] The digitization project covers a
subset, so keep the underlying office series in the recovery queue after an
online miss. [N185 @2026-11-22] The Genealogy Gems discussion
from the available excerpt points to this release. [N184 @2026-11-22]

### 3. Recover the recorded name without inventing a renaming event

**Trigger:** the U.S. name is absent from the arrival index.

1. Build a compact variant list from earlier records, original-language given
   names, initials and recognizable handwriting alternatives. Routine renaming
   by Ellis Island inspectors is a misleading search premise.[8]
2. Remove the first name or exact-age restriction; test one variant at a time.
   Add one discriminating attribute such as companion, residence or ship.[10]
3. Search an accompanying child or spouse when the adult's entry remains
   elusive, then read the surrounding party in the image.[7]

**Output:** a query ladder and candidate manifest rows. **Check:** preserve the
indexed spelling and the image reading separately. A spelling resemblance
retrieves a candidate; companions and destination details must connect it to
the researched person.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A Foundation search sends the passenger's name and any birth, residence or arrival details entered to the Statue of Liberty & Ellis Island Foundation. Apply the privacy gate in `SKILL.md` first.

In the Foundation's [Arrival Search](https://www.statueofliberty.org/arrival-search/),
start with the surname and leave Exact Match off when the spelling is uncertain.
If the results are crowded, add Arrival Location or one supported field under
Advanced Search. Use a range around an estimated Birth Year or Arrival Year.
Keep Last Residence separate from birthplace. [N93 @2026-11-18]
Marks's advice from the available excerpt is to narrow crowded results with
known details and allow a couple of years on either side. [N91 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A One-Step query sends the passenger's and any companion's names and the town or voyage details entered to Stephen P. Morse's One-Step tool. Apply the privacy gate in `SKILL.md` first.

If the Ellis Island name search is empty and the town is known, try the One-Step enhanced Ellis Island form.
Search by Town Name with the surname blank, then narrow a crowded result by
First Name of Companion or another supported attribute. Confirm which place
the original manifest field records. [N113 @2026-11-20] [N114 @2026-11-20]

If you need to choose a One-Step tool, open Morse's [About this Website and how to use it guide](https://stevemorse.org/onestep/onestep3.htm).
Use the Ellis Island section to choose a passenger-name search, a ship-arrival
search or a direct lookup by roll and frame, according to the locator you have.
[N147 @2026-11-21] [N148 @2026-11-21]

When building the query ladder, give children traveling with an Italian mother
variants under both her birth surname and the father's surname. For a Jewish
emigrant, include Yiddish forms of the given
name when the person's records or family context support them. For earlier
New York lists, include an abbreviated given name such as `Wm` for William.
For a married woman, include her husband's surname on its own and inspect
candidate entries headed `Mrs.` These variants come from the available excerpt
of Marks's interview and from Cooke's interview notes. [N91] [N98] Use the
surrounding rows and independent records to confirm the person and relationship.

In the Statue of Liberty–Ellis Island database, the
[Genealogy Gems interview](https://www.youtube.com/watch?v=4xyd2c5Cv1Q) recommends not using the
search filters for arrivals outside 1892–1924. It says many post-1924 records were added later,
indexed only by year with a 1 January placeholder date, so a month-and-day search returns
nothing. Never record an indexed 1 January as the arrival date until the manifest image confirms
it. An empty exact-date search does not show absence. This describes the indexing in 2023;
re-check current behaviour.

When the U.S. surname differs from earlier records, look for a record that states the change.
Naturalization papers can ask what name the applicant will use, a pension file may give an
alias, a passport application may explain a difference from the father's name, and courts or
newspapers may record a legal change. Log each earlier name with its source and date. Allow for
parallel use too: a congregation's register may keep the birth name while newspapers or work
records use an anglicized form. For Italian emigrants, also search a married woman under her
birth surname. Children listed beside an adult with another surname may be travelling with their
mother. [Castillo's talk](https://www.youtube.com/watch?v=qDW8dEp5mN0),
[Lisson's discussion](https://www.youtube.com/watch?v=dcx-iIn1TzE) and the
[Italian-records discussion](https://www.youtube.com/watch?v=UC1J5HuNYns) motivate these checks.
They do not show that a given file states a change or how a clerk recorded a surname, so confirm
relationships from other records.

### 4. Split a Canadian or Mexican route into its actual legs

**Trigger:** an ancestor is present in the U.S. but no plausible U.S. sea
arrival appears, or records mention Canada or Mexico.

1. Search the possible arrival into the neighboring country separately from
   the subsequent U.S. land entry. Do not force both events into one year.
2. Check U.S. border series for the crossing period and traveler category,
   including people whose nationality differs from the neighboring country.[N9]
3. Read the recorded crossing station and destination. The St. Albans district
   collection name does not establish a crossing at St. Albans, Vermont.[N40] Open
   the card's reverse or second page: it can record a medical examination, the
   admission decision with its reason, and where the person left the United
   States. Add that exit as its own journey row.[N9]
4. For a double surname, search each component and the combined form; preserve
   the actual image spelling. Tabulate repeated crossings as separate events.[N9]

**Output:** a linked route with documented and missing legs. **Check:** each leg
has its own locator; an unavailable early series is a coverage gap.
[NARA series by port of entry](https://www.archives.gov/research/immigration/ports),
[Mexican border crossing series and coverage](https://www.archives.gov/research/immigration/border-mexico),
[Canadian-border district explanation](https://www.archives.gov/publications/prologue/2000/fall/us-canada-immigration-records-1.html)

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A Canadian route index query sends the traveler's name and any entered birth, residence or journey details to the selected provider, FamilySearch or Ancestry. Apply the privacy gate in `SKILL.md` first.

For a crossing station lead, use the Canada-to-U.S. indexes on FamilySearch and Ancestry
(collection 1803785, labelled 1895–1956, and collection 1075, labelled 1895–1960).
Use the Research Wiki series table on the FamilySearch collection page to choose
the microfilm and determine whether a second manifest is expected. For the
St. Albans district, use FamilySearch collection 2185163 (1895–1954), which
includes Soundex indexes M1461 and M1463 and manifests M1464 and M1465.
Read the crossing station on the card or manifest. [N109 @2026-11-20] [N110 @2026-11-20]
A record filed under St. Albans places the crossing at Sault Ste-Marie,
Michigan, in the example from the available excerpt. [N107 @2026-11-20]

For a Detroit lead from the available excerpt, search Ancestry's Detroit border crossing and passenger collection (1070). [N107 @2026-11-20]
Use the record type and year to choose the series. For example, NARA lists
Detroit entry cards as M1478 (1906–1954), vessel passenger and alien crew
lists as M1479 (1946–1957), and a later vessel and airplane series as A3728
(1957–1981). Use each series' own span when judging a miss. [N111 @2026-11-20] [N108 @2026-11-20]

For the Canadian seaport lead from the available excerpt, search Ancestry's U.S.-bound vessel collection
(60501) for passenger and crew entries in 1912–1939 or 1953–1962. [N107 @2026-11-20]
Use the port and vessel to retrieve that arrival leg, then check for a separate
U.S. land entry. [N112 @2026-11-20] [N108 @2026-11-20]

On a land-border form, copy any prior U.S. visits, companions and named contacts
at either end as separate clues. Treat the recorded relationship as a lead.
On Form 1-Canada, use the earlier Canadian port, date and ship to retrieve
the overseas leg. For someone whose destination at that time was Canada,
browse the Canadian passenger list even if the U.S. list made at the Canadian
seaport omits the traveler. [N132] [N134]

On the Canadian side, Library and Archives Canada staff said in a
[2017 interview](https://www.youtube.com/watch?v=Dqa7RGnfDOk) that no Canadian government
border-entry records exist before 1908, and that Canada recorded entries, not departures. Treat
this as the speakers' description: unless a repository finding aid shows otherwise, do not expect
pre-1908 Canadian land-border lists, and do not treat a missing Canadian exit record as negative
evidence. Census and city-directory entries can bracket otherwise undocumented
crossings. Verify current LAC coverage. Before treating an early Canadian arrival list as a full
roster, check which passengers it itemizes. Some earlier lists left out personal details for
wives, minor children, labourer groups and cabin passengers, so a spouse or child who seems to
be missing stays an open question. The
[Scottish-migration lecture](https://www.youtube.com/watch?v=aZgUeKOaLtY) does not identify which
years or ports are affected.

A crossing record from Canada is not by itself an immigration event. MyHeritage's guide to its
*United States, Border Crossings from Canada, 1895–1956* collection says it also records American
citizens visiting Canada, tourists and people on work trips,[N64 @2026-11-12] and the collection's
2021 release notice says many of its records concern U.S. or Canadian citizens crossing for work
or travel.[N65 @2026-11-12] Search it for an ancestor who never emigrated as well. Read the
recorded citizenship, residence and destination before adding a migration row, and log a return
from a visit as a trip in the journey table.

For a Mexican crossing, keep the provider's date range separate from the underlying port
series. FamilySearch labels its index *United States, Border Crossings from Mexico to United
States, 1903–1957*; it includes aliens and citizens at various ports, not every crossing.
For a year outside that span, return to the port-series coverage and another provider rather
than extending the index's negative result. [N68 @2026-11-16] [N69 @2026-11-16]

For a Canadian route before 1895, do not expect a U.S. Canadian-border entry from the St. Albans
series described by NARA. Search the arrival into Canada and dated residence evidence instead;
a Canadian ship arrival and the later land crossing remain separate events. [N70], [N71]

### 5. Recover an arrival through the departure list

**Trigger:** the arrival transcription is confusing, or the departure port
and sailing are known.

1. Locate the departure collection and any separate handwritten index.
   Search surname alone if the full-name query fails.
2. Compare departure and arrival images using sailing, age, party members
   and destination; differences become questions to resolve.
3. Distinguish the passenger's intended final destination from the ship's
   arrival port and intermediate calls. Preserve those fields separately.[7]

**Output:** a paired departure/arrival extract with unresolved differences.
**Check:** confirm the same person and journey before combining the entries.
Two websites reproducing one manifest are alternate access paths to that
record, not two independent attestations.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A British outward-list query sends the passenger’s name and any entered residence or voyage details to FamilySearch. Apply the privacy gate in `SKILL.md` first.

If a U.S. arrival search stalls and the route may have crossed Britain,
test the Atlantic leg from Liverpool even for a traveler with a non-British
nationality. Treat a Hull lead as a possible transfer into Britain. [N176 @2026-11-22]
For an 1890–1960 lead, search the BT 27 outward passenger lists through
FamilySearch’s *United Kingdom, Outgoing Passenger Lists*. Keep the original
embarkation leg separate from the Atlantic sailing you recover. [N177 @2026-11-22]

For a Swedish arrival in 1820–1850, look up Nils William Olsson and Erik Wikén's
*Swedish Passenger Arrivals in the United States, 1820–1850* through the
[Library of Congress passenger-list guide](https://guides.loc.gov/nordic-scandinavian-emigration/passenger-lists).
Use the U.S.-wide volume when the port is unknown. Follow any listed ship and
date back to the original list. [N145 @2026-11-21] [N146 @2026-11-21]

Departure lists survive unevenly. Choose the series from the manifest's port of
embarkation and record that series' surviving span in the coverage table before
searching:

- **Hamburg:** the Staatsarchiv Hamburg holds 555 volumes of emigrant lists,
  1850–1934, also searchable on Ancestry.[49]
- **Bremen:** most original lists were destroyed. About 3,000 survive for
  1920–1939, and copies made for statistics survive for 1907/08 (only about 16%
  of those lists) and 1913/14.[50,55]
- **Rotterdam:** the Stadsarchief Rotterdam holds the Holland America Line
  passenger lists with a name search. The index names only the person who made
  the booking, often with an initial for the first name, so search the person
  likely to have made the booking, and do not expect other party members to be
  named.[51]

A published passenger compilation is a derivative, so read its introduction. Some departure-port
compilations, such as a Bremen-to-New York set, were rebuilt from U.S. arrival manifests. Cite
such a compilation as derived from the arrival record, not as independent departure evidence,
and check each entry against the arrival image. For the 1727–1808 ship lists of German
passengers, which the speakers describe as held by the Pennsylvania State Archives (confirm the
holding before requesting), cite Strassburger and Hinke's German
Pioneers volumes as transcriptions. When the immigrant's signature or written name form matters,
ask the Pennsylvania State Archives for copies of the original ship lists. The
[German-origins lecture](https://www.youtube.com/watch?v=2PxBQeskcSI) and the
[State Archives staff account](https://www.youtube.com/watch?v=lZl4PtvBXIU) motivate this step.
They do not describe the compilers' extraction criteria or which lists carry signatures, and a
signature alone does not identify a person.

#### Follow a known vessel into a bibliographic source

For an already supported ship and journey, search a vessel bibliography for references
to a log, voyage account, passenger or crew record. Preserve the cited title, volume/page
or manuscript description and follow it to the actual library or archival holding.
A bibliographic entry remains a lead until the cited material is retrieved and inspected.

Before attaching a reference or illustration to the journey, compare its dates and vessel
with the supported sailing: use vessel type, captain, tonnage or documented renaming when
available. Keep unresolved namesakes separate, including different voyages of the same
ship. Preserve an original spelling beside a proposed correction. A contemporary account
can supply voyage context without proving that the ancestor personally experienced each
event it describes. The ShipIndex interview illustrates this bibliography-to-holding route
and the risk of same-name vessels; it does not establish current holdings or access.[32]

For colonial Pennsylvania, keep a German passenger's arrival allegiance oath separate from a
naturalization proceeding. The province required foreign males aged 16 and over to swear
allegiance from 1727; that ship-list oath alone does not establish naturalization. Record the
document's actual title and date before assigning a citizenship event. [N81], [N82]

### 6. Reconstruct the whole manifest row

**Trigger:** an index exposes only a name and year, a relative is missing, or
the apparent destination does not fit.

1. Save the heading, ship, arrival date, list/page number and passenger line.
2. Inspect adjacent images for the continuation of the form. Match the list
   and line numbers across the two halves; the next displayed image alone is
   insufficient.
3. Extract each labeled place separately: birthplace, last residence,
   embarkation, intended destination, relative left behind and U.S. contact.
   Read companions' rows where they explain the party.[6,7]

**Output:** a full-row extract with both image locators and a contact queue.
**Check:** the headings govern the interpretation. A contact recorded as an
uncle, cousin or friend is a lead to investigate, including its address; it
does not establish that relationship without further records.[6,11]

In the Foundation’s Arrival Details, take the line number and image reference
to View Full Image. Read that row on the image. Use the text view as a
locator. [N182 @2026-11-22] Check adjacent images for a continuation, matching the
list and line numbers. Use the Foundation’s [Tips & Tricks guide](https://www.statueofliberty.org/wp-content/uploads/2026/04/Arrival-Records-Collection-Tips-Tricks-1.pdf)
for the carousel and list-number procedure. [N190 @2026-11-22] The Genealogy Gems tour
from the available excerpt demonstrates how to follow the line number. [N181 @2026-11-22]

In MyHeritage's New England and North Carolina passenger and crew collections,
check both halves when the viewer joins a two-page manifest. If the second half
is absent, locate the continuation by ship, list and line before marking the
entry read. [N149 @2026-11-21] [N150 @2026-11-21] [N151 @2026-11-21]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A New York passenger index query sends the passenger's name and any entered birth or voyage details to MyHeritage. Apply the privacy gate in `SKILL.md` first.

For 1890–1891 New York arrivals recorded with Austrian, Polish or Galician
citizenship, use the MyHeritage Austria, Poland and Galicia index from JewishGen.
Save the indexed name, ship, arrival date, roll and line reference. Use M237
rolls 543–580 to retrieve the manifest. If the line points to someone else,
check the vessel's other numbered lists. Read any age, occupation, marital status
and destination on the manifest, and keep the indexed citizenship separate
from birthplace. [N125 @2026-11-20] [N126 @2026-11-20] [N127 @2026-11-20]

For 1906–1942 ship arrivals, search MyHeritage's New York Passenger List Book Indexes
and use the indexed name, birth year, arrival year and ship to locate the row.
When the viewer shows a joined two-page manifest, inspect both halves of the
same image. Match line numbers before transcribing the continuation. [N128 @2026-11-20] [N131 @2026-11-20]

Date the manifest before treating a missing contact as an omission. On the
1907 two-page form, look for the nearest relative or friend in the country
the passenger came from and the separate U.S. relative-or-friend field.
Use the actual headings to determine which questions were asked. [N128] [N133] [N92]

Read the question about earlier U.S. visits by heading. On the 1907
two-page form it is on the continuation. Copy the reported when and where into
a separate journey row and search that earlier arrival window. [N132] [N133]

Copy any brackets grouping passengers and preserve the adjacent relationship
labels with their row numbers. For each family member still missing, search for
a separate arrival and compare the order, companions and named contacts across
journeys. Check a stated relationship against household and vital records,
including a witness or informant role that links the same people. [N132]

When the form records who paid the passage and how much cash the passenger
carried, extract those fields separately and read them with the traveling party.
Use them to identify leads about who helped fund the trip. Leave the passenger's
means and motives open. If an earlier-arriving spouse lived elsewhere, compare
the intended destination with the spouse's dated residence before drawing
conclusions about where the traveler settled. [N85] [N86] [N88]

If a manifest labels a passenger `Hebrew` in the historical race-or-people
column, retain the label verbatim as the clerk's recorded classification for
Jewish origin. Keep nationality, birthplace and language in their own fields. Marks
points to the label in her advice from the available excerpt. [N91] [N97]

A clerk may have filled a column such as nationality or residence once and drawn a ditto line
down the page. When a filter on an attribute you know is correct returns nothing, rerun the
search without it. Read a dittoed value as the page's default, not as that passenger's own
statement. A New York page carried “Sweden” down from the first entry, hiding a German family from a German-nationality search [N22]. Also do not assume a
family appears together on one list. Follow annotations that point to another page and line. In
later periods, search the same voyage's U.S.-citizen list for a naturalized relative who may
have gone back to bring them over [N23].
When separate citizen lists existed depends on the period and port, and neither source shows how
widespread these practices were.

When possible companions may be on other pages, inventory the available passenger rows
for one defined sailing. Record its date/ship and page extent; retain each row's page and
image locator, literal name and place-field heading/value. Mark missing pages or rows rather
than calling an incomplete extract the whole sailing. Sort complete rows together by the
recorded place field and name, preserving the original text and checking any split names.
Compare candidates with a source-linked census or tax neighborhood from a stated later
date, then inspect the passenger images and keep proposed cross-record identities separate.
This can expose a possible companion several pages away. Sharing a sailing or neighborhood
does not establish kinship or identity, and finding no overlap does not disprove the voyage.
The [passenger-inventory demonstration](https://www.youtube.com/watch?v=xm7HHLneP-E)
supplies this method; no particular export control or complete index is assumed.[31]

When party markings are absent, prioritize fellow passengers who share both the
recorded town and the intended destination. Carry both literal fields and each
row locator into the companion comparison. [N156]

### 7. Turn a detention mark into an outcome search

**Trigger:** the row contains detention or special-inquiry markings, a
crossing-out, or an unexplained alteration.

1. Preserve the original and amended readings. Identify the mark using a
   manifest-annotation guide rather than guessing from its appearance.
2. Inspect appended detention and special-inquiry pages for that sailing.
   Match the manifest list/line reference as well as the name.
3. Record the release, exclusion or other outcome actually documented, and
   search the resulting destination/contact when useful.[10,11]

**Output:** an arrival-to-outcome chain or an explicitly missing outcome.
**Check:** detention alone does not say that the passenger was deported;
crossing-out alone does not settle whether the person traveled. Do not count
meals as days without understanding the form's accounting.
[JewishGen left-margin guide](https://jewishgen.org/infofiles/manifests/left/)

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A San Francisco detainee index query sends the traveler's name and any entered arrival year or ship to MyHeritage. Apply the privacy gate in `SKILL.md` first.

For a possible San Francisco special inquiry in 1910–1941, search the MyHeritage San Francisco special-inquiry index.
Use the name, arrival year and ship to match the detention register image to
the traveler. The San Francisco registers of persons held for inquiry
(February 1910–May 1941, NAID 4468084) are a separate route when the vessel's
images lack the appended sheets. Check the recorded disposition before assigning
an admission or exclusion outcome. [N128 @2026-11-20] [N129 @2026-11-20] [N130 @2026-11-20]

For a San Francisco inquiry, browse FamilySearch’s *Immigration Office Special
Inquiry Records* (collection 2299374, M1388) by date and ship if the name index
misses or the vessel images omit the inquiry. [N173 @2026-11-22] For a Japanese, Filipino
or Hawaiian inquiry in 1928–1942, also check the separate registers for those
held for inquiry (NAID 4497860). These are inquiry registers, so keep a
separate passenger-arrival search open. [N169 @2026-11-22] [N172 @2026-11-22]

Read a left-margin `X` as a detention lead and `S.I.` as a special-inquiry lead.
Browse the sailing's appended sheets, starting at the end of its image sequence,
and copy the stated cause, disposition and discharge date. Expand `LPC` as
“likely to become a public charge.” Use dated detention and discharge entries
to establish the interval and keep meal counts as a cross-check. A count alone
does not fix the number of days. [N95] [N96] [N99] Marks's advice
from the available excerpt is to follow the margin marks to the detention
pages and check the meal columns. [N91]

Treat polygamy and anarchism entries on forms used under the 1907 Immigration
Act as answers to admission screening questions. Use the separate inquiry or
disposition record to establish whether officials refused admission. [N104]
Marks's explanation from the available excerpt points to the screening purpose. [N91]

When an Ellis Island record points to an exclusion or appeal, follow the action
date to a separate case file. For an action before 1 April 1944, check the INS
Subject and Policy Files (NAID 559947), especially if the case was appealed.
For actions on or after that date, start with the A-File route in workflow 11.
If a later appeal still points to the Subject and Policy Files, check both
series. Keep the manifest and any inquiry sheet as their own sources. A routine
arrival or an unappealed exclusion may have no surviving case packet.
[N159 @2026-11-21] [N160 @2026-11-21]

**Privacy gate:** <!-- privacy-gate: request --> A special-inquiry index request sends the immigrant's name and any supplied birth, arrival or case details to the USCIS Genealogy Program. Apply the privacy gate in `SKILL.md` first.

For a supported pre-April 1944 special-inquiry lead without a file number,
request a USCIS Genealogy Program name-index search for the Subject and Policy
Files. Carry the returned number into the archival recovery queue.
[N130 @2026-11-21]

### 8. Separate the voyage from later verification on the same image

**Trigger:** marginal dates or numbers appear decades after the sailing, or
an annotation is being treated as another arrival.

1. Copy the mark, its column and any date exactly, keeping uncertainty visible.
2. Consult the guide for that position. Inspection marks and later
   naturalization-verification marks serve different purposes.
3. Add the later administrative event to a separate timeline row. For an
   occupation-column verification, interpret the district using the key for
   the annotation's date: districts were renumbered. Use that geographic lead
   to choose courts. The verification application number cannot locate
   naturalization records; it is not a court petition or citizenship-certificate
   number. Follow other references only after identifying their record type.

**Output:** an annotation ledger and targeted court/file leads. **Check:**
never replace the manifest's voyage date with a later verification date, or
turn a verification reference into proof that citizenship was granted.
[JewishGen verification-annotation guide](https://jewishgen.org/InfoFiles/Manifests/occ/)

### 9. Follow naturalization across courts and record forms

**Trigger:** a census suggests citizenship or first papers, but the familiar
naturalization database has no result.

1. Build a residence-by-year court table covering relevant municipal,
   county, state and federal jurisdictions. Federal standardization in 1906
   did not end local-court naturalizations.
2. Search declarations and petitions independently; they can be in different
   courts. Follow an index reference to the volume/page or petition itself.[4]
3. Search court minutes and related local holdings when a dedicated
   naturalization series is absent. Look for declarations, admission/oath
   entries and attachments, not only a certificate.[12]
4. Follow the located proceeding through available continuances to its final
   admission, dismissal or other order; retain the order's locator and date.
   Report that proceeding's outcome separately from filing or hearing notices.
   A dismissed petition still has a useful packet; leave later or other
   proceedings unresolved. The [final-order example](https://familylocket.com/back-to-the-basics-with-naturalization-records-part-3/)
   motivates this check without adopting its inconsistent dates or ultimate status narrative.

If residence or property evidence supplies a federal homestead-entry lead, add its
[separate land-entry file](land-index-book-series-recovery.md#5-carry-a-us-federal-patent-lead-into-its-separate-entry-file)
to the recovery queue. The [NARA records interview](https://www.youtube.com/watch?v=T9iEw4Zhb7M)
identifies such packets as a possible location of naturalization papers. Preserve any
paper's actual title, date and supplied court/reference with its locator inside the land
file; follow a supplied court lead to the corresponding proceeding. A paper found in a
land packet does not mean the court file has been inspected. This retrieval lead supplies
no universal eligibility rule, citizenship conclusion or expected packet size.[29]

**Output:** a court packet, or a court-by-court recovery queue. **Check:** first
papers are not completed naturalization. NARA generally holds declarations
and petitions rather than the citizenship certificate.
[NARA naturalization guide](https://www.archives.gov/research/immigration/naturalization)

Before reporting a declaration or petition as lost, or blaming a court not yet searched, check
whether the paper was required at all. Read the act cited on any petition you find, and check
the exemptions in force for the dates. A declarant's widow and minor children might need only
the oath. An honorably discharged soldier might petition without a declaration. Some states gave
voting or land rights on a declaration alone, so a petition may never have been filed. Extend
the search window through the person's whole life, since naturalization could come decades after
arrival. The [naturalization introduction](https://www.youtube.com/watch?v=2K4FYUhoNbc) and
[Tanner's lecture](https://www.youtube.com/watch?v=8d_4x7YTNQA) motivate this check but do not
give each act's exact terms. Verify the law that applied.

In a naturalization file, check adjacent images for a certificate of arrival. Use its port,
date, ship and arrival name to retrieve the manifest image, then compare the petitioner's own
statements with that row. A certificate points to a manifest entry; it does not automatically
identify the petitioner. Matching file numbers link papers to each other, but a petitioner who
is absent from the cited manifest and gives a different arrival year may have used someone
else's arrival. The [Lil Dicky tree example](https://www.youtube.com/watch?v=SKDoU7MJkds) and
[Mayhem on a Manifest](https://www.youtube.com/watch?v=ZgyxRZdHgcw) motivate this; neither shows
how common borrowed certificates were.

For a claimed naturalization, compare the person's 1900–1940 census status entries across
years before accepting a same-name court hint elsewhere. Use changes from alien to first
papers to naturalized to rank the court-search window and residences. Keep each census answer
as an informant's report: an inconsistent answer does not by itself exclude a court record.
[N72], [N73]

When a naturalized voter’s court is unknown, read the historical voter
registration for the documented jurisdiction. Read the naturalization date
and court where supplied, and use them to locate the proceeding. [N174]
In California, check the Great Register and use the underlying registration
affidavit when a later printed index omits naturalization particulars. Treat
the voter registration as a lead to the court record. [N175]

For a foreign-born man aged 21 or older in 1870, read column 19 of the
population schedule as a reported citizenship clue and seek the underlying
proof. If the person later applied for a U.S. passport, extract any court and
naturalization date from the application and search that proceeding. Record
the census and passport statements with their own dates and sources.
[N115] [N116] [N117]

When an index says “first papers,” retrieve the declaration of intention
and check its birth and arrival fields. For “second papers,” retrieve the
petition for naturalization. On a petition with family fields, copy the
reported spouse and children with any birth dates, and the date and place
of marriage when supplied. Use the forms' actual fields and keep the reported
relationships provisional. [N115] [N118] [N119] [N132]

When an arrival search stalls, use the voyage or arrival year stated in
the petition to rerun the manifest search, even if the packet has no certificate
of arrival. Check the stated port and ship against the voyage itself before
replacing any established journey date. [N132] [N118]

When the granted court packet lacks the certificate, check family papers
for the original. Copy the name, certificate date and any issuing court or
number. Before 27 September 1906, courts did not keep backup copies of these
certificates; check the court's admission order if the family copy is missing.
For a grant from 27 September 1906 through 31 March 1956, follow the C-File
route for the federal duplicate. [N115] [N119]

For an Ohio federal-court lead, use the NARA Chicago inventory to identify the
district and city, then check dates separately for the petition index,
declarations and petitions. Keep plausible Ohio local courts in the court
table on both sides of the 1906 change. Treat the listed spans as ranges that
can contain gaps. [N123 @2026-11-20] [N124 @2026-11-20] [N118 @2026-11-20]

Use the series search from the available excerpt of Just Genealogy's catalog
demonstration. [N161 @2026-11-21] Search the NARA Catalog for
`petitions for naturalization` plus the court or place. Open the series description for the
court, dates and holdings location, then check the partner list and the
applicable name index. A series description can exist without a linked petition
image. [N162 @2026-11-21] [N144 @2026-11-21]

For U.S. District Court petitions from the Southern District of New York,
start with M1972 (1897–1944). Use the roll list with the volume and page or
petition number from your locator. Check the separate M1676 petition index
for its own 1824–1941 range. M1879 covers Eastern District petitions.
[N163 @2026-11-21] [N164 @2026-11-21]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A Queens or Bronx naturalization query sends the applicant's name and any entered origin, arrival or filing details to the NY Naturalizations portal. Apply the privacy gate in `SKILL.md` first.

For the Queens and Bronx lead from the available excerpt, search the NY Naturalizations portal. [N138 @2026-11-20]
Use the filing county and number to match the documents. The clerk ranges are
1795–1952 for Queens and 1914–1952 for the Bronx. Check the available
declaration, petition or arrival certificate for birthplace and port. A
declaration-only Bronx filing can be absent from the online search. Keep the
clerk's declaration series in the recovery queue for that case.
[N139 @2026-11-20] [N140 @2026-11-20] [N141 @2026-11-20] [N142 @2026-11-20]

For the Waterbury court lead from the available excerpt, use the NARA partner
list to locate the separate FamilySearch volumes for the District Court at
Waterbury, New Haven County. [N143 @2026-11-20]
Check Adults (NAID 4522153), Minors (4522170) and “Under 18” (6920294),
each 1885–1906, and “Second Papers” (6920472), 1885–1903. Match the actual
volume title before recording which series a search tested. [N144 @2026-11-20]

A missing earlier declaration can be legitimate under the minor-alien exception used in
1824–1906. Check the actual proceeding and applicable law: the 1824 act concerned applicants
aged at least 21 who had lived in the United States for the three years before turning 21 and
five years in total, within its historical eligibility restrictions. Do not apply it to every
person who arrived under 21, or equate it with derivative citizenship through a parent.
[N74], [N75]

Copy what each naturalization witness actually attested, including the period of acquaintance
or residence. Under the 1906 act the qualifying witnesses were U.S. citizens and testified about
residence and character; use a foreign-born witness's own citizenship history as another search
lead. A witness signature does not prove lawful qualification, kinship, or acquaintance in the
old country. Use the residence requirement of the act actually applied to look for earlier U.S.
residence, allowing for the act's exceptions. [N76], [N77], [N78], [N79]

The 1906 declaration and petition forms supplied birth fields; the act qualified the petition's
date and place of birth with "if possible". Extract the birth particulars actually recorded,
earlier names and arrival details, then compare them with the origin records. A blank field is
not proof the record is from before 1906. These are the applicant's statements, not an automatic
identity bridge across the Atlantic.
[N80], [N79]

For an exact hometown, start with the relevant passenger manifest when it has
town-level fields. If the manifest stops at a country, check the declaration
and petition for the named place of birth. Pre-1906 courts used their own
forms and only some give a precise birthplace. If the court papers stop at a
country or an allegiance, look for the town in vital records. [N92] [N100]
The sequence follows Rich Venezia's advice from the available excerpt. [N87]

After a court search, leave open the possibility that the person never began
naturalization. Becoming a U.S. citizen was voluntary. Record the court and
date coverage of the search and keep citizenship unresolved unless other
evidence establishes it. [N100] Non-filing is a possibility in Venezia's advice
from the available excerpt. [N87]

### 10. Replace a missing woman's or child's petition with a status timeline

**Trigger:** a woman or child is described as a citizen, yet no individual
naturalization petition is found.

1. Tabulate birth, arrival, marriages, spouses' or parents' citizenship events,
   residence and the child's age at each relevant event.
2. Check the historical rule applicable to those dates and circumstances.
   Use [NARA's women's naturalization history](https://www.archives.gov/publications/prologue/1998/summer/women-and-naturalization-1.html)
   for marriage-related changes. The [State Department FAM link](https://fam.state.gov/FAM/08FAM/08FAM030109.html)
   is a lead for historical derivative-citizenship charts for a child whose status may follow a
   parent's naturalization: the source fetch failed with a certificate error on 3 November 2026,
   so the page's title and contents were not confirmed (sources, item 46). Obtain a readable
   authoritative rule before using it to infer citizenship. Select the
   period and check its conditions before predicting a record category; do not
   apply the modern rule across all periods.
3. Search the spouse's/parents' court papers, derivative citizenship
   documentation, or a woman's repatriation oath and related file where the
   timeline warrants it. Citizenship might have arisen without the person's
   own petition, and later documentation was not always obtained.[2]

**Output:** a status hypothesis linked to specific record searches. **Check:**
absence of a personal petition does not establish noncitizenship; the
supporting family events and historical rule must be checked separately.

When a naturalization paper names a former sovereign or an "alien parent," copy
that clause literally with the named person, the paper's date and its locator.
Keep it as the applicant's nationality statement and a separate parent/origin
lead, including an unfamiliar name form. Compare the parent's dated records
before choosing an origin jurisdiction. Do not replace the stated allegiance
with the present-day country of the petitioner's birthplace, or infer inherited
citizenship from a parent’s birthplace. One reported petition named a Danish sovereign and called the applicant’s father his “alien parent” [N35]. The article gives no precise locator for the original court paper.

Check how the citizenship rules in force on the marriage date applied to each spouse [N45]. A 1910 marriage appears on a Minnesota-born woman’s later oath application, helping explain the alien designation in her census entry [N25]. Search her own name. After 1922, check adjacent filings in the same series for a separate petition by the spouse or another relative, then verify each filing’s own date and identity [N25].

### 11. Route federal records by type and actual custody

**Trigger:** a court packet is incomplete, an A-number appears, or the
research has stalled at a generic USCIS request.

**Privacy gate:** <!-- privacy-gate: request --> An A-File request to the USCIS
Genealogy Program, or by FOIA for a higher-numbered file (step 2), sends the
identifiers of a person who may be living; answer the privacy gate in `SKILL.md`
first.

1. Name the desired object: naturalization C-File, Alien File (A-File), or
   Alien Registration form (AR-2). These are different objects. NARA's overview
   places C-File naturalizations from 27 September 1906 through 31 March 1956;
   subsequent naturalization records were filed in A-Files.
2. For an A-File, inspect NARA's catalog entry and Contact(s). Save the name,
   NAID and A-number. NARA receives A-Files 100 years after the person's birth
   year. Transfer eligibility by age does not prove transfer. In August 2025
   the National Archives at Kansas City held more than 1.5 million A-Files,
   from across the United States. The National Archives at San Francisco (San
   Bruno) held more than 300,000, from the San Francisco, Honolulu, Reno and
   Guam offices. Check both. The Catalog lists the name of everyone in NARA's
   A-File holdings, so search it by name.[47] A file not yet transferred stays
   with USCIS. Its Genealogy Program accepts only A-Files numbered below 8
   million; a higher number needs a FOIA request.[56]
3. **Privacy gate:** <!-- privacy-gate: request --> An AR-2 or C-File request
   sends the identifiers of a registrant or naturalized person, who may be
   living, to NARA or USCIS; answer the privacy gate in `SKILL.md` first.
   For AR-2, check the Flexoline Index's current coverage, then follow NARA's
   AR-2 instructions. USCIS does not process AR-2 requests received on or after
   17 May 2024; the forms are now requested from NARA.[36,57] An indexed number
   can lack a corresponding form image; the form may have moved into an A-File.
4. For C-Files, use the USCIS Genealogy Program: a known valid certificate/file number allows a [Genealogy Records Request (G-1041A)](https://www.uscis.gov/sites/default/files/document/forms/g-1041ainstr.pdf); without that number, an Index Search Request (G-1041) may be needed first.
   Under the fee rule in force since 1 April 2024, each request costs $30 online
   or $80 on paper (fee schedule G-1055, read 2026-11-07).[58,59] When USCIS
   already holds a record in digital form, it sends the electronic copy with the
   index search result at no extra fee. A record kept only on paper or microfilm
   still needs a G-1041A.[59] USCIS says most C-Files exist only on microfilm,
   so expect that second step for a C-File.[60]
   For other records outside the located NARA holdings, consult current USCIS instructions for the identified record type and available identifiers.

Alongside an A-file lead, search supported spouses, former spouses, siblings or travel
companions as separate file candidates in the catalogues or collections actually available.
Retain each candidate's own name, identifiers and Contact(s), and compare its identifying
details before using the file. A related person's file is a possible source about the
target, not the target's file or proof of the relationship. The
[related-file search account](https://lostrussianfamily.wordpress.com/2026/09/26/nara-quietly-expands-two-databases-of-its-most-valuable-immigration-collections-to-2-5-million-files/)
supplies this extension; the existing type and custody checks still apply.[30]

Do not read a miss in FamilySearch's *United States, Index to Alien Case Files, 1940-2003* as
evidence that no A-File exists. FamilySearch describes it as an index to the A-Files at the
National Archives at Kansas City and warns that files from the Guam, Honolulu, Reno and San
Francisco districts, held at San Bruno, may not be included.[N66 @2026-11-12] A 2025 post on
NARA's own A-File databases calls the FamilySearch index incomplete and not up to
date.[N67 @2026-11-12] Run the Catalog name search in step 2 whatever this index returns.

**Output:** a request-ready locator packet and named custodian. **Check:** an
A-number alone proves neither A-File custody nor AR-2 image availability. A
catalog miss leaves custody unresolved.
[NARA naturalization](https://www.archives.gov/research/immigration/naturalization),
[A-Files](https://www.archives.gov/research/immigration/aliens),
[AR-2](https://www.archives.gov/research/immigration/alien-registration-ar-2)

**Privacy gate:** <!-- privacy-gate: request --> A USCIS index search, a visa-file request or an
alien-registration request names an immigrant who may be living, and the files can name family
members; answer the privacy gate in `SKILL.md` before sending any of them.

For an intended journey under the Immigration Act of 1924, distinguish
a visa issued abroad, inspection at the U.S. port and the admission decision.
If the visa survives, check the inspection endorsement for the arrival date,
port and means of transport. Use these details to find the manifest
and any separate disposition. Visa issuance alone leaves entry unresolved.
If a quota might explain a missing journey, check the applicable category and
year before attributing the gap to the law. [N179] [N180]

Keep the visa number printed on the manifest separate from the INS Visa File number. INS assigned its own number and indexed by name, birth date and birthplace [N105]. If the file number is unknown and USCIS holds the series, request a USCIS index search for the arrival first to get the file number, then make a separate records request.

Check the current custodian and whether the visa papers were placed in a later A-File or C-File [N106 @2026-11-19].

For the entry itself, look for supporting vital records, certificates, addresses and photographs. One forum search using a manifest visa-number lead ended without a result [N28]. Record where the search stopped; it does not establish that a file never existed.

Alien registration was not only the 1940 AR-2. For WWI enemy-alien registrations and state-run
registrations, ask both the state archives and the NARA regional facility with jurisdiction over
that state. Log which level and which series were checked. Many of these series are browse-only
or missing from the major search engines. The speaker's examples include Minnesota 1918 and
North Carolina 1927–1940, and a German registrant's papers can name family in Germany. The
[Lisa Lisson interview](https://www.youtube.com/watch?v=4d43ZFUIzbs) and
[Miles Meyer](https://www.youtube.com/watch?v=tBweLebo7TA) motivate this; verify each series'
existence, eligibility and survival.

For a WWI enemy-alien registration lead, establish the person's residence during the applicable
registration period, then use NARA's survival guide to choose the actual series.
No master list of registrations, permits or arrests survives. The surviving material is
incomplete and also exists outside NARA. Registration was administered by U.S. Marshals;
the guide identifies only selected district courts with registration records, so a generic
court search is not a substitute for its series list. [N83 @2026-11-16] [N84 @2026-11-16]

Keep an internment inquiry separate from registration. The DOJ *Alien Enemy Index, 1917–1919*
(NAID 602456) gives a related file number; a `9` points to *Class 9 (European War Matters)
Litigation Case Files and Enclosures* (NAID 599528). Follow that reference and record the actual
arrest-to-release or deportation material returned, without inferring an outcome from the index.
For Swiss diplomatic assistance, also search the State Department's *Name Index, 1910–1973*
(NAID 581008) and retain any correspondence file reference. A registration does not establish
internment, and a name-index hit does not guarantee the underlying file survives.
[N83 @2026-11-16] [N84 @2026-11-16]

### 12. Repair an image failure with an archival locator

**Trigger:** an index points to a wrong image, a page is missing, or the
expected entry cannot be reached in the viewer.

1. Save the failed link and the index's ship/date, list/line, roll/frame or
   court volume/page reference. Distinguish printed page numbers from viewer
   image numbers.
2. Browse from the ship/date or nearby valid frames; try another provider of
   the same series. For court volumes, inspect page-number continuity and
   the volume's internal index.[12]
3. **Privacy gate:** <!-- privacy-gate: request --> A targeted request names the
   researched person, who may be living; answer the privacy gate in `SKILL.md`
   first. If the digitized sequence skips the referenced page, prepare a targeted
   request to the holding archive with the volume, page, person and date;
   include the observed image gap.

**Output:** a recovered image or a reproducible gap report. **Check:** stop
repeating name queries once the failure is demonstrably in the image link or
digitization. A missing online page does not establish that the archival entry
is missing.
[Morse image and browse FAQ](https://stevemorse.org/ellis2/faq.htm)

For New York arrivals, browse the NARA microfilm by roll when the index fails
or a name was never indexed. M237 covers 1820–1897 (675 rolls) and T715 covers
1897–1957 (8,892 rolls); the two series meet in June 1897.[52] Find the roll
for the ship and arrival date and read it image by image. Single reels are also
on the Internet Archive, one item per reel with the reel's date span in the
description (item IDs such as `passengerlistsoo0148unix` for M237 and
`passengercrewlis4247unit` for T715).[53] For an 1820–1891 name index, use
FamilySearch's "New York, Passenger Lists, 1820-1891" (collection 1849782);
arrivals from 1892 to 1897 are in a separate collection.[54]

## Prompt-craft

“Recover the historical U.S. records for this person. Start with the failed
query and known locators. Choose the relevant workflow, list ordered actions,
and produce the journey table, coverage row and recovery queue. Preserve
original names, event dates, list/line and volume/page references. Explain
exactly which image or court entry supports each recovered statement. Keep
unreadable text, untested searches, absent online images and unresolved custody
distinct. Do not infer citizenship, kinship or port from a search result label.”
