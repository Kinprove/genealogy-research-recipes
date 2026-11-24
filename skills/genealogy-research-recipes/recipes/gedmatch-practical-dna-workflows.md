---
id: "gedmatch-practical-dna-workflows"
title: "Working reproducibly with GEDmatch"
summary: "Work reproducibly in GEDmatch: kit baselines, one-to-one checks, segment search, tag groups, triangulation, phasing and Lazarus kits."
kind: "platform"
scope: {"platforms": ["gedmatch"], "tasks": ["GEDmatch One-to-Many, One-to-One, match-both, Segment Search, tag groups, Multiple Kit Analysis, Triangulation, parental phasing or Lazarus reconstruction.", "GEDmatch Superkit, overlap cutoffs, endogamy thresholds and GEDCOM or MRCA tree comparison."]}
privacy: "genetic-third-party"
gates: ["privacy-transfer"]
guardrails: [{"id": "GEDMATCH-PRACTICAL-DNA-WORKFLOWS-01", "text": "A match-list row, a pairwise segment, a shared-match list, a triangulation result and a generated kit answer different questions. Keep their tool, inputs and settings attached to every result."}, {"id": "GM-01", "text": "Authorization to analyze a kit is not permission to upload it."}, {"id": "GM-02", "text": "require that person's explicit permission for GEDmatch and the chosen option."}, {"id": "GM-03", "text": "For an upload request, make the gate explicit in the first reply: ask whether the file is the user's own test or someone else's, distinguish permission to access or analyze it from permission to transfer it, and ask about permission for GEDmatch and the chosen visibility and law-enforcement matching options."}]
handoff: ["ai-for-dna-research", "dna-comparison-controls", "evidence-proof-judgment", "unknown-parentage-wato", "xdna-phasing-judgment"]
checked: "2026-11-12"
checked_basis: "Rechecked 2026-11-12"
capabilities: {"browse": ["gedmatch"], "local_script": [], "extensions": [], "data_transfer": ["export", "link", "third-party-tool", "upload"], "contact": []}
router: {"section": "DNA", "group": "DNA testing sites and tools", "order": 31}
---

# Recipe: Working reproducibly with GEDmatch

## Contents

- Goal
- The failure to prevent
- Before starting
- Eight workflows
- Compare trees through GEDCOMs
- Hand off interpretation

## Goal

Run GEDmatch comparisons, targeted segment searches, triangulation, parental phasing and Lazarus
reconstruction with enough recorded information to repeat the analysis. Each workflow produces
an artifact and a completion check. Examples and field schemas are original synthesis; example
kit handles are fictional.

## The failure to prevent

A match-list row, a pairwise segment, a shared-match list, a triangulation result and a generated
kit answer different questions. Keep their tool, inputs and settings attached to every result.
Report an absent row as absent from that particular run. A generated kit remains a generated
kit, even when GEDmatch assigns it a normal-looking kit number.

## Before starting

Use kits you are authorized to analyze and keep kit identifiers, contact details and raw files
in the private working dataset. Find each named tool in the current account; capture its actual
controls and access requirements. Tutorials below describe historical interfaces. An unavailable
tool is an access limitation, not a completed comparison. Do not substitute remembered default
thresholds, match limits, kit prefixes or processing times for what the current screen reports.

Plan for paid tools before the session. GEDmatch's Tier 1 help lists Segment Search, the Phasing
tool and Lazarus among the paid Tier 1 tools. It says tools marked "Tier 1" on the home page
require a paid membership, and it lists One-to-Many and One-to-One as free [H9 @2026-11-12].
GEDmatch's 2025 upload guide lists Matching Segment Search, Triangulation and Multiple Kit
Analysis among its paid tools [H1 @2026-11-12], and GEDmatch's triangulation tutorial opens
Triangulation from the Tier 1 tools, not the free ones [H4 @2026-11-12]. Check the home-page
marking for those three before planning workflows 4–8.

