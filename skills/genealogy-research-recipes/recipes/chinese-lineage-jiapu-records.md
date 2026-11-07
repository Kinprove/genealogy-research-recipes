---
id: "chinese-lineage-jiapu-records"
title: "Recover a Chinese emigrant's lineage from character-written names, village and jiapu"
summary: "Recover a Chinese emigrant's character-written name and ancestral village before searching lineage genealogies (jiapu)."
kind: "records"
scope: {"platforms": [], "tasks": ["Recover a Chinese emigrant's character-written name and ancestral village before searching lineage genealogies (jiapu)."]}
triggers: ["Recover a Chinese emigrant's character-written name and ancestral village before searching lineage genealogies (jiapu)"]
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "CHINESE-LINEAGE-JIAPU-RECORDS-01", "text": "never derive a character from a romanization, and keep each romanization, port and generation-character match as its own observation."}]
handoff: []
checked: "2026-11-07"
checked_basis: "checked 2026-11-07"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"tier": "pointer", "group": "Migration and origins", "order": 1115}
---

# Recover a Chinese emigrant's lineage from character-written names, village and jiapu

Use when a Western record (manifest, obituary, census, family group sheet) names a Chinese
emigrant only in romanization, and the goal is a lineage genealogy (jiapu/zupu). Recover the name
and small ancestral village **in characters** first. Record every romanization, port, regional
label, woman's name formula, generation-character match and computed date as its own labelled
observation. Do not merge them into an identity. For the general rule that a port of embarkation is not a birth
town, see [arrival-record extraction](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/russian-empire-emigrant-origin-recovery.md).
Route identity rulings to [evidence/proof judgment](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md)
and AI transcription of characters to [AI for documentary records](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/ai-for-documentary-records.md).

## Contents

- Set two prerequisites before placing anyone
- Never derive a character from a romanization
- Build the name/place register
- Search jiapu collections by exact character and county
- Place the ancestor as a hypothesis
- Keep literal dates apart from derived values
- Close with a lineage packet

## Set two prerequisites before placing anyone

Do not place anyone in a jiapu until you hold two things in characters:

1. The name of the **last emigrant**, i.e. the ancestor who last left China or another country.
   The surname is written first, normally as one character, followed by a given name of
   normally two characters. [S1], [S2]
2. The **small ancestral village**, not a province, city or port. [S1], [S2], [S4]

You may search for **candidate books** before both are complete. To do so you need the surname
character from a character-written source, plus a county, ancestral hall or region clue. If the
village is unknown, start at county level. [S5] Log every book found this way as a candidate.

Look for these in sources that write characters:

