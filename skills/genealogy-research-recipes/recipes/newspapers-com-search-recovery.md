---
id: "newspapers-com-search-recovery"
title: "Newspapers.com: Recover Notices That Name Searches Miss"
summary: "Find notices on Newspapers.com that name searches miss, after checking which titles and issues are actually covered."
kind: "platform"
scope: {"platforms": ["newspapers.com"], "tasks": ["a failed newspaper name search, an unknown maiden name, a missing obituary, immigration or family-reconstruction leads, title changes, incomplete issue coverage, alternate holdings or unreadable OCR."]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "NEWSPAPERS-COM-SEARCH-RECOVERY-01", "text": "A surname can occur in one item and a travel verb in another on the same page. Confirm the subject and event within the actual item before assigning that event to the searched person."}]
handoff: ["ai-for-documentary-records", "australia-nz-record-routing", "court-case-file-recovery", "criminal-court-prison-record-recovery", "evidence-proof-judgment", "research-documentation", "us-federal-court-case-file-recovery"]
checked: "2026-11-12"
checked_basis: "Rechecked 2026-11-12"
capabilities: {"browse": ["newspapers.com"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool"], "contact": []}
router: {"section": "Record websites, libraries and maps", "group": "Record websites", "order": 45}
---

# Newspapers.com: Recover Notices That Name Searches Miss

## Contents

- Goal
- Decisive rules
- Resolve a title to a holding and an issue
- Use a notice index's documented personal-place field
- Follow an obituary collection's actual arrangement
- Search recipes
- Bounded execution and stopping rules
- Prompt-craft

## Goal

Recover an ancestral newspaper notice when an exact-name search fails, and distinguish a
page containing search terms from a notice that actually reports the person's event.

Use this recipe for retrieval on Newspapers.com and for resolving an alternate holding when its
coverage is insufficient. For evaluating a recovered person's
identity, use [Evidence and Proof Judgment](evidence-proof-judgment.md). For difficult
image transcription or translation, use [AI for Documentary Records](ai-for-documentary-records.md).
For Australian and New Zealand newspapers, start from Trove and Papers Past with
[Australia and New Zealand record routing](australia-nz-record-routing.md); the OCR and
notice-reading rules here apply to them too.

## Decisive rules

1. **A failed name query is a failed retrieval attempt.** It does not establish that the
   notice was never printed. Check available issues, printed naming conventions and OCR
   separately; each failure needs a different remedy. (S1, S3, S8, S10)
2. **A listed title is not complete issue coverage.** Inspect the actual dates, editions
   and pages available for the event. A title's displayed year span does not establish
   that the required issue survives or is available to you. (S3, S8)
3. **Search the identifier the newspaper would have printed.** Read nearby notices to
   learn whether that title uses middle names, initials, married names or compressed
   surname lists. Do not keep repeating the modern full name. (S2, S5, S6)
4. **Keep printed spelling separate from OCR test strings.** A letter-substitution query
   can recover an image without demonstrating that the newspaper printed that spelling.
   A human-readable name can still be unsearchable. (S1, S10)
5. **Read the notice, not just the hit.** A surname can occur in one item and a travel
   verb in another on the same page. Confirm the subject and event within the actual
   item before assigning that event to the searched person. (S4)
6. **Publication location and date describe the newspaper.** They do not automatically
   identify the person's residence or the event's date. Travel, regional circulation,
   reprints and later proceedings can move the useful notice elsewhere. (S2, S3, S6)
7. **Make a clipping private before you save it.** Newspapers.com clippings are public by
   default: other people can see them on the All Clippings tab, in search and on your profile,
   with your member name. Before you clip an obituary, a notice that names living people or
   material for a client, set new clippings to private in Account Details → Clipping
   Settings, or choose private while you create that clipping. The setting changes only new
   clippings; use Edit on each existing clipping to change it. A library guide warns that
   saving or downloading a selected part of a page might also create a public clipping, so
   check My Clippings afterwards. In the research record, cite the title, date, page and page
   URL, not only a clipping link. (H4, H5, H6, S54)

## Resolve a title to a holding and an issue

Use this step when Browse lacks the expected title/issue, or when a newspaper catalog gives a
promising title without accessible pages. Keep three dates separate: the newspaper's publication
span, a repository's held span and the issues you actually inspected. A title directory or a
finding-aid collection link supplies a locator, not proof that the target issue is digitized.
(S12–S14)

After a miss in an Ancestry Newspapers.com index, read the collection's coverage notes and
compare them with the titles and issues available in Newspapers.com Browse [S103 @2026-11-22],
[S104 @2026-11-22]. For a U.S. locality, use the Directory of U.S. Newspapers in American
Libraries to identify additional titles and their holders [S105 @2026-11-22]. Inspect any
accessible likely issue directly and log that inspection separately from the index search.

1. **Resolve the historical title.** Begin with the event interval, likely publication locality
   and relevant language/community. For U.S. titles, search the
   [Directory of U.S. Newspapers in American Libraries](https://www.loc.gov/collections/directory-of-us-newspapers-in-american-libraries/).
   Open each plausible title record; record its title identifier (such as LCCN), place,
   publication span and catalog URL. Follow predecessor/successor records across a title change
   and keep their identifiers separate. A newspaper that changed its name can require a
   different title record for the target year. (S12, H1)

   For a county, list every title the directory shows across the family's whole residence period.
   Extend the period past deaths, because obituaries and estate notices come later, and back before
   the earliest births or marriages. Include small, inexpensive and competing papers. Use known party, labor, immigrant or working-class readership to choose additional titles [S37], [S38], [S39], [S40]. Give each title its own register row and verify the available issues before recording a miss [S14].
2. **Resolve the holder and format.** Follow the title record's holdings links and the identified
   institution's catalog. For each relevant holding, record institution, holding identifier or
   call number, format, stated held dates/gaps and access route. Print, microfilm and digital
   holdings can cover different date ranges. If you use a locality-based finding aid, follow
   its collection link to the actual provider or repository before recording coverage.
   A collection-level lead stays `holding unverified` until its holdings are checked [S13], [S14], [H2].
3. **Verify the target issue.** For a digital holding, open its issue calendar/list and then the
   required date and edition; record the pages present and what you could inspect. For a print
   or microfilm holding, prepare a bounded request or visit plan with title identifier, call
   number, format and exact dates. Record `physical issue not inspected` until the actual issue
   has been checked. A catalog's held date span alone does not settle a particular issue/page.
   Apply the OCR/name tactics below to accessible images; an access problem needs the recorded
   alternate holding or request, rather than more spelling probes [S14], [H2].

Search local library and historical society catalogs as well as the state library and WorldCat before closing a title search. The Library of Congress directory entry for the *Daily Sentinel-Tribune* omitted the Wood County District Public Library, where a researcher had used its complete microfilm run [S83]. Record each holding separately [S84].

**Artifact:** one register row for each title–holding–target-issue combination:

| Field group | Record |
| --- | --- |
| Title | Title ID/URL, printed title, publication place, publication span, predecessor/successor IDs relevant to the target year |
| Holding | Repository, holding ID/call number and catalog URL, print/microfilm/digital format, stated held dates and explicit gaps |
| Issue | Target date and edition, issue/page URL or physical locator, pages present, pages actually inspected, OCR availability observed |
| Decision | Retrieval date, status, next holding/request to check and next-check date |

Use `title lead only`, `holding unverified`, `digital issue inspected`, `physical issue inspected`,
`digital issue inaccessible`, `physical issue not inspected` or `issue absent from checked holding`.
Keep a no-match search in an inspected issue separate from those coverage/access states.
If several holders cover the interval, retain separate rows so the format and access result
remain traceable.

**Stop when** each selected title has an identified holding and an inspected target issue, or an
explicit unresolved status with its next action. If the necessary issue remains inaccessible
or absent, report that boundary and proceed only with the available scope under the stopping
rules below. Once an issue is inspected, use its identifier/URL in the recovered notice's source
record; the directory record remains the locator.

The Library of Congress migrated Chronicling America on **2025-08-04**. Its title directory is
now a separate searchable collection covering newspapers in all formats; digitized newspaper
pages are in [Chronicling America](https://www.loc.gov/collections/chronicling-america/).
The 2016/2023 tutorials' old tabs and screen positions are historical examples. Use current
collection links and inspect the destination rather than reproducing those old controls. (H1)

## Use a notice index's documented personal-place field

If a separate notice index actually documents a place-only query that includes personal
origin or birthplace, try the supported locality without an uncertain surname. Retain that
field's meaning, filters and candidate identifiers, then inspect the full notices.
Publication place has a different role. The [Ryerson index description](https://lostrussianfamily.wordpress.com/2025/09/27/two-major-australian-databases-ease-researching-of-ussr-ancestors-and-relatives/)
supplies a conditional retrieval route; when the field role is unknown, keep the route
unavailable rather than assuming present syntax or coverage on any provider.

## Follow an obituary collection's actual arrangement

Inspect the index or clipping collection before repeating a global name query. Select the
required year in a year-gated text index. For a volume limited to a surname/letter range,
choose the supported volume and browse bounded pages when usable text search is absent.
Carry any newspaper, issue and page reference to the full notice; keep missing publication
details unknown. The [year-index and clipping-volume examples](https://whoareyoumadeof.com/blog/how-to-search-for-obituaries-for-free-by-name/)
motivate this dispatch. Searching accessible text does not search unseen images or other volumes.

## Search recipes

The following names, addresses and queries are invented examples, not executed searches
or reported discoveries. Newspapers.com documents this syntax: a search requires all its
terms by default; quotation marks keep words together; `?` replaces one letter and `*`
several letters; `OR` and `NOT` go between terms, written in capitals as in its examples.
It documents no minimum number of letters for a wildcard and no proximity operator, so do
not rely on either. A wildcard hit is an OCR probe, not a spelling the newspaper printed.
Set place and publication-date limits separately. (S9, H7, H8, H9)

| # | Trigger | Search or browse plan | What to inspect before using the result |
| --- | --- | --- | --- |
| 1 | Nothing appears for the expected place and date. | Use Browse to inspect titles and the actual available issues for that interval. Check competing papers and predecessor/successor titles, including small title changes such as adding Daily. (S3, S8, S9) | Is the relevant issue, edition and page present and accessible with your subscription tier? Record a coverage gap separately from a query that returned no match. |
| 2 | A full name returns no useful notice. | Inspect naming style in a known issue. For William Richard Evans, try `"Richard Evans"`, `"W R Evans"` and a surname-only `Evans` search in a tighter place/time scope. Also try a known nickname and the abbreviated given name that editors used to save space even if the person never did, such as `"Wm Evans"`, `Jas.`, `Saml.`, `Geo.`, `Chas.` or `Thos.` (S2, S6, S91, S92) | Are these forms actually used by the title or plausible for this person? Initial spacing and punctuation can differ; a failed exact phrase does not eliminate the initial form. |
| 3 | A woman's own full name is missing. | Try her maiden and married surnames, then her husband's name or initials: `"Mrs Robert Evans"`, `"Mrs R Evans"`. Keep searching her maiden surname in issues long after the wedding, where an item can call her `"the former Mary Jones"` or `"formerly Miss Jones"`. Search surname-only lists and notices about relatives when her given name is omitted. (S5, S9, S11, S75, S76) | Does the item identify the wife, or only a different person sharing the surname? Read compressed lists with their heading and surrounding sentences. One `Misses` or `Mrs.` before a run of surnames applies to each of them: after `Misses` they are maiden surnames, after `Mrs.` married surnames, without given names. |
| 4 | The image looks readable but the query misses it. | First look at how the OCR read the name: check the highlighted words on a hit's page thumbnail, or open the article text (OCR) under a clipping of the item, made private as in rule 7. Query the misreading you see. Otherwise test a small set of visually plausible letter confusions, such as B/H or C/E, based on the scan, or run one wildcard probe such as `Ev?ns`. For a `Mc` surname, try dropping the `c` and splitting the remaining `M` off as an initial: Peter McLane was indexed as Peter M Lane [S82]. Shorten an over-specific phrase, search an uncommon given name alone within a tight place and date scope, or search another intact word from the expected notice. (S1, S11, H7, H8, H10, H15, S82) | Read the original letters. Label a distorted or wildcard search form as an OCR probe, not a corrected historical name. |
| 5 | A smudged target name may be in a group notice. | Search a known relative, witness, neighbor or club member who could appear in that same item; alternatively search the known club name within the relevant title/time. (S1; club-name search authored) | Does the recovered item actually include the target? A notice about the club alone supplies context, not personal participation. |
| 6 | A common surname produces too much noise. | Try a surname with a known occupation or address: `Evans carpenter`, `Evans "42 Oak Street"`. In 20th-century papers, also search the family's known telephone number: a classified ad for eggs, straw or livestock may print only the number. Run these as separate clue-based passes. (S3, S79, S80) | Do the clue and surname belong to the same notice and person? Inspect the full address; a reused address can lead to different occupants. A telephone number can match through a transposed or mistyped digit, so check that what the ad offers fits the family. |
| 7 | You need a visit, departure or migration clue. | Run one verb per pass: `Evans visited`, `Evans arrived`, `Evans left`, `Evans returned`, `Evans moved`. Read society items in both plausible departure and destination papers, and in the parents' hometown paper, where a person who never lived there can appear visiting relatives. (S4, S71, S72) | Who performed the action, when, and where? A highlighted surname beside an unrelated arrival notice is not the searched person's trip. |
| 8 | Obituary searches miss women or a legal event. | Inspect bridal showers, society columns, school/teacher/nursing news, guardianship, estate and land-sale notices. Use surname with a relevant keyword, such as `Evans guardian`, then browse the corresponding section. (S3, S5) | Is the item an announcement, allegation, filing or outcome? A guardian notice is a court-record lead; it does not establish that both parents died. |
| 9 | You need an overlooked connection to a place. | Search `"letter list"` in a plausible locality and interval, then read the listed names, including initials and women. Browse such lists when the person's name fails OCR. (S7) | An unclaimed letter can suggest an intended destination or travel stop. It does not establish residence; shared surnames do not establish kinship. |
| 10 | The hometown paper fails or an immigrant's name is distorted. | Search neighboring towns, regional papers and former residences. Choose papers by distance, not by county or state line: the nearest larger town's paper, a neighboring county seat's paper and weeklies across a state line can carry the area's obituaries and local columns. Include ethnic-language papers serving the community, even when published outside its city; try attested native-language name forms. (S3, S6, S63, S64) | Separate publication place from event place. Inspect the actual foreign-language name and origin statement rather than assuming an English rendering preserved them. |
| 11 | One article suggests a longer story. | Search subsequent months for court proceedings, settlement or verdict; revisit former residences for a death mention. Reuse newly recovered witnesses, addresses and institutions as search clues. (S2, S3) | Record each article's publication date and reported event date separately. Do not turn the first report or filing into the final outcome. |
| 12 | Keywords still fail despite an available likely issue. | Switch retrieval mode: browse its pages directly. For an obituary, marriage or birth item, also search the matching index. Newspapers.com's 2023–24 posts put these indexes in the Categories drop-down under the Keyword box. For an obituary or marriage, the Newspapers.com index on Ancestry is a second route. Follow any candidate to the image. (S5, S6, H13, H14) | The index is another access path, not independent corroboration. A category search reaches only items placed in that index, so a miss there needs the same search without the category. Check the full notice and its boundaries; inspect missing or inaccessible pages separately. |

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The research subject’s name and any identifying details in the repeated query go to Newspapers.com.\
If a person drops out of the historical record and hometown-area papers yield nothing,
rerun the same name search beyond the last known home state. When the destination is unknown,
drop the title restrictions and keep the original publication-date window as you search across
the country. Leave publication place open if the country is uncertain [S102]. Read distant hits
for details that distinguish the person from namesakes.

A Pennsylvania-only pass would have missed the *Sacramento Bee* hit from the available excerpt
of the episode’s sponsor segment [S100], [S101].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The research subject’s surname fragment and identifying search terms go to Newspapers.com.\
When a printed misspelling could explain an exact-surname miss, try the wildcard tactic suggested
in the interview, from the available excerpt [S97]. First test an internal asterisk on a known public
hit in the user's account. If it works, keep the likely intact beginning and ending of the surname
and replace the uncertain letters with `*`, as in `Ev*ns`. Run the surname probe with the same title
and date limits [S98]. Read the name on the image and record the printed spelling, OCR text and
query separately. If the probe fails, search an intact event term or browse the likely issues.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The deceased family members' surname and the locality terms in the query go to Newspapers.com.\
When Irish graves share a surname, search that surname with the townland on each headstone,
using the approach from the available excerpt [S106]. Run separate passes for the
inscribed form and any attested modern form. For a Northern Ireland townland, compare the
forms in the Northern Ireland Place-Name Project's historical locality entries [S107]. Read the
notices for explicit relationships before linking the people buried there.

For a branch that moved to Canada or the United States, search its destination papers with
the same surname and the Irish townland or county as keywords, following the search
from the available excerpt [S106]. Set the publication filter to the destination.
Use an origin named in a destination notice to choose which Irish papers to search next [S108].

When a notice dates an event relative to another date, such as ‘issued yesterday’ or ‘last
Wednesday’, retain the literal wording and its anchor before deriving a date. For `ult.` (the preceding month), identify the date of the item, letter or original report that supplied the expression [S33], [S47]. Save `wording |
anchor and basis | derived event date | uncertainty` separately from the publication date. If a
reprint, such as one whose original date is unknown, or an ambiguous anchor prevents a reliable
calculation, leave the event date unresolved.

For `inst.` or ‘instant’, use the month of the dated statement; for `prox.` (proximo), use the next month [S85], [S86]. A regiment leaving ‘on the 10th instant’ was due to leave on the tenth of the writer’s month [S85]. Check for a dateline or quoted letter before using the issue’s month.

For an independently documented business/address, also search a successor's advertisement
and read any wording naming the former operator. Retain the notice date and literal wording
about the former and current operators as a business-occupancy lead. Correlate dated records before
assigning the person’s residence or departure. John Dawson’s January 1830 hotel advertisement in Athens named L. A. Erwin as the former occupant, leaving the date of the handover and ownership open [S52].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The deceased occupants' historical house number and street name go to Newspapers.com.\
Search the historical house number and street name by themselves in local papers from the
household's period of occupancy. Leave the surname out of this pass [S94]. Check estate-sale and
auction ads for itemized household goods [S95]. Search before a documented move as well as after a death: an estate-sale advertisement may describe belongings sold before a family left [S93]. Verify who occupied the address on the advertisement date before attributing the goods.

Date every letter-list entry and record the office holding the unclaimed mail; it suggests an
intended destination or travel stop, not a residence. A pickup office can sit in another county or state than the residence, so search the
residence records of every county that office served, including across the border. A dated
series of offices can frame a migration before residence records show it; a new pickup office
supports a move hypothesis, not a move date. In the same case, a December 1841 entry at
Columbus, Georgia, prompted the hypothesis that the man meant to collect mail there while moving
to Chambers County, Alabama. Columbus is across the
Chattahoochee and not on Chambers County's border. (S7, S52, S53, H3)

When a family moved to a place where no relative, former neighbor or associate can be found, look for an advertisement that drew them. Land agents, speculators and developers promoted their settlements in newspapers, as well as in broadsides, pamphlets and books aimed at prospective migrants [S73], [S74]. Search the papers of the place the family left, in the years before the move, for the destination's name with a word such as `land` or `farms`. An advertisement found there is a motive to test against the move's date and route; it does not show that the family read it [S73].

When the local issue is lost, undigitized or silent, search the name across titles without a place filter. Editors exchanged items and wire services carried them to distant and overseas papers [S15], [S17], [S19], [S21], [S22]. A Louisiana notice asked Texas papers to copy it [S47]: use Texas as a place to search, then verify which title actually printed it. The request alone leaves residence and travel unresolved. For each copy, record title, date, length, differences and any credited original. Group derivative versions under the originating report, including any borrowed claim about where the person came from [S14], [S16], [S18], [S20], [S23].

For a death, set the issue window from the event chain rather than stopping at the first obituary.
A short death notice can precede a full obituary printed months later, after a winter burial or
once news of a death abroad or at sea arrived. Memorial or anniversary notices can appear a year or
more later. If a burial date is known and name searches fail, browse the issues just before it.
Read each concurrent title's notice and look for paid death notices, inquest and estate notices.
Record each as a separate item with its own publication date: named relatives can differ, and
identical text may be a copy. Sources: [timing](https://www.youtube.com/watch?v=AU9HgBQ8PwM),
[delayed publication](https://www.youtube.com/watch?v=_PfJrt10Srg),
[burial-date browse](https://www.youtube.com/watch?v=blTnP8wcqvk),
[memorial notices](https://www.youtube.com/watch?v=70ya-VPbkBc),
[concurrent obituaries](https://www.youtube.com/watch?v=qLzNItRPj_c) and S3. None sets a typical
interval, so set the extended window as an explicit budget.

If an obituary refers to an unidentified event, such as “the flood,” use the event's likely place
and date to select local papers [S94]. Follow the speaker's suggestion from the available excerpt
and browse the issue for that date and the issues immediately before and after it [S93], [S96].
Read the local reporting for the event's name and effects. Keep the identification provisional
until the place and timing fit the obituary's reference.

For a death in roughly the last hundred years, search the papers of the birthplace, the marriage place and every place the person lived for a significant time, as well as those of the death place: a family could place the obituary in a former hometown [S62], [S63]. The tip's author notes that this does not hold for most 19th-century deaths [S62]. For an emigrant, also search the home country's papers. A family there could print a death notice for a death abroad that the destination's papers never carried, and a Scottish local paper's death notices of 1837 to 1855 include deaths in Australia, Canada, India and the United States [S65], [S66].

Read local correspondents’ and gossip columns in the weeks or months before the death for an illness, hospital stay or relative’s visit [S80]. A 1923 item about Nancy Rampley’s illness gave her sister’s residence but slightly misstated her name [S81]. Use the place to search the sister’s own records before adopting the spelling.

Read an obituary's relationships as the family's account. The newspaper or funeral home usually printed what the family supplied without checking it, a relative often wrote it in a hurry, and space or cost could cut names [S67], [S68]. When a long survivor list can be grouped more than one way, for example which surname or spouse goes with which listed child, write out every grouping and test each against the obituaries and records of the relatives it names [S67].

For a recent death, also read the guestbook, tribute wall or comments under an online obituary [S87]. One memorial platform's guestbook lists each signer with their connection to the deceased, such as family, friend, coworker or schoolmate [S88]. Record each stated connection as the commenter's claim and use it as a lead. Commenters are usually living people: keep their names and messages in the user's private research notes and out of anything shared (Living people, in `SKILL.md`).

For a migrant who died away from home, inspect death lists in the destination city’s papers. A transcription of the *Wiener Zeitung* of 8 March 1871, p. 955, describes Georg Skoday as having arrived from Verbocz and dying in Vienna’s general hospital on 2 March [S46]. Copy any name, age, occupation, cause and address in the entry. Separate the death date from the issue date and follow the stated origin to its registers, leaving birthplace open.

For vital events, run surname-plus-event passes instead of full-name searches: born, christened,
engaged (a truncated stem where the engine supports it), shower, wedding, eloped, divorce,
anniversary, funeral, cards of thanks. A birth notice may name only the parents ('born to Mr and
Mrs …'), so a miss on the child's name eliminates nothing. Linking an unnamed child rests on date,
parents and family records, so record that link as inferred. Where marriage records are lost or
announcements scarce, search marriage-licence lists. A licence does not prove that a ceremony took
place, or when. Derive a date from a list's relative wording only as described for relative dates
above. Sources:
[vital-event keywords](https://www.youtube.com/watch?v=RvbalvEJXn8),
[death-notice types](https://www.youtube.com/watch?v=_PfJrt10Srg),
[unnamed child](https://www.youtube.com/watch?v=v_tpU77sOn4),
[licence lists](https://www.youtube.com/watch?v=NMjImd0Oy7U)
([also](https://www.youtube.com/watch?v=ezp_SFmMdYM)). A surname hit is not an identity match.

Read a wedding report to its end. Some local papers printed the guests or the presents with each giver's name [S77], [S78]. Known relatives among the givers corroborate that the bride or groom is the person you are researching, and a giver you cannot place is a lead to kin or associates: relatives can appear there with no relationship stated [S77], [S78]. A list printed as partial leaves givers out, so a missing name shows nothing [S78].

Do not cap the publication-date filter at the event year, and open hits dated long after the
person's lifetime. Congregation histories, 'years ago' columns and rosters of a war's participants
printed decades later can carry earlier births, marriages, service or obituaries. This matters most
when the original years are not digitized. Read the heading to learn what compiled list or column
it is. Record the later issue's date, any original date it cites and the stated event date
separately. Search the original issue or underlying record. A Civil War roster shown in one presentation was printed in 1905 [S34]. Treat late rosters, reprinted obituaries and retrospective church features as later accounts, recording any abridgment [S29], [S35], [S36].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The deceased ancestor's or veteran's name and any identifying search terms go to Newspapers.com.\
After the ancestor's death, search the family surname with `"family reunion"` in papers
serving the descendants. Read the report for earlier generations, as in the case
from the available excerpt [S109]. Use its named relationships as leads to records from the
lifetimes of the people it describes [S110].

For Revolutionary War service leads, search the veteran's name in issues around documented
local commemorations, using the video's suggestion from the available excerpt [S111].
Test the July 1826 Independence Jubilee and the 1876 Centennial where their coverage
fits the veteran's community [S112], [S113]. Record any stated unit, rank or service as a lead
to check against service or pension records.

For probate, court, tax or land matters, and especially when deeds or court files are missing,
browse the legal-notice matter as well as running name searches. Notices may lack a heading and sit
among advertisements. Find the publication rule in force for that time and place. It may name a
qualifying paper, another county or a number of insertions, so search every qualifying paper,
including cheap legal-notice papers, across the whole insertion run. Copy any deed book and page,
trustees, recording date or land description verbatim, and use them to request the record; carry any
court and case number into the [handoff from a court notice](#optional-handoff-from-a-court-notice).
A notice is a published summary. It does not establish the outcome, title or kinship,
or that the book survives. 'Residence unknown' means unknown to officials on that date, not a move
or death. The [legal-notice examples](https://www.youtube.com/watch?v=Mr03rzuk2gA),
[child-support account](https://www.youtube.com/watch?v=5vF5SAYIYU0) and
[attorney's account](https://www.youtube.com/watch?v=q5-kKlUKfHs) motivate this. The statute in the attorney's account is
illustrative; establish each jurisdiction's actual rule.

When deed books burned or are thin, also browse the routine real-estate-transfer columns [S89]. An NGS Monthly article, judged from the available excerpt, says that from the late 19th century many papers, though not all, printed brief abstracts of recorded transfers and mortgages that name grantors and grantees, locate the land and give the price, and that these can stand in for a deed index [S90]. If the county's own run of the paper burned too, look for the same title in another holding with the title–holding–issue workflow above [S89]. Copy each abstract verbatim with its issue and page, and use it to request the deed where the book survives.

In an equity notice addressed to absent defendants, copy the named parties, court, type of suit and wording about residence [S55]. The September 1840 Cheraw District notice in *Goodson et al. v. Beck et al.* named out-of-state defendants in a bill for account and partition [S56]. A separate Cheraw order called for publication twice a month for three months [S57]; an 1853 South Carolina decision explains the period’s use of publication in place of service [S58]. Search for the underlying case file before drawing conclusions about the parties.

Search crime news as well as obituaries and family notices. In the 1940s to 1960s, U.S. local papers reported police raids on gay bars and often printed the names, addresses and occupations of the people arrested, sometimes on the front page [S59], [S60]. After the 1964 raid on the Fun Lounge near Chicago, in which 109 people aged 19 to 56 were arrested, the *Chicago Daily News* printed a partial list in which almost every name carried the person's age, address and place of work, supplied by the police; other Chicago papers printed teachers' names and addresses [S60]. A journalism historian describes the same practice in Washington, D.C., where men had their names, ages and street addresses printed [S61]. When the question concerns a relative who may have been gay or lesbian in that period, or a family story of an arrest or a lost job, search the surname with `raid` or with the bar's name, such as `Evans raid`, and browse the issues from the day of a known raid onward. Read the item as a report of an arrest only: it does not establish the person's sexual orientation or any offence. A court dismissed the charges against 99 of the 109 Fun Lounge arrestees three weeks later [S60], so follow the case as in row 11 of the search table and the [court-notice handoff](#optional-handoff-from-a-court-notice).

Treat such a report as a sensitive finding. Someone arrested in the 1960s may still be alive, so treat each person it names as living unless you know otherwise. Keep the name, the arrest and any copy of the item in the user's private research notes. Never publish, share or upload a possibly living person's name or arrest from such a report, for example in an online tree, a public clipping or a report for others (privacy gate and Living people, in `SKILL.md`). Do not use the printed address or workplace to find where that person lives or works now. In anything shared, refer to the other people the report names by role, as `SKILL.md` asks for third persons named in police files.

When a county's own records are burned or thin, search its associates who advertised often,
such as innkeepers and merchants, as hard as the target. Date each advertisement and notice by
title and issue. An associate's run can trace a group's route where the target yields only one
or two notices. An associate's advertisement places the associate, not the target, so tie the
target in with a notice that names him, such as a sheriff's sale he signed as deputy, which
places him in office in that county on that date. Pair a sheriff's-sale, execution or
bankruptcy notice with any surviving sheriff's deed: the notice explains why the deed exists,
and the deed can confirm whether the sale took place. In Cass County, Thomas B. Royston signed an 1834 sale notice as deputy sheriff, while John Dawson’s more frequent advertisements traced Dawson’s movements [S52], [S53].

From notices already found, list every printed form of address and search those the initials and
married-name passes miss. These include title-only forms (`Judge Evans`), honorific-only forms
(`Mr. and Mrs. Evans`, `Master Evans` for a boy), Jr./Sr., and typesetting shortcuts such as `M'`
for `Mc`. Use period vocabulary for clue terms, such as railway as well as railroad. For an
obituary, also search a relationship phrase joined to a relative's printed name, such as
`"wife of John Evans"` or `"child of Emma Evans"`. Use exact phrases only as currently documented.
Any hit is only a candidate; confirm within the item that it concerns the target. The
[typesetting and title examples](https://www.youtube.com/watch?v=RHv0Zxq5MlU),
[honorific-list example](https://www.youtube.com/watch?v=5iXqxWAnHRQ) and an untested
[viewer suggestion](https://www.youtube.com/watch?v=UMxoiaZiSkc) motivate these passes. They do not
show how common any form was.

## Bounded execution and stopping rules

Begin with a target question, an approximate event interval, known residences, names and
two or three distinctive clues. Set a query budget and an issue-browsing budget before
starting. Choose specific titles and intervals; “browse newspapers” is not a bounded task.

Name the venue actually searched in the examined scope. A general web search is not a newspaper
search: database pages may not be indexed. Use web search only to discover titles and sites, then
search inside each. The same title may also be hosted elsewhere, such as a state archive or
Chronicling America, with its own OCR. A re-search there can surface a missed name, but it finds
the same printed notice, not corroboration. Treat an aggregator-site obituary as a possibly scraped
or rewritten copy. Find the original before extracting relationships; a relative missing from the
copy proves nothing. The [database talk](https://www.youtube.com/watch?v=1Ptl1u6wRoY),
[second-host example](https://www.youtube.com/watch?v=ezp_SFmMdYM) and
[aggregator examples](https://www.youtube.com/watch?v=81A_q2fGuqo) motivate this. They do not
establish current indexing, which host's OCR is better, or how to spot rewritten text.

For New York titles, also search Fulton History (fultonhistory.com), a free site run by one man; a 2023 comparison counts more than 1,000 papers there, over half of them from New York, and reports that its searches may not lead to every result and that the site has periodic outages [S69]. A 2020 user guide reports that a search there shows at most 5,000 hits and that OCR misreads letters such as `i` and `l` [S70]. Narrow a broad search to one title or a short date range until it returns fewer than 5,000 hits, and try letter-substitution probes as in row 4 [S69], [S70]. A miss there is a no match for that search only; a site that does not respond is access blocked.

Run the recovery in this order:

1. **Check availability.** Record each promising title and its relevant available issues.
   If the required issue is absent, investigate another paper or its earlier/later title.
   Libraries and historical societies may hold microfilm, originals, abstracts or clipping
   files. Repeating spelling variants cannot recover an issue absent from the venue. (S3, S8)
2. **Change the identifier.** Use the title's printed naming style, women's married forms,
   a constrained surname search and a few image-informed OCR probes. Change one useful
   dimension per pass so you know which adjustment produced a candidate. (S1, S2, S5, S6)
3. **Change the route.** Search an associate or distinctive clue; expand publication
   geography and timing when the person's movements or the story justify it. For the
   relevant event types, try the matching index through Categories or on Ancestry.
   (S1, S2, S3, S6, S10, H13)
4. **Read selected issues.** Use the expected section as an entry point. If its placement
   is unknown, browse the selected issue's pages. Record which issues and pages you
   actually examined; skipped or inaccessible pages remain unexamined. (S6)
5. **Inspect every candidate notice.** Open the page, identify the item boundaries and
   read the sentence linking the person to the event. Keep the title, publication place,
   issue date, page, URL and the notice's own stated event date. (S4)

Newspapers.com sorts results by Best Match unless you choose otherwise. To read a story's reports in order, sort by paper date with the oldest first. When you repeat a search from the research log, sort by Date added, which puts matches from the most recently added papers first, so the papers added since your last run come before those you have read [H9 @2026-11-14], [S65 @2026-11-14]. That order goes by when a paper was added, so it does not bring forward a match that the site's re-OCR newly found in an older paper; a no match recorded before the re-OCR still needs the repeat described under the result labels below.

If a target issue was missing in Chronicling America when you last searched, look up the title's
LCCN in the Library of Congress's [Recent Additions](https://guides.loc.gov/chronicling-america/recent-additions)
table. Open the matching batch link and confirm the target issue date and edition before counting
it as newly available [S99 @2026-11-20].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The logged query sends the research subject’s and any named associates’ names and identifying terms to Chronicling America.\
Rerun the logged query over the newly available target issues, following the interview's suggestion
from the available excerpt to revisit a search after holdings grow [S97]. Keep the earlier search
scope and date in the log. If the issue is still missing, keep the coverage gap and check the next
holding.

Stop this retrieval task when the requested notice has been recovered and inspected, when
the remaining necessary material is unavailable or inaccessible, or when the agreed
search/browse budget is consumed. Report which of these conditions ended the run.

Use precise result labels:

- **Recovered candidate:** an inspected notice matches the retrieval question; state any
  remaining same-name uncertainty and hand it to the identity-evaluation recipe.
- **No match in examined scope:** list the queries, titles, intervals and issues examined.
  Do not broaden this to “no newspaper record exists.” Newspapers.com said in a blog post of
  2026-11-09 that it had completed a re-OCR of the whole site and that a new search may return
  results the older OCR missed. A no match recorded before that post may rest on the older text,
  so run its queries once more over the same titles and intervals before relying on it.
  [H15 @2026-11-12]
- **Coverage gap:** identify the absent issue, edition or page and the next holding to check.
- **Access blocked:** identify material that exists but could not be inspected.
- **Publisher Extra required:** a kind of access blocked. Use it when a hit is listed but its
  page needs a Publisher Extra subscription. Publisher Extra adds the papers still under
  copyright ("typically 1931 and newer", per the plans page); Basic does not include them.
  Such a hit shows that the issue exists and that its OCR matched the query, so it is neither
  a coverage gap nor a no match in examined scope. Record the subscription tier you searched
  with: Ancestry's Newspapers.com FAQ says All Access includes Publisher Extra, yet it tells a
  member who sees indexed records but not the images to move from All Access with Basic to
  Publisher Extra, so check the account rather than assume. [H11 @2026-11-12], [S10 @2026-11-12]

### Optional handoff from a religious-life notice

For a supported religious-life lead, inspect available reception or vow notices using relevant
period terms such as `ceremony of reception`, `receive the habit`, `white veil` or `postulant`.
Retain any birth/baptismal and religious names actually linked in the same item, its named
institute, literal event wording/date and notice locator. Use that institute as a lead to its
actual custodian and appropriate record series through the [manuscript-holder workflow](research-documentation.md).
Keep a ministry location separate from the motherhouse; shared postnominals do not uniquely
identify an institute. The [historical interview](https://familylocket.com/rlp-410-catholic-nun-research-with-sunny-morton/)
motivates this name-to-institute bridge. A notice does not guarantee a personnel file or resolve
the candidate's identity; preserve its literal ceremony stage rather than equating all stages.

### Optional handoff from a court notice

If a recovered notice supplies a case or docket number, preserve it with the printed parties,
stated court/jurisdiction and date, keeping the newspaper citation. Resolve the relevant court
series and present custodian for that period; for a U.S. court use
[court case files](court-case-file-recovery.md), or
[U.S. federal court case files](us-federal-court-case-file-recovery.md) when the court was
federal; for a reported arrest, criminal trial or imprisonment, also use
[criminal court and prison records](criminal-court-prison-record-recovery.md). Use the number only
in a collection whose actual arrangement supports it. Check a retrieved file against the parties
and case context, preserving its own locator, inspected pages and gaps. Keep a notice-only lead or
unavailable file explicit.
The *Dallas Daily Herald* docket for 28 October 1875 gave no. 2745 for *Belle Carpenter v. John W. Carpenter*, leading a researcher to the numbered Dallas County file [S48]. Keep each allegation attributed to its source until the case papers establish the outcome.

## Prompt-craft

```text
Find a newspaper notice about [person/event], approximately [interval], associated with
[places]. Known printed names/aliases: [forms]. Distinctive clues: [relatives, address,
occupation, church, club]. Query budget: [limit]. Browse budget: [specific issues/intervals].

Check actual issue availability first. Inspect the title's naming style; try initials,
middle names and relevant maiden/married/husband-name forms. If OCR fails, search an
associate or distinctive clue, then browse selected issues. Expand place/date only with
a stated reason. Use only currently documented query syntax. Make any clipping private
before saving it.

When Browse coverage is insufficient, follow the title–holding–issue workflow and
return its register with the documented fields, statuses and next action.

Inspect the complete notice before attaching an event to the person. A surname and verb
elsewhere on the same page are not a match. Treat a letter-list entry as a connection
clue, not proof of residence. Return candidate notices with title/date/page/URL, the
queries and issues actually examined, and the exact stopping condition. Label unavailable
issues separately from no-match searches. Do not invent discoveries.
```
