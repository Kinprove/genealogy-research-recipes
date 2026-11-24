---
id: "irish-catholic-parish-image-recovery"
title: "Recover an Irish Catholic parish entry at the NLI"
summary: "Find an Irish Catholic baptism or marriage in the National Library of Ireland's parish-register images."
kind: "records"
scope: {"platforms": [], "tasks": ["RootsIreland/Findmypast transcriptions, Catholic parish/register selection, a link opening the register's first page, date browsing or exact image citations."]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "IRISH-CATHOLIC-PARISH-IMAGE-RECOVERY-01", "text": "Carry an Irish Catholic baptism or marriage lead into the National Library of Ireland's register images, inspect the actual entry and preserve the register and image locators. A transcription can identify a parish and date without supplying an image; a baptism date remains a baptism date unless the original separately records birth."}]
handoff: []
checked: "2026-10-07"
checked_basis: "checked 2026-10-07"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request", "third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Britain and Ireland", "order": 132}
---

# Recover an Irish Catholic parish entry at the NLI

## Contents

- Goal
- Inputs and routing
- 1\. Select the Catholic parish and the correct register
- 2\. Use the external index to reach the image sequence
- 3\. Narrow pages by event and date, then inspect the entry
- 4\. Save the register identity and the exact image locator
- Prompt pattern

## Goal

Carry an Irish Catholic baptism or marriage lead into the National Library of Ireland's register
images, inspect the actual entry and preserve the register and image locators. A transcription
can identify a parish and date without supplying an image; a baptism date remains a baptism
date unless the original separately records birth.

## Inputs and routing

Start with the candidate name, event, approximate date and supported place or parish. Keep a
transcription or commercial-index lead as a separate record of what it displayed. Use the
FamilySearch and Ancestry recipes for their own search/access tools, source-citation for citation
construction, and ai-for-documentary-records for handwriting or Latin interpretation. This recipe
adds the NLI parish, register, filter and image-recovery procedure.

If an emigrant's origin is only "Ireland", first seek a more specific locality in a bounded
set of destination-country records. In particular, inspect an available will for a named
executor or beneficiary still in Ireland, and follow a documented sibling's records for an
origin clue. Record `literal place | person and role | record/date/locator | next locality check`.
A beneficiary's Irish residence is a locality lead, not the emigrant's birthplace or proof
of their relationship. Compare the recovered place with the Catholic parish and diocese in
step 1; do not silently substitute a civil parish or townland. If no sufficiently specific
place emerges, leave the parish unresolved rather than selecting a same-name family. [P6]

## 1. Select the Catholic parish and the correct register

Search the NLI parish name or use its map to inspect the locality. Confirm the Catholic parish
and diocese before selecting a register: a civil parish or townland is a different geographic
unit. The map supports adjoining-parish discovery; it is not an exact boundary map. [O1]

Identify the parish type from the source's church name, denomination or collection heading.
For a Catholic event with a Church of Ireland or unqualified parish label, use the recorded
townland or street to identify the Catholic parish that served the place at the event date.
Confirm that jurisdiction before selecting a same-name register. [S9, S10]

Read the selected parish's register information. Record microfilm/item, event type and available
dates, then open the corresponding register image or microfilm link. A parish can have several
volumes covering different events and years, as the Ancestry demonstration shows. [P3, O1]

Check the register's coverage before you read a miss as absence. The NLI images are of baptism
and marriage registers up to about 1880, the microfilming cut-off; most parishes recorded no
burials before then. Start dates run from the 1740s–50s in some city parishes, through the
1780s–90s in counties such as Kildare, Wexford, Waterford and Kilkenny, to the 1850s–60s on the
western seaboard. [O3, O5] The images are not name-indexed on the NLI site. Findmypast and Ancestry
index the same images, free with an account, and RootsIreland (paid) indexes most parishes,
generally to about 1900. [O3, O4]

