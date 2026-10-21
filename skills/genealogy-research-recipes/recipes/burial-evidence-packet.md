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

For a difficult inscription, an optional second photograph uses light directed from the side
by a hand-held reflector or flashlight, held clear of the marker. Keep the ordinary-light and
side-lit views together, label the surface and lighting, and leave uncertain letters unresolved.
This step does not involve rubbing, cleaning, wetting or touching the marker. [P6]

For a family monument, inspect available views of its front, reverse and lower additions.
Label the surface shown and keep unseen or unreadable parts explicit. For each named person,
retain the literal burial-place statement and its image/surface locator separately from the
monument's physical cemetery and plot. A family monument can name people buried elsewhere;
compare their location statements with available burial records instead of assigning everyone
named on the monument to its plot. Unresolved burial locations stay open. [P5]

For a bilingual stone, transcribe the Hebrew and secular-language portions separately. The
gravestone tutorial demonstrates the deceased's Hebrew given name and the father's Hebrew name
as useful leads that can be absent from the secular portion. Preserve the raw wording, the
person's stated role and uncertain letters before adding a translation. Do not require every
stone to contain the same fields. [P1, O1]

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

If a form can capture the device's current position, use that control only while physically at
the intended site. When entering information off-site, leave current-position capture unused.
Retain where the coordinate came from and what point it represents; keep an independently
supplied coordinate with its source instead of replacing it with the contributor's location.
Unknown point meaning stays unresolved. The dated Cemetery Registry demonstration motivates this
capture-origin check, not a guarantee of coordinate accuracy, grave identity or access. [P4]

When the plot cannot be located or the online entry lacks detail, identify the cemetery office
and prepare a request for the recorded burial and its plot location. The gravestone tutorial
recommends asking the office before visiting. Give the candidate name, known date, cemetery and
any existing locator; request the corresponding register entry or available burial information.
Send the request only when contact is authorized. [P1]

Where the actual source offers it, inspect the matched plot's roster before a bounded
neighboring-plot search. Retain each burial/plot identifier and the actual distance or selected
area separately from coordinates. Use co-burial/proximity to nominate associates and retrieve
their burial records before proposing a relationship. The [co-plot search description](https://lostrussianfamily.wordpress.com/2025/10/25/free-database-offers-more-than-5-million-indexed-burial-records-for-moscow/)
supplies no fixed search radius or current provider/plot-accuracy guarantee.

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
