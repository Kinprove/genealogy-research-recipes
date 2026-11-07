# Recipe: Recover separate military and Soviet-repression record episodes

## Contents

- Goal
- Start from the event and source scope
- Preserve date roles and successive episodes
- Recover the next document before combining the biography
- Sources

## Goal

Move from WWI/WWII or Soviet-repression name hits to source-linked episodes without merging
different people, different arrests or different record types into one apparent final fate.
Use [evidence/proof judgment](evidence-proof-judgment.md) for the identity ruling; this recipe
organizes the records and retrieval gaps that the ruling needs.

## Start from the event and source scope

For each result, record the portal, original contributing collection, record ID, document type,
archive/file/page locator and whether its image was actually read. Two portals reproducing one
document are two access routes, not two independent observations.

OBD Memorial describes a bank centered on deaths, missing persons and other irreversible losses,
including primary burial locations. That remit does not make every hit a death certificate or
make the bank a complete service roster. Its own account identifies material still needing
recovery/digitization. Keep coverage conclusions at the level actually documented. [H1]

OBD Memorial's search is not deaths-only. Its advanced search has loss groups (Сведения о
потерях, including POW documents and striking-off orders), Book of Memory groups (Книги Памяти)
and personnel groups (Сведения о личном составе). The personnel groups hold conscription and
demobilisation lists, transit-point and reserve-regiment lists, unit name lists, the officer
service-card file and the sailors' card file, so they include men who came home. Choose the
groups for the question and record which were enabled. A miss shows neither non-service, nor
death, nor survival. [H23]

For a WWI lead, check the portal's present collection/search scopes, including any separate
document catalogue, before describing what a name search covered. An empty hero-name search cannot establish that an
individual never served; neither does it prove that a particular unindexed file exists. For
Austro-Hungarian army service for men from Galicia and Bukovina, see
[Route a Galician or Bukovinian record by date, confession and custodian](galicia-bukovina-habsburg-record-routing.md).

On GWAR (gwar.mil.ru, «Памяти героев Великой войны 1914–1918», In memory of the heroes of the
Great War 1914–1918), read a card's place as the residence or call-up place. As read in a 2025
archived capture of the form and in the site's own text seen in search-engine extracts on
2 November 2026 (the live site failed TLS), the person search puts its place fields (Губерния,
Уезд, Волость, Населённый пункт: province, district, rural district, settlement) under 'Место
жительства / место призыва на военную службу' (residence / place of call-up), and the form has no
separate birthplace group. Take a birthplace only from the underlying document, and use the
card's area only as a search area for the baptismal parish. [H16], [H17]

GWAR's sources are selected separately, among them name lists of losses, the award card file,
the prisoner-of-war card file, burial passports and service records (послужные списки). Record
which sources a search included. A miss in loss material says nothing about the POW card file,
burial passports or service records, and a tool or API that queries only some card types does
not cover the rest. A card count is not a people count: the site's own figures give about 6.8
million POW-file cards for about 3.5 million lower-rank records, so a result set is not a roster
of soldiers, residents or families. Do not name the archive behind the POW card file until a card
or the site states it. [H17], [H18]

OBD Memorial returns only records that meet the condition in every filled field, so changing one
name part at a time misses a card with two variant parts. Test chosen combinations instead, for
example Георгиевич, Егорович and Юрьевич as father's-name lanes; they are search lanes, not proof
that the forms name one man. Use the trailing `*` wildcard on uncertain endings (the help documents
it for single-line and full-text queries); е and ё are treated alike. Only one field must be
filled, so when the surname may be unrecognisable, search given name and patronymic with a year
or place and no surname, then filter locally. Flag hits on commonly confused names for an
identity check. Use the same tactics on GWAR or memory books only after reading their own search
help. [H24]

