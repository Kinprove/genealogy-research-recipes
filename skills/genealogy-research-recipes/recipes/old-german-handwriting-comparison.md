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
capabilities: {"browse": ["public catalogues, documentation and historical records"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Germany", "order": 96}
---

# Test a reading of an old German handwritten word

Use this recipe when one name, place or term in a German church or civil record controls the next search. Use the original scribe’s repeated forms to decide between candidate readings.

## Select a model for the word’s script

Use Archion’s alphabet table and examples for the relevant style. Check whether the scribe switched to Latin letterforms for the disputed word or name. Locate two repetitions of the uncertain letter in the same hand before changing the transcription. [S1], [S2]

If the letter remains uncertain, compare its strokes with the German Script Tutorial practice sheets and then return to examples in the record itself. [S1], [S4]

## Compare proposed readings in the generator

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The candidate text goes to the Schrift-Generator. Apply the [privacy gate](../SKILL.md#privacy-gate) and substitute a non-identifying sample with the same letter sequence when the original contains personal details.

Enter a short candidate word in the Schrift-Generator and choose the matching script or comparison view. Compare the joining strokes and the disputed letters with the original. Treat the generated word as a comparison sample and record any remaining uncertainty in the transcription. [S1 @2026-11-18], [S3 @2026-11-18]
