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

A versioned YAML 1.2 file per recipe, `provenance/<recipe-id>.yml`, holds JSON
objects, one per line, under `sources` and `claims`. Python's standard library
parses this strict subset. The file sits outside the shipped skill folder. The
source sidecar keeps only its prose bibliography and final Credits; the
bibliography remains readable and retains its original evidence limits.

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
ledger schema for every sidecar, exact URLs, bibliography-entry and anchor drift,
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

## Ledger location, 2026-11-12 (#205)

The ledger first sat in a block inside each source sidecar. Those sidecars ship
with the skill, and `SKILL.md` sent the assistant into them. Before the move the
blocks were 4,156,652 of the 6,029,610 bytes in `sources/` (69%), more than half
of it full copies of recipe paragraphs used as claim anchors, with 235 lines over
2,000 characters. Each ledger now lives in `provenance/<recipe-id>.yml`; no record
changed, and the frozen inventory is byte-identical. `sources/` is 1,872,678
bytes, and one sidecar instead of 135 is larger than its recipe. `SKILL.md`
directs the assistant to the cited prose entry only. The validator refuses a
ledger block inside a sidecar and a ledger file without a recipe.

A recipe header's `checked_basis` is now matched against the prose alone, so a
ledger copy of the recipe's own sentence can no longer satisfy it (#207, item 1).
`us-federal-court-case-file-recovery` relied on that copy; its header now quotes
its sidecar's `read 2026-11-07`, and the catalog accepts `read` as a check verb.

## Inline source IDs and check dates, 2026-11-22 (#697)

**Question.** Which source IDs, check dates and access qualifications must appear
in the recipe text so that a reader or a consuming model can use a claim correctly?
The issue compared the current layout with two alternatives: keep check dates only
in the sidecar and ledger, or keep the whole claim-to-source mapping there as well.
Pull request #667 prompted the question. In the Southern Claims Commission recipe,
dated markers sit between the steps that lead from an envelope-only House file to
the M2007 docket cards.

**Decision.** Keep the current format. Each alternative loses a check, or loses
information that a reader of the shipped skill needs. No validator, test or recipe
change follows. These elements stay visible in the recipe text:

- every source ID marker, in the sentence it supports;
- for an unread source, the dagger and attributed wording, and for a partly read
  source, the scope wording, in the sentence that cites it;
- for a `platform-ui`, `fee`, `portal-availability` or `custody` claim, the
  claim's check date on a marker of each cited source;
- the archival identifiers and historical dates that a lookup needs, such as
  M2007, Record Group 123 and its Archives identifier, or the 3 March 1873
  deadline. These are part of the instructions, not provenance markers.

Nothing moves to the sidecar or the ledger.

### What reaches a reader

No release build or package includes the ledger. A Git install copies it, but
outside the skill folder that `SKILL.md` points the assistant to. The sidecars
ship in every build except the Claude directory build, which omits `sources/` and
links the sidecars on GitHub (`scripts/build_dist.py`). So the recipe text is the
only place where every installed copy shows a claim's sources and its check date.
`SKILL.md` tells the assistant to read the sidecar entry for each cited ID. It
defines `[S12 @2026-11-07]` as the claim's last check date. The recipe header's
`checked` date records one dated source check for the whole recipe, and the
catalog requires it only for platform recipes. It is null in 52 of the 189 recipes that have reviewed current-state claims, including the
Southern Claims Commission recipe.

The issue assumed that the sidecar already shows the claim dates. A sidecar entry
shows when its source was retrieved, which is not always when the claim was
checked. There are 1,366 reviewed current-state claims. For 1,265 of them, the
ledger records every cited source as retrieved on the day the claim was checked.
For 101, at least one cited source was retrieved later, so its sidecar entry shows
a later date than the claim's check. In 3 claims, no cited entry shows the claim's
date at all: `southern-claims-commission-case-files#C-02` to `#C-04` were
checked on 2026-11-18 and cite only S2, which the sidecar records as read on
2026-11-21.

### What the checks read

| Check | What it reads |
| --- | --- |
| Expiry of a current-state claim | The ledger's `checked` date only |
| Dated marker | For each cited source, a marker with the ledger's `checked` date |
| Source join | The paragraph's rendered markers, compared with the ledger's `sources` |
| Unread or partly read source | The sentence that holds each marker of that source |
| Unregistered passage | A marker, or a domain, currency, current-state phrase or custodian name in the raw paragraph |

The dated-marker check only keeps a visible date equal to the ledger date. The
source join is the only check that compares the ledger mapping with a second,
independent record. Of the 3,852 reviewed paragraphs, 3,427 need a ledger record
only because they carry a marker.

Each change below was applied to the real Southern Claims Commission recipe,
sidecar and ledger, and run through `validate()` from `scripts/provenance.py`
with the date 2026-11-22. The alternatives were simulated with a patched copy of
`validate()`. For "dates only in ledger and sidecar", the dated-marker check was
removed. For "IDs and dates only in ledger", the source join was removed too, and
access wording was checked per paragraph, the smallest unit that a ledger record
can name. The last column is discussed below.