**Privacy gate:** <!-- privacy-gate: request --> An entry after a register's end can name people
who may be living; answer the privacy gate in `SKILL.md` before you request one. For an event after
1880, ask the parish, which keeps the original registers; a priest may search them for a fee or
donation. [O5]

Record the alternative names given on the NLI parish page. A Catholic parish can appear under more
than one name, so a lead's parish name may not match the NLI heading. Match the lead's parish name
to an NLI name or listed variant before concluding the parish is absent. [P4]

If the target date precedes a parish’s surviving register, check when the parish was formed and which parish previously served the place. In the 2016 demonstration, a parish created after 1850 had a neighbor with earlier registers covering the formerly undivided parish [P3]. Record the dates and jurisdiction before choosing a volume.

**Output:** `place lead | Catholic parish | diocese | register URL | microfilm/item |
event type | described dates | parish-history question | next register`.

**Check:** The selected series fits the event and date. A place-name match or modern parish
alone does not establish that coverage.

## 2. Use the external index to reach the image sequence

For the NLI register-image site, the documented search is by parish, not a person's name.
Use the parish/date/event from an external index or transcription to choose the image sequence,
or browse the defined register directly. [O1]

If the NLI images lack the target event or year, check RootsIreland for the baptism, marriage or
burial. Choose the county or genealogy centre under **Online Sources**
[S9 @2026-11-22] [S11 @2026-11-22] [S12 @2026-11-22].
Check the Roman Catholic parish row for the event column, date range and any listed gaps
[S13 @2026-11-22]. Record the list URL and mark an omitted event or year as an index coverage gap.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A named lookup sends the subject's name and event details to RootsIreland. Apply the privacy gate in `SKILL.md` before entering those fields.

Search the listed Catholic series when it covers the event and year. Save a hit as a
transcription lead. Use its parish, event and date to select an NLI image sequence where one is available.

After an earlier RootsIreland miss, compare the logged coverage with the current county list
[S16 @2026-11-23] and check for additions dated after that search [S15 @2026-11-23]
(coverage lead from the available excerpt [S14 @2026-11-23]). Repeat the named lookup when the
added coverage includes the target Catholic parish, event type and year. Record the change,
its source URL and the retry date.

In the 2022 RootsIreland demonstration, a baptism transcription supplies the parish and a link
to NLI. In the 2024 comparison, a Findmypast transcript has both an NLI register link and a
separate original-record viewer: one opens the NLI sequence at its beginning, while the other
opens the demonstrated entry in Findmypast. These are historical examples; verify the actual
destination and access outcome instead of assuming every current index has either link. [P1, P2]

If no index lead appears under the English given name, search again under its Latin register form.
In the 2022 classes Johnson says Ancestry (and Findmypast, which shares its database) shows
the priest's Latin given name without an English equivalent. Neither class gives a list of
equivalents or says whether this still holds, so record which form produced the hit. A nil result
under one form is not evidence that no entry exists. Confirm any Latin-form hit on the image before
linking it to the English-named person. [P1, P4]

Preserve both the index URL and the opened image/register URL. If a link lands at the register's
start, the original entry remains to be located. If access fails, record the exact route and
failure; the register has not been examined through that route.

### Additional search keys and regional transcripts

For a late-1700s Catholic baptism or marriage, check IrishGenealogy’s Church Records
as Daniel Loftus suggests [S5 @2026-11-18] [S6 @2026-11-18]. Use the church area,
event type and year range [S7 @2026-11-18]. Confirm coverage for that parish, event and
year before interpreting a miss. For example, Irish Ancestors lists eighteenth-century
baptisms for St James’s, Dublin City, on IrishGenealogy [S8 @2026-11-18].

