---
name: genealogy-research-recipes
description: >-
  Investigate genealogy questions with DNA matches and historical records. Use when recovering
  an ancestor’s identity, parentage or place of origin; reconciling conflicting records or DNA
  results; searching archives, record sites or family papers; interpreting genetic comparisons;
  or preparing citations, research logs and proof arguments. Includes platform workflows and
  boundaries for living people, data transfers and contact.
---

# Genealogy research recipes

Distilled, fact-checked **judgment and practical workflows** for genealogy work with DNA and records. Each recipe targets
what an LLM does *not* reliably know, or does *wrong* by default: the named failure modes, the
delegate-vs-never-trust lines, the reasoning sequence a human must own, and the records needed
to resume an investigation. Judgment recipes focus on reasoning; platform playbooks provide
ordered actions and investigator-created schemas with dated platform-documentation checks.

The research methods apply across platforms, including work from exported data. Kinprove
authorship does not require a Kinprove account, connector or scoring engine.

## Version and updates

This copy is version 1.19.0, released 2026-11-14.

Many installations do not update by themselves. If today's date is more than 7 days after
that release date, end your first answer in the conversation with one short note: this copy
of the recipes was released on that date, and a newer version may be available. Give the
update step for the user's installation, or the applicable options if the host is unclear:

- Copies installed from a plugin directory (Anthropic's Claude directory or the ChatGPT/Codex
  plugin directory): updates arrive through that directory.
- Claude Code: `claude plugin update genealogy-research-recipes@kinprove`. For automatic
  updates, run `/plugin`, open **Marketplaces**, select `kinprove` and choose
  **Enable auto-update**.
- Claude.ai or the Claude desktop app: on the Plugins page, select **Check for updates** on
  the `kinprove` marketplace, or turn on **Sync automatically**.
- Hermes Agent: `hermes plugins update genealogy-research-recipes`.
  Catalog reviews can lag GitHub; if no change is reported, use the latest GitHub release's
  full commit SHA in
  `hermes plugins install Kinprove/genealogy-research-recipes --force --ref <full-commit-sha> --no-enable && hermes plugins enable genealogy-research-recipes`.
- OpenClaw: `openclaw plugins update genealogy-research-recipes`.
  ClawHub releases can lag GitHub; if no change is reported, reinstall from the repository:
  `openclaw plugins install git:github.com/Kinprove/genealogy-research-recipes --force`.

Give this note once per conversation, after the answer itself. Skip it when you do not know
today's date. Do not check for a newer version over the network yourself.

## How to use

