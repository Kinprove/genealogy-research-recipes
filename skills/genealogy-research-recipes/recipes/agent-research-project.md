---
id: "agent-research-project"
title: "Running a long genealogy project with an AI agent"
summary: "Keep an AI agent's genealogy work honest over months: what counts as evidence, how to lay out Markdown research notes, what 'searched', 'saved' and 'done' must mean, how corrections reach every note, and how to delegate and write to a tree safely."
kind: "judgment"
scope: {"platforms": [], "tasks": ["running a multi-session genealogy investigation with an AI agent", "keeping genealogy research notes in Markdown or Obsidian", "delegating genealogy reading to sub-agents", "carrying a correction through notes and a tree", "research vault", "Obsidian genealogy notes", "the agent says saved or done", "sub-agent genealogy research", "long genealogy project", "keep research across sessions", "correct a claim everywhere", "fill empty surname fields in a tree"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "AGENT-RESEARCH-PROJECT-01", "text": "Treat a model-written summary, tag or \"key insight\" as a pointer. Open the source before writing a claim."}]
handoff: ["evidence-proof-judgment", "research-documentation", "source-citation", "ai-for-documentary-records", "archival-image-coverage-verification", "family-collection-intake-and-capture", "gedcom-research-export"]
checked: null
checked_basis: null
capabilities: {"browse": [], "local_script": [], "extensions": [], "data_transfer": ["publish", "third-party-tool", "upload"], "contact": []}
router: {"tier": "full", "group": "Evidence and documentation", "order": 136}
---

# Running a long genealogy project with an AI agent

Use this when an agent works on one family across many sessions and keeps notes in Markdown, for
example in an Obsidian vault. It covers what an agent gets wrong about its own work.

Other recipes own the neighbouring topics: proof arguments in
[evidence-proof-judgment](evidence-proof-judgment.md), log columns in
[research-documentation](research-documentation.md), citation form in
[source-citation](source-citation.md), handwriting and AI reading in
[ai-for-documentary-records](ai-for-documentary-records.md), page coverage in
[archival-image-coverage-verification](archival-image-coverage-verification.md), and tree files in
[gedcom-research-export](gedcom-research-export.md).

Rules and figures without a public source are Kinprove observations, according to Kinprove's own
private project records [S1†].

## Contents

- The mistake behind most failures
- Where to start
- Give each kind of information one home
- Markdown and Obsidian
- Words the agent must earn
- Searches and absence
- Reading a source
- Correcting a claim
- Long sessions and interruptions
- Delegating to sub-agents
- Writing to a tree
- Deleting, moving and backing up
- Review before a note counts

## The mistake behind most failures

An agent treats its own earlier output as evidence. It quotes its note, trusts its summary, believes
a passing check, and says "saved" or "nothing found" without proof. Months later nobody can tell a
document from a guess.

Every fact passes through layers, and each layer can lose or invent something:

```text
original page -> reading -> note -> tree -> chat summary
```

- Settle a doubt by going up the chain. Never settle it between two copies.
- Count repeated copies of a claim as one witness.
- Treat the tree as an inventory of what is held and a set of leads, not as evidence. Walk it before
  proposing an identification, and ask what each entry rests on before defending it. An entry
  defended as established turned out to be the researcher's own DNA guess.
- Treat a model-written summary, tag or "key insight" as a pointer. Open the source before writing
  a claim.

## Where to start

If you set up only five things, set up these:

