---
id: "myheritage-historical-record-search"
title: "Recovering historical records with MyHeritage"
summary: "Recover MyHeritage historical records hidden by collection coverage, search fields, name variants, languages or OCR."
kind: "platform"
scope: {"platforms": ["myheritage"], "tasks": ["no-result searches, Collection Catalog, relative pivots, historical jurisdictions, newspaper keywords/OldNews or an index that must lead onward to an original record."]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "MYHERITAGE-HISTORICAL-RECORD-SEARCH-01", "text": "Preserve the sparse baseline before tightening it. If a tighter query fails, relax one condition at a time and record the reason; changing everything together conceals what excluded the record."}]
handoff: ["ai-for-documentary-records", "beider-given-name-variants", "evidence-proof-judgment"]
checked: "2026-11-12"
checked_basis: "Rechecked 2026-11-12"
capabilities: {"browse": ["myheritage"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool", "export"], "contact": []}
router: {"section": "Record websites, libraries and maps", "group": "Record websites", "order": 46}
---

# Recipe: Recovering historical records with MyHeritage

## Contents

- Goal
- The mental model
- Operating rules
- Fifteen practical howtos
- Prompt-craft
- Pitfalls worth internalizing

## Goal

Recover candidate historical records when a MyHeritage search fails or returns too much.
Diagnose coverage, indexed fields and restrictions; preserve what was searched and what changed.
All worked examples below are synthetic.

## The mental model

Collections, indexes/OCR, supplied fields, matching rules and displayed presentation can each hide
or distort a relevant record. Change one layer at a time and compare the returned evidence.
A successful retrieval still needs identity verification.

## Operating rules

- Separate **documented facts, estimates and hypotheses** before constructing a query. Do not
  require a guessed maiden name, calculated birth year or uncertain birthplace in every search.
- Check the collection description and actual form. Categories and individual collections offer
  different fields; a field offered by the general search is not a promise of complete indexing.
- Names are optional search inputs. Use the offered spelling, initials and additional-field
  controls deliberately; do not assume an old demonstration describes today's defaults. [H1]
- Preserve the sparse baseline before tightening it. If a tighter query fails, relax one condition
  at a time and record the reason; changing everything together conceals what excluded the record.
- Verify original wording and the person's role. Transliterated results, OCR, extracted relatives,
  inferred dates, trees and automated matches are finding aids, not independently established facts.
- Route AI transcription/translation to `ai-for-documentary-records.md`, bounded Ashkenazi given-name
  lookup to `beider-given-name-variants.md`, and identity/conflict/negative-evidence rulings to
  `evidence-proof-judgment.md`. This recipe prepares candidates and search coverage, not a verdict.

## Fifteen practical howtos

### 1. Search the catalog for record sets before searching their people

Clear previous catalog filters, then try jurisdiction and record-type words in the collection
title/description search: school, register, passport, probate, newspaper. These keywords locate
collections; they are not a search for every personal name inside their records. [S2, H2]

For Jewish research, try Jewish-related descriptions alongside the relevant town and civil,
religious or national record groups. A neutral collection title may contain relevant material.
Neither a keyword match nor its absence establishes complete coverage of a community. [S4]

For wills, check both **Wills & Probates** and **Court Records**. Try `notarial` in the catalog
with the relevant jurisdiction as well. **Netherlands, Notarial Records, 1600–1935** includes
wills alongside other deeds, so a title search for `will` alone can miss a useful collection
[S49 @2026-11-20] [S50 @2026-11-20] [S51 @2026-11-20].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Names and case or prison details that identify people who may be living go to MyHeritage when these collections are searched. Keep those terms local until the gate is answered.

For a Scottish civil dispute, search **Scotland, Court of Session Processes, Acts and Decrees,
1560–1930**. Use the case date and description to distinguish people with the same name
[S61 @2026-11-21]. For criminal proceedings, start with the court or prosecution series instead
[S62 @2026-11-21].

Use **Scotland, Crown Counsel Procedure Books** to identify a possible prosecution
[S56 @2026-11-21]. For a Crown Counsel opinion in the AD9 series, read the disposition.
Some cases went to the High Court or Sheriff Court and others were dropped. Use the named court
to look for trial papers and leave the trial unresolved until you find them [S57 @2026-11-21].

For Scottish custody, check **Scotland, Prison Registers** for historical admissions of women
and children as well as men. Keep the prison and admission year distinct from the person's
residence and birth details [S56 @2026-11-21] [S58 @2026-11-21] [S59 @2026-11-21].
The registers include untried prisoners. Verify any trial or conviction separately
[S60 @2026-11-21].

### 2. Check coverage and remove filters that hide useful collections

Use catalog type, location and time filters to discover plausible sets, then read their descriptions.
Check date span, locality, record type, source institution, image availability and update information.
A broad title is not assurance that every town, year or surviving volume is included. [H2, H3]

Repeat discovery without an images restriction: an index may provide the locator needed elsewhere.
A collection-level image indicator does not guarantee an image for every entry. Clear accumulated
filters when changing jurisdictions, and preserve promising index-only collections in the ledger.

MyHeritage describes **France Deaths** as an index of INSEE data that can include births and deaths
abroad [S33 @2026-11-20]. Keep those places eligible. The provider estimates that the index captures
about 8% of deaths in 1970 and about half in 1971 [S33 @2026-11-20]. After a zero in either year,
leave the death unresolved and check the civil death register for the known locality. INSEE identifies civil
registration reports as the underlying source [S34 @2026-11-20].

In **Latvia, Jewish Birth Records from JewishGen**, check the town and year before interpreting
a miss. The index spans 1838–1921, with most entries from 1854–1909
[S29 @2026-11-20] [S30 @2026-11-20]. Check coverage of the town's registers outside that concentration.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Names, event dates and places that identify anyone who may be living go to MyHeritage when you rerun a query or search the India indexes. Apply the same check to the other collections below and keep identifying terms local until the gate is answered.

For **Germany, North Rhine Westphalia, Deaths 1874–1938**, identify the specific registry office
(*Standesamt*) and year. The 2022 district list and later Aachen-to-Rheydt office range describe
individual releases [S98 @2026-11-22] [S99 @2026-11-22]. The collection description includes parts of Düsseldorf and
Köln [S100 @2026-11-22]. After a miss, use the office and year to check the Landesarchiv Nordrhein-Westfalen’s
finding aid for the duplicate death register [S101 @2026-11-22].

For a Cheshire baptism, compare **Cheshire Parish Births and Baptisms** with **Cheshire Bishop’s
Transcripts Baptisms**. For a marriage, use **Cheshire Bishop’s Transcripts Marriages** alongside
the parish register [S105 @2026-11-22]. The bishop’s transcript is an abbreviated copy. If the register is
missing or illegible, check the transcript for the same parish and year. Record which version
you examined and check the parish holdings through Cheshire Archives [S106 @2026-11-22].

In **France, Church Marriages and Civil Marriages**, open the image and identify whether it
shows banns, a church marriage or a civil act [S110 @2026-11-22] [S108 @2026-11-22] [S109 @2026-11-22]. Use a banns entry to look for
the marriage act. Check departmental coverage and turn to the local registers after a miss [S109 @2026-11-22].

When revisiting an earlier search, set the Collection Catalog sort to **Last Updated**. Compare
the dates on relevant collections with the date of your earlier search and rerun the query in sets added
or revised since then [S54 @2026-11-21] [S55 @2026-11-21]. A recent update by itself establishes
nothing about the town or years added.

For a suspected death in Finnish military service, search **Finland, Second World War Casualties**
within MyHeritage’s stated 1938–1944 scope. Record unit, rank, death date and place, and burial
place separately. If the entry mentions a disappearance, capture or wound, record it as a
separate event [S137 @2026-11-23]. When the death is uncertain or falls outside
the stated span, check the National Archives of Finland’s guide for the service card
(*kantakortti*) and the series for the incident [S138 @2026-11-23].

For an 1851 Scottish household, check the **1851 Scotland Census Extract** for a lead and
confirm access in the user's account [S52 @2026-11-21]. Use the locality and household details
from a hit to find the return image on Scotland's People [S77 @2026-11-21].

For a Piotrków Trybunalski birth, check **Piotrków Trybunalski Poland Births, 1808–1875**
and verify access in the user's account [S52 @2026-11-21]. The collection indexes Jewish births.
If the community or year falls outside its scope, start with the appropriate local registers
[S78 @2026-11-21] [S79 @2026-11-21].

For India, match the event to **India, Births and Baptisms, 1786–1947**,
**India, Marriages, 1792–1948**, or **India Deaths and Burials, 1719–1948**
[S82 @2026-11-21] [S83 @2026-11-21]. Check coverage of the specific place and community.
If coverage is missing or unclear, follow the family to its local religious or community
records or regional archives and keep the event unresolved [S82 @2026-11-21].

### 3. Run a sparse → tight → relaxed ladder

Start sparsely, select a suitable collection, then add one supported event or relative.
If candidates disappear, remove the weakest condition first. [S1, S6, H1]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A scoped query may send names, dates or places identifying people who may be living to MyHeritage. Hold those terms locally until the gate is answered.

When tree profiles crowd out documentary results, select **Historical records** on desktop
or **All Collections → Records** on mobile web if the filter is available [S95 @2026-11-22]. Log that
scope. Search Connect lists other users’ queries under **Family Trees** [S97 @2026-11-22]. Switch
back to **All Collections** for a separate pass if you need tree leads [S95 @2026-11-22].

Before running a sensitive query, check **My Privacy → My member preferences → Enable Search
Connect**. Have the user clear that option if they want to keep their search terms out of Search
Connect and disable recent searches [S95 @2026-11-22] [S96 @2026-11-22]. Search Connect can expose query details to
other members [S97 @2026-11-22]. Keep the research log local if the query must stay private.

If **Recent searches** is available, identify the card by the query’s name, birth year and place,
then reopen the query from that card. Log the filters you actually see before comparing the
results. Use the card’s **X** to remove it from the list. Check **Search Connect** separately
when the goal is to stop future searches from appearing there [S95 @2026-11-22].

Use the historical-record search form when an older guide directs you to the original
**AI Record Finder** Chat tab [S118 @2026-11-22]. MyHeritage retired that beta on 2024-08-09 [S117 @2026-11-22].

Run the target query from the category or subcategory form when you know the record type. For a
single set, open its own form from the Collection Catalog or the category's collection list. Log
that scope before returning to global search [S28 @2026-11-20] [H1 @2026-11-20].

Keep the all-terms exact-match switch off for the sparse baseline. Use field-level name matching
when only the name should be exact. Turn on all-terms exact matching only when you intend to
require exact matches on all the entered terms [S28 @2026-11-20] [H1 @2026-11-20].

**Synthetic walk-through:** Anna Weiss's marriage in 1911 is documented; birth in 1887 and
Millford birthplace are estimates. Suppose requiring exact spelling and both estimates fails.

1. **Sparse:** In a suitable marriage collection, search Anna Weiss without birth year/place;
   keep exact given-name matching enabled.
2. **Tight:** Keep that exact-name constraint and add only the documented marriage year, 1911;
   compare the returned candidates.
3. **Relax:** Keep the collection and 1911; loosen exact given-name matching to admit initials
   or variants where the form supports them. Inspect each candidate's original wording.

These are proposed queries, not reported results. Keep each attempt and its reason in the ledger.

For a common first name and surname, try a documented, distinctive middle name as a separate
**Keywords** query under **+ More**, if the form offers it [S66 @2026-11-21] [H1 @2026-11-21].
Compare it with the baseline before requiring that middle name in later searches.

### 4. Search the name as it might actually have appeared

Create a short variant list: native spelling, maiden and married surnames, familiar given name,
initials and middle names. Try fictional Anna Maria Weiss as Anna Weiss and Maria Weiss, then the
documented married surname. Use offered initials matching or exact-spelling controls consciously. [H1]

Do not type `*` or `?` into a MyHeritage name field to generate variants. MyHeritage's search-engine
help documents exact-match, spelling-variation and initials options and no wildcard syntax
[H1 @2026-11-12].

A Family Tree Magazine guide last updated in November 2026 reports that MyHeritage
supports neither character [S18 @2026-11-16], and MyHeritage's Knowledge Base says its own variant
matching should make wildcards unnecessary [S19 @2026-11-16]. A 2025 MyHeritage blog post gives `*`
a fixed letter range [S17 @2026-11-16]; neither that help page nor the Knowledge Base article
documents the rule, so do not adopt it.
Admit variants with the spelling-variation option and enter each listed spelling as its own query.
A wildcard query that returns nothing has not searched the variants.

An exact form can reduce a common-name result set, but also exclude abbreviated or reordered text.
In newspapers, a woman may appear under her husband's name or an honorific. Test those forms as
separate leads; do not turn a familiar name or shared surname into an identity conclusion. [S1, S3, H5]

For a known deceased person in the **Index to Soviet Extraordinary Commission Pinsk Records from
JewishGen**, try the surname alone or with the given-name initial. The index can reduce the given
name to an initial, so a compulsory full name can hide a candidate [S29 @2026-11-20] [S31 @2026-11-20].

### 5. Preserve native names beneath translated results

MyHeritage's Global Name Translation can match name versions, nicknames and different alphabets,
and transliterate returned names into the query language. That convenience can hide the precise
original spelling. Save the native name alongside the displayed version. [S1, S4, H4]

In the search form, the filters under **+ More** include an option to show results from other
languages [H1 @2026-11-12]. Record its state with each query. With the option off, a zero says
nothing about records in other languages or scripts. With it on, a zero still does not prove
absence. In the Internet Archive capture of 2026-07-17 of a MyHeritage collection page, the search
form's tooltip says a translation shown in square brackets is not in the original data and may be
inaccurate [H12 @2026-11-12].

Where possible, inspect the original record and retry a documented native spelling separately.
Treat plausible name equivalents as search alternatives, not interchangeable evidence. Ask a
qualified reader about ambiguous letters; verify transcription and translation as separate tasks.

### 6. Attach every date to the event it describes

Distinguish birth, marriage, death, residence and publication dates before choosing a field.
Current search forms support year or full-date entry; use the precision the evidence warrants.
If a range control is unavailable, test neighboring years separately or omit the weak date. [H1]

A school yearbook's publication year differs from a pupil's birth year. A birth year inferred from
grade or age remains an estimate. An obituary's publication date may follow the death; an article
can commemorate an event decades earlier. Do not force all those dates into birth-year search. [S3, S6]

In a civil registration index, verify whether a quarter denotes registration rather than birth;
keep certificate volume/page locators. A pension file can be created years after military service:
do not restrict discovery to the war years alone. [S5, S9]

When a marriage index gives both a license issue date and a marriage date, log them separately.
If the entry gives only the issue date, leave the ceremony date open and look for a completed
certificate or return that records it. [S23, S24]

In **New York, Chemung County Births**, keep the child's birth date and the announcement's
publication date in separate fields. Use the surname and parents to identify the intended
notice [S61 @2026-11-21]. Use the publication date to locate the issue in the Chemung County
Library District's newspaper holdings. A missing notice leaves the civil birth entry open
[S63 @2026-11-21].

### 7. Separate the person's place from the record's place

Identify birthplace, residence, event location, publication town and collecting jurisdiction.
A fictional death in Millford may be reported by a newspaper published in nearby Ashbridge.
Try Millford as a keyword while broadening the publication-place restriction. [S6]

Check neighboring towns, historical spellings and jurisdictions created by border changes.
Search the countries under which the locality's records might be cataloged, then inspect the
collection description. A modern national filter can conceal records organized another way. [S1, S5]

A Germany birthplace can appear in a U.S. census return [S8]. Follow the collection title and its creator to identify the source. Conversely, U.S. nationals who served with Canadian forces may appear in Canadian military records [S9]. Record the person’s role and the jurisdiction responsible for the record separately.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Names, birthplaces or other search details identifying people who may be living go to MyHeritage when the query runs. Keep those details local until the gate is answered.

Check **Germany, Revoked Citizenships and Property Seizures from JewishGen** for 1933–1945
citizenship, property or business sanctions. Keep former German residents and people in annexed parts of
Czechoslovakia in scope. Read the type of action and last residence before interpreting the entry
[S29 @2026-11-20] [S32 @2026-11-20].

Include the **Lithuanian-Jewish Revision Lists from LitvakSIG** for a relevant locality now in
Poland or Belarus. Check the historical district and nearby places of registration, even if the
family lived elsewhere. Check which years survive before interpreting a gap in the results
[S102 @2026-11-22] [S103 @2026-11-22] [S104 @2026-11-22].

For Spanish Civil War exile research, try **Spain, Migration to the Americas, 1880–1930** without
requiring the title's date range or a Spanish birthplace [S35 @2026-11-20] [S36 @2026-11-20].
MyHeritage illustrates that exception with a 1942 Mexican immigration entry for an exile born in
Paris who had lived in Valencia [S35 @2026-11-20].

In **France, Naturalizations**, use the decree date from the index to find the published decree.
Check both the *Bulletin des lois* and the *Journal officiel* for publication in 1924–1930.
Residence in France leaves naturalization an open question
[S37 @2026-11-20] [S38 @2026-11-20] [S39 @2026-11-20].

Check **Netherlands, Batavian-French Army Studbooks, 1795–1813** when service may have
crossed Dutch and French commands [S58 @2026-11-21]. For the Dutch studbooks, use the
Nationaal Archief's inventory **2.01.15** and record the inventory item and folio. If a name
is missing, check the supplementary extracts before drawing a conclusion about the person's
service [S64 @2026-11-21].

If an arrival search fails for a traveler who may have sailed from Gothenburg, try
**Sweden, Gothenburg, Passenger Lists 1869–1951**. Use the departure date, transit port and
destination, where shown, to choose the next passenger list. Keep the Swedish departure
and the eventual arrival as distinct events [S71 @2026-11-21] [S72 @2026-11-21].

For a deceased traveler who may have booked with the Holland America Line, search MyHeritage
collection **20275, Netherlands, Holland-America Line, Passenger Lists**, for 1900–1969. Keep the
booking place, departure port and date, ship, and recorded arrival place in separate fields
[S134 @2026-11-23] [S135 @2026-11-23]. Check the Rotterdam City Archives scan and its passenger
count. A group booking can carry only the booker’s name. If a suspected companion is missing
from the list, try the booker in MyHeritage and check an arrival manifest for the voyage
[S136 @2026-11-23].

### 8. Find the target through a better-documented relative

Use the additional-fields control, currently labelled **+More**, for relatives, life events,
keywords or gender where offered. Test a known parent or spouse when the target's own name or
dates are missing. Avoid filling every relative field with guesses. [S1, H1]

Alternatively search the relative directly, then inspect their household or named associates.
In passenger records a person can appear as a destination contact or relative remaining abroad,
as well as a traveler. Read the role and column: a name hit does not establish immigration. [S5]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> If the query identifies anyone who may be living, their name or other identifying terms go to MyHeritage. Hold the query locally until the gate is answered.

Run a parent-name search with the principal's name blank. In MyHeritage's **New York City Births,
1866–1909**, start with the **Mother** field and inspect the child's recorded name in the hit
[S20 @2026-11-18] [S21 @2026-11-18]. In **New York City Marriages, 1866–1949**, try a known parent
of either spouse, since MyHeritage indexes parents as searchable people [S20 @2026-11-18].

### 9. Replace a weak name with a distinctive contextual clue

In a text-searchable collection, try an address, occupation, employer, school activity, place,
relative or unusual event. For fictional Samuel Reed, compare his name plus Oak Street with his
name plus a documented workshop. Search the strongest clues separately when their combination fails.

A property advertisement or legal notice may identify an address without naming the ancestor.
Use period occupation terms, street-name variants and relevant local vocabulary. A contextual hit
locates a page to read; it does not establish who occupied the address at another date. [S2, S3, S6]

For a documented local business, locality and period, consider an available local school yearbook
from that period and inspect its actual advertising section, often near the back. The business
owner need not be known as a pupil. Record the school, edition/year and page or image locator
with the advertisement's literal business name, address and any pictured premises, then seek
corroborating records. An advertisement alone does not establish ownership, school attendance
or patronage. Keep an unavailable edition or uninspected section as a gap. [S10, S11]

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A relative’s name used as a cemetery keyword goes to MyHeritage. Keep the name local if the relative may be living until the gate is answered.

In **Canada, Gravestones and Memorials**, run a documented relative’s name in **Keywords**.
That searches the inscription transcription, where a person can be mentioned without being the
principal name in the entry. Check the inscription before assigning the principal’s dates or
burial place to the relative [S111 @2026-11-22] [S112 @2026-11-22].

### 10. Move from a person-name index to full text when available

Check whether the same material has a structured name index and a full-text counterpart.
Names can be visible on a page but absent from the extracted name index. Search an available
text version with a surname, nickname, school or activity, then inspect the page. [S6]

Record that these are two retrieval routes into the same underlying material, not two independent
witnesses. Do not presume that every collection offers both. If the catalog or description gives
only an index, follow its source information rather than inventing a hidden full-text interface.

### 11. Diagnose OCR with the page, then change the query

Compare a returned page with its OCR text when available. Look for damaged print, misread letters,
columns read out of order and names split across lines. A printed Rosen- at one line's end and
berg at the next can defeat a search that expects the joined spelling. [S1, S3]

Try another documented name form, drop an exact-name restriction, or replace the name with a
distinctive contextual keyword. Adapt to a misreading actually observed on the page rather than
generating endless arbitrary typos. If text recovery fails, browse the likely issue or section.
Do not assume wildcard, Boolean or quoted-phrase syntax works without current documentation.

In the OldNews page viewer, open the full-page OCR to compare a difficult hit with the scan.
If the print is faint, adjust the viewer’s contrast or brightness before marking the passage
unreadable. Transcribe from the page image [H6 @2026-11-23] [S125 @2026-11-23].

### 12. Search newspaper images and extracted records as complementary routes

MyHeritage's **Names & Stories** collections offer structured records extracted from newspapers;
OldNews offers newspaper material to search and read. For covered material, try structured event
and relative fields. Follow the record's OldNews link or **View full newspaper page** control to
read the printed article; record any access restriction. If one route fails, try the other with
name variants or contextual words. [S7, H6, H7]

Extracted event dates or expanded relatives' names can be inferred from the article's wording.
Compare each field with the printed statement and label an inference instead of treating it as a
verbatim fact. Check each service's actual title/date coverage; their holdings need not coincide.

For example, a printed age can produce an indexed birth year that never appears in the article.
Search the literal name and reported age or relative in full text, rather than requiring that
derived year. An expanded parent's surname also need not occur as a complete printed name.

These records were extracted by AI, and each carries an article summary that AI generated
[H7 @2026-11-12]. MyHeritage's collection page, in its Internet Archive capture of 2026-07-17,
warns of mistakes such as incorrect relationships and advises reading the scanned page
[H12 @2026-11-12]. Use the summary only to find the article, and quote and cite only the printed
article.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Names, relationships and event dates that identify anyone who may be living go to MyHeritage in the newspaper query. Those details go to OldNews when the standalone search runs. Keep those query terms local until the gate is answered.

In a standalone OldNews search, use **More options** under **Publication year**. Select
**Match year exactly** for a known year or **Year range** for explicit bounds. For a known issue,
choose **Exact date** and enter its publication day, month and year. Broaden the bounds when the
publication date is uncertain [S124 @2026-11-23]. The results also offer **Publication date**
and **Publication name** filters. Use the latter to select the verified newspaper title and
check the publication locality if titles are similar [H6 @2026-11-23] [S123 @2026-11-23] [S125 @2026-11-23].

Set **Publication place** to the newspaper’s locality or country. Use **Place must match**
when the search requires that publication place. Clear it and widen the place for possible
coverage from other cities or countries. Put the event place in the terms if it helps identify
the story [H6 @2026-11-23] [S125 @2026-11-23] [S126 @2026-11-23].

In the Collection Catalog, look up **OldNews** and the publication’s state or country. Open a
grouped **Names & Stories** collection when that state appears among several in its title.
For example, Ohio shares a collection with Indiana and Michigan. Check the newspaper’s city
and years before treating a search in the group as coverage of that title [S86 @2026-11-22] [S87 @2026-11-22] [S88 @2026-11-22].

Alongside OldNews, try **Newspaper Name Index, USA, Canada, and Australia** for a U.S. or
Canadian paper. This structured index has a **Spouse** field and applies synonym matching
differently to given names and surnames. Use a known spouse as a separate pass, and try
documented surname forms explicitly. Keep the publication title, place and date from a hit to
retrieve the page [S86 @2026-11-22] [S89 @2026-11-22] [S90 @2026-11-22].

After a name-index miss, use **Browse by location** on OldNews. Drill down to the newspaper’s
publication locality and check the listed titles and date spans [S86 @2026-11-22] [S91 @2026-11-22] [S92 @2026-11-22]. If the town’s
paper is missing or the story might have been reported elsewhere, check nearby publications and
titles from towns where relatives lived at the time [S86 @2026-11-22]. Seek any uncovered title or year in
another holding.

For a Nordic title, compare the title and year listed on OldNews with the coverage of
MyHeritage’s **Nordic Newspapers from OldNews.com** before repeating a query. Record any issue
found through both routes once [S126 @2026-11-23] [S127 @2026-11-23]. For a Fraktur title in the
covered material, retry an earlier OCR miss on OldNews. Browse the likely issue if the text query still
misses [S126 @2026-11-23] [S128 @2026-11-23].

For a death notice, try the separate **Obituary Index from OldNews.com** for Australia, Canada
or the United States. Choose the index by the newspaper’s publication country. Keep the death
or burial details separate from the obituary’s publication place and date [S86 @2026-11-22] [S119 @2026-11-22] [S120 @2026-11-22] [S121 @2026-11-22].

For newspaper wedding leads, check the country’s **Marriages from Newspapers on OldNews.com**
collection for the United States, Australia, Canada or New Zealand [S86 @2026-11-22] [S87 @2026-11-22] [S93 @2026-11-22] [S94 @2026-11-22].
Read the actual notice and classify it as a marriage report, engagement, license, divorce
or advance announcement. Record a planned wedding date separately from publication and look
for evidence of the ceremony. If a couple-name query misses, try the known officiant or
attendant as a separate text or **Keywords** query where available [S93 @2026-11-22] [S94 @2026-11-22].

For a known Australian title, check **Australia Newspapers** alongside the OldNews indexes.
The scans for that OCR collection come from the National Library of Australia’s Trove. Use the
paper, issue date and page from the hit to identify the same issue in Trove [S105 @2026-11-22] [S107 @2026-11-22].

Match the publication locality to the stated scope of the OCR collection. **Poland Newspapers
from OldNews.com** uses modern Polish borders [S113 @2026-11-22] [S122 @2026-11-22]. **Baltic Newspapers from OldNews.com**
lists coverage in Latvia and Estonia [S113 @2026-11-22]. For a historical locality outside those bounds,
look for the paper under the country that now contains the town or in another holding.

For a **Names & Stories** wedding search, try the documented marriage date in the event field.
The index can resolve relative wording using the issue date. For a wife named by given name only,
try her given name with her husband's surname as a separate query. Transcribe the words from the
scan and label any date or surname that the index supplied [H7 @2026-11-20].

Look below the **Names & Stories** snippet for other indexed people when a list is shown. Verify
each person's role on the printed page before treating them as a relative [H7 @2026-11-20].

For France, check both **France, Names & Stories in Newspapers** and **France, Names & Stories in
Newspapers from OldNews.com**. Use the OCR and Gallica scan link for the first collection and the
OldNews scan for the second. Log the newspaper, issue date and page to spot the same article in
both routes [S40 @2026-11-20] [S42 @2026-11-20] [S43 @2026-11-20] [S44 @2026-11-20].

For the Netherlands, compare **Netherlands, Names & Stories in Newspapers** with the
issue-level **Netherlands Newspapers from OldNews.com**. In the structured result, read the
full OCR text when shown and note the paper, publication place and issue date. If the name
index misses, search the issue collection for the notice or a relative, or browse an
identified issue [S73 @2026-11-21] [S74 @2026-11-21] [S75 @2026-11-21].

Before treating a **Names & Stories** hit as verified, use its newspaper title, publication
place and date to locate the printed page. Check the user's access to full pages on OldNews
through MyHeritage Omni or OldNews Pro. If the page is blocked, use the issue locator to seek
the same scan in another holding and keep the extract provisional
[S73 @2026-11-21] [S76 @2026-11-21] [S80 @2026-11-21].

### 13. Read beyond the highlighted hit

Read the whole article, continuation, page heading and surrounding entries. In censuses, inspect
the preceding and following pages for household continuation and nearby relatives. In yearbooks,
inspect other pages and adjacent years for the same pupil's activities and name forms. [S1, S6]

For a death or unusual incident, search later issues and other local papers: the first report may
precede a fuller obituary or correction. Preserve newspaper title, publication date, page and a
full-page copy when available, alongside any clipping. Copied reports are not independent witnesses.

In the OldNews viewer, use the arrows or page selector to check other pages of the same issue
for a continuation or related material. Record the page number for each part
[H6 @2026-11-23] [S129 @2026-11-23].

**Privacy gate:** <!-- privacy-gate: export --> The full newspaper page can include names, photos and details about anyone who may be living. Export it from OldNews to the user’s own device or local printer after clearing the gate.

When keeping an OldNews copy, check the controls available in the user’s account. Use **Download**
for the full-page JPEG and the **Print** control for a paper copy. Keep the issue and page citation
with the copy. Mark the passage separately if needed. The downloaded image omits the search
highlights [H6 @2026-11-23] [S130 @2026-11-23] [S131 @2026-11-23].

For an obituary index hit, inspect the card image before moving on to the newspaper. In
MyHeritage's **San Joaquin County Public Library Obituary Index, 1850–1991**, the card can carry
the newspaper clipping itself [S25 @2026-11-18] [S26 @2026-11-18] [S27 @2026-11-18]. Read the
clipping separately from the card's annotations.

In MyHeritage's **New York City Marriages, 1866–1949**, page through the entire result. For
1908–1937, both a Health Department certificate and a City Clerk license can document the same
marriage. MyHeritage groups them in one result when it has both [S20 @2026-11-18] [S22 @2026-11-18].
Within the City Clerk papers, check the officiant's completed certificate for witnesses
[S20 @2026-11-18]. Record their names and any historical addresses or signatures on that page
as leads for identifying them.

In MyHeritage's **New York City Deaths, 1866–1948**, check the scanned certificate for the person
who reported the death, even when the index has no reporter [S20 @2026-11-18]. Keep that role
distinct from the attending physician or the person who requested funeral services.

In **Spain, Catalonia, Barcelona Births and Baptisms, 1850–1923**, check both sets of grandparents
and the parents' birthplaces and residence. Use the grandparents to distinguish similarly named
parents and the birthplaces to choose which parish records to check next
[S40 @2026-11-20] [S41 @2026-11-20].

For a known deceased person in the Netherlands, check **Online Familieberichten (Dutch Death Notices)** in the
user's MyHeritage account and use the original Online Familieberichten project if the entry is unavailable.
Identify the item as a death announcement, funeral notice or memorial card before using its dates
[S52 @2026-11-21] [S81 @2026-11-21].

In **England, Funeral Notices and Obituaries** and **Wales, Funeral Notices and Obituaries**,
use any last and former residences to distinguish candidates. To locate the original obituary,
use the newspaper title and its publication place and date. Keep those separate from the
deceased's residence and death date [S58 @2026-11-21].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Names and historical places identifying people who may be living go to MyHeritage when you run the census query. Keep those terms local until the gate is answered.

Use **United States Consolidated Federal Censuses, 1790–1950** to find candidate appearances
across census years. An entry can represent one census or several [S114 @2026-11-22] [S115 @2026-11-22]. Open **See
variations from sources** to compare each recorded name and birth detail. Follow the linked
returns and check the named household and locality for each year [S114 @2026-11-22]. Follow a relative’s
linked consolidated entry when offered and verify that person against the returns too [S114 @2026-11-22].
Treat each cross-year link as a candidate identification until the returns support it.

For an omitted census year, search the corresponding single-year collection in MyHeritage or
browse the schedules for the likely locality through the National Archives’ links by year.
Leave the reason for the gap open [S114 @2026-11-23] [S144 @2026-11-23]. Check each year’s
reported age before using an estimated birth year. For residence and occupation, record the
value and return locator separately for each census year [S114 @2026-11-23].

For the **1950 United States Federal Census**, include Canton (Kanton), Johnston, Midway
or Wake when the research points to one of those islands. Open the corresponding schedule
to verify the entry [S68 @2026-11-21] [S69 @2026-11-21] [S85 @2026-11-21].

After a MyHeritage 1950 U.S. census name miss, use a map of the known 1950 residence to identify
the enumeration district. Browse the population schedules at the National Archives by district
number. Check any sheets numbered from 71 onward for people enumerated out of order [S70].
Do not attribute a miss to the initial state-by-state rollout [S67, S69].

### 14. Use supplied tree-event geography as a search worklist

When a tree-event map or locality list is available, retain its person/branch, event-type
and date scope before choosing a place. Open the underlying people/events and preserve
their references. Use that scoped list to choose the next locality and record series,
keeping uncertain locations and their source support visible. A shared pin establishes
neither residence nor kinship. The [MyHeritage demonstration](https://www.youtube.com/watch?v=0v0fbjil9W8)
illustrates this planning use; apply the controls actually available rather than assuming
a current map widget or export.

### 15. Turn an index-only hit or automated match into a retrievable lead

Classify the source behind each Record Match before using it. MyHeritage identifies Geni, FamilySearch and WikiTree results as matches to other family trees [S15]. Follow their cited records and evaluate those separately; the Record Match label does not turn another user’s tree assertion into an independent historical record [S16].

For **Filae Family Trees**, missing profiles may reflect the indexing rule. Filae limits sharing
with MyHeritage to non-confidential profiles treated as deceased, which restricts MyHeritage search
results and Record Matches [S45 @2026-11-20] [S46 @2026-11-20]. Leave the contents of the original
tree unresolved when a profile is absent.

If expected Record Matches are not displayed, inspect **Settings**, the confidence slider and the record-type filters described by MyHeritage. Broaden one filter at a time and record what changes [S14 @2026-11-16]. Do not treat a filtered view as a search of every match, or assign an unverified numeric meaning to a slider position [S16 @2026-11-16].

After an unproductive signed-in search, check the user's **Search Alert** settings and review any
alert they supply against the saved query. MyHeritage documents exclusions for very common names
and searches with too many results. Keep the manual follow-up on the worklist if no alert arrives
[S47 @2026-11-20] [S48 @2026-11-20].

If no image is supplied, save the collection citation, originating institution, reference number,
volume/page and original-source link that are actually provided. Use that locator to seek the image
or request the record from its custodian. State explicitly when the original remains unavailable.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Name and date terms that identify anyone who may be living go to MyHeritage in the biography or patent query. Keep them local until the gate is answered.

Use **Indiana Biographies** (collection 20489) as a publication index. If the result supplies a
card image, use it to verify the publication title, date and any page reference. Locate that
edition or issue before citing a biographical detail. For a difficult title, check the Indiana
State Library’s biography index source list [S139 @2026-11-23] [S140 @2026-11-23].

Search **Inventors of Historical Patents** (collection 10834) by the candidate’s name. Use the
index’s publication country and date to find the patent. Open the patent’s first page and
record the invention, patent number and application filing date separately from the publication
date [S141 @2026-11-23] [S142 @2026-11-23] [S143 @2026-11-23].

Treat record matches, related-record suggestions and tree matches as new searches to evaluate.
Compare names, roles, dates, places and relationships against the source; retain competing candidates.
End with the coverage ledger and next discriminating search, not “MyHeritage has no such record.”
Use the evidence/proof recipe for any proposed identity or negative-evidence conclusion. [S1, S5]

If you copy information from a Smart Match or Record Match, review fields individually before
saving. Log the destination person, match/source link, previous value and copied value for each
change, keeping conflicting evidence visible. A fuller imported value is not necessarily a better
supported one. [S12, H9, H10]

For **Smart Matches**, undoing confirmation leaves already extracted and saved tree information
in place. If a match later proves wrong, use the field log to revisit the affected person, facts
and citations; check their other support before correcting or removing the imported assertions.
Verify the resulting tree values separately from the match's status. Undoing confirmation alone
does not repair the tree. [S12, H8]

A MyHeritage search can run without the subscription that opens a result
[S53 @2026-11-21]. When a hit is paywalled, check what the result list shows in the user's
own account. Save any visible birth or marriage date, newspaper year or identifying image
detail as a lead. Use it to choose a register or newspaper issue to check elsewhere
[S52 @2026-11-21]. Keep the blocked record unverified.

If a historical-record search returns a profile from a MyHeritage family tree, look at the bottom
of its record page for the link to the originating tree. Inspect the profile and follow any
record citations as leads [S65 @2026-11-21] [S84 @2026-11-21].

In an existing tree, open **Photo Discoveries** and preview the offered photos with **View
Discovery** before using any of them. Note the source family site and any supplied title,
description or tags. Open **View original photo** to inspect the uncropped image. Verify
the matched profile against documented dates and relationships. Record a person’s recognition
as their attributed claim and leave identity unresolved if the only clue is resemblance
[S132 @2026-11-23] [S133 @2026-11-23].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Prefilled names, dates and places from a tree profile go to MyHeritage when the search runs. If anyone identified may be living, clear the gate before starting the profile search.

When an existing tree profile has no useful Record Match, use **Research this person** from the
profile page to open a historical-record search. Inspect the prefilled details, remove
unsupported tree values and compare the result with a sparse search. Keep the automated
match list open as a separate source of leads [S116 @2026-11-22] [S84 @2026-11-22].

## Prompt-craft

Supply sourced facts with uncertainty labels, catalog descriptions, available fields,
previous queries and candidate images. Then ask:

> Build a controlled MyHeritage recovery sequence. Separate documented facts from estimates.
> Identify which collection and field could hold each clue. Keep a sparse baseline; tighten one
> condition, then state which weak condition to relax if it fails. Include name/native-script,
> date-role, geography, relatives and text/image pivots only where useful. For each candidate,
> preserve original wording, identify inferred fields and record what remains unverified.
> Return the query ledger and next discriminating search. Do not conclude identity or absence.

Without verified access, an assistant prepares queries rather than claiming it searched.
Use offered controls or separate attempts instead of undocumented platform syntax.

## Pitfalls worth internalizing

- More facts can reduce recall when they are estimates, wrong event types or unindexed fields.
- Global results and relevance order do not establish complete archival coverage or correct identity.
- A catalog keyword searches collection metadata; a personal-name search searches different material.
- Translated display names and inferred newspaper fields can look more definite than the original.
- Publication place/date need not equal the person's residence or event place/date.
- A shared source republished elsewhere is another access route, not another independent witness.
- Image restrictions, stale filters and a missing text counterpart can manufacture apparent absence.
- OCR recovery ends at the readable original; no general OCR-accuracy percentage settles a particular hit.