1. Match the user's requested output to the most specific recipe below. A task recipe
   retrieves records, prepares an artifact or carries out a platform workflow; a judgment
   recipe governs what evidence permits you to infer. If both match, read the task recipe
   in full and the judgment recipe's rules section. If two or more task recipes remain
   plausible, ask one focused scoping question before opening more than one task recipe,
   and wait for the answer before giving that workflow. For example, ask which population
   and place a 1944 deportation concerns, rather than assuming a particular deportation.
   For a record-source question, also ask first when a missing locality, period,
   population or migration destination prevents choosing a concrete source, even if a
   broad recipe fits. While waiting, give the one question and a brief reason for it;
   save the source list and research workflow for the reply. "Came from Russia" alone
   does not establish a modern country, community or destination record system.
   For a place in Central or Eastern Europe, choose by the state that held it on the event
   date and by the family's religion, not by today's border. Start with the
   [Central and Eastern Europe by period state](#central-and-eastern-europe-by-period-state)
   routers. Elsewhere in the Russian Empire, use the
   [Orthodox metrical-book recipe](recipes/russian-orthodox-metrical-book-recovery.md) for
   Orthodox events and the
   [Jewish metrical-book recipe](recipes/russian-empire-jewish-metrical-book-recovery.md)
   for Jewish events outside the Kingdom of Poland. For the Kingdom of Poland, and for any
   Geneteka, Metryki or Szukaj w Archiwach hit, use
   [Polish index recovery](recipes/polish-index-original-record-recovery.md).
   For a general question about proof or research method, give a conditional method
   plan and ask for the context needed to choose actual record collections.
2. **Read the selected task recipe in full before advising** — the value is in the
   specifics, not the summary. If a tool returns only part of the file, continue through
   its remaining sections to the end. For a judgment recipe, read its rules and the
   sections relevant to the question. A router summary or first page does not complete
   the task-recipe read.
   Carry any material source limitation alongside the claim it affects: a search-result extract,
   unread page or unavailable recording is a lead, not a verified reading. Consult the paired
   `https://github.com/Kinprove/genealogy-research-recipes/blob/edc63d0d7ca51c809a77747ff2bf76e45eccd67a/skills/genealogy-research-recipes/sources/` file when the claim's support is unclear; attribute an independently read source
   explicitly rather than treating an inaccessible additional citation as confirmation.
3. Apply its "never trust / never delegate" boundaries as **hard constraints on your own output** —
   those are the exact places a confident answer goes wrong (e.g. fabricating cM→relationship odds,
   reading a WATO ranking as a verdict, ignoring endogamy).
4. If no recipe matches, answer normally — don't force-fit. If a matched recipe is silent
   on the particular question, say what it does not cover and answer normally; do not
   present the uncovered answer as recipe guidance.
5. Before any step that uploads, exports, links, publishes, contacts a person, requests a
   record about a person who may be living, or pastes data into a third-party tool, answer
   the [privacy gate](#privacy-gate). Recipes mark such steps with a **Privacy gate**
   checkpoint; the gate applies to unmarked steps of the same kinds too. For a living person,
   also follow [Living people](#living-people).

## Read source limits

A source marker identifies evidence, not a guarantee that the page was read or that it supports
every sentence. Most cited passages lack a recorded review against their sources, and a marker or
a date alone does not show that one was reviewed. When relying on a factual passage, read the
entry for each cited source ID in its `https://github.com/Kinprove/genealogy-research-recipes/blob/edc63d0d7ca51c809a77747ff2bf76e45eccd67a/skills/genealogy-research-recipes/sources/<recipe-id>.md` sidecar and carry the limitations
that entry states.

`[S12 @2026-11-07]` gives the claim's last check date. A dagger such as `[S16†]` marks limited or
unavailable access: preserve the attributed observation and qualification rather than restating
it as a verified fact. A passage without a recorded review can cite a limited-access source
without a dagger, so take access limits from the sidecar entry, not from a missing dagger. A
partial read supports only its recorded scope. A fresh date or a `read` status does not establish
that a genealogical inference is correct.

## Privacy gate

Answer these items in writing, in your reply, before the step runs. If any answer is
unknown, do not move the data: keep it local and tell the user what is missing.

- **People.** Name everyone whose data is involved. Treat anyone who may be living as
  living. A minor's data needs a parent's or guardian's permission.
- **Data.** Name the exact fields, files, segments, photos or records. Say explicitly when
  they show health status, a tentative relationship, unexpected parentage or another
  sensitive finding.
- **Destination.** Name the service, tool, person or place the data goes to.
- **Audience.** Say who can see it there, now and after later setting changes.
- **Controls.** Inspect the destination's visibility, searchability, matching and export
  settings and any extension's permissions, and record what you saw and the date. For a DNA
  database, include whether law-enforcement uploads can match the kit.
- **Permission.** Get explicit permission from each living person whose data leaves the user's
  own device or account, or becomes visible to others there (a tree link, a searchable or
  shared setting), for this action and this destination; an extension or a tool that
  receives the data counts as a destination. Kit or account access, or permission to analyze,
  is not permission to move or disclose. A file that stays on the user's own device needs no
  further permission, but the Retention item applies to it. A private first message that asks
  a person for permission needs the tester's (or user's) authorization, not that person's
  prior permission; it may show that person only their own data and the question, never
  other people's sensitive findings.
- **Redaction.** Say what you remove or replace before the data moves.
- **Retention.** Keep exported match lists, segment files and record copies on the user's
  own device, not in shared folders or other services. Delete them when the research
  question is answered, unless the tester (for records, the user) asks to keep them.
- **Jurisdiction.** Ask where the user, the tester and each named person live, and which
  rules apply there. Data-protection law can apply: genetic data is "sensitive" data under
  the EU GDPR ([European Commission](https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en))
  and [UK GDPR Article 9](https://www.legislation.gov.uk/eur/2016/679/article/9); both laws
  exclude purely personal or household activity, which sharing or publishing can leave (see
  [family interviews](recipes/family-interviews-and-oral-tradition.md)); U.S. state laws such
  as California's Genetic Information Privacy Act give rights over genetic data a testing
  company holds ([California Attorney General](https://oag.ca.gov/news/press-releases/attorney-general-bonta-urgently-issues-consumer-alert-23andme-customers));
  Russia's personal-data law is [152-FZ](https://www.consultant.ru/document/cons_doc_LAW_61801/).
  Record requests have their own access rules, such as Japan's koseki rule
  ([koseki recipe](recipes/japanese-koseki-honseki-recovery.md#4-check-eligibility-before-requesting))
  and the 75-year rule for Russian archives
  ([Soviet personal files](recipes/soviet-personal-file-recovery.md#5-log-each-catalogue-hit-as-a-candidate-with-its-own-locator)). The destination's
  terms apply too. Do not state a legal conclusion: ask the user to confirm the rule that
  applies, or keep the data local.

For DNA data, also apply the consent and redaction rules in
[AI for DNA research](recipes/ai-for-dna-research.md#verification--privacy-discipline).

### Living people

Stay on the family-history question and the materials the user supplied. Do not look up a
living person's current address, phone number, email, workplace, online accounts,
movements or finances, and do not trace minors on the web. Do not use people-search or
contact-aggregator services. Never use leaked or breached data, another person's account or
session, or a false pretext. When the question itself concerns a living person (unknown
parentage, a planned contact), identify them only as far as the question needs and keep the
data to the minimum.

Contact a living person only through a route the person or the tester already has, the
testing site's own messaging, or a relative who agrees to pass the message on. The identity
that must be easy to check is the sender's. Stage a contact about DNA (a DNA match, a kit
manager, or a relative asked to test or approached about a DNA or parentage question) through
[DNA match outreach staging](recipes/dna-match-outreach-staging.md). For any other contact,
such as a cousin asked for a photograph, a record submitter or a donor, apply that recipe's
consent and disclosure rules and its log, and skip what applies only to DNA tests (a tester's
agreement, kit pair, site, shared cM).

### Record requests

When a record may be about a living person, request only what the family question needs.
Never request a record to find a living person or to learn about their present life. Name
the record's own access rule (closure period, who is entitled, the subject's consent) and
follow it. An office's rule on who may order a record is not the subject's permission: the
Permission item still applies to each living person the request names. Until every item is
answered, the request stays an unsent draft on the user's device. Send only the identity and
kinship proof the custodian asks for. The Retention item and the next rule apply to what arrives.

### Third persons in sensitive files

Informers, witnesses, interrogators and co-accused named in repression, interrogation,
police or compensation files are not republished, and are not named in a report or tree
shared with others. Refer to them by role, for example "a witness".

<!-- recipe-catalog:start -->
## Recipes

Generated from the recipe headers. Full entries list the tasks they serve and quote the
recipe's core guardrail. The short topic pointers are discovery links; they list tasks only
where the header names some beyond the summary. Both tiers require reading the recipe before
advising. A dated source check is a maintenance reminder, not verification of every claim or
live control.

- **`recipes/jewish-archival-list-triage.md`** — Finding Jewish genealogical lists behind archival catalogue titles.
  Select Ukrainian archival cases for named Jewish lists while separating title, geographical and
  document evidence.
  *Use for:* false-positive keywords, generic titles, civil-registration fund scope or candidate
  lists that have been presented as verified contents.
  *Core guardrail:* A geographical association does not establish either Jewish contents or the
  identity of a person. Do not present a title match as a verified Jewish list.

- **`recipes/elib-ukrainian-archive-reference-books.md`** — Recovering and identifying Ukrainian archival guides in ELIB.
  Retrieve Ukrainian archival guides from ELIB and identify the correct volume, part and fund scope.
  *Use for:* catalogue-card versus PDF confusion, leading-zero item IDs, keyword misses, similar
  volume titles or garbled cover-text extraction.
  *Core guardrail:* Prefer the current card's link over a constructed URL. A constructed route is a
  retrieval lead until its response is verified as the intended PDF; redirects, error HTML or an
  access failure leave acquisition unresolved.
  *Dated source check:* 2026-11-12.

- **`recipes/dna-comparison-controls.md`** — DNA comparison controls across services.
  Reconcile conflicting vendor or native results using exact tests, query controls, local marker
  coverage and reporting scope.
  *Use for:* an absent match, raw-file X coverage, PAR/build ambiguity or doubled totals.
  *Core guardrail:* If the expected positive is missing, investigate the query, selection and
  processing before interpreting an empty list.

- **`recipes/archival-image-coverage-verification.md`** — Verifying archival images, case boundaries and search coverage.
  Verify case boundaries, image order, transcript version and the pages and targets actually
  inspected.
  *Use for:* catalogue/cover disagreements, conflicting readings or completeness claims.
  *Core guardrail:* A completed reader session establishes execution coverage, not transcription
  accuracy. A new surname was not searched merely because its pages occurred in an earlier sweep for
  other names.

- **`recipes/corpus-seeded-name-search.md`** — Corpus-seeded name searches across scripts and OCR.
  Recover attested spellings across scripts and OCR by separating encoding, orthography and field
  behaviour.
  *Use for:* Hebrew/Yiddish name misses, lossy search folds or uncalibrated zero results.
  *Core guardrail:* A completed zero-hit query describes that query and scope; it does not exclude a
  person whose record or spelling has not been tested.

- **`recipes/holocaust-testimony-source-interpretation.md`** — Interpret a Holocaust name record through its underlying source.
  Interpret a Yad Vashem result through its testimony, wartime list or survivor source and statement
  dates.
  *Use for:* unspecified death circumstances, submitter roles or evacuation conflicts.
  *Core guardrail:* Recover the information behind a Yad Vashem name result without converting a
  memorial submission, archival list or evacuation entry into an unsupported death or family
  conclusion.

- **`recipes/russian-military-repression-record-episodes.md`** — Recover separate military and Soviet-repression record episodes.
  Reconcile WWI/WWII and Soviet-repression records as separate dated source episodes.
  *Use for:* awards versus loss reports, repeated arrests or copied regional entries, GWAR and OBD
  Memorial queries, Russian-front WWI prisoners of war, WWII Soviet prisoners of war and occupation
  victims.
  *Core guardrail:* an award order after a missing report does not, by itself, establish survival
  between those dates. Obtain an event-specific source before extending a life or death interval.

- **`recipes/genealogy-standards-audit.md`** — Auditing a genealogy research package against professional standards.
  Audit a dossier, report, proof draft or documented tree by tracing each claim through examined
  sources and explained reasoning.
  *Use for:* citation gaps, search coverage, negative-evidence claims, GPS review, dependent
  conclusions, or choosing a research report, proof statement, summary or argument.
  *Core guardrail:* A populated log, polished footnote or completed checklist does not establish the
  Genealogical Proof Standard (GPS). The researcher owns the final ruling on evidentiary
  sufficiency.

- **`recipes/jewish-genealogy-conditional-hypotheses.md`** — Jewish genealogy: conditional naming, town and DNA clues.
  Apply working hypotheses to Jewish naming, locality and DNA clues while keeping each proposition
  separate.
  *Use for:* proposed parentage, name equivalence, namesakes, naming customs, ancestral towns,
  conditional branches or segment attribution through an endogamous pedigree.
  *Core guardrail:* A proposed father can select a search town; establishing that father still does
  not establish the child's birthplace, the intended namesake or the ancestor behind every shared
  segment.

- **`recipes/burial-evidence-packet.md`** — Build a burial evidence packet from cemetery records.
  Recover a cemetery entry, its photograph or inscription, and the plot and cemetery-record locators
  needed to inspect the burial.
  *Use for:* cemetery coverage, surname variants, Hebrew and civil inscriptions, death/burial
  discrepancies or a database hit that needs a cemetery-record follow-up; names on a Soviet
  mass-grave plate
  *Core guardrail:* Keep death, burial, inscription and database statements distinguishable. The
  result is a packet another researcher can inspect, with missing fields and unresolved
  discrepancies visible.

- **`recipes/city-directory-observation-workflow.md`** — Build a checked city-directory observation series.
  Build a comparable series of city-directory names, addresses and occupations from checked editions
  and sections.
  *Use for:* a known address with unknown names, surrounding locality sections, abbreviation keys,
  index errors, address/occupation changes or a person missing from one directory edition.
  *Core guardrail:* A gap in a database's editions and an absent entry on inspected pages are
  different results. Neither alone establishes why the person is missing.

- **`recipes/land-index-book-series-recovery.md`** — Recover land instruments through indexes, book series and entry files.
  Follow a land-record lead through both relevant index directions to the correct instrument and
  record-book series, or carry a federal patent lead into its separate entry file.
  *Use for:* grantor/grantee indexes, ambiguous book locators, separate book series, delayed
  recording, a surname search that missed the alternative index entry, Swedish property-book
  room/successor references and changed parcel designations, Bavarian property-protocol creators and
  tax-book identifier/volume handoffs, or cash-sale, bounty-land and homestead supporting packets.
  *Core guardrail:* Keep both index directions, the instrument and recording dates, and the original
  locator visible, so one missed surname entry or guessed book does not become a false absence.

- **`recipes/probate-case-document-inventory.md`** — Inventory the documents of a probate case.
  Recover the documents behind a probate index, will or administrator's bond as a case inventory
  with unresolved leads.
  *Use for:* probate record series, references to other documents, later actions, non-will
  proceedings, Swedish court-copy versus heirs-original and poverty-certificate checks, reverse
  searches from a guardian to wards, or an estate search that stopped at the first useful document.
  *Core guardrail:* Keep a case inventory and a queue of unresolved references, so finding one
  useful document does not silently finish the estate search.

- **`recipes/us-military-pension-file-recovery.md`** — Recover and inventory a U.S. military pension file.
  Carry a service clue or pension index card to the appropriate application file and inventory the
  claim's documents.
  *Use for:* pension-card identifiers, record custodians, complete versus abbreviated copy products,
  widow/dependent applications, household and means statements, objections or later claim decisions.
  *Core guardrail:* Preserve the distinction between an index, a service record, a pension file and
  an abbreviated copy product.

- **`recipes/irish-catholic-parish-image-recovery.md`** — Recover an Irish Catholic parish entry at the NLI.
  Carry an Irish Catholic baptism or marriage lead into the NLI parish-register images and locate
  the actual entry.
  *Use for:* RootsIreland/Findmypast transcriptions, Catholic parish/register selection, a link
  opening the register's first page, date browsing or exact image citations.
  *Core guardrail:* Carry an Irish Catholic baptism or marriage lead into the National Library of
  Ireland's register images, inspect the actual entry and preserve the register and image locators.
  A transcription can identify a parish and date without supplying an image; a baptism date remains
  a baptism date unless the original separately records birth.

- **`recipes/polish-index-original-record-recovery.md`** — Recover a Polish original from an index or archival description.
  Recover an original Polish register entry from Geneteka, Metryki or Szukaj w Archiwach, or
  document the retrieval gap.
  *Use for:* SKAN links, locality/confession/year/act locators, PRADZIAD descriptions, archival
  fonds and units, missing scans or alternative holding routes.
  *Core guardrail:* A register description establishes a lead to holdings, not that the target entry
  has been inspected. Preserve the complete reference, not just a short number detached from its
  archive and fonds.

- **`recipes/rootsmagic-tree-reconciliation-workflow.md`** — RootsMagic: Reconcile a Local Tree with Ancestry and FamilySearch.
  Reconcile selected facts and sources between RootsMagic, Ancestry TreeShare and FamilySearch.
  *Use for:* person crosswalks, staged additions/replacements, citation and media transfer,
  duplicate sources, destination checks or resuming a bounded synchronization batch.
  *Core guardrail:* Choose the destination and operation for each object, then inspect the saved
  result.
  *Dated source check:* 2026-11-12.

- **`recipes/wikitree-dna-tester-links.md`** — WikiTree: Link DNA Tests to the Correct Tester and External Kit.
  Register a DNA test on the actual tester's WikiTree profile and verify its FamilyTreeDNA or
  GEDmatch link destination.
  *Use for:* tester/kit crosswalks, external tree links, visibility settings, propagated DNA
  Connections or pedigree leads needing documentary follow-up.
  *Core guardrail:* Do not mark a relationship DNA-confirmed solely because a tester appears in a
  list or because the external tree link works.
  *Dated source check:* 2026-11-12.

- **`recipes/usa-immigration-search-recovery.md`** — Recover U.S. immigration and naturalization records.
  Twelve historical U.S. immigration workflows: reconstruct journeys, test port, airport and border
  coverage, recover name variants, pair departures with arrivals, read complete manifests,
  distinguish detention outcomes, interpret dated verification marks, find naturalizations across
  courts, check historical citizenship rules, locate federal files and recover broken image links.
  *Use for:* ship and aircraft passenger lists, Canada/Mexico crossing records, naturalization
  minute books, C-files, A-files and AR-2 records.
  *Core guardrail:* The recurring mistake is treating a search miss as a missing ancestor when the
  failure lies in the selected port, date, recorded name, image, citizenship history or custodian.

- **`recipes/familysearch-practical-record-workflows.md`** — FamilySearch record recovery and Tree maintenance.
  Nineteen FamilySearch operations: recover Catalog/DGS holdings and image-only records, preserve
  view-scoped citations, refine Full Text/Simple Search, recover page references hidden in an
  assertion’s reason, clean up Source Linker attachments and same-name Tree repairs, share research
  reports with checked visibility and reader access, recover a missing Memory from an independent
  copy and record a supported relationship without inventing a parent.
  *Use for:* FamilySearch howtos, Catalog/film/DGS crosswalks, unindexed images, Full Text or Simple
  Search, Source Linker cleanup, profile repair and Source Box reuse.
  *Core guardrail:* Confirm candidates from the image and context. A name appearing in text does not
  establish the candidate's identity.
  *Dated source check:* 2026-11-12.

- **`recipes/russian-empire-emigrant-origin-recovery.md`** — Recovering a Russian Empire emigrant's origin locality.
  Five workflows for tracing an emigrant from destination records to an exact historical locality:
  reconcile arrival clues, recover failed name searches, extract complete manifests, follow
  contact/travel networks, and prepare a locality and archive handoff. Principally 1880–1924 U.S.
  arrivals, including Canadian transit, across confessions.
  *Use for:* conflicting arrival years, changing names, missing manifest pages, two contact fields,
  separate family arrivals, residence/birthplace ambiguity or an unresolved origin town.
  *Core guardrail:* Preserve the wording and field role until the movement and locality evidence
  resolve them.

- **`recipes/us-census-practical-workflows.md`** — Practical U.S. census workflows.
  Ten practical U.S. census procedures: recover households, browse target-year districts, follow
  1950 revisit sheets, compare pre-1850 age bins, bridge the 1890 gap, extract supplements and
  family fields, search mortality schedules, follow surname changes, and follow a farm lead into an
  agricultural schedule.
  *Use for:* a missing census household, an address without a name hit, sheet 71, tick-mark counts,
  substitute censuses, sample lines, marriage/children fields, competing child rosters, mortality
  reporting windows, or formerly enslaved families under different surnames.
  *Core guardrail:* Preserve the original census locator and keep literal observations separate from
  calculations and proposed identities.

- **`recipes/geni-practical-research-workflows.md`** — Practical Geni research workflows.
  Eight practical Geni workflows: recover name variants, preserve relationship focus, cite facts,
  choose projects, compare merge candidates, track tree conflicts, create GEDCOM branches and
  inspect scoped exports.
  *Use for:* Geni language/alias fields, relationship paths, source documents, public projects or
  private workspaces, merge requests, unmerge requests, GEDCOM imports and tree reports.
  *Core guardrail:* Distinguish tree assertions, source-supported statements, pending requests and
  completed changes. Draft any manager or curator request for my review; do not send it.
  *Dated source check:* 2026-11-12.

- **`recipes/ancestry-dna-match-investigation.md`** — AncestryDNA: eight practical ways to investigate matches.
  Eight practical AncestryDNA workflows: use a target's closest relatives, build branch anchor
  tables, search collateral names, organize groups and notes, correct tester links, audit labels and
  recover missing match rows.
  *Use for:* AncestryDNA match investigation, Pro Tools Enhanced Shared Matches, colored dots,
  linked trees, ThruLines, access-dependent gaps or connecting a match to another testing site.
  *Core guardrail:* Keep three columns: observed cM, dated label with its origin, and sourced
  pedigree path.
  *Dated source check:* 2026-11-12.

- **`recipes/myheritage-dna-match-investigation.md`** — MyHeritage DNA match investigation playbook.
  Nine practical MyHeritage DNA workflows: select the right kit, preserve theories before
  reassignment, build filtered shortlists, use labels and notes, capture pair-specific shared-match
  values, compare triangulation subsets, audit theory connections, recover private-tree leads,
  contact matches and resume dated packets.
  *Use for:* MyHeritage DNA match investigation, kit relinking, largest-segment sorting,
  labels/favorites, Shared DNA Matches, Theory of Family Relativity or an investigation follow-up.
  *Core guardrail:* Save empty results with their actual query, kit, filters and date. Do not fill
  an unshown DNA measurement with zero or infer that a person outside the list has no shared DNA.
  *Dated source check:* 2026-11-12.

- **`recipes/unknown-parentage-wato.md`** — Work an unknown-parentage case with DNA matches and WATO.
  Placing an unknown person (an unknown parent, an adoptee's bio-parent, an unplaced ancestor) into
  a tree using DNA matches + WATO odds.
  *Use for:* "who is my unknown grandfather/father", adoptee bio-family search, WATO hypothesis
  scoring, clustering matches to an ancestral couple, tied hypotheses, choosing a discriminating
  tester, or deciding which observations to withhold from a calculation.
  *Core guardrail:* WATO assumes single-path descent. Pedigree collapse / endogamy / a match related
  through two lines silently invalidates the score — the tool has no way to know and will still rank
  confidently.

- **`recipes/ai-for-dna-research.md`** — Using AI reliably in DNA genealogy research.
  Using an AI assistant *reliably* on DNA/genealogy work: what to delegate freely, what to never
  trust, and the prompt patterns that work. Includes endogamous match prioritization, segment
  attribution, targeted testing of outmarrying branches, and coherent family comparisons across
  tested ancestors, siblings and descendants. *Also use for:* "how are these two families
  connected", multiple related focal testers, repeated descent paths, a long segment in a relative
  that is shorter/absent in a descendant, mixed-origin segment overhangs, fused clusters, validating
  a match's own pedigree, or inspecting supplied ethnicity-region maps and AncestryDNA Journeys
  timelines for locality-search leads.
  *Use for:* any "can AI/ChatGPT/Claude help me with my DNA / tree / citations", **or** whenever you
  (the assistant) are about to compute or assert something in this domain.
  *Core guardrail:* Never ask the LLM to compute relationship probabilities from a cM number — it
  *fabricates* them. Route a *single* cM figure to the **Shared cM Project / DNA Painter's Shared cM
  Tool** (point cM → the *range* of candidate relationships); if you have a tree plus multiple
  matches to place, that's **WATO** — a *different* DNA Painter tool that scores hypothesis slots,
  not a cM→relationship lookup.

- **`recipes/ydna-mtdna-interpretation.md`** — Interpreting Y-DNA and mtDNA — what a haplogroup or STR/sequence match can (and can't) establish.
  Interpreting Y-DNA and mtDNA results (a haplogroup assignment, a Y-STR genetic-distance match, an
  mtDNA sequence match): what each can actually establish about a *genealogical-timeframe*
  relationship, and where confident interpretation crosses into fabrication. The Y-STR/mtDNA
  complement to `ai-for-dna-research.md` (autosomal cM).
  *Use for:* "what does my haplogroup / Y-STR match / mtDNA match mean", "how many generations back
  is genetic distance N", "does this haplogroup contradiction prove a non-paternity event",
  differing Y labels, measured versus inferred SNP results, choosing a tester to split an unresolved
  SNP block, TMRCA disagreement with a dated pedigree, or a pair matching on both autosomal DNA and
  Y-DNA/mtDNA through potentially different ancestral lines.
  *Core guardrail:* **you do not compute or assign haplogroups, TMRCAs, or NPE verdicts from your
  own reasoning.** Every such value is a *hypothesis to route to the right tool or corroborate* —
  never a fact to state.

- **`recipes/xdna-phasing-judgment.md`** — X-DNA and Visual/Parental Phasing — where confident-sounding analysis silently goes wrong.
  X-DNA matches and visual/parental phasing: what a segment, an X match, or a phased chromosome map
  can actually confirm or eliminate, and where confident-sounding analysis is actually fabrication.
  *Use for:* "is this X-DNA match trustworthy", "what's the minimum X cM threshold", "phase my kit
  against a parent or siblings", "half-sister or aunt", "does this X match rule out a father",
  reconstructed-kit quality, artificial homozygosity, or interpreting matches to a synthetic kit.
  *Core guardrail:* **Ban invented small-segment statistics.** Any false-positive-rate or
  chance-match number must be attributed to a specific company/study (23andMe 2014, AncestryDNA
  2020, FTDNA's Family Finder Matching 5.0) — never a smoothed or averaged figure presented as a
  universal law.

- **`recipes/ai-for-documentary-records.md`** — Using AI reliably in documentary & records genealogy research.
  Using an AI assistant *reliably* on DOCUMENTARY / records work (NOT DNA): handwriting
  transcription & translation, AI full-text / OCR finding aids (FamilySearch Full-Text Search),
  reviewing & correcting AI-indexed records, evaluating AI record hints, and image restoration /
  colorization / generation & evidentiary trust.
  *Use for:* any "can AI/ChatGPT/Gemini transcribe or translate this handwriting", "full-text search
  for unindexed deeds/probate", "correct AI-indexed records", "evaluate an AI record hint",
  "colorize/restore an old photo".
  *Core guardrail:* **Every AI output is a hypothesis to verify against the original record, never a
  fact to file.**

- **`recipes/evidence-proof-judgment.md`** — Correlating evidence & proving identity — the judgment AI gets wrong.
  Correlating evidence & proving identity: the judgment an AI gets WRONG when it recites the
  Genealogical Proof Standard but misapplies it — same-name conflation, conflict- flattening,
  over-reading a document, negative-evidence errors, DNA/documentary siloing, de-novo fabrication,
  and sycophancy toward the answer you want. Includes a premise and dependency register for
  investigating a tentative branch without silently inheriting its assumptions.
  *Use for:* separating same-named people, resolving conflicting records, weighing indirect vs
  negative evidence, combining DNA with documents into ONE proof, conditional placements,
  discriminating hypothesis tests or revising dependent claims — **and** whenever you (the
  assistant) are about to state a genealogical conclusion.
  *Core guardrail:* **You rule on identity and proof. The model assembles and drafts — it never
  concludes.**

- **`recipes/russian-empire-jewish-identity-attribution.md`** — Name mismatch in a Russian-Empire Jewish family — which branch, and what DNA can still say.
  A Russian-Empire Jewish ancestor who turns up under a given name, patronymic or surname that fits
  neither candidate branch: the inverse of same-name collapse (one person, several names), read
  through the imperial record system — revision lists (ревизские сказки), family lists (посемейные
  списки), metrical books and recruit files as ledgers of *registration* (приписка), not vital
  records — with the naming and re-registration mechanisms (double names, head-of-household
  patronymics, heir naming, stepchild, fostered orphan, levy evasion, son-in-law surname, surname
  split, conversion) carried as competing hypotheses, and the "prediction must differ" test before
  any DNA is asked to choose between branches of one endogamous family.
  *Use for:* "which brother was his father", a boy registered in a relative's household, a wife's
  child from a first marriage, a family hiding a son from the recruit levy / cantonists, brothers
  under different surnames, a patronymic that is the grandfather's or the husband's name, a person
  missing from a revision list, or DNA that "can't tell the two branches apart" under Ashkenazi
  endogamy plus repeated pedigree collapse.
  *Core guardrail:* **A name mismatch never changes the branch verdict on its own; the household
  chain does.** Chain the person through household number → previous household number → age at
  previous revision → "выбыло" column → additional lists before you interpret any name.

- **`recipes/jewishgen-search-family-reconstruction.md`** — JewishGen searches that recover families missed by a name-and-town query.
  Retrieving JewishGen family records when names, ages, towns or a woman's surname are uncertain.
  Build explicit name-variant and mixed-field search batches, distinguish registration from
  residence, and look for wives' natal families or married daughters through children's records and
  household comparisons.
  *Use for:* JewishGen exact, partial, phonetic or fuzzy searches; double names and patronymics;
  conflicting ages or delayed registration; a missing marriage record, unknown maiden name or
  daughter who disappears under a married surname; counting result rows as distinct entries, keying
  households on the original record, and telling an overflow, an error or an uncovered database from
  a completed search with no hits.
  *Core guardrail:* Do not convert a phonetic, household or age match into a relationship.
  *Dated source check:* 2026-11-12.

- **`recipes/beider-given-name-variants.md`** — Ashkenazi given-name variants from Beider's indexes.
  Expanding documentary searches with recorded Ashkenazi given-name forms from the male and female
  J-Roots Beider indexes.
  *Use for:* an unfamiliar or approximate Cyrillic given name, compound names, alternate spellings,
  ambiguous article labels, or documenting a DNA match's family under another name form.
  *Core guardrail:* Two forms in one dictionary article create search candidates; they do not
  establish that two records describe the same person.

- **`recipes/myheritage-historical-record-search.md`** — Recovering historical records with MyHeritage.
  Recovering MyHeritage historical records hidden by collection coverage, query fields, name
  variants, languages or OCR.
  *Use for:* no-result searches, Collection Catalog, relative pivots, historical jurisdictions,
  newspaper keywords/OldNews or an index that must lead onward to an original record.
  *Core guardrail:* Preserve the sparse baseline before tightening it. If a tighter query fails,
  relax one condition at a time and record the reason; changing everything together conceals what
  excluded the record.
  *Dated source check:* 2026-11-12.

- **`recipes/newspapers-com-search-recovery.md`** — Newspapers.com: Recover Notices That Name Searches Miss.
  Recovering newspaper notices when issue coverage, printed names or OCR hide an ancestor on
  Newspapers.com. Build a title–holding–issue register first, resolve another holding when coverage
  is insufficient, then search initials, married names, associates, occupations and addresses and
  verify the original notice.
  *Use for:* a failed newspaper name search, an unknown maiden name, a missing obituary, immigration
  or family-reconstruction leads, title changes, incomplete issue coverage, alternate holdings or
  unreadable OCR.
  *Core guardrail:* A surname can occur in one item and a travel verb in another on the same page.
  Confirm the subject and event within the actual item before assigning that event to the searched
  person.
  *Dated source check:* 2026-11-12.

- **`recipes/hebrewbooks-search-recovery.md`** — Recovering HebrewBooks search misses.
  Recover HebrewBooks names or passages missed by OCR, catalogue spelling or a query that never
  reached search.
  *Use for:* Hebrew OCR letter confusions, catalogue versus full-text searches, short mobile
  queries, inaccessible routes, Shafeh title searches, given-name indexes and viewer versus printed
  page numbers.
  *Core guardrail:* An access error, an unsubmitted query and a completed search with zero hits are
  different observations. Record the surface and the observation before interpreting it.
  *Dated source check:* 2026-11-12.

- **`recipes/ancestry-record-search-recovery.md`** — Ancestry record-search recovery.
  Recovering archival records missed by an Ancestry search. Diagnose scope and coverage before
  relaxing dates, places or names; use collection descriptions, original book indexes, census
  districts and the holding archive.
  *Use for:* an attached census disappearing from results, narrow Card Catalog matches,
  birthplace/residence confusion, conservative wildcard batches, name-free searches, book page
  versus image numbers, enumeration-district browsing, or index-only records.
  *Core guardrail:* Keep three observations separate: no indexed candidate; no matching images in
  the available inventory; and documented absence in the original surviving records.
  *Dated source check:* 2026-11-12.

- **`recipes/23andme-match-research.md`** — Working with 23andMe DNA: matches, matrices, segments, and preservation.
  Twelve practical workflows for 23andMe match research, permitted comparisons, numerical matrices
  and dated preservation.
  *Use for:* match worksheets, connection permissions, selected-segment painting, parent-side
  information, ancestry confidence/history, legacy bucketing, reconstructed ancestors, extension
  exports/groups, manual shared-match charts, or floating research-tree branches.
  *Core guardrail:* The expensive mistake is assuming that every visible DNA Relative can be
  compared in every position, every percentage is autosomal-only, and every Download button returns
  the same kind of evidence.
  *Dated source check:* 2026-11-12.

- **`recipes/ftdna-practical-dna-workflows.md`** — Maintaining FamilyTreeDNA exports and tree links.
  Eight FTDNA workflows for Matrix observations, paired match/segment exports, duplicate-name joins,
  MyHeritage tree links, Family Matching and public Y-DNA Group Time Tree, supplied Globetrekker map
  or two-label comparison packets.
  *Use for:* Family Finder CSV scope, opaque note handles, selected-match segment files, transferred
  links that need confirmation, dated parental-bucket inventories, subgroup selections, branch
  estimates, obscured map nodes, hidden details or authorized project-display checks.
  *Core guardrail:* A match name is a join key, not a unique person identifier. Matching Bucket and
  Linked Relationship are values observed at download. Record link changes separately from the
  retrieval date, keep the export choice and kit with the rows, and refresh match metadata after
  relinking.
  *Dated source check:* 2026-11-12.

- **`recipes/dnapainter-practical-dna-workflows.md`** — Practical DNA Painter maps, matrices and tree worklists.
  Ten practical DNA Painter workflows: paint measured matches, copy or merge maps of one tester,
  intersect phased inheritance, calculate provisional missing intervals, combine coordinate spans,
  plan descendant tests, annotate cluster-derived maps, build direct-ancestor gap worklists, audit
  numeric pair amounts, and inspect Shared cM histograms and two-value range screens.
  *Use for:* Paint a new match, map duplication/CSV transfers, Common Segment Generator, Inferred
  Segments Generator, Distinct Segment Generator, Coverage Estimator, Cluster Auto Painter
  annotations, ancestral-tree reports, sourced numeric pair matrices, or Shared cM histograms and
  two-value range screens.
  *Core guardrail:* A copied segment belongs to its original comparison; an intersection is
  coordinate geometry; an inferred interval is a deduction; the Coverage Estimator is a
  pedigree-based estimate. Keep those outputs distinguishable.
  *Dated source check:* 2026-11-12.

- **`recipes/gedmatch-practical-dna-workflows.md`** — Working reproducibly with GEDmatch.
  Eight GEDmatch workflows: establish kit/run baselines, follow shortlist entries into direct
  comparisons, check three-kit cores, bound locus searches, freeze tag/MKA groups, preserve
  triangulation, and record parental-phasing or Lazarus input groups and generated-kit roles.
  *Use for:* GEDmatch One-to-Many, One-to-One, match-both, Segment Search, tag groups, Multiple Kit
  Analysis, Triangulation, parental phasing or Lazarus reconstruction.
  *Core guardrail:* A match-list row, a pairwise segment, a shared-match list, a triangulation
  result and a generated kit answer different questions. Keep their tool, inputs and settings
  attached to every result.
  *Dated source check:* 2026-11-12.

- **`recipes/source-citation.md`** — Source citation record.
  Preserve a retrievable source record and connect each citation to the evidence it supports.
  *Use for:* source citations, repository and item locators, layered citations, shortened references
  *Core guardrail:* An index entry and an inspected original image have different retrieval paths;
  record which one you used.

- **`recipes/research-documentation.md`** — Research log and report.
  Preserve searches, results, document numbers and analysis so an investigation can resume.
  *Use for:* research logs, research reports, NIL searches, coverage and linked next actions
  *Core guardrail:* Use `NIL` for a completed search with no hits. Record inaccessible images,
  interrupted searches and unsearched collections with their actual status.

- **`recipes/rabbinic-literature-person-search.md`** — Search rabbinic and Hasidic literature for a person or a lineage.
  Find and interpret passages about a Jewish ancestor, rabbinic office or claimed lineage in
  rabbinic and Hasidic books.
  *Use for:* rebbe descent traditions, rabbis of a town, responsa, approbations and Hasidic tales
  *Core guardrail:* Keep two questions apart: did the ancestor exist, and is the bridge from your
  person to that ancestor documented? Rabbinic books often answer the first and rarely prove the
  second.

- **`recipes/agent-research-project.md`** — Running a long genealogy project with an AI agent.
  Keep an AI agent's genealogy work honest over months: what counts as evidence, how to lay out
  Markdown research notes, what 'searched', 'saved' and 'done' must mean, how corrections reach
  every note, and how to delegate and write to a tree safely.
  *Use for:* running a multi-session genealogy investigation with an AI agent; keeping genealogy
  research notes in Markdown or Obsidian; delegating genealogy reading to sub-agents; carrying a
  correction through notes and a tree; research vault; Obsidian genealogy notes; the agent says
  saved or done; sub-agent genealogy research; long genealogy project; keep research across
  sessions; correct a claim everywhere; fill empty surname fields in a tree
  *Core guardrail:* Treat a model-written summary, tag or "key insight" as a pointer. Open the
  source before writing a claim.

## More recipes by topic

### Central and Eastern Europe by period state

- **`recipes/galicia-bukovina-habsburg-record-routing.md`** — Route a Galician or Bukovinian record by date, confession and custodian.
  Route a Galician or Bukovinian event by date, confession and custodian, and decide the army before
  searching WWI records.

- **`recipes/bessarabia-moldova-record-routing.md`** — Route a Bessarabian or Moldovan record by date, district and bank of the Dniester.
  Route a Bessarabian, Moldovan or left-bank Dniester event by its date, district and present
  custodian, then search ANA fond 211 by opis.
  *Use for:* Search Bessarabian and Chișinău notarial acts in the ANA notarial fonds by office,
  notary and year.; Search Bessarabian and Moldovan newspapers in the Arcanum database and read each
  hit on the page image.

- **`recipes/historic-hungary-record-routing.md`** — Route a record from historic Hungary by county, successor state and record type.
  Route a birth, marriage, death, census or tax entry from the pre-1920 Kingdom of Hungary by
  county, successor state and record type.

- **`recipes/austrian-confessional-register-routing.md`** — Route an Austrian or Czech-lands vital event to the confessional register that recorded it.
  Route an Austrian or Czech-lands vital event to the register that legally recorded it: a
  confessional register, the 1870 register for people outside a recognised church, or the regional
  archive that now holds the books.

### Church and civil registers

- **`recipes/us-vital-registration-coverage.md`** — Build a U.S. vital-registration coverage register before calling a birth or death record missing.
  Build a register of every U.S. birth and death registration authority and series before calling a
  record missing.

- **`recipes/us-church-record-custody.md`** — Find the custodian of a U.S. church record before calling it missing.
  Work out the denominational branch, congregation and current custodian of a U.S. church record.

- **`recipes/missing-marriage-jurisdiction-search.md`** — Search candidate jurisdictions for a missing marriage.
  Replace a marriage missing from the couple's home county with a dated, ranked list of candidate
  jurisdictions.

- **`recipes/early-new-england-town-records.md`** — Read early New England town books across parent towns and decode Torrey entries.
  Resolve village names to recordkeeping towns, read early New England town books across parent,
  daughter and neighbouring towns, preserve foundling narrative fields and decode Torrey's marriage
  notation.

- **`recipes/quaker-meeting-record-recovery.md`** — Recover a Quaker ancestor from monthly-meeting minutes and removal certificates.
  Recover a Quaker ancestor from men's and women's monthly-meeting minutes and both
  removal-certificate series.

- **`recipes/catholic-parish-diocesan-record-recovery.md`** — Recover a Catholic sacramental entry through parish, diocesan and successor holdings.
  Build a holdings register for a Catholic sacrament across the parish, alternative parishes, the
  diocesan copy, the successor custodian, dispensation files and Puerto Rican probanzas de soltería.

- **`recipes/catholic-sacramental-cross-notations.md`** — Follow Catholic baptism–marriage cross-notations between parishes.
  Follow a Catholic baptism–marriage cross-notation to the other sacrament's entry in another
  parish.

- **`recipes/hispanic-catholic-register-recovery.md`** — Recover a Mexican or Hispanic Catholic ancestor across parish and civil registers.
  Find a Mexican or other Hispanic Catholic ancestor across parish books and civil registers.

- **`recipes/portuguese-parish-civil-register-recovery.md`** — Recover a Portuguese ancestor in the parish and civil registers of mainland Portugal, the Azores and Madeira.
  Find a baptism, marriage or death in mainland Portugal, the Azores or Madeira in the parish books
  or the civil register.

- **`recipes/brazilian-parish-civil-registry-recovery.md`** — Recover a Brazilian ancestor in parish books, registry-office records and their substitutes.
  Find a Brazilian baptism, church marriage or burial, or a civil birth, marriage or death entry,
  and rebuild a family when the parish books are lost.

- **`recipes/french-canadian-register-recovery.md`** — Recover French-Canadian ancestors from combined registers, post and Montréal entries and notarial acts.
  Recover French-Canadian ancestors from combined registers, French-post and Notre-Dame de Montréal
  entries and notarial acts.

- **`recipes/french-belgian-civil-act-extraction.md`** — Extract French and Belgian civil acts field by field.
  Extract French or Belgian civil acts, trace French marginal continuations and separately
  maintained copies, and check Paris reconstructions when the original series is unavailable.

- **`recipes/dutch-civil-church-record-recovery.md`** — Recover Dutch civil acts and the church register kept before civil registration.
  Recover Dutch acts through ten-year tables, marriage supplements, separate contracts and guardian
  agreements; search burial/fee entries under the household head and trace the church registers kept
  before civil registration began.

- **`recipes/amsterdam-archival-record-recovery.md`** — Recover and read an Amsterdam City Archives register entry.
  Follow an Amsterdam City Archives index hit, tree claim or burial card back to its own register
  entry.

- **`recipes/scandinavian-parish-record-recovery.md`** — Reconstruct a Swedish household through parish examination and moving registers.
  Reconstruct a Swedish household through the household-examination, birth, marriage, death and
  moving registers.

- **`recipes/scandinavian-patronymic-farm-name-record-recovery.md`** — Recover a Scandinavian emigrant's home-parish entries under patronymic, farm and soldier names.
  Find a Danish, Norwegian, Swedish or Icelandic emigrant's home-parish entries under patronymic,
  farm and soldier names.

### Country record routing

- **`recipes/italian-stato-civile-parish-record-recovery.md`** — Recover an Italian ancestor in the Stato civile, parish books and conscription lists.
  Send an Italian birth, marriage or death to the register that was the legal record in that place
  and year (a Napoleonic municipal register, an Austrian-era parish book or the comune's Stato
  civile), then search conscription lists and the population register as separate series.

- **`recipes/us-tribal-enrollment-record-recovery.md`** — Find a claimed Native American ancestor on the right tribal roll, and read what the roll proves.
  Find a claimed Native American ancestor on the roll that fits the tribe, place and period, find
  who holds it now, and read what an enrollment, a rejected application or an absence proves.
  *Use for:* family lore of a Cherokee or other tribal ancestor; Dawes, Guion Miller, Baker or
  Indian Census Rolls; an ancestor missing from the Dawes Rolls or a rejected enrollment application

- **`recipes/spanish-civil-parish-record-routing.md`** — Route a Spanish or Andorran record to the archive that holds it on the event date.
  Route a Spanish or Andorran vital, padrón, Catastro, notarial, military or Civil War record to the
  body that holds it on the event date.

- **`recipes/french-departmental-record-routing.md`** — Route French records by département, creator, series and access rule.
  Route French civil, census, military, property, notarial, medal, consular, OFPRA refugee and
  prison records by creator, département, series and access rule; follow cadastral names through
  mortgage accounts to deeds and historical Paris addresses to property registers; trace
  Saint-Pierre victim leads to civil records/death judgments and pre-parish town lineages to civic
  admissions; follow missing Léonore dossiers into published nominations and named prisons through
  tables to admission entries; distinguish recruitment stages and JMO context, adoption-date
  references, Basque house-entry names and Breton marriage decrees.

- **`recipes/swedish-military-record-routing.md`** — Route a Swedish soldier, sailor, officer or conscript to the military series that survive for his type and period.
  Route a Swedish soldier, sailor, officer or conscript to the military series that survive for his
  type and period.

- **`recipes/australia-nz-record-routing.md`** — Route an Australian or New Zealand record to the holder and window of its date.
  Route an Australian or New Zealand birth, marriage, death, electoral roll, arrival, newspaper
  notice, Māori Land Court record or Aboriginal agency file to the holder and date window of its
  record.

- **`recipes/canadian-provincial-record-routing.md`** — Route a Canadian vital, military or Indigenous-series record to its province, custodian and access category.
  Route a Canadian vital registration, world-war personnel file, Métis or First Nations record, or
  British Home Child to the province, custodian and access category of its date and series.

### Irish and British records

- **`recipes/england-wales-gro-index-recovery.md`** — Read England and Wales GRO and FreeBMD index entries as registration observations.
  Read England and Wales GRO and FreeBMD index entries as registration observations.

- **`recipes/english-nonregister-record-recovery.md`** — Recover English records beyond the parish register.
  Take an English or Welsh question past the parish register to poor-law, apprenticeship, pre-1858
  church-court probate, dissenter or Catholic series, and Welsh marriage supplements with house/farm
  clues.

- **`recipes/uk-census-and-1939-register-interpretation.md`** — Read England and Wales censuses and the 1939 Register under each year's own rules.
  Read England and Wales censuses from 1841 to 1921 and the 1939 Register under each year's own
  rules.

- **`recipes/scottish-parish-statutory-record-recovery.md`** — Recover a Scottish birth, marriage or death across parish and statutory registers.
  Recover a Scottish birth, baptism, marriage or death across Old Parish, statutory, corrected-entry
  and kirk-session records.

- **`recipes/irish-civil-registration-jurisdiction-recovery.md`** — Recover an Irish civil-registration certificate and its jurisdiction chain.
  Carry an Irish civil-registration index entry or townland lead to the matching certificate and its
  jurisdiction chain.

- **`recipes/irish-probate-and-deed-recovery.md`** — Recover an Irish will, grant or deed after the 1922 losses.
  Recover an Irish will, administration or deed after the 1922 losses through the surviving
  calendars, will books, indexes and the Registry of Deeds, north and south.

- **`recipes/irish-emigrant-origin-locality.md`** — Resolve an Irish emigrant's origin locality from a place statement.
  Resolve an Irish place named by an emigrant's records or family tradition to a searchable
  locality.

- **`recipes/irish-land-valuation-occupancy-series.md`** — Read Irish valuation, tithe and estate-rental lists as dated occupancy series.
  Read Griffith's Valuation, tithe books, valuation revisions and estate rentals as dated occupancy
  series.

- **`recipes/irish-1901-1911-census-returns.md`** — Search, retrieve and read the Irish 1901 and 1911 census returns.
  Search, retrieve and read the Irish 1901 and 1911 census returns.

- **`recipes/convict-transportation-record-chain.md`** — Reconstruct a transported convict as a chain of record episodes.
  Rebuild a transported British convict's sentence as a chain of dated record episodes.

### German records

- **`recipes/german-register-image-recovery.md`** — Recover a German register entry through its locality, record offices and register version.
  Trace an emigrant's German place name to its church or civil register entry through the locality,
  record offices and register version; retain distinct named sponsor and proxy roles.

- **`recipes/german-emigrant-origin-sources.md`** — Trace a German emigrant's home town through emigration files, indexes and the parish register.
  Trace a German emigrant's home town through emigration files, indexes and the origin parish
  register.

- **`recipes/german-local-census-registration-recovery.md`** — Recover German local census lists and residential-registration entries.
  Recover German nominal census lists (roughly 1816–1916), residential-registration entries and
  associated settlement or trade-permission files.

- **`recipes/german-military-record-period-routing.md`** — Route a German soldier to the military series that survive for his period, army and rank.
  Route a German soldier to the series that survive for his period, army and rank class; recover
  dated hospital-book episodes when personnel files are missing.

- **`recipes/nazi-era-ancestry-proof-records.md`** — Find and read a Nazi-era ancestry proof as a certified copy of register entries.
  Find and read a Nazi-era ancestry proof (Ahnenpass, Ahnentafel, certified extracts) and route the
  search by the role that required it.

- **`recipes/german-official-gazette-notice-search.md`** — Read German official-gazette personnel, expulsion and expatriation notices as dated administrative notices.
  Read German gazette personnel, expulsion and expatriation notices as dated acts by a named
  authority.

- **`recipes/german-compensation-file-recovery.md`** — Recover a German compensation file from a Lastenausgleich or Wiedergutmachung index hit.
  Carry a Lastenausgleich or Berlin Wiedergutmachung index hit to the file behind it.

### Russian Empire and Soviet records

- **`recipes/russian-orthodox-metrical-book-recovery.md`** — Recover a Russian Orthodox metrical-book entry through the period parish, the consistory copy and its margin notes.
  Locate and read a Russian Orthodox metrical entry through the period parish, the consistory copy
  and its margin notes.

- **`recipes/russian-empire-jewish-metrical-book-recovery.md`** — Recover a Russian-Empire Jewish metrical entry through the registering rabbinate and its substitutes.
  Find the crown rabbinate that registered a Jewish community in the event year, check its book's
  survival and list named substitutes.

- **`recipes/russian-revision-list-household-chaining.md`** — Chain a Russian-Empire revision-list household across copies, sections and revisions (Urals evidence).
  Chain a non-Jewish revision-list household across copies, sections and revisions.
  *Use for:* Route an Orenburg Cossack, Bashkir or Tatar revision-era household by its jurisdiction
  on the record date.

- **`recipes/muscovite-census-settler-origin-recovery.md`** — Push a Ural or Siberian peasant line before 1719 through Muscovite census, fiscal and fugitive-inquiry books.
  Push a Ural or Siberian peasant line before 1719 through Muscovite census, fiscal and
  fugitive-inquiry books.

- **`recipes/russian-estate-registration-status.md`** — Read a Russian-Empire estate label as a dated registration status and choose the series by date.
  Read a Russian-Empire estate label as a dated registration status and choose the record series by
  the date it was acquired.

- **`recipes/russian-volost-town-administration-records.md`** — Find household-level series in volost, village-society and town-administration fonds.
  Find household-level lists in volost, village-society and town-administration fonds when metrical
  books or revision lists stop.

- **`recipes/old-believer-sectarian-record-recovery.md`** — Recover Old Believer and Edinoverie families from raskol series in consistory, revision, district and police fonds.
  Recover Old Believer and Edinoverie families from raskol series in consistory, revision, district
  and police fonds.

- **`recipes/orthodox-clergy-record-recovery.md`** — Rebuild a Russian Orthodox cleric's career and household from directories, eparchial gazettes and clergy registers.
  Rebuild a Russian Orthodox cleric's dated chain of posts and household from directories, eparchial
  gazettes and clergy registers.

- **`recipes/russian-imperial-service-record-recovery.md`** — Recover a pre-1917 Russian official's service list through the employing institution's fond.
  Recover a pre-1917 official's formulary or service list through the employing institution's fond.

- **`recipes/school-university-record-recovery.md`** — Recover a pupil or student through school, district, copy and later-file layers.
  Recover a pupil or student across school, educational-district, parallel-copy, yearbook and
  later-file layers.

- **`recipes/soviet-personal-file-recovery.md`** — Recover Soviet personal files when ZAGS or metrical records are lost.
  Rebuild a Soviet-era life from institutional personal files when ZAGS or metrical records are
  lost.

- **`recipes/russian-orthodox-confession-list-reading.md`** — Read Russian Orthodox confession lists household by household across years.
  Read Russian Orthodox confession lists by household across years, test ages and names, and check
  them against revision lists and metrical books.
  *Use for:* исповедная ведомость, исповедная роспись or духовная роспись of the Russian Empire;
  Compare исповедные ведомости across years

- **`recipes/russian-household-list-transcription-audit.md`** — Audit a transcription of a Russian confession list or revision list against the images.
  Audit a transcription of a Russian confession list or revision tale against the images: count the
  people first, settle glyphs against the same scribe, keep relationship chains, name forms and kin
  terms as written, and record the image value with its inconsistencies.
  *Use for:* Audit a researcher's, volunteer's or model's transcription of a Russian Orthodox
  confession list (исповедная ведомость) or revision tale (ревизская сказка) against the images.;
  Audit a spreadsheet of Russian household-list entries; проверить расшифровку исповедной ведомости
  или ревизской сказки

- **`recipes/chechen-ingush-1944-deportation-records.md`** — Trace a Chechen or Ingush family through the 1944 deportation and special settlement.
  Trace a Chechen or Ingush family through the 1944 deportation and special settlement, with both
  names of renamed places and both ends of the exile.

- **`recipes/russian-village-family-reconstitution.md`** — Reconstitute a Russian village's families when a generation's records are missing.
  When a Russian peasant's own birth or parentage record is missing, index everyone the village's
  registers name, in every role, rebuild its couples and households across the household-list,
  metrical-book and civil-register years, and test each identity with countable checks.
  *Use for:* Find the father of a Russian Orthodox peasant born after the last confession lists,
  whose birth entry does not survive; One man written under several surnames, or none, in metrical
  books and ZAGS registers; восстановить семьи деревни по исповедным ведомостям, метрическим книгам
  и книгам ЗАГС

### Censuses, tax, land and property

- **`recipes/canadian-census-interpretation.md`** — Interpret a historical Canadian census entry as a de jure listing.
  Read a historical Canadian census line as a de jure listing, and browse by geography when a name
  search misses.

- **`recipes/tax-roll-observation-workflow.md`** — Read tax rolls as a liability-bounded annual series.
  Read town, township or county tax lists as a liability-bounded annual series for each jurisdiction
  and tax type.

- **`recipes/deed-content-relationship-clues.md`** — Read deed content as dated relationship, probate, migration and parcel hypotheses.
  Read a retrieved deed's type, consideration, estate terms, parties, court-bond security recitals
  and parcel for dated clues to heirship, probate, migration or land identity.

- **`recipes/us-federal-land-entry-file-recovery.md`** — Recover a U.S. federal land-entry case file behind (or without) a GLO patent.
  Follow a GLO patent, bounty-land number or final-proof notice to the federal land-entry case file.

- **`recipes/marks-and-brands-record-recovery.md`** — Recover a livestock mark or brand registration.
  Carry a livestock marks-and-brands index entry to the actual registration or a described copy.

- **`recipes/georgia-texas-state-land-grant-recovery.md`** — Read Georgia and Texas original land grants: lottery draws, headright classes and the land office file.
  Find and read an original land grant from the State of Georgia or from Spain, Mexico, the Republic
  or the State of Texas, and keep each lottery entry, headright class or certificate within what its
  act required.
  *Use for:* a Georgia land lottery entry for orphans, a widow, a blank or a fortunate drawer; a
  Texas headright class, certificate or General Land Office file; no grant found for a Georgia or
  Texas ancestor

### Courts, legislatures, prisons and institutions

- **`recipes/court-case-file-recovery.md`** — Recover a U.S. court case file from its pointer records.
  Recover a U.S. state or local civil, chancery, divorce, criminal or incapacity case file through
  the records that point to it, then inventory its loose papers.

- **`recipes/us-federal-court-case-file-recovery.md`** — Recover a U.S. federal court case file.
  Take a lead to the right federal court for the period, its National Archives record group and
  index, and the loose case file.

- **`recipes/criminal-court-prison-record-recovery.md`** — Trace a U.S. arrest or imprisonment to its trying court, prison and clemency records, with England/Wales and Swedish routes.
  From an arrest, prison or census-institution lead, find the court that tried the case and recover
  U.S. prison, inmate, clemency and pardon records; a state or local court's case file belongs to
  court case-file recovery, a federal one to federal court recovery. Its England/Wales sections
  cover no-fixed-abode leads, assize and Old Bailey trials, absconder notices, charge searches and
  sentence wording; its Swedish sections cover prison, police-gazette and court-copy searches.
  *Use for:* Sing Sing name indexes

- **`recipes/state-legislative-private-act-petitions.md`** — Recover a state legislative private act and its petition.
  Recover a state legislative private act, such as a legitimation, name change, divorce or pension,
  and the petition behind it.

- **`recipes/illegitimacy-record-recovery.md`** — Recover records of a birth outside marriage.
  Find the bastardy bonds, court proceedings, support orders and church entries that a birth outside
  marriage could create, and preserve express status statements in apprenticeship instruments.

- **`recipes/institutional-patient-record-recovery.md`** — Recover an asylum or state-hospital patient through custodians, courts and newspapers.
  Seek asylum or state-hospital records through the custodian, court and newspapers; in Dutch
  research, check a child's marriage papers and locally described admission correspondence.

- **`recipes/us-period-law-record-reading.md`** — Read U.S. records under the law and legal language of their own place and date.
  Read a U.S. record's legal words, courts, bonds, and age or inheritance rules under the law of its
  own place and date, and keep each inference within what that law required.
  *Use for:* dower, dowry, next friend, adr c t a, voidable, penal sum or mainpernor in a record;
  Did the law of that place and date allow this marriage or inheritance

### Migration and origins

- **`recipes/immigrant-congregation-origin-records.md`** — Find an immigrant's hometown in U.S. congregation records.
  Find an immigrant's hometown in the registers of U.S. congregations chosen by language community,
  dates and address.

- **`recipes/surname-distribution-locality-leads.md`** — Rank localities to search from dated surname-distribution sources.
  Rank localities to search from dated surname-distribution sources for an uncommon surname.

- **`recipes/us-freedpeople-record-recovery.md`** — Trace an African American ancestor across the 1870 boundary.
  Trace an African American family back across the 1870 boundary.

- **`recipes/british-colonial-slave-registers.md`** — Trace an enslaved ancestor through the British colonial slave registers and compensation records.
  Trace an enslaved ancestor through the British colonial slave registers of 1813–1834 and the
  compensation records.

- **`recipes/chinese-lineage-jiapu-records.md`** — Recover a Chinese emigrant's lineage from character-written names, village and jiapu.
  Recover a Chinese emigrant's character-written name and ancestral village before searching lineage
  genealogies (jiapu).

- **`recipes/japanese-koseki-honseki-recovery.md`** — Recover the kanji name and honseki before requesting a Japanese koseki.
  Recover the kanji name and full historical domicile (honseki) before requesting a Japanese family
  register (koseki).

### Places, maps, libraries and manuscripts

- **`recipes/historical-place-name-resolution.md`** — Resolve a historical place name to dated, same-named candidates.
  Resolve a place named in a record, letter, Bible or biography to dated, same-named candidates from
  period gazetteers.

- **`recipes/historical-map-record-recovery.md`** — Recover and read historical maps as dated, copy-specific evidence.
  Read a fire-insurance sheet, atlas, plat, quadrangle or overlay as a dated observation; trace a
  detached archival map toward its possible originating case.

- **`recipes/published-book-catalogue-and-full-text-discovery.md`** — Find a published local history, compiled genealogy or family book across catalogues and full text.
  Find a published local history, compiled genealogy or family book across catalogues and full text.

- **`recipes/periodical-index-search-retrieval.md`** — Search a genealogical periodical index and retrieve the article.
  Search a genealogical periodical index such as PERSI and retrieve the article.

- **`recipes/manuscript-collection-recovery.md`** — Recover manuscript and archival collections that may mention an ancestor.
  Find personal, family and organisational papers by context, alternate ledger/daybook labels and an
  established society's personal-name index; request linked account pages or a complete claim folder
  with earlier applications.

- **`recipes/local-repository-uncatalogued-holdings.md`** — Ask for a local repository's uncatalogued holdings before reporting a negative.
  Ask a local library, society or archive about its uncatalogued holdings after its catalogue
  returns nothing.

### Family papers, photographs and oral history

- **`recipes/family-collection-intake-and-capture.md`** — Take in, capture and hand over an inherited family collection.
  Take in, inventory, plan the capture of and hand over an inherited family collection of boxes,
  albums, loose photographs, papers or existing scans.

- **`recipes/family-photograph-attribution-and-dating.md`** — Attribute and date an inherited family photograph from captions, provenance and imprints.
  Attribute and date an inherited family photograph from captions, provenance and the photographer's
  imprint.

- **`recipes/family-papers-and-bible-register-dating.md`** — Separate writing, mailing and event dates in family papers and Bible registers.
  Separate writing, mailing and event dates in letters, envelopes, address books, family Bible
  registers and inscribed books.

- **`recipes/family-interviews-and-oral-tradition.md`** — Record a family interview or inherited account with its speaker, prompter and chain.
  Record an interview with a relative, a supplied recording or an inherited story with its speaker,
  prompter and chain of transmission.

- **`recipes/repository-photograph-collection-search.md`** — Search repository photograph collections by place and subject.
  Search repository photograph collections for an ancestor, home, shop or community by place and
  subject.
  *Use for:* Search current and completed auction or marketplace lots for old family photographs.

### DNA workflows and research planning

- **`recipes/admixture-model-run-scope.md`** — Record the run scope before reading a G25, calculator or qpAdm admixture result.
  Record the run scope of a G25, calculator or qpAdm admixture result before reading it.

- **`recipes/ethnicity-estimate-version-comparison.md`** — Save, date and compare successive ethnicity-estimate versions.
  Save, date and compare successive ethnicity-estimate versions (AncestryDNA, MyHeritage,
  FamilyTreeDNA).

- **`recipes/dna-match-outreach-staging.md`** — Stage and draft outreach to a DNA match or untested relative.
  Stage and draft outreach to a DNA match, a match's account manager or an untested relative.

- **`recipes/descendancy-gap-worklist.md`** — Build a ranked descendancy gap worklist.
  Turn "research the descendants" into a ranked list of gaps tied to the records each lifespan
  crosses.

- **`recipes/gedcom-research-export.md`** — Export research findings to a GEDCOM file without changing what they prove.
  Export research findings to a GEDCOM file, or bring a supplied one into research, without changing
  what they prove.

### U.S. military service

- **`recipes/us-military-service-type-record-routing.md`** — Route pre-1900 U.S. military service by service type before searching or ruling it out.
  Route pre-1900 U.S. military service by service type to its own record series and custodian.

- **`recipes/us-civil-war-service-record-episodes.md`** — Read Civil War registration, service cards and unit events as separate episodes.
  Read Civil War draft registration, service cards, roster remarks and unit events as separate
  episodes.

- **`recipes/us-20th-century-military-service-reconstruction.md`** — Rebuild a 20th-century U.S. Army or Air Force service record after file loss or restriction.
  Rebuild a 20th-century U.S. Army or Air Force service record from records held outside a burned,
  thin or restricted personnel file, including state WWI questionnaires and Gold Star family
  packets, separate court-martial trial files, discharge-gated final pay and award General Orders.

<!-- recipe-catalog:end -->

## What a recipe is (and isn't)

- **Fact-checked.** Each recipe separates independently verified claims from figures reported by a
  cited source but not independently verified. Honor that line — don't present a source-reported
  transcript figure (a specific cM number, a percentage) as a rule.
- **Judgment, not fundamentals.** Recipes carry the non-obvious judgment an unaided answer gets
  wrong, not the well-documented basics you already produce reliably.
- **Platform procedures are dated.** Playbooks pair concrete actions with source-linked records.
  Verify available controls for the selected kit/account and preserve the actual observation scope.

## Attribution

These recipes are original Kinprove-authored distillations, licensed FSL-1.1-MIT (see `LICENSE`).
Third-party facts and methods are credited in each recipe's `https://github.com/Kinprove/genealogy-research-recipes/blob/edc63d0d7ca51c809a77747ff2bf76e45eccd67a/skills/genealogy-research-recipes/sources/<slug>.md`; any
reproduced third-party data is carved out in `NOTICE`.
