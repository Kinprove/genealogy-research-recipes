---
name: genealogy-research-recipes
description: >-
  Genealogy/DNA research: unknown parentage and WATO; endogamy, family comparisons, Y/mt/X DNA, phasing, admixture, cross-vendor controls, match outreach; documentary identity, conditional hypotheses, Genealogical Proof Standard and standards audits; archival image/transcript/index coverage, Ukrainian Jewish-list triage, ELIB guides; Jewish-name/OCR searches; Russian-Empire names, registration and emigrant origins; Holocaust testimony; Russian/Soviet military/repression episodes. Workflows for Ancestry, MyHeritage, FamilySearch, JewishGen, HebrewBooks, Beider indexes, 23andMe, FTDNA, GEDmatch, DNA Painter, Newspapers.com, Geni, WikiTree and RootsMagic. U.S., UK, Irish, Polish, Dutch, French, German, Nordic, Hispanic and Russian record recovery: church/civil registers, censuses, court, prison, asylum and school files, land, tax, livestock brands, military, place names, maps, books and manuscripts; Chinese jiapu, Japanese koseki; family photos, papers, Bible registers, oral history. Read the recipe first.
---

# Genealogy research recipes

Distilled, fact-checked **judgment and practical workflows** for genealogy work with DNA and records. Each recipe targets
what an LLM does *not* reliably know, or does *wrong* by default: the named failure modes, the
delegate-vs-never-trust lines, the reasoning sequence a human must own, and the records needed
to resume an investigation. Judgment recipes focus on reasoning; platform playbooks provide
ordered actions and investigator-created schemas with dated platform-documentation checks.

The research methods apply across platforms, including work from exported data. Kinprove
authorship does not require a Kinprove account, connector or scoring engine.

## How to use

1. Match the user's task to a recipe below.
2. **Read that recipe file in full before advising** — the value is in the specifics, not the summary.
3. Apply its "never trust / never delegate" boundaries as **hard constraints on your own output** —
   those are the exact places a confident answer goes wrong (e.g. fabricating cM→relationship odds,
   reading a WATO ranking as a verdict, ignoring endogamy).
