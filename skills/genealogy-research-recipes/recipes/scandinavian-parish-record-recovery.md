---
id: "scandinavian-parish-record-recovery"
title: "Reconstruct a Swedish household through parish examination and moving registers"
summary: "Reconstruct a Swedish household through the household-examination, birth, marriage, death and moving registers."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "SCANDINAVIAN-PARISH-RECORD-RECOVERY-01", "text": "Follow the family by farm or residence and by page cross-reference, not by patronymic. Settle identity at the household level."}]
handoff: ["scandinavian-patronymic-farm-name-record-recovery", "tax-roll-observation-workflow"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images", "MyHeritage Swedish household and vital-record indexes"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 118}
---

# Reconstruct a Swedish household through parish examination and moving registers

Use this recipe when you have a Swedish or Finnish ancestor's name, a rough parish or farm, and rough birth or marriage dates, and you can view digitized images of the household examination (husförhör), birth, marriage, death and moving-in/moving-out registers. The household examination is your index into the other registers. Follow the family by farm or residence and by page cross-reference, not by patronymic. Settle identity at the household level. Finland kept the same kind of register; its differences are in "Finland: work the rippikirjat the same way" below.

Check the parish's actual holdings and image-access conditions at FamilySearch, Riksarkivet and ArkivDigital. Do not infer access or coverage for one parish from a country-wide description.

For a Danish parish, use [Danish church books and probate](danish-church-book-probate-recovery.md) for the church books, civil marriages and probate.

Related recipes:

- [FamilySearch record workflows](familysearch-practical-record-workflows.md) for FamilySearch Catalog, film and image-route steps.
- [Evidence/proof judgment](evidence-proof-judgment.md) for merge, separate and proof rulings.
- [Archival image coverage](archival-image-coverage-verification.md) for claims that a volume's images are complete.
- [Scandinavian patronymic and farm names](scandinavian-patronymic-farm-name-record-recovery.md) for Norwegian censuses and emigrant protocols, and Danish censuses and levying rolls.

## Contents

- Do not start from a patronymic name hit
- Read the household examination page as a locator set
- Carry the household from volume to volume by residence
- Do not treat one entry as the whole family
- Follow a missing birth to another parish
- When the page trail breaks
- Do not call it a census
- Bridge gaps with poll-tax registers and probate
- Before 1869, look for emigrants in the moving-out registers
- Finland: work the rippikirjat the same way
- Close with a household chain packet

## Do not start from a patronymic name hit

- Do not link people from a name index just because they share a -son/-dotter name and similar dates in one parish. A shared patronymic only shows that their fathers had the same given name. It is not evidence of kinship.
- Tanner says a family is only correctly identified once you place it at a specific house or farm, with the person living there and having children there. If the person is not in that household, he says you probably have the wrong person [S4].
- An index hit is only a pointer to a household examination page. It does not identify the person.

## Read the household examination page as a locator set

On the examination page, record each of these items separately [S1], [S2]:

- the farm and the household’s position on its page. Several families can occupy one farm. Use the household head and neighbours to distinguish them [S1];
- the head of household and his occupation;
- each member’s date and place under the printed birth headings. Copy them as written and label any separate christening date [S1], [S5];
- the couple's marriage date;
- the moved-in and moved-out columns, and any crossed-out names with their notes on departure or death.

Use the examination entry to locate the child’s birth and the parents’ marriage. Compare the names, dates and residence in both originals with the household page, and record any disagreement [S1].

The cross-references run both ways. Expect them and follow them [S5]:

- Birth entries often give the family's page in the examination volume.
- Marriage entries give the residence pages of both the bride and the groom.
- Death entries name the residence.
- Moving entries frequently give the page of the farm where the migrant settled, or the parish they came from.
- A move within the parish is noted with the page of the new residence. A move out of the parish is often noted with the departure date and the number of the moving-out entry.

Record every page reference exactly as written, including ones you have not followed yet. If an expected reference is missing, note that as well.

### Separate Swedish banns from the wedding

Start the banns search in the bride's parish. Record the announcement under *lysning* and establish the wedding date from the *vigsel* entry. If the banns entry gives no wedding date, follow any wedding-parish note and search for the wedding separately. The two entries can be in different parishes. [S32] [S33] [S34]

When an index hit gives a banns number and a wedding number, copy each with its label, parish and year. Use each number in the corresponding register or column and confirm both spouses in the entries. Keep entry numbers separate from printed page numbers. [S32] [S35]

### Decode an urban number before opening a page

A number beside an urban birth may identify a *tomt* (lot). Read the column heading and find the lot in the book’s index. In ArkivDigital’s Borås example, lot 7 led to printed page 15, shown as viewer image 12 [S23].

1. Copy the reference and its column heading, parish, date and referring volume.
   Distinguish a lot number, a printed page or folio (*fol.*), and a viewer image
   number. Leave an unexplained number unresolved.
2. Compare all volumes covering the relevant period. Their descriptions may divide
   the town by lot ranges, named places or page intervals. Select the volume whose
   stated division contains the target; overlapping years do not mean duplicate books.
3. Read the contents and place/lot indexes at the front or back. Follow the lot's
   index entry to its printed page, then check the lot heading and household there.
   Keep the index locator, target page and viewer image separate.
4. When a move gives a place name in place of a number, check the town’s place index before searching another parish. Follow every starting page for the locality and any continuation. ArkivDigital found the Karlsdal household in the second indexed block after a miss in the first [S23].
5. Re-read the receiving page's layout: moving-in, moving-out and death columns
   can change position or extend across a spread. Compare the receiving entry's
   stated previous residence and year with the departing entry. Preserve conflicts
   instead of silently making the two references agree. [S23]

A strike-through alone records neither death nor emigration. Read the corresponding
death or departure column and follow the actual reference. If it gives a parish and
moving date or entry number, carry those into the moving-register search; do not turn
every crossed-out household into a death or overseas departure. [S23]

### Follow an unknown-whereabouts reference as a register continuation

When the destination says *obefintlighetsbok*, preserve that wording and any folio
reference. ArkivDigital's example explains it as a register for people whose residence
was not known to the parish, including people who had not taken out a moving certificate.
The label does not establish that they emigrated. [S23]

Use the catalogue and contents for the relevant dates to locate the *obefintlighetsbok*, whether it is a section in a household volume or a separate book. Follow its folio, check the household and retain any conflict with the birth entry. In the Borås example, the birth day changed from 22 to 23 January and a later departure column named Stockholm Maria [S23]. Use that dated note to search the receiving parish. Keep the earlier period of unknown whereabouts open.

Add each step to the household chain: referring entry and literal wording, reference
type and its reading basis, selected volume/index block, received entry, incoming/outgoing
crosscheck and retrieval status. An unavailable section, unreadable number or unresolved
destination stays an open link. This procedure establishes how to test a continuation;
it does not verify the narrated family's identity or explain an unlocated person's absence.

## Carry the household from volume to volume by residence

1. Write down the farm or residence from the current volume.
2. Open the index of farms and residences in the next volume. Genealogy Gems says most volumes have one, near the front or the end [S5].
3. Go to the few pages that index points to. Do not search the next volume by name.
4. Local societies have made name indexes only for some larger parishes and cities [S5]. They save time, but they are not the route.
5. Brady notes that the examination books were later replaced by a different format [S1]: the parish books, which Riksarkivet's census database also draws on. When the examination series ends, open the parish's parish books in the Catalog and keep following the residence.

### Resolve GB/NB against the chronological volume set

When an entry gives *GB* or *GL* with a page, ArkivDigital explains these as *gamla boken* or *gamla längden*, the previous book or register. *NB* or *NL* means *nya boken* or *nya längden*, the following book or register [S21]. Preserve the letters and page exactly before resolving the destination.

1. Record the current parish, series, volume and stated years alongside the reference. Identify the preceding or following chronological set of household examination or parish books from the volume descriptions.
2. Check how that set is divided. A large parish can have several books in one period; the target need not have the immediately preceding or following catalogue number, and the books' year ranges need not match exactly [S21].
3. Use the recorded farm or residence and the available residence index to select a book in that set. Open the referenced printed page, keeping its number separate from the viewer image number.
4. Compare the destination's household, residence and dates with the starting entry. Keep a missing or conflicting destination unresolved; do not replace the written reference with the nearest catalogue number or a same-name household.
5. Add the starting entry, literal reference, tested destination and result to the household chain. A resolved continuation supplies another register observation; it does not make the volume boundary a move date.

## Do not treat one entry as the whole family

- Read forward to the latest volume that shows the couple. Hallen says early entries list only the children born so far, and later children were added afterwards [S3].
- Expect children who died young to be missing from the rolls [S3]. Search the birth and death registers for them and list them separately, marked as found outside the household lists.
- Compare residence, age and other identifying details in the parent’s death entry with the household roll [S33]. If it gives surviving children, count only those alive at the parent’s death. Brady reports a death entry counting two sons and one daughter, matching the three children on the roll [S1]. Check birth and burial registers for children who died earlier. Reopen the identification if the discrepancy persists.

## Follow a missing birth to another parish

If a person's birth, or a parent's birth, is not in the current parish, keep going. Search that parish's moving-in and moving-out registers. Record the previous or next parish and the date given, then continue in that parish's examination and vital registers [S2]. Tanner says a moving-out note usually records where the person went [S4].

If the receiving household book gives only a birth year, establish the arrival period and browse the parish’s surviving incoming moving certificates (*inflyttningsattester*). The sending priest may have supplied a full date and birthplace that the receiving priest abbreviated. Compare any detail found with the original birth entry [S20].

For an immigrant from abroad, look for the incoming certificate in the church archive of the first Swedish parish of arrival, not a later one: the certificate stays with the parish that received it [S24]. Parish archive inventories file these certificates in series H II, the attachments to the moving registers, often titled *Bilagor till flyttningslängderna*; the wording varies by parish [S25]. Search NAD by that parish to see whether H II survives for the arrival years and whether it is digitized, then browse it for the arrival interval.

Check the parish’s archive description and its National Archival Database (NAD) entry for the pastorate and mother or annex parish at the date of the event. A joint register may be catalogued under the other parish: ArkivDigital’s 2026 demonstration followed the linked Götlunda birth and baptism books for 1688–1706 and 1707–1723 into Flistad’s archive [S20]. Verify both the parish and the years in the volume. A note of loss explains a gap in the records.

## When the page trail breaks

Genealogy Gems lists several ways the trail can break [S5]:

- the move happened in a year with no surviving migration records;
- the family moved into a city with many parishes;
- the move was never noted;
- boundary changes created a new farm or residence.

In these cases, browse the examination volumes by the recorded birth date. Birth dates sit in their own column and are easier to spot than names [S5]. A birth-date hit is only a candidate household. Before you link it, confirm it by matching the other members and the farm, and by at least one independent birth, marriage or death entry. Use any surviving farm or moving references as further support. In these cases their absence is expected and does not block the link.

For Stockholm city from 1878 to 1926, the roteman offices kept the population register because parish registration could no longer keep up. Search the Rotemansarkivet at Stockholms stadsarkiv. Its online database is incomplete; the whole archive is on the computers in the archive's reading rooms. Record which version you searched. [S27]

### Use Swedish household and vital-record indexes to recover a parish lead

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Apply the privacy gate to the names, dates and places that the search will send to MyHeritage and to each person those terms describe, including anyone who may be living. Send only the terms needed for the search.

Search MyHeritage’s *Sweden Household Examination Books* when the household-page trail breaks. Start with the name and recorded birth date, and put a known residence parish in the Residence field. The catalogue describes coverage mainly from 1800 to 1947. [S45 @2026-11-20] Check the parish and years covered before interpreting a miss.

Take a promising hit to the full household page and record its parish, volume and page. Compare the residence, stated relationships, marriage dates and any moves with the last verified household entry. [S44] Keep a name-only hit as a candidate. Follow a move within the parish by its page reference and a move across parishes through the moving registers. [S46]

Search the matching MyHeritage collection if you still need a parish or cannot locate the vital entry. Carry the hit back to the parish books and establish identity from the household and original entries.

For a birth, use *Sweden Births, 1850–1920*. Take the parents' names and recorded residence into the parish's household examination or parish book. If the birth entry also gives a baptism date, record it separately. [S32 @2026-11-18] [S36 @2026-11-18]

For a wedding, use *Sweden, Marriages and Banns, 1850–1945*. Compare both spouses' names, recorded ages or birth years, and residences with the household entries. Use a parent's name to extend the line only when the parish entry actually identifies that person as a parent. [S32 @2026-11-18] [S37 @2026-11-18]

For a death, use *Sweden, Deaths, 1850–1945*. Match the birth date or age, residence and any named relatives to the household. In the parish entry, record the death and burial dates separately when both are given. [S32 @2026-11-18] [S33 @2026-11-18] [S38 @2026-11-18]

If the image is a church-book extract sent to Statistics Sweden (*SCB*), cite it as an extract and take its parish and year to the parish's own register. Check that register before treating an omitted detail as absent. [S32] [S39]

### Follow a Norwegian or Danish lead through its separate bulletin index

When a dated move, destination or other independent lead points to Norway or Denmark, check that country's police-bulletin finding aids separately. In its 4 June 2025 demonstration, ArkivDigital described Norwegian name-register volumes outside its Swedish searchable police-notice index, and Danish index sections for people born in Sweden or Norway [S22]. These provide a separate entry route; a Swedish index miss does not search them.

| Country and series | Entry route described in the demonstration |
| --- | --- |
| Norway: *Polititidende* | Select Norway in the archive search and inspect the series' separate name-register volumes; the presenter also points to the Norwegian National Library's digitized series. |
| Denmark: *Politiets Efterretninger* | Inspect the name registers, including the separate sections for Swedish- and Norwegian-born men and women; the presenter points to Copenhagen City Archives. |

1. Check the actual catalogue and index volume for the lead's dates. Record the years, sections and fields it covers, the extent inspected and any unavailable volume. The demonstration's holdings and interface are historical, and do not establish present access or complete country coverage.
2. Search the supported name forms in the appropriate index or birthplace section. A special Swedish/Norwegian-born section is a finding route, not proof that its birthplace information is correct or that every migrant appears there.
3. Copy the index's year, division, notice or item number and any other locator exactly, then retrieve that specific notice. Retain the index and notice as linked records; a name-register row is not the notice itself [S22].
4. Extract only the notice's actual names, stated birth details, dates, places and roles. Preserve the reporting authority and whether the text concerns a missing person, an allegation, release or another matter. The demonstration includes notices beyond criminal convictions [S22]. Neither disappearance from a household register nor presence in a police index establishes a crime or guilt.
5. Use a stated place and date to queue the corresponding local household or moving record. Compare the notice's birth details with the parish evidence before linking people. Record a date discrepancy rather than silently correcting it, and keep an unsuccessful search bounded to the inspected index's fields and years.

This route leaves unverified holdings, unindexed fields and Finnish bulletin coverage unresolved. It supplies a possible next locality or record, not an explanation for every disappearance.

## Do not call it a census

- A priest updated the household examination across a period. Cite the parish, volume and the years or dated marks that apply to the person [S2].

- Riksarkivet’s Folkräkningar database has complete national data for 1880, 1890, 1900 and 1910. For 1860 it covers only Jämtlands län, and for 1870 only Västerbottens and Norrbottens län [S26 @2026-11-19]. The database omits 1920, and 1930 registration varies by county [S41 @2026-11-19], [S40 @2026-11-19]. The public 1930 search includes only people born more than 100 years ago [S42 @2026-11-19]. Check the county’s registration status before interpreting a miss.

- Follow the census extract back to its source. Swedish censuses from 1860 drew on named extracts from parish registers [S41]. For Stockholm city, the 1930 project identifies the population register of the *Mantalskontoret* as its source [S43].
- Early coverage:
  - Riksarkivet's administrative history assigns parish registration to the pastor under the Church Law of 1686 and describes catechism or household-examination lists. [S28] This is the statutory context, not proof that a volume survives for a particular parish or year.
  - Check the parish’s actual holdings for each year. Riksarkivet dates the oldest surviving examination lists to the late 1600s or early 1700s and notes that an entry focused on religious knowledge may omit the birth year [S28].
  - Identify the parish's separate moving-in and moving-out series and their surviving spans before searching them. If no separate volume covers the move, inspect the examination's own moving columns. [S2]
- Before you claim any volume is missing, check that parish's actual holdings.

## Bridge gaps with poll-tax registers and probate

- **Mantalslängder (poll-tax registers).** They were compiled every year and place adults on a farm year by year, so use them to bridge a lost or missing household examination volume. [S6 @2026-11-16], [S7 @2026-11-16] Riksarkivet's October 2026 page places the Stockholm city originals at Stockholms stadsarkiv. [S6 @2026-11-16] The registers list mainly the people liable to the tax: Skatteverket gives 12 and over from 1635, 15–63 for 1652–1840, 17–63 for 1841–1856, 18–60 for 1857–1862, and 18 and over from 1863 until the tax ended in 1938; practice varied between places. [S18 @2026-11-16] A royal letter of 18 February 1765 ordered the whole population to be entered in them. [S18 @2026-11-16] Even after that, children usually appear only as numbers in columns, and exempt adults may be missing or entered only with a note. [S7 @2026-11-16] A mantalslängd household is not a complete list of names.
  - If the parish is known but the tax archive's administrative arrangement is not, use the [parish/year contents-index route](tax-roll-observation-workflow.md#swedish-mantalslängder-enter-by-parish-and-year). Carry each inspected year into the household chain; read its headings before interpreting a change.
- **Probate inventories.** Search them by the deceased and the court district. Use the heirs named to bridge parish moves and to check a sibling set.
  - Sweden: bouppteckningar from before 1980 are in the archives of the tingsrätt (district court) and of its predecessors: the rådhusrätt (town court), the domsaga and the häradsrätt (rural district court). Riksarkivet supplies inventories drawn up up to 30 June 2001. [S8 @2026-11-16]
  - Norway: death and probate records are in the archive of the sorenskriver (rural district judge) or, for a town, the byfogd (town judge). [S19 @2026-11-16] On Digitalarkivet, for example, Mandal sorenskriveri's skifteprotokoller (probate journals) sit under that archive, in the series *Dødsfall og skifte*. [S9 @2026-11-16] Some newer death and probate material has access restrictions. [S19 @2026-11-16]

For a Danish probate, use [Danish church books and probate](danish-church-book-probate-recovery.md#route-a-probate-by-status-and-date).

**Poll-tax scans and coverage.** Riksarkivet's database page gives 15–62 for everyone able to work, without naming a period. [S29 @2026-11-13] Before you read an adult's absence from a mantalslängd as a negative, check that year's age range. Riksarkivet has scanned the mantalslängder of the whole of Sweden for 1642–1820 and indexed them by parish. Some volumes were not scanned. The regional archives (landsarkiv) keep other copies, not scanned, which may hold years missing from the scans. [S29]

## Before 1869, look for emigrants in the moving-out registers

Swedish emigration registration began in 1869. The lists were filed with the police in the ports of departure, Gothenburg being the largest. [S10 @2026-11-13] The Gothenburg series is in the archive of Göteborgs poliskammare at Riksarkivet. [S11 @2026-11-13] For earlier emigration, Riksarkivet's administrative history names only the parish moving-out registers (utflyttningslängder) and, possibly, military records. [S10] From 1861 a second source lists emigrants: the clergy's summary population reports to Statistics Sweden (summariska folkmängdsredogörelser). They give each parish's emigrants with name, occupation, year of birth and destination country, and Riksarkivet indexes them as *Emigranter 1861–1940*. They cover only legal emigration, that is, people who asked for a moving certificate. [S30 @2026-11-13] A port-list nil before 1869 is not a negative: search *Emigranter 1861–1940* (from 1861) and the moving-out register, then cross-check the household examination rolls.

Emiweb hosts the Swedish port passenger lists (*Passagerarlistor för svenska hamnar*) as a subscription database. Its only free option is a trial with limited search. [S12], [S13]

## Finland: work the rippikirjat the same way

- The Finnish household register is the rippikirja (communion book; Swedish kommunionbok). It is a running register of the Lutheran parish's inhabitants, so follow it by farm and page as above. [S14 @2026-11-16]
- Where the parish also kept a lastenkirja (children's book), the rippikirja lists only confirmed parishioners, usually those over 15. Look for younger children in the lastenkirja; their entries were moved to the rippikirja after confirmation. Where the parish kept only a rippikirja, it usually lists all ages. [S17 @2026-11-16]
- Church records in Lutheran parishes were mostly kept in Swedish until the later 19th century and mainly in Finnish after that. [S17 @2026-11-16] Search Swedish and Finnish forms of names and places. For Orthodox records, add Russian forms: those church archives were written in Russian until the 1920s. [S31 @2026-11-16]
- HisKi does not cover every parish or year. [S15 @2026-11-16] Check which parishes and years it covers before you read a nil, and verify every hit against the church-book image.
- Katiha (katiha.kansallisarkisto.fi) is a searchable database of data from the church archives of the Karelian areas ceded to the USSR, from the 1600s to the 1900s. [S16 @2026-11-16]

**Orthodox names and church-book images.** Before the late 19th century Orthodox church books gave a patronymic instead of a surname, except in some North Karelian parishes such as Ilomantsi and Taipale, which recorded surnames. The Orthodox church kept the Julian calendar until 1920, so check which calendar an Orthodox date uses before you compare it with other records. [S31 @2026-11-16] Lutheran and Orthodox church books have been microfilmed, and many older books are digitized in the National Archives of Finland's Astia service; much of the material more than 100 years old is freely available online, while younger records have restrictions. Check the particular book's availability, and look for the image of each index hit there; if the book is not digitized, record the image as not seen. [S17 @2026-11-16], [S31 @2026-11-16]

## Close with a household chain packet

Return:

- the chain of parish, volume, page and farm for each observation, in order;
- urban lot/place and unknown-whereabouts references, with their decoded roles, tested index blocks and unresolved continuations;
- each member's birth date exactly as recorded on each page, with any christening date labelled separately;
- links to the original birth, marriage and death entries;
- the origin and destination parishes, with dates, from the moving registers;
- any mantalslängd years and probate inventories used to bridge a gap, with their court or archive locators;
- children found only in the vital registers, listed separately;
- each gap, labelled as a volume that is unavailable, a volume that has not been inspected, or a volume that was inspected without finding the person or the connecting entry, with a note of what was searched.

A parallel household found by birth-date browsing stays a candidate until the person making the ruling decides on it under [evidence/proof judgment](evidence-proof-judgment.md).
