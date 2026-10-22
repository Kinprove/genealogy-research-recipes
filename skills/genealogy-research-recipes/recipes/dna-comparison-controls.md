# Recipe: DNA comparison controls across services

## Goal

Decide what agreement, an absent match, or a changed shared-cM total can establish
when comparing services or exports. Use before treating another service as a control
for a reported pair. These are measurement checks; segment validity and ancestral
attribution remain separate questions.

## Resolve the tests and the search

Identify both actual tests, their tested people, source/generation and selected kit
IDs. A person may have several tests; an available test of that person does not show
that the requested test was uploaded, processed or selected. Repeated downloads or
uploads of one test do not provide independent tested relatives.

A surname search can retrieve an ancestral surname rather than the tested person's
name. MyHeritage documents both as search targets. Inspect the returned card's own
person and kit, and use spelling or script variants as leads rather than identity
proof. A search miss with unresolved kit identity leaves the control unavailable. [H1]

Check the query or comparison with a known positive on the same selected kit and
scope. Choose a control that exercises the operation being relied on: retrieving a
close relative does not establish sensitivity to a small segment, X coverage, or
correct behavior for every other kit. If the expected positive is missing,
investigate the query, selection and processing before interpreting an empty list.
This control procedure is original methodological synthesis, not a vendor guarantee.

