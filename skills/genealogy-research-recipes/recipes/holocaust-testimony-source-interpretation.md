---
id: "holocaust-testimony-source-interpretation"
title: "Interpret a Holocaust name record through its underlying source"
summary: "Interpret a Yad Vashem result through its testimony, wartime list or survivor source and statement dates."
kind: "records"
scope: {"platforms": [], "tasks": ["unspecified death circumstances, submitter roles or evacuation conflicts."]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "HOLOCAUST-TESTIMONY-SOURCE-INTERPRETATION-01", "text": "Recover the information behind a Yad Vashem name result without converting a memorial submission, archival list or evacuation entry into an unsupported death or family conclusion."}]
handoff: ["dna-match-outreach-staging", "evidence-proof-judgment"]
checked: "2026-10-18"
checked_basis: "opened 18 October 2026"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": ["contact"]}
router: {"tier": "full", "group": "Featured workflows", "order": 5}
---

# Recipe: Interpret a Holocaust name record through its underlying source

## Contents

- Goal
- Recover the source, not only the name result
- Recover the described parts of an original case
- Recover separated evacuation household cards
- Keep dated observations distinct from final fate
- Choose the next retrieval action from the actual gap
- Sources

## Goal

Recover the information behind a Yad Vashem name result without converting a memorial
submission, archival list or evacuation entry into an unsupported death or family conclusion.
Use [evidence/proof judgment](evidence-proof-judgment.md) for resolving identity and conflicts;
this recipe supplies the source-specific distinctions that must survive that process.

## Recover the source, not only the name result

1. Preserve the record ID, collection title, source type, archive/file/page locator and inspection
   date. Open the source image when available. Keep an uninspected index transcription labelled
   as such, even when the search result supplies many biographical fields.
2. Separate a Page of Testimony from a contemporaneous list, a postwar compilation and a survivor
   registration. Yad Vashem's historical guide describes these mixed origins and explicitly notes
   that some lists include survivors. The database's commemorative title is not an individual
   death finding. [H1]
3. On a Page of Testimony, capture the filing date, submitter, stated relationship, language and
   literal death statement. A submitter need not be a relative. Do not infer eyewitness knowledge
   from the form's name or a family relationship. The official instructions allow the entry
   “Holocaust” when the circumstances of death are unknown: that word supplies neither a specific
   death location nor an execution date. [H2; interpretation of the form]
   Pages were gathered in several collection drives, from the 1950s and again in a large drive in
   1999, and the names database shows records from independent sources side by side, each with
   its own fate statement. [H11] If you find several Pages for one victim, keep each with its own
   submitter, birth year and death place instead of merging them. A death place on a Page may be
   the submitter's inference from what happened to the town or the transport; unless the Page
   says how the submitter knew, record it as the submitter's statement, not as a known place of
   death.
4. Keep birth, prewar residence, wartime location, evacuation destination and alleged death place
   in distinct columns. Retain all alternative names actually displayed; compare them with the
   image rather than resolving a field conflict by overwriting it.

The last two steps are an extraction worksheet, not a claim about a permanent API schema or
the present behavior of any search filter.

