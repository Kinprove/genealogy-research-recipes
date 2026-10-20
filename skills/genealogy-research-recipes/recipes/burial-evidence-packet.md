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

For a bilingual stone, transcribe the Hebrew and secular-language portions separately. The
gravestone tutorial demonstrates the deceased's Hebrew given name and the father's Hebrew name
as useful leads that can be absent from the secular portion. Preserve the raw wording, the
person's stated role and uncertain letters before adding a translation. Do not require every
stone to contain the same fields. [P1, O1]

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

When an inscription supplies a death date and age in years, months and days, retain both
literal inputs before calculating a birth-date lead. Amy Johnson Crow's example counts
back the years, then months, then days, carrying the year and using the actual length of
each month crossed. Record that arithmetic and its calendar basis with the calculated
value. Incomplete age units, an uncertain calendar or unresolved month-end/leap-day
conventions do not support a unique exact birth date; leave the calculation unresolved
where its basis is missing. The recorded age may itself be inaccurate. Keep a separately
stated birth date alongside the calculation and send a conflict to evidence and proof
judgment, rather than overwriting either value. [P6]

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
or entitlement to the records. [P5]

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

If an online memorial assigns an early burial to a named cemetery, compare the burial date
with that cemetery's documented opening or operating period. An opening after the burial
excludes it as the original burial ground; keep a later reinterment or marker transfer
unresolved until its own evidence is found (section 3). Record the dating source and any
uncertainty about earlier use of the site. Use the burial entry's parish or church and the
locality's cemetery histories to list grounds operating at the burial date as candidates,
with a source for each period and parish connection. A candidate ground does not locate
a grave. The [Anne Doucet example](https://dna-explained.com/2025/01/04/anne-doucet-1713-1791-oceans-rivers-and-perseverance-52-ancestors-438/)
motivates this chronology check; its proposed final grave location remains unverified. [P4]

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
