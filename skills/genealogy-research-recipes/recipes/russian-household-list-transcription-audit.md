---
id: "russian-household-list-transcription-audit"
title: "Audit a transcription of a Russian confession list or revision list against the images"
summary: "Audit a transcription of a Russian confession list or revision tale against the images, keeping names, kin terms and counts as written."
kind: "records"
scope: {"platforms": [], "tasks": ["Audit a researcher's, volunteer's or model's transcription of a Russian Orthodox confession list (исповедная ведомость) or revision tale (ревизская сказка) against the images.", "Audit a spreadsheet of Russian household-list entries", "проверить расшифровку исповедной ведомости или ревизской сказки"]}
privacy: "none"
gates: []
guardrails: [{"id": "RUSSIAN-HOUSEHOLD-LIST-TRANSCRIPTION-AUDIT-01", "text": "**Record what the image says, even against other years.**"}]
handoff: ["ai-for-documentary-records", "evidence-proof-judgment", "historical-place-name-resolution", "russian-orthodox-confession-list-reading", "russian-revision-list-household-chaining", "russian-village-family-reconstitution"]
checked: "2026-11-10"
checked_basis: "opened 2026-11-10"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Russian Empire and Soviet Union", "order": 69}
---

# Audit a transcription of a Russian confession list or revision list against the images

Use this recipe when you check a transcription of a Russian Orthodox confession list or a revision tale against the images: a researcher's spreadsheet, a volunteer index, or your own or a model's first reading. The result is a list of proposed corrections that the researcher can accept or reject, each with its evidence.

An audit goes wrong in a few predictable ways:

- Fields are compared row by row, so a person who is missing from the transcription is never noticed.
- A disputed digit or letter is settled against a general idea of the script, not against the same scribe's hand.
- A reading is "confirmed" by another transcription, or by a list copied from the same one.
- Relationship chains are flattened, and names and kin terms are normalised.
- The image is corrected toward what other years say.
- The researcher's own additions, or columns left out on purpose, are reported as errors.

The reading itself is covered elsewhere. This recipe adds only the audit steps.