4. If no recipe matches, answer normally — don't force-fit.
5. Before linking DNA results to a searchable tree, transferring genetic or match data to
   another service, or using an extension to export it, make a separate privacy decision.
   Record the people and exact data involved, the destination and intended audience; inspect
   the available visibility/searchability controls, export fields and extension permissions.
   Explain any tentative relationships or sensitive findings the action could disclose.
   Require explicit permission covering that action, destination and each person's genetic
   data; kit/account access or permission to analyze alone does not establish it.
   If permission or disclosure scope is unclear, do not link, transfer or export; keep the
   material local. Apply the consent and redaction rules in
   [AI for DNA research](recipes/ai-for-dna-research.md#verification--privacy-discipline).

## Recipes

- **`recipes/jewish-archival-list-triage.md`** — Select Ukrainian archival cases
  for named Jewish lists while separating title, geographical and document evidence.
  *Use for:* false-positive keywords, generic titles, civil-registration fund scope
  or candidate lists that have been presented as verified contents.
  *Core guardrail:* a title or locality signal is a retrieval lead; verify the
  requested named entries and retain uninspected cases explicitly.

- **`recipes/elib-ukrainian-archive-reference-books.md`** — Retrieve Ukrainian
  archival guides from ELIB and identify the correct volume, part and fund scope.
  *Use for:* catalogue-card versus PDF confusion, leading-zero item IDs, keyword
  misses, similar volume titles or garbled cover-text extraction.
  *Core guardrail:* verify the actual book; a constructed URL is a retrieval lead,
  and a historical guide does not establish current case availability or contents.

- **`recipes/dna-comparison-controls.md`** — Reconcile conflicting vendor or native
  results using exact tests, query controls, local marker coverage and reporting scope.
  *Use for:* an absent match, raw-file X coverage, PAR/build ambiguity or doubled totals.
  *Core guardrail:* unavailable inputs and out-of-scope displays are not measured negatives;
  reciprocal reports are not independent observations.

- **`recipes/archival-image-coverage-verification.md`** — Verify case boundaries,
  image order, transcript version and the pages and targets actually inspected.
  *Use for:* catalogue/cover disagreements, conflicting readings or completeness claims.
  *Core guardrail:* a finished reading pass, readable copy or indexed case does not
  establish complete image, target-name or subsection coverage.

- **`recipes/corpus-seeded-name-search.md`** — Recover attested spellings across
  scripts and OCR by separating encoding, orthography and field behaviour.
  *Use for:* Hebrew/Yiddish name misses, lossy search folds or uncalibrated zero results.
  *Core guardrail:* normalization is not spelling expansion; preserve originals and
  treat rescued hits as candidates rather than identity or kinship proof.

- **`recipes/holocaust-testimony-source-interpretation.md`** — Interpret a Yad Vashem
  result through its testimony, wartime list or survivor source and statement dates.
  *Use for:* unspecified death circumstances, submitter roles or evacuation conflicts.
  *Core guardrail:* a memorial database hit is not by itself a death finding; match
  identities and date roles before combining the timeline.

- **`recipes/russian-military-repression-record-episodes.md`** — Reconcile WWI/WWII
  and Soviet-repression records as separate dated source episodes.
  *Use for:* awards versus loss reports, repeated arrests or copied regional entries.
  *Core guardrail:* administrative dates and alleged events are distinct; a later
  order does not establish survival and a duplicated index is not independent support.

- **`recipes/genealogy-standards-audit.md`** — Audit a dossier, report, proof draft or
  documented tree by tracing each claim through examined sources and explained reasoning.
  *Use for:* citation gaps, search coverage, negative-evidence claims, GPS review,
  dependent conclusions, or choosing a research report, proof statement, summary or argument.
  *Core guardrail:* a completed checklist does not establish proof; name the inspected
  evidence and remaining gaps, and leave evidentiary sufficiency to the researcher.

- **`recipes/jewish-genealogy-conditional-hypotheses.md`** — Apply working hypotheses
  to Jewish naming, locality and DNA clues while keeping each proposition separate.
  *Use for:* proposed parentage, name equivalence, namesakes, naming customs, ancestral
  towns, conditional branches or segment attribution through an endogamous pedigree.
  *Core guardrail:* settling kinship does not settle birthplace, namesake or every segment;
  preserve the premises and dependencies in `recipes/evidence-proof-judgment.md`.

- **`recipes/burial-evidence-packet.md`** — Recover a cemetery entry, its photograph
  or inscription, and the plot and cemetery-record locators needed to inspect the burial.
  *Use for:* cemetery coverage, surname variants, Hebrew and civil inscriptions,
  death/burial discrepancies or a database hit that needs a cemetery-record follow-up.
  *Core guardrail:* distinguish death, burial, inscription and database statements;
  keep missing fields and conflicting observations visible in the evidence packet.

- **`recipes/city-directory-observation-workflow.md`** — Build a comparable series
  of city-directory names, addresses and occupations from checked editions and sections.
  *Use for:* surrounding locality sections, abbreviation keys, index errors,
  address/occupation changes or a person missing from one directory edition.
  *Core guardrail:* separate unavailable and uninspected editions from inspected
  sections with no hit; a gap does not establish a move, death or identity.

- **`recipes/land-index-book-series-recovery.md`** — Follow a land-record lead through
  both relevant index directions to the correct instrument and record-book series,
  or carry a federal patent lead into its separate entry file.
  *Use for:* grantor/grantee indexes, ambiguous book locators, separate book series,
  delayed recording, a surname search that missed the alternative index entry,
  or cash-sale, bounty-land and homestead supporting packets.
  *Core guardrail:* copy the original locator, distinguish instrument and recording
  dates, and report bounded retrieval coverage before interpreting title or kinship.

- **`recipes/probate-case-document-inventory.md`** — Recover the documents behind
  a probate index, will or administrator's bond as a case inventory with unresolved leads.
  *Use for:* probate record series, references to other documents, later actions,
  non-will proceedings, reverse searches from a guardian to wards, or an estate search
  that stopped at the first useful document.
  *Core guardrail:* finding a will does not finish the case; retain each document's
  locator and remaining retrieval gaps, then hand off evidence interpretation.

- **`recipes/us-military-pension-file-recovery.md`** — Carry a service clue or pension
  index card to the appropriate application file and inventory the claim's documents.
  *Use for:* pension-card identifiers, record custodians, complete versus abbreviated
  copy products, widow/dependent applications, household and means statements,
  objections or later claim decisions.
  *Core guardrail:* distinguish the index, service record, pension file and copy product;
  preserve original image order beside the claim timeline and explicit missing material.

- **`recipes/irish-catholic-parish-image-recovery.md`** — Carry an Irish Catholic
  baptism or marriage lead into the NLI parish-register images and locate the actual entry.
  *Use for:* RootsIreland/Findmypast transcriptions, Catholic parish/register selection,
  a link opening the register's first page, date browsing or exact image citations.
  *Core guardrail:* verify the opened route and entry; preserve register and image
  locators, and keep baptism distinct from birth unless the original records both.

- **`recipes/polish-index-original-record-recovery.md`** — Recover an original Polish
  register entry from Geneteka, Metryki or Szukaj w Archiwach, or document the retrieval gap.
  *Use for:* SKAN links, locality/confession/year/act locators, PRADZIAD descriptions,
  archival fonds and units, missing scans or alternative holding routes.
  *Core guardrail:* an index or holding description is not an inspected original;
  preserve the act's locator and the exact level where access or retrieval stopped.

- **`recipes/rootsmagic-tree-reconciliation-workflow.md`** — Reconcile selected
  facts and sources between RootsMagic, Ancestry TreeShare and FamilySearch.
  *Use for:* person crosswalks, staged additions/replacements, citation and media transfer,
  duplicate sources, destination checks or resuming a bounded synchronization batch.
  *Core guardrail:* review each object and direction, then reopen the destination
  to verify the saved content; the three trees are not an automatic mirror.

- **`recipes/wikitree-dna-tester-links.md`** — Register a DNA test on the actual
  tester's WikiTree profile and verify its FamilyTreeDNA or GEDmatch link destination.
  *Use for:* tester/kit crosswalks, external tree links, visibility settings,
  propagated DNA Connections or pedigree leads needing documentary follow-up.
  *Core guardrail:* a registered test or tree-derived connection is not a measured
  comparison or DNA-confirmed relationship; preserve each observation separately.

- **`recipes/usa-immigration-search-recovery.md`** — Twelve historical U.S. immigration
  workflows: reconstruct journeys, test port, airport and border coverage, recover name variants,
  pair departures with arrivals, read complete manifests, distinguish detention outcomes,
  interpret dated verification marks, find naturalizations across courts, check historical
  citizenship rules, locate federal files and recover broken image links.
  *Use for:* ship and aircraft passenger lists, Canada/Mexico crossing records, naturalization minute books,
  C-files, A-files and AR-2 records.
  *Core guardrail:* preserve the complete image context and actual collection coverage;
  resolve citizenship rules and file custody for the person's dates before drawing conclusions.
  *Public companion route:* when this recipe names `russian-empire-immigration-research`,
  use the public [Tracing Immigrant Origins outline](https://files.lib.byu.edu/family-history-library/research-outlines/NonGeographic/TracingImmigrantOrigins.pdf)
  for finding the original hometown and selecting origin-side sources. Confirm the historical
  jurisdiction and record language with current archive finding aids. For Jewish name and
  registration/residence attribution, use the [Russian-Empire identity recipe](recipes/russian-empire-jewish-identity-attribution.md).
  The U.S. workflows can also be used independently.

- **`recipes/familysearch-practical-record-workflows.md`** — Seventeen FamilySearch operations:
  recover Catalog/DGS holdings and image-only records, preserve view-scoped citations,
  refine Full Text/Simple Search, clean up Source Linker attachments and same-name Tree repairs,
  and share research reports with checked visibility and reader access.
  *Use for:* FamilySearch howtos, Catalog/film/DGS crosswalks, unindexed images, Full Text
  or Simple Search, Source Linker cleanup, profile repair and Source Box reuse.
  *Core guardrail:* inspect actual images and identities; preserve query/view scope;
  verify report audience and visibility before treating an attachment as shared evidence.

- **`recipes/russian-empire-emigrant-origin-recovery.md`** — Five workflows for tracing
  an emigrant from destination records to an exact historical locality: reconcile arrival
  clues, recover failed name searches, extract complete manifests, follow contact/travel
  networks, and prepare a locality and archive handoff. Principally 1880–1924 U.S. arrivals,
  including Canadian transit, across confessions.
  *Use for:* conflicting arrival years, changing names, missing manifest pages, two contact
  fields, separate family arrivals, residence/birthplace ambiguity or an unresolved origin town.
  *Core guardrail:* preserve each person's record and place role; verify linked pages and
  outcome evidence; direct U.S.-bound Canadian transit does not imply a Form 30A record.

- **`recipes/us-census-practical-workflows.md`** — Nine practical U.S. census procedures:
  recover households, browse target-year districts, follow 1950 revisit sheets, compare
  pre-1850 age bins, bridge the 1890 gap, extract supplements and family fields, search
  mortality schedules, and follow surname changes.
  *Use for:* a missing census household, an address without a name hit, sheet 71,
  tick-mark counts, substitute censuses, sample lines, marriage/children fields, competing child rosters,
  mortality reporting windows, or formerly enslaved families under different surnames.
  *Core guardrail:* preserve the original locator and literal observations; keep
  calculated intervals and proposed identities separate, and route proof rulings to
  `recipes/evidence-proof-judgment.md`.

- **`recipes/geni-practical-research-workflows.md`** — Eight practical Geni workflows:
  recover name variants, preserve relationship focus, cite facts, choose projects, compare
  merge candidates, track tree conflicts, create GEDCOM branches and inspect scoped exports.
  *Use for:* Geni language/alias fields, relationship paths, source documents, public projects
  or private workspaces, merge requests, unmerge requests, GEDCOM imports and tree reports.
  *Core guardrail:* preserve profile URLs and dated scope; distinguish tree assertions,
  source-supported statements, pending requests and completed changes. Draft manager or
  curator requests for human review, and inspect private content before sharing an export.

- **`recipes/ancestry-dna-match-investigation.md`** — Eight practical AncestryDNA workflows:
  use a target's closest relatives, build branch anchor tables, search collateral names,
  organize groups and notes, correct tester links, audit labels and recover missing match rows.
  *Use for:* AncestryDNA match investigation, Pro Tools Enhanced Shared Matches, colored dots,
  linked trees, ThruLines, access-dependent gaps or connecting a match to another testing site.
  *Core guardrail:* preserve dated access and pair-specific observations; shared matches are
  clues rather than segment triangulation, and tree paths need documentary verification.

- **`recipes/myheritage-dna-match-investigation.md`** — Nine practical MyHeritage DNA workflows:
  select the right kit, preserve theories before reassignment, build filtered shortlists, use
  labels and notes, capture pair-specific shared-match values, compare triangulation subsets,
  audit theory connections, recover private-tree leads, contact matches and resume dated packets.
  *Use for:* MyHeritage DNA match investigation, kit relinking, largest-segment sorting,
  labels/favorites, Shared DNA Matches, Theory of Family Relativity or an investigation follow-up.
  *Core guardrail:* keep kit identity, access, filter state, pair-specific values and exact
  comparison sets explicit; an unshown measurement is not zero, and a theory is a path to review.

- **`recipes/unknown-parentage-wato.md`** — Placing an unknown person (an unknown parent, an
  adoptee's bio-parent, an unplaced ancestor) into a tree using DNA matches + WATO odds.
  *Use for:* "who is my unknown grandfather/father", adoptee bio-family search, WATO hypothesis
  scoring, clustering matches to an ancestral couple, tied hypotheses, choosing a discriminating
  tester, or deciding which observations to withhold from a calculation.
  *Core guardrail:* WATO ranks placements on a tree **you already built**, gives **relative** odds
  among competing hypotheses (never a verdict), and breaks **silently** under endogamy / pedigree
  collapse / any multi-path match.

- **`recipes/ai-for-dna-research.md`** — Using an AI assistant *reliably* on DNA/genealogy work:
  what to delegate freely, what to never trust, and the prompt patterns that work. Includes
  endogamous match prioritization, segment attribution, targeted testing of outmarrying branches,
  and coherent family comparisons across tested ancestors, siblings and descendants.
  *Also use for:* "how are these two families connected", multiple related focal testers,
  repeated descent paths, a long segment in a relative that is shorter/absent in a descendant,
  mixed-origin segment overhangs, fused clusters, validating a match's own pedigree,
  or inspecting supplied ethnicity-region maps and AncestryDNA Journeys timelines for locality-search leads.
  *Use for:* any "can AI/ChatGPT/Claude help me with my DNA / tree / citations", **or** whenever
  you (the assistant) are about to compute or assert something in this domain.
  *Core guardrail:* never fabricate cM→relationship odds (route to the Shared cM Project / DNA
  Painter WATO); every AI output is a **hypothesis to verify**, never a fact to file.

- **`recipes/ydna-mtdna-interpretation.md`** — Interpreting Y-DNA and mtDNA results (a haplogroup
  assignment, a Y-STR genetic-distance match, an mtDNA sequence match): what each can actually
  establish about a *genealogical-timeframe* relationship, and where confident interpretation
  crosses into fabrication. The Y-STR/mtDNA complement to `ai-for-dna-research.md` (autosomal cM).
  *Use for:* "what does my haplogroup / Y-STR match / mtDNA match mean", "how many generations back
  is genetic distance N", "does this haplogroup contradiction prove a non-paternity event",
  differing Y labels, measured versus inferred SNP results, choosing a tester to split an
  unresolved SNP block, TMRCA disagreement with a dated pedigree, or a pair matching on both
  autosomal DNA and Y-DNA/mtDNA through potentially different ancestral lines.
  *Core guardrail:* never assign a haplogroup or compute a GD→generations/TMRCA point estimate from
  memory (route to FTDNA Discover / TiP report / Match Time Tree, quote a resolution-dependent
  **range**); an exact match at low resolution is **unresolved**, not recent; a haplogroup
  contradiction or absent surname-match is a **flag needing corroboration**, never proof of an NPE.

- **`recipes/xdna-phasing-judgment.md`** — X-DNA matches and visual/parental phasing: what a
  segment, an X match, or a phased chromosome map can actually confirm or eliminate, and where
  confident-sounding analysis is actually fabrication.
  *Use for:* "is this X-DNA match trustworthy", "what's the minimum X cM threshold", "phase my kit
  against a parent or siblings", "half-sister or aunt", "does this X match rule out a father",
  reconstructed-kit quality, artificial homozygosity, or interpreting matches to a synthetic kit.
  *Core guardrail:* never invent a small-segment or X-DNA false-positive rate or cM threshold — cite
  the specific company/study, since they diverge by design and by pair-sex; phasing reduces but never
  eliminates pseudosegments on either side; usable X evidence can reject an incompatible
  non-PAR route, while compatibility alone does not confirm the proposed ancestor.

- **`recipes/ai-for-documentary-records.md`** — Using an AI assistant *reliably* on DOCUMENTARY / records
  work (NOT DNA): handwriting transcription & translation, AI full-text / OCR finding aids (FamilySearch
  Full-Text Search), reviewing & correcting AI-indexed records, evaluating AI record hints, and image
  restoration / colorization / generation & evidentiary trust.
  *Use for:* any "can AI/ChatGPT/Gemini transcribe or translate this handwriting", "full-text search for
  unindexed deeds/probate", "correct AI-indexed records", "evaluate an AI record hint", "colorize/restore
  an old photo".
  *Core guardrail:* every AI output is a **hypothesis to verify** against the ORIGINAL image; a bare LLM is
  not a search engine; never use an AI-restored/generated face for identification.

- **`recipes/evidence-proof-judgment.md`** — Correlating evidence & proving identity: the judgment an AI gets
  WRONG when it recites the Genealogical Proof Standard but misapplies it — same-name conflation, conflict-
  flattening, over-reading a document, negative-evidence errors, DNA/documentary siloing, de-novo fabrication,
  and sycophancy toward the answer you want. Includes a premise and dependency register
  for investigating a tentative branch without silently inheriting its assumptions.
  *Use for:* separating same-named people, resolving conflicting records, weighing indirect vs negative evidence,
  combining DNA with documents into ONE proof, conditional placements, discriminating
  hypothesis tests or revising dependent claims — **and** whenever you (the assistant)
  are about to state a genealogical conclusion.
  *Core guardrail:* the human owns every ruling (merge/separate, conflict resolution, exhaustiveness, the final
  "therefore proven"); a provisional link can direct a search without establishing
  dependent ancestry. The model assembles and drafts but NEVER concludes.
- **`recipes/russian-empire-jewish-identity-attribution.md`** — A Russian-Empire Jewish ancestor who turns up
  under a given name, patronymic or surname that fits neither candidate branch: the inverse of same-name
  collapse (one person, several names), read through the imperial record system — revision lists (ревизские
  сказки), family lists (посемейные списки), metrical books and recruit files as ledgers of *registration*
  (приписка), not vital records — with the naming and re-registration mechanisms (double names, head-of-household
  patronymics, heir naming, stepchild, fostered orphan, levy evasion, son-in-law surname, surname split,
  conversion) carried as competing hypotheses, and the "prediction must differ" test before any DNA is asked to
  choose between branches of one endogamous family.
  *Use for:* "which brother was his father", a boy registered in a relative's household, a wife's child from a
  first marriage, a family hiding a son from the recruit levy / cantonists, brothers under different surnames,
  a patronymic that is the grandfather's or the husband's name, a person missing from a revision list, or
  DNA that "can't tell the two branches apart" under Ashkenazi endogamy plus repeated pedigree collapse.
  *Core guardrail:* chain the household before you judge the name; find the приписка before you search a
  town; write which tester's result would DIFFER under the two hypotheses before touching a match list — if
  none differs, say "undecidable with current testers" and name the tester who would decide it.

- **`recipes/jewishgen-search-family-reconstruction.md`** — Retrieving JewishGen family records when
  names, ages, towns or a woman's surname are uncertain. Build explicit name-variant and mixed-field
  search batches, distinguish registration from residence, and look for wives' natal families or
  married daughters through children's records and household comparisons.
  *Use for:* JewishGen exact, partial, phonetic or fuzzy searches; double names and patronymics;
  conflicting ages or delayed registration; a missing marriage record, unknown maiden name or
  daughter who disappears under a married surname.
  *Core guardrail:* verify each collection's field and search-method semantics; a name, age or
  household match creates a candidate, and a recruitment explanation remains a hypothesis until
  independent records support it.

- **`recipes/beider-given-name-variants.md`** — Expanding documentary searches with recorded
  Ashkenazi given-name forms from the male and female J-Roots Beider indexes.
  *Use for:* an unfamiliar or approximate Cyrillic given name, compound names, alternate
  spellings, ambiguous article labels, or documenting a DNA match's family under another name form.
  *Core guardrail:* query offline with `scripts/lookup_beider_name.py --name` for up to 20
  article groups by default, including similar candidates when an exact match exists; then
  retrieve a selected article's recorded variants with `--key`. Comparison ignores spaces
  and supported hyphens/dashes; keep compound component searches separate. Distinguish
  unavailable local data from an absent entry. Approximate matches are spelling suggestions,
  not source-backed synonyms; article membership never proves identity or kinship.

- **`recipes/myheritage-historical-record-search.md`** — Recovering MyHeritage historical
  records hidden by collection coverage, query fields, name variants, languages or OCR.
  *Use for:* no-result searches, Collection Catalog, relative pivots, historical jurisdictions,
  newspaper keywords/OldNews or an index that must lead onward to an original record.
  *Core guardrail:* diagnose coverage and field meaning before tightening; change one constraint
  at a time, preserve original text, and treat structured or translated values as search leads.

- **`recipes/newspapers-com-search-recovery.md`** — Recovering newspaper notices when issue
  coverage, printed names or OCR hide an ancestor on Newspapers.com. Build a title–holding–issue
  register first, resolve another holding when coverage is insufficient, then search initials,
  married names, associates, occupations and addresses and verify the original notice.
  *Use for:* a failed newspaper name search, an unknown maiden name, a missing obituary,
  immigration or family-reconstruction leads, title changes, incomplete issue coverage,
  alternate holdings or unreadable OCR.
  *Core guardrail:* a page-level hit can join different notices; verify each person, relationship,
  event date and place in its actual notice. A failed query is not evidence that an event never
  happened, and a second index of the same newspaper image is not independent corroboration.

- **`recipes/hebrewbooks-search-recovery.md`** — Recover HebrewBooks names or passages
  missed by OCR, catalogue spelling or a query that never reached search.
  *Use for:* Hebrew OCR letter confusions, catalogue versus full-text searches, short
  mobile queries, inaccessible routes, Shafeh title searches, given-name indexes and
  viewer versus printed page numbers.
  *Core guardrail:* distinguish an unsubmitted query or access error from a completed
  search with no hits. Keep OCR test strings separate from historical names, and record
  the book ID, viewer page, printed locator and edition separately.

- **`recipes/ancestry-record-search-recovery.md`** — Recovering archival records missed by an
  Ancestry search. Diagnose scope and coverage before relaxing dates, places or names; use
  collection descriptions, original book indexes, census districts and the holding archive.
  *Use for:* an attached census disappearing from results, narrow Card Catalog matches,
  birthplace/residence confusion, conservative wildcard batches, name-free searches, book
  page versus image numbers, enumeration-district browsing, or index-only records.
  *Core guardrail:* search results generate candidates; a zero-result query does not prove
  absence, and the original document must support identity before filing a relationship.

- **`recipes/23andme-match-research.md`** — Twelve practical workflows for 23andMe
  match research, permitted comparisons, numerical matrices and dated preservation.
  *Use for:* match worksheets, connection permissions, selected-segment painting,
  parent-side information, ancestry confidence/history, legacy bucketing,
  reconstructed ancestors, extension exports/groups, manual shared-match charts,
  or floating research-tree branches.
  *Core guardrail:* verify actual access and quantity scope; keep shared-list
  membership, matching intervals, ancestry estimates and documentary identity separate.

- **`recipes/ftdna-practical-dna-workflows.md`** — Eight FTDNA workflows for Matrix observations, paired
  match/segment exports, duplicate-name joins, MyHeritage tree links, Family Matching
  and public Y-DNA Group Time Tree, supplied Globetrekker map or two-label comparison packets.
  *Use for:* Family Finder CSV scope, opaque note handles, selected-match segment files,
  transferred links that need confirmation, dated parental-bucket inventories,
  subgroup selections, branch estimates, obscured map nodes, hidden details or authorized project-display checks.
  *Core guardrail:* reconcile export scope before joining; hold out ambiguous names;
  confirm each tree link and preserve observed vendor assignments separately from pedigree proof.
  A selected Group Time Tree view has its own scope; missing or withheld details
  do not establish an absent lineage, and kit access does not authorize public display.

- **`recipes/dnapainter-practical-dna-workflows.md`** — Ten practical DNA Painter workflows:
  paint measured matches, copy or merge maps of one tester, intersect phased inheritance,
  calculate provisional missing intervals, combine coordinate spans, plan descendant tests,
  annotate cluster-derived maps, build direct-ancestor gap worklists, audit numeric pair amounts,
  and inspect Shared cM histograms and two-value range screens.
  *Use for:* Paint a new match, map duplication/CSV transfers, Common Segment Generator,
  Inferred Segments Generator, Distinct Segment Generator, Coverage Estimator,
  Cluster Auto Painter annotations, ancestral-tree reports, sourced numeric pair matrices,
  or Shared cM histograms and two-value range screens.
  *Core guardrail:* verify the people, chromosome copy and genome build; keep measured
  comparisons, inferred intervals, coordinate unions, pedigree estimates and documentary
  tree worklists distinguishable. A relationship note does not assign all of a match's intervals;
  matrix shading does not establish a relationship, and copied names do not supply cM.

- **`recipes/gedmatch-practical-dna-workflows.md`** — Eight GEDmatch workflows:
  establish kit/run baselines, follow shortlist entries into direct comparisons, check
  three-kit cores, bound locus searches, freeze tag/MKA groups, preserve triangulation,
  and record parental-phasing or Lazarus input groups and generated-kit roles.
  *Use for:* GEDmatch One-to-Many, One-to-One, match-both, Segment Search, tag groups,
  Multiple Kit Analysis, Triangulation, parental phasing or Lazarus reconstruction.
  *Core guardrail:* preserve actual access, thresholds, pairwise intervals and fixed
  rosters; separate shared-list membership and generated-kit signals from pedigree proof.

## More recipes by topic

Steps 2 and 3 of How to use apply here too: read the matching file in full before advising,
and treat its guardrail as a hard limit on your own output.

### Church and civil registers

- **`recipes/us-vital-registration-coverage.md`** — Build a register of every U.S. birth and death registration authority and series before calling a record missing. *Guardrail:* the statewide mandate year is not the first year of coverage, and one county index miss is not "no record exists".
- **`recipes/us-church-record-custody.md`** — Work out the denominational branch, congregation and current custodian of a U.S. church record. *Guardrail:* do not report "not found" or "records lost" until that custody path has been checked.
- **`recipes/missing-marriage-jurisdiction-search.md`** — Replace a marriage missing from the couple's home county with a dated, ranked list of candidate jurisdictions. *Guardrail:* one county miss is not a finished search; report a gap only after every ranked candidate is searched or recorded as unavailable.
- **`recipes/early-new-england-town-records.md`** — Resolve village names to recordkeeping towns, read early New England town books across parent, daughter and neighbouring towns, preserve foundling narrative fields and decode Torrey's marriage notation. *Guardrail:* decode a Torrey entry before using it, and record which whole volumes were read.
- **`recipes/quaker-meeting-record-recovery.md`** — Recover a Quaker ancestor from men's and women's monthly-meeting minutes and both removal-certificate series. *Guardrail:* check that Hinshaw covers the meeting, decode the meeting before placing the entry, and keep each numbered date exactly as written.
- **`recipes/catholic-parish-diocesan-record-recovery.md`** — Build a holdings register for a Catholic sacrament across the parish, alternative parishes, the diocesan copy, the successor custodian, dispensation files and Puerto Rican probanzas de soltería. *Guardrail:* one failed parish search or online collection does not show that the entry never existed or that the register was lost.
- **`recipes/catholic-sacramental-cross-notations.md`** — Follow a Catholic baptism–marriage cross-notation to the other sacrament's entry in another parish. *Guardrail:* indexes drop the baptism-place statement and the later marriage note, so read the original page in both directions.
- **`recipes/hispanic-catholic-register-recovery.md`** — Find a Mexican or other Hispanic Catholic ancestor across parish books and civil registers. *Guardrail:* select the parish, not the town, search every surname arrangement, and never copy a baptism date into the birth field.
- **`recipes/french-canadian-register-recovery.md`** — Recover French-Canadian ancestors from combined registers, French-post and Notre-Dame de Montréal entries and notarial acts. *Guardrail:* do not call the person absent until the French-Canadian name forms are exhausted.
- **`recipes/french-belgian-civil-act-extraction.md`** — Extract French or Belgian civil acts, trace French marginal continuations and separately maintained copies, and check Paris reconstructions when the original series is unavailable. *Guardrail:* bind each annotation to its subject and copy; keep record and event dates apart, and convert Republican dates with a tool, never by arithmetic.
- **`recipes/dutch-civil-church-record-recovery.md`** — Recover Dutch acts through ten-year tables, marriage supplements, separate contracts and guardian agreements; search burial/fee entries under the household head and trace pre-1811 church registers. *Guardrail:* an index miss is not absence, and a father, death date or sibling set from a compiled tree needs the original entries.
- **`recipes/amsterdam-archival-record-recovery.md`** — Follow an Amsterdam City Archives index hit, tree claim or burial card back to its own register entry. *Guardrail:* read the entry by its register type, not by the index label; an ondertrouw is a registration, not a wedding.
- **`recipes/scandinavian-parish-record-recovery.md`** — Reconstruct a Swedish household through the household-examination, birth, marriage, death and moving registers. *Guardrail:* follow the family by farm and page cross-reference, not by patronymic, and settle identity at the household level.
- **`recipes/scandinavian-patronymic-farm-name-record-recovery.md`** — Find a Danish, Norwegian, Swedish or Icelandic emigrant's home-parish entries under patronymic, farm and soldier names. *Guardrail:* the American surname is usually not the register name; separate same-named parishioners by birth date, parents, spouse and farm, never by name alone.

### Irish and British records

- **`recipes/england-wales-gro-index-recovery.md`** — Read England and Wales GRO and FreeBMD index entries as registration observations. *Guardrail:* an entry gives a registration quarter, district and locator, not an event date, birthplace, spouse pairing or parentage.
- **`recipes/english-nonregister-record-recovery.md`** — Take an English question past the parish register to poor-law, apprenticeship, pre-1858 church-court probate and dissenter or Catholic series. *Guardrail:* a silent parish register does not make the question unanswerable; record which series do not cover the case.
- **`recipes/uk-census-and-1939-register-interpretation.md`** — Read England and Wales censuses from 1841 to 1921 and the 1939 Register under each year's own rules. *Guardrail:* settle the year's image, writer, reference night and coverage before reading any value as presence, age or status.
- **`recipes/scottish-parish-statutory-record-recovery.md`** — Recover a Scottish birth, baptism, marriage or death across Old Parish, statutory, corrected-entry and kirk-session records. *Guardrail:* register gaps and unsearched denominations are coverage still to search, not proof that the event did not happen.
- **`recipes/irish-civil-registration-jurisdiction-recovery.md`** — Carry an Irish civil-registration index entry or townland lead to the matching certificate and its jurisdiction chain. *Guardrail:* the index film is not the certificate and the registration quarter is not the birth date; keep same-named townlands and civil versus Catholic parishes apart.
- **`recipes/irish-emigrant-origin-locality.md`** — Resolve an Irish place named by an emigrant's records or family tradition to a searchable locality. *Guardrail:* a named town is a lead of unknown administrative level, not the birthplace, and surname presence or a matching farm name does not prove origin.
- **`recipes/irish-land-valuation-occupancy-series.md`** — Read Griffith's Valuation, tithe books, valuation revisions and estate rentals as dated occupancy series. *Guardrail:* these lists are not household censuses, and an occupier change is not father-to-son inheritance.
- **`recipes/convict-transportation-record-chain.md`** — Rebuild a transported British convict's sentence as a chain of dated record episodes. *Guardrail:* one index entry never stands for the whole chain; each episode keeps its own series, locator and date role.

### German records

- **`recipes/german-register-image-recovery.md`** — Trace an emigrant's German place name to its church or civil register entry through the locality, record offices and register version; retain distinct named sponsor and proxy roles. *Guardrail:* do not take the first same-named town, assume it kept its own records, or cite a derivative as the original.
- **`recipes/german-emigrant-origin-sources.md`** — Trace a German emigrant's home town through emigration files, indexes and the origin parish register. *Guardrail:* a miss in permission files or a regional index does not prove that the person did not come from that state; confirm every hit in the original register.
- **`recipes/german-local-census-registration-recovery.md`** — Recover German nominal census lists (roughly 1816–1916) and residential-registration entries for a town. *Guardrail:* "we have no census" is not proof of absence, statistical tables are not the record, and a stated origin town is not the birthplace.
- **`recipes/german-military-record-period-routing.md`** — Route a German soldier to the series that survive for his period, army and rank class. *Guardrail:* a canton, gazette notice or casualty-list line is a lead, never a birthplace, death date or identity.
- **`recipes/german-official-gazette-notice-search.md`** — Read German gazette personnel, expulsion and expatriation notices as dated acts by a named authority. *Guardrail:* a notice does not show residence in the district, prove a departure or confirm identity.
- **`recipes/german-compensation-file-recovery.md`** — Carry a Lastenausgleich or Berlin Wiedergutmachung index hit to the file behind it. *Guardrail:* a hit does not show who filed, which relatives the file names or that the indexed person is yours, and a no-hit does not mean no file mentions a relative.

### Russian Empire and Soviet records

- **`recipes/russian-orthodox-metrical-book-recovery.md`** — Locate and read a Russian Orthodox metrical entry through the period parish, the consistory copy and its margin notes. *Guardrail:* margin decrees are separate dated events, and names and patronymics are hypotheses, not proof of descent.
- **`recipes/russian-empire-jewish-metrical-book-recovery.md`** — Find the crown rabbinate that registered a Jewish community in the event year, check its book's survival and list named substitutes. *Guardrail:* synagogues or a large Jewish population do not show that a place had its own crown rabbi, so do not search for "the village's" book.
- **`recipes/russian-revision-list-household-chaining.md`** — Chain a non-Jewish revision-list household across copies, sections and revisions. *Guardrail:* a central and a local copy are not two confirmations, and Urals fond numbers and age patterns must be checked locally.
- **`recipes/muscovite-census-settler-origin-recovery.md`** — Push a Ural or Siberian peasant line before 1719 through Muscovite census, fiscal and fugitive-inquiry books. *Guardrail:* each book is a copy-specific observation, and a stated origin stays testimony until a departure-side entry matches.
- **`recipes/russian-estate-registration-status.md`** — Read a Russian-Empire estate label as a dated registration status and choose the record series by the date it was acquired. *Guardrail:* the town in the label is not the birthplace or residence, and a factory or rural-inhabitant label is not a job.
- **`recipes/russian-volost-town-administration-records.md`** — Find household-level lists in volost, village-society and town-administration fonds when metrical books or revision lists stop. *Guardrail:* do not stop at church registers and revision lists, and an inventory title stays a lead until the file is inspected.
- **`recipes/old-believer-sectarian-record-recovery.md`** — Recover Old Believer and Edinoverie families from raskol series in consistory, revision, district and police fonds. *Guardrail:* absence from the ordinary Orthodox books does not mean the family went unrecorded; a confession label is a dated administrative classification.
- **`recipes/orthodox-clergy-record-recovery.md`** — Rebuild a Russian Orthodox cleric's dated chain of posts and household from directories, eparchial gazettes and clergy registers. *Guardrail:* do not merge or split clergy who share a surname before that chain is built, and re-establish editions and fonds for each diocese.
- **`recipes/russian-imperial-service-record-recovery.md`** — Recover a pre-1917 official's formulary or service list through the employing institution's fond. *Guardrail:* do not stop at metrical books, revision lists or a military archive; search the employer, provincial and later-employer fonds, not only the first.
- **`recipes/school-university-record-recovery.md`** — Recover a pupil or student across school, educational-district, parallel-copy, yearbook and later-file layers. *Guardrail:* absence from a compiled or published list does not show that the person never attended.
- **`recipes/soviet-personal-file-recovery.md`** — Rebuild a Soviet-era life from institutional personal files when ZAGS or metrical records are lost. *Guardrail:* a negative archive reply is not a dead end; questionnaires and autobiographies are dated self-reports, and catalogue name hits are candidates.

### Censuses, tax, land and property

- **`recipes/canadian-census-interpretation.md`** — Read a historical Canadian census line as a de jure listing, and browse by geography when a name search misses. *Guardrail:* do not read a Canadian listing as a "present on census night" headcount.
- **`recipes/tax-roll-observation-workflow.md`** — Read town, township or county tax lists as a liability-bounded annual series for each jurisdiction and tax type. *Guardrail:* a first appearance, last appearance or gap is a bounded interval under that year's liability rules, not a birth, coming of age, move or death.
- **`recipes/deed-content-relationship-clues.md`** — Read a retrieved deed's type, consideration, estate terms, parties, court-bond security recitals and parcel for dated clues to heirship, probate, migration or land identity. *Guardrail:* every clue is a dated hypothesis with a stated corroboration need, never a kinship finding.
- **`recipes/us-federal-land-entry-file-recovery.md`** — Follow a GLO patent, bounty-land number or final-proof notice to the federal land-entry case file. *Guardrail:* the patent image is not the entry file, and a failed GLO name search does not prove that no claim existed.
- **`recipes/marks-and-brands-record-recovery.md`** — Carry a livestock marks-and-brands index entry to the actual registration or a described copy. *Guardrail:* read the index's own filing key before searching, since it can be the brand's initial rather than the owner's surname.

### Courts, legislatures, prisons and institutions

- **`recipes/court-case-file-recovery.md`** — Recover a U.S. civil, chancery, divorce, criminal or incapacity case file through the records that point to it, then inventory its loose papers. *Guardrail:* captions, arrests, index entries and case-law searches stay bounded leads.
- **`recipes/us-federal-court-case-file-recovery.md`** — Take a lead to the right federal court for the period, its National Archives record group and index, and the loose case file. *Guardrail:* decide whether the matter is federal before searching a county courthouse; a complete-index miss is a bounded negative that does not clear other relatives.
- **`recipes/criminal-court-prison-record-recovery.md`** — Find the trying court, its present custodian and the surviving prison series for a suspected arrest, trial or imprisonment. *Guardrail:* establish which court tried the case before searching, and weigh an inmate-list miss against other evidence.
- **`recipes/state-legislative-private-act-petitions.md`** — Recover a state legislative private act, such as a legitimation, name change, divorce or pension, and the petition behind it. *Guardrail:* do not stop at the one-line index or printed act, ignore entries at the same locator, or skip legislative records because the event looks like a county matter.
- **`recipes/illegitimacy-record-recovery.md`** — Find the bastardy bonds, court proceedings, support orders and church entries that a birth outside marriage could create, and preserve express status statements in apprenticeship instruments. *Guardrail:* do not decide illegitimacy from weak signals, and record allegations, not paternity.
- **`recipes/institutional-patient-record-recovery.md`** — Seek asylum or state-hospital records through the custodian, court and newspapers; in Dutch research, check a child's marriage papers and locally described admission correspondence. *Guardrail:* incapacity does not establish admission or diagnosis, and an access refusal does not establish that no file survives.

### U.S. military service

- **`recipes/us-military-service-type-record-routing.md`** — Route pre-1900 U.S. military service by service type to its own record series and custodian. *Guardrail:* a miss in federal compiled-service or pension indexes is not "no service", and an empty bounty-land search means nothing if the man was never eligible.
- **`recipes/us-civil-war-service-record-episodes.md`** — Read Civil War draft registration, service cards, roster remarks and unit events as separate episodes. *Guardrail:* registration is not service, the regiment's battles are not the soldier's, and a database miss does not prove non-service.
- **`recipes/us-20th-century-military-service-reconstruction.md`** — Rebuild a 20th-century U.S. Army or Air Force service record from records held outside a burned, thin or restricted personnel file, including state WWI questionnaires and Gold Star family packets. *Guardrail:* check the file's actual status before saying "it burned", and do not give the man his unit's events.

### Migration and origins

- **`recipes/immigrant-congregation-origin-records.md`** — Find an immigrant's hometown in the registers of U.S. congregations chosen by language community, dates and address. *Guardrail:* a miss at the nearest church or in an abstract's index is not absence, and one hometown statement is not proven identity.
- **`recipes/surname-distribution-locality-leads.md`** — Rank localities to search from dated surname-distribution sources for an uncommon surname. *Guardrail:* the result is a bounded search list, never an origin finding.
- **`recipes/us-freedpeople-record-recovery.md`** — Trace an African American family back across the 1870 boundary. *Guardrail:* test free versus enslaved status first; a surname, enslaver, list order or DNA signal stays a hypothesis until a record names the person.
- **`recipes/chinese-lineage-jiapu-records.md`** — Recover a Chinese emigrant's character-written name and ancestral village before searching lineage genealogies (jiapu). *Guardrail:* never derive a character from a romanization, and keep each romanization, port and generation-character match as its own observation.
- **`recipes/japanese-koseki-honseki-recovery.md`** — Recover the kanji name and full historical domicile (honseki) before requesting a Japanese family register (koseki). *Guardrail:* a romanized name or remembered region is not enough for a request, and a passenger-list hit is a candidate, not an identity.

### Places, maps, libraries and manuscripts

- **`recipes/historical-place-name-resolution.md`** — Resolve a place named in a record, letter, Bible or biography to dated, same-named candidates from period gazetteers. *Guardrail:* do not default to the well-known namesake; keep the name as written and let other dated evidence choose.
- **`recipes/historical-map-record-recovery.md`** — Read a fire-insurance sheet, atlas, plat, quadrangle or overlay as a dated observation; trace a detached archival map toward its possible originating case. *Guardrail:* a candidate case link or estimated map date does not establish the depicted event or a same-named person's identity.
- **`recipes/published-book-catalogue-and-full-text-discovery.md`** — Find a published local history, compiled genealogy or family book across catalogues and full text. *Guardrail:* a metadata search miss never establishes that a book does not exist or is not held; record what each tool covered.
- **`recipes/periodical-index-search-retrieval.md`** — Search a genealogical periodical index such as PERSI and retrieve the article. *Guardrail:* these indexes are not full text, so a personal-name miss usually means the article text was never searched, and a hit is only a citation.
- **`recipes/manuscript-collection-recovery.md`** — Find personal, family and organisational papers by context, alternate ledger/daybook labels and an established society's personal-name index; request linked account pages or a complete claim folder with earlier applications. *Guardrail:* a name-search miss is not absence, and one reported packet does not guarantee standard contents or a current copy route.
- **`recipes/local-repository-uncatalogued-holdings.md`** — Ask a local library, society or archive about its uncatalogued holdings after its catalogue returns nothing. *Guardrail:* an empty catalogue search leaves the uncatalogued holdings uninspected, so it is not a negative.

### Family papers, photographs and oral history

- **`recipes/family-collection-intake-and-capture.md`** — Take in, inventory, plan the capture of and hand over an inherited family collection of boxes, albums, loose photographs, papers or existing scans. *Guardrail:* do not optimize for tidy files; renaming, re-ordering, front-only scans or treating a crop as the master destroys the holder, order and reverse evidence.
- **`recipes/family-photograph-attribution-and-dating.md`** — Attribute and date an inherited family photograph from captions, provenance and the photographer's imprint. *Guardrail:* never compare faces or name anyone by appearance; record each identification as an attributed claim, test it against the named person's documented lifetime, and turn each date clue into a bound.
- **`recipes/family-papers-and-bible-register-dating.md`** — Separate writing, mailing and event dates in letters, envelopes, address books, family Bible registers and inscribed books. *Guardrail:* a postmark or return address records a mailing or an address, not the event; assess each Bible entry's writing occasion, near the event or copied later, separately from its stated event date.
- **`recipes/family-interviews-and-oral-tradition.md`** — Record an interview with a relative, a supplied recording or an inherited story with its speaker, prompter and chain of transmission. *Guardrail:* do not turn a recollection straight into tree facts; keep the prompter's details apart from the speaker's, an uncertain name uncertain, and each relay in the chain as its own witness.
- **`recipes/repository-photograph-collection-search.md`** — Search repository photograph collections for an ancestor, home, shop or community by place and subject. *Guardrail:* never compare faces or name anyone by appearance, and record a recognition by the user or a relative as that person's attributed claim; a name-search miss does not show that no image exists, and a donor caption or added geotag is not a settled identification or location.

### DNA workflows and research planning

- **`recipes/admixture-model-run-scope.md`** — Record the run scope of a G25, calculator or qpAdm admixture result before reading it. *Guardrail:* check fit and scope before reading proportions, and never rank runs across calculators.
- **`recipes/dna-match-outreach-staging.md`** — Stage and draft outreach to a DNA match, a match's account manager or an untested relative. *Guardrail:* when the tester's consent is missing or unclear, prepare only a contact plan and a draft for the tester's own review, and do not choose recipients or send anything. In every case, never announce a suspected relationship, and log silence as silence, not refusal.
- **`recipes/descendancy-gap-worklist.md`** — Turn "research the descendants" into a ranked list of gaps tied to the records each lifespan crosses. *Guardrail:* an empty tree field leaves the event unresolved; it does not mean the event never happened.

## Supporting references

- [Research log and report](recipes/research-documentation.md) preserves searches, document
  numbers, results and the analysis needed to resume an emigrant-origin investigation.
- [Source citation record](recipes/source-citation.md) preserves repository, collection,
  archive/film identifiers, item locators, images and access dates for each observation.

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
Third-party facts and methods are credited in each recipe's `sources/<slug>.md`; any
reproduced third-party data is carved out in `NOTICE`.
