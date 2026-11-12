---
id: "corpus-seeded-name-search"
title: "Corpus-seeded name searches across scripts and OCR"
summary: "Recover attested spellings across scripts and OCR by separating encoding, orthography and field behaviour."
kind: "judgment"
scope: {"platforms": [], "tasks": ["Hebrew/Yiddish name misses, lossy search folds or uncalibrated zero results."]}
triggers: ["Hebrew/Yiddish name misses", "lossy search folds", "uncalibrated zero results"]
privacy: "none"
gates: []
guardrails: [{"id": "CORPUS-SEEDED-NAME-SEARCH-01", "text": "normalization is not spelling expansion; preserve originals and treat rescued hits as candidates rather than identity or kinship proof."}]
handoff: ["archival-image-coverage-verification", "beider-given-name-variants", "bessarabia-moldova-record-routing", "galicia-bukovina-habsburg-record-routing", "jewishgen-search-family-reconstruction"]
checked: "2026-10-18"
checked_basis: "opened 2026-10-18"
capabilities: {"browse": [], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "full", "group": "Featured workflows", "order": 4}
---

# Recipe: Corpus-seeded name searches across scripts and OCR

Use when a remembered spelling, transliteration or name dictionary fails to retrieve a person from Hebrew/Yiddish or other historical text. This recipe owns retrieval diagnostics. Use [beider-given-name-variants.md](beider-given-name-variants.md) for dictionary candidates and [jewishgen-search-family-reconstruction.md](jewishgen-search-family-reconstruction.md) for database-specific family searches.

## Contents

- Build a small attestation inventory
- Diagnose three different failures
- Retrieve through another recorded participant
- Calibrate the actual field
- Stop with a scoped result

## Build a small attestation inventory

Read candidate-bearing passages in the available corpus before fixing the search pattern. Retain each literal surface form, source/page, surrounding words, possible name role and confidence. For a large corpus, use bounded discovery batches; report which portions were actually examined. With only a remote search interface, seed from returned passages and existing records rather than claiming a full-corpus pass.

Keep observed spellings, dictionary forms and generated possibilities in separate columns. A remembered list is a starting set, not an exhaustive inventory; corpus discovery is also not a guarantee of completeness. Review matched surface forms with context before interpreting counts. Short stems can match ordinary words, place names and unrelated surnames.

