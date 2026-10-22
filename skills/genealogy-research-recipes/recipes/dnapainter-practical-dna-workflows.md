# Recipe: Practical DNA Painter maps, matrices and tree worklists

## Goal

Build a reusable chromosome-map packet and perform the right operation on it: paint an observed match, move existing data, intersect inherited intervals, infer missing intervals, combine overlapping coordinates, or plan another descendant's test. Use a direct-ancestor tree separately when the next task is to inspect pedigree gaps or repeated paths. Use a numeric tester-pair matrix to audit sourced shared amounts beside documented relationships. Use Shared cM histograms and a two-value range screen to inspect sourced pair amounts.

The failure to prevent is treating everything DNA Painter draws or calculates as an observed match. A copied segment belongs to its original comparison; an intersection is coordinate geometry; an inferred interval is a deduction; the Coverage Estimator is a pedigree-based estimate. Keep those outputs distinguishable.

## Inputs and routing

Use a named focal tester, authorized segment tables, known relatives and a specific question. A segment table needs chromosome and start/end positions; retain reported cM and SNP counts when available. Raw genotype files and a match's total cM alone are not chromosome-painting inputs. [S1, S2]

For the ancestral-tree workflow, use a named root and an authorized pedigree or GEDCOM; it does not require segment data.

For the numeric-matrix workflow, use identified tester pairs, sourced shared cM amounts and
separate relationship evidence. An ICW cluster membership or pasted list of names supplies
no missing pairwise amount.

Provider download procedures belong to the relevant provider's documentation; provider investigation belongs to its own recipe. For segment validity, triangulation, X-DNA and phasing judgment use [X-DNA and phasing judgment](../../genealogy-research-recipes/recipes/xdna-phasing-judgment.md). For unknown-person placement use [Unknown parentage and WATO](../../genealogy-research-recipes/recipes/unknown-parentage-wato.md). This recipe owns the subsequent DNA Painter operations.

Keep a small operation register beside the map:

| Field | Record |
| --- | --- |
| Operation | Paint, copy, intersect, subtract, union, coverage estimate, cluster annotation, ancestor-gap worklist, numeric-pair audit or Shared cM histogram/range screen |
| People | Focal tester and both members of each source comparison |
| Inputs | Saved tables, provider, retrieval date, genome build and filters |
| Assignment | Maternal/paternal/unknown and named ancestor, couple or provisional group |
| Output | Saved map, tree or matrix, exported table and notes |
| Status | Observed coordinates or amounts, inferred assignment, planning estimate or documentary worklist |

This register is a recommended research artifact; it is not a DNA Painter import format. A person's map is a container for research about that person's chromosomes. Do not reuse another person's coordinates merely because their map is convenient.

## 1. Paint a measured match and inspect the saved result

1. Create or open the focal tester's chromosome map. Select one identified relative with a usable pairwise segment table. Preserve the original table before editing or pasting. Require the incoming intervals and any existing painted intervals to use one verified genome build before painting. Convert differing coordinates to that common build outside DNA Painter and retain the originals and conversion record; stop if a build is unknown.
2. Open **Paint a new match**, paste the segment table and use **Preview**. Compare the parsed chromosomes and interval endpoints with the original. Record the selected cM filter; parsing successfully does not mean every source row survived it. DNA Painter's documented ordinary painting default is 7 cM, adjustable in the form. [S1, S2]
3. Enter the match identity and assign the supported parental side and ancestor or couple. If the connection is unresolved, use a provisional group. A group label describes your interpretation; it does not establish it. Save the match. [S1]
4. Click a chromosome's number to open it and inspect all painted segments. In the closed view, groups higher in the key cover lower groups at overlapping positions. Dragging a group changes the visible layer, not its coordinates or evidential strength. [S3]
5. Preserve a note explaining the assignment and its source comparison. For an apparent contradiction, inspect the underlying intervals and provider comparison before recoloring anything. DNA Painter cannot compare raw DNA between two matches; a visual overlap is a reason to investigate, not a triangulation result. [S2]

**Artifact:** source segment table, saved match and assignment note. **Checkpoint:** every retained painted interval can be traced to the correct focal-tester/match comparison; hidden layers have been inspected.

