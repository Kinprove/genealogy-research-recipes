Genealogy Research Recipes — Kinprove Claude Skill — Third-party content notice

This Skill package contains prompts and original documentation authored by
Kinprove and licensed under the Functional Source License 1.1 (MIT Future
License) — FSL-1.1-MIT — see LICENSE. Copyright 2026 Kinprove.

The package manifests state the licence as the SPDX expression

  FSL-1.1-MIT AND LicenseRef-Third-Party-Content

FSL-1.1-MIT covers Kinprove's original recipes, code and documentation.
LicenseRef-Third-Party-Content is defined in the next section. The release
date of every version, and the day it becomes available under MIT, are listed
in CHANGELOG.md inside the skill folder.

-----------------------------------------------------------------------------
LicenseRef-Third-Party-Content
-----------------------------------------------------------------------------
Third-party material that the package reproduces is not licensed by Kinprove
and keeps its own rights. This covers:

  - the Beider name-index data described below; and
  - a source's own expression in the passages credited "(quoted)" or
    "(adapted)" in the Credits list of a recipe's https://github.com/Kinprove/genealogy-research-recipes/blob/90e00fd9f529beee13a325a92eee4b61eb57c474/skills/genealogy-research-recipes/sources/<slug>.md file.

Kinprove grants no licence to this material, under FSL-1.1-MIT or otherwise.
Anyone who reuses it needs whatever permission its rights holder requires.

-----------------------------------------------------------------------------
Recipes, sources and Credits
-----------------------------------------------------------------------------
The one hundred and thirty-five recipes are original Kinprove-authored
distillations of genealogy judgment and practical workflows. Facts, methods,
and community teaching that a recipe cites but does NOT reproduce (for example
the Leeds Method, WATO / "What Are The Odds", the Genealogical Proof Standard)
need only source attribution and are credited in each recipe's
https://github.com/Kinprove/genealogy-research-recipes/blob/90e00fd9f529beee13a325a92eee4b61eb57c474/skills/genealogy-research-recipes/sources/<slug>.md — they are not carved out here.

Each https://github.com/Kinprove/genealogy-research-recipes/blob/90e00fd9f529beee13a325a92eee4b61eb57c474/skills/genealogy-research-recipes/sources/<slug>.md file ends with a Credits list, the package's rights
record. Every line names a source, its rights statement and one class:

  (kinprove-original)  Kinprove's own synthesis, under FSL-1.1-MIT.
  (quoted)             a short quotation, credited to its source.
  (adapted)            Kinprove's restatement of a source's facts or method,
                       or a short credited paraphrase or translation of a
                       brief passage.

Some Sources entries also carry a "Rights:" note; the Credits list remains the
rights record.

Kinprove uses facts, methods, procedures, register and locator data, and short
credited quotations. It does not relicense any source's expression.

Rights holders: if you believe a recipe reproduces your work beyond that,
write to hola@kinprove.io or open an issue at
https://github.com/Kinprove/genealogy-research-recipes/issues. Kinprove will
rewrite the passage in its own words or remove it.

-----------------------------------------------------------------------------
Beider name-index data
-----------------------------------------------------------------------------
The factual recorded-name/article mappings in
resources/beider-name-indexes.json (inside the skill folder) are adapted from
Nison's male and female Beider indexes on J-Roots Forum:

  https://forum.j-roots.info/viewtopic.php?f=98&t=2060#p32424
  https://forum.j-roots.info/viewtopic.php?f=98&t=2059#p32423

Dictionary articles are by Alexander Beider. Data was acquired on 2026-10-03
from complete first-post archive captures dated 2024-12-25; archive URLs and
source hashes are included in the JSON. Recorded names are normalized for
case, whitespace and hyphens while article alternatives are preserved.
Forum prose and discussion replies are excluded.

Basis: each row records a fact, namely that a recorded name appears under a
given article of Beider's dictionary. Kinprove treats these mappings as facts,
not protected expression, and reproduces them without a licence. No explicit
upstream data licence was identified, and permission was not requested. Some
jurisdictions protect a compilation or database regardless of its originality
(for example the EU database right and the Russian database-maker right), so
Kinprove grants no rights in these mappings: they fall under
LicenseRef-Third-Party-Content, not FSL-1.1-MIT. The JSON file repeats this in
its "rights" field. Kinprove removes the data at the request of the index's
compiler or of Alexander Beider.