| Change | Current | Dates only in ledger and sidecar | IDs and dates only in ledger | One date per claim |
| --- | --- | --- | --- | --- |
| Ledger names the wrong source (C-07) | Caught | Caught | Passes | Caught |
| Ledger record removed, marker kept (C-07) | Caught | Caught | Passes | Caught |
| Marker and ledger record both removed (C-07) | Passes | Passes | Passes | Passes |
| Check older than 180 days (C-02) | Caught | Caught | Caught | Caught |
| Ledger date changed, recipe unchanged (C-05) | Caught | Passes | Passes | Caught |
| Dagger removed (C-01) | Caught | Caught | No marker to change | Caught |
| Attribution wording removed (C-01) | Caught | Caught | Caught | Caught |
| Unread source moved to another sentence (C-09) | Caught | Caught | Recipe text unchanged | Caught |

C-01 is one sentence long, so the per-paragraph check still caught the removed
attribution there. Moving dates out keeps the expiry check and loses only the
visible date and its comparison with the ledger. Moving the IDs out lets a wrong
or missing ledger link pass, as well as a qualification moved to another sentence.

Qualifications are bound to sentences. 464 reviewed claims cite both a fully read
source and a limited or partial one. In 422 of them, at least one sentence cites a
read source but not the limited one. The validator can require the qualification
in the limited source's own sentence only because the marker shows which sentence
that is.

### Model probe

Three tasks were given to `claude-opus-5-5`, with `SKILL.md` as system
instructions and a read tool for the recipes, isolated as in
`evals/run_evals.py`. The tasks were: an envelope-only disallowed House file
(referral, M2007, Record Groups 123 and 205, Fold3), a barred claim (M87, M1407,
Record Group 233, Fold3), and a New York City birth certificate without a
certificate number (portal steps). In each task, the user's date was 15 September
2027, past every expiry window. Each layout ran three times per task. For each
layout, `SKILL.md` described the markers that layout uses. The same model,
without the layout name, graded each answer against the recipe's facts.

| Layout | Right steps | States the check date | Warns that steps may have changed | Keeps attribution |
| --- | --- | --- | --- | --- |
| Current, no sidecars | 9/9 | 3/9 | 1/9 | 9/9 |
| No inline dates, no sidecars | 9/9 | 0/9 | 2/9 | 9/9 |
| No inline dates, sidecars readable | 9/9 | 2/9 | 2/9 | 8/9 |
| One date per claim, no sidecars | 9/9 | 1/9 | 0/9 | 8/9 |

- Every layout gave the right steps and identifiers. The markers did not stop the
  model from following a procedure.
- Answers seldom stated a check date in any layout. Every answer ended with the
  release-date note that `SKILL.md` requires under "Version and updates". In
  this probe, that note told users that their copy might be out of date; the claim
  dates mostly did not.
- Two answers failed the attribution grade. On rereading, both rest on sources
  the recipe records as read: S2 and S5 for the Fold3 collections, and S6 for
  the name search. Neither states the unread advice as fact.
- Limits: one model, which also graded; three tasks; three samples per cell. A
  month counted as stating the check date, and an answer that did not use the
  attributed advice counted as keeping its attribution. The steps grade passed
  one answer that used the birth year where the recipe asks for the filing year.
  No layout removed the source IDs, no run used the current layout with readable
  sidecars, and no task asked for the evidence behind a claim. For the layout
  with readable sidecars, `SKILL.md` said that each sidecar entry records the
  check date, which is true only where the retrieval and check dates match. The
  runs without sidecars had no web access, so they could not open the GitHub
  links that the Claude directory build uses.

The outcome rules were fixed before the run. Inline dates counted as used if, for
each task, at least 2 of 3 answers with them stated the date and at most 1 of 3
answers without them did. This held for the barred-claim task only. So the probe
adds only weak evidence about dates, and the decision rests on the checks and
counts above.

### One date per claim, not adopted

This option was not one of the two alternatives that #697 named. Each claim has one
check date. Because the validator requires it on a marker of each cited source,
the 3,992 dated markers in the 1,366 claims repeat their claim's date; 1,123
claims carry more than one. Showing the date once, on the paragraph's last dated
marker, would leave 1,366 dated markers. In the rendered text, the number of dated
markers followed by more words in the same paragraph would fall from 2,483 to 440.
With this layout, the validator caught the same changes as with the current one.

It is not adopted, because the probe found a reader who misread it. In two of the
three answers to the envelope task in this layout, the model said that the Court
of Claims referral step had no recorded check date, and one told the user to
treat the step as a lead to confirm. That step's marker had lost its date, and
the paragraph's last marker carried the date that covers it. No answer with every
marker dated said so. The probe rules also accepted this layout
only if, for each task, it stated the date in no more than one answer fewer than
the current layout; it failed on the barred-claim task (0 of 3 against 2 of 3).
Only `SKILL.md` would tell a reader that a date at the end covers the earlier
steps, and a reader on GitHub does not see it.

Changing the layout would require these changes:

- one date per claim: replace the dated-marker check in `validate()`, and rewrite
  the 1,123 reviewed paragraphs that carry more than one dated marker, with their
  ledger anchors;
- dates only in ledger and sidecar: remove that check, and rewrite 1,380 reviewed
  paragraphs, the 1,366 current-state ones and 14 others that carry a dated
  marker, with their ledger anchors. No pending record carries a dated marker;
- IDs and dates only in ledger: also remove the source join and the sentence
  checks and their tests, and rewrite every reviewed paragraph and the 1,003
  pending ones that carry markers, with their ledger anchors. The frozen inventory
  fingerprints those pending records, so each would first need a review;
- each of them: change the "Read source limits" text in `SKILL.md` and the
  provenance section of `MAINTAINERS.md`, and update the tests that quote dated
  recipe text or test the dated-marker rule.