If an FTDNA segment map already exists, keep any later import of parental-side information
as a separate operation. Jonny Perl's September 2024 tutorial describes importing a second
file containing FTDNA's match-level maternal/paternal bucket information after the segment
file. Preserve both dated files and check that they concern the same kit and matching
identities. Use that route only if the actual importer and its identity mapping can be
inspected; ambiguous matches remain unresolved. Keep the reported bucket label separate
from your evidence for a segment's parental side or ancestor. If the tool would silently
turn a match-level label into an unsupported interval assignment, retain the label in your
external match notes instead. Save which labels were added, left unassigned or could not
be mapped. [S10]

For a map's optional Y/mt panel, keep three fields distinct: the reported haplogroup and
its tester/test level, an authorized kit link, and the documented direct-line ancestor
selected for display. A known lineage can be recorded while its haplogroup remains unknown;
choosing an ancestor group does not supply a test result. Check the saved panel and linked
kit before sharing. The chromosome-map panel and an ancestral tree's haplogroup fields are
different objects: record which was edited. If a tree propagates a label to other people,
inspect those annotations and preserve the original tester and the conditional lineage
basis; propagation does not mean those ancestors were tested. Use the
[Y/mt workflow](ydna-mtdna-interpretation.md) to assess the underlying result. [S19, S20]

## 2. Copy or merge map data without changing whose DNA it represents

Choose the smallest transfer that answers the question. Duplicate the map for an alternative analysis; copy one match for a focused comparison; export a filtered subset for an ancestor; export the unfiltered table for a whole-map transfer. Use these as alternate maps of the same focal tester. [S4]

1. Duplicate through the settings cog if you need a working copy. Edit or remove groups in that copy.
2. For one match, click one of its segments, choose **View match**, then **Copy match segment data to clipboard**. Paste into the destination's **Paint a new match** form.
3. For one interval, click the segment, then the chromosome number inside its popup; the clipboard receives that segment's data.
4. For a map or subset, open settings → **All segment data**. Set or clear table filters deliberately, then choose **CSV file**. That CSV contains the table currently displayed. Import it through **Import segment data** where available. [S4]
5. Record the source and destination map names, filters and expected row count. Before pasting or importing into a nonempty map, require the incoming and existing intervals to use one verified genome build; convert differing coordinates outside DNA Painter with a retained conversion record, or stop if a build is unknown. Check the imported interval count, identities and assignments against the exported table; inspect duplicate-looking intervals rather than assuming import deduplicated them.

**Artifact:** original map, working copy or destination map, dated CSV and transfer register. **Checkpoint:** the subset is intentional and the destination still describes the correct tester. To derive a child's map from a parent's phased map, use the next workflow rather than copying the whole map.

## 3. Remap inherited intervals with the Common Segment Generator

Use this when the intervals' chromosome copies are already known. The [Common Segment Generator](https://dnapainter.com/tools/csg) intersects coordinates; it does not compare genotypes or establish that overlapping matches share the same DNA. [S5, H1]

1. Select a phased ancestral interval set for a tested parent and the child's measured inheritance through that parent. For example, intersect a child's match to a grandparent with the relevant parent-map intervals assigned to the child's great-grandparent.
2. Save both input sets and document why they refer to the same inherited chromosome copy. Require both sets and the destination child map to use one verified genome build before intersecting their coordinates. If builds differ, convert the coordinates to that common build outside the generator and retain the originals and conversion record. If either build or chromosome copy is unknown, stop this remapping operation.
3. Paste the two sets into the generator and record the cM cutoff. Generate the common intervals. The blog's low 3 cM default was chosen for phased known-family data; it is not a general threshold for trusting small matches. [S5]
4. Inspect output endpoints: each interval must lie inside an interval from both inputs. Review X results separately; the author's own worked use required removing false X intervals. [S5]
5. Paint the output on the child's map, naming the ancestral assignment and recording both inputs. Repeat separately for the other ancestral groups.

**Artifact:** paired inputs, intersected intervals and child-map entries. **Checkpoint:** the common genome build, chromosome copy and inheritance path are documented before any ancestral label is carried forward.

## 4. Calculate provisional missing intervals with the Inferred Segments Generator

Use subtraction when a close relative shares a known match on DNA the focal tester did not inherit. This requires the relationship path and grandparents' independence assumed by the method; coordinate subtraction alone cannot establish the ancestor. [S6]