When sharing appears only under relaxed settings, add a known negative. Run the same tool
and lowered minimum segment size on pairs documented as unrelated within the time frame of
interest. If those pairs show similar summed small-segment totals, the relaxed total does
not distinguish a genealogical connection. Do not turn it into a predicted relationship, or
assign it to a tree line without records or segments above the usual minimum. The
[unrelated-pair demonstration](https://www.youtube.com/watch?v=ZqK9b2Vt6gQ) motivates this
check; its pairs are anecdotal, not a measured false-positive rate or a vendor threshold.

## Establish what could have been observed

Keep the tool, date, exact pair, readiness, chromosome scope, coordinate build and
exposed reporting/filter settings with the result. Check usable shared markers in
the interval being tested. GEDmatch's SNP-overlap matrix describes common marker
coverage across the kits; a genome-wide count does not establish local coverage or
whole-test equivalence. No-calls are not observations of a matching genotype. The
Family Finder 5.0 white paper explicitly distinguishes genotyped/imputed calls and
does not count a no-call as a matched SNP. [H2, H3]

Inventory each raw file before using it as comparison input. Record its download or generation
date, header, any lab batch or results date shown, and per-chromosome counts of rows, calls and
no-calls, including X, Y and MT. A vendor name, format label or header method tag does not fix
the marker set. Downloads of one kit at different times can differ, and assay generations change
under one label. Before using one file in place of another, compare the two directly for SNPs in
common and SNPs unique to each. Zero rows for a chromosome make that input unavailable, not a
negative result. Keep the file's own counts separate from the usable or slimmed counts a tool
reports after upload. The [raw-file SNP-count comparison](https://genarchivist.net/showthread.php?tid=2449),
[re-download header discussion](https://genarchivist.net/showthread.php?tid=1739),
[method-tag discussion](https://genarchivist.net/showthread.php?tid=1999),
[added-rsID download comparison](https://genarchivist.net/showthread.php?tid=729) and
[Family Finder generation discussion](https://genarchivist.net/showthread.php?tid=2412) motivate
this. They establish no vendor policy, batch cutoff or effect on matching. [H12, H13]

For X, distinguish raw-data coverage from the service's displayed matching scope.
The presence of X-labeled markers does not establish usable coverage of a particular
non-PAR interval. Identify PAR using
the test's actual build: the Genome Reference Consortium lists different boundaries
for GRCh37 and GRCh38. Ordinary no-father-to-son X routing concerns non-PAR; PAR can
recombine between X and Y. Check the parent's and child's usable coverage of the
same interval before treating an absent parental segment as a contradiction. [H4, P1]

| Observation | Supported report |
| --- | --- |
| Exact test not identified, not uploaded, or inaccessible | Control unavailable |
| Failed query, failed comparison, or processing incomplete | No completed comparison result |
| Relevant interval has no usable shared input | This input cannot test the interval |
| Tool omits the chromosome or requires another qualifying result | Claim outside this tool's observable scope |
| Completed comparable run reports no qualifying segment | No segment reported within the recorded scope and limits |

Two documented examples show why scope matters. MyHeritage's app browser describes
autosomal chromosomes; its silence does not test an X-only claim. FamilyTreeDNA's
X-Matches list requires qualifying autosomal sharing, so absence from that list can
occur despite X sharing. These are documented tool behaviors, checked 2026-10-18;
recheck the actual service rather than extending them to every raw-file generation
or future interface. [H5, H6]

A result below a reporting floor need not appear. The smallest match in an old
export does not establish the service's current admission rule. Differences in
marker coverage, maps, phasing, imputation, joining and filters offer possible
explanations for disagreement; the discrepancy alone does not select its cause.
Family Finder 5.0 is one documented example of processed output, not an unfiltered
reference instrument. [H3]

When one match person appears under several kits (different chips, a self-converted file, a
sequencing extract), keep a separate row for each kit against the same tester. Record its
platform, any conversion before upload, any imputation by the receiving site, and the
compared-SNP overlap. Do not adopt the highest or first-listed total; record the spread across
kits as unresolved variation for this pair. A
[multi-platform kit comparison](https://forum.molgen.org/index.php/topic,10116.0.html) and a
[converted-upload discrepancy report](https://forum.molgen.org/index.php/topic,10423.0.html)
motivate this step. Neither shows which value is correct or establishes the cause. [H18, H19]

For degraded, forensic, artifact or heirloom-derived kits, record the reported call rate or
processing status with each result, and treat segment count, endpoints and total cM as
uncertain readings rather than full-coverage input for relationship prediction; the
[investigative-genealogy discussion](https://www.youtube.com/watch?v=3xodviufcG4) and the
[heirloom-kit example](https://www.youtube.com/watch?v=lMnm4UjIO60) motivate this but supply
no validated call-rate cutoff, SNP-density threshold or error bound.

For a kit derived from whole-genome data, treat the FASTQ or BAM/CRAM as the source and each
uploaded chip-style file as a separate derived input. Record the alignment build, the extraction
template and its build, the conversion tool, and which derived file went to which service.
Extract in the comparison data's build instead of relying on a liftover. A variant-only VCF omits
reference-matching positions, so a missing position is not a measured reference call, and a BAM
rebuilt from such a VCF adds no coverage. Before reading matches or an empty list, check the
summary statistics: no-call share, autosomal heterozygosity, and X/Y calls against known sex. An
all-no-call file or implausible heterozygosity marks the derived file as unusable input, whether
from the derivation or the source data; report the control as unavailable. The
[WGS-extraction discussion](https://forum.molgen.org/index.php/topic,14971.0.html),
[WGS-to-chip conversion discussion](https://genarchivist.net/showthread.php?tid=1345),
[conversion-before-upload advice](https://genarchivist.net/showthread.php?tid=939) and
[sequencing-file quality warning](https://genarchivist.net/showthread.php?tid=106) motivate this.
They give no thresholds, liftover error rate or measured loss, and the symptoms do not identify a
cause. [H14, H15, H16, H17]

## Reconcile rows before interpreting totals

Keep the original reports. Identify the pair and interval behind each row before
summing: A's report of sharing with B and B's report of the same sharing with A are
two reports of one comparison. Repeated exports add no sharing. Different endpoints
or cM values require reconciliation; approximate overlap alone is insufficient to
declare records identical. This follows from the pairwise measurement definition,
not an empirical relationship cutoff.

When one provider's row overlaps several rows in another report, retain a one-to-many
crosswalk: original row IDs, endpoints, cM and SNP counts for every reported fragment.
Preserve internal gaps and unresolved splitting/joining after checking the actual tests,
build and reporting scope. Close endpoints or similar summed cM do not justify filling a
gap, merging rows or declaring equivalent inherited tracts. This applies the
[fragment-comparison example](https://www.youtube.com/watch?v=3vWBeFUBVdg) without adopting
its proposed endpoint tolerance or inferring the cause of a provider difference.

Compare totals using the same autosomal/X scope, minimum-segment inclusion and FIR
counting convention. A suspiciously doubled total is a reason to inspect reciprocal
rows, not to apply a universal cM ceiling or divide every result by two. Preserve a
changed algorithmic measurement separately from any inferred change in relationship.

Small-segment inclusion is a second reason, besides reciprocal rows, why one service's total
may be much larger. To compare totals from services with different minimum-segment rules,
recompute from each match's segment-level export. Drop rows below the chosen common minimum,
sum what remains, and keep the reported total and the recomputed total as separate labelled
values. Some difference may remain after recomputing; it does not select a cause. The
[vendor-total explanation](https://www.youtube.com/watch?v=ecwbM9Lc-Gg) and the
[threshold comparison](https://www.youtube.com/watch?v=W278DGiDKq0) motivate this step; their
per-vendor thresholds are not verified here and may be out of date.

For Ancestry, keep the Timber-adjusted total and the unweighted total as separate labelled
values. Compare the unweighted amount, segment count and longest segment with another service's
figures. A Timber reduction is the vendor's weighting, not a disagreement in measured sharing.
Posters suspect weighting can also push an expected match below a list threshold. A direct
comparison of the same raw files in another tool is then a separate measurement with its own
thresholds, not a correction. The
[Timber cross-vendor comparison](https://genarchivist.net/showthread.php?tid=137) and a
[multiple-test Timber discussion](https://genarchivist.net/showthread.php?tid=905) motivate this.
Even unweighted figures still differ between vendors, and the threads do not establish when a
match is dropped. [H20, H21]

## Handoff

Report the matched observation or bounded absence, the control's scope, unresolved
coverage/settings and the decision it supports. Agreement between algorithms can
support a measured pattern; it does not prove a named ancestral connection. Continue
with [X and phasing judgment](xdna-phasing-judgment.md),
[family-level DNA reasoning](ai-for-dna-research.md), or the appropriate platform
workflow. For GEDmatch's run manifests and direct pair checks, use
[its practical workflows](gedmatch-practical-dna-workflows.md).
