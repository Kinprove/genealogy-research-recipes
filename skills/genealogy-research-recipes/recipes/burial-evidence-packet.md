# Build a burial evidence packet from cemetery records

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

A miss in Find a Grave, BillionGraves or another crowd-sourced site is not a coverage test,
especially for small, inactive or private-land burial grounds. Also check county-society
inventories, state cemetery surveys or commission databases, and state-archive or archaeological
survey files, which may not be digitized. Record each survey's title, date, holding place and any
registered cemetery number as a separate locator. A listing locates a burial ground, not who lies
in it. A survey reading is a derivative transcription made at its date. Where a stone has since
broken or vanished, keep it as a dated observation (Section 5). Keep inscriptions actually read
apart from locations based on word of mouth or dowsing. The
[cemetery-records class](https://www.youtube.com/watch?v=th8_R6cKTnw),
[periodicals talk](https://www.youtube.com/watch?v=ETyI_TSMpzQ),
[family-cemetery session](https://www.youtube.com/watch?v=4di3XOsN4GE),
[burial-place talk](https://www.youtube.com/watch?v=Cfdt0Fd0opI),
[etiquette class](https://www.youtube.com/watch?v=fBm75Zoz1-A),
[preservation interview](https://www.youtube.com/watch?v=38jzvP3IYKc) and research-trip videos
([2021](https://www.youtube.com/watch?v=kINOGgLV3ak),
[2024](https://www.youtube.com/watch?v=0v5fySALYxs)) motivate this. They do not measure how
complete or accurate a survey is, and a preservation group reports finding errors in its own
compilation.

For a published necropolis or burial list, record what it was compiled from: cemetery documents
or monuments, or the death section of parish metrical books. Treat the two kinds as separate
sources and compare them where both exist. A list built from death entries records deaths in the
parish, not observed graves, though it may be the only option once a cemetery has been destroyed.
A highly selective compilation, such as the consistory lists described in the
[necropolis-list discussion](https://rodgersforum.borda.ru/?1-7-0-00000136-000-0-0-1774709430=),
is not a coverage test, so a name missing from it proves nothing. The thread reports no result
from comparing the two kinds.

**Output:** `database | query | coverage checked | candidate URL | cemetery | section |
photo available | image examined | next source`.

**Check:** Distinguish a searched name, an included cemetery and an inspected inscription.

## 2. Search the recorded name fields separately

When an East European Jewish stone has no surname, JOWBR documents searches using the deceased's
given name, the father's given name or the Hebrew Name field. Use the known locality to assess
the returned candidates; a common patronymic can produce many hits. [O1]

For an Eastern European database, inspect the form's native labels before entering the name.
The 2025 Pomnim example orders its boxes as surname, given name and patronymic; the Pogost example
adds gender and cemetery. Enter the supported native-script form rather than assuming that a
translated page has translated the database's names. Confirm the current form when executing
these older examples. [P3]

**Output:** a query row for each field combination, retaining the exact entered strings and
the candidate record links.

**Check:** A search expansion supplies candidates; it does not equate a Hebrew patronymic with
a civil surname or identify the father.

## 3. Preserve the photograph and both inscriptions

Open the available photograph and save its URL, cemetery and plot information. Keep any permitted
original image separate from a working crop or adjusted reading copy. Record which image was
actually inspected.

Record whether the stone's letters were traced (outlined) before the photograph was taken. A
traced photograph shows the tracer's reading, not the carving itself. Check each doubtful letter
against the wording expected at that point in the formula and, where available, a better or
untreated image; note which image each reading comes from. The
[matzevah-reading discussion](https://forum.j-roots.info/viewtopic.php?f=208&t=9621) shows a
letter read as מ that a participant identified as a wrongly traced ה of צנועה. It supplies no
untreated comparison images, and the expected formula only flags a doubtful letter; it does not
settle the reading.

For a difficult inscription, an optional second photograph uses light directed from the side
by a hand-held reflector or flashlight, held clear of the marker. Keep the ordinary-light and
side-lit views together, label the surface and lighting, and leave uncertain letters unresolved.
This step does not involve rubbing, cleaning, wetting or touching the marker. [P27]

Record which faces of the stone, and of any family marker, the images actually show: front, back
and sides. A spouse, a second burial or a list of children can appear only on the back. On a
Jewish stone, the back can carry the Hebrew name and patronymic, while a memorial-site photograph
may show only the English front. Mark an unseen face `not examined`, not absent, and queue a
request for its photograph. Do not record a person as absent from a marker after only one face has
been inspected. The [family-cemeteries video](https://www.youtube.com/watch?v=rA5-uq548q4),
[cemetery photographs tips](https://www.youtube.com/watch?v=7zW86N6q4Yc),
[cemetery steps session](https://www.youtube.com/watch?v=crq_j9WnVn8) and
[Lil Dicky tree session](https://www.youtube.com/watch?v=SKDoU7MJkds) motivate this. A name on
another face does not by itself establish burial at that spot or a relationship, and the back may
carry nothing.

For a family monument, inspect available views of its front, reverse and lower additions.
Label the surface shown and keep unseen or unreadable parts explicit. For each named person,
retain the literal burial-place statement and its image/surface locator separately from the
monument's physical cemetery and plot. A family monument can name people buried elsewhere;
compare their location statements with available burial records instead of assigning everyone
named on the monument to its plot. Unresolved burial locations stay open. [P26]

For supplied cemetery-visit photographs, retain an actual cemetery-sign photograph as a
context image and link it to the corresponding grave-photo IDs using the supplied visit
notes or other documented association. On an authorized future visit, photographing the
cemetery sign first can help preserve this context. If no such image was supplied, record
it as absent; do not invent a sign image or assume that every adjacent camera file belongs
to that cemetery. A sign identifies the photographed place, not the person or burial. [P24]

For a bilingual stone, transcribe the Hebrew and secular-language portions separately. The
gravestone tutorial demonstrates the deceased's Hebrew given name and the father's Hebrew name
as useful leads that can be absent from the secular portion. Preserve the raw wording, the
person's stated role and uncertain letters before adding a translation. Do not require every
stone to contain the same fields. [P1, O1]

On a short formulaic Hebrew epitaph, transcribe the descriptor before the name as its own field:
for example איש or אשה, הבתולה (maiden), הבחור (young man) or הישיש (old man). Use it as a possible
life-stage or marital-status clue when comparing candidates. Do not turn it into an age or a proven
marital status. Leave a doubtful term unresolved. In the
[epitaph-descriptor discussion](https://forum.j-roots.info/viewtopic.php?f=208&t=9621), the sense
of החתן (groom, young man or something else) stayed disputed; one participant only tentatively
settled on "young man".

Before treating a word on a Hebrew stone as a surname, check whether it is a status or occupation
marker, such as כ"ץ for a kohen, הלוי for a Levite, or, less certainly, שו"ב for a ritual
slaughterer. Record the literal letters and the proposed expansion separately. Assign the title to
the man it follows: after a woman's patronymic, it describes her father, not her. Try to find the
person in the locality's records for the period by given name and father's name rather than by the
apparent surname. The [matzevah-reading discussion](https://forum.j-roots.info/viewtopic.php?f=208&t=9621)
and [title question](https://forum.j-roots.info/viewtopic.php?f=75&t=7576) motivate this. כ"ץ (Katz) can be a real surname in other contexts, and neither thread proves an identification. A conflict such as
'bar' followed by a female name stays unresolved until the image is checked.

Treat ר' or 'Reb' before a man's name on a stone as an honorific, not evidence of rabbinic
ordination. Likewise, do not turn 'Rabbi' or 'Rev.' in later family or community sources into the
occupation rabbi. Record the literal title. Then look for period or scholarly accounts of what the
person actually did, such as ritual slaughterer, teacher or prayer leader. The
[title-and-ordination discussion](https://forum.j-roots.info/viewtopic.php?f=4&t=4667) motivates
this. It sets a tombstone reading beside community histories that describe the man's roles and
mention no ordination. Usage varied by period and community; the title alone neither proves nor
rules out ordination.

Keep the dates separately:

| Field | What to retain |
| --- | --- |
| Death date on inscription | Literal English/secular and Hebrew forms, each with its label |
| Age at death on inscription | Literal value and stated units, linked to the inscription's death date; missing units stay unknown |
| Calculated birth-date lead | Separate derived value, input death date and age, calendar and arithmetic; label `calculated, not stated` |
| Burial date | The date explicitly supplied as burial, with its source |
| Database date | Displayed value, field label and record URL |
| Converted date | Separate derived value, calendar and conversion basis, if checked |
| Unreadable or absent value | Unknown; no guessed completion |

**Check:** An unread inscription, missing date or unverified conversion stays unknown. The
packet records the source statements and does not select a final death date. [P1, O1]

When an inscription dates the death by a festival day or its abbreviation, such as אחש for the
last day of Pesach, expand it to the Hebrew calendar day before any Julian or Gregorian
conversion. Keep the literal phrase, the expansion and the reference used as the basis in the
Converted date row. Check the day against the community's festival practice, and convert only when
the year has been read. Do not replace the phrase with an approximate 'around Passover'. The
[festival-date discussion](https://forum.j-roots.info/viewtopic.php?f=208&t=9621) motivates this
with one abbreviation glossed by a link. It sets no conversion rules.

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
unresolved transfer. A new marker does not date the burial or identify the remains. The
[George Estes dedication example](https://dna-explained.com/2023/09/19/calling-all-descendants-of-george-estes-1763-1859-youre-invited-to-his-revolutionary-war-grave-dedication-52-ancestors-410/)
motivates this event chain without independently verifying the reported relocation.

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

If a form can capture the device's current position, use that control only while physically at
the intended site. When entering information off-site, leave current-position capture unused.
Retain where the coordinate came from and what point it represents; keep an independently
supplied coordinate with its source instead of replacing it with the contributor's location.
Unknown point meaning stays unresolved. The dated Cemetery Registry demonstration motivates this
capture-origin check, not a guarantee of coordinate accuracy, grave identity or access. [P25]

When the plot cannot be located or the online entry lacks detail, identify the cemetery office
and prepare a request for the recorded burial and its plot location. The gravestone tutorial
recommends asking the office before visiting. Give the candidate name, known date, cemetery and
any existing locator; request the corresponding register entry or available burial information.
Send the request only when contact is authorized. [P1]

Before treating a missing or unfindable marker as a wrong lead, ask the cemetery office about the
grave's type and status when contact is authorized. Is it a war grave? Was the stone removed, for
example as unstable? Record any reported grave status and the current section, row and number
beside the original locator. If the office reports an anonymous interment, ask for the recorded
burial field and log it as the locator of an unmarked burial. The
[Berlin grave-photo request thread](https://forum.ahnenforschung.net/forum/thread/19335-fotow%C3%BCnsche-berlin-wer-braucht-fotos-von-berliner-grabstellen-kirchen-h%C3%A4user/)
motivates this. Its report that a war grave survives and its advice that the office can name the
field of an anonymous burial are local forum statements; the thread does not show a field being
released, and grave-retention rules vary by cemetery and period. [P19]

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

A burial register or burial-certificate file can confirm a burial without giving any grave
location. Record the plot as `not recorded in this series` instead of expecting the register to
supply it. Where the burial series closely parallels the death register for the same community, as
in the [Moscow burial-certificate discussion](https://forum.j-roots.info/viewtopic.php?f=20&t=5084),
cite both and mark them as related records, not two independent confirmations. That example rests
on one researcher's description of a single year's file. It does not show how other cemeteries or
periods kept their records.

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

Where the actual source offers it, inspect the matched plot's roster before a bounded
neighboring-plot search. Retain each burial/plot identifier and the actual distance or selected
area separately from coordinates. Use co-burial/proximity to nominate associates and retrieve
their burial records before proposing a relationship. The [co-plot search description](https://lostrussianfamily.wordpress.com/2025/10/25/free-database-offers-more-than-5-million-indexed-burial-records-for-moscow/)
supplies no fixed search radius or current provider/plot-accuracy guarantee.

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

**Output:** `cemetery | address | section | plot | GPS as supplied | map URL | office/register
locator | access or contact status | next action`.

**Check:** A map point helps retrieval. It does not establish that a same-named online memorial
belongs to the target, or that an adjacent burial is a relative.

## 5. Keep a discrepancy open and choose the next record

Compare the inscription, online transcription and available cemetery record. If a death date
differs from a civil or Social Security entry, preserve both values with their sources. The
gravestone webinar specifically recommends recording the discrepancy, because errors can occur
in either the stone or a government database. [P1]

Keep an earlier inscription transcript or research letter with its author/date, exact
reported reading and any available image reference. Record a later inspection separately
as not located, not inspected, unreadable or partly read, according to what happened.
A failed present reading neither verifies nor erases the older statement. The [road-trip example](https://familylocket.com/rlp-231-family-history-road-trip/)
motivates this distinction without supplying an earlier photograph or proving identity,
marker replacement or the reason a present reading failed.

If an online memorial assigns an early burial to a named cemetery, compare the burial date
with that cemetery's documented opening or operating period. An opening after the burial
excludes it as the original burial ground; keep a later reinterment or marker transfer
unresolved until its own evidence is found (section 3). Record the dating source and any
uncertainty about earlier use of the site. Use the burial entry's parish or church and the
locality's cemetery histories to list grounds operating at the burial date as candidates,
with a source for each period and parish connection. A candidate ground does not locate
a grave. The [Anne Doucet example](https://dna-explained.com/2025/01/04/anne-doucet-1713-1791-oceans-rivers-and-perseverance-52-ancestors-438/)
motivates this chronology check; its proposed final grave location remains unverified. [P21]

Choose the next retrieval action from the gap: a clearer photograph for uncertain letters, a
cemetery register for an unlabelled burial date, or the underlying civil record for a conflicting
death date. Finding a death record does not guarantee that a burial record will be found, and
finding a burial record does not guarantee a death record. [P2]

**Completion packet:** candidate identifier; exact searches; coverage observation; full-record
and image URLs; raw inscriptions and uncertain readings; separately labelled dates; cemetery,
section, plot and supplied GPS; any register/office locator; discrepancies; and the next source.
All source-dependent fields are nullable. Use `not supplied`, `not examined`, `unreadable` or
`unresolved discrepancy` to explain the gap instead of filling it with an inference.

## Prompt pattern

> Build a burial evidence packet from these cemetery records and photographs. Keep candidates
> separate. Preserve raw Hebrew and secular inscriptions, name roles, death and burial dates,
> calendar labels, plot/GPS identifiers and source URLs. State which images were inspected.
> Leave unsupported fields unknown; list discrepancies and the next original record to retrieve.
> Do not choose an identity or final date from the database label alone.
