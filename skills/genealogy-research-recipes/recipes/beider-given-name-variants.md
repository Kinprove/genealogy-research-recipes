---
id: "beider-given-name-variants"
title: "Ashkenazi given-name variants from Beider's indexes"
summary: "Expanding documentary searches with recorded Ashkenazi given-name forms from the male and female J-Roots Beider indexes."
kind: "judgment"
scope: {"platforms": [], "tasks": ["an unfamiliar or approximate Cyrillic given name, compound names, alternate spellings, ambiguous article labels, or documenting a DNA match's family under another name form."]}
privacy: "none"
gates: []
guardrails: [{"id": "BEIDER-GIVEN-NAME-VARIANTS-01", "text": "Two forms in one dictionary article create search candidates; they do not establish that two records describe the same person."}]
handoff: ["evidence-proof-judgment", "russian-empire-jewish-identity-attribution"]
checked: "2026-10-01"
checked_basis: "Consulted 2026-10-01"
capabilities: {"browse": [], "local_script": ["scripts/lookup_beider_name.py"], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "full", "group": "Featured workflows", "order": 33}
---

# Recipe: Ashkenazi given-name variants from Beider's indexes

## Contents

- Goal
- Load only the requested name
- What the index changes in a search
- Apply the result to records and DNA research
- Fact-check status

## Goal

Find an ancestor or a DNA match's documentary family under another recorded given-name
form. Use the male and female J-Roots indexes to expand a search, preserving the distinction
between an index entry, a dictionary article and the identity of a person.

These indexes are a useful starting point, **not final or exhaustive lists of names or
their variants**. Add forms found in the person's documents to the search inventory;
absence from an index does not invalidate a documented spelling.

## Load only the requested name

The recorded-name and dictionary-article mappings are bundled in
[`../resources/beider-name-indexes.json`](../resources/beider-name-indexes.json).
Do not load the JSON file or every variant group into the conversation when this recipe
is selected. When present, the lookup helper reads the local JSON inside its process and returns only
bounded article candidates for the requested name. Lookup works offline; source URLs record attribution
and are not fetched during a query.

The bundled snapshot contains 1,647 male and 814 female name/article associations from
complete first-post archive captures dated 2024-12-25, retrieved on 2026-10-03. The JSON
records the archive URLs, capture dates and source hashes; it does not claim to reflect
later forum edits.

### With the helper

When `scripts/lookup_beider_name.py` is present, run from this skill's directory:

```sh
python3 scripts/lookup_beider_name.py -h
python3 scripts/lookup_beider_name.py --sex male --name "Гершель"
python3 scripts/lookup_beider_name.py --sex female --name "Песя"
```

Use `--sex both` when the sex is unknown. Name searches return up to **20 dictionary-article
groups across the selected sexes and inputs**, including similar candidates even when an exact
match exists. Matching spellings from one article use one slot. Each group includes the source,
its key, the best indexed spelling per input, the match type, edit distance and total variant
count. `candidate_count` and `truncated` describe the full eligible group set; `--limit` can
raise the bound to 50 for the current query. Similarity is a search lead, not a source-backed
synonym of an unlisted input.

Select an article to retrieve its recorded variants separately:

```sh
python3 scripts/lookup_beider_name.py --name "Довыд"
python3 scripts/lookup_beider_name.py --key DOVID
python3 scripts/lookup_beider_name.py --key BASHEVE
```

`--key` matches an article key exactly. It returns at most 20 variants per matching index
result by default, up to 50 with `--limit`, their total count and truncation, retaining every article membership of each
returned spelling. It does not expand other articles transitively. No full-index output mode
is provided.

### Without the helper

The Anthropic directory copy ships no scripts. Use the host's file search on
`resources/beider-name-indexes.json`; never load the whole JSON into the conversation.
Search the exact spelling after NFC normalization and uppercasing, then search for the
separator-normalized spelling, ignoring spaces and supported hyphens/dashes as described
below. A host search pattern can allow these separators between letters. Read only matching
`[recorded name, article key]` entries and enough nearby metadata to identify the male or
female index and its source. If sex is unknown, search both indexes.

Keep up to **20 article groups across the selected sexes and inputs**, grouping matching
spellings by index and article key and retaining alternative article memberships. Search a
selected key exactly to read its recorded variants, at most 20 per index by default. Report
any truncation; a bounded view is a partial search inventory. Keep compound-component
searches separate, with their own 20-group bound, and inspect at most the first six parts
per input. Component hits never establish an exact whole-name match.

State plainly that **similar-candidate (fuzzy) search was not available**. Do not invent
approximate candidates or treat file-search results as helper JSON output. Missing data,
unreadable data or a host search that cannot perform the required comparison means
**source unavailable**, not an absent entry. A completed search with no match means only
**not in this index under the reported matching policy**. Apply the same article-selection
and identity rules below.