1. A read-only folder for originals.
2. One living note per open question, holding the five items listed below.
3. The definitions in [Words the agent must earn](#words-the-agent-must-earn), applied to every report.
4. A search log beside each question that keeps the search states apart.
5. A rule that a correction is not finished until every copy of the claim is fixed.

**Privacy gate:** <!-- privacy-gate: upload, publish --> Project notes can name living people and
hold tentative relationships. When they are kept in a shared folder, a cloud-synced or hosted
service, or a repository other people can read, saving to them moves that data to the service and to
everyone with access. Answer the privacy gate in `SKILL.md` before saving there; write access to the
notes is not permission to disclose. Without permission, keep living people's details and the
hypotheses about them in a local file, and save only the rest.

At the start of a session, reload the instructions, read the note for the question and check the
live state. At the end, update that note and the search log, save them to the project notes and write
the next check.

## Give each kind of information one home

| Kind | Home | Rule |
| --- | --- | --- |
| Originals: scans, PDFs, tree exports | A read-only folder on storage you control | Never convert, recompress or overwrite. Keep the provider's image ID and the full reference. |
| Readings of a source | One entry per reader, beside the source | Record reader, model, date, status and literal text. A new reading never overwrites an old one. |
| Person or question note | One note per person or open question under research | Holds the current answer. New readings attach here. Do not start a parallel note. |
| Dated report | One per research pass | Records what was searched and found that day. Later changes are dated notices only. |
| Search log | Beside the question | Follow [research-documentation](research-documentation.md). |
| Method note | A separate folder | Reusable technique only. Record which case a rule came from and whether that case still stands. |
| Agent memory | The agent's own store | Pointers to notes. No case facts. |
| Tree | Your genealogy program or site | The one place for relationships. A graph or index built from it is a copy you can rebuild. |
| Machine text and derived search files | A clearly marked folder | Exclude from source counts, coverage and cleanup decisions. |

Give every field one writer. If a value is read from a document, keep it in one place that other
notes link to, so a correction happens once.

### What a person or question note holds

1. The current answer, with its date and how to verify it.
2. Each kinship labelled documented or inferred.
3. Open conflicts, naming each source's value and why one was not adopted.
4. Rejected identities as explicit "not the same as" lines.
5. The next check.

Put limits on the claim they limit. A caveat left in the bibliography is lost when the claim is
reused, and a short chat answer needs the same caveat as the note.

### Layout rules that hold up

- **Do not create one note per person in the tree.** Bulk conversion produces thousands of empty
  notes that go stale. Write notes only for people and questions under real research.
- **Give same-named people separate notes** with a fixed label in the name, such as life years or
  parentage [S7]. Number namesakes. "Cannot merge" is a valid result.
- **Treat a dated report as coverage, not knowledge.** Reconcile it into the living note statement
  by statement, in the same piece of work. In one point-by-point comparison, a third of the
  statements in ten reports had never reached the person's note.
- **Put decisive findings where the next worker must pass.** A note does nothing because it exists
  or is linked. In one measured vault, most notes were never opened.
- **Keep run progress and tool instructions out of biographies.** Status sentences go false after
  later repairs. Use a separate log, and state the real scope of every summary in its first line.
- **Never cite a temporary folder, personal path or ignored directory.** Copy what a conclusion
  relies on to durable storage first, and keep addresses and quotations in a durable note.
- **Copy names and references exactly** from the owning note or image, never from a brief or file
  name. Put normalised forms in separate fields. Record references as text, not screenshots.
- **Read a note immediately before changing it.** The owner may have edited it during a long review.

## Markdown and Obsidian

These come from an Obsidian vault of about 860 research notes kept in git.

- **Do not rely on hand-inserted note templates.** Templates inserted by hand were rarely followed: 2 of 143
  reports and 1 of 55 question pages. Pages generated by a script matched their template 65 times out
  of 65. Generate what is regular, and put what must be written into a step the agent has to perform.
- **Give every field and view a named reader.** Fields added for uniformity go stale or stay empty.
- **Generate index pages and tables.** A hand-kept list silently omits what it should hold: one index
  lacked 62 of 95 reports. Keep generated blocks between markers and fix the generator, not its output.
- **Put orientation first.** Where things stand and how to continue go at the top of a working map,
  with dated news below. On one map a growing dated feed pushed the first heading down to line 305.
- **Choose the link form by who follows it.** Wikilinks work for people inside Obsidian. Resolve them
  before passing them to a tool that needs a file path. Bare note names collide: one link resolved to an identically named note in another
  volume and passed every check. Qualify any name that can repeat, and validate links with a script.
- **When moving files,** resolve each link against the old layout and leave dated records unchanged.
  A stale path finds nothing and reads as an absence of evidence.
- **Keep frontmatter small and check its types.** Models write YAML that parses but means something
  else: a list item ending in a colon becomes a mapping. Quote values that hold colons or quotation
  marks, and check that a list holds only strings.
- **Do not encode status in folders.** Moving a file each time its status changes means repairing
  links each time. Organise by family, place or topic, and keep status in a field.
- **Archiving closes nothing.** Keep an unresolved archived question linked from a live page.
- **Keep what an agent must read in plain Markdown.** An agent reading the file sees a Dataview query,
  not its result.

Obsidian repairs links itself in one case: with its Automatically update internal links setting on,
it updates the links to a file renamed in Obsidian or moved with its `move` command
[S8 @2026-11-13], [S9 @2026-11-13]. Its help says nothing about a move made by a script, a shell
command or git; after such a move, check every link as the rule on moving files above says.

## Words the agent must earn

Hold every report to these definitions.

| Word | True only when | Never proved by |
| --- | --- | --- |
| saved | The note was updated and the change is in the project notes | A promise to remember, a scratch folder, an uncommitted working copy |
| searched | A real tool return or saved response exists, showing what was actually sent | A planned click, a plausible ID, a search snippet |
| not found | The search finished and its scope is stated | An error, login page, CAPTCHA, timeout, blank page, capped or partial result |
| read | A stated range of pages or frames was opened and read through, and the rest is logged as unread | A download, an OCR run, a filename match, a finished job |
| verified | The checker opened the original and read that name, date or number there | Agreement with one's own transcript, a hash, a page count, a schema, a link check |
| independent evidence | No single informant, image or draft could have produced both, and the search angles can fail in different ways | Two OCR passes of one image, several agents repeating one pattern, copies of one draft |
| new | It was compared person by person with the notes and the tree | A spelling variant, or a fresh citation for a link already known |
| done | Each expected item was checked at its destination for real content, the total matches, and the indexes and notes that lead to it are updated | An exit code, a status flag, a log line, a model's "complete", an upload receipt |

Hash, page-count, schema and link checks prove file integrity and form only. Notes can pass all of
them while one name carries many different birth years. Make every check print what it examined,
and make it fail if it examined nothing.

Before relying on a figure in a note, re-measure it from the raw input and state which items and
which period it covers. A count from a subset reads as a verdict on the whole collection.

## Searches and absence

- Keep separate states: not listed, unreachable, not inspected, not tested, query lost, true no
  result. Show an unchecked field as "not inspected", never as blank.
- Never turn a bare absence into a fact about a person. No record is not death. A missing family
  section is not childlessness. No documented link is not "unrelated". Write "unsupported", not
  "disproven", unless the negative-evidence gate in
  [evidence-proof-judgment](evidence-proof-judgment.md) is met.
- Treat any capped, lazy-loaded or paginated result as partial until unique record IDs match the
  publisher's total. If the site shows no total, report the result as partial.
- Before arguing from a person's absence from a list, read how the list was compiled: title page,
  headers, footnotes and the household's own row.
- Make every "pass complete" mark name the exact list of targets it covered. A filter added late
  silently dropped one surname of five, and the completion mark then proved nothing for that family.
- Before naming a next source or calling a find new, search your notes for earlier readings, known
  losses and old negatives. Make "destroyed" and "already searched" findable by reference number.
- Record "looked at and rejected for this question" apart from "used", with the reason. Keep a
  table of refuted ideas at the head of a long investigation.
- Decide before you check a claim what each outcome will do. "Not found" is not "false", and an
  unconfirmed claim stays what its author reports.

## Reading a source

- Transcribe the page before looking at the tree. A familiar surname can prime a reader to find a
  person who is not on the page.
- Call a re-read blind only if its brief held no candidate names, numbers or ranges. For a contested
  reading, get a blind literal transcription first. If blind readings still disagree, find a better
  image or another primary source. Do not vote, and do not ask again.
- Test a PDF or OCR text layer against the page image before relying on it. Settle digits, dates and places on the image,
  and record which layer each claim rests on.
- Use indexes and keyword search to enter a source, not to prove identity, completeness or absence.
  For discovery, run every surname in the tree against the source. Searching only for the people you
  expect reconfirms known links.
- Record three things separately: the source was read completely, the copy is complete, and what it
  says is true.
- A quotation is not verification. Ask what in the sentence would have to be false if the claim were
  right. One check logged the clause that refuted a finding as support for it.
- Use quotation marks only for exact text in a saved copy. Keep the source's own wording beside any
  paraphrase, so that "suggests looking" does not become "reports finding".

## Correcting a claim

- Find and fix every note, tree entry, table and index that repeats it. A corrected report leaves a
  refuted spouse sitting in the tree note unless someone goes looking.
- Put a dated retraction directly beside the claim. Mark superseded conclusions visibly. Do not
  overwrite them, and do not rewrite a dated report.
- Treat your own fix as a new unverified claim. In one review of stale-claim corrections, about one
  in eight was itself wrong, so a model must not apply content fixes unread.
- When one error of a type appears, audit everything produced under the same assumption, and fix
  the script or instruction that produced it.
- When a premise falls, recheck everything built on it, including method rules drawn from that case.
- Change a conclusion only when the evidence or the reasoning changes, not because someone pushed
  back. When the researcher gives a firm ruling, record it in their exact words, as theirs, and work
  from it until new evidence or changed reasoning bears on it: the researcher rules on identity and
  proof ([evidence-proof-judgment](evidence-proof-judgment.md)). Record a relative's firm statement
  in their exact words, as theirs, but keep it an account to assess, not a ruling or a
  tree fact ([family-interviews-and-oral-tradition](family-interviews-and-oral-tradition.md)). Do
  not attribute either one to a document.
- Use a fixed list of written statuses, such as refuted, weakened, under-determined and candidate,
  and state the evidence behind any rejection. A confidence label is a judgment by whoever assessed the evidence, never a script's reading of words
  in the text.

## Long sessions and interruptions

- Keep a running plan and findings file. Save each query with its output and completeness as you go.
  Work reconstructed from a final chat cannot separate a real negative from an incomplete run.
- After an interruption, reload the governing instructions and check the live state. Memory, task
  lists and old reports are an index. Live state and the newest instruction outrank them.
- Write a status with the way to verify it. Record an outdated next step in the research log as
  done or dropped, with its result, then replace it in the status so a resumed session does not act
  on it. The log keeps the record and analysis that led to the step
  ([research-documentation](research-documentation.md)).
- Before saying something is inaccessible, new or never requested, or asking the researcher for a
  document, search earlier sessions, the notes and the researcher's own files.
- Have the agent write recurring corrections and working procedures into its permanent instructions
  and show the line. An agent that says it has remembered a rule repeats the mistake next session. A
  correction about one case belongs in that case's note.

## Delegating to sub-agents

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Notes and images given to an AI agent or sub-agent can name living people and send their data to a third party; answer the privacy gate in `SKILL.md` before handing them over.

- Have every delegate write findings to a named file after each small unit of work, and check that
  the file exists. Delegates cut off by a limit lose whatever stayed in their final message.
- Treat a delegate's facts, counts and confidence labels as leads. Open the cited record, compare
  names with the source rows and recompute totals from the saved files.
- Test a shared brief on one item before dispatch. Copy the researcher's decisions verbatim, because
  one paraphrased "hold them" lost who had been cleared. Give parallel workers one convention, one
  citation list and an explicit hold list.
- Give each item one owner. Let one agent write to the tree and one agent make requests to a fragile
  site.
- Ask for read, uncertain, unread and failed items separately against the assigned list. A failed
  reply is never a negative, and several delegates retrying one pattern are one test.
- When filtering automatically, keep all raw rows. A model may rank names but must not discard them.
  A frequency filter once dropped over a thousand names that were mentioned only once.
- Attach citations while drafting, from the saved text of pages actually opened. Search snippets
  and URLs in a brief are unverified hints.

## Writing to a tree

**Privacy gate:** <!-- privacy-gate: publish --> Writing to an online tree can publish living people's data to other members; answer the privacy gate in `SKILL.md` before writing.

- Read approval at its literal scope, tied to the exact people and destination reviewed. "Use your
  judgement" delegates what to propose, not permission to write.
- While extracting, create a parent or spouse link only from what the source states. An extracting
  agent's own identification never becomes a structured link, and if a source names one parent, the
  child stays single-parent. A link proved by reasoning across sources needs the written argument in
  [evidence-proof-judgment](evidence-proof-judgment.md) and the researcher's approval.
- Derive every relationship by walking actual parent-child links to a named anchor, and count
  generations from the anchor for both people in both directions.
- Treat a person ID as valid only together with its tree and account. In one project, 148 of the 149
  IDs shared by two tree files named different people, and the lookup answered confidently about the
  wrong one.
- Before creating anyone, check for duplicates in the local export and then in the live tree. A
  person missing from an export is not a finding until the current tree has been checked.
- Prove every new way of writing on a throwaway tree first. On one site, adding a partner made that
  partner the parent of existing children, and saving a dialog without a date deleted an event.
- Read back each write field by field. After an ambiguous failure compare the live record, and never
  resend blindly.
- Do not add an unproved inferred link to the tree. Keep it, with its reasoning, in the research
  notes or a separate worksheet ([evidence-proof-judgment](evidence-proof-judgment.md)). When the
  tree already holds such a link, entered earlier or by someone else, mark it as tentative on the
  tree itself and write the reason in the notes: removing it is a change to the tree that needs
  approval, and an unmarked link reads as proved. Apply the mark only to that link, not to
  descendants or to every source conflict.
- Give uncertainty a dedicated place, such as a research note on the person, with a reason, author
  and date. Name fields that hold research
  notes, and invented people that hold gaps, are later read as facts. Label placeholders and exclude
  them from counts of real ancestors.
- Change an existing name only with approval. List conflicts with the old value, new value and source.
- Close each bulk import with per-row receipts, and reconcile what was emitted, what was stored and
  what the agent reported. In one import, 98 of 183 parent links vanished without an error.
  Report a receipt check as exactly that: receipts matched against the plan show what was sent
  and acknowledged, not what each person's page shows now. Report a read-back only for the people
  whose pages you reopened.
- When one field is empty for a whole imported group, check how the import was run before
  treating the gap as missing from the records: an option or a column mapping can drop a field for
  everyone.
- Treat a full re-import as destructive replacement. Keep a restorable copy, confirm the file's
  identity first, and never report zero people imported as success.

Before writing any surname into a tree, a bulk fill of empty fields included, sort each value into
one of four kinds and keep the kind in the batch plan: printed for this person in the source;
inferred from a parent; a place name, title or patronymic; or unknown. Only the first is a
transcription.

- **Inferred from a parent.** Copying a father's surname to a child claims two things: that this
  is his child, and that the family used that surname as a hereditary name in the child's
  generation. Where a book prints the surname for the father and for one son, it is still an
  inference for the other children. Write it only with a research note on the person that says it
  is inferred and from whom, and never count it as transcribed.
- **Inferred through a "possibly".** Where the source marks the parentage as possible, a surname
  derived through it is conditional too. Carry the source's qualifier into the person's research
  note; never put it inside the name field.
- **Not a surname.** A place name ("of Dubrovny"), a title ("Besht", the acronym of Baal Shem
  Tov) or a patronymic in a parent's surname field is not a family name. Never copy it to anyone
  else: copied mechanically, it gives the tree a family of people surnamed "Besht". Where the
  family used patronymics, a child's name comes from the father's given name, not from his
  surname field ([Scandinavian patronymic and farm names](scandinavian-patronymic-farm-name-record-recovery.md)).
  Moving such a value out of the parent's own field is a name change and needs approval.
- **Unknown.** Where nothing establishes the surname, leave the field empty. An empty field keeps
  the question open; an invented surname reads as a fact.
- **Birth and married surnames are separate fields.** Never move a value from one to the other: a
  woman's married surname does not go into her birth-surname field, and her birth surname does not
  go into her married-surname field. A wife printed under her husband's surname gives her married
  surname; it does not by itself give her birth surname.
- **Exceptions.** Before a bulk fill, hold back every person whose source value is not a plain
  surname or whose parentage is marked possible. Resolve each one separately on its own evidence;
  never fill it with the surname of the only male relative in view.

## Deleting, moving and backing up

**Privacy gate:** <!-- privacy-gate: upload, publish --> A backup or off-site copy on a drive the
user controls stays local. A copy held by a backup service, a cloud folder or a shared folder moves
the originals and notes, and the living people in them, to that destination and to whoever can open
it. Answer the privacy gate in `SKILL.md` before creating or extending such a copy. Opaque handles
for living people reduce what the copy exposes; they do not replace permission.

- Before deleting, check what still cites the file. One cleanup removed the only authority for a
  negative kinship conclusion that four notes still relied on.
- Delete source files only with separate approval, from a frozen list, after the copies at the
  destination are verified. Decide duplicates by hash, then by comparing images, and leave a choice
  between differing copies to the researcher.
- Before reorganising remote material, copy, verify and only then move.
- Keep human judgments in the person or question note, where imports and regeneration cannot replace
  them. One regeneration erased hand-entered people while reporting success.
- Keep the original capture of every source on storage you control. An attachment on someone else's
  site does not preserve the master [S5]. Map what each backup covers, keep one copy off-site, and
  prove a restore works [S2, S3, S4, S6].
- Assume research on real families will leak into shared files. Use opaque handles for living people
  from the start. Treat exact dates, URLs and filenames as personal data, and never put a password
  in a note.

## Review before a note counts

Have an independent reviewer re-read the original source, not your summary or transcription table.
Give the reviewer an enumerated list of what to check, and audit the items marked confident as well
as the doubtful ones: our worst errors sat in the unflagged group. Plan and code reviews do not cover
conclusions. Keep the reviewer's verdicts, so that the check can be repeated.
