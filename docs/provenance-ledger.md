# Provenance ledger migration (#95)

## Decision before implementation

The objective is to make an assertion traceable to its evidence and recorded access
limits, and to expose missing checks before a release. Earlier corrections to issues
including #65, #76, #78, #83 and #96 fixed individual defects and routing metadata. They did not
create a claim-to-source contract. #77, #81, #82 and #84 remain separate work; this
migration must preserve their findings rather than declare them resolved.

The current inputs are the public recipes, their source sidecars, the catalog
generator and the CI suite. They are available in this checkout. The corpus has
136 sidecars, including numbered bibliographies, tables and unnumbered lists;
19 corresponding recipes lack the usual inline source markers. These files
support a structural migration. They cannot establish that a page was read, or
reconstruct missing statement-level attribution.

Implement a conservative migration and an enforceable contract for reviewed
records. A valid reviewed claim can be used with its recorded qualifications;
an invalid one blocks CI. An unresolved legacy record remains visible migration
debt and is not promoted to verified evidence. This changes the next decision:
maintainers can distinguish a source recheck, an attribution repair and a wording
correction rather than repeat a corpus-wide freshness sweep.

The initial migration is offline and bounded to these public files. It preserves
their text and URL case. It does not reopen external research, rewrite thousands
of claims as observations, assign new check dates or infer rights. Stop automatic
migration at an ambiguous attribution: record it as pending. A narrowly scoped
real example and synthetic failure tests exercise the reviewed-record contract.

## Contract

A versioned YAML 1.2 block in each source sidecar holds JSON objects, one per
line, under `sources` and `claims`. Python's standard library parses this strict
subset. Put it **before Credits**, whose final-section contract remains in force.
The prose bibliography remains readable and retains its original evidence limits.

Each source has a stable ID, exact URLs, type, publication/retrieval dates, access
enum, rights, evidence basis, entry digest and reverse claim references. Unknown
values remain null or `unknown`. Multiple URLs do not imply all were read: a
reviewed fact requires a single-URL read/partial entry, or separately reviewed
entries for the supporting URLs. `partial` needs an explicit scope limitation.

Each claim has a stable ID, exact recipe anchor, source IDs, kind, check date,
statement status and review status. Reviewed anchors are unique, have source
markers, and current-state claims carry matching dated markers. Non-read sources
can support attributed observations with a dagger and explicit limited-access
wording; they cannot support facts. An access record is evidence about retrieval,
not proof that the source supports an inference.

Legacy records are imported as pending. A separate frozen inventory fingerprints
their source entries and claim anchors. Normal regeneration cannot add migration
exceptions. Changed or new factual passages must be reviewed; removing debt does
not grant permission to add another exception. A heuristic flags unmarked domains,
fees, current-state phrases and named custodians, but cannot discover every factual
sentence or judge whether an attribution is historically correct.

Generate a corpus report with reviewed current-state claims and per-recipe debt.
CI checks schema, entry/anchor drift, source joins, exact URL preservation, access
qualifications, freshness and report drift. It does not fetch external sites or
treat HTTP 200 as evidence of reading. Live link checking is separate from this
offline evidence contract.

## Boundaries and remaining work

Keep source IDs stable; do not renumber evidence simply to make a contiguous list.
Do not replace #77's repair with invented sources. Preserve numbering gaps and
unresolved markers in the migration report. #82 owns existing pinned cross-links;
this work must not silently rewrite them. The catalog already generates routing
and validates counts; reuse it rather than create a second header or exporter.

Existing public recipes accept reviewed corrections in place under the current
MAINTAINERS/CONTRIBUTING contract. A bot-only edit rule would contradict that
workflow and require a real export bot and private-generator integration, neither
of which is available here. Do not invent a private source commit or exporter
version for an export manifest. These proposals need an explicit owning pipeline
before they can become truthful enforcement.

Green tests prove the contract's implementation, not that the corpus's genealogy
claims are correct.

## Accepted scope and closeout, 2026-11-08

The maintainer accepted a narrower acceptance scope for #95 on 2026-11-08. The
structural migration and its checks close the issue. The legacy records are not
reviewed in one bulk pass.

**Shipped checks.** `scripts/provenance.py --check` runs in CI. It enforces the
ledger schema in every sidecar, exact URLs, bibliography-entry and anchor drift,
source joins and generated backlinks, unique reviewed anchors whose markers match
their sources, dagger and attributed wording for unread sources, visible scope
wording for partial reads, dated markers and 90- or 180-day expiry for reviewed
current-state claims, the frozen legacy inventory and report drift. Separate
tests cover YouTube ID case, HTTPS links, source numbering and citation
resolution, section counts, unread-source caveats, local recipe links, dated
current facts and the Credits list.

**Resolved evidence links.** One reviewed source,
`us-federal-court-case-file-recovery#S9`, and one reviewed current-state claim,
`us-federal-court-case-file-recovery#C-3062c226d110`.

**Remaining records.** 4,208 pending source records and 2,192 pending candidate
anchors stay frozen and listed in [the provenance report](../PROVENANCE.md). An
edit that changes one of them makes CI require its review, and regeneration then
prunes its exception. No bulk pass promotes them.

Limits measured at closeout:

- 1,495 pending sources are cited by no candidate paragraph. The validator
  refuses a reviewed source that no claim cites. These records resolve only when
  a recipe cites them with a marker or the entry is removed.
- Many entries record only a publication date. Reviewing such an entry without
  new evidence leaves its access `unknown`. Every reviewed paragraph that cites
  it must then carry a dagger and attributed wording. Recording an actual
  retrieval date in the entry avoids that.
- The importer treats every bullet before Credits as an entry. Some prose
  bullets, for example `admixture-model-run-scope#B1` to `#B11`, are therefore
  counted as source records. They are not evidence, and no claim cites them.
- Pending current-state claims have no automatic expiry. The recipe header's
  90-day check covers `platform` recipes only.

## Integration before merge, 2026-11-08

The public base advanced to `56b3c4ec63ba4c961151363bc407813f4d017046`
after the first review. It includes the internal-link checker, Beider contract,
source/recipe corrections, unread-source qualifications, numbering placeholders
and offline recipe handoffs from PRs #181, #179, #184, #183, #172 and #182.
Those accepted results are incorporated without reopening their research or
changing their text. The initial, still-unmerged inventory is regenerated from
this base; this is not a new exception-enrollment mechanism for normal commands.
The one reviewed NARA source and claim retain their original IDs, check date,
access basis and exact evidence. No additional source is promoted to reviewed.

The visibility check uses the same pinned Markdown/HTML dependencies as the
existing link checker. Source matching, date checks and access qualifications
share parsed prose, excluding metadata in inline and reference links. Exact raw
anchors remain the basis for identity and drift checks. The validator batches
local parsing and never follows links; CI installs the parser before these checks.
