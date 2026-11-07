# Recover a Polish original from an index or archival description

## Contents

- Goal
- Inputs and routing
- 1\. Preserve the index lead before following SKAN
- 2\. Use the description to identify the holding series
- 3\. Move from the unit to the original entry
- 4\. Classify the gap and choose another holding route
- Completion packet and prompt

## Goal

Turn a Polish index entry or register description into an inspected original entry, or a precise
retrieval gap. Carry the locality, confession, event year and act number across Geneteka,
Metryki and Szukaj w Archiwach without confusing an index, a PRADZIAD description, a fonds,
an archival unit and a scan.

## Inputs and routing

Start with the index row or desired event, its supported locality and approximate date. Resolve
an ambiguous locality before selecting a holding archive. Use the existing research-documentation
recipe for the ordinary log and source-citation for citation construction. FamilySearch and
Ancestry have their own holdings, internal-index and access workflows. JewishGen search and family
reconstruction, broad origin-place recovery, transcription and identity judgment remain with
their respective recipes.

This workflow begins at a Polish index or archive lead. It does not reconstruct the emigrant's
origin town or create a general list of Polish research websites.

## 1. Preserve the index lead before following SKAN

Copy the displayed name, event type, year, parish or registration district, confession if supplied,
act number, comments and index URL. Keep each candidate separate. Do not convert an act number
into an image number.

Where Geneteka supplies a **SKAN** link, follow it and inspect the destination's register
description and actual entry. If the link is absent or fails, keep the row as an index lead and
record the failure. The absence of that link establishes no absence in other image portals or
the holding archive. The Polish-records guide demonstrates both Geneteka's scan links and a
subsequent Search the Archives route. [P1]

Before you trust a Geneteka row or a miss, set the search to fit the lead. For the former eastern
lands, select the **Ukraina**, **Białoruś** and **Litwa** territories as well as the modern
voivodeships, and check coverage for each act type. To find a person as a parent, leave
**Nie wyszukuj w rodzicach** (do not search parents) unticked; a child's birth row is not the
parent's birth. Use **Wyszukaj jako para** (search as a couple) for a couple.
**Wyszukaj również w pobliskich parafiach (15km)** adds nearby parishes; a hit there does not place
the person in that parish. Some indexed data has no available scans. [O2], [O3], [O4]

A results page read with a fetch or HTML tool can show the column headers and no rows, even for a
very common surname; one such fetch on 2026-11-02 also showed no result counter. Check the loaded
rows and the counter in a real browser, and never log NIL from such a fetch. [O3]

A Geneteka miss does not exhaust the Polish indexes. Search the regional projects whose area fits
the parish: Poznań Project (Wielkopolska marriages, 1800–1899), BaSIA (western Poland), Lubgens
(Lublin region), Projekt Podlasie (Podlasie and Mazovia), GENEO at JZI (Suwałki and Augustów
area), Świętogen (Kielce region), PomGenBaza (Pomerania) and JRI-Poland (Jewish records).
Geneszukacz checks a surname only across Geneteka and three other Polskie Towarzystwo
Genealogiczne lists (1918–1920 soldier lists and the 1926 Polish declaration for the United
States); it does not search the regional projects. Log each project searched and its coverage for
the parish before you record NIL. [O5], [O6], [O7], [O8], [O9], [O10], [O11], [O12], [O13]

Search every form of a woman's surname. A surname ending in a consonant other than -g takes -owa for a wife and
-ówna for a daughter (Nowakowa, Nowakówna); one ending in a vowel or -g takes -ina/-yna and -anka
(Konopczyna, Konopczanka); -ski becomes -ska. [P4], [P6] A maiden name is written z + genitive
plural: "z Kowalskich" means née Kowalska. The same construction can name a place of origin, so
read the plural family-name form before taking it as a maiden name. [P5] If an indexed maiden name
matches no known surname, open the image for a misread "z …" phrase, then search the rebuilt base
form and the indexed form as separate lanes.