1. Choose a match whose relevant relationship runs through one grandparent and establish that the relevant grandparents are unrelated. For example, use your sibling's comparison with a cousin who descends from your paternal grandfather's sibling. Retrieve two complete, comparable pairwise segment tables: focal tester–match and close relative–match. Record provider thresholds, genome build and comparison completeness. Require both tables and the destination map to use one verified genome build before subtraction; convert differing coordinates outside the generator and retain the conversion record, or stop if a build is unknown. A missing export or unavailable comparison is not a negative result.
2. In the [Inferred Segments Generator](https://dnapainter.com/tools/isg), put the focal tester–match intervals in **box 1** and the close relative–match intervals in **box 2**. It returns box 2 minus box 1. A partial overlap can split or shorten an interval; reversing the boxes answers another question. [H2]
3. Save the generated intervals. Their cM values are recalculated; do not expect exact agreement with the provider's original values. [H2]
4. For a suitable parent/sibling comparison, a missing interval associated with one grandparent can support a provisional assignment to the other grandparent on that parental side. With a first cousin, the inference may only exclude a particular great-grandparent. Full-aunt/uncle segments can span fully identical regions and include DNA from both grandparents, so do not apply the simple whole-interval rule indiscriminately. [S6]
5. Keep all inferred intervals provisional. Paint using a match name such as `Match A — inferred`; put exclusions in segment notes instead of inventing a positive assignment. Compare with observed intervals before promoting any inferred label. A small shared subset below a provider's reporting threshold can explain an apparent discrepancy. [S6]

For the specific tested-grandparent scenario, box 1 can contain your measured match to that grandparent and box 2 can be populated with a full chromosome set to infer the other grandparent's contribution on that parental side. Use this shortcut here for autosomes: remove X from the populated second field before generating and handle X through the linked X-inheritance recipe. Missing X comparison data or a male's paternal-grandparent path otherwise risks an erroneous full-X inference. The built-in full set accounts for unsampled starts on chromosomes 13, 14, 15, 21 and 22; do not replace it with hand-made `1–end` intervals. [S7, H2]

**Artifact:** both pairwise tables, generated intervals and visibly inferred map labels. **Checkpoint:** verify the common genome build, distinguish `no reported interval` from demonstrated absence of inherited DNA, and retain the limited conclusion justified by the relative used.

## 5. Combine overlapping comparisons with the Distinct Segment Generator

Use the [Distinct Segment Generator](https://dnapainter.com/tools/dsg) when several relatives share segments with the same target match and you want the distinct coordinate span represented across their comparisons. Pasting multiple sets returns merged distinct intervals and recalculated cM; the tool assumes build 37. [S8, H3]

1. Save one pairwise table for each relative–target comparison. Label the people and require all input coordinates to be verified build 37 before combining sets. Convert other builds outside the generator and retain the originals and conversion record; stop if a build is unknown. [H3]
2. Paste the selected sets into the single input box and generate distinct segments.
3. Save the output and total. Inspect an overlapping chromosome to confirm that the shared span is not counted repeatedly.
4. Keep the original per-person tables. The combined output is a coordinate union across these comparisons, not a measured match between an untested ancestor and the target, and not a single relative's ordinary pairwise cM total.
5. Use it to prioritize a match for further tree research while recording the proposed transmission paths and remaining alternatives. The developer presents this use as experimental, not a definitive relationship-identification method. [S8]

**Artifact:** labeled source tables, distinct intervals and a prioritization note. **Checkpoint:** no relationship or ancestral-genome coverage claim is inferred solely from the union total.

## 6. Plan the next descendant's test with the Coverage Estimator

Use the [Coverage Estimator](https://dnapainter.com/tools/coverage) for a different question: how much of an ancestor's autosomal DNA is expected to be represented by tested descendants? It takes a descendancy tree and tester marks, not a segment union. [S9, H4]

1. Start a tree with the ancestor as root; add the documented descendants or import a GEDCOM and select that ancestor. Back up an existing tree before GEDCOM import, which replaces its contents.
2. Mark the descendants whose tests you can use. Check every tester's descent paths to the root: a tester related to the root more than once must appear on each documented path and be marked as tested at each occurrence. These are occurrences of the same tester, not additional independent tests. Record database access; realizing the full represented coverage requires access to the tests in the same database. A mixed-database tree is not automatically an accessible combined research dataset. [H4]
3. Mark deceased people and known testing willingness. Note the current estimate, request next-tester suggestions and compare feasible candidates. Suggestions exclude people marked willing as well as unwilling, so compare willing candidates manually too. A tested child of an already-tested parent does not add coverage in this model. [S9]
4. Record the proposed tester and expected change, then compare feasibility with the research question. This is a planning estimate based on typical inheritance; actual inherited DNA can differ. [S9]
5. Save to the account where available and download the Coverage tree text file as a recoverable artifact. A browser-local tree can disappear when browser data is cleared. [H4]

**Artifact:** descendant tree, accessible-tester inventory, saved tree file and next-test decision. **Checkpoint:** the displayed percentage remains an estimate; the tree and available tests are checked before interpreting lack of useful matches as evidence against the ancestral hypothesis.

## 7. Annotate a cluster-derived map without assigning the whole cluster

When an existing cluster result needs annotations, preserve its original HTML, focal tester,
database, run date and filters. The January 2020 Cluster Auto Painter walkthrough describes
supported cluster HTML and, for its GEDmatch/MyHeritage inputs, a separate shared-segment CSV.
Check the actual importer's requirements before generating a separate working map; a cluster
matrix without matching coordinates is not itself a segment table. [S11]

1. Inspect the generated map's available match report and find an identified match. Check the
   match's source comparison and the cluster it was placed in before annotating it.
2. Record the documented relationship and its source as a match-level note. Assign a parental
   side or ancestor to an interval only when that interval has its own support; leave uncertain
   intervals unassigned. Retain the original cluster membership in the notes or operation register.
3. Review other matches individually and save the annotated map beside the original cluster
   output. Keep the relationship evidence distinguishable from imported cluster membership.

The source describes match/group overlays and group/segment notes. The separate working copy
and annotation register extend this recipe's existing preservation controls. Its worked
example's overlap-to-parental-side inference is not adopted: an overlapping color does not
establish mutual matching, triangulation or an ancestral couple. [S11]

**Artifact:** original cluster inputs, annotated working map and assignment evidence.
**Checkpoint:** a documented relationship has not silently assigned all of the match's
segments or every member of its cluster to one parental side or ancestor.

## 8. Turn a direct-ancestor tree into a bounded research worklist

An ancestral tree starts with the person whose ancestors are being examined. It differs from
the descendancy tree used by the Coverage Estimator in workflow 6. The saved tutorials describe
GEDCOM root selection, tree completeness and repeated-path views, and a separate Brick Walls
report. Treat their button names, limits and defaults as dated descriptions. [S12, S13, S14]

1. Preserve the input tree and identify the intended root. In the available import or manual
   entry view, record the included generation depth, notes and living-person handling. Check
   the resulting root and known ancestors against the input before interpreting gaps.
2. Inspect the tree's available completeness and repeated-path views. Distinguish a missing
   ancestor within the imported scope from a generation omitted by the import or view. Repeated
   appearances are paths to a person in the supplied pedigree, not independent proof of that
   person's identity or of DNA inherited along each path. [S12, S14]
3. Build a worklist from the available ancestor-gap report or visible tree. Record the displayed
   generation filter and preserve the shown rows when exporting; the December 2024 tutorial
   describes a default recent-generation subset and a CSV of the displayed table. Keep each
   gap or surname clue tied to its branch and label unproved clues as hypotheses. [S13, S14]
4. Keep source-backed annotations separate from inherited colors or automatically propagated
   labels. Before sharing, inspect the actual view and its living-person/notes scope; if that
   scope cannot be checked, keep the worklist local. The output selects documentary follow-up,
   not a new ancestral or genetic conclusion. [S12, S14]

**Artifact:** root and import-scope note, preserved tree, branch-specific ancestor-gap worklist.
**Checkpoint:** every gap is interpreted within the observed tree scope; the percentage or
color of a tree view has not become a measurement of inherited DNA.

When using an available **Dimensions** view, name the category and retain the tree fields
from which its values were generated. Compare generated values with the person's source
facts, especially a country inferred from free-text birthplace. Correct a value only with
support and keep unresolved values unknown. A custom category needs a source for each
person's entry; a propagation checkbox supplies none for that person's ancestors. Save
the checked category view with its root and scope. Religion, cause of death and other
personal facts must not spread through a pedigree merely because a shared color is useful.
The 2021 tutorial supplies category creation and per-value editing; its limits and privacy
defaults require checking in the actual interface. [S21]

For a **Places** view, retain the original birthplace wording beside the generated location
and the root, generation and lineage filters shown. Check ambiguous placements against the
person's supported locality. Where the actual interface offers text-based re-geocoding or
a coordinate selector, save the proposed correction and its evidence, inspect the resulting
placement and keep the original wording. Leave an unresolved place unresolved; a country
default or a map search result does not establish it. A root location omitted by living-person
privacy is missing input, not evidence of an unknown birthplace; do not disclose it merely
to make a map render. The displayed connections link pedigree birthplaces, not observed
travel routes or the transmission of a particular DNA segment. [S22]

## 9. Audit a numeric pair matrix against its measurements and relationships

**Use when:** you have pairwise shared amounts and want to check their entry or compare them
with separately documented relationships. This is a numeric audit, not an ICW graph analysis.

1. Give each tester a distinct identifier and retain each pair's provider, report date,
   supplied amount and source. Keep unknown amounts blank. Names copied from a cluster
   do not supply cM values; the November 2025 example explicitly leaves those for manual
   entry. Use only an import or manual-entry route actually available for the supplied
   data, then compare the saved cells with their sources. [S15, S18]
2. Enter relationships separately from measurements and retain their documentary basis.
   Leave an unresolved relationship unknown or in a hypothesis note. If a sibling-clone
   control is available, check every copied relationship for that new tester, including
   half relationships or multiple paths; enter the new tester's own measured amounts.
   The August 2025 example copies relationship labels but leaves cM blank. [S15, S17]
3. Inspect one tester's pair values at a time. Where relationship-based percentile or
   standard-deviation views are offered, retain the selected mode, displayed relationship
   and reference-data label beside the raw amount. Use an unusual display to recheck
   the input, tester identity and relationship evidence. A percentile describes position
   in the referenced distribution; it is not a probability that the relationship is true.
   No SD cutoff, exclusion threshold or reference-model validation is supplied here.
   If the display's basis is unavailable, retain it as an unexplained provider output. [S16, S17]
4. Preserve the original matrix and a correction log. Reopen the saved result after edits;
   do not assume that a historical edit-mode save/cancel behavior still applies. A symmetric
   pair shown twice remains one comparison. Keep any shared/exported view within the
   permissions and fields actually inspected. [S16]

**Artifact:** an identified pair table with source amounts, independently sourced relationships,
observed display mode, discrepancies and correction history.
**Checkpoint:** no pasted name, copied relationship, blank cell or display outlier has become
a measured amount or a new relationship conclusion.

## 10. Inspect Shared cM histograms and a two-value range screen

Use the available Shared cM Project view to inspect a reported amount against a named
relationship's reference observations. Preserve the tester pair, provider, date, total
definition and displayed project version. These totals do not supply painting coordinates.

1. Open the histogram for a relationship being considered and retain the entered cM,
   bin and displayed number of submissions. A value inside the published range does
   not establish the relationship. Where percentages below and above the entered value
   are shown, record which relationship's distribution they describe. The August 2022
   tutorial uses approximate interpolation within histogram bins; these percentages
   are not probabilities that one relationship is true rather than another. [S23]
2. For an available two-value view, identify both measured tester–match pairs first.
   Check that the two testers have the same genealogical relationship to the match
   under the hypothesis being examined. Full siblings are the tutorial's starting
   example; same-generation cousins need additional path checks. Extra relationships
   through an unshared ancestor or different generations can invalidate this screen.
   Preserve each total's definition; an unavailable comparison is not a measured zero.
   Do not choose between filtered and unfiltered totals to favor a hypothesis. [S24]
3. Enter the two eligible amounts and save the displayed relationship ranges that
   accommodate both. This is a range screen, not a joint probability calculation or
   relationship proof. The November 2022 tutorial's histogram percentages describe
   the **first** input: check the actual view's labels, and swap the order if needed
   to inspect the other amount. Keep the original pair labels with both views. [S24]
4. If using the highest and lowest of several eligible relatives' amounts, retain
   the full measurement set and eligibility checks. The relatives' results are not
   independent evidence. A surprising screen result sends you back to the inputs,
   paths and reference scope; it does not by itself reject a documented relationship.

**Artifact:** sourced pair amounts, relationship hypothesis and eligibility checks,
saved histogram/range views, reference version and interpretation note.
**Checkpoint:** a distribution percentage, missing comparison or two-input range fit
has not become a relationship probability or an inferred measurement.

## Prompt pattern

“For focal tester A, perform only [operation]. Inputs are these labeled tables/tree and these documented relationships. Preserve originals. Return an operation register, the resulting intervals, matrix or tree, and the checkpoint result. Keep observed, inferred and estimated outputs distinct. Do not turn an overlap, coordinate union or coverage percentage into a new measured match.”