- **Confession lists.** Layout, attendance columns, ages and names: [reading confession lists](russian-orthodox-confession-list-reading.md).
- **Revision lists.** Copies, age pairs, formulas and household chaining: [revision-list household chaining](russian-revision-list-household-chaining.md).
- **Handwriting and AI readings.** Same-clerk letter comparison, period kin terms, and the rule that several readings of one image are one chain: [AI for documentary records](ai-for-documentary-records.md).
- **Places.** An unidentified place: [historical place-name resolution](historical-place-name-resolution.md).
- **The final ruling.** Identity and relationship conclusions: [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- 1\. Count the people before you compare fields
- 2\. Settle a disputed glyph against the same scribe
- 3\. Tie each age to its person
- 4\. Read the household as the scribe wrote it
- 5\. Read names against the household and the other years
- 6\. Read ages and dates as the scribe produced them
- 7\. Check each item against the other years and the other source's image
- 8\. Keep what is not an error out of the error list
- 9\. Present disputed readings and record the ruling
- Output

## 1. Count the people before you compare fields

A field-by-field read finds wrong values, not a person the transcriber left out. Count first.

- **Use the list's own numbers.** In a confession list the first columns carry the running numbers of the household, of each male and of each female. [S13] The tenth-revision form that BYU transcribes has a male half and a female half, each with its own column of those now present. [S19] For each household, count the people in the transcription against those numbers. A skipped number or a number used twice marks a missing or doubled person.
- **Reconcile the totals person by person.** A confession list can total households and male and female souls [S13]. In the 1858 Radyvyliv revision the male total appears to count households, while the female total agrees with the entries [S31]. Check the original subtotal and both halves of the list before reporting a missing person.
- **Count both halves of a revision.** A daughter or a widow can stand only in the female half. Read the female half against the male half household by household ([step 4](#4-read-the-household-as-the-scribe-wrote-it)).

## 2. Settle a disputed glyph against the same scribe

Start from the same-clerk rule in [AI for documentary records](ai-for-documentary-records.md#generate-candidates-for-an-uncertain-german-word). An audit adds four checks.

- **Use the scribe's own forms, not a chart.** The National Archives' transcription tips say letters "will often appear similar or standard throughout a handwritten document by the same scribe". [S1] Wikipedia's article on skoropis notes that each scribe had his own letter forms, so a vague place must be compared "with already read parts of the same text". [S4] BYU's Russian tutorial warns that a letter may not appear on its alphabet charts at all, and that one document can hold several styles of the same letter. [S2] For a digit, compare it with the same scribe's other numbers and dates on the page. BYU's French numbers page recommends checking other records by the same scribe "to ensure the correct reading of a particular number". [S3]
- **Confirm the reference sample first.** Pick a word whose reading is fixed by something else, such as a formula word or a name confirmed in another list. The National Archives' tips start from a phrase that "doesn't often have any spelling surprises". [S1] A misread reference passes its error to every reading built on it.
- **Put the two disputed glyphs side by side.** Two digits that each look like a reference 4 can still differ from each other. The National Archives' tips reason the same way within one word: if one letter is an "e", the look-alike next to it "probably isn't". [S1]
- **Keep a stroke rule for each scribe.** BYU suggests making your own alphabet chart of how a scribe writes each letter. [S2] Record a feature such as the direction of a digit's top hook with that scribe and that list, and do not carry it to another hand.

Two Russian features change names:

- **Old letter forms.** In 18th-century скоропись в could be written as a quadrilateral or lying on its side. [S5] When a clear-looking reading contradicts every other list, suspect your letter model before you suspect the scribe.
- **Raised letters.** Выносные буквы are written above the line, "хотя они и составляют часть слова, остающегося в строке", and at first they marked an omitted ъ or ь. [S5] Read the raised letter as part of the name, and test each candidate name against the other years.

## 3. Tie each age to its person

Trace the line from the person’s running number through to the age. A crowded page makes it easy to take a value from an adjacent row [S6]. According to Kinprove’s private audit notes, the researcher reported a sloping line with the age above the name [S26†]. Check the parent’s and child’s rows together.

## 4. Read the household as the scribe wrote it

- **A dead father can still name the household.** A 1748 heading names Vasily Nikiforov as deceased and introduces children born since the previous revision [S14]. Enter the sons listed in the body. Look for the father in the previous revision or a confession list.
- **Follow the person named in each possessive.** A relationship can refer to the head or to another member [S19]. In one 1850 transcription «Кузьмин сын Василий» names Kuzma as father, then «Никифора Петрова другой сын Иван» returns to Nikifor [S15]. The 1816 phrase «Естифеевы сыновья» likewise introduces Estifey’s sons [S16]. Add a level if necessary and leave an ambiguous attachment open. See [confession-list layout](russian-orthodox-confession-list-reading.md#2-read-the-layout-before-the-names).
- **Preserve the original relationship and its referent.** An 1817 translation gives “Iosel’s son” in the comments but adds “[Nephew]” in the relation-to-head column. The brackets mark the translator’s inference [S18]. Keep a separate field for that interpretation.
- **Cross-check the two halves of the revision.** A wife or daughter may appear only on the female side [S19]. Identify whom a phrase such as «Ивана Мартынова жена» names, then follow «его же дочери» back to the same man [S17]. Compare the male entries before linking the row to a father or son of similar name.
- **Keep period kin terms as written.** Dal gives several affinal meanings for зять [S20] and says приемыш can refer to a child taken into the family or regionally to a son-in-law taken into the house [S21]. An 1817 translator renders a six-year-old’s entry as “Son-in-law (primak)” [S18]. Preserve the term and source before proposing any marriage. Add a more specific relation in brackets only with its supporting record. See [period kin terms](ai-for-documentary-records.md#what-to-never-trust-or-delegate-verify-or-dont).
- **In an entry without a surname, read the second name element as a patronymic form.** Where a revision entry gives only the head's given name and patronymic, the son's patronymic follows the father's given name: in Wikipedia's example, Прокопий Иванов's son Василий is Василий Прокопьев, "а вовсе не Иванов". [S22] Wikipedia calls such forms in older entries, as in «посиделец Ивашка Григорьев», "ещё не фамилии" (полуотчества). [S23] Call it a patronymic in the audit, not a surname, and reason from it to the father, after the [converts check in the revision-list recipe](russian-revision-list-household-chaining.md#4-transcribe-each-entry-field-by-field). Where an entry also carries a surname, keep both. A missing surname does not by itself show that the family had none ([village family reconstitution, step 1](russian-village-family-reconstitution.md#1-identify-people-by-an-identity-key-not-by-the-surname)).
- **Read the margins.** Copy brackets with their words, including group attendance marks [S24]. For a transfer, record the named owner, destination and any instruction to enter the person there. In one 1763 tale the note directs the reader to Kochetovka in Saransk uezd on the owner’s estate [S25]. Search the receiving estate’s register for the corresponding entry.

## 5. Read names against the household and the other years

Start from [reading confession lists, step 4](russian-orthodox-confession-list-reading.md#4-compare-the-household-across-several-lists) ("Treat every name as a hypothesis"). An audit adds three checks.

- **Compare the letters that distinguish the candidates.** For Данилов and Денисов, compare the vowel after Д and the consonant before ов with the same scribe’s forms [S10]. According to Kinprove’s private audit notes, the researcher reported a Максимъ/Михаил confusion [S26†]. Compare the disputed к/х against verified letters in that hand ([step 2](#2-settle-a-disputed-glyph-against-the-same-scribe)).
- **Search both church and everyday name forms.** Petrovsky links Фетис to Феоктист [S7], Финоген to Афиноген [S8], and Аксинья to Ксения [S9]. Compare the same household across lists: a Tula researcher reads Алифан in an 1850 revision and Вонифатий in an 1851 confession list [S34]. Keep competing readings for Митяй Лукиев: Митя can derive from Дмитрий or Митрофан [S35], [S36], and the entry alone leaves the father’s name unresolved [S34]. Include patronymics derived from everyday names in surname searches, such as Меркулов from Меркул, a form of Меркурий [S37], [S38]. Retain the source spelling.
- **Match the household before resolving a name.** Compare age and family composition [S12]. Read the preceding revision and the next one when available, then return to the original image with the proposed reading [S10], [S11].

Look for the other year’s entry when a supposed second given name makes no sense. In the published 1795 revision the editor interpreted «Авдотья не Агафья» as a correction after comparing the 1782 entries [S11]. A later confession list may copy the earlier one and repeat its error [S13]. Keep the two readings and their relationship in the audit log.

## 6. Read ages and dates as the scribe produced them

Start from [reading confession lists, step 4](russian-orthodox-confession-list-reading.md#4-compare-the-household-across-several-lists) ("Test the ages" and "Treat agreement between years with care"). An audit adds these checks.

- **Test whether the scribe carried ages forward.** Compare previous and current age pairs with the interval between revisions [S27]. In the published 1795 list the pairs differ by 13 years, the interval since 1782 [S11]. Use that pattern to rank uncertain digits. Preserve a clearly written age even when it breaks the pattern.
- **Expect ages repeated from the previous list.** The same forum thread notes that a new tale was built on the previous one, so its errors in age, name or patronymic were often («частенько») "попросту дублировали". [S27] A person who carries the same age in two lists several years apart may be a copied entry or a declared age that did not change ([revision-list recipe, step 5](russian-revision-list-household-chaining.md#5-test-formulas-placements-and-ages-before-using-them)). Keep the image value and add a note such as "same age as in the previous list; other years give birth about 1780". Do not correct it, and do not use it alone for a birth estimate.
- **Check the transcriber's own scheme too.** A sheet can fill ages by its own rule, such as the previous age plus the interval. An entry that breaks the transcriber's rule, or a death that has no note while its age follows the rule, needs the image.
- **Keep the original unit and precision.** Russian archival publication guidance preserves historical number forms [S28]. An 1858 transcription retains months and fractional years («4 мес», «12 1/2») [S33]. Put any normalised value beside the literal age and record its unit.
- **Date the event from its remark.** The 1795 tale records Evstafey Fedorov’s death in 1786 [S11]. Keep the stated year apart from the date of the revision, compare its digits with the same hand ([step 2](#2-settle-a-disputed-glyph-against-the-same-scribe)), and seek an independent death record when precision matters [S27].

## 7. Check each item against the other years and the other source's image

- **Cross-check every item, not only the hard ones.** For each item you will put to the reviewer, set out the image reading, then a small table of the same person in the other lists: year, stated age and implied birth year. The table often settles the item, and it shows the reviewer the evidence in one place.
- **Open the other source's image, not its transcription.** A revision sheet in the same workbook is the same transcriber's reading and repeats its errors ([AI for documentary records, rule 3](ai-for-documentary-records.md#operating-rules--the-non-negotiables-apply-these-on-every-task)).
- **Log what you find in other sheets.** A cross-year lookup on the images can expose an omission or a misread name in another year's transcription. Record it for that sheet's own audit; do not fix it out of turn.

## 8. Keep what is not an error out of the error list

- **Columns left out on purpose.** In confession lists the attendance column holds "был", "была", or a bracket over a group marked "были" ([reading confession lists, step 3](russian-orthodox-confession-list-reading.md#3-read-the-attendance-columns-as-an-administrative-mark)). [S24] A transcription that leaves these marks out on purpose has no omission. Ask before you report one.
- **The researcher's own additions.** Editors mark their own additions separately. The National Archives asks transcribers to put their comments in a separate field, not in the transcription. [S1] Russian archival guidance puts words restored by the editor in square brackets. [S28] BYU's palaeography introduction uses brackets for letters the transcriber inserted. [S30] A translated 1817 revision list states that its bracketed items are the translator's and "do not appear in the original record". [S18] A column such as a family surname added as a research tag has no counterpart in the image. Do not report it as an error and do not remove it.

## 9. Present disputed readings and record the ruling

Start from [AI for documentary records](ai-for-documentary-records.md#verification--privacy-discipline) ("Several readings of one image are one documentary chain"). An audit adds the ruling.

- **Record what the image says, even against other years.** Russian archival guidance does not correct wrong numbers or wrong proper names in the text. It gives the probable correct form in a note, or "Так в документе" when other sources cannot check it. [S28] The National Archives asks transcribers to type words exactly as written, "even misspelled words". [S1] An edition of a 19th-century journal leaves incorrect dates "to stand" and occasionally adds notes to clarify or correct them. [S29] So when a couple's ages fit neither the earlier nor the later list under any reading, record the image value and the inconsistency.
- **Record the decision on a disputed reading.** Give the alternatives, same-hand comparisons and cross-year evidence to the researcher. Record which reading they adopted, why, and who made the decision. Keep any conflicting original reading visible [S1], [S28].
- **Make crops a reviewer can check.** A very wide strip is hard to check in a small preview, and a vision model reads it no better. Anthropic's vision documentation says a large image is scaled down to fit a maximum long edge while its aspect ratio is kept, and that this can "make text less legible". [S32] So a strip twenty times wider than it is tall keeps only a twentieth of that limit as its height. Crop close to the item. Include two or three lines of context, the person-number margin and the age column, and look at the crop yourself before you send it to the reviewer.

## Output

Return two tables:

1. **Audit log.** One row per item: list and leaf, household and person numbers, the image reading, the transcription, the evidence (same-hand comparison, other years, the other source's image), the class (error, not an error, disputed), and the ruling with who made it.
2. **Finds for other sheets.** Omissions and misreadings found in other years' transcriptions while checking this one, logged for their own audit.

An unidentified place stays a reading with "name not established" and the searches made; see [historical place-name resolution](historical-place-name-resolution.md). Leave identity and relationship rulings to [evidence/proof judgment](evidence-proof-judgment.md).

To merge the audited year sheets into one village panel, use [village family reconstitution, step 8](russian-village-family-reconstitution.md#8-build-the-village-panel-from-faithful-year-sheets).