### Output contract

For the helper, use either 1 to 10 nonempty `--name` inputs or one `--key`, never both. Each input
must be at most 120 characters and contain more than whitespace or supported hyphens/dashes.
`--limit` accepts integers from 1 to 50, with a default of 20. For `--name`, it bounds
article groups separately in the whole-name `results` and `component_search.results`
buckets, across all selected sexes and inputs in each bucket. For `--key`, it bounds
variants per matching index result.

Completed queries and reported errors print one JSON object to stdout. Read `status`
as well as the process exit code:

| Status | Exit code | Meaning and next action |
| --- | --- | --- |
| `found` | 0 | A whole-name exact or separator-normalized match, or a matching article key. Retrieve the selected article's variants and compare records. |
| `candidates_found` | 0 | Only approximate whole-name candidates. Keep them as spelling leads. |
| `not_in_index` | 0 | No admitted whole-name candidate or matching key. Check any `warning` and separate component results; this is a completed query, not a lookup failure. |
| `source_unavailable` | 1 | Bundled data are missing or invalid. Report source unavailable; do not infer an absent name. |
| `internal_error` | 1 | An unexpected helper failure; `error` gives its exception type. Report the failure without interpreting it as an index result. |
| `invalid_request` | 2 | Invalid arguments; `error` explains the problem. Correct the option, input or limit before rerunning. |

`-h` / `--help` prints plain-text help instead of JSON and exits 0. An interrupted
query exits 130 without a result; a reader closing the output pipe early makes the helper
exit quietly with code 0 and may leave no complete JSON object. Neither provides an index result.

### How similar candidates are found

The helper compares NFC-normalized uppercase forms and ignores spaces and supported
hyphens/dashes in a separate comparison key. Supported separators are whitespace and
`-‐‑‒–—−`. It preserves the raw query and indexed spelling.
`exact` means the normalized spelling matches; `separator_normalized` means only separators
differ. Thus `Довид-Лейб`, `Довид Лейб` and `Довидлейб` share a comparison key; this does not
assert that the compound form has an entry in the current index.

`fuzzy` candidates use unrestricted Damerau–Levenshtein distance: insertions, deletions,
substitutions and adjacent transpositions. Compact inputs of one or two letters require zero
edits; three or four allow one; longer inputs allow two. Exact matches rank first, then
separator-normalized matches, then fewer edits. Within an edit tie, a coarse Cyrillic
consonant signature can prioritize agreement: remove vowels and hard/soft signs, fold
Б/П, В/Ф, Г/К, Д/Т, Ж/Ш and З/С, and collapse repeated consonants. This heuristic does not
admit additional candidates or provide a confidence probability. It is not a general
cross-language phonetic encoder; `--name` expects recorded Cyrillic forms and `--key` accepts
Latin article keys. A `--name` input with no Cyrillic letters, or a `--key` with Cyrillic
letters, adds a `warning` field to the output; its `not_in_index` then reflects the wrong
script, not the index, so rerun with the other option.

For example, `Дови` can suggest both DOV and DOVID; `Срулик` can suggest ISROEL, RUVN and
SHMUEL. Keep the alternatives until the original document and its context distinguish them.
An approximate-only whole-name result has `status: candidates_found`; a whole-name exact or
separator match has `status: found`.

Whitespace/hyphen compounds also produce a separate `component_search`, recording each part's
parent input and position; only the first six parts of each input are searched
(`max_components_per_input` in the reported matching policy). Its article groups have their own bound, count and truncation.
Component matches never count as an exact whole-name match: `Довид-Хаим` may have useful
component results while the whole-name status remains `not_in_index`. Compare the original
document before interpreting parts as a double given name.

If the bundled JSON is missing or invalid, report **source unavailable**. A successful
lookup with no admitted whole-name candidate means **not in this index under the reported
matching policy**, not "this name did not exist" or
"this person is absent."

## What the index changes in a search

The label in parentheses is the **dictionary article where a form is discussed**, not a
unique person's name or an instruction to replace every occurrence with one canonical form.
The index describes traditional Jewish names from sixteenth- through nineteenth-century
documents in several languages; names that became traditional only after 1917 are outside
its stated scope. It does not supply a universal map of Soviet or American name substitutions.

These compact examples illustrate why the lookup matters; query the needed local group:

| Index | Recorded forms | Dictionary article |
| --- | --- | --- |
| Male | Хаим, Хайкель | KHAYEM |
| Male | Лейб, Лейба | LEYB |
| Male | Гершель | GERSHN **or** HIRSH |
| Female | Бася, Песя | BASHEVE |
| Female | Хана, Геся | KHANE |
| Female | Гося | GOLDE **or** HODES |

