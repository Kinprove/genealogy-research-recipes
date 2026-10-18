# Sources: corpus-seeded name search

Primary pages opened 2026-10-18; cited as references, not reproduced.

- **S1. Unicode Consortium, [UAX #15: Unicode Normalization Forms](https://www.unicode.org/reports/tr15/)**, sections 1.1–1.3. Distinguishes canonical/compatibility equivalence and warns that compatibility transformations can remove meaningful distinctions. It does not prescribe name-search masks or removal of Hebrew points.
- **S2. Unicode Consortium, [The Unicode Standard, chapter 9, Hebrew](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-9/)**, sections 9.1.1–9.1.2. Describes separately encoded final letters, Yiddish digraphs and presentation forms. It does not instruct researchers to equate different spellings. A local Python `unicodedata` check also confirmed that NFKD leaves the three Yiddish digraph characters and five final letters intact.
- **S3. JewishGen, [Transcription Rules for JewishGen Databases](https://www.jewishgen.org/databases/%24transcription.html)**, name/town fields and section V. Supports the distinction between displayed text and hidden fields used for typed-field indexing.
- **S4. JewishGen, [Revision Lists for Belarus](https://www.jewishgen.org/databases/Belarus/BelarusRevisionLists.htm)**, given-name search instructions. Documents a phonetic-search miss involving a diminutive; the collection-specific example does not measure every engine's recall.

Corpus attestation, positive-control queries, surface-form review and separately labelled search lanes are workflow synthesis. No percentage improvement, universal consonant swap or claimed complete name inventory is asserted. Dictionary membership, search counts and successful normalization provide no person-identity or kinship proof.
