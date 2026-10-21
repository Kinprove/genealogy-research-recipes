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

For a bilingual stone, transcribe the Hebrew and secular-language portions separately. The
gravestone tutorial demonstrates the deceased's Hebrew given name and the father's Hebrew name
as useful leads that can be absent from the secular portion. Preserve the raw wording, the
person's stated role and uncertain letters before adding a translation. Do not require every
stone to contain the same fields. [P1, O1]

Before treating a word on a Hebrew stone as a surname, check whether it is a status or occupation
marker, such as כ"ץ for a kohen, הלוי for a Levite, or, less certainly, שו"ב for a ritual
slaughterer. Record the literal letters and the proposed expansion separately. Assign the title to
the man it follows: after a woman's patronymic, it describes her father, not her. Try to find the
person in the locality's records for the period by given name and father's name rather than by the
apparent surname. The [matzevah-reading discussion](https://forum.j-roots.info/viewtopic.php?f=208&t=9621)
and [title question](https://forum.j-roots.info/viewtopic.php?f=75&t=7576) motivate this. כ"ץ (Katz) can be a real surname in other contexts, and neither thread proves an identification. A conflict such as
'bar' followed by a female name stays unresolved until the image is checked.

Keep the dates separately:

| Field | What to retain |
| --- | --- |
| Death date on inscription | Literal English/secular and Hebrew forms, each with its label |
| Burial date | The date explicitly supplied as burial, with its source |
| Database date | Displayed value, field label and record URL |
| Converted date | Separate derived value, calendar and conversion basis, if checked |
| Unreadable or absent value | Unknown; no guessed completion |

**Check:** An unread inscription, missing date or unverified conversion stays unknown. The
packet records the source statements and does not select a final death date. [P1, O1]

If a source reports reinterment or a replacement marker, retain original burial, reported
transfer and later marker installation as separate source-linked events. Keep original and
present cemetery/plot locators separately; seek the relocation or register evidence for an
unresolved transfer. A new marker does not date the burial or identify the remains. The
[George Estes dedication example](https://dna-explained.com/2023/09/19/calling-all-descendants-of-george-estes-1763-1859-youre-invited-to-his-revolutionary-war-grave-dedication-52-ancestors-410/)
motivates this event chain without independently verifying the reported relocation.

## 4. Carry the hit to the plot and cemetery records

Save the cemetery's name, address, section and plot exactly as supplied. JOWBR's full record or
cemetery link can provide cemetery contact information and maps. A BillionGraves photograph may
have GPS information; the cemetery-program tutorial demonstrates using its map to locate a
marker. Record a supplied coordinate as a coordinate, and a section/plot reference as a separate
locator. [P2, O1]

When the plot cannot be located or the online entry lacks detail, identify the cemetery office
and prepare a request for the recorded burial and its plot location. The gravestone tutorial
recommends asking the office before visiting. Give the candidate name, known date, cemetery and
any existing locator; request the corresponding register entry or available burial information.
Send the request only when contact is authorized. [P1]

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
