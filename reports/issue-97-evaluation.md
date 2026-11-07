# Issue 97 evaluation evidence

The revised candidate passes **14/14 cases** across the documented local case batches, with three samples per case.

The skill inputs are commit `4653a3e70554d6ed3e403a274f1e9990d37656c2`. The normal `claude3` profile resolved to `claude-opus-5-5`; no model override was supplied. Native Read returned complete selected files, matching the primary read-file server's default. All materials are synthetic.

| Case | Routing and regex | Complete rubric | Result |
| --- | --- | --- | --- |
| cm-relationship | 3/3 | 3/3 | pass |
| deportation-1944 | 3/3 | 3/3 | pass |
| family-interview | 3/3 | 3/3 | pass |
| gedcom-ancestry | 3/3 | 3/3 | pass |
| gedmatch-upload | 3/3 | 3/3 | pass |
| match-outreach | 3/3 | 3/3 | pass |
| match-outreach-helper | 3/3 | 3/3 | pass |
| memorial-proof | 3/3 | 3/3 | pass |
| parentage-proof | 3/3 | 3/3 | pass |
| photo-attribution | 3/3 | 3/3 | pass |
| russia-origin | 3/3 | 3/3 | pass |
| unreadable-village | 3/3 | 3/3 | pass |
| wato-ranking | 3/3 | 3/3 | pass |
| ystr-distance | 3/3 | 3/3 | pass |

Routing and regex require 3/3; at least 2/3 samples must satisfy every rubric question. Denied, unfinished or out-of-scope reads fail.

The [JSON receipt](issue-97-evaluation.json) preserves the earlier batch, its original grades, documented equivalent-wording corrections, final synthetic answers, structured judge decisions, source/harness hashes and trace digests. The earlier batch passed 8/14 as recorded and 12/14 after checked lexical corrections using the same answers and original judge decisions. Its incomplete supplemental reads and parentage-plan omissions motivated the final adapter and instruction fixes.

A later full batch stopped after 34 completed samples when native Read rejected the large proof recipe at its default token limit. Eight complete cases were retained, and each of the six affected or unfinished cases received three fresh samples after an actual large-read delivery check. Skill bytes and case contracts are identical across those batches. Six frozen clarification answers were rejudged under the stricter wait-for-answer instruction; a question-then-workflow control was rejected. Original denied reads remain in the receipt's transport-stop record.

The unchanged **v1.12.0** release has preserved failures: its upload replies omit destination/setting consent, and its GEDCOM replies omit living-person redaction. Historical totals in the receipt use their recorded contracts and are diagnostics rather than a final direct comparison. The false QUAY-to-proven mapping control is also preserved and rejected.

On 2026-11-07 the owner explicitly revised issue 97's merge gate: preserve the failed unchanged-release baseline and require all revised-candidate cases to pass. Per-case criteria are unchanged. This decision does not authorize a merge. GitHub-hosted model evaluation is last observed skipped without the repository's ANTHROPIC_API_KEY secret; the owner will add it. The successful local profile does not supply that runner credential.
