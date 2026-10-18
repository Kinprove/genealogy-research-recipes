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

## Establish what could have been observed

Keep the tool, date, exact pair, readiness, chromosome scope, coordinate build and
exposed reporting/filter settings with the result. Check usable shared markers in
the interval being tested. GEDmatch's SNP-overlap matrix describes common marker
coverage across the kits; a genome-wide count does not establish local coverage or
whole-test equivalence. No-calls are not observations of a matching genotype. The
Family Finder 5.0 white paper explicitly distinguishes genotyped/imputed calls and
does not count a no-call as a matched SNP. [H2, H3]

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

## Reconcile rows before interpreting totals

Keep the original reports. Identify the pair and interval behind each row before
summing: A's report of sharing with B and B's report of the same sharing with A are
two reports of one comparison. Repeated exports add no sharing. Different endpoints
or cM values require reconciliation; approximate overlap alone is insufficient to
declare records identical. This follows from the pairwise measurement definition,
not an empirical relationship cutoff.

Compare totals using the same autosomal/X scope, minimum-segment inclusion and FIR
counting convention. A suspiciously doubled total is a reason to inspect reciprocal
rows, not to apply a universal cM ceiling or divide every result by two. Preserve a
changed algorithmic measurement separately from any inferred change in relationship.

## Handoff

Report the matched observation or bounded absence, the control's scope, unresolved
coverage/settings and the decision it supports. Agreement between algorithms can
support a measured pattern; it does not prove a named ancestral connection. Continue
with [X and phasing judgment](xdna-phasing-judgment.md),
[family-level DNA reasoning](ai-for-dna-research.md), or the appropriate platform
workflow. For GEDmatch's run manifests and direct pair checks, use
[its practical workflows](gedmatch-practical-dna-workflows.md).
