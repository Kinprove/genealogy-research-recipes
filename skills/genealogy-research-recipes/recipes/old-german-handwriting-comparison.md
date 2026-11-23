---
id: "old-german-handwriting-comparison"
title: "Test a reading of an old German handwritten word"
summary: "Compare a disputed Old German word with script samples, generated candidate forms and examples in the same hand."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "OLD-GERMAN-HANDWRITING-COMPARISON-01", "text": "Use the original scribe’s repeated forms to decide between candidate readings."}]
handoff: ["ai-for-documentary-records", "german-register-image-recovery"]
checked: null
checked_basis: null
capabilities: {"browse": ["public catalogues, documentation and historical records"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool", "publish"], "contact": []}
router: {"section": "Records by country and region", "group": "Germany", "order": 101}
---

# Test a reading of an old German handwritten word

Use this recipe when one name, place or term in a German church or civil record controls the next search. Use the original scribe’s repeated forms to decide between candidate readings.

## Select a model for the word’s script

Use Archion’s alphabet table and examples for the relevant style. Check whether the scribe switched to Latin letterforms for the disputed word or name. Start with short words or names you can already read and locate two repetitions of the uncertain letter in the same hand before changing the transcription. [S1], [S2], [S5]

For early parish entries in the Czech lands, compare specimens of both Czech and German Neo-Gothic cursive. Give the German form (Kurrent) more weight as a comparison sample for later eighteenth-century entries and confirm the match against the scribe’s letterforms. [S5], [S6]

Check the entry’s language and keep Kurrent among the candidates for parish registers from the Czech lands after 1850, where German-language writing retained it after Czech-language writing shifted to Latin letterforms. [S5], [S7]

If the letter remains uncertain, compare its strokes with the German Script Tutorial practice sheets and then return to examples in the record itself. [S1], [S4]

## Build and test candidate readings

For an unfamiliar parish, skim later historical registers or indexes written in Latin script for local surnames and place names. Treat those spellings as candidates and test them against the older entry’s strokes. [S5]

If you know the entry’s language and the beginning of a word is hard to read, work backward from its last legible letters. Use the ending to propose possible readings and check their opening strokes against the scribe’s other words. [S5]

Sketch a candidate surname locally from the matching Kurrent alphabet and trace its strokes. Compare where the strokes turn or join at the disputed letters with the scribe’s forms. [S5], [S8]

## Compare proposed readings in the generator

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The candidate text goes to the Schrift-Generator. Apply the [privacy gate](../SKILL.md#privacy-gate) and substitute a non-identifying sample with the same letter sequence when the original contains personal details.

Enter a short candidate word in the Schrift-Generator and choose the matching script or comparison view. Compare the joining strokes and the disputed letters with the original. Treat the generated word as a comparison sample and record any remaining uncertainty in the transcription. [S1 @2026-11-18], [S3 @2026-11-18]

## Ask for a second reading

**Privacy gate:** <!-- privacy-gate: publish --> The scan link and partial transcription can reveal people named on the page. Apply the [privacy gate](../SKILL.md#privacy-gate) before sharing either with readers of the Genealogie forum.

If the disputed word still needs a second reading and the gate clears the material, post a focused request in the Genealogie forum’s Čtení starých materiálů section. Give the archival scan link and the entry’s position on the image. Identify the word and include your partial reading of the surrounding words in the record’s language, with gaps marked. [S5 @2026-11-22], [S9 @2026-11-22]