A name joined by "vel" or "alias" (Nowak alias Vilk) is a second name of the same person, not a second
person, and records may show either name alone. Search each element and the compound, copy the
compound as written, and do not treat a switch from one element to the other as a new family
without looking for the joined form. [P5], [P6], [P7]

**Output:** `index URL | candidate | locality/district | confession | event | year | act |
comments | SKAN destination | observed link result`.

**Check:** The destination image shows the event and act being pursued. A matching name in
another year or register is another candidate.

## 2. Use the description to identify the holding series

In Szukaj w Archiwach, use **Search vital records** to investigate the relevant registration
locality. Inspect the returned years, confession, record type and holding archive. A parish or
registry-office seat can be the catalog locality even when the person lived elsewhere. [O1]

Alternatively, the documented direct search uses **Akta stanu cywilnego** plus locality, with
the parish or synagogue district where supported. The official examples distinguish a Roman
Catholic parish from an **Okręg Bożniczy**, a synagogue district. Select the series that fits
the lead; do not substitute a modern municipal name for the record creator. [O1]

Treat PRADZIAD as a finding aid. It is searched inside Szukaj w Archiwach: choose **PRADZIAD**
in the document-type list, or use **Search vital records**, whose rows carry PRADZIAD description
fields. Its descriptions can identify locality, confession, years, record type and archive;
**PRADZIAD does not contain scans**. To investigate scans, follow
the supplied reference code into the archival fonds, then open **List of files**. The official
instructions say that the file list shows available units and scan counts. [O1]

For the Akta Stanu Cywilnego (ASC, the civil-status registers kept by each confession) that AP
Katowice describes, the duplicates went to the competent local courts from the early nineteenth
century, and the state archive now holds them. [O14] Record which copy an
image or index row comes from. Before you call an entry unreadable or unannotated, look for the
other copy and record its custodian.