- **Regional transcripts after the NLI run.** Check IrishGenealogy’s parish and year coverage. Its help lists Kerry baptism and marriage transcripts to about 1900 and Dublin City Catholic registers [S1 @2026-11-16]. Preserve a transcript separately from an original image; this regional route does not extend the NLI images across all Ireland.
- **Sponsors and witnesses.** Search a documented sponsor or witness as well as the principal. IrishGenealogy results include parent, sponsor and witness roles [S1 @2026-11-16]. Read the role and event before extending the cluster; sponsorship does not itself name a family relationship.
- **IrishGenealogy Latin given names.** Use Carolus/Charles, Gulielmus/William, Jacobus/James, Joannes or Ioannes/John, and Honoria/Nora as additional keys. IrishGenealogy lists Demetrius for Jeremiah, Diarmuid or Darby [S1 @2026-11-16]; compare the full entry before choosing among those English forms.
- **Contracted surnames.** For Prendergast, test Pender too: Matheson’s 1901 synonyms list associates the forms [S2 @2026-11-16]. Compare the entry details before joining the hits [S4 @2026-11-16].
- **Video source.** Only a transcript excerpt was inspected for the video’s first three search suggestions above [S3 @2026-11-16].

**Output:** `index/transcription URL | recorded parish/event/date | followed link |
destination | actual access result | entry located or outstanding`.

**Check:** A displayed transcription and an inspected original are different outputs.

## 3. Narrow pages by event and date, then inspect the entry

The NLI help documents **Filter Events/Dates** with event, year and month. Use the baptism or
marriage date supplied by the lead. These controls highlight corresponding pages; they do not
find or identify the named person within a page. Browse the highlighted sequence for the actual
entry. [P1, P2, O1]

Inspect pages whose dates differ from the main description. NLI explains that page-level filter
metadata can include annotations outside the register's main described dates. [O1]

Compare names, residence, event and date with the register image. Johnson reads Bridget’s surname as Smyth where the index has Smith [P1]. In a Molahiffe entry the index estimated a birth on 24 July 1852, the date the register gives for baptism [P2]. Preserve uncertain letters and enter a baptism date as such.

Treat matching Ancestry and Findmypast entries as one derived lead. Johnson describes a shared transcription and treats RootsIreland as separately transcribed. In the Galway example, the transcription gives the father as Martin Fitzgerald but the image records only Martin’s given name [P4]. A Findmypast speaker said the two vendors indexed the same images together and advised retrying a failed search on the other platform because the indexes differed slightly [P5]. Check any hit against the image.

For faint text, try NLI's documented brightness, contrast or inverse-image controls. Label the
adjusted view; retain the original locator. Route disputed readings to the documentary-records
workflow. [O1]

**Output:** `register | event/year/month filter | page range inspected | exact entry |
raw names/roles | stated residence | baptism/marriage date | separately stated birth date |
transcription discrepancy | unread text`.

**Check:** The filter selects a page range. Completion requires the entry, its date label and
its register context.

## 4. Save the register identity and the exact image locator

Inspect the register's identification information as well as the target page. The citation
demonstration returns to the opening identification image for parish, diocese, event type and
dates. Save that context with the microfilm/item identifier. [P2]

Preserve the exact URL for the page actually inspected and its NLI page number. The demonstration
shows the URL changing when a different page is selected. Numbered NLI page metadata also lists
the microfilm and parish context. Keep any printed register page or entry number in a separate,
nullable field; a viewer page number is not automatically the original pagination. [P2, O2]

When a page download is offered and permitted for the intended use, retain the original image
with its locator. Reopen the saved link when access is available and compare the entry. If that
check cannot run, record it as unperformed rather than claiming the link was tested. [O2]

**Completion packet:** index lead; Catholic parish/diocese; register identity and described
coverage; microfilm/item; selected event/year/month and inspected range; exact page URL and viewer
number; original printed locator if present; raw entry reading; separately labelled event/birth
dates; discrepancy or unread text; and remaining work.

## Prompt pattern

> Recover the NLI parish-register image behind this Irish Catholic index lead. Confirm the
> Catholic parish and event/date coverage; record the microfilm/item and actual link destination.
> Use the event/year/month page selection, then locate and compare the entry. Preserve the exact
> image URL, viewer number, any printed locator and the raw names/roles. Keep baptism and birth
> statements separate. Return the inspected range, uncertainty and next register without inventing
> an image, reading or identity.
