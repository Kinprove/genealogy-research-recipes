---
id: "jewish-archival-list-triage"
title: "Finding Jewish genealogical lists behind archival catalogue titles"
summary: "Select Ukrainian archival cases that hold named Jewish lists, separating title, place and document evidence."
kind: "records"
scope: {"platforms": [], "tasks": ["false-positive keywords, generic titles, civil-registration fund scope or candidate lists that have been presented as verified contents."]}
privacy: "none"
gates: []
guardrails: [{"id": "JEWISH-ARCHIVAL-LIST-TRIAGE-01", "text": "A geographical association does not establish either Jewish contents or the identity of a person. Do not present a title match as a verified Jewish list."}]
handoff: ["archival-image-coverage-verification", "corpus-seeded-name-search"]
checked: "2026-11-07"
checked_basis: "checked 2026-11-07"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Ukrainian archives", "order": 97}
---

# Recipe: Finding Jewish genealogical lists behind archival catalogue titles

Use when selecting Ukrainian archival cases likely to contain named Jewish people:
metrical books, revision lists, resident rolls or civil registers. This is catalogue
triage before document retrieval. For checking the retrieved object's boundaries and
inspected pages, continue with [archival-image-coverage-verification.md](archival-image-coverage-verification.md).

## Contents

- Set the target before filtering
- Use title signals for recall, then inspect their meaning
- Keep geographical selection separate from content verification
- Record what each decision rests on

## Set the target before filtering

Define whether the task needs a list of named people, a personal dossier, aggregate
statistics or any evidence about a community. A statistical return without names
does not satisfy a named-list request; a personal dossier may still be useful for a
different research question. Keep those distinctions instead of treating everything
outside the current target as historically irrelevant.

Keep each candidate keyed by archive, fund, inventory and case, with the literal
title, date range, catalogue locator and discovery method. A fund number alone is
not a case identifier. Repeated catalogue exports are not independent candidates.

## Use title signals for recall, then inspect their meaning

Search relevant Ukrainian and Russian historical record terms, including stems such
as `євре`/`евре` and `синаго`, alongside record-type and locality terms. Pre-1917 file titles
about Jewish communities also use `кагал` (kahal), `коробочн` (the kosher-meat tax,
коробочный сбор), `свечн` (the candle tax, свечной сбор), `посемейн` (family lists), `мещанск`
with `еврейск` in either order (a Jewish townspeople's society; titles have both «еврейского
мещанского» and «мещанского еврейского») and `призывн` (conscription lists, not specific to
Jews, so read each hit in context). These are the Russian forms found in file titles; a
Ukrainian catalogue description may translate them, so test the Ukrainian equivalent as well.
Preserve the exact query and searched catalogue scope. Older spelling or a generic title can hide a
relevant list; a zero title hit does not establish that a fund has no such records.

Rabbinate files need two stems, because Ukrainian and Russian spell the word differently: a Ukrainian
description has «рабинат» where a Russian title has «раввинат». The Odesa regional archive's
guide, for example, heads fond 39 «Одеський міський рабинат» and gives the Russian name «Одесский
городской раввинат» beside it. [B7] Search both `рабин` and `раввин`; `рабин` also matches
surnames such as Рабинович, so read each hit.

Copy the original Ukrainian heading before translating it. A translator may turn a surname or locality into an ordinary word. When an exact phrase fails, search the inflected form or a distinctive stem, then read the full heading. Miller illustrates the difference with nominative `Канівський повіт` and genitive `Канівського повіту` [U567f922da6fa]. Log both queries and the scope you searched.

When site search is unhelpful, try browser Find on the original-language page and record
that page's scope separately from a whole-site or archive-specific search. A shortened
search string is a retrieval probe, not a new historical name form. Use
[corpus-seeded name search](corpus-seeded-name-search.md) for the wider spelling and field
diagnostics; the archive-wiki example does not verify the contents of any retrieved fund.

An isolated `жид` or `ізраїл` token, surname, patronymic or nearby town is a lead to
read in context. It may be part of a personal name or place name. A geographical
association does not establish either Jewish contents or the identity of a person.
Do not present a title match as a verified Jewish list.

Inspect the complete title, fund creator, dates and available description. Open the
finding aid or case images when those fields cannot resolve the question. A generic
peasant or volost heading can be deprioritized in a narrow title sweep; that choice
does not establish the absence of Jewish entries in a broader fund inspection.
Similarly, an administrative title may conceal an attached named schedule.