**Privacy gate before any upload:** Authorization to analyze a kit is not permission to
upload it. An upload places that person's genome in GEDmatch, where the kit's settings decide who
can match and see it. Before each upload, answer the privacy gate in `SKILL.md`: record the
tested person, the file and the privacy option the upload form currently offers, with what
GEDmatch's current terms say each option allows for law-enforcement matching (the uploader
chooses an option at upload [H11]; read the terms rather than assuming an opt-out excludes
every law-enforcement comparison), and require that person's explicit permission for GEDmatch
and the chosen option. If permission is unclear,
do not upload. Apply the consent rules in
[AI for DNA research](ai-for-dna-research.md#verification--privacy-discipline).

For an upload request, make the gate explicit in the first reply: ask whether the file
is the user's own test or someone else's, distinguish permission to access or analyze
it from permission to transfer it, and ask about permission for GEDmatch and the chosen
visibility and law-enforcement matching options. Before drafting that reply, read the linked
**Verification & privacy discipline** section for its rules on consent and de-identification.
Identify those controls as items to inspect on the current form; do not claim to have
checked them from a tutorial. Until
the answers establish informed permission, stop at these questions and a plan to inspect
the controls before giving executable upload steps.

Use separate workflows for general spreadsheet export and cluster construction. This recipe
owns the GEDmatch run and comparison records.

Before using another service's result as confirmation or exclusion, apply
[DNA comparison controls](dna-comparison-controls.md) to exact-test identity,
query controls, local marker coverage and reporting scope.

## Eight workflows

### 1. Establish a kit registry and a comparable run baseline

1. **Privacy gate:** <!-- privacy-gate: upload --> Upload a kit only after the privacy gate in
   `SKILL.md`, as the checkpoint in "Before starting" describes. Record each kit's tested person,
   testing source and whether it is measured, phased or reconstructed. Keep multiple tests of one
   person as separate kit records. Preserve the original download and the upload receipt; use
   the vendor's current upload instructions. [H1]
2. Record the readiness state actually shown. GEDmatch's help says a kit must finish processing,
   "typically 24–48 hours after upload", before its matching tools work; use that only to plan
   the session, and let the status shown decide. [H10] After processing, use a known relative as a
   comparison control. Save its baseline One-to-One result rather than treating an upload
   receipt as evidence that matching is ready. [H2]
3. Start a run record before every subsequent workflow. Capture the precise tool name/version
   shown, input kit numbers, displayed coordinate build, cM/SNP thresholds, match-count cap,
   chromosome/window filters, exclusions and other changed options. Mark controls the tool
   does not expose as `not exposed`; save the parameter screen with the result.

After the upload checkpoint above, send the tester's existing AncestryDNA autosomal raw data
file to GEDmatch [H20 @2026-09-27] for cross-company matching, as the presenter suggests in the
supplied, unverified transcript excerpt [S31† @2026-09-27]. Once the kit is ready, run One-to-Many
Limited and record the search scope as kits uploaded to GEDmatch, including kits from other
testing services [H3 @2026-09-27], [H20 @2026-09-27].

GEDmatch offers free upload of an existing AncestryDNA file [H21 @2026-09-27] and free basic
matching in One-to-Many Limited [H3 @2026-09-27].

Never combine raw files from different people into one uploaded kit. A merged file can carry
more than two alleles at a position, so the matcher may report sharing that no single genome
supports. Coverage gained this way is not a measured relationship. Combine only one person's own
tests, and register the result as a derived kit that lists every source file. Represent an
untested person through workflows 7–8 and keep the role label. When one person has several
uploads, record which kit is active for matching and which are held aside, and name the active
kit as that person's baseline. In the cited interview, several active uploads could produce repeated
kit rows for one tester; verify the current matching controls and the rows actually returned. Match lists can also differ by source, so record the kit actually used in
every run. The [sibling walkthrough](https://www.youtube.com/watch?v=-C6gmmx8nr0) and
[interview answer](https://www.youtube.com/watch?v=zvZhuusSROY) motivate this. Current upload
validation, and the matching setting's name and effect, remain unverified.

**Privacy gate:** <!-- privacy-gate: upload --> A Superkit is a new kit of one person's genome in
GEDmatch's database: generate it only after the privacy gate in `SKILL.md`, with that person's
explicit permission for the Superkit and its privacy option, exactly as for an upload.
GEDmatch's own route for combining one person's tests is the Tier 1 tool "Combine multiple kits
into 1 Superkit", which its help scopes to results from different testing companies for the same
individual [H9 @2026-11-19], [H15 @2026-11-19]. Never select another
person's kit as an input. Register the Superkit as derived with its source kits, and name one kit
as the active baseline, as above. Compare the candidate separately with the source kit and the
Superkit. Record the SNP overlap, shared cM and segments for each run. In GEDmatch's tutorial,
one match went from roughly 194,000 comparable SNPs to almost 400,000 with identical shared cM.
Another went from 12.40 to about 21.60 cM [H19 @2026-11-19]. A kit can add comparable positions
across testing companies [S26 @2026-11-19]. Report the measured change for this pair.

When parental relatedness affects the interpretation, run the parental-relatedness check on the
relevant selected kit and store the result, its thresholds, the output it reports and its
limitations in the kit registry. The check reads only that tester's own data, so no parent kit is
required. Do not copy this kit's detected-run result to another relative; interpret its relevance
through documented shared parents, and retain each kit's own detection limits. Interpreting any run
of shared material belongs to `xdna-phasing-judgment.md` and the endogamy guidance in
`ai-for-dna-research.md`. The
[presenter's tool-order walkthrough](https://www.youtube.com/watch?v=PBL_T2TY93U) motivates the
per-kit step.

If an authorized, available lookup tool accepts a retained exact kit ID, email or GEDCOM
ID, query that key and record its type and the actual lookup scope. Preserve the returned
aliases, associated kits/GEDCOMs and manager roles the comparison needs; do not copy contact
details beyond what the kit already shows to matches (Living people, in `SKILL.md`). One
email's kits need not represent one tested person. Verify tested-kit provenance separately before comparison.
Keep an empty, inaccessible or unavailable lookup unresolved under its observed scope;
it does not establish that a person or kit does not exist.

Historical example: Family History Fanatics, [User Lookup](https://www.youtube.com/watch?v=1QMQ9EgJcK0)
(2019-04-16), demonstrating Genesis; current tool, field and visibility behavior remain unverified.

When inspecting a supplied combined AutoKinship report, record which component reports
actually have results. Keep each group label with its run and report type: an AutoCluster
number and an AutoSegment number identify different groups, even when the numbers match.
Preserve every reported membership for a kit rather than forcing one group per person.
An AutoSegment member may lack AutoCluster membership in that report. In Estes's report,
AutoCluster 136 contained five segment clusters. Bill appeared in only one of them, AutoSegment
185 on chromosome 3 [S19]. Record the component, group and kit together when following a match.

For a crosswalk, retain `run_id, report_type, reported_group, kit_id, membership, result_ref`
and any supplied interval fields. Link entries through verified kit identities while retaining
each report's original labels and scope; an unresolved identity or unavailable component stays
unresolved. The crosswalk records tool output, not an ancestral assignment, a validated
predicted tree or a checked triangulation result. Use the later comparison workflows for
the pairwise evidence actually needed. This register is synthesis, not an import format. [S19]

**Artifact:** private kit registry: `kit_id, person_handle, source, kit_type, input_kits,
upload_receipt, readiness, baseline_run_id`. Run manifest: `run_id, retrieved_at, tool_label,
input_kits, build, cm_min, snp_min, match_cap, chromosome, window_start, window_end, exclusions,
other_options, parameter_capture, result_file, row_count, outcome`.

**Complete when:** each used kit has an identified origin and readiness observation, and the
known-relative control has a saved result. Record unavailable controls explicitly.

### 2. Follow a One-to-Many candidate into One-to-One

1. Run One-to-Many for the focal kit and preserve the candidate row, including the match kit,
   total/longest-segment values, source and reported overlap when present. Use kit IDs as keys;
   display names are labels. [H3]
2. **Privacy gate:** <!-- privacy-gate: export --> The saved table holds a living match's segment
   data; keep it on the user's device and delete it when the question is answered, as the
   privacy gate in `SKILL.md` says. Open the candidate's direct comparison, or enter the two kit
   IDs into One-to-One. Save the position table and, when useful, the graphics. Historical tutorials demonstrate using the
   match-list link to prefill the pair and a positions-only view for copying. [S1, H2]
3. Record every reported segment: kit pair, chromosome, start/end, cM and SNP count, with its
   run ID. Keep X comparisons in separately labeled rows.
4. When reports disagree, first verify the kit pair, exact tool/algorithm label, build, thresholds,
   segment-splitting options (hard-break prevention, mismatch bunching), match-list scope and
   readiness. Re-run with comparable exposed controls; retain both original reports. Do not lower
   the threshold simply to recover a desired match.

Before following a candidate, read the focal kit's whole match-list profile. When a kit returns
many rows with large shared totals whose longest segments stay small, open several of its top
matches' own One-to-Many lists. If those show no comparable inflation, mark the kit
`profile anomalous` and do not convert its totals into relationships. Record each kit's vendor
and export format with the observation. An
[anomalous match-list thread](https://forum.molgen.org/index.php/topic,14468.0.html) and a
[vendor-upload discussion](https://forum.molgen.org/index.php/topic,10116.0.html) motivate the
check. Neither establishes a cause (population background, chip or file artifact, or altered
data) or sets any threshold, and neither verifies which vendors' files are unsuitable.

If the top matches' own lists show the same inflation, or the tester's ancestry comes from a
documented intermarrying community, read each row's largest segment beside its total. A large total
made of small segments, with a small largest segment, is a recognized sign of endogamy and does not
support the close relationship the total alone suggests [S28 @2026-11-19]. Keep the default run.
Where the current form offers a minimum-segment setting, re-run One-to-Many with a higher minimum
as a separate recorded run. GEDmatch's 2026 guide describes the minimum as typically 7 cM,
recommends adjusting it when endogamy is suspected and gives 10–15 cM as a raised setting
[H17 @2026-11-19]. Legacy Tree recommends recalculating totals at GEDmatch under higher thresholds
and comparing the results [S30 @2026-11-19]. Cooper used 12 cM in an endogamy search
[S26 @2026-11-19]. Keep both runs and compare the largest segment with the total for the
surviving candidates. Multiple distant relationships can inflate the total. Use the endogamy
guidance in `ai-for-dna-research.md` before assigning a relationship.

Keep every displayed match-list column as reported, but mark any estimated generation or
relationship column as derived from the shared total. A derived value is not a second
observation. Do not add it to the cM figure as corroboration, and do not convert it into a cousin
level by a fixed offset, because one total is consistent with several relationship ranges. Record
the total and let `ai-for-dna-research.md` and `unknown-parentage-wato.md` handle relationship
ranges. The [presenter's analysis of the generation column](https://www.youtube.com/watch?v=V9hvINBzZmc)
motivates this; his plotted figures are his own and are not reproduced here.

When the question turns on identity state rather than amount, also record whether each reported
region is half-identical or fully identical, and which tool reported it. Sibling-type questions
whose totals fall in an overlapping relationship range depend on this state. A segment list of cM
and SNP counts cannot supply it, and vendor exports may omit it. The
[presenter's sibling answer](https://www.youtube.com/watch?v=U27k4R4rUkY) motivates recording the
state. It does not set any threshold for how much fully identical material a relationship
requires. Send the recorded regions to `ai-for-dna-research.md` (its fully-identical-regions step) for the
relationship assessment.

To see identity state at GEDmatch, use One-to-One with graphics. Practitioner guides describe its
green bars as DNA identical on both copies of the chromosome and yellow bars as identical on one
copy [S21 @2026-11-12], [S22 @2026-11-12]. Estes (2023) names GEDmatch and 23andMe as the services that show it, not
FamilyTreeDNA, MyHeritage or AncestryDNA; a 2019 overview likewise names only 23andMe and GEDmatch
[S21 @2026-11-12], [S23 @2026-11-12]. For a pair tested at those other companies, the GEDmatch graphic is therefore the
view to use. Long green runs point to DNA shared through both parents, but small scattered green
spots also occur between half siblings: a few green spots are not evidence of full siblingship
[S21 @2026-11-12], [S22 @2026-11-12].

Where a match list reports an overlap figure, record it per row with each kit's testing source and
version. Overlap describes which positions both kits were assayed at, not shared ancestry. Keep a
missing or NA overlap value as unexplained, not as zero overlap or as evidence of no
relationship. Separately, a One-to-One shared-SNP percentage is not evidence of relatedness or
ancestry: unrelated pairs commonly show similar percentages. If you cite one, record an
unrelated-pair comparison under the same settings as a baseline and rely on the reported
segments. The [overlap discussion](https://www.youtube.com/watch?v=Ypfn6mzRbOc) and
[ancient-sample answer](https://www.youtube.com/watch?v=GEc8JVzCX5o) motivate this. Neither sets a
threshold or an expected range, or explains why values are missing.

Record the overlap cutoff each One-to-Many run applied and whether a row's overlap is
colour-flagged. GEDmatch's One-to-Many page says a pink overlap value may indicate a less accurate
match [H3 @2026-11-19]. Its tutorials raise the cutoff to drop low-overlap kits and list a
changeable cutoff among the Tier 1 features [H16 @2026-11-19], [H18 @2026-11-19]. A 2022 guide
advises against ignoring low-overlap matches outright [S29 @2026-11-19]. Cooper cautions that
overlap under 100,000 SNPs can be less accurate [S26 @2026-11-19]. Treat that as her caution.
GEDmatch's cited guides do not establish it as a cutoff. Check each flagged row in One-to-One
before relying on the total, and keep the flag in the ledger.

**Artifact:** candidate-to-comparison ledger: `candidate_run_id, pair_run_id, kit_a, kit_b,
chromosome, start, end, cm, snps, comparison_type, status, discrepancy_reason`.

**Complete when:** each investigated candidate has a saved direct result, an explicit
`no segment reported under these settings`, or `unavailable`. A blank ledger cell is unfinished.

### 3. Turn a match-both lead into a checked three-kit comparison

1. **Privacy gate:** <!-- privacy-gate: export --> The membership list names living testers;
   keep it on the user's device and delete it when the question is answered, as the privacy
   gate in `SKILL.md` says. Use the current match-one-or-both/shared-match tool to collect
   candidate C for focal kits A and B. Save that run's settings and the original membership
   list. [S2]
2. Run A–B, A–C and B–C One-to-One comparisons. The membership list does not supply the
   three chromosome-level results. [S3, H4]
3. For intervals on the same chromosome and coordinate build, record their common core:
   `core_start = max(pair_starts)` and `core_end = min(pair_ends)`. Require a nonempty interval
   in all three saved comparisons. Compute base-pair overlap only; do not convert its fraction
   into a guessed cM value or claim that a segment threshold applies to the core itself.
4. Record the status as `three pairwise intervals overlap`, `no common core`, `pair missing`
   or `unavailable`. Send the measured intervals to the interpretation recipe before assigning
   an ancestor. [H4]

The match-both tool's two cM thresholds, for the largest segment and for the total, decide which
people qualify as matches; they do not remove individual segments, and both were described at a
10 cM default in 2021 and 2022 (Brons, Who Are You Made Of?, last updated 2021-04-20 [S24];
Kessler, Behold Blog, 2022-11-12 [S25]). Do not lower them to equal a segment-level setting in a
later tool, such as Double Match Triangulator's 7 and 15 cM segment limits: those apply to
segments, so the two need not match [S25]. Lowering the largest-segment threshold only admits more
people whose best segment is small; with endogamy, or a long shared-match list, raise it instead
[S24], [S25].

When overlapping matches fall into two ancestral groups, tabulate the start and end positions
from every pair's comparison table and record the testing source for each kit. In one worked
case the presenter compared exact endpoints between groups that looked similar on the graphic
[S10]. Different chips can shift reported boundaries. A shared start is a reason to check the
actual overlap and all pairs. It cannot identify a parental side or a common ancestor.

**Artifact:** triplet table: `kit_a, kit_b, kit_c, ab_run, ac_run, bc_run, chromosome, build,
pair_intervals, core_start, core_end, status, interpretation_ref`.

**Complete when:** all three pair results and the common-core check are present. An unchecked
B–C comparison cannot be replaced by two overlaps with A.

### 4. Search one locus, then investigate the overlapping candidates

1. Choose a saved segment, then enter its focal kit, chromosome and coordinate window in
   Segment Search. Capture the display build, match cap, thresholds and exclusions shown. [H5]
2. **Privacy gate:** <!-- privacy-gate: export --> Segment Search results list living matches'
   kits and segments; keep them on the user's device and delete them when the question is
   answered, as the privacy gate in `SKILL.md` says. Save the returned CSV when offered;
   otherwise preserve the table and report with their run manifest. Treat every returned interval as a candidate: the search can return a segment
   that overlaps only part of the requested window. Its display color is not a pairwise test. [H5]
3. Sort by chromosome/start/end and record the actual overlap with the target window. Select
   useful candidates for Multiple Kit Analysis or workflow 3; retain the selection list. [H5]
4. If a known direct match is absent, check the run's cap, exclusions, thresholds and tool label
   against its saved One-to-One result. Compare that exact pair again. Keep an unresolved
   absence as `not returned by this search`, with both run IDs.

**Artifact:** locus-search ledger: `search_run_id, focal_kit, chromosome, build, target_start,
target_end, match_kit, returned_start, returned_end, overlap_start, overlap_end, followup_run_id,
status`.

**Complete when:** the search scope and output are preserved and every selected candidate has
its follow-up result or explicit access limitation. Do not call a bounded search exhaustive.

### 5. Freeze a tag group before Multiple Kit Analysis

1. Create a tag group for a specific comparison question, or select a fixed kit subset from a
   result table. Record the exact roster in its displayed order and mark its first kit: several
   group tools compare every kit only to that first kit, while others compare all pairs. A color
   or group name alone does not preserve the roster. [S4, H7]
2. Open Multiple Kit Analysis for that roster. Capture the autosomal matrix and, for
   cross-source comparisons, the SNP-overlap matrix. These report shared-DNA amounts and
   common assayed-marker counts respectively; neither replaces chromosome-level pair results.
   Save row/column kit identities with the matrix. [H6]
3. Use the group's chromosome/segment views to select direct pairwise checks. Its Segment
   Search is restricted to the group rather than the broader search roster. Record that scope
   difference before comparing results with workflow 4. [H7]
4. If the group changes, give the new roster a revision and preserve the old matrix. Re-run the
   affected comparison rather than pasting fresh cells into an older snapshot.

**Artifact:** group manifest: `group_id, roster_revision, kit_ids, selection_basis, created_at,
matrix_run_ids, segment_run_ids`. Matrix cells retain `row_kit, column_kit, value, metric,
run_id`; missing/unavailable cells remain explicit.

**Complete when:** the saved matrix has a fixed identifiable roster, labeled metrics and a
recorded scope. A matrix cluster remains a lead for pairwise investigation.

### 6. Preserve and check a triangulation run

1. Enter the focal kit in Triangulation. Capture the maximum kit count, upper close-match
   cutoff, minimum segment setting, chromosome, build and cross-matching option actually used.
   Start with one chromosome when investigating a specific interval. [H4]
2. Decide explicitly whether close relatives belong in this run. Excluding them can reduce
   repetitive groups; retaining a documented side-specific relative serves a different question.
   Save the chosen cutoff and excluded roster where available. A tutorial's cutoff does not
   reliably exclude every member of a relationship category. [H4]
3. Preserve the original result rows and grouping display. For a triplet you intend to use,
   collect the three direct pair results through workflow 3. Before treating a larger set as
   one all-pairs group on a common core, check every unordered pair on that core; connected
   triplets and similar coordinates alone do not establish that property. [S3, H4]
4. Store a candidate ancestral path separately from the tool result. Naming the ancestor
   requires the documented pedigrees and interpretation review.

**Artifact:** triangulation ledger: `triangulation_run_id, focal_kit, group_label, member_kits,
chromosome, build, reported_interval, checked_pair_run_ids, common_core, unchecked_pairs,
candidate_path_ref, status`.

**Complete when:** the claimed group property is supported by the saved pair checks; otherwise
retain only the verified triplets and label the larger set `partially checked`.

### 7. Make a parental-phasing experiment reproducible

1. Supply the child and its actual tested parent(s) to the current Phasing tool. Identify the
   parent roles from the input pedigree and tool output. Save the submitted form and generated
   kit IDs; do not infer the roles from a remembered prefix convention. [S5, S6]
2. Register each output as `phased`, with the input kits and parent role attached. The output
   represents an inferred parental contribution to that child, not a measured full parental kit.
   Keep the original child's kit as the comparison baseline. [S5]
3. Compare the original and generated kits against documented relatives from each parental
   side using recorded One-to-One settings. Preserve missing and contradictory results along
   with positive ones; send them to `xdna-phasing-judgment.md` for assessment. [S6]

**Artifact:** phasing experiment: `experiment_id, child_kit, maternal_input, paternal_input,
tool_options, output_kit, output_role, baseline_run, control_kit, documented_side,
output_comparison_run, observed_result, unresolved_issue`.

**Complete when:** every generated ID has its inputs and role, plus saved control comparisons
or an explicit `no independent control available` limitation. Generating an ID alone does not
validate the phased data.

### 8. Trial a Lazarus reconstruction with an input-group ledger

1. Choose the target and list documented relationships for every proposed input. In the
   demonstrated Lazarus grouping, group 1 contains descendants; group 2 contains relatives of
   the target who are not descendants; optional group 0 contains the spouse or relatives of that
   spouse unrelated to the target, to remove spouse-side contributions. Verify the current
   form's group definitions before entry. Do not populate a group by matching surname alone. [H8]
2. Select descendants from distinct available branches. A tested child already carries what
   that child's children inherited from the target; grandchildren help cover a branch whose
   relevant parent is unavailable. Log every input's branch and any additional relationship. [H8]
3. Run the trial mode first, when offered. Save inputs, sex/X setting, thresholds, processing
   choice and coverage report, and save every result table when it is generated: the demonstrated
   tool did not show them again. Revise one input or setting at a time, starting each revision
   from the downloadable input file when offered, and preserve each run. Coverage describes
   reconstruction output, not its accuracy. [H8]
4. Use a tested target, when available for a control experiment, or reserve a documented relative
   outside the construction inputs for comparison. Record what that control can check; sharing
   a segment with one held-out relative does not validate the whole kit. Without a control,
   mark the output `unvalidated`. Register it as `reconstructed` and review genotype quality
   through `xdna-phasing-judgment.md` before using it as research evidence.

**Artifact:** reconstruction ledger: `experiment_id, target_handle, input_kit, group,
documented_relationship, branch, additional_paths, settings_capture, trial_run, coverage_report,
output_kit, validation_control, validation_run, validation_status`.

**Complete when:** each input has a justified role, the trial is preserved and validation limits
are stated. Full database processing requires a separate explicit decision by the kit manager;
the recipe does not change anyone's kit visibility or permissions.

## Compare trees through GEDCOMs

A tree comparison proposes a common ancestor for a DNA match; it does not test one. Use these
steps to make the proposal and then test it.

1. **Privacy gate:** <!-- privacy-gate: upload, link --> A GEDCOM upload places a family tree, linked to
   a tested person's kit, on GEDmatch, where other users' tree tools search it [H12 @2026-11-19].
   Before uploading, answer the privacy gate in `SKILL.md` for the tree's living people and the
   linked tester. Export ancestors only, as Cooper recommends [S26 @2026-11-19].
   Remove anyone who may be living unless that person permits the upload.
   GEDmatch's help says people marked living are hidden from everyone except the GEDCOM's owner,
   and that the upload takes a plain-text `.ged` file [H14 @2026-11-19]; hidden people's data
   still leaves the user's device. Record the GEDCOM number assigned and the kit linked to the tested person's place in the tree;
   the common-ancestor search needs that link [S27 @2026-11-19].
2. Choose the tool for the question and record its inputs. GEDmatch's tutorial describes a
   two-GEDCOM comparison that takes two GEDCOM numbers and checks only those trees, a search of one
   GEDCOM against all uploaded GEDCOMs, and GEDCOM + DNA matches, which limits a kit's match list
   to matches with an attached tree [H12 @2026-11-19]. Its most-recent-common-ancestor (MRCA) tool
   searches the trees of a kit's DNA matches and takes the number of kits searched, a minimum cM
   and a match score [H13 @2026-11-19]. A 2022 guide calls that search a Tier 1 tool
   [S27 @2026-11-19]. Cooper also described the pairwise comparison and the subscriber search
   across matches' trees [S26 @2026-11-19]. Check the current home-page marking.
3. **Privacy gate:** <!-- privacy-gate: export --> The MRCA result lists living matches' kit
   numbers, names and email addresses [S27 @2026-11-19]. Keep it on the user's device, do not
   copy match email addresses into the research record (Living people, in `SKILL.md`), and delete
   it when the question is answered, as the privacy gate in `SKILL.md` says. Save each run's tool,
   GEDCOM numbers, linked kit, kit count, minimum cM and match score with the result.
4. Compare a proposed ancestor's birth date, birthplace and relatives in both trees. In the
   GEDmatch tutorial, a pair sharing 35 cM returned the same ancestor name but the birth date
   and birthplace differed [H13]. Keep the candidates separate until records link them. Even
   a documented common ancestor may represent only one of several relationships [S27]. Check
   the pair in One-to-One and verify every generation on both paths. In another single-segment
   case, Cooper's tree comparison reached thirteenth-century Norway. She suspected a closer
   undocumented connection [S26]. Leave the segment's source unresolved and send competing
   paths to `evidence-proof-judgment.md`.

**Artifact:** tree-comparison ledger: `run_id, tool_label, gedcom_a, gedcom_b, linked_kit,
match_kit, settings, candidate_ancestor, generations_a, generations_b, match_score, pair_run_id,
path_check, status`.

**Complete when:** each candidate ancestor has a saved pair result from workflow 2 and a checked
documentary path, or is marked `tree overlap only`. A returned name is not a confirmed common
ancestor.

## Hand off interpretation

Use `genealogy-research-recipes` → `xdna-phasing-judgment.md` for segment trust, triangulation, X,
phasing and reconstructed-kit quality; `ai-for-dna-research.md` for endogamy, multiple descent
paths and selecting relatives; `unknown-parentage-wato.md` for placement hypotheses; and
`evidence-proof-judgment.md` for documentary identity and conclusions. Pass the preserved
run records with those requests.

**Privacy gate before painting:** <!-- privacy-gate: third-party-tool --> The measurements carry other testers' segment data. Before
passing them to DNA Painter, answer the privacy gate in `SKILL.md`: require
explicit permission covering this action, this destination and each person's data, and strip
identifiers the map does not need, as
[AI for DNA research](ai-for-dna-research.md#verification--privacy-discipline) requires. If
permission is unclear, keep the measurements in the local run records. With that permission, pass
verified measurements to the painting workflow in DNA Painter.