- a family-held jiapu (the presenter says keeping it was the eldest son's duty);
- family group sheets annotated with characters;
- tombstones, which can give both the village and the name;
- Chinese association histories or officer lists. [S1], [S2]

**Privacy gate:** <!-- privacy-gate: request --> An exclusion-file request can disclose an
emigrant's identity and sensitive family links, including relatives who may be living. Answer
the privacy gate in `SKILL.md` before sending a request or supporting identity documents.

For emigrants to the United States, also check **Chinese Exclusion Act case files in NARA
RG 85**. They can contain Chinese names, village maps, family details and interrogation
statements. Use the port or immigration office and case references to locate the relevant
series. Before requesting a file, verify its current NARA custodian and access rules. The exclusion laws operated in
1882–1943, but individual series and files can extend beyond those dates. NARA's older
holdings guide is a starting point, not a current facility list. [S7]

Keep a claimed immigration identity separate from the person's other names and family links.
Some files contain coaching material for a **paper-son identity**, a claimed relationship used
for admission. Neither that relationship nor the village and family memorized for it is
automatically the emigrant's biological lineage. Compare independent character-written
sources before selecting a jiapu. [S7]

Treat English obituaries and immigration romanizations as leads only. In the presenter's Hawaii
example, the obituary's romanization did not resemble the real name. Even an overseas
obituary's printed **characters** were wrong in that example, while the association record had
the correct ones. [S1], [S2] If you have no surname character from a character-written source,
report that the search is blocked. Do not guess.

## Never derive a character from a romanization

Do not convert a Western spelling into one Pinyin character. Wade-Giles and Pinyin spell the same
character differently, and Mandarin and Cantonese read it differently. For example, Wade-Giles
*ts'ai* and Pinyin *cai* are the same syllable. One English spelling can also stand for several
distinct surnames. [S2], [S5] Narrow a romanized surname with:

- the family's dialect;
- the destination country;
- any remembered meaning of the name;
- a relative who reads Chinese. [S4]

A surname tool that weights region and dialect can propose candidates. Check each candidate
character's alternative readings and older or variant forms, because published genealogies may
print an older form. [S5] Keep every candidate as a candidate until a character-written source
confirms it.

## Build the name/place register

Give each source its own row: source, literal romanized form, literal character form (or
"none"), and a role label. Never collapse rows into one "correct spelling".

- **Name types.** A man can carry a genealogical name, a courtesy name, a pseudonym or alias,
  and a taboo name. Record which one the jiapu entry headlines. Keep Western-record forms,
  including a wrong surname the family used, as labelled alternates. In the presenter's example
  the family used "Fong" although the lineage surname was Kwang/Kwong. [S3]
- **Ports.** Hong Kong, Macau and Canton are ports of embarkation. Most emigrants of 1850–1950
  came from the countryside and left through these ports, and arrivals often answered "where
  from" with the port they had just left. By default, classify these as port tokens and keep
  looking for the village. [S3], [S4]
- **Regional labels.** "See Yup", "Sze Yup", "Siyi" or "CF" written beside a name refers to
  the Siyi four-county region on the west side of the Pearl River Delta: Taishan (Toishan),
  Xinhui (Sunwui), Kaiping (Hoiping) and Enping (Yanping). It is not a given name or surname. The
  presenter has seen it entered as a woman's name on group sheets and as an alias. File it as a
  region clue that narrows the county search. [S3]
- **Women's formulas.** Read husband's surname + natal surname + 氏 as "of the X family", not
  as a personal name. The presenter's tombstone example is romanized "Fong Wong Shee". He reads
  it as: husband's lineage surname (Kwang/Kwong, which the family wrote as "Fong"), natal family
  Wong, and 氏 "of the family". Take the surname character from a character-written source
  such as the jiapu or the stone itself, not from either romanization. Expect a role character
  for "mother" or "wife" before or in place of a name on tombstones and in jiapu entries. Record
  the natal surname as a clue. If the entry gives only the natal surname + 氏 or a role
  character, record the personal name as **unknown**. Do not invent or infer one. Personal names
  are seldom recorded, but if the source does record one (for example after the "mother" role
  character), transcribe it literally. [S1], [S2]

## Search jiapu collections by exact character and county

The presenters (2019, 2022) describe FamilySearch's Chinese genealogy collection as about 13
million images that you had to browse by surname and then place. [S3], [S5] That is now out of
date. FamilySearch has a dedicated Jiapu Search by surname, ancestral village, ancestral hall
name, first ancestor's name or generation name. It also has advanced image-search filters and a
map browse covering more than 65,000 jiapu. Individual names inside the books are still **not
indexed**, so once you find a book you page through its available images. [S6]

**Access check, 7 November 2026:** FamilySearch's help page carries a notice that access to certain Chinese family records is suspended while it reviews privacy laws, contracts and
technology. Read the current notice and check the particular book's image access before
calling it viewable. Keep a restricted or unavailable book separate from a search with no
candidate title; neither establishes that no jiapu survives. [S6]

The procedure:

1. Choose the surname by its **exact character**. In the presenter's example, several surname
   entries shared one romanization.
2. Choose the ancestral county, and the village or ancestral hall if you have it.
3. Review **every** jiapu that matches. There are often several. [S3]

For each book, log:

- the title;
- the edition type. A copy can be a later reconstitution: the presenter's example was rebuilt in
  1986 after the original was destroyed;
- the search fields and values used;
- the page/image extent you actually inspected. [S3]

If the collection has no match, the presenter names these fallback holders:

- the lineage keeper among living relatives;
- the ancestral village hall, temple or shrine;
- the Shanghai Library: first check its [Genealogy Knowledge Service Platform](https://jiapu.library.sh.cn/)
  for catalogue entries and available digitized texts/images. The platform launched in 2016;
  the presenter's reading-room experience is not a current requirement for every title.
  Check access for the specific edition and volumes, then ask about on-site holdings or copies
  for material unavailable online. A catalogue entry does not guarantee image access. [S8]
- booksellers. His example family's book turned up by chance in a Hong Kong bookstore. [S1], [S3]

Record each fallback as checked, unchecked or inaccessible. A failed search is not evidence that
no jiapu exists.

On My China Roots, expect the same name to appear in several same-surname books from different
regions. Filter by the native place known from an independent source, such as a tombstone. Then
check that the parents' and children's names match before tracing back one generation at a time.
A name hit alone is not identity. [S4] Its presenter (2024) describes the family tree books as
full-text searchable but not yet name-indexed, with results filterable by province. [S4]

## Place the ancestor as a hypothesis

- Read **this branch's** generation poem and naming instructions. The generation character can
  be the first or second character of the given name; check whether its position alternates.
  Do not borrow another branch's sequence. Only after establishing the applicable poem and
  generation number, counted from the founding migrant ancestor, use it to narrow browsing.
  [S1], [S3], [S9]
- A matching character or poem does not establish a shared lineage between same-surname
  families. A generation-character match does not identify a person either.
  Branches can use different sequences, and a shared sequence is not a substitute
  for village and recorded parent/child links. An emigrant's overseas school, courtesy or
  paper name may have no generation character; leave the generation unresolved rather than
  forcing that name into a poem. The presenter also notes looser practice in recent generations
  and near-homophone characters within a generation. [S1], [S3], [S7], [S9]
- If you place someone in a blank slot or as a missing sibling, write it up as a hypothesis and
  name each piece of supporting evidence (for example: a gravestone naming the village, a
  matching generation character, known brothers). The presenter's "about 95%" confidence is his
  own judgment, not a measure. [S2], [S3]
- A jiapu can omit a brother proven elsewhere. Treat absence from the jiapu as a possible
  omission. [S2]

## Keep literal dates apart from derived values

- **Imperial dates.** Transcribe reign title, regnal year, month and day literally. Note when a
  stone mixes imperial and Western dates. [S1], [S2] Count regnal years from the era's first year
  (元年). Tongzhi year 1 = 1862. The change of era name in 1861 did not make 1861 Tongzhi year 1;
  keep accession, enthronement and the era's first year distinct. [S10]
  The sum 1861 + N gives only the Gregorian year in which Tongzhi year N **begins**. Each
  regnal year starts at the Chinese New Year, so its last lunar months can fall in January or
  February of the next Gregorian year. Convert the complete date (regnal year, month and day) with
  a lunisolar conversion table, and take the Gregorian year from the table, not from the
  arithmetic. Keep the literal form beside the result. Never read the lunar month as a Western
  month.
- **The presenter's worked example is wrong.** He converts Tongzhi 9, month 8, day 14 to
  14 August 1871 by counting from 1861 and reading the eighth lunar month as August. [S1], [S2]
  Tongzhi 9 began in 1870, and the example's month 8, day 14 falls in early September 1870, not August.
  Take the exact day from a conversion table before recording it. Do not reuse 1871.
- **Computed birth year.** A year estimated from the founder's birth date (1104 in the
  presenter's example) divided across the generation count is an estimate. Label it with its
  basis. The presenter himself calls 10–20 years of accuracy the best achievable. [S3]
- **Assumed birthplace.** A birthplace taken from the lineage village is an assumption. The
  presenter notes jiapu rarely state birthplace. [S3]
- **Placeholder wife.** A placeholder for an unnamed wife inferred from recorded children, and
  any estimated age gap or residence for her, are the presenter's working conventions, not
  observations. He says he is unsure they are the official method. Keep any recorded natal
  surname as the only observation. [S3]

## Close with a lineage packet

Return:

- the name/place register;
- classified place tokens (port, region, village);
- women's entries, each with the natal surname and the personal name as recorded, or the personal
  name marked unknown when the source gives only surname + 氏 or a role character;
- the jiapu search log: surname character, county/village, search fields used, books and pages
  reviewed, edition type, candidate or confirmed status, fallback holders checked;
- the candidate placement with its generation-character and family-name checks and their limits;
- literal dates alongside labelled derived values, with the conversion table named;
- the next source that could close the identity gap.