Do not infer the parish's location from the city of the holding archive. A [Polish
archive-holdings discussion](https://forum.j-roots.info/viewtopic.php?f=165&t=470) shows that a
register answered by a Warsaw archive came from an Archiwum Główne Akt Dawnych (AGAD) inventory of
registers from the "eastern territories", not from a Warsaw parish. Identify the fonds, its
inventory and the unit signature, and treat the parish's location as unresolved until that
description or another source places it. Record whether the signature has scans. The source covers
only this inventory, not AGAD's full scope or current scan coverage. [C1] For Eastern Galician
metrical books in Lviv (TsDIAL) and Warsaw (AGAD), see
[Route a Galician or Bukovinian record by date, confession and custodian](galicia-bukovina-habsburg-record-routing.md).

**Output:** `description URL | creator/locality | confession | record type | described years |
archive | full fonds reference | unit/year needed | scans listed`.

**Check:** A register description establishes a lead to holdings, not that the target entry
has been inspected. Preserve the complete reference, not just a short number detached from
its archive and fonds.

## 3. Move from the unit to the original entry

Open the unit that contains the required year and event type. Check its register title,
identification pages and actual content before searching for the act. Use a photographed index
where available, or define a bounded page range to browse. Record the act/page reference and
the image locator separately.

For a marriage in an ASC fonds from the Congress Poland civil-status system, check the fonds'
**List of files** for a separate annexes unit (alegata) for the same year as well as the
register. The annexes hold the dated supporting papers, such as birth extracts and banns
certificates, whose content the register entry leaves out. Cite each paper as its own source with
its own date, and do not use any of them as the marriage date. Where the parish kept only church
metrical books, as in the former Russian western provinces, do not expect an alegata unit.
[O16], [P10], [P11], [P12]

When Metryki covers the relevant register, the demonstrated route is region → parish → available
years/record type → scans. The tutorial follows those choices into a register image; this is
a second retrieval route, not a promise that every Polish parish is included. [P2]

Match the original's event, year, act and participants to the index lead. Preserve material
differences between the index and the image, including an uncertain name or date. Use the
documentary-records recipe for the reading and the evidence-judgment recipe for any identity
conclusion.

**Output:** `archive/fonds | unit | register title | event/year | act | printed page |
image URL/ordinal | inspected range | original reading | index discrepancy`.

**Check:** The chain ends at the entry, with enough context to identify its register. An act
number, printed page and viewer ordinal are separate coordinates.

## 4. Classify the gap and choose another holding route

If the central portal does not expose the image, check the holding archive's own digital portal.
The Eastern European research interview specifically describes regional Polish archival portals
with digitized material not yet integrated into the central portal. Check the current regional
catalog rather than assuming that this historical observation applies to every archive. [P3]

In Szukaj's vital-record results, **no fonds** means that the fonds is currently unavailable on
that website. It does not mean the archival documents never existed. If the needed unit has no
online image, preserve its reference and prepare an image/copy request to the identified holder;
contact remains a separately authorized action. [O1]

For a 20th-century civil-status register, do not assume the state archive is the holder. A
[civil-registry custody discussion](https://forum.j-roots.info/viewtopic.php?f=4&t=4667) reports
that many such books are still held by the local civil registry office (Urząd Stanu Cywilnego).
When the archive's catalog shows no unit for a recent year, check the current USC custody for that
locality before sending the request. Do not label the record missing. [C2]

The Civil Status Records Act (Prawo o aktach stanu cywilnego, Dz.U. 2014 poz. 1741) sets the
transfer rule for books kept before 1 March 2015. The USC passes a book to the competent state
archive 100 years after the birth book was closed, and 80 years after the marriage or death book was
closed. When one volume holds several books, the period runs from the closing of the last of them
(art. 128(1)). A book whose period ended after 1 March 2015 goes to the archive within two years of
that date (art. 129(3)). A birth or marriage book stays at the USC longer while a person entered in
it has no death act or registered death; if that person has no PESEL number, the USC may transfer
the book anyway (art. 128(1a)–(1b)). [O17]

So a book older than 100 or 80 years can still be at the USC. Once the period, including that
extension, has run out, the USC issues no certificate (odpis) from the book. Until it transfers the
book, it gives access under the archives act (art. 130(3)–(4)). [O17]

**Privacy gate:** <!-- privacy-gate: request --> A USC request can reach a book that still holds
living people, which is why the book stayed at the office; answer the privacy gate in `SKILL.md`
before sending it.

Ask the USC that holds the book for access to the named book and entry before you call it lost, and
record whether it granted access or refused. [O17]

For a Congress Poland (Kingdom of Poland) civil-registration register, expect Polish entries until the end of 1867.
A regulation required Russian from 1 January 1868, so expect Russian from 1868 and confirm it
from the language of each transition year's entries and its index. Do not expect a Latin-to-Russian switch in these registers. [P8], [P9] Use the year's language to choose the search spelling
and to judge whether a Cyrillic or index spelling re-transliterates a Polish original.

When preparing the request, give the surname in both Polish and Russian (Cyrillic) forms. List the
known spelling variants and ask explicitly for similar-sounding names to be checked. A [Polish
archive-request discussion](https://forum.j-roots.info/viewtopic.php?f=165&t=470) reports that
archives do not widen a search unless asked. Treat a match on a variant as a candidate, not as an
identity. [C1]

When the vital-record route stops and you turn to printed context, Polona, the National Library of
Poland's digital library, holds digitised books, periodicals and daily newspapers (browsable by
date in its press panel), maps, flyers and posters. Treat its OCR text layer as a lead and cite the
publication and page from the image. [O15]

Use one gap label per unresolved route: `index only`, `broken link`, `fonds unavailable on portal`,
`unit described without scan`, `access blocked`, or `bounded range inspected without candidate`.
Keep uninspected and inspected material separate.

## Completion packet and prompt

Deliver the index row, description and fonds/unit chain, original image and inspected range, or
the exact unresolved link in that chain. Include the next portal, unit or holder to check.
Do not describe the original as missing when only an access route failed.

> Recover the original Polish entry behind this index or description. Preserve locality,
> confession, event/year/act, holding archive, full fonds reference, unit, original page and
> image locator separately. Show every completed step and actual access outcome. Compare the
> entry with the index; retain uncertain readings and competing candidates. If retrieval stops,
> identify the exact gap and next holding route without inventing a scan or identity.
