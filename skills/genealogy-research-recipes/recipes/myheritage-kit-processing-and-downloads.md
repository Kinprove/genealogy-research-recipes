---
id: "myheritage-kit-processing-and-downloads"
title: "Identify the processing and file type of a MyHeritage DNA result"
summary: "Identify how MyHeritage processed a kit, distinguish its raw autosomal file from CRAM, and check options for a legacy result."
kind: "platform"
scope: {"platforms": ["MyHeritage"], "tasks": []}
privacy: "genetic-third-party"
gates: ["privacy-transfer"]
guardrails: [{"id": "MYHERITAGE-KIT-PROCESSING-AND-DOWNLOADS-01", "text": "Identify the kit’s processing method from the file header before interpreting it."}]
handoff: ["dna-comparison-controls", "ai-for-dna-research"]
checked: "2026-11-18"
checked_basis: "Read 2026-11-18"
capabilities: {"browse": ["public catalogues, documentation and historical records"], "local_script": [], "extensions": [], "data_transfer": ["export", "request", "upload"], "contact": []}
router: {"section": "DNA", "group": "DNA testing sites and tools", "order": 30}
---

# Identify the processing and file type of a MyHeritage DNA result

Use this recipe if you need to distinguish an uploaded array result from a sequenced kit, or select a file for the research question. Identify the kit’s processing method from the file header before interpreting it. Apply the [DNA privacy rules](ai-for-dna-research.md#verification--privacy-discipline) before handling a kit.

## Inspect the kit locally

**Privacy gate:** <!-- privacy-gate: export --> The tester’s raw genotype file leaves MyHeritage for the user’s own device. Apply the [privacy gate](../SKILL.md#privacy-gate) and its local retention rule.

Download the regular raw DNA file to the user’s own device if a copy is required. Open only the file header to check for the platform’s processing description. Record the method and kit date in the research log, keeping an ambiguous or missing header unresolved. [S1 @2026-11-18], [S2 @2026-11-18], [S4 @2026-11-18]

## Interpret low-pass coverage and imputation

For the 2× low-pass implementation described by MyHeritage, read 2× as mean depth across positions. Individual sites can differ from that average. Treat an imputed genotype as a statistical estimate and distinguish it from a directly observed read when documenting your evidence. [S1]

## Choose the file that answers the question

**Privacy gate:** <!-- privacy-gate: export --> The tester’s extended genomic data leaves MyHeritage for the user’s own device. Apply the [privacy gate](../SKILL.md#privacy-gate) to the export and assess any later transfer separately.

Choose the regular raw autosomal file when the task expects a genotype file. Choose the **Specialized Genomic CRAM File** for sequence reads from a MyHeritage kit processed with WGS. Download the CRAM locally only when the research question requires it. [S1 @2026-11-18], [S2 @2026-11-18]

## Check options for an array result

**Privacy gate:** <!-- privacy-gate: upload --> The tester’s biological sample and kit identifiers would go to MyHeritage and its laboratory. Confirm the tester’s authorization and apply the [privacy gate](../SKILL.md#privacy-gate) before submission.

If the kit contains only an uploaded array file and the research requires WGS, use a new MyHeritage cheek-swab kit for the tester’s physical sample. Keep the old result and the newly processed kit distinct in your log. [S1 @2026-11-18], [S4 @2026-11-18], [S5 @2026-11-18]

**Privacy gate:** <!-- privacy-gate: request --> The tester’s kit information and consent go to MyHeritage and its laboratory and authorize a new use of the stored sample. Apply the [privacy gate](../SKILL.md#privacy-gate) before requesting processing.

If the tester already has an eligible stored backup vial, request processing of the stored sample only after confirming that WGS is offered for that sample and country and obtaining the tester’s explicit consent. Record the new kit’s processing method from its own header. [S1 @2026-11-18], [S3 @2026-11-18]