For a repression lead, record each list's or database's stated inclusion rule and geography
before reading a miss. Posters in a [repression-databases discussion](https://forum.j-roots.info/viewtopic.php?f=64&t=558)
note that a Magadan list covers only people given a second sentence in the camps and shot there,
and that the Memorial database mainly covers Russia, without a Ukrainian regional series of
rehabilitation volumes. In the [repression-records discussion](https://forum.j-roots.info/viewtopic.php?f=64&t=561),
for a person absent from Russian databases, a possible match under a different given name appears
in the "Stalin lists" and in a Ukrainian database under that republic's code; posters call its
regional loading uneven. A [Ukrainian repression-lists discussion](https://forum.j-roots.info/viewtopic.php?f=64&t=7018)
reports that one project's online database and printed volumes differ, and that the volumes
predate many file transfers, so they do not identify the present custodian. Search the trial
republic's database and volumes, recording each result separately. A miss is absence from that set
only; these posts describe past coverage without measuring it.

The Perm Memorial martyrology states its own inclusion rule. It lists only people repressed on
political grounds by judicial and extrajudicial bodies in Perm krai and since rehabilitated,
compiled from investigation files in ПермГАНИ (Perm State Archive of Recent History). It does not
cover prisoners of ITL (corrective labour camps) and filtration camps, exiles or special settlers;
the site calls collecting them a separate, larger task. So a special settler's absence there says
nothing. [H37]

раскулаченные.рф is a joint project of Sverdlovsk oblast archives, the oblast state archive (ГАСО)
among them, on people dekulakised in the Ural oblast in the 1920s–30s. Its cards give residence,
the basis document and the archive cipher down to the leaf, and, where known, the family members
with kinship and ages. A card can name other household members by their relationship to its head,
so record whose card it is and the target's role on it before attaching a hit. Memsearch aggregates Memorial and other
memory-project databases, regional ones included; record which source database each hit came
from. [H38], [H39], [H40]

**Privacy gate:** <!-- privacy-gate: request --> A query through IPN's form sends details of a
repressed person and the asking family, who may be living; answer the privacy gate in `SKILL.md`
before sending it.

For a person from Poland's pre-war eastern territories (Kresy) deported or imprisoned under
Soviet rule, search IPN's Indeks Represjonowanych (indeksrepresjonowanych.pl). It covers people
who came under Soviet occupation after 17 September 1939 and were repressed in prisons, camps and
exile. About 316,000 records are public out of about 1.2 million in IPN's internal database
(counts as of 2 November 2026). IPN staff search the internal database when answering queries
sent through the site's 'Prześlij zapytanie' (send a query) form, so a miss in the public index
calls for a query, not a negative. The index is built from questionnaires from victims and their
families, Polish archives and institutions, and post-Soviet archival data obtained through
Memorial (Moscow); Ośrodek KARTA published 21 volumes from it in 1995–2013. Check each card's
provenance before treating it as an archival record. [H41]

For Western-Ukrainian deportation and repression in 1944–1953, search published documentary
series as well as databases. 'Літопис УПА. Нова серія' (Chronicle of the UPA, New Series, from
1995) publishes documents from ЦДАГОУ and ЦДАВОУ (the central state archives of public
organisations and of the supreme bodies of power), the SBU archive and West-Ukrainian oblast
archives. [H32], [H33] A second series is the three-volume 'Депортації. Західні землі України
кінця 30-х – початку 50-х рр.' (Deportations: the western lands of Ukraine, late 1930s to early
1950s; ed. Yu. Slyvka, Lviv, 1996–2002; vol. 3 is memoirs). [H34] Read each volume's contents
before claiming it holds a family list. Cite series, volume and page, and copy only the target
family's entry, since the lists name other private families. Record a compiling body's label such
as 'пособник' (accomplice) as the regime's label, not as fact.

For the 1944 Chechen and Ingush deportation and special-settlement files, see
[Trace a Chechen or Ingush family through the 1944 deportation and special settlement](chechen-ingush-1944-deportation-records.md).

## Preserve date roles and successive episodes

Use the following extraction structure; the table is a research worksheet, not a promise that
every collection supplies every field:

| Document or entry | Extract separately | Do not substitute |
| --- | --- | --- |
| Award material | Action/service dates, recommendation, higher commanders' conclusions, award ordered, order or decree title and date, recipient descriptors, any posthumous wording | Order date for a dated observation of life; the recommended award for the award ordered |
| Loss or missing report | Event/status as written, last contact/event date, report date, unit, informant | “Missing” for a demonstrated death date |
| Military-registration (военкомат) entry | Office, kind of registration, call-up date and 'дата выбытия' (date of leaving the register) exactly as written | 'Выбытие' for a death date or an upper bound on life; a commissariat away from the family's residence for a proven move |
| Hospital or prisoner record | Admission/capture/registration event, place/unit/camp, identifier and recorded outcome | Arrival for discharge, recovery or death |
| Burial entry | Original burial, later reburial if stated, dates and supporting document | Original site for verified present grave location |
| Repression entry | Arrest, allegation/code, deciding body, decision, punishment, later rehabilitation | Allegation for factual guilt; sentence for demonstrated execution |

The date cautions are inferences about what a document actually asserts. In particular, an
award order after a missing report does not, by itself, establish survival between those dates.
Obtain an event-specific source before extending a life or death interval.

**Privacy gate:** <!-- privacy-gate: request --> A hospital or wound request asks for
military-medical records about a serviceman who may still be living; answer the privacy gate in
`SKILL.md` first.

For a WWII hospital or wound question, send the archive request to the TsAMO branch for
military-medical documents (филиал ЦАМО РФ военно-медицинских документов, Lazaretny per. 2,
St Petersburg). The Military Medical Museum has not answered archive requests since 2012 and
redirects them to that branch. [H48]

For a WWI prisoner taken on the Russian front, the ICRC Geneva archive is the wrong default. By the
ICRC's own FAQ, lists from the Russian front were not sent to Geneva but collected by the Danish
Red Cross in Copenhagen; the Geneva documents come mainly from the Western, Romanian and Serbian
fronts. So a miss in the ICRC 1914–1918 database is not a negative for these men. [H19] Where
that database does apply, it searches by name only, not by regiment, capture date or camp, and
its cards sit in separate catalogues by nationality and military or civilian status (29 in all),
each searched separately. [H19], [H20] The Copenhagen material is now at Rigsarkivet (Dansk Røde
Kors, Krigsfangeafdelingen). Only samples survive: two selected boxes of the card index of Russian
prisoners in Germany (c. 1915–1918) and one random sample bundle of lists (1917–1918), with no
online images found. A miss there is not a negative either. [H21], [H22]

A missing award sheet is not by itself a gap. The portal project's own description, quoted in an
[award-archive discussion](https://forum.j-roots.info/viewtopic.php?f=36&t=4542), says that from
the 10 November 1942 decree, commanders of armies, corps, divisions, brigades and regiments could
also issue award orders. No award sheet was foreseen for these unit orders; the deed is described
in the recipient's row of the award list. Read that row and record the order's issuing level. The
same description says some awards have only a short name entry with no deed text, so a row without
a description does not prove that a sheet was lost. This is the project's account, not a check of
any particular order.

Read every side of a WWII award sheet (наградной лист) image and find the conclusions of the
higher commanders and the military council member wherever the form puts them. Those conclusions
could approve, lower or at times raise the recommended award, so a change from the recommendation
is recorded there, not in the proposal. [H25], [H26] On Pamyat Naroda, open every document in the man's
record group, not only the first hit.

From 4 June 1944 to 14 September 1957, the Order of the Red Star, the Order of the Red Banner and
the Order of Lenin were also awarded for long service: the Red Star at 15 years, the Red Banner at
20 and again at 30, Lenin at 25. The Medal 'For Battle Merit' was awarded at 10 years. The Navy
followed from 25 September 1944. Awards were timed to 1 May and 7 November, and in practice Army
and Navy awards stopped in 1956. [H27], [H28], [H29] A decree or order titled 'за выслугу лет'
(for long service) marks these awards. [H28] Before writing a combat narrative for such an award
to a career serviceman, find the title and date of the awarding decree or order.

Treat a loss report's residence/relatives column as an entry whose informant and date are unknown.
In an [OBD/Pamyat Naroda discussion](https://forum.j-roots.info/viewtopic.php?f=36&t=4542), one
report names a father who had died years before call-up. Another poster says the relatives column
often gives the family's evacuation address. Do not infer from this column that the relative was
alive or where the family lived before the war; seek civil or prewar residence records. The
posters could not say how the column was filled in.

A casualty compilation can list the wounded beside the dead, and a database built from it
can enter the out-of-action date in a field labelled as death. Record the compilation's own
event class and date separately from the database label before treating the date as a death.
The [Russo-Japanese War casualty-book discussion](https://forum.j-roots.info/viewtopic.php?f=181&t=2248)
motivates this check; it does not establish any particular person's fate.

Keep repeated arrests as separate episodes even if the identity is established. OpenList's own
description explains that people can occur in several regional Books of Memory, can have been
persecuted more than once, and can acquire OCR or field-placement errors during compilation.
Thus different dates can describe successive events, duplicates or a collision of identities;
the date difference alone does not select among them. [H2]

A death certificate issued to relatives of an executed or repressed person is a separate
administrative document. It is not the record of the event. Record its issue date, issuer and its
stated date, place and cause apart from the sentence and any execution record. A later corrected
certificate is a further episode. A [repression-records discussion](https://forum.j-roots.info/viewtopic.php?f=64&t=561)
relays a poster's account that relatives of people sentenced to death in 1937–38 were told of
ten-year camp terms without correspondence and later given fictitious natural-cause certificates.
A [publication notice](https://forum.ahnenforschung.net/forum/thread/7649/)
reports deliberately false certificates for people executed in Moscow in 1950–53. Rehabilitation
wording saying that relatives were not found or whereabouts are unknown records an inquiry, and an
early case termination does not establish death: the repression-records discussion reports a release after one.
Not every certificate is false, and neither thread offers a test. Seek decision, execution,
custody or later-residence records before closing the life interval.

Record each review of a case as its own dated episode, with the deciding body and exact wording.
A Khrushchev-era review may annul a sentence for lack of evidence or of a crime without using the
word 'rehabilitated'. A 1990s decision may then rehabilitate formally; in other files the
Khrushchev-era review stood alone, with no later formal rehabilitation. Do not date exoneration by
the only document that uses the word, and do not call a review a rehabilitation unless its wording
sets the sentence aside. The [repression-records discussion](https://forum.j-roots.info/viewtopic.php?f=64&t=561)
reports both patterns from files posters read. It gives no rule for deciding which pattern applies
to a particular case.

## Recover the next document before combining the biography

Early in a WWII search, check family-contributed memorial pages: Бессмертный полк (Immortal
Regiment, moypolk.ru) story pages, where families upload photos, and the Moscow electronic memory
book «Бессмертный полк. Москва» (polk.mos.ru), which holds relatives' scanned photos and wartime
letters on pages that registered relatives can edit. [H30], [H31] Such scans can be missing from
state databases. Search moypolk.ru with its own search, not a web search engine
([research documentation](research-documentation.md#research-log)). Grade the page text and each posted scan
separately with [evidence/proof judgment](evidence-proof-judgment.md), then seek the original.
Use only the documents and text on these pages: never compare faces or identify anyone in their photos. The
pages can name living relatives; keep their details out of shared output.

1. Copy the compilation's original source citation and archival locator. For a name collision,
   compare locality, occupation, relatives, unit/camp, case number and event dates. Keep missing
   descriptors unknown. A birth-year tolerance may widen retrieval; it is not an identity rule.
2. **Privacy gate:** <!-- privacy-gate: request --> The custody and exile requests below ask for
   files on a repressed person and family members who may be living; answer the privacy gate in
   `SKILL.md` before sending them.
   For a repression lead, separate the investigation/decision record from custody, transfer,
   settlement and rehabilitation records. Preserve the exact legal code, jurisdiction and date;
   do not guess a missing subarticle or transfer another republic's numbering automatically.
   A sentence handed down between 26 May 1947 and the entry into force of the decree of
   12 January 1950 (effective on publication) cannot have been a death sentence. The Presidium
   decree of 26 May 1947 abolished capital punishment in peacetime, replacing it with 25 years in
   corrective labour camps, and commuted death sentences not yet carried out; the 1950 decree, as
   an exception to it, allowed the death penalty again for traitors, spies and
   saboteur-diversionists. [H35], [H36] So do not infer execution in that window, and check the
   exact decision date, not the offence date. When a mass eviction is framed as a reprisal for a
   village event, tie the family to the operation, not to the event, unless the document links
   them.
   Treat each file class as its own retrieval target. Posters in a [repression-records discussion](https://forum.j-roots.info/viewtopic.php?f=64&t=561)
   report that the investigation file stays where the case was heard. It holds interrogations,
   the decision and rehabilitation papers, not confinement details. A prisoner's personal file
   stayed where the sentence was served, and a transfer could start a second file. For custody,
   ask the interior-ministry information centre of the region of last confinement for a
   registration card, which may carry a file number or a destruction note. For exile, ask the
   place of exile. A [regulation extract](https://forum.j-roots.info/viewtopic.php?f=64&t=564)
   adds exile/special-settlement files and filtration-check files after capture. It also says
   only the requested person's portion of a group case is supplied. The survival and retention
   claims are unverified, and a destruction note is not a negative search of other series. A
   standard certificate gives only core fields, so request family composition explicitly.
   Record whether you received a certificate, selected copied pages or the file read in person
   ([archive-access guide](https://forum.j-roots.info/viewtopic.php?f=64&t=5700)); cite a
   certificate as the certificate, not the inspected file, and treat an omitted fact such as
   relatives as unchecked rather than absent.
3. Identify the present custodian from a current official finding aid or archive response for
   the particular file/series. A broad Imperial/Soviet/WWII year division is only a starting
   clue; branch, record creator and later transfers can matter. For example, in Ukraine the SBU
   sectoral state archive (ГДА СБУ) and the Sectoral State Archive of the Ukrainian Institute of
   National Memory (ГДА УІНП) are separate custodians. Law No. 316-VIII of 9 April 2015 mandated
   the transfer of the repressive organs' 1917–1991 records to ГДА УІНП within two years, but the
   transfer has not been shown complete: ГДА УІНП's 2025 report lists no SBU accession, and ГДА
   СБУ still cited its own fonds in 2026. Confirm the holder of the specific file and do not assume
   either. [H42], [H43], [H44] This recipe supplies no fixed
   archive boundary, access entitlement or response-time promise.
4. Record what was delivered: pages/images inspected, stated omissions and any unavailable,
   withheld or redacted material. An inaccessible image is not a negative name search. Do not
   recover deliberately withheld content through alternate image leakage.
5. **Privacy gate:** <!-- privacy-gate: request --> A follow-up archive inquiry asks again about
   a person who may be living; answer the privacy gate in `SKILL.md` before sending it.
   When an archive says “no information,” preserve the repository, series or search scope it
   actually checked. Ask about a documented transfer or another specific creator when relevant;
   do not translate a local reply into proof of universal loss or launch an endless archive sweep.

A target can also appear in someone else's case. A sentence 'as ЧСИР' (member of a
traitor-to-the-motherland's family) points to a relative's own entry and case number. That
relative was not always a husband, and a shared surname does not identify them. A person with no
file of his own may appear as a witness, or be mentioned, in the investigation files of
relatives, in-laws or colleagues. Record the interrogation date and his self-reported statements
from that file. Keep each person's arrest, deciding body, sentence and rehabilitation as separate
episodes. The [camp-relatives discussion](https://forum.j-roots.info/viewtopic.php?f=64&t=7064),
a [witness-interrogation example](https://rodgersforum.borda.ru/?1-29-0-00001498-000-0-0-1668855363=)
and a [relative's-case suggestion](https://rodgersforum.borda.ru/?1-29-0-00000128-000-0-0-1768448567=)
motivate this. Absence from repression lists does not show that a person was never repressed or
died naturally. None of these sources establishes a later fate, or a relative's identity without
documented descriptors.

Records made by the target's children can carry dated statements about a parent. A son's WWII
entry on Pamyat Naroda may name a parent as next of kin at a later, distant address; a
[descendant-search example](https://rodgersforum.borda.ru/?1-2-0-00001643-000-0-0-1734245901=)
found this for a family exiled in 1933. A child's personnel file with an employer or education
department may hold an autobiography giving a parent's occupation and death year; a
[repression-records discussion](https://forum.j-roots.info/viewtopic.php?f=64&t=561) shows one
that gave only a death year for a parent who had been arrested. Record each as the writer's
statement at its own date, a separate episode, and use it to search that place's lists or arrest
and decision records. Without matching descriptors it does not prove the parent's identity. It
does not show when or how the family left exile, and a stated death year does not establish the
date or cause of death; the wording may be guarded.

When a report wrapper explicitly describes attached family correspondence, continue to the
actual letter and envelope within the available unit. Keep their separate locators, writer,
soldier and addressee roles, date and literal return/delivery address. Use that dated address
for a specific locality-list search; a later list's different date, address and member roles
remain a separate episode. The [attached-letter example](https://forum.j-roots.info/viewtopic.php?f=197&t=1199)
motivates this handoff. Unnamed children in a letter do not establish a named parent's edge,
and a reported attachment remains uninspected until its actual pages are examined.

Read an obtained investigation file for its embedded documents, not only the accusation. The
arrestee questionnaire or interrogation record may name the spouse, children, siblings and
parents. Copied identity papers may cite issuing offices and children's birth-certificate
numbers. A later prosecution's file may hold a petition from an earlier case. Give each item its
own page locator, date and author, and keep earlier-case papers in their first episode. Treat
family answers as the arrestee's own statements: they are leads to civil-registry (ZAGS) or
village-soviet records, not proof of kinship. If two documents list different children, keep both
versions. The [questionnaire](https://forum.j-roots.info/viewtopic.php?f=64&t=561),
[interrogation-record](https://forum.j-roots.info/viewtopic.php?f=64&t=558),
[copied-passport](https://rodgersforum.borda.ru/?1-16-0-00001211-000-0-0-1779216842=) and
[repeat-prosecution](https://rodgersforum.borda.ru/?1-14-0-00000057-000-0-0-1768992933=) reports
each describe particular files. They do not show that every file holds such material, or that an
earlier case file is lost.

For a supported conscription-office/date lead, check confirmed surviving series for the
conscription-registration entry and its dispatch/command identifier, and separately the
register of incoming front notifications. Carry actual entry and notification locators into
the next retrieval step. Compare available departure, receiving/training and later-unit
records before treating a former unit's missing report as final fate. Dispatch or a hospital
destination does not demonstrate arrival or death. The [soldiers' records discussion](https://forum.j-roots.info/viewtopic.php?f=36&t=1813)
motivates these complementary series checks without establishing survival or current custody.

If a source names the target's commander or another documented officer associate, retain
the event date and exact name/role. Seek that officer's service record for the relevant date,
then use a supported unit reference to choose documents that might name the target. Do not
carry a unit known in a later year back to an earlier event. The same discussion motivates
this associate-to-unit lead; shared service, the target's presence and fate need their own records.

**Stop condition:** finish the bounded source/episode inventory, state the remaining identity or
fate question, and name the document that could distinguish the alternatives. A further inquiry
needs an identifiable input/custodian and a result that can change the decision. Sending a request
or seeking rehabilitation is a separate action requiring the user's scope and current rules.

## Sources

[Primary-source checks and withheld claims](../sources/russian-military-repression-record-episodes.md).
