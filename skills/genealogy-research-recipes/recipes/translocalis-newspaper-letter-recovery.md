---
id: "translocalis-newspaper-letter-recovery"
title: "Find Finnish newspaper letters by signature, author and place"
summary: "Recover attributed, unsigned and reprinted Finnish newspaper letters using Translocalis signature, author and sending-locality metadata."
kind: "records"
scope: {"platforms": [], "tasks": ["Translocalis clippings", "paikalliskirjeet", "Finnish reader letters"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "TRANSLOCALIS-NEWSPAPER-LETTER-RECOVERY-01", "text": "A signature search alone cannot close an inventory of a writer’s letters."}]
handoff: ["historical-newspaper-section-search", "evidence-proof-judgment"]
checked: null
checked_basis: null
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 233}
---

# Find Finnish newspaper letters by signature, author and place

Use this recipe to find a letter printed in the nineteenth-century Finnish-language press or to test
an attribution or suspected reprint. For an article outside the project’s scope, use [newspaper
section search](historical-newspaper-section-search.md).

## Search signature and author separately

Start with the National Library of Finland’s [Translocalis
collection](https://digi.kansalliskirjasto.fi/collections?id=742). Use it for local readers’ letters
in the Finnish-language press through 1885 [S2 @2026-11-22], [S3 @2026-11-22], [S4 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The signature and author searches send the identifying terms you enter to the Digi Translocalis collection. Apply the privacy gate in the skill instructions before submitting a signature, name or other identifying term.

In the collection keywords, search `translocalis_104` for the printed signature, including an
initialled form or pseudonym. Run a separate `translocalis_105` search for the attributed writer’s
name. In a general clipping keyword list, use the Translocalis field code to identify the matching
metadata rather than reading a similarly worded keyword from another collection as a Translocalis
attribution [S3 @2026-11-22], [S4 @2026-11-22].

A signature search alone cannot close an inventory of a writer’s letters. Compare the abbreviated
signature and the reported locality with the proposed writer’s names and known locality. Record the
catalogue attribution as a lead and keep the identification provisional while corroboration is
missing. According to the community author, the attributed-name field recovered letters whose
signatures omitted the full surname [S1†].

## Look for reprints and unsigned versions

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The full-text fallback sends the chosen excerpt from the letter to Digi. Check the phrase for identifying or private details before submitting it. Prefer a distinctive non-identifying phrase and apply the privacy gate in the skill instructions before submitting any identifying text.

Read *toisinto* as a reprint. If the author keyword misses, search Digi’s newspaper text for a
distinctive phrase from the letter, then compare wording and publication dates across newspapers [S2],
[S3]. According to the community author, a reprint found by word search had no author metadata [S1†].

Browse the Translocalis sending-locality keyword (`translocalis_101`) for unsigned versions and
reprints. For a place in Finland, start with the project’s 1860 municipality label. Try the 1885 label
under `translocalis_102` if the municipality changed [S4 @2026-11-22].

On a known Digi issue page, turn on **Korosta leikkeet** and check whether the letter itself is
highlighted. Verify the collection on a matching clipping before counting it as Translocalis coverage
[S4 @2026-11-22], [S5 @2026-11-22]. According to the community author, a known letter had no
highlighting in the 2023 interface [S1† @2026-11-22]. Check the issue in the current viewer and keep
the letter in the research even if no Translocalis clipping is visible.

Return the issue date, title, page and clipping locator for each printing, with its literal signature,
who supplied any author attribution and the evidence linking the printings. Keep a recorded reprint
distinct from independent reporting.

[Source bibliography and credits](https://github.com/Kinprove/genealogy-research-recipes/blob/2b4157d8449d36b2a0e62fb1f75fe9f581deb15a/skills/genealogy-research-recipes/sources/translocalis-newspaper-letter-recovery.md).