The last male and female examples appear under more than one article. Keep every candidate
article rather than silently choosing the first. Likewise, an unfamiliar-looking form such
as Песя is a reason to consult the entry, not to guess a connection from its sound.

### Sacred names and their vernacular companions

The index files a Hebrew sacred name and the Yiddish name traditionally paired with it under
separate article keys, and `--key` does not follow one article to another. A man recorded as
Лейба in one document can be Yehuda or Aryeh on a gravestone or in a marriage contract. Query
every key in the row. The pairs are those in Warren Blatt's JewishGen talk on Jewish given names,
which notes that the origins of some associations are debated. JewishGen's
[Given Names Data Bases](https://www.jewishgen.org/databases/givennames/) list such double names
by region. A pair is a search lead, not evidence that two records name one person.

| Sacred name or kinnui | Vernacular companion | Article keys to query |
| --- | --- | --- |
| Yehuda; Aryeh | Leib | `YUDE`, `ARYE`, `LEYB` |
| Naftali; Tsvi | Hirsh | `NAFTOLE`, `HIRSH` (no key for Tsvi) |
| Binyamin; Ze'ev | Volf | `BENYOMEN`, `ZEV`, `VOLF` |
| Yissakhar; Dov | Ber | `ISOKHER`, `DOV`, `BER` |
| Efraim | Fishel | `EFROYEM`, `FISHL` |
| Asher | Zelig | `OSHER`, `ZELIKMAN` |
| Uri | Shraga | `URE`, `SHRAGE`, `URSHRAGE` |
| Menachem | Mendel | `MENAKHEM`, `MAN` (Мендель is filed under MAN) |
| Meshulam | Zalman | `MESHULEM`, `SHLOYME` (Залман is filed under SHLOYME) |
| Yehoshua | Falk | `YOSHUE`, `FALK` |
| Mordechai | Gimpel | `MORTKHE`, `GIMPL` |
| Eliezer | Lipman | `ELIEYZER`, `LIPMAN` |
| Chanokh | Zundel | `KHANEKH`, `ZUNDL` |

Some companions already sit inside the sacred name's own article, so `--key` returns them:
Залман under SHLOYME, Занвель under SHMUEL, Айзик under ITSKHOK, Иосель under YOYSEF and Лазар
under ELOZER.

### Entries to check against the dictionary

A few entries in the source posts look out of place. The bundled data keep them exactly as the
posts give them, so check the dictionary article before you rely on one:

| Index | Recorded form | Article in the post | Why to check |
| --- | --- | --- | --- |
| Male | `ЗЫСМАН` | `ZISKIND` | ЗУСМАН and ЗЫСЬКА are under ZUSMAN |
| Male | `МИЛЯ` | `RAKHMIEL`, `SHMUEL` | Eight РАХМ- forms are under IRAKHMIEL; query `--key IRAKHMIEL` and `--key RAKHMIEL` together |
| Male | `ИОСИЯ` | `HOSHEYE` | The form may belong to another biblical name |
| Male | `ПЕРЛ` | `BER` | The female index files Перла and Перля under PERLE |
| Female | `МОША` | `MOYSHE` | MOYSHE is otherwise a male article |

## Apply the result to records and DNA research

1. Preserve the original spelling and identify the field: given name, double-name element,
   patronymic or surname. Look up each given-name element separately; this resource does not
   infer a father's name from a patronymic or a given name from a surname.
2. Retrieve each selected article's forms with `--key`, or an exact article-key file search
   when the helper is absent, and search them in the appropriate name
   field. Keep approximate suggestions and article alternatives separate, including when an
   exact spelling has more than one interpretation. A bounded list with
   `truncated: true` is a partial search inventory, not complete coverage.
3. Correlate hits by date, town, household and relatives. Two forms in one dictionary article
   create search candidates; they do not establish that two records describe the same person.
   Different articles likewise do not rule out a documented personal name change.
4. For a DNA match, use the expanded searches to document the pedigree. Name resemblance or
   article membership contributes no DNA relationship probability. Household and identity
   conflicts belong in `russian-empire-jewish-identity-attribution.md`; combining documents
   and DNA into a conclusion belongs in `evidence-proof-judgment.md`.

## Fact-check status

The examples and ambiguous entries above were checked directly against the two indexes on
2026-10-01. The entries to check were compared with the 2024-12-25 archive captures named in the
JSON on 2026-11-07, and the companion pairs with Blatt's slides and the bundled keys on the
same day. The indexes' historical coverage is the compiler's stated scope. The complete
dictionary articles and the equivalence of any particular person's records have not been
established by this lookup.