In a mixed postwar bundle, classify each component instead of inheriting the container's
“survivors” label or the first document's producer. A component may record deaths, burials,
relatives' addresses or displaced people. Preserve the stated compiler separately from a
later forwarding or stamping body and date; a stamp alone does not date compilation. The
[mixed-list discussion](https://forum.j-roots.info/viewtopic.php?f=26&t=138)
motivates this check; the underlying components and their individual statements still need inspection.

## Recover the described parts of an original case

**Privacy gate:** <!-- privacy-gate: request --> A list or case of the 1940s can name people who
are still living; answer the privacy gate in `SKILL.md` before requesting a missing part.

If a result opens only part of a list or case, retain the original repository/signature and
the folios actually inspected. Look for other described digital parts of that same original
case. Keep the name-record ID, archive item, JM/film key, original list/page/entry and viewer
image number separate; similar or adjacent IDs establish neither page order nor identity.
For an unavailable part, prepare the exact title/language/signature and missing extent for
the actual holder's supported request route. The [forum's partial-list examples](https://forum.j-roots.info/viewtopic.php?f=26&t=1196)
motivate this handoff, without establishing current access or a universal holding repository.

Before seeking another part, identify what moved and why the record was created: evacuated
people or archival documents, an arrival/card record or a later damage claim. Compare the
original-language title, place, date and actual film signature boards. Where descriptions
identify overlapping district-letter volumes or mixed-region units, retain the precise part
inspected rather than treating one missing segment as loss of the whole case. The
[evacuation-source discussion](https://forum.j-roots.info/viewtopic.php?f=197&t=1199)
motivates these source-class checks without establishing present scan availability.

When an evacuation entry names a destination region, check whether another repository holds
selected copies from that region's state archive. The
[USHMM evacuation finding-aid examples](https://forum.j-roots.info/viewtopic.php?f=167&t=4906)
show copy collections from Kazakh regional archives whose finding aids describe evacuee lists and
aid files by original file (delo) and folio. Record the copy's accession/RG number and the
original archive, file and folio as separate locators. A selected-records copy may not reproduce
a whole file. A finding-aid description does not show that a given person appears, so inspect the
listed folios before drawing any conclusion.

Archives of evacuation destinations also run their own name-searchable evacuee databases, such as
the Uzarchive agency's evacuation.archive.uz (Uzbekistan) and the Mari El State Archive's
evacuation.gosarhivrme.ru (people evacuated to the Mari ASSR, 1941–1945). [H9], [H10] Search the
destination region's database, then the original list it cites. Uzbek records give a list number
and a position on that list, not a page. A miss is not a negative. A fund label such as
'Holocaust' on a result says nothing about the person's ethnicity or fate: Uzbek records carry it
even for evacuees recorded as Russian. On 2026-11-04 the birth dates on the Uzbek records opened
showed a placeholder date, so take birth data from the original list, not the database card. [H9]

## Recover separated evacuation household cards

Inspect the actual card's front and reverse before interpreting a derived “with children”
tag. Where supplied, retain the original list number, page, person serial and explicit
relationship; use those coordinates to seek separated head/member cards. Alphabetical card
order and adjacent database IDs do not supply family order. Use recorded addresses and
attested surname alternatives as additional retrieval keys, preserving competing heads,
ambiguous roles and missing serials. The same discussion motivates this household crosswalk;
original coordinates or proximity alone do not establish kinship or complete household survival.

**Privacy gate:** <!-- privacy-gate: request --> An evacuation card can describe a person who
is still living, such as an evacuated child; answer the privacy gate in `SKILL.md` before
requesting it.

When an evacuation search returns only a summary certificate (справка) and the question is origin
or ethnicity, request a copy of the card itself. An
[evacuation-card discussion](https://forum.j-roots.info/viewtopic.php?f=20&t=5084) reports that
cards recorded nationality and birthplace, while the certificate issued from them omits
birthplace. Record whether you inspected the card or only the certificate. A certificate's silence
is not evidence that no birthplace was recorded, and a card entry is a registration statement,
not a birth record. The thread does not show which card formats carry these fields, or the
current request conditions.

For a compilation covering several regions or source lists, keep the region and source-list
reference with each row/family counter. Identical counters across lists do not join households.
Preserve original entries, compiler corrections and oral accounts as separate attributed
statements. The [regional compilation example](https://forum.j-roots.info/viewtopic.php?f=197&t=12365)
motivates this qualification of the household crosswalk; underlying records still need inspection.

For a Jewish refugee family in the Soviet interior during the war, also search the JDC Archives
Names Database, which indexes individuals found in JDC's historical records. [H18 @2026-11-08] In
the finding aid for JDC's New York office, 1933–1944, File 428 holds JDC's beneficiary lists Nos.
1–73 from the parcel service it ran from Tehran for Polish-Jewish refugees in the USSR; the File
427 entry says these lists gave the names and addresses of refugees, mostly in Asiatic Russia, and
were forwarded from New York to Tehran between January 1943 and November 1945. [H19 @2026-11-08] A
family story on the JDC Archives site reports finding a grandmother on the 1943–1945
parcel-beneficiary list in the Names Database, with the family's wartime address in Samarkand.
[H20 @2026-11-08] Search the Names Database by surname together with the wartime town, and treat a
hit as the person's address on that list's date, not as proof of survival.

## Keep dated observations distinct from final fate

Build one row per statement, including contradictory submissions:

| Record/source | Statement as written | Person-identifying details | Date and its role | Basis/limit |
| --- | --- | --- | --- | --- |
| Testimony image | Reported death or unknown circumstances | Names, relatives, places | Claimed event date; separate filing date | Submitter's stated knowledge |
| Evacuation or wartime list | Registration, movement or presence as actually recorded | Household and individual fields | List/event date, as identified | Administrative entry; inspect its purpose |
| Postwar record | Later presence or other recorded event | Descriptors for matching | Event date; separate recording date | Identity still requires correlation |

An evacuation entry can challenge a supposed earlier death only after the people and relevant
dates are matched. Registration alone does not establish survival to the end of the war.
Conversely, a later memorial submission does not overrule a wartime observation merely because
it was filed later. Keep an unresolved conflict visible instead of choosing the tidiest timeline.
These are reasoning consequences of the source types, not a reliability ranking for every record.

## Choose the next retrieval action from the actual gap

- If an index differs from the image, preserve both readings and identify the layer containing
  the discrepancy. A corrected transcription does not automatically correct the original assertion.
- If the source is a list, identify its title, date, jurisdiction and inspected image range.
  Record whether names were searched in an index, read in images, or remain uninspected.
- If a submitter is useful, treat the name and stated relationship as a lead. Researchers can
  submit Pages of Testimony; a contact field does not establish a living relative. [H1, H2]
- If the alleged death place or last residence points to another record set, search the
  matching database below. Each has its own coverage, so a miss covers only that database.

  | Alleged death place or last residence | Search next | What it can add |
  | --- | --- | --- |
  | A camp, ghetto, deportation, forced-labour or displaced-persons trail, anywhere | [Arolsen Archives online collections](https://collections.arolsen-archives.org/en/search) | Scans of camp, deportation, forced-labour and postwar records [H12] |
  | Germany, within its borders of 31 December 1937 | [Bundesarchiv Gedenkbuch](https://apps.bundesarchiv.de/gedenkbuch/) | A name list of Jews who lived there and were murdered or died as a result of persecution; no images [H13] |
  | Theresienstadt, or deportation from today's Czech Republic | [Terezín Initiative database of victims](https://www.holocaust.cz/en/database-of-victims/) | About 80,000 deported people, with document images for some entries [H14] |
  | Łódź ghetto | [JewishGen Łódź Ghetto Database](https://www.jewishgen.org/databases/Poland/LodzGhetto.html) | Entries from the 1994 *Lodz-Names* list of ghetto inhabitants, drawn from the ghetto's population registry books [H15] |
  | France | [Mémorial de la Shoah person search](https://ressources.memorialdelashoah.org/rechav_pers.php) | Jews deported from France and other people in its records; searchable by convoy number [H16] |
  | Any | [USHMM Holocaust Survivors and Victims Database](https://www.ushmm.org/remember/resources-holocaust-survivors-victims/database-of-holocaust-survivor-and-victim-names/search-names); [JewishGen Holocaust Database](https://www.jewishgen.org/databases/holocaust/) | Records from the museum's collections that name individuals, survivors included; camp records, transport lists and other name lists [H17] |

  An Arolsen T/D (tracing and documentation) file is opened when someone enquires about a
  person, and later enquiries go into the same file. [H12] An enquirer's statements in it carry
  the enquirer's knowledge, like a Page of Testimony. Classify copies of other documents in the
  file by their own author and purpose, as for a mixed postwar bundle above.
- If no name result is found, report the names/scripts, fields, filters, collection and date
  actually checked. The historical guide describes incomplete victim and survivor documentation;
  do not replace that limitation with a fixed present-day coverage percentage. [H1]

- If the person was killed or held under German occupation of Soviet territory, also search the
  Extraordinary State Commission (ЧГК) acts: see [Recover separate military and Soviet-repression record episodes](russian-military-repression-record-episodes.md#start-from-the-event-and-source-scope).

**Completion packet:** inspected source locators, statement rows, candidate identity status,
the exact unresolved conflict and one source capable of resolving it. Current interface modes,
contact routes and access availability must be checked when used. This recipe does not authorize
contacting a submitter or submitting a correction.

**Privacy gate:** <!-- privacy-gate: contact --> A submitter or a relative named on a Page may be
living. If the user asks to contact one, answer the privacy gate in `SKILL.md` first. Follow its
Living people rule: use the consent, disclosure and log rules of
[DNA match outreach staging](dna-match-outreach-staging.md) without its DNA-only items.

## Sources

[Primary-source checks and limits](https://github.com/Kinprove/genealogy-research-recipes/blob/09760df06be02b62a23de79a4fb5bf4a5680680a/skills/genealogy-research-recipes/sources/holocaust-testimony-source-interpretation.md).
