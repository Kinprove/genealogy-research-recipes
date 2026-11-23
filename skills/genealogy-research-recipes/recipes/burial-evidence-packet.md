---
id: "burial-evidence-packet"
title: "Build a burial evidence packet from cemetery records"
summary: "Recover a cemetery entry, its photo or inscription, and the plot and register locators needed to check a burial."
kind: "records"
scope: {"platforms": [], "tasks": ["cemetery coverage, surname variants, Hebrew and civil inscriptions, death/burial discrepancies or a database hit that needs a cemetery-record follow-up", "names on a Soviet mass-grave plate"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "BURIAL-EVIDENCE-PACKET-01", "text": "Keep death, burial, inscription and database statements distinguishable. The result is a packet another researcher can inspect, with missing fields and unresolved discrepancies visible."}, {"id": "BUR-01", "text": "Keep death, burial, inscription and database statements distinguishable."}, {"id": "BUR-02", "text": "identity or conflicting-date conclusions belong to evidence-proof-judgment."}]
handoff: ["german-military-record-period-routing", "immigrant-congregation-origin-records", "soviet-personal-file-recovery", "us-20th-century-military-service-reconstruction"]
checked: "2026-10-07"
checked_basis: "checked 2026-10-07"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["link", "publish", "third-party-tool", "upload"], "contact": ["contact"]}
router: {"section": "Record types in any country", "group": "Burials, directories, land and probate", "order": 246}
---

# Build a burial evidence packet from cemetery records

## Contents

- Goal
- Before starting
- 1\. Check coverage before changing the name
- 2\. Search the recorded name fields separately
- 3\. Preserve the photograph and both inscriptions
- 4\. Carry the hit to the plot and cemetery records
- 5\. Keep a discrepancy open and choose the next record
- Prompt pattern

## Goal

Recover a cemetery entry, its available photograph or inscription, and the information needed
to locate the burial in the cemetery's own records. Keep death, burial, inscription and database
statements distinguishable. The result is a packet another researcher can inspect, with missing
fields and unresolved discrepancies visible.

## Before starting

Record the candidate's supported name forms and approximate place/date. Treat the candidate as
unresolved until the collected records establish identity. Use the research-documentation recipe
for the ordinary log and source-citation for citation construction; this packet adds cemetery
identifiers. Transcription and translation belong to ai-for-documentary-records, and identity or
conflicting-date conclusions belong to evidence-proof-judgment.

## 1. Check coverage before changing the name

Choose a database that covers the plausible cemetery or locality. In JOWBR, check the cemetery
inventory, including the cemetery section, before treating a name search as a coverage test.
JOWBR can contain inscriptions, cemetery-register information or published material, and a
photograph is present only when one was submitted. [O1]

Save each candidate's URL and the displayed cemetery/section. Open the full burial record when
available; in JOWBR the headstone icon identifies a supplied photograph, and **View Full Burial
Record** exposes the available fields and image. Leave missing fields empty. A result without a
photograph remains a useful locator, but the inscription has not been examined. [O1]

For a Jewish burial, search JewishGen's JOWBR or its copies on MyHeritage and BillionGraves.
Record the cemetery, reported birth and death details, age at death and any names supplied for
parents or spouse. Treat matching copies of the same JOWBR entry as one record for those details.
[P177 @2026-11-18], [P178 @2026-11-18], [P179 @2026-11-18]

A miss in Find a Grave, BillionGraves or another crowd-sourced site is not a coverage test,
especially for small, inactive or private-land burial grounds. Also check county-society
inventories, state cemetery surveys or commission databases, and state-archive or archaeological
survey files, which may not be digitized. Record each survey's title, date, holding place and any
registered cemetery number as a separate locator. A listing locates a burial ground, not who lies
in it. For older compiled transcriptions, check the local-history collection of the library or
historical society near the cemetery. Some hold 1930s WPA tombstone transcripts [P4], [P61], [P65].

For a Finnish archaeological register entry, save the site ID and read **Kuvaus** (description)
alongside **Tutkimukset** (investigations). Record the date and scope of fieldwork separately from
each reported feature or find and its source. The 2002 inventory did not visit
Sahrajärvi-Kuoliosaari (1000030045), even though it recorded the witness account behind the grave-like
depressions and skull finds reported in Kyläkoski’s excerpt. [P296† @2026-11-23], [P297 @2026-11-23],
[P298 @2026-11-23]

FamilySearch lists Full-Text under its Search menu. Sign in and try `cemetery` with the place name to locate digitized transcriptions [P64 @2026-11-19].

Keep each survey’s date with its reading of a stone that later broke or disappeared. Record whether the compiler read the inscription, relied on a local account or located the grave by dowsing. The Berks County preservation group reported that its compilation included dowsing-based locations and that it still found errors [P192].

At a plantation cemetery for enslaved people, log visible ground depressions as possible grave
locations even where there are no markers. On an authorized visit, note the depressions from the
surface without probing or disturbing the ground. Look for an existing cemetery delineation
survey to check their position. Leave the occupants unidentified from these features alone.
[P158], [P159]

In Interment.net, open the cemetery’s individual transcriptions and record the compiler, fieldwork
date and underlying source where given. Keep a register-based entry separate from a reading of a
stone. Before using any survey’s silence, compare the candidate’s burial date with the fieldwork
cutoff for that section. Carry a later or undated burial to the cemetery register. [P226 @2026-11-21], [P227 @2026-11-21]

On a Find a Grave cemetery page, read **Photographed** as the share of that cemetery’s listed
memorials with photos. In the cemetery’s memorial map, a pin requires memorial GPS. Use the
memorial list as well as the map when looking for a name, and use the interment register to
check which burials the site omits. [P258 @2026-11-22] [P259 @2026-11-22] According to the supplied Morton tutorial excerpt,
check the cemetery-level photo counts. [P264† @2026-11-22]

For an Ulster burial, use the Ulster Historical Foundation’s **Graveyards in Ulster** to identify
candidate grounds and their records. Then check the separate gravestone inscription collections.
The **North Ulster Gravestone Collection** lists its burial grounds in the search form and contains
a partial upload. Leave the burial open after a miss.
[P269 @2026-11-22], [P270 @2026-11-22], [P271 @2026-11-22]

For a burial ground with no surviving markers, use deeds and local histories to locate the ground.
Build the burial list from named burials in church records, newspapers or histories that identify
the person’s burial. Retain the source for each name and leave individual plots unresolved unless a
record supplies them. [P226], [P228]

Compare dated cemetery transcriptions word by word, including older editions: a stone legible to a 1940s compiler may have worn away by the 1990s [P118]. Record the compiler and date for each reading and check disputed words against an image or the surviving stone [P146].

A marker search can miss early Acadian burials at Fort Anne in Annapolis Royal because the
wooden crosses used during the French period deteriorated.
Search the Nova Scotia Archives' St. Jean-Baptiste parish registers for 1702–1755 when the
date fits. Retain the parish entry and leave the plot unresolved unless another record locates it.
[P194 @2026-11-20], [P195 @2026-11-20], [P196 @2026-11-20]

According to Donald Lines Jacobus, the WPA index is a route to Connecticut gravestone
inscriptions [P213† @2026-11-20]. If a town's death entry is missing or its stone is unreadable,
search the Charles R. Hale Collection's statewide index. Check the town's circa-1934
cemetery transcriptions for the inscription and its reported death date. In FamilySearch's Hale index,
check whether the hit points to a cemetery transcription or a newspaper notice.
[P214 @2026-11-20], [P215 @2026-11-20]

For an Iowa burial, search the 1930s WPA Graves Registration Project transcription that IAGenWeb
hosts at iowawpagraves.org. A Wayback Machine capture of 17 January 2026 lists 656,621 records from
82 counties and names the 17 counties the project never indexed: Appanoose, Benton, Cherokee,
Clinton, Dallas, Des Moines, Dubuque, Hardin, Humboldt, Ida, Iowa, Jasper, Lyon, Monona, Osceola,
Pottawattamie and Warren [P151 @2026-11-16]. In those counties a miss is a coverage gap; elsewhere
a miss leaves the individual burial unresolved. A presenter thought the WPA might have skipped Henry County [P150 @2026-11-16]; the captured county list gives 3,379 records there [P151 @2026-11-16]. Check the lists for the people they actually include: the Tama County transcription for Day Cemetery names Mary A. Blazer [P152 @2026-11-16]. Its contributor could not tell whether the workers read the stones or used courthouse death records or obituaries. Cite the WPA transcription and verify the entry against a stone, photograph or cemetery record.

German graves are reassigned after a rest period (Ruhezeit), and small children rarely received
permanent stones. A gravestone survey such as the CompGen Grabstein-Projekt
(grabsteine.genealogy.net) therefore under-represents older burials, above all infants and young
children from around 1900 and earlier. A missing child there is an expected gap, not a negative.
Do not rebuild a sibship from the stones. Take child deaths from the civil (Standesamt) or church
death and burial registers. [P53, P54]

Swedish and Danish graves are leased, so expect missing stones there too. A Swedish grave right
(gravrätt) now runs 25 years; older rights ran 50 years or in perpetuity. An unrenewed grave returns
to the cemetery administration, which takes the stone into its care, and the plot can be reused 25
years after the last burial. A Danish grave is cleared (sløjfet) once its protection period
(fredningstid) has ended and the lease is not renewed: the family may take the stone, the cemetery
may store it for a time, and unless it is registered as worth preserving (bevaringsværdig) it may be
discarded. An emigrated family left nobody to renew, so a missing stone there is weak evidence that
nobody was buried. Take the burial from the parish burial register and the cemetery's grave
register. Then check the cemetery wall or lapidarium, where some cemeteries keep selected older
stones. [P61, P62, P63]

For an Israeli burial, work from the burial society (חברה קדישא, chevra kadisha) that served the
place. Nationwide aggregators are incomplete:
MyHeritage's Israel grave collection, built with BillionGraves, covers 138 cemeteries and says it
does not hold every grave. [P40] So a miss there, in JOWBR or in Find a Grave is not a negative.
Find the society in the Israel Genealogy Research Association (IGRA) list of burial societies, which is based on
the Ministry of Religious Services lists, and ask it for the entry when contact is authorized. [P39]

Search the heritage inventory once for the burial ground and again for individual markers. In a 2022 MACRIS search, Plymouth’s Old Burial Hill survey was under `Burial Ground` and individual markers appeared under `Object` [P38]. Keep the category and locator for each item.

