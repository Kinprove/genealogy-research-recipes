# Recipe: Corpus-seeded name searches across scripts and OCR

Use when a remembered spelling, transliteration or name dictionary fails to retrieve a person from Hebrew/Yiddish or other historical text. This recipe owns retrieval diagnostics. Use [beider-given-name-variants.md](beider-given-name-variants.md) for dictionary candidates and [jewishgen-search-family-reconstruction.md](jewishgen-search-family-reconstruction.md) for database-specific family searches.

## Build a small attestation inventory

Read candidate-bearing passages in the available corpus before fixing the search pattern. Retain each literal surface form, source/page, surrounding words, possible name role and confidence. For a large corpus, use bounded discovery batches; report which portions were actually examined. With only a remote search interface, seed from returned passages and existing records rather than claiming a full-corpus pass.

Keep observed spellings, dictionary forms and generated possibilities in separate columns. A remembered list is a starting set, not an exhaustive inventory; corpus discovery is also not a guarantee of completeness. Review matched surface forms with context before interpreting counts. Short stems can match ordinary words, place names and unrelated surnames.

Determine whether each token is a given name, compound-name component, patronymic, surname, occupation or another descriptor. Do not discard an occupational-looking token categorically: it may function as a surname in the particular record. Search the plausible roles separately when unresolved. Neither a descriptive title nor an occupational surname by itself proves that two people had the same occupation.

## Diagnose three different failures

| Failure | Controlled comparison | Limitation |
| --- | --- | --- |
| Encoding | Original text versus a documented normalized search copy | Equivalent encoding does not generate other spellings |
| Orthography or name form | Attested language/script forms, compound-name components and dictionary candidates | A linguistic candidate is not a same-person link |
| OCR/extraction | Distinctive shorter spans; observed line breaks, spaces or letter confusions | A repaired search string is not a corrected transcription |

For local Hebrew/Yiddish text, Unicode normalization can reconcile some encoding differences. Decomposition followed by removal of selected Hebrew combining marks is an additional, lossy search transform; normalization alone does not strip points. Apply any such transform to both pattern and search text, preserve the originals and verify retrieved passages. [S1]

Hebrew final letters and Yiddish digraph characters are separately encoded. If needed for retrieval, explicitly test final-to-medial folding (`ךםןףץ` → `כמנפצ`) or digraph expansion (`װ/ױ/ײ` → `וו/וי/יי`) in a search copy. These are application choices, not effects guaranteed by NFC/NFKD or instructions to rewrite source spelling. They can merge distinct strings; inspect the resulting homographs. [S1, S2]

Removing points does not supply missing vowel letters, convert one surname spelling into another or resolve Hebrew versus Yiddish orthography. Add consonant substitutions only as bounded exploratory lanes motivated by the source, observed OCR errors or linguistic evidence. There is no universal substitution mask that proves coverage of every Slavic name in Hebrew script.

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

JewishGen's transcription rules allow hidden “Other Surnames” and “Other Towns” fields to make names in comments searchable in typed fields. Their existence does not show they were populated in a particular collection. Compare free-text and typed-field retrieval where supported. [S3]

Phonetic search is another candidate lane: JewishGen's Belarus instructions explicitly document name forms that it misses. It cannot replace searches for attested alternatives. [S4]

## Stop with a scoped result

Keep the corpus/index version or access date, field, exact Unicode query, filters, transformation policy, inspected portions and result identifiers. Separate occurrences, unique records/books and identified people. Label source-confirmed target readings, distinct similar names, rejected noise and unresolved passages separately.

A successful search can still have incomplete coverage. A completed zero-hit query describes that query and scope; it does not exclude a person whose record or spelling has not been tested. When a newly attested form changes an earlier negative, rerun the affected searches and amend that specific conclusion. Do not infer kinship from the rescued name hit.

For checking the source images and unreadable gaps, use [archival-image-coverage-verification.md](archival-image-coverage-verification.md). Sources and synthesis limits: [source notes](../sources/corpus-seeded-name-search.md).
