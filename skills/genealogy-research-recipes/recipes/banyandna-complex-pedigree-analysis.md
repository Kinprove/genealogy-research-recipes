---
id: "banyandna-complex-pedigree-analysis"
title: "Test a complex pedigree in BanyanDNA"
summary: "Test a pedigree with more than one relationship path using BanyanDNA validation and alternative placements with documented autosomal comparisons."
kind: "platform"
scope: {"platforms": ["banyandna"], "tasks": []}
privacy: "genetic-third-party"
gates: ["privacy-transfer"]
guardrails: [{"id": "BANYANDNA-COMPLEX-PEDIGREE-ANALYSIS-01", "text": "Read the result as conditional on the paths represented in the project."}]
handoff: ["ai-for-dna-research", "cousin-relationship-paths", "dna-comparison-controls", "unknown-parentage-wato"]
checked: "2026-11-22"
checked_basis: "Opened 2026-11-22"
capabilities: {"browse": ["record catalogues and documentation"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool"], "contact": []}
router: {"section": "DNA", "group": "DNA testing sites and tools", "order": 37}
---

# Test a complex pedigree in BanyanDNA

Use this recipe when documented pedigree collapse, double cousins or other multiple paths make a single-path shared DNA estimate an unsuitable test. Sketch the paths and plausible alternatives locally before opening a project.

## Set up the pedigree and comparisons

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Before entering data, clear the [privacy gate](../SKILL.md#privacy-gate) and follow the [DNA consent and redaction rules](ai-for-dna-research.md#verification--privacy-discipline) for the living testers’ relationship paths, labels and pairwise shared cM sent to BanyanDNA. Check the project’s visibility and use the minimum agreed data.

Enter the permitted pedigree and pairwise cM in BanyanDNA. Represent each known relationship in the project. Enter each measured pair under the two people compared, including pairs involving additional testers when permitted. Keep a local record of the provider and reporting basis for each value. According to the developer interview, comparisons from several testing sites can be entered into the same project [S1† @2026-11-22]. Check their reporting basis with [DNA comparison controls](dna-comparison-controls.md) before combining them [S3 @2026-11-22].

## Validate a proposed pedigree

In the Calculations panel, run validation against the proposed pedigree. Compare each pair’s observed cM with the simulated average and spread. Read flags as a cue to inspect the comparison and its documented paths. Recheck the entered value, the two profiles and the relationships represented, especially where more than one pair challenges the same placement [S2 @2026-11-22] [S3 @2026-11-22].

Read the result as conditional on the paths represented in the project. Where endogamy likely created paths beyond the oldest documented ancestors, leave those paths unresolved. Record whether the model accounts for the extra sharing before using the result to choose a placement [S2].

## Compare plausible placements

Create separate hypotheses for the proposed positions of the person whose placement is uncertain, and run the hypothesis calculation. Compare the relative scores only across the placements tested in that run. Investigate the higher-scoring placements using records or independent comparisons that could distinguish them. Keep the tested alternatives and the unresolved relationships with the run notes [S3 @2026-11-22].