For a published necropolis or burial list, record what it was compiled from: cemetery documents
or monuments, or the death section of parish metrical books. Treat the two kinds as separate
sources and compare them where both exist. A list built from death entries records deaths in the
parish, not observed graves, though it may be the only option once a cemetery has been destroyed.
A highly selective compilation, such as the consistory lists described in the
[necropolis-list discussion](https://rodgersforum.borda.ru/?1-7-0-00000136-000-0-0-1774709430=),
is not a coverage test, so a name missing from it proves nothing. The thread reports no result
from comparing the two kinds.

Grand Duke Nikolai Mikhailovich published three necropolises in 1907–1914: «Московский некрополь»
(three volumes, 1907–1908, compiled by V. I. Saitov and B. L. Modzalevsky), «Петербургский некрополь»
(four volumes, 1912–1913, compiled by Saitov) and volume 1 of «Русский провинциальный некрополь» (1914,
compiled by V. Sheremetevsky). The provincial volume covers eleven guberniyas, among them Moscow,
St Petersburg and Novgorod, and the Valaam and Konevets monasteries; its preface says it was built
from the lists of people buried in churches and cemeteries that a Holy Synod circular of 29 November
1908 asked every diocese to send. [P100], [P101], [P102]

The Presidential Library shows volume 1 of each without login, and the Russian State Library's copy
of the provincial volume is in open access. [P100 @2026-11-13], [P101 @2026-11-13],
[P102 @2026-11-13], [P103 @2026-11-13]

For a Jewish burial in Vienna's Zentralfriedhof, check both Jewish sections, at Gate I and
Gate IV. Record the section with the grave locator. Use the Jewish Community of Vienna's
online burial database through 1945. A later burial lies outside that database's stated
coverage. [P205 @2026-11-20], [P206 @2026-11-20]

For a South African burial, open the province’s photo collection in **eGGSA Graves**. If the
locality is uncertain, also check **Location Unknown**. Keep the photographed inscription with
its gallery or cemetery heading and take a burial or kinship claim to the underlying record.
[P278 @2026-11-22], [P279 @2026-11-22]

For an Estonian burial, check whether the cemetery participates in Haudi before searching its
burials. Save the plot locator and open the cemetery map when supplied. A hit can come from a
cemetery book or a marker inventory. Record the basis if given and use the underlying entry or
stone to settle a conflict. A miss leaves an unrecorded burial or a lost source possible.
[P280 @2026-11-22], [P281 @2026-11-22]

According to Scott’s supplied transcript excerpt, a Chalmette headstone search can miss an
earlier interment or a burial without an individual marker. [P294†] For a Confederate prisoner
originally buried at Chalmette, check Cypress Grove Cemetery in New Orleans for the reinterment.
The National Park Service documents the transfer there and records mass burials at Chalmette.
Use a dated burial or transfer record to place the individual. [P295]

For a death in war or a veteran's burial, search the official registers, which governments and
war-graves bodies compile, each as its own surface. A miss outside a register's stated coverage
is not a negative.

- **CWGC Find War Dead** covers about 1.7 million Commonwealth service dead of 1914–1921 and
  1939–1947, and civilians killed by enemy action in 1939–1947. A record generally gives the place
  of burial or commemoration, and next of kin only in some cases. [P68, P69]
- **ABMC** lists Americans buried or commemorated in its overseas First and Second World War
  cemeteries and on its Walls of the Missing, with plot, row and grave for a burial. It does not
  include those brought home for burial, or any burial in the United States. [P70]
- **VA Nationwide Gravesite Locator** covers national, state veterans', other military and
  Department of the Interior cemeteries. It covers a private cemetery only where the grave has a
  government marker, and has no private-cemetery burials before 1997. [P71] Even within that
  coverage, a miss there is not a negative; see
  [us-20th-century-military-service-reconstruction.md](us-20th-century-military-service-reconstruction.md).
- **Volksbund Gräbersuche online** lists over 5.4 million German war dead and missing, mainly of
  the two world wars, with places of death and grave locations. About 450,000 names are still to be
  entered. [P72] For the Volksbund as a lead beside service records, see
  [german-military-record-period-routing.md](german-military-record-period-routing.md).
- **ОБД Мемориал**, the Russian Ministry of Defence database of Red Army losses in the Second
  World War and after, gives the original burial places of more than 5 million soldiers and
  officers. [P73] An original burial place can differ from the present grave after a reburial, so
  look for the present grave separately.

For a death in Finnish military service in 1939–1945, search Sotasampo’s **Menehtyneet** by name.
Keep any **Hautausmaa** (cemetery) value separate from the place of death. The linked cemetery view
draws on the same casualty data. Check the interment register or a dated transfer record before
assigning a grave. [P300 @2026-11-23], [P301 @2026-11-23] For a 1918 Finnish Civil War death, search
**Sotasurmasampo 1914–1922** and use the death details to narrow the burial search.
[P300 @2026-11-23], [P302 @2026-11-23] According to Kyläkoski’s excerpt, these services carry data
from the National Archives’ older casualty searches. [P299† @2026-11-23]

When you need a photograph of a military grave or memorial, search The War Graves Photographic
Project by name and match the cemetery and unit to the official register. Search beyond Commonwealth
casualties when the case calls for it. Record whether the photograph depicts a grave marker or a
commemoration. [P226 @2026-11-21], [P229 @2026-11-21]

For a U.S. veteran whose grave may be in a private cemetery or outside the United States, search
MyHeritage’s *United States, Veterans Burials*, which lists records from 1763 onward. Keep the
stated burial place, birth and death dates and any spouse name. Use the named cemetery to look for
an interment entry. [P250 @2026-11-21], [P252 @2026-11-21]

ABMC covers more than its First and Second World War cemeteries. Its Honolulu Memorial names 8,209
people listed as missing from the Korean War and 2,504 from the Vietnam War, and ABMC also
administers Mexico City National Cemetery, Corozal American Cemetery in Panama and Clark Veterans
Cemetery in the Philippines [P99 @2026-11-13]. Do not rule ABMC out for a missing service member of
those wars or a burial in those three cemeteries.

According to Katharine Andrew, DAR has a Revolutionary War grave marker index
[P211† @2026-11-20]. In the Genealogical Research System's Revolutionary War Records section,
use the **DAR Marker and Grave Location Index**. Search by the marker's locality when known.
The chapter state identifies the state of the chapter that placed the marker. A miss leaves the grave
unresolved because the index covers recorded reports from the 1890s to about 2005.
[P212 @2026-11-20]

According to Craig Scott, the Quartermaster records are a route to U.S. military cemetery
and headstone files [P216†]. In the Record Group 92 guide, search section 92.8.3 for the exact national
cemetery name and retain its date range. For post cemeteries in the Philippine Islands,
Puerto Rico or Cuba, use section 92.8.4 for the 1894–1917 reports and burial lists.
For the locating and marking of Confederate graves, use section 92.10.2, especially for
prisoners who died in the North. Distinguish a located grave from a name on a monument
commemorating people whose graves could not be found. [P217]

For a War of 1812 death, use the hospital or place of confinement named in the service
records to narrow the cemetery search. According to Craig Scott, local battle-cemetery
sites can supply leads in the Buffalo area [P224†]. For a death at the Williamsville
military hospital, check the Garrison Cemetery (War of 1812 Cemetery) in Cheektowaga.
Use the survey’s cemetery description and the hospital record as locators. A hospital
death alone leaves the individual’s burial place unresolved. [P225]

For an early U.S. government headstone in a private cemetery, route the search by the likely
application or order date. According to a supplied transcript excerpt, the presenter suggests
checking the Quartermaster files for an early marker [P172†]. For an application around 1910,
use Record Group 92, NM-81 entry 592, *Applications for Headstones in Private Cemeteries,
1909–1924* (National Archives ID 607866), arranged by state and county of burial. For an order
from about 1879 to 1903, check the card series M1845. Match the series to the date of the paperwork
and retain the series locator even when a database search misses. [P173]

For later applications, search Ancestry's *U.S., Headstone Applications for Military Veterans,
1861–1985*. Its description lists applications made in 1925–1963. [P191 @2026-11-18] For
M1916 (1925–1941) and M2113 (1941–1949), also search FamilySearch's *United States, Headstone
Applications for U.S. Military Veterans, 1925–1949*. [P173 @2026-11-18], [P174 @2026-11-18]
Search these series even for an earlier death if a later application is plausible. A miss in
the later collections leaves a circa-1910 application unresolved.

For a burial linked to a U.S. military post, camp or station, search FamilySearch's
*United States, Burial Registers for Military Posts, Camps, and Stations, 1768–1921*
(RG 92 microfilm M2014). If a name search misses, browse under the post. Check the remarks
for a removal and use its destination as a lead to the later grave. [P221 @2026-11-20]

For M1845 headstone orders, search FamilySearch's *United States, Records of Headstones of
Deceased Union Veterans, 1879–1903*. Copy the cemetery, grave or section if given, and
contract date. Use the cemetery fields to find the interment entry. Read the series years
as the headstone order period and retain the recorded death date separately. [P222 @2026-11-20]

Inspect the reverse of the 1925–1949 U.S. military headstone application. Record any service
entries, such as enlistment, unit or discharge, and any certification or stamps by image
number and side. If only the front is available, mark the reverse unexamined. According to
Scott's 2022 comparison, Ancestry displayed color in the copies he examined [P216†]. If a scan
obscures detail, compare the same application and side on both sites in the user's own account
where available.
[P173]

On a Soviet WWII mass grave (братская могила), check the name on the plate against the burial records. A 1965 Karelia plate drew on a military commissariat’s list of the dead [P94], and a Kaliningrad researcher reported names transferred between memorial lists without the remains [P93]. Under a 2023
Ministry of Defence letter, a soldier wrongly counted at a second burial is removed from its list
but his name normally stays on its plate. [P92] A user-contributed photograph of a plate, for
example on «Место памяти», shows only what is inscribed: record the contributor, date and page
locator. [P95]

For a burial in Russia, the record to check is the burial's passport (учётная карточка), the main
document for registering and identifying a military burial: the local administration drafts it and
signs it with the military commissariat, and each keeps a copy. [P92 @2026-11-08] Its named list
marks each person as «увековечен» (named on the plate) or «не увековечен» (not named), so absence
from the plate is not absence from the burial.

**Output:** `database | query | coverage checked | candidate URL | cemetery | section |
photo available | image examined | next source`.

**Check:** Distinguish a searched name, an included cemetery and an inspected inscription.

## 2. Search the recorded name fields separately

According to the supplied tutorial excerpt, Morton demonstrates broadening Find a Grave memorial and
cemetery searches using the available search controls. [P264† @2026-11-22] In **More search options**, enter a maiden surname in the surname field
and enable **Maiden name**. Run separate passes for the other options, such as similar spellings or a known spouse, parent, child or sibling.
Use `?` for one missing letter and `*` for zero or more. Add a cemetery location to narrow results.
Run a biography keyword as its own pass because it excludes entries without that word in their
biography. [P266 @2026-11-22] Where the burial ground is uncertain, open **Cemeteries** and search by name
or browse and zoom the map around the locality. [P267 @2026-11-22] Open a candidate cemetery and run separate surname
searches there for birth and married names, including for relatives absent from memorial links.
[P265 @2026-11-22]

If a common first and last name swamp the Find a Grave results, try the known distinctive
middle name alone. Compare the names and dates on any hit against the candidate’s records.
A miss leaves memorials that omit the middle name in play.
[P268]

For Manchester, use MyHeritage's *England, Lancashire, Manchester Burials* for entries from
1850 onward. Save the deceased's name and the stated date and place of burial. For parish
burials, search its separate Diocese of Manchester collection (1603–1910). The similar
titles and overlapping years cover different sets of records.
[P177 @2026-11-18], [P189 @2026-11-18], [P190 @2026-11-18]

For Oldham, compare a hit from MyHeritage’s *England, Lancashire, Oldham Burials*, announced with
burials from 1800 onward, with FamilySearch’s *England, Lancashire, Oldham Cemetery Registers,
1797–2004*. Use the FamilySearch registers for a 1797–1799 candidate. Keep death date and age
separate from the date and place of burial. [P236 @2026-11-21], [P237 @2026-11-21]

For Cumberland or Lancashire, search MyHeritage’s *England, Cumberland and Lancashire Burials* from
1728 onward. Record the place of death separately from the burial date and place. Use the named
burial place to follow the entry into cemetery or parish records. [P238 @2026-11-21], [P241 @2026-11-21]

For Stockton-on-Tees, search MyHeritage's Durham burial index from 1871 onward for the name
and stated date and place of burial. Check the council's burial register search as well.
Leave a miss unresolved. The council says its online entries are incomplete.
[P186 @2026-11-18], [P187 @2026-11-18], [P188 @2026-11-18]

According to the supplied interview excerpt, try the National Burial Index after a miss in an
index created by FamilySearch. [P292† @2026-11-22] In Findmypast’s **National Burial Index for England & Wales**,
search by name, year and locality. Keep the stated age, burial date and burial place. Check which
register or earlier transcription supplied the entry before treating a hit in another index as
independent. [P293 @2026-11-22]

For a French hit in MyHeritage's *France, Church Burials and Civil Deaths*, read the underlying
entry and label it as a parish burial or a civil death. The combined index gives the death
date and place. Take the burial place and date only from a statement about burial, and use the
death commune as a lead when the burial place is missing. Coverage varies by département.
[P180 @2026-11-18], [P181 @2026-11-18]

For Jewish deaths and burials in England, Wales, Jersey or the Isle of Man, search
MyHeritage's *United Kingdom, Jewish Death and Burial Records* (1733–2012). Record the full
name and stated death place, plus any birth date, death date or age. Check the JCR-UK
cemetery list for local coverage and shared submissions to JOWBR before counting another
hit as independent. Take the burial place from an explicit burial statement.
[P201 @2026-11-20], [P202 @2026-11-20], [P203 @2026-11-20]

If a Jewish grave search misses, search JewishGen's **Memorials & Plaques Database** for a
synagogue or society memorial. On a plaque hit, copy the deceased's name, civil and Hebrew
death dates, Hebrew name, parents' names, any cemetery ID and comments as supplied. Check
which name field matched. Use a cemetery ID to seek a burial record and keep the plaque as evidence
of commemoration. [P201 @2026-11-20], [P204 @2026-11-20]

For Stockholm, search MyHeritage’s *Sweden, Stockholm Burials* from 1773 onward. Use the stated
cemetery and burial date to choose a grave book in Hittagraven’s older indexes. Check the years
listed for that particular cemetery before using a miss. [P238 @2026-11-21], [P242 @2026-11-21],
[P243 @2026-11-21]

For a Paris municipal cemetery burial, search MyHeritage’s *Daily Burial Registers of Parisian
Cemeteries* and check its cemetery list, including the sites outside the city limits. In the
Archives de Paris, use the annual index and open the daily register by cemetery. Follow the
burial date or, if the index gives the death date, its entry number. Copy the grave location
and label the death and burial dates from the entry itself.
[P198 @2026-11-20], [P199 @2026-11-20], [P200 @2026-11-20]

For Santiago General Cemetery, search MyHeritage’s *Chile, Santiago Burials* from 1893 onward.
Retain the stated burial date and place. Test the cemetery before interpreting a miss for a death
elsewhere in Santiago. [P250 @2026-11-21], [P251 @2026-11-21]

When an East European Jewish stone has no surname, JOWBR documents searches using the deceased's
given name, the father's given name or the Hebrew Name field. Use the known locality to assess
the returned candidates; a common patronymic can produce many hits. [O1]

For an Eastern European database, inspect the form's native labels before entering the name.
The 2025 Pomnim example orders its boxes as surname, given name and patronymic; the Pogost example
adds gender and cemetery. Enter the supported native-script form rather than assuming that a
translated page has translated the database's names. Confirm the current form when executing
these older examples. [P3]

For a Russian municipal cemetery database, a result that shows only a count of matches
identifies no one: after a demand by Roskomnadzor (the federal communications regulator) dated
3 August 2026, Moscow's E-poisk shows only match counts. [P33] Search both е and ё spellings. If
a search matches fields exactly and caps the number of rows, split it by cemetery or year. If
dates come back as UTC timestamps, do not shift them yourself; keep the raw value and take the
calendar date from the card or the burial record. Treat a nationwide aggregator such as Pomnim
Online, which collects entries from users and organisations, as a copy: confirm the entry in the
local database and read the headstone photograph against the registry spelling. [P34] Recent
burials concern living relatives, so do not collect grave-holders' contacts. For a Russian death
with no burial hit, the notarial probate-case register is a separate locator; see
[soviet-personal-file-recovery § 3](soviet-personal-file-recovery.md#3-route-each-institution-to-its-series-and-present-custodian).

For a Riga burial, search cemety.lv by given name and surname; do not stop at BillionGraves or Find
a Grave. Riga City digitised data on about 800,000 burials in 13 municipal cemeteries and published
it there, and the site's region filter also covers many other Latvian municipalities. [P41, P42]
Citizens can submit updates and additions, so treat an entry as possibly amended by a user and
check it against the municipal record or the gravestone. [P41]

For a Lithuanian burial, search cemety.lt, Cemety's Lithuanian site. On 2026-11-12 it
listed 2,927 cemeteries and 1,915,979 deceased, searchable by name, cemetery and region and by
birth and death year with a tolerance of up to ten years, with an English interface
[P96 @2026-11-12]. The Ukrainian site, cemety.com.ua, then listed only 2 cemeteries and 3,953
deceased, so a miss there is not a negative [P97 @2026-11-12]. Vera Miller reports that entries
give the full name, birth and death dates, the cemetery and the grave's location, with gravestone
photographs [P98 @2026-11-12]. Read a hit against its photograph or the cemetery's own record.

For a Polish burial, do not stop at Find a Grave or BillionGraves either. Search Grobonet
(grobonet.com), a nationwide search fed by local cemetery systems. Then find the city's own
cemetery-administration locator by searching `[city] wyszukiwarka grobów` ('grave search');
Kraków, Warsaw and Wrocław, for example, run municipal locators. Coverage follows the
administrator or provider, so a miss is not a negative. Check a hit against the cemetery office's
record or the gravestone. [P55, P56, P57] For a Warsaw death in 1945, the Polish Genealogical
Society's obituary index (nekrologi.genealodzy.pl) covers the notices printed in Życie Warszawy
that year; each hit gives the issue, date and microfilm reference. [P58] For a former German
cemetery now in Poland, search the Grabstein-Projekt (section 1); it covers selected cemeteries,
not all of them. [P59]

For a Canadian burial, also search Canadian Headstones (canadianheadstones.ca), a collection of
headstone photographs and transcriptions from cemeteries across Canada, by first or last name
[P121 @2026-11-14], [P139 @2026-11-14]. Middle names sit in its first-name field, so enter
`John%` rather than `John`; `%` is its wildcard elsewhere too, as in `M%Donald` for McDonald or
MacDonald. Its menus also offer Overseas Canadian Headstones and a cemetery lookup
[P139 @2026-11-14]. Records are submitted and transcribed by contributors, so a miss is not a
negative; read a hit against its photograph [P121 @2026-11-14], [P139 @2026-11-14].

For a Queensland burial, also search MyHeritage's Australia, Queensland Funeral Home and Burial
Records, which MyHeritage's wiki listed with 633,015 records on 2026-11-16 [P157 @2026-11-16].
MyHeritage describes it as an index of funeral-home and cemetery burial records whose entries
typically give the full name, age at death, burial date, burial place and notes, each marked as
coming from a funeral home or a cemetery [P156 @2026-11-16]. Record that marking with the hit. A
cemetery record normally names the cemetery and the Queensland town; a funeral-home record generally
names only the town [P156 @2026-11-16]. Read a funeral-home result's burial place as a town, not a
cemetery, and take the cemetery and plot from the cemetery's own record (Section 4). The
description names no date range and no contributing firms or cemeteries, so a miss is not a
negative.

For Rockhampton, use MyHeritage’s *Australia, Queensland, Rockhampton Burials* from 1864 onward
alongside the Regional Council’s cemetery indexes. Search North and South Rockhampton separately
when the cemetery is uncertain. Record age and death date apart from interment date and cemetery.
For 1858–1864, check the council’s listing for the separate Rockhampton Court House records. [P238 @2026-11-21], [P239 @2026-11-21], [P240 @2026-11-21]

For a Hart Island burial, check MyHeritage’s index, which describes entries from 1872 onward,
and the city’s **Cemetery Management Tracking System**, which starts in 1977. Keep the place
and date of death separate from the interment. Use the Medical Examiner number if available and
carry a supplied plot number to the city’s plot map. A fire destroyed some burial records, so leave
a miss unresolved. Record the circumstances of public burial only when a source supplies them.
Families could choose public burial for a claimed relative.
[P274 @2026-11-22], [P275 @2026-11-22], [P276 @2026-11-22], [P277 @2026-11-22]

For Denver’s Riverside Cemetery, search MyHeritage’s *Colorado, Denver, Riverside Cemetery Burials*
and Denver Public Library’s *Riverside Cemetery Burial Register Index, 1876–1963*. The library dates
the first interment to 1876. If a MyHeritage hit gives an earlier date within its advertised
1855–1963 span, check for an earlier burial elsewhere or a later transfer and take the Riverside
burial date and location from the cemetery evidence. [P238 @2026-11-21], [P244 @2026-11-21], [P245 @2026-11-21], [P246 @2026-11-21]

For Walnut Hills Cemetery, search MyHeritage’s *Ohio, Hamilton, Cincinnati, Walnut Hills Cemetery
Burials* from 1843 onward. Preserve the reported birth place, birth, death and burial dates and any
parent or spouse names. Route Spring Grove and Oak Hill candidates to *Ohio, Hamilton, Cincinnati
Burials*, which covers those cemeteries from 1845 onward. [P238 @2026-11-21], [P247 @2026-11-21],
[P248 @2026-11-21]

For Norfolk, Virginia, start with the city’s **Search Burial Records** for its eight municipal
cemeteries and retain the stated burial cemetery and any mapped grave location. Use the *Virginia,
Norfolk Burials* index named in MyHeritage’s 2023 announcement as an additional lead when accessible
in the user’s account. Keep burial and death fields separate. [P238 @2026-11-21], [P249 @2026-11-21]

To list the relatives the FamilySearch Family Tree places in one cemetery, open the cemetery in
FamilySearch's Cemeteries search on the website (the mobile Family Tree app lacks it), signed in
with the user's own account, and click **Only show my relatives**; only people in the Family Tree
appear [P122 @2026-11-14], [P140 @2026-11-14]. The list is tree data, not a burial record: open
each person's own burial source. A relative missing from it is not a negative. Users report that
the filter left out a relative by marriage buried beside a blood relative, that a relative whose
profile had an attached Find a Grave record never appeared in the cemetery's list, and that a
relative can be listed under a duplicate profile not linked to the user's tree
[P141 @2026-11-14].

**Output:** a query row for each field combination, retaining the exact entered strings and
the candidate record links.

**Check:** A search expansion supplies candidates; it does not equate a Hebrew patronymic with
a civil surname or identify the father.

## 3. Preserve the photograph and both inscriptions

Open the available photograph and save its URL, cemetery and plot information. Keep any permitted
original image separate from a working crop or adjusted reading copy. Record which image was
actually inspected. On a memorial site, open every gallery image at its original size (on Find a
Grave, **View original**). A main photo may be cropped to one name and hide a spouse on the same
face. Record a cropped image as a partial view of that face. [P66, P67]

A memorial's gallery can hold more than the stone: sites where volunteers photograph headstones
can also carry the person's portrait and a picture of an obituary clipped from a newspaper
[P153 @2026-11-16]. On Find a Grave the uploader marks each photo Grave, Person, Family or Other,
Other being generally a document or record, and the uploader's profile name shows beneath it as
**Photo added by** [P154 @2026-11-16], [P155 @2026-11-16]. Open every type, not only Grave: the
type is the uploader's choice. Record a clipping as the uploader's copy of an obituary, with the
newspaper title and date only where the clipping or caption shows them, and find the printed notice
before citing it as the obituary. Record a portrait as the uploader's attribution, not an
identification, and do not compare faces. A Family photo can show living relatives: note that it
exists without identifying them.

Keep four things apart: the database entry, the photograph, your own transcription of the
photograph, and any epitaph that a publication, memorial page or family compilation quotes. A
database's name, father's-name and date fields are its statement about the burial, not a reading
of the stone, even when a photograph is attached. A transcription the database supplies is someone
else's reading, like a quoted epitaph. Read the photograph blind first: transcribe what is legible
and mark what is not before you look at the database fields or a quoted epitaph. If you saw them
first, say so beside your reading: it is then not blind. Then set the other readings beside yours
and mark each of their words as shown on the photograph, contradicted by it, or not visible in it.
A word that only the database or the quotation supplies stays attributed to that source and is not
reported as part of the inscription. Not visible is not absent: the word may be eroded, on a face
not photographed or outside the image.

At Săpânța's Merry Cemetery, record the painted cross’s carved scene and epitaph separately.
Use a depicted activity as a lead for an occupation search. Confirm the occupation in a
record independent of the carver’s depiction. [P205], [P207]

Before using the comparison, check that the attached photo actually shows the target's
marker. If the name or plot evidence points to a different marker, log the attachment as
a mismatch. Read doubtful letters and symbols against the carving. Preserve even apparent
errors in the literal transcription and keep proposed corrections in the research notes.
[P160]

Preserve each face’s carved line breaks in the literal transcription. If a field takes only one
line, mark each line break with `/`. Keep apparent spelling and date errors as carved, with any
proposed reading or correction in the notes. [P226], [P230]

If her inscription reads only ‘Mrs. [husband’s name]’, transcribe the designation as carved
and keep the birth and death dates separately. Leave her given and maiden names unresolved.
Use the husband’s name as a search lead in the census and check the household against the
burial evidence. [P193]

For a Polish immigrant buried in the United States, inspect the stone and cemetery record
for an exact village of origin. Preserve the spelling and the place's stated role. Use a named
village to choose candidate parishes and check the lead in the immigrant’s U.S. parish
marriage or baptismal records. [P197]

Treat the birth name and birth date on the stone as leads when the informant's firsthand
knowledge is unknown. An accurate memorial transcription still carries the same inscription
claim. Check those details against a birth or baptism entry where available. [P160], [P163]

Record the pixel width and height of each image you read, and what was and was not legible at that
size, for example `1200 × 900 px; given name and month-year legible; father's name eroded`. Read
the largest copy available, not a thumbnail. A word that cannot be read in a small or compressed
copy is unread, not missing from the stone. An AI model may receive a smaller image than the file;
see [ai-for-documentary-records](ai-for-documentary-records.md#the-pitfalls-worth-internalizing-the-least-obvious-most-llm-usable-part).

According to the Family Tree Magazine cemetery segment, try inverting the colors of a photograph of
faint lettering. [P231†] Use a local working copy and check the reading against the original. Label
each reading by image and mark any still-doubtful letters. [P226], [P232]

Record whether anyone outlined the inscription before photographing it. Compare a doubtful letter with an untreated image if available and label each reading by its image. In a matzevah discussion a reader proposed that an apparent מ was the traced ה of צנועה [P17]. Without an untreated image, record the expected formula as a reason to recheck the carving.

For a difficult inscription, an optional second photograph uses light directed from the side
by a hand-held reflector or flashlight, held clear of the marker. Keep the ordinary-light and
side-lit views together, label the surface and lighting, and leave uncertain letters unresolved.
This step does not involve rubbing, cleaning, wetting or touching the marker. [P27]

Record which faces of the stone, and of any family monument, the images actually show: front, back,
sides and any lower additions. A spouse, a second burial or a list of children can appear only on
the back. On a Jewish stone, the back can carry the Hebrew name and patronymic, while a
memorial-site photograph may show only the English front. Mark an unseen face `not examined`, not
absent, and queue a request for its photograph. Label the surface each image shows and keep
unreadable parts explicit. [P26] Do not record a person as absent from a marker after only one face
has been inspected. The [family-cemeteries video](https://www.youtube.com/watch?v=rA5-uq548q4),
[cemetery photographs tips](https://www.youtube.com/watch?v=7zW86N6q4Yc),
[cemetery steps session](https://www.youtube.com/watch?v=crq_j9WnVn8) and
[Lil Dicky tree session](https://www.youtube.com/watch?v=SKDoU7MJkds) motivate this. A name on
another face does not by itself establish burial at that spot or a relationship, and the back may
carry nothing.

On an authorized visit, photograph every accessible face and any smaller inscribed detail even when
writing the transcription on site. Check for footstones, cornerstones and enclosures. Record damage
and visible repairs with the affected face so later readings can be checked against the right
feature. [P226], [P230]

When a monument has an inset or added plaque, transcribe the original stone, the inset and
any maker’s mark on the enclosure under their own photo locators. Label a named maker and
place with the object they identify. In the Fasty survey, a Russian dedication surrounded
a Polish plaque naming a different set of people as buried there. [P290] Read each
surface’s burial statement on its own before checking the interment register. [P230]

When reading Polish and Lithuanian names in a burial group, retain each spelling as carved
and log any supplied variant separately. Repeat the search with both forms and include nearby
family stones outside a language-specific survey’s selection. A Pivašiūnai survey omitted a
stone it found because the surname was written in a Lithuanianized form. [P291]

For each person named on a family monument, retain the literal burial-place statement and its
image/surface locator separately from the monument's physical cemetery and plot. A family
monument can name people buried elsewhere; compare their location statements with available
burial records instead of assigning everyone named on the monument to its plot.
Unresolved burial locations stay open. [P26]

For a marker built into a wall or laid as paving, record its observed location and look for a
heritage survey or earlier description that traces its previous setting. Leave the grave location
open until burial evidence places the remains. [P287] The 1600 Mościcki slab in the church
vestibule at Jabłonka Kościelna had reportedly served as paving after the family chapel at
Tybory-Kamianka was demolished. [P285] [P286]

In a columbarium inscription, record a stated place of origin and any permitted destination
for a future transfer in their stated roles. Look for a dated record of an actual transfer before
changing the interment location. A published selection organized around stated origins can omit
people whose plaques give no origin. Keep the burial open and look for a fuller inventory or the plaques themselves.
[P288]

A name cut on a stone before that person died records where they meant to be buried when the
stone was set, not a burial. A couple's stone put up at the first death, or a stone bought at a
child's death that also names the living parents, can leave a survivor's death date blank or
part-cut (`19__`). That blank shows neither that the person is still alive nor that they lie
there: they may have moved, divorced or remarried and been buried elsewhere, been cremated, or
died with nobody to have the date cut [P111], [P112], [P113], [P114], [P144]. Record the burial
as unresolved until an interment entry or other burial record places it. Until a death record is
found, treat a survivor who could still be alive as a living person [P144].

A widow named beside her first husband may appear in later census, death and burial records only
under a later husband's surname, so search for her under each later married name [P110], [P112].
One person can have a stone with each spouse in different places while lying under only one.
Look for the other stone, and record each stone's wording apart from the place of burial
[P115], [P145]. A death certificate's burial-place field is a lead to the cemetery, not the
interment record (Section 4): settle the burial with that cemetery's interment entry.

Many 20th-century monuments in the former Soviet Union carry a portrait of the deceased: a
photoceramic or enamel medallion, or a photograph under glass or plastic. [P30, P31] A grave
photograph is then also a person photograph. Record the portrait as attributed by the inscription
on the same monument, never identified by face, and never compare it with other photographs.
Repeated photographs of one monument are one chain for its inscription and portrait, not
independent confirmations.

For supplied cemetery-visit photographs, retain an actual cemetery-sign photograph as a
context image and link it to the corresponding grave-photo IDs using the supplied visit
notes or other documented association. On an authorized future visit, photographing the
cemetery sign first can help preserve this context. If no such image was supplied, record
it as absent; do not invent a sign image or assume that every adjacent camera file belongs
to that cemetery. A sign identifies the photographed place, not the person or burial. [P24]

Before surveying multiple graves, sketch the natural rows against fixed features such as fences,
paths or trees. Work section by section in row order, number the rows and assign each monument a
unique survey code. Use that code on the sketch, photos and transcript, keeping survey codes
distinct from official plot numbers. [P226], [P230]

If dictating inscriptions during an authorized visit, state the monument code and face first, then
say and spell each name and repeat each date. Record and transcribe the audio on the user’s device,
and check the transcript against the photographs before entering names or dates in the packet.
[P226]

Read any wide shot of a row or section in a supplied photo set as well as the close-ups. It
records where stones stand relative to one another and can show a stone with the target surname
that nobody photographed close up [P119], [P149]. Log such a stone as `seen in wide shot, not
photographed` with the image ID, read only what is legible at that size, and queue a close-up
or a return-visit item. On an authorized visit, photograph each group of graves together before
the single stones [P149].

For a bilingual stone, transcribe the Hebrew and secular-language portions separately. The
gravestone tutorial demonstrates the deceased's Hebrew given name and the father's Hebrew name
as useful leads that can be absent from the secular portion. Preserve the raw wording, the
person's stated role and uncertain letters before adding a translation. Do not require every
stone to contain the same fields. [P1, O1]

On a short formulaic Hebrew epitaph, transcribe the descriptor before the name as its own field:
for example איש or אשה, הבתולה (maiden), הבחור (young man) or הישיש (old man). Use it as a possible
life-stage or marital-status clue when comparing candidates. Keep the literal term when meanings compete: readers proposed both ‘groom’ and ‘young man’ for החתן on one matzevah [P17]. Leave exact age and marital status open.

Before treating a word on a Hebrew stone as a surname, check whether it is a status or occupation
marker, such as כ"ץ for a kohen, הלוי for a Levite, or, less certainly, שו"ב for a ritual
slaughterer. Record the literal letters and the proposed expansion separately. Assign the title to
the man it follows: after a woman's patronymic, it describes her father, not her. Try to find the
person in the locality's records for the period by given name and father's name rather than by the
apparent surname. The [matzevah-reading discussion](https://forum.j-roots.info/viewtopic.php?f=208&t=9621)
and [title question](https://forum.j-roots.info/viewtopic.php?f=75&t=7576) motivate this. כ"ץ (Katz) can be a real surname in other contexts, and neither thread proves an identification. A conflict such as
'bar' followed by a female name stays unresolved until the image is checked.

Transcribe ר׳ or ‘Reb’ as an honorific. Check ‘Rabbi’ or ‘Rev.’ against evidence for ordination and for the work the person performed. Community histories quoted for one man described as ‘Rev.’ identified him as a ritual slaughterer and teacher [P20]. Record those roles separately and leave ordination open where the sources are silent.

Do not expand ב"ב as the city of Bnei Brak by default. The abbreviation has many expansions, among
them בני ביתו ('his household'), the Talmud tractate בבא בתרא (Bava Batra), בעל בית ('householder')
and בן בנו ('his grandson'). [P48] In a rabbinic citation, test the tractate first [P49]; after a
person's name in a greeting or dedication, test 'his household'. Read it as Bnei Brak only when the
context is clearly a modern address; otherwise the family gets a false residence.

Keep the dates separately:

| Field | What to retain |
| --- | --- |
| Death date on inscription | Literal English/secular and Hebrew forms, each with its label |
| Age at death on inscription | Literal value and stated units, linked to the inscription's death date; missing units stay unknown |
| Calculated birth-date lead | Separate derived value, input death date and age, calendar and arithmetic; label `calculated, not stated` |
| Burial date | The date explicitly supplied as burial, with its source |
| Database date | Displayed value, field label and record URL |
| Photograph date | When the image was taken, if stated, and separately when it was posted, each with its source |
| Converted date | Separate derived value, calendar and conversion basis, if checked |
| Unreadable or absent value | Unknown; no guessed completion |

The death date that a record or database gives, the burial date, the date on the inscription and
the photograph's date are four different statements, and any of them can be unknown. Keep each as
its own labelled date with its source, and leave an unknown one empty, in the packet and in any
tree entry made from it. Do not fill a missing burial date with the death date, the inscription's
date, or the date the photograph was taken or posted.

**Check:** An unread inscription, missing date or unverified conversion stays unknown. The
packet records the source statements and does not select a final death date. [P1, O1]

When an inscription dates the death by a festival day or its abbreviation, such as אחש for the
last day of Pesach, expand it to the Hebrew calendar day before any Julian or Gregorian
conversion. Keep the literal phrase, the expansion and the reference used as the basis in the
Converted date row. Check the day against the community's festival practice, and convert only when
the year has been read. Do not replace the phrase with an approximate 'around Passover'. The
[festival-date discussion](https://forum.j-roots.info/viewtopic.php?f=208&t=9621) motivates this
with one abbreviation glossed by a link. It sets no conversion rules.

Read how a Hebrew year is written before converting it. לפ"ק (לפרט קטן, 'by the small count')
marks a year written without the thousands, so תשי"ח לפ"ק is 5718. [P44, P46] The numbers 15 and
16 are written ט"ו and ט"ז, not י"ה and י"ו. [P44] The Hebrew year begins in Tishrei: subtract 3761
for a date from Tishrei to 31 December and 3760 for a date from 1 January to the end of Elul.
1 Tishrei 5718 fell on 26 September 1957. [P43, P45] A year read without its month therefore
spans two civil years (5718 gives 1957 or 1958): record the span in the Converted date row, not
one year. In a leap year a bare Adar is ambiguous unless the stone says Adar I or Adar II; keep
both candidate dates. [P45, P46] נלב"ע expands to נפטר לבית עולמו ('departed to his eternal
home'). [P47]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Calendar conversion sends the deceased’s transcribed Hebrew date to JewishGen. Answer the privacy gate in `SKILL.md` before submitting it and keep names, images and other details local.

For a legible Hebrew day, month and year, use JewishGen’s standalone
[Calendar Converter](https://jewishgen.org/JOS/josdates.php). Submit only those three fields.
Keep the Gregorian result in the Converted date row beside the literal Hebrew date and preserve
the inscription’s event label. [P306 @2026-11-23], [P307 @2026-11-23]

A Hebrew day begins at sunset. Converters return the civil date of the daytime part, so a death
after sunset may have fallen on the civil evening before the converted date: keep both civil dates
unless the time of death is known, and compare each with the civil record. [P74, P75] Most Hebrew
stones give the date of death, after נפטר or נפטרה ('died'); some older European stones give the
date of burial instead. Note which word the date follows before you label it a death date. [P76,
P77]

When an inscription supplies a death date and age in years, months and days, retain both
literal inputs before calculating a birth-date lead. Amy Johnson Crow's example counts
back the years, then months, then days, carrying the year and using the actual length of
each month crossed. Record that arithmetic and its calendar basis with the calculated
value. Incomplete age units, an uncertain calendar or unresolved month-end/leap-day
conventions do not support a unique exact birth date; leave the calculation unresolved
where its basis is missing. The recorded age may itself be inaccurate. Keep a separately
stated birth date alongside the calculation and send a conflict to evidence and proof
judgment, rather than overwriting either value. [P23]

If a source reports reinterment or a replacement marker, retain original burial, reported
transfer and later marker installation as separate source-linked events. Keep original and
present cemetery/plot locators separately; seek the relocation or register evidence for an
unresolved transfer. George Estes’s 2023 marker dedication was announced for Oak Ridge Cemetery, but the transfer of his remains is reported in family accounts [P35].

Transcribe ‘woodman of the world’ or ‘Dum Tacet Clamat’ as carved and use it to look for
Woodmen of the World membership. Seek an explicit membership statement in contemporary
death or funeral coverage. A tree-stump shape alone leaves the affiliation unresolved.
[P209], [P210]

For a U.S. government headstone, distinguish the pointed, shieldless Confederate design
from the rounded Civil War–Spanish War design used for Union veterans. Use the shape to
label the design and check the inscription and service record for the veteran’s allegiance
and unit. [P223]

When a volunteer transcription runs a company letter into a regiment number, compare the upright
character with adjacent letters and digits on the stone, then test the candidate unit and company in
the service roster. According to Scott’s reading, `Company 113th Wisconsin Infantry` could be split
as `Company I, 13th Wisconsin Infantry`; use the National Park Service’s 13th Wisconsin Infantry
entry to check the unit name. [P255†], [P256]

When one grave has a family stone and a commemorative marker, such as a military marker a society
placed later, record each date with the marker it comes from, who placed it and when. Record
lettering cut later, such as sandblasted text beside raised original lettering, as a later
addition. A date conflict between markers stays an unresolved discrepancy (Section 5). [P66]

For a name on the Great War memorial along boulevard de Ménilmontant at Père Lachaise, record the
monument as commemoration of a Parisian death or disappearance and seek a separate burial record
before assigning a grave. [P233], [P235]

For a U.S. government marker, look for the memorial designation `IN MEMORY OF` [P176]. A relative reported a Maryland veterans’ cemetery tablet for a sailor lost at sea aboard USS *Cyclops* [P175]. Record the memorial site separately and seek a disposition record before assigning a place of burial.

Date a stone independently of the deaths it records. One researcher found court records dating a stone to 1906 for a relative who died in 1888 [P116]. An Irish family stone may record deaths several decades after the event from relatives’ recollections [P117], [P142]. Check its dates against a census, civil death registration and burial register, testing even a death inscribed as 1899 against a possible 1901 census entry for the same person [P117]. For the marker’s purchase or erection, check estate or court accounts, cemetery burial or memorial registers, and funeral-home files [P116], [P143]. Record an unknown erection date as such.

In a damaged or cleared cemetery, compare the present enclosure with any dated map of its former
extent. Record the areas outside the boundary as lost or not examined, so that a missing stone is
not read as absence of burial. For a stone recovered from a pile or dump, or reset in a special
row, record where it was found, the project's stone number or marking, and whether the reset spot
is reported as its original place. A displaced stone's present position does not locate the grave
and supports no neighbour inference. The
[cemetery-restoration discussion](https://forum.j-roots.info/viewtopic.php?f=208&t=9621) motivates
this. It does not show how original positions were determined, and its burial-count estimate is
simple arithmetic.

## 4. Carry the hit to the plot and cemetery records

Save the cemetery's name, address, section and plot exactly as supplied. JOWBR's full record or
cemetery link can provide cemetery contact information and maps. A BillionGraves photograph may
have GPS information; the cemetery-program tutorial demonstrates using its map to locate a
marker. Record a supplied coordinate as a coordinate, and a section/plot reference as a separate
locator. [P2, O1]

To check a Find a Grave location, look for the same marker on BillionGraves. Match the carving
and marker before comparing the cemetery or any GPS point, and log the source of each locator.
BillionGraves distinguishes GPS headstone records from photos without coordinates. A shared
photo counts once for what is visible on the stone. [P160 @2026-11-18], [P161 @2026-11-18]

On a Find a Grave memorial page, use **Show Map** when available to inspect the contributed
marker location. GPS can be added separately from a photo. Read **Add to Map** as a prompt to add
coordinates, and check the photos separately. Confirm a plotted point against the section and plot
reference before using it on a visit.
[P258 @2026-11-22], [P260 @2026-11-22]

For an Arlington National Cemetery hit in MyHeritage, retain the interment date separately from
the death date. Save the service details and whichever locators appear, including a court, column
or niche for a columbarium burial. Open the cemetery’s **ANC Explorer** to check the locator
and both headstone faces where available. The MyHeritage collection comes from Arlington, so
matching entries there and in ANC Explorer can share a source.
[P272 @2026-11-22], [P289 @2026-11-22], [P273 @2026-11-22]

If the section or plot is unknown, inspect the posted gravesite photos for the marker's
position in the grounds and its size relative to nearby stones. Use those features to choose
where to look on an authorized visit. Match the inscription before assigning the plot. [P209]

If a form can capture the device's current position, use that control only while physically at
the intended site. When entering information off-site, leave current-position capture unused.
Retain where the coordinate came from and what point it represents; keep an independently
supplied coordinate with its source instead of replacing it with the contributor's location.
Unknown point meaning stays unresolved. The dated Cemetery Registry demonstration motivates this
capture-origin check, not a guarantee of coordinate accuracy, grave identity or access. [P25]

If the death municipality in France is known but the cemetery is not, check whether its archival
descriptions list `registres des convois funéraires` or `registres des transports de corps` for the
relevant period. A Paris transport entry of 27 December 1955 gave Vignot in the Meuse as the destination for Victor Grandsire, four days after his death [P28]. Copy the date and destination, then seek the interment entry and plot at the receiving cemetery.

For a Père Lachaise ossuary reference, use the name recorded at deposit to trace the cemetery of the
former concession and search that cemetery’s daily burial register. Section 1.2.2 of the 2014 Paris
municipal audit identifies documentation of deposits from reclaimed concessions at Père Lachaise and
at the cemetery of origin. Record the deposit and earlier burial separately. [P233], [P234], [P200]

To trace a U.S. service burial or transfer in the World War I era, look in RG 92,
NM-81 entry 1942, *Burial Case Files*, 1915–1939 (National Archives ID 595318).
Check for scans in the catalog by name, including surname group files when present.
Read reports, applications, letters and telegrams for the temporary burial, the next of kin's
choice of return home or permanent burial in Europe, and the actual transfer or reburial. Use the
**Report of Disinterment and Reburial** and any shipment papers to follow the remains
to the final cemetery. Keep a requested destination and the completed transfer separately.
[P173], [P218], [P219]

For an early military burial routed through Manila, use the post-cemetery papers in RG 92
to trace the death, temporary plot and shipment separately. According to Scott,
the route through San Francisco continued to the next of kin [P216†]. Follow the documented
route to the receiving cemetery. Treat a port or next-of-kin destination as a transfer locator.
Leave final burial unresolved until a burial record places it.
[P217], [P220]

When the plot cannot be located or the online entry lacks detail, identify the cemetery office
and prepare a request for the recorded burial and its plot location. The gravestone tutorial
recommends asking the office before visiting. Give the candidate name, known date, cemetery and
any existing locator; request the corresponding register entry or available burial information.
Send the request only when contact is authorized. [P1]

Before treating a missing or unfindable marker as a wrong lead, ask the cemetery office about the
grave's type and status when contact is authorized. Is it a war grave? Was the stone removed, for
example as unstable? Record any reported grave status and the current section, row and number
beside the original locator. If the office reports an anonymous interment, ask for the recorded
field. A Berlin cemetery inquiry located a surviving war grave by section and row; in a separate anonymous-burial inquiry the discussion suggested asking for the field but recorded no answer [P19]. Log the locator the office actually provides.

For a civil burial permit in Spanish-language records, search the jurisdiction’s finding aids
under the locally used term. Try `pase de sepultación` for Chile or `licencia de enterramiento`
for Spain. Search alongside the civil death registration. Compare the permit’s death details against that entry. If the permit names
the intended cemetery, use that name to find its interment register and check whether burial went
ahead there.
[P282], [P283], [P284]

Custodians may produce only what is asked for by name. Request each record type separately:
interment register, plot purchase or deed, burial or grave-opening permit, transit permit,
funeral-home case file, and any sexton notes or folders. Log each as requested, produced or
reported absent. Where registers run in interment order, search a reinterred burial under its
removal date, not the death date. A plot owner, purchaser or payer is a relationship lead, not a
burial or proven kin. The [death-records class](https://www.youtube.com/watch?v=70ya-VPbkBc),
[cemetery-records class](https://www.youtube.com/watch?v=th8_R6cKTnw),
[funeral-home talk](https://www.youtube.com/watch?v=ybuFUjhcwok),
[sexton-notes episode](https://www.youtube.com/watch?v=7JQcEHgDwxs),
[plot-purchase distinction](https://www.youtube.com/watch?v=gG5ZL8ueNx4) and Mount Moriah
interviews ([2020](https://www.youtube.com/watch?v=WoBE9ZAMsg4),
[2024](https://www.youtube.com/watch?v=gLXeAlkY6j0)) motivate this. They are US examples, and
record survival and arrangement vary.

Identify the series and column headings before interpreting a cemetery index's name and
date. An entry in a lot sale register can name the purchaser and date of purchase, as in
Boston's Evergreen Cemetery records. Carry those fields to the interment record by lot or
grave number. Keep the purchase and interment as separate events. [P180], [P185]

For Brooklyn's Green-Wood Cemetery, use MyHeritage's burial collection (1840–1937) to recover
the burial number, lot number and funeral director where shown. Use the burial number to
identify the entry and the lot number to locate the plot. Keep the undertaker as a separate
record lead. The cemetery's own online burial search may show the date of interment at the
current grave after a move. Check the register for the earlier interment before using that
date for the original burial. [P180 @2026-11-18], [P182 @2026-11-18],
[P183 @2026-11-18], [P184 @2026-11-18]

Address each request to the body that holds that record. In the United States the usual holders
are:

| Record | Usual holder or issuer | What it shows |
| --- | --- | --- |
| Church burial register | The church, parish or its archive | The burial service; the person may be buried elsewhere [P78] |
| Interment register; lot or plot-ownership books | The sexton or cemetery office; for a public cemetery, the town or county, or in some states, such as Utah, the state archives [P79, P80] | Burials, and separately who owned each plot |
| Burial, removal or transit permit | Issued under state law; in California, through a funeral establishment or the local vital-records office [P81] | Permission to bury, cremate or move the body |
| Funeral-home case file | The firm or its successor; some collections were given to libraries, archives or societies [P82] | Private business records, kept at the firm's discretion |

If a U.S. burial permit is missing from the cemetery’s records, check the county court’s records for
a permit series covering the place and period. According to Scott, permits are one target for
courthouse research. [P253† @2026-11-21] For Wicomico County, Maryland, route a 1900–1911 search to
the Maryland State Archives’ Circuit Court burial permit series T4244, paper unit T4244-1. [P254 @2026-11-21]

Permit rules and record survival vary by state and period.

**Privacy gate:** <!-- privacy-gate: contact --> A search request to a council, church, record office or Friends group names the deceased and the burial place and discloses the user's research interest; answer the privacy gate in `SKILL.md` before you send it.

**Privacy gate:** <!-- privacy-gate: contact --> A former cemetery inquiry shares the historical site locator and the user's research interest with a local heritage group or a resident the user already knows. Use an authorized contact route and answer the privacy gate in `SKILL.md` before sending.

For a former Jewish cemetery at Borșa, Maramureș, look for the illustrated map in the
*Memorial Book of Borsha* and compare it with the accounts of the three cemeteries on
pages 49–50 [P208]. When contact is authorized, ask a local heritage group or a resident
the user already knows whether a cemetery used to stand at the mapped site.
Keep the site as a candidate when no complete marker is visible, as Horowitz reports
that an exposed fragment at Borșa turned out to be part of a tombstone with a legible
inscription [P205]. Record any inscription visible on an authorized surface inspection
and leave partly buried stones undisturbed.

In England and Wales, the registers of a council-run cemetery are held by the council's
bereavement service, often called Cemeteries and Crematoria ('Cems and Crems') or Bereavement
Services; find it by searching either name with the town [P105 @2026-11-14],
[P125 @2026-11-14]. A privately owned cemetery keeps its own records [P105 @2026-11-14]. Older
registers may have been deposited in the local archive instead: Sheffield Archives hold the
city's civil cemetery registers from 1836 to the late 20th century [P128 @2026-11-14], and
Gloucestershire Archives list the cemetery records they hold [P126 @2026-11-14]. Search a
published register first where one exists, such as Birmingham's, digitised to 2014
[P125 @2026-11-14].

Otherwise ask the council's bereavement service to search its registers for the grave number and
section, giving the name, the date of death and the cemetery, as Leeds asks [P105 @2026-11-14],
[P123 @2026-11-14]. Many councils charge for a search: on 2026-11-14 Leeds charged £47, with no
charge when no location is found, and Wirral £64 [P123 @2026-11-14], [P124 @2026-11-14]. Leeds
has no computerised records before June 1987, and many of its records are not indexed
[P123 @2026-11-14], so a failed council search means not found, not no burial.

Read what the cemetery register itself records before you order a death certificate. Registers
vary by cemetery and period, and some early ones hold less than later ones [P109], [P126]. Most
of those Gloucestershire Archives describe give the name, age, occupation, burial date, minister
and grave number, and some the date and place of death [P126]. York Cemetery's give the grave
type, dates of death and burial, residence, cause of death, the person who arranged the burial and
the officiating minister [P108], [P129]. Its
'informant' column names that relative, executor or undertaker, not the informant of the civil
registration [P129]. Record which fields the register has. It is a burial record, not the civil
death registration: where it lacks a field you need or its date conflicts, the certificate is
still the record to get [P108], [P109].

Read the section and the grave type too, not only the location. Under the Burial Acts, part of a
new public cemetery was consecrated for Church of England burials and part left unconsecrated for
other denominations; Leeds's municipal cemetery opened in 1845 with the two sections [P106],
[P130]. An Ulster-born man buried in the consecrated part had a first child baptised Catholic [P106]. Record the section and officiating minister as clues [P109], [P129], then compare baptism and chapel records, as in [english-nonregister-record-recovery § 5](english-nonregister-record-recovery.md#5-a-label-that-says-only-dissenter-or-nonconformist).

Do not doubt an identification because a suicide lies in consecrated ground. In England and Wales
the Burial of Suicides Act 1823 already allowed a person found felo de se to be buried in the
churchyard, but only between 9 p.m. and midnight and without a Christian service [P106], [P135].
The Interments (felo de se) Act 1882 repealed it and allowed the burial in any way the Burial
Laws Amendment Act 1880 permits, while stating that it did not authorise the rites of Christian
burial [P134]. Both Acts concern only a coroner's verdict of felo de se, so find the inquest
verdict before reading anything into the burial's place, hour or service [P134], [P135].

A private grave was bought, the purchase confirmed by a certificate or 'grave paper', and the headstone
was a separate fee, so an unmarked plot can still be a family's private grave: find it by its
grave number on the cemetery plan instead of calling it a pauper's grave [P106], [P132]. A
private grave usually held one family, though servants were sometimes buried in it too [P131]. A
common or public grave belonged to the cemetery and held unrelated people who died within a few
days of one another; the cheapest, the lock-up grave, stayed open under a locked wooden cover
between burials [P106], [P129], [P131]. Do not treat people sharing a common-grave number as kin,
or everyone named on one stone: an inscription grave, in Leeds the 'guinea grave', was a common
grave whose shared headstone gives each unrelated occupant's name, age and date of death [P106],
[P131], [P132]. Check the grave type in the register before you infer a family from a grave or a
stone.

'Pauper's grave' was not an official term. It describes a burial at public expense, paid by the
parish before 1834 and by the Board of Guardians after, in an unmarked common grave [P106],
[P132], [P133]. For a death in a workhouse, also look in its registers: the master kept a
register of deaths, and the creed and admission and discharge registers record deaths too
[P133]. Find the poor law union from the jurisdiction table in
[english-nonregister-record-recovery § 1](english-nonregister-record-recovery.md#1-build-the-dated-jurisdiction-table-before-choosing-a-series).

A churchyard burial is recorded in the parish register, which rarely says where in the ground the
grave lies [P104], [P127]. Ask at the church and the county record office for a plan of the
churchyard; at the record office, search the parish's deposited records, including its
miscellaneous records [P104], [P127]. Then look for a survey or map by the family history
society, a Friends group or the record office's volunteers; a society's may need membership
[P104], [P127].

With a grave number, find the plan before a visit: on the cemetery's own website, the council's
cemetery pages, which may sell plot maps, a Friends group's site, a local heritage group or the
family history society [P105]. Some Friends groups map each plot with its occupants and a
thumbnail of any recorded headstone, partly for members only [P105], [P136]. When the plan does
not settle where the grave lies, ask a Friends group to help find it; some do so on the ground,
sometimes for a donation [P105], [P107]. A plan drawn by volunteers from the visible stones,
without an official plot list, can leave out unmarked graves, and an original plan may be
incomplete, so a name missing from a plan is not a negative [P104].

For a Church of England churchyard, the Church Heritage Record shows where each churchyard is, not
its graves [P104 @2026-11-14], [P137 @2026-11-14]. Plot-level plans and memorial photographs come
from the National Burial Grounds Survey, which covers Church of England churchyards diocese by
diocese and needs each parish's consent; in July 2024 the General Synod agreed that parishes
should be told not to sign up [P137 @2026-11-14], [P138 @2026-11-14]. Check the diocese's status
on the survey's map. Record a churchyard it has not reached as `not surveyed`, not as evidence
that the grave is absent.

A burial register or burial-certificate file can confirm a burial without giving any grave
location. Record the plot as `not recorded in this series` instead of expecting the register to
supply it. In a Moscow researcher’s account, the 1917 burial certificates in fond 1457 omitted the plot and closely paralleled the death register in fond 2372 [P15]. Compare the two series and record any dependence before counting confirmations.

When no funeral home or cemetery is named, or the named office or firm has closed, trace who now
holds the records and list the possible custodians for the period before concluding that no record
exists or that it is lost. Use that year's city directory
business and church listings, or an old telephone directory, and census records for the death
place. Widen to nearby towns or the county where a small place had one firm. Log each funeral
home, cemetery and church with the directory title and year. When contact is authorized, ask
surviving local funeral homes about closed firms and small family burial grounds. A listing names
a possible holder; it does not show that the firm handled this burial or that its records survive.
The [death-records class](https://www.youtube.com/watch?v=70ya-VPbkBc),
[burial-place talk](https://www.youtube.com/watch?v=Cfdt0Fd0opI),
[date-of-death video](https://www.youtube.com/watch?v=bc92E8Oq4zU) and
[funeral-home tip](https://www.youtube.com/watch?v=twrGXgz08S0) motivate this step.

If an inspected death certificate names an undertaker or funeral home, preserve its literal
name, address and date as a separate record-recovery route. Use a period city directory's
business or address entries to clarify a difficult name. For a closed firm, look for evidence
of a successor business or a funeral-record collection deposited at a historical society or
library. Another firm at the same address is a lead, not proof of business succession or
record transfer. Confirm the relevant dated holdings and access with the actual prospective
holder before treating the records as available; keep the certificate, directory entry and
custody evidence separately cited. Prepare a bounded request for the person's funeral or
burial record, retaining requested, unavailable and received states. Use the same contact
authorization rule above. The demonstration establishes no present holder, guaranteed survival
or entitlement to the records. [P22]

Inspect the undertaker’s certification on every page and face of a death certificate. In a New York City example the person who hired the undertaker was identified as the deceased’s sister [P60]. Transcribe the name and role as written. For ‘M. [Surname], the sister of deceased’, test both a sister with that initial and one whose husband used it. Check the certificate’s burial-place field against the named cemetery’s interment entry, including when the cemetery lies in another state.

A funeral guest register or memorial book, usually kept by the family and handed down, lists
people who came to pay their respects. Use each name as a lead to relatives, associates and
neighbours, including relatives by marriage, some from marriages that had ended [P120], [P147],
[P148]. A signer with a family surname whom you cannot place is a candidate relative to research;
one you cannot connect is a candidate friend or associate, not evidence of kinship [P147].
Signatures can be hard to read, and people often arrived together, so read a difficult name
against the names beside it [P120]. For a recent funeral the signers are living people: keep
their names in the private research log.

Where the actual source offers it, inspect the matched plot's roster before a bounded
neighboring-plot search. Retain each burial/plot identifier and the actual distance or selected
area separately from coordinates. Use co-burial/proximity to nominate associates and retrieve
their burial records before proposing a relationship. The [co-plot search description](https://lostrussianfamily.wordpress.com/2025/10/25/free-database-offers-more-than-5-million-indexed-burial-records-for-moscow/)
supplies no fixed search radius or current provider/plot-accuracy guarantee.

If a memorial's family link appears to come from neighbouring markers or a shared surname
in one lot, check the actual grave sequence and adjacent inscriptions on an authorized
visit or in a dated set of site photos. Keep the observed layout as a locator for the
relationship search. Confirm kinship from the records for the people named. [P160]

Some online burial databases, including ones run alongside grave-care businesses, publish
burial cards with monument photographs and, for some entries, coordinates. [P32] Where one holds
a card for a known deceased relative, use its photograph and coordinates to find older
neighbouring monuments and cards on the same plot, as locators only. Coverage is limited to what
that site has recorded, and proximity is not kinship. Keep only a crop of the relevant monument,
because such photographs can show living mourners.

If a plot-owner card points to the named owner's other cards or lots, follow those
locators even when they fall outside the neighboring area; keep owners and referenced
lots separate from actual interments. [P29]

In immigrant-city Jewish cemeteries, such as those around New York, many plots belonged to
landsmanshaftn (hometown societies), as well as to synagogues, unions, family circles and
fraternal orders. [P51, P52] A society or section name in an interment record, such as
'First [Town]er … Society', points to a hometown. Not every member came from the named town, and
neighbouring graves in a society plot may belong to unrelated members. A married woman buried in
her husband's society plot gets his town, not necessarily her birthplace. The YIVO Archives at the
Center for Jewish History hold records of many landsmanshaftn, some with plot maps, and the
finding aid is arranged by ancestral town. [P50, P51, P52] In New York and New Jersey cemeteries,
a society plot usually has a gate or arch naming the society, often with its officers: record that
inscription as its own locator, with its photograph, beside the plot reference. Gate names can be
eroded, and a plot can pass from one society to another, so confirm it in the cemetery's records.
[P83] For congregation and society records as
origin evidence, see [immigrant-congregation-origin-records.md](immigrant-congregation-origin-records.md).

Treat the cemetery named on a volunteer memorial as that memorial's statement, not an observed
burial. A profile may be created speculatively to request a photo lookup, or by a relative before
burial arrangements are made, naming the intended cemetery. Record the creator and creation date
where the page shows them, and any photograph or cited source. Without these, carry the cemetery
as `cemetery claimed, unsupported` until an interment entry or equivalent burial evidence
confirms it; a grave photograph or dated society transcription corroborates the marker's location
and inscription, not the interment. The
[birth-and-death sources talk](https://www.youtube.com/watch?v=gG5ZL8ueNx4), its
[later version](https://www.youtube.com/watch?v=YW9oCpm5id4) and the
[Find a Grave discussion](https://www.youtube.com/watch?v=M6NwvqpYK58) motivate this. They give no
rate for speculative memorials and do not show how any site displays creation history.

**Privacy gate:** <!-- privacy-gate: contact --> Messaging a memorial's contributor about a
photograph reaches a living stranger and discloses the user's research interest; answer the privacy
gate in `SKILL.md` first.

Read a Find a Grave memorial against the site's own rules, which describe what contributors are
asked to do, not what was checked. Contributors are asked to add only verified burial places, not
presumed ones, and a memorial with the burial details unknown is warranted only in rare cases.
[P84, P85] Memorials for living people are not acceptable, and one is removed when the person or
a family member asks; a person may create a pre-need memorial for themselves once a pre-need
headstone is in place. [P84] A cenotaph, a memorial for someone buried elsewhere, is marked by a
setting among the grave-marker options, and family links belong on the memorial of the actual
burial. [P86] Members enter the family links themselves [P87]: record them
as the contributor's claim. Corrections go through Suggest Edits; the manager may decline one, and
an edit left unanswered for 21 days passes to Find a Grave's own queue. [P88] For a photograph,
the help pages direct you to the contributor for permission [P89]. The contributor is the contact
for permission and provenance, not proof of who owns the copyright: an uploaded studio portrait
may belong to someone else.

Follow family links as leads to other memorials, including ones in a different locality.
For each link, log the source that supports the claimed relationship, or mark the claim
unsourced. If a public tree repeats the claim for the same deceased person, open the tree's
attached evidence and trace which source each copy cites. A tree and a memorial that point
to one another leave the relationship unsupported. [P160]

Find a Grave asks if the creator is a close relative for deaths within the past year.
For a memorial created by someone outside its transfer guidelines, it limits what others
see for the first three months. [P165 @2026-11-18] Keep original creator and current manager
separate. When the original creator is missing, log authorship as unknown and report those
unknowns if counting family and non-family creators. Check the informant's firsthand knowledge
for each fact before relying on it, even if the site shows a family relationship.
[P160 @2026-11-18]

According to a supplied transcript excerpt, the interview describes finding linked memorials
across localities and Daniel Loftus suggests requesting a photo when the marker cannot be
visited in person. [P164†]

**Privacy gate:** <!-- privacy-gate: contact --> A marker photo request shares the deceased's memorial, plot details and any note with Find a Grave and its photo volunteers, and appears with the cemetery's requests. Leave e-mail sharing off and answer the privacy gate in `SKILL.md` before sending.

Use **Request Photo** on the memorial when an on-site photo is needed. Supply the confirmed
plot reference and specify the face or detail needed, including why a new image is needed
if one already exists. Request the surviving marker without presuming it is a headstone.
[P166 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: link --> Putting memorials into a Virtual Cemetery sends the memorial IDs and the user’s list name to Find a Grave. Grouping can reveal the user’s family connections or visit plans if made public. Check visibility and answer the privacy gate in `SKILL.md` before saving.

If the user wants a grave-visit list across physical cemeteries, save the memorials to a Virtual
Cemetery with **Save to**. Choose **Private** and reopen the list from the user’s profile before
the visit. [P262 @2026-11-22] [P261 @2026-11-22] [P258 @2026-11-22] According to the supplied Morton tutorial excerpt, the
Save to menu offers the Virtual Cemetery option. [P264† @2026-11-22]

Before an authorized visit where the user wants to help, open the cemetery's **Photo Requests**
list. Use the requested memorial's supplied grave location and any cemetery plan to locate
the marker. Check the inscription and plot against the request before taking the picture.
[P167 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Claiming a photo request sends the user’s account and chosen memorial request to Find a Grave. Check who can see the volunteer’s claim and answer the privacy gate in `SKILL.md` before confirming it.

If the user can visit the grave and wants to take responsibility for the photo request, select and
confirm Claim only after checking that the request has a usable locator. Reopen it through
**Requests I Claimed** before the visit.
[P258 @2026-11-22], [P263 @2026-11-22]

**Privacy gate:** <!-- privacy-gate: upload --> Sending a grave photo gives Find a Grave and memorial viewers the deceased's inscription and any included coordinates, which can disclose the photographer's location at capture. Crop bystanders and keep incidental living-person details local. Answer the privacy gate in `SKILL.md` before sharing.

Upload the marker photo through **Fulfill** only for the verified memorial with the photo
request. [P167 @2026-11-18]

Upload a geotagged marker photo only when the user has authorized sharing the location.
With Location Services on, Find a Grave's Android app uploads the coordinates with the
photo through **Add Photo**. Capture the location at the marker. [P168 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Device-assisted navigation gives the Find a Grave app the visitor's current location and the marker location. Answer the privacy gate in `SKILL.md` before using device location.

For device-assisted navigation, use **Map It** on a memorial with GPS in the iOS app.
Keep the grave's mapped point as the marker locator. [P169 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: publish --> A memorial correction sends the deceased's corrected fields and supporting details to Find a Grave and, for a suggestion, the manager. Accepted changes are visible on the memorial. Keep living people's details local and answer the privacy gate in `SKILL.md` before submitting.

Submit a documented memorial correction through **Edit** if the user's account currently
manages the memorial or **Suggest Edits** if someone else manages it. Keep the inscription
as carved in the packet when the memorial field is corrected.
[P160 @2026-11-18], [P170 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: link --> A family link sends the memorial IDs and relationship to Find a Grave and can disclose family connections to memorial viewers. Answer the privacy gate in `SKILL.md` before linking.

Enter the verified relative's Memorial ID in the corresponding **Family Members** field
when editing or suggesting a link. Check the target memorial and relationship first.
[P171 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A management claim gives Find a Grave the user's account, the deceased relative's memorial and their relationship. Management may be visible to viewers and the site's relationship setting controls its display. Answer the privacy gate in `SKILL.md` before submitting.

Use **Manage** on a recently deceased close relative's memorial within a year of death
if the user wants to manage it and qualifies under the site's transfer guidelines. Enter
the relationship through the prompt and keep its display private. Once the account manages
the memorial, use the correction step above.
[P165 @2026-11-18], [P170 @2026-11-18]

On BillionGraves, the app attaches GPS to photographs taken with it, volunteers transcribe the
stones, and records not uploaded through the app have no GPS. [P90, P91]

**Output:** `cemetery | address | section | plot | GPS as supplied | map URL | office/register
locator | access or contact status | next action`.

**Check:** A map point helps retrieval. It does not establish that a same-named online memorial
belongs to the target, or that an adjacent burial is a relative.

## 5. Keep a discrepancy open and choose the next record

Compare the inscription, online transcription and available cemetery record. If a death date
differs from a civil or Social Security entry, preserve both values with their sources. The
gravestone webinar specifically recommends recording the discrepancy, because errors can occur
in either the stone or a government database. [P1]

**Privacy gate:** <!-- privacy-gate: contact --> A family marker correction request shares the deceased service member’s grave locator and evidence of religious identity, and the signing relative’s name and relationship, with Operation Benjamin and ABMC. Answer the privacy gate in `SKILL.md` before sharing either the inquiry or supporting documents.

For a U.S. World War II grave under a Latin cross at an ABMC cemetery, record the marker and grave
locator, then check independent military and family records for evidence of Jewish identity.
According to the Just Genealogy excerpt, a family request and Operation Benjamin’s research led
to replacement markers. [P303† @2026-11-23] If the records support a correction, have a family member
work with Operation Benjamin and sign the request for ABMC to review.
[P304 @2026-11-23], [P305 @2026-11-23]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> An obituary phrase sent to Google can disclose details of the deceased and anyone named in the text. Use a short phrase free of living people's details and answer the privacy gate in `SKILL.md` before sending.

Search Google for a distinctive phrase from an uncited memorial biography, in quotation marks,
to trace it to an obituary. Open the funeral home's notice or the digitized newspaper and
cite that version for the death and any stated next-of-kin details. Keep names of living
survivors local and distinguish announced burial plans from an interment record.
[P160 @2026-11-18], [P162 @2026-11-18]

When two Find a Grave memorials place the same candidate in different cemeteries, keep both cemetery
claims and check each interment register for a dated burial or removal. Test a cenotaph at either or
both sites. A photographed stone can still be commemorative. [P257] According to Scott, one of two
competing memorials had a stone photograph and the other had a portrait, leaving the burial
unresolved. [P255†]

Keep an earlier inscription transcript or research letter with its author/date, exact
reported reading and any available image reference. Record a later inspection separately
as not located, not inspected, unreadable or partly read, according to what happened.
A 1966 researcher transcribed a double marker at McGee Cemetery and noted faint lettering; a later visitor could not locate it [P37]. Keep both observations and leave the reason for the failed search open.

If an online memorial assigns an early burial to a named cemetery, compare the burial date
with that cemetery's documented opening or operating period. An opening after the burial
excludes it as the original burial ground; keep a later reinterment or marker transfer
unresolved until its own evidence is found (section 3). Record the dating source and any
uncertainty about earlier use of the site. Use the burial entry's parish or church and the
locality's cemetery histories to list grounds operating at the burial date as candidates,
with a source for each period and parish connection. A candidate ground does not locate
a grave. The reported 1884 opening of Saints-Anges excludes it as Anne Doucet’s original 1791 burial ground but leaves any later removal unresolved [P21].

If a family story places the death abroad, search for a grave by name without restricting
the search to the reported death place. Compare the candidate's dates and name against
independent records. In one reported case, a family story pointed to a death in Mexico
and a matching grave entry pointed to Petaluma [P209]. Carry the cemetery as a burial
lead and check the place of death separately in a death record or contemporary notice.

Choose the next retrieval action from the gap: a clearer photograph for uncertain letters, a
cemetery register for an unlabelled burial date, or the underlying civil record for a conflicting
death date. Finding a death record does not guarantee that a burial record will be found, and
finding a burial record does not guarantee a death record. [P2]

**Completion packet:** candidate identifier; exact searches; coverage observation; full-record
and image URLs; each image's pixel size and what was legible at it; raw inscriptions as read blind,
with uncertain readings, and any database or quoted reading kept beside them; separately labelled
dates, including death, burial, inscription and photograph dates; cemetery,
section, plot and supplied GPS; any register/office locator; discrepancies; and the next source.
All source-dependent fields are nullable. Use `not supplied`, `not examined`, `unreadable` or
`unresolved discrepancy` to explain the gap instead of filling it with an inference.

## Prompt pattern

> Build a burial evidence packet from these cemetery records and photographs. Keep candidates
> separate. Transcribe each photograph blind before reading database fields or a quoted epitaph.
> Preserve raw Hebrew and secular inscriptions, name roles, calendar labels, plot/GPS identifiers
> and source URLs. Keep death, burial, inscription and photograph dates apart. State which images
> were inspected, their pixel size and what was legible at it.
> Leave unsupported fields unknown; list discrepancies and the next original record to retrieve.
> Do not choose an identity or final date from the database label alone.
