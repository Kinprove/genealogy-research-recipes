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
router: {"section": "Record types in any country", "group": "Burials, directories, land and probate", "order": 164}
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

FamilySearch lists Full-Text under its Search menu. Sign in and try `cemetery` with the place name to locate digitized transcriptions [P64 @2026-11-19].

Keep each survey’s date with its reading of a stone that later broke or disappeared. Record whether the compiler read the inscription, relied on a local account or located the grave by dowsing. The Berks County preservation group reported that its compilation included dowsing-based locations and that it still found errors [P192].

At a plantation cemetery for enslaved people, log visible ground depressions as possible grave
locations even where there are no markers. On an authorized visit, note the depressions from the
surface without probing or disturbing the ground. Look for an existing cemetery delineation
survey to check their position. Leave the occupants unidentified from these features alone.
[P158], [P159]

Compare dated cemetery transcriptions word by word, including older editions: a stone legible to a 1940s compiler may have worn away by the 1990s [P118]. Record the compiler and date for each reading and check disputed words against an image or the surviving stone [P146].

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

ABMC covers more than its First and Second World War cemeteries. Its Honolulu Memorial names 8,209
people listed as missing from the Korean War and 2,504 from the Vietnam War, and ABMC also
administers Mexico City National Cemetery, Corozal American Cemetery in Panama and Clark Veterans
Cemetery in the Philippines [P99 @2026-11-13]. Do not rule ABMC out for a missing service member of
those wars or a burial in those three cemeteries.

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

For Manchester, use MyHeritage's *England, Lancashire, Manchester Burials* for entries from
1850 onward. Save the deceased's name and the stated date and place of burial. For parish
burials, search its separate Diocese of Manchester collection (1603–1910). The similar
titles and overlapping years cover different sets of records.
[P177 @2026-11-18], [P189 @2026-11-18], [P190 @2026-11-18]

For Stockton-on-Tees, search MyHeritage's Durham burial index from 1871 onward for the name
and stated date and place of burial. Check the council's burial register search as well.
Leave a miss unresolved. The council says its online entries are incomplete.
[P186 @2026-11-18], [P187 @2026-11-18], [P188 @2026-11-18]

For a French hit in MyHeritage's *France, Church Burials and Civil Deaths*, read the underlying
entry and label it as a parish burial or a civil death. The combined index gives the death
date and place. Take the burial place and date only from a statement about burial, and use the
death commune as a lead when the burial place is missing. Coverage varies by département.
[P180 @2026-11-18], [P181 @2026-11-18]

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

Before using the comparison, check that the attached photo actually shows the target's
marker. If the name or plot evidence points to a different marker, log the attachment as
a mismatch. Read doubtful letters and symbols against the carving. Preserve even apparent
errors in the literal transcription and keep proposed corrections in the research notes.
[P160]

Treat the birth name and birth date on the stone as leads when the informant's firsthand
knowledge is unknown. An accurate memorial transcription still carries the same inscription
claim. Check those details against a birth or baptism entry where available. [P160], [P163]

Record the pixel width and height of each image you read, and what was and was not legible at that
size, for example `1200 × 900 px; given name and month-year legible; father's name eroded`. Read
the largest copy available, not a thumbnail. A word that cannot be read in a small or compressed
copy is unread, not missing from the stone. An AI model may receive a smaller image than the file;
see [ai-for-documentary-records](ai-for-documentary-records.md#the-pitfalls-worth-internalizing-the-least-obvious-most-llm-usable-part).

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

For each person named on a family monument, retain the literal burial-place statement and its
image/surface locator separately from the monument's physical cemetery and plot. A family
monument can name people buried elsewhere; compare their location statements with available
burial records instead of assigning everyone named on the monument to its plot.
Unresolved burial locations stay open. [P26]

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

When one grave has a family stone and a commemorative marker, such as a military marker a society
placed later, record each date with the marker it comes from, who placed it and when. Record
lettering cut later, such as sandblasted text beside raised original lettering, as a later
addition. A date conflict between markers stays an unresolved discrepancy (Section 5). [P66]

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

If a form can capture the device's current position, use that control only while physically at
the intended site. When entering information off-site, leave current-position capture unused.
Retain where the coordinate came from and what point it represents; keep an independently
supplied coordinate with its source instead of replacing it with the contributor's location.
Unknown point meaning stays unresolved. The dated Cemetery Registry demonstration motivates this
capture-origin check, not a guarantee of coordinate accuracy, grave identity or access. [P25]

If the death municipality in France is known but the cemetery is not, check whether its archival
descriptions list `registres des convois funéraires` or `registres des transports de corps` for the
relevant period. A Paris transport entry of 27 December 1955 gave Vignot in the Meuse as the destination for Victor Grandsire, four days after his death [P28]. Copy the date and destination, then seek the interment entry and plot at the receiving cemetery.

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

Permit rules and record survival vary by state and period.

**Privacy gate:** <!-- privacy-gate: contact --> A search request to a council, church, record office or Friends group names the deceased and the burial place and discloses the user's research interest; answer the privacy gate in `SKILL.md` before you send it.

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

Before an authorized visit where the user wants to help, open the cemetery's **Photo Requests**
list. Use the requested memorial's supplied grave location and any cemetery plan to locate
the marker. Check the inscription and plot against the request before taking the picture.
[P167 @2026-11-18]

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

**Privacy gate:** <!-- privacy-gate: third-party-tool --> An obituary phrase sent to Google can disclose details of the deceased and anyone named in the text. Use a short phrase free of living people's details and answer the privacy gate in `SKILL.md` before sending.

Search Google for a distinctive phrase from an uncited memorial biography, in quotation marks,
to trace it to an obituary. Open the funeral home's notice or the digitized newspaper and
cite that version for the death and any stated next-of-kin details. Keep names of living
survivors local and distinguish announced burial plans from an interment record.
[P160 @2026-11-18], [P162 @2026-11-18]

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