For each attested form, also record who produced it: family tradition, an enumerator or clerk, a
formal document or the person's own signature. Add the record type, place and date range. Mark
forms seen only once, or only in one record class or under one recorder. Check whether a spelling
change coincides with a new priest or clerk, or whether forms cluster by jurisdiction. These
patterns guide later searches. They do not choose a 'correct' spelling, and they do not prove that
differently spelled entries are one person. Examples from
[Brady](https://www.youtube.com/watch?v=aL2BGQ7raRw),
[Castillo](https://www.youtube.com/watch?v=qDW8dEp5mN0) and
[Allen](https://www.youtube.com/watch?v=XJeAPcgLHpc) motivate this step. Allen's AI-generated
spelling explanations were not verified.

Determine whether each token is a given name, compound-name component, patronymic, surname, occupation or another descriptor. Do not discard an occupational-looking token categorically: it may function as a surname in the particular record. Search the plausible roles separately when unresolved. Neither a descriptive title nor an occupational surname by itself proves that two people had the same occupation.

An index may also have given a token the wrong role. A word repeated in every entry on a register
page, such as a German 'died' formula, can be indexed as a first name. A copied tree may carry
another researcher's placeholder for an unknown name, such as Danish 'Ukendt'. The compiler of a
surname index to a Russian regional-history book cautions that headings formed from given names
may be patronymics rather than surnames. Before adding such a token to the
inventory or searching it as a family surname, read the original entries or the indexed page. The
[register-formula example](https://forum.ahnenforschung.net/forum/thread/928/) and
the compiler's caution in a
[book surname-index thread](https://rodgersforum.borda.ru/?1-7-0-00000258-000-0-0-1776484154=)
motivate this check. They supply no list of formula words, placeholders or affected headings.

In some German registers, a person appears as 'X gnt. Y' (genannt). X is usually the birth or
earlier surname and Y a farm or house name. A man who married onto a farm, or a later spouse of its
widow or widower, may take the farm name. Names can also stack ('X gnt. Y gnt. Z'). Record each
part separately, and search the birth surname and every farm name as separate lanes. A shared farm
name links people to a holding; by itself it does not show blood kinship. A
[chain-marriage example](https://forum.ahnenforschung.net/forum/thread/928/)
motivates this step. It does not show how widespread the custom was or how consistently clerks
wrote it.

In Pennsylvania German baptisms, the first given name, such as Johann or Anna, could be given to
every child of the same sex in a family. The second name was the call name (Rufname) the child
went by: a family's Johann Georg, Johann Jacob and Anna Barbara were known as Georg, Jacob and
Barbara [S32, S33]. Search each child under the call name alone as its own lane. Do not treat the
shared first name as the name in daily use, and do not merge siblings who appear in later records
as plain Johann or Anna. A baptism that gives only 'Johannes' may belong to a man later known as
John [S32]. A call-name match is a candidate, not proof that two entries are one person.

## Diagnose three different failures

| Failure | Controlled comparison | Limitation |
| --- | --- | --- |
| Encoding | Original text versus a documented normalized search copy | Equivalent encoding does not generate other spellings |
| Orthography or name form | Attested language/script forms, compound-name components and dictionary candidates | A linguistic candidate is not a same-person link |
| OCR/extraction | Distinctive shorter spans; observed line breaks, spaces or letter confusions | A repaired search string is not a corrected transcription |

For local Hebrew/Yiddish text, Unicode normalization can reconcile some encoding differences. Decomposition followed by removal of selected Hebrew combining marks is an additional, lossy search transform; normalization alone does not strip points. Apply any such transform to both pattern and search text, preserve the originals and verify retrieved passages. [S1]

Hebrew final letters and Yiddish digraph characters are separately encoded. If needed for retrieval, explicitly test final-to-medial folding (`ךםןףץ` → `כמנפצ`) or digraph expansion (`װ/ױ/ײ` → `וו/וי/יי`) in a search copy. These are application choices, not effects guaranteed by NFC/NFKD or instructions to rewrite source spelling. They can merge distinct strings; inspect the resulting homographs. [S1, S2]

Removing points does not supply missing vowel letters, convert one surname spelling into another or resolve Hebrew versus Yiddish orthography. Add consonant substitutions only as bounded exploratory lanes motivated by the source, observed OCR errors or linguistic evidence. There is no universal substitution mask that proves coverage of every Slavic name in Hebrew script.

For Cyrillic or other non-ASCII names in a local database, match on case-folded keys built from
both the query and the stored text, for example with Python's `str.casefold()`, which its
documentation offers for caseless matching, and keep the source spelling unchanged. [S30] SQLite's
`NOCASE` collation folds only ASCII letters, and by default its built-in `lower()`, `upper()` and
`LIKE` also handle case only for ASCII, so a miss from these is not a negative; its documentation
names the ICU extension for Unicode-aware `lower()` and `LIKE`. [S27, S28, S29] Also check each
name for letters from a second script: Unicode's confusables data lists Cyrillic а, е, о, р, с and
х as look-alikes of Latin a, e, o, p, c and x. [S31] Search each script form as a separate lane.

Pre-1918 Russian text needs a pre-reform spelling lane. OCR of pre-reform print and HTR
(handwriting recognition) of manuscripts can keep the old letters, so a query in modern spelling
can miss the entry. The decree of 10 October 1918 replaced ять (ѣ) with е, фита (ѳ) with ф and і
with и, and dropped ъ at the end of words while keeping it inside words as a separator [S17]. The
Narkompros (People's Commissariat for Education) decree of 23 December 1917 had set the same rules
[S18]. Ижица (ѵ, izhitsa) is named in neither decree: it had become rare, fell out of use gradually
and still turns up in some register names, so treat it as a rare variant [S17, S19]. Search both
forms, for example Ѳома/Фома, Ѳеодоръ/Феодор (and the vernacular Фёдор), Тимоѳей/Тимофей and
Аѳанасій/Афанасий, and keep the forms the returned text actually holds. Confirm every hit on the
image. In a volume that binds several parishes, limit a negative to the target parish's section
and to the years and pages that carry recognised text.

Transcription can also move or replace whole name parts. When an expected entry is missing from a
transcribed index, test a query with the given name and patronymic swapped, since a man recorded
as X son of Y may be indexed as Y son of X. Also allow for an indexer who substituted a dissimilar
local name for a Jewish given name. Run these as separate logged lanes and confirm any hit against
the record image before using it. A
[transcribed metrical-index example](https://forum.j-roots.info/viewtopic.php?f=164&t=6963)
reports both errors in one database. It gives no error rate and does not say which collections are
affected.

When a record was written in a language or dialect other than the family's, search the recording
office's form of the name as a separate lane. Church entries may Latinize given names. A French
administration may write Jean for Johann. A court, military or district office in a High German
area may give a Low German parish family's name in its High German form. In Lithuanian Lutheran
records, different pastors, even in one church, may record the same person under very different
German or Lithuanian name forms. Check where the recording office sat, not only the parish, and
keep the literal form in the inventory. The [Jensen](https://www.youtube.com/watch?v=g8pltErjQpU),
[Minert](https://www.youtube.com/watch?v=cc8_6tNN8C4) and
[Sinickas](https://www.youtube.com/watch?v=xoY83Sx3ANk) transcripts give examples, not a
systematic conversion table. A matching form is a candidate, not proof of identity. For Romanian
and Russian name lanes in Bessarabian records, see
[Route a Bessarabian or Moldovan record by date, district and bank of the Dniester](bessarabia-moldova-record-routing.md).

In English-language records, a German surname may be translated by meaning, not only respelled:
Zimmermann as Carpenter, Schwarzwälder as Blackwelder, Becker as Baker [S34]. More often the
English form follows the sound, as Bentz to Pentz and Pence [S34], or Stehli to Staley and Bauman
to Bowman, and given names take English forms, as Heinrich to Henry and Maria to Mary [S33]. Search
the translated surname as its own lane: a spelling-variant or Soundex search will often miss it
(Zimmermann and Carpenter have different Soundex codes). Keep
the literal form in the inventory, and treat a translated-name hit as a candidate until place,
family and dates connect it.

In Russian-language records an Armenian given name may appear as a Russian one. A 2024
Familio.Media article by Nina Galishnikova describes a list of Moscow Armenian community members
of the 18th to early 20th centuries, compiled from Armenian-language documents of the Moscow
Armenian Spiritual Board and checked against Russian-language records and Vagankovo Armenian
cemetery epitaphs. It reports two kinds of pair: a Russian equivalent, as Akob/Yakov (Акоб/Яков)
and Ovanes/Ivan (Ованес/Иван), and a similar-sounding name, as Arutyun/Artemy (Арутюн/Артемий)
and Mkrtych/Nikita (Мкртыч/Никита). [S26] Search each form as a separate lane; the pairs were
observed in one community.

Grammatical endings need their own lanes. In German-language registers, a woman's surname may
carry a feminine -in suffix that is not part of the family name. When such a name is hard to read,
drop the suffix, keep uncertain first letters open, check the readings against a local family
book's surname variants and list of wives, then return to the original entry. In Ural and Siberian
records an indeclinable -ских form may alternate with -ские or -ская for one family, and -ов/-ев
could be written inconsistently. Search each ending, including feminine and plural forms, and keep
each literal ending in the inventory. A -ских form can also be the genitive plural of an owner's
-ский surname, as in 'вотчина графинь X-ских' (the estate of the Countesses X-sky). Decide from
grammar and context before you create an indeclinable -ских peasant family. See the
[family-book example](https://forum.ahnenforschung.net/forum/thread/17915/),
the [Ural Civil War thread](https://rodgersforum.borda.ru/?1-23-0-00000012-000-0-0-1714980847=)
and the [genealogy terms thread](https://rodgersforum.borda.ru/?1-0-0-00000141-000-0-0-1701453218=).
None gives a rule for which form a clerk used. A family book is a compilation, and identity still
needs original entries and place and household evidence.

An 18th-century Russian commoner's patronymic is usually the short possessive form, Иван Петров
(сын), not Иван Петрович. The -ович form had been a privilege since the 16th century, and Catherine
II's rules for officials gave it in official papers only to generals and the matching highest
officials [S35]. A woman's form adds -а, often with
дочь (Петрова дочь), and a father's name ending in -а gives -ин, as Малина to Малинин; -овна was
rare in the earlier period [S36]. When a transcribed or full-text index misses an 18th-century
person, search the short form (Петров, Петрова) as well as -ович and -овна, as Vera Miller also
advises [S37]. Do not file the short form as a surname. For reading such entries, see
[the household-list audit](russian-household-list-transcription-audit.md).

Baltic surnames change with sex, and Lithuanian ones also with marital status. A Lithuanian man's
surname ends in -as, -is, -ys, -us, -ė or -a. An unmarried woman's replaces that ending with
-aitė, -ytė, -utė or -iūtė, and a married woman's with -ienė, or sometimes -uvienė after a
two-syllable name in -us [S38], as Briedis, Briedytė and
Briedienė [S39]. Older records may write the maiden suffix as -kė instead of -tė [S38]. A Latvian
surname has a masculine and a feminine form, as Kalniņš and Kalniņa [S40] or Briedis and Briede
[S39]. Search the man's form, each woman's form and a documented stem wildcard as separate lanes,
and convert a woman's form back to the family name before comparing relatives [S38, S41].

Latin inflection needs its own lanes too. A Latin church entry may name a child's father in the
genitive, so both the given name and a Latinized surname end in -i instead of the nominative form.
An indexer may misread such an ending as a new name. Early-modern university matriculations may
Latinize the surname with an -us ending and add adjectival words for town or nation after it.
Search the nominative, the inflected Latin form and a reconstructed vernacular form as separate
lanes. Keep the literal entry, and do not search origin adjectives as surnames. The
[Latin register-name examples](https://forum.ahnenforschung.net/forum/thread/928/)
give two instances and no conversion rules. A reconstructed vernacular name is only a candidate.
For Polish-orthography and Latin given-name lanes in Galician registers, see
[Route a Galician or Bukovinian record by date, confession and custodian](galicia-bukovina-habsburg-record-routing.md).

## Retrieve through another recorded participant

When the target name may be misread, try an independently known co-listed household member
or participant whose name may have survived recognition. Test an optional place constraint
separately if the entry may omit it, keeping collection/year bounds explicit. Log the alternate
query, then return to the full entry and image to read the target. The [co-listed-name example](https://genery.com/ru/forum/viewtopic.php?t=4868)
supplies a retrieval tactic; co-occurrence corrects neither transcription nor kinship by itself.
Use only syntax supported by the actual field, without transferring another database's controls.

## Calibrate the actual field

Before interpreting zero results, try an independently known positive that the same field and scope should retrieve. Distinguish catalogue author/title, body-text OCR, typed name fields and free text. If the control fails, investigate scope, access or field behaviour; report the failed control rather than the target's absence. A functioning website does not establish a functioning within-book index.

Remote services may normalize differently from local code. Submit original and transformed queries separately and compare returned identifiers. Check only the syntax needed for the task; do not transfer local regex, wildcards or Boolean syntax to an undocumented interface.

If you build a word index from Tesseract's TSV output, parse it as raw tab-separated text, not as quoted CSV: Tesseract writes each word into its row with no quoting or escaping. [S23] A default reader, such as Python's `csv` module or pandas `read_csv`, uses `"` as its quote character with `QUOTE_MINIMAL`. It treats a word token that begins with a double quote, such as an OCR'd opening quotation mark, as the start of a quoted field, and a quoted field can run across tabs and line ends. [S24, S25] The following rows are then swallowed into one cell, their words vanish from the index, and a name looks absent when it is not: a false negative. Parse with quoting disabled (`csv.QUOTE_NONE`, or `quoting=3` in pandas). Compare the parsed row count with the file's line count minus the header, and check that no text field contains the TSV header or runs of numeric columns.

A Belarusian or Ukrainian database may index names in that language's spelling, in Russian, or
both. Run each spelling as a separate lane, and calibrate each database's own convention before
trusting a zero. On 2026-11-02 the Virtual Museum of Soviet Repressions in Belarus (represii.net)
returned no hits for a common surname in Russian spelling and 194 for its Belarusian spelling
[S20]. Zhnivo (db.zhnivo.com) covers the historical Belarusian lands and destinations of Belarusian
migration such as Siberia and the Baltics. Its search help asks for the surname in Russian,
although the site is in Belarusian, with `|` between alternatives in one field and `*` as a
wildcard. The help also warns that machine-read names can differ from the original by a letter or
two, so confirm each hit on the document it points to. Its terms forbid automated bulk or partial
download without the project's permission, so search it by hand in the user's browser. [S21]

A site search can silently drop one query term. Some engines ignore words outside a length range or
on a common-word list, then return results for the remaining words. A multi-word result list may
therefore not contain the target at all. Read any ignored-terms notice even if its stated reason
looks wrong, and compare each term with the engine's stated limits. Retry an over-long name as a
shorter stem with a wildcard, and confirm that hits contain the target. The
[forum-search test](https://forum.j-roots.info/viewtopic.php?f=181&t=9163) documents one
installation's configurable limits. Other sites differ, and a stem can match unrelated words.

Some lists, registers and card indexes are arranged alphabetically and may need to be browsed in
filing order when a name search fails. Before you report a name as absent from one, find out how
its compiler filed letters. A list made in a language with extra letters may give letters such as
Spanish ñ or the traditional ll, or Icelandic á, ð and þ, their own alphabet position, while a
transcribed copy may have dropped those letters. Browse both positions, plus the entries just
before and after the target surname, and record the ranges you browsed. The
[Scandinavian](https://www.youtube.com/watch?v=1CzAygZqg2Q),
[Icelandic](https://www.youtube.com/watch?v=4jhIdvmyFUw) and
[Mexican](https://www.youtube.com/watch?v=siMS_6gGKYs) examples supply no collation table for any
particular index. In the [Maryland death-index example](https://www.youtube.com/watch?v=ClvFJDrlrUw),
browsing the Murray cards filed right after Murphy found a card whose date conflicted with the
known events. A card found by browsing is only a candidate until it is tested against known events.

JewishGen's transcription rules allow hidden “Other Surnames” and “Other Towns” fields to make names in comments searchable in typed fields. Their existence does not show they were populated in a particular collection. Compare free-text and typed-field retrieval where supported. [S3]

Phonetic search is another candidate lane: JewishGen's Belarus instructions explicitly document name forms that it misses. It cannot replace searches for attested alternatives. [S4]

## Stop with a scoped result

Keep the corpus/index version or access date, field, exact Unicode query, filters, transformation policy, inspected portions and result identifiers. Separate occurrences, unique records/books and identified people. Label source-confirmed target readings, distinct similar names, rejected noise and unresolved passages separately.

A successful search can still have incomplete coverage. A completed zero-hit query describes that query and scope; it does not exclude a person whose record or spelling has not been tested. When a newly attested form changes an earlier negative, rerun the affected searches and amend that specific conclusion. Do not infer kinship from the rescued name hit.

For checking the source images and unreadable gaps, use [archival-image-coverage-verification.md](archival-image-coverage-verification.md). Sources and synthesis limits: [source notes](../sources/corpus-seeded-name-search.md).