Search for elections of rabbis, assistant rabbis and prayer-school boards under `выбор`, `раввин` and `молитвен`. A Vilnius archive researcher reports extracting candidates and electors for Druya, including the 1892 prayer-school board elections (LVIA 381-17-1277) [B3]. Use these terms to search Ukrainian inventories. For synagogue membership, check religious-community registration files under the local administration. A forum reader reported seeing only part of the Vinnytsia inventory online [B4]. The regional archive’s inventory of fond R-196, opys 1, describes file 843 for the Kloyz synagogue in Lityn (1925–26) as containing a statute, minutes and lists [B8]. Inspect the lists for their dates, fields and inclusion rules before using a name as evidence of participation, residence or kinship.

## Keep geographical selection separate from content verification

For district or village civil-registration funds, a per-village keyword filter can
miss records selected through their district-level creator. Check the fund's actual
territory, period and record types. If independent locality evidence makes that
territory relevant, retain its in-scope cases as geographical candidates for review.
Do not label the entire fund Jewish, assume all years are relevant, or infer a
person's ethnicity from the administrative boundary.

Search town, uezd and guberniya inventories, including the treasury chamber. Check whether an uezd list includes its principal town before recording a negative. A forum source raises that question for the 1874 Vitebsk guberniya lists of Jewish men [B1]. In another discussion a researcher reports that a file catalogued simply as an undated Gomel uezd revision may contain lists of Jewish men [B2]. Record the title as written and inspect the pages. Also copy the exact registration society from the person’s record. A burgher designation alone establishes neither a separate Jewish society nor residence in the place of registration.

For revision lists from Kremenets district, Volhynia guberniya, use present-day Ternopil Oblast
as a lookup lead [B9 @2026-11-22]. Search for `Кременецького повіту` in the State Archive of
Ternopil Oblast's Kremenets City Magistrate inventory, fond 37, opys 2 [B10 @2026-11-22].
For 1858, also check the two Zhytomyr cases indexed as Jewish revision lists, fond 118,
opys 14, cases 142 and 144 [B11 @2026-11-22]. Keep the historical district in the search and
check the locality and year of each candidate before using it.

Search Jewish-society metrical-book inventories by society, year and event. The Streshin discussion lists separate 1880 marriage and death books under fond 2412, inventory 1, files 88 and 89, and identifies the rabbi of the second district (*stan*) of Rogachev uezd [B2]. Check Streshin alongside Rogachev, Zhlobin and Karpilovka in that district, then verify the locality and person in each entry. An inventory title alone cannot establish either.

For 1941–44, also check occupation-administration creators, such as a district Gebietskommissariat
or a town burgomaster. A [finding-aid excerpt for copied regional fonds](https://forum.j-roots.info/viewtopic.php?f=167&t=4906)
lists case titles under such creators: a census of the Jewish population, residence permits and
refusals, and labour requests. When working from a copy collection, record the original archive,
fund, inventory, case and folio count beside the copy's record-group and accession numbers. These
titles remain catalogue leads. The excerpt does not show named entries or that other regions have
similar copies, and an entry does not establish a person's fate.

If combining keyword and model-assisted title review, use the same frozen input
pool, merge by the full case key, and preserve which method proposed each row.
Agreement between two title classifiers is still title-level evidence. A model's
suggestion of “possible Jewish witnesses” requires inspection of the named source.

## Record what each decision rests on

Use explicit, task-specific states such as:

- **Catalogue lead:** the title or fund context suggests relevance; contents unchecked.
- **Needs source review:** a material ambiguity remains, with the exact page or file needed.
- **Named list verified:** inspected pages contain the requested kind of named entries;
  record those pages and the stated community or record context.
- **Outside this target:** explain the observed reason and whether contents were inspected.
- **Unavailable:** access failed or the necessary description/images were not obtained.

Verification of a named list does not identify every person in it as Jewish. Preserve
the document's own community, religion or administrative labels and any limits on
their applicability. Individual identity and kinship require their own evidence.

Before subtracting material said to be already indexed or uploaded, compare the
specific case, part, years and coverage. An uploaded fund is not proof that every
case or subsection is available. Retain unchecked candidates and reconcile counts
against the declared input pool; do not call a title-only sweep exhaustive.

Deliver the case keys, exact titles, reasons, inspected locators and unresolved
retrieval needs. Stop at the agreed catalogue or case scope; an uninspected reserve
is a possible next source, not a completed search.

This triage rubric is an investigator-created workflow. [Source notes](../sources/jewish-archival-list-triage.md)
separate it from provider facts and related verification methods.
