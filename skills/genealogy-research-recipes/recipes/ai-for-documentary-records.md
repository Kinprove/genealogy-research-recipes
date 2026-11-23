---
id: "ai-for-documentary-records"
title: "Using AI reliably in documentary & records genealogy research"
summary: "Use AI safely on records: handwriting transcription and translation, OCR full-text search, AI-indexed records, record hints and photo restoration."
kind: "judgment"
scope: {"platforms": [], "tasks": ["any \"can AI/ChatGPT/Gemini transcribe or translate this handwriting\", \"full-text search for unindexed deeds/probate\", \"correct AI-indexed records\", \"evaluate an AI record hint\", \"colorize/restore an old photo\"."]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "AI-FOR-DOCUMENTARY-RECORDS-01", "text": "**Every AI output is a hypothesis to verify against the original record, never a fact to file.**"}]
handoff: ["research-documentation", "russian-household-list-transcription-audit"]
checked: "2026-11-02"
checked_basis: "opened 2026-11-02"
capabilities: {"browse": [], "local_script": ["generated plotting script"], "extensions": [], "data_transfer": ["export", "publish", "third-party-tool", "link"], "contact": []}
router: {"section": "Research method", "group": "AI and long projects", "order": 5}
---

# Recipe: Using AI reliably in documentary & records genealogy research

## Contents

- Goal
- The mental model (get this right or everything downstream breaks)
- Operating rules — the non-negotiables (apply these on every task)
- What to delegate freely (AI is genuinely good at these)
- What to never trust or delegate (verify, or don't)
- Prompt-craft that practitioners found works (the reusable core)
- Worked mini-examples (workflow logic, not clicks)
- Image restoration, colorization & generation — protecting evidentiary trust
- The pitfalls worth internalizing (the least-obvious, most-LLM-usable part)
- Verification & privacy discipline

## Goal

How an AI assistant (or a genealogist using one) applies AI to **documentary records** — handwritten, foreign-language, and unindexed sources — reliably: what to hand off freely, what to never trust, the prompt patterns that hold up, and why generated or "restored" images corrupt evidentiary trust.

## The mental model (get this right or everything downstream breaks)

AI is a **language-prediction system, not a reasoning authority** — it produces *plausible* text, not *verified* text, and it has no access to a record it hasn't been given or can't actually retrieve. **Every AI output is a hypothesis to verify against the original record, never a fact to file.** (Denyse Allen — the DNA sibling recipe rests on the same frame; stated once here.)

Two corollaries specific to records work:

- **Transcription and translation are separate tasks — verify each independently.** A transcription can be correct while its translation is wrong, and a tool that chains transcribe→translate→summarize carries one early misread into every downstream output. (James Tanner; Genealogy TV; Family Locket)
- **The better-looking tool is the more dangerous one.** LLM errors are subtle and contextually plausible — the kind you don't notice; dedicated HTR engines like Transkribus produce *visibly* wrong text you can catch (a practitioner heuristic, not a benchmark). You must know enough of the language, script, and domain to spot a plausible error at all. (Family Locket)

## Operating rules — the non-negotiables (apply these on every task)

1. **Verify every AI output before it enters a tree or report — plausible ≠ correct.** Check record-derived claims (transcriptions, abstracts, extracted facts) against the original record; check contextual/research claims (legal terms, history, strategy, open-web finds) against an authoritative cited source. An AI suggestion is never itself evidence.
2. **A bare LLM is not a search engine.** With no verified browsing it fabricates both the record and its citation. Supply the record yourself, or use a dedicated full-text / AI-OCR finding aid for the *finding* phase.
3. **Open the IMAGE, never the index.** Indexed narratives re-use old index errors that were already corrected on the image elsewhere.
4. **Transcription and translation are separate, separately-verified steps** — never trust a chained transcribe→translate→summarize on one pass.
5. **Names, dates, numbers, and place/legal descriptions are the highest-error zone** — check those first and word-by-word.
6. **Start from a high-resolution image and pick the reasoning/"Thinking" model yourself.** Image quality gates everything (download high-res, not low-res screenshots; crop clippings tightly), and auto-routing may not select the reasoning model for a hard task. A high-resolution file does not guarantee a high-resolution model input; see the downscaling pitfall below. (Family Locket; James Tanner)
7. **A saved AI-index correction is a live shared edit** — it appears on the record right away and becomes searchable within minutes, and it persists even if you later abandon the record. Treat every Verify/correct click as a real edit. (Ada Luque Nelson)

## What to delegate freely (AI is genuinely good at these)

- **Handwriting transcription.** Compare draft readers on a short, image-verified sample in the target hand, language and period. Check names and numbers on the image. Family Locket compared Gemini-backed Goldie May, Kindex, Leo and MyHeritage Scribe on the same deed [B32]; that comparison does not predict their accuracy on another hand.
- **Translation.** Verify the transcription first. Translate a verified passage, retain the original beside it, and check legal and local terms in a period-appropriate reference. In a Norwegian farmbook, translating *bygsla* as “built” instead of “leased” changed the family’s land tenure [B40].
- **Explaining archaic, legal, and foreign terminology and context** — imparlance, covenant, replevin, dower rights; Norwegian farmbook abbreviations (*f.*=født/born, *d.*=død/died); Latin causes of death. Cross-check every legal term against a historical legal dictionary. (Family Locket; Kitty Cooper)
- **Structuring and abstracting records you SUPPLY** — deed abstracts (grantor/grantee/consideration/boundaries/chain of title), chronological court-order tables, research logs, timelines, sourced life-maps. AI organizes what you give it; it does not find new records. (Family Locket; Denyse Allen)
- **Full-text / AI-OCR finding aids over unindexed images** — **FamilySearch Full-Text Search** surfaces people buried inside its AI-transcribed image collections that traditional indexes omit. It covers a broad and growing set of collections (prominently U.S. Land & Probate, U.S. Plantation Records, and Mexico Notary, with more added over time) but NOT every FamilySearch image collection — consult the current Full-Text collection list / Browse All Collections for what is actually searchable by jurisdiction and record type. (James Tanner; Kathryn Grant)
- **Compare supplied records.** Ask for a table with a citation for each person, date, place and role. Use differences across successive pre-1850 census tally columns as leads to household changes [B22], [B23].
- **Privacy gate:** <!-- privacy-gate: third-party-tool --> Family photos given to an AI tool can show living or possibly living people; answer the privacy gate in `SKILL.md` before uploading them.
- **Photo / image ANALYSIS for context** — surfacing an overlooked person in shadow, dating a scene by a car model or a uniform — as *leads* to corroborate against period photos and newspapers, never as conclusions. (Family Locket; Genealogy TV)
- **Research planning.** Ask for candidate record groups, the question each might answer and a way to locate it. Check the suggested sources before recording any result [B21], [B23].
- **Voice-preserving editing and drafting** — proofread-with-original/revision/highlighted-changes; draft a family-history chronicle from supplied transcriptions — but Claude tends to over-rewrite when asked to change just one paragraph. (DNAeXplained; Genealogy TV)

For a record image already on MyHeritage, run Scribe AI from the record page, or from the photo
in your gallery, with View insights instead of downloading and re-uploading the image
[S1 @2026-11-12], [S2 @2026-11-12]. The option appears on many record images, not all
[S2 @2026-11-12].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A document uploaded to Scribe AI gives
its contents, possibly including living people, to MyHeritage; answer the privacy gate in
`SKILL.md` first.

Upload a multi-page document as one PDF rather than as separate images: Scribe AI reads a PDF as
one unit, typically up to about 15 pages, with a 10 MB file limit [S1 @2026-11-12],
[S2 @2026-11-12].

For a local scan, clear the Scribe AI upload gate above, then open [Scribe
AI](https://www.myheritage.com/scribe-ai) and choose **Upload image** [S62 @2026-11-22],
[S63 @2026-11-22]. Expand the full transcription for the source-language reading and the
extracted-details section for names, dates and places [S61 @2026-11-22], [S62 @2026-11-22]. Set
the site language to the intended translation language before running the analysis. When the
report supplies a translation, compare it with the checked source-language reading
[S61 @2026-11-22], [S62 @2026-11-22].

Trace each fact from Scribe AI’s **Historical context** to the image or to an independently
verified source. In the provider’s death-record example, the tool added the subject’s father’s
occupation in the context section [S62]. Keep details found only in that section as research
leads until sourced.

For a gravestone report in Scribe AI, check **Inscription** against the photo and retain the
literal wording. Check **Translation** against that reading and use **Inscription highlights**
to locate names and dates [S62 @2026-11-23]. In **Iconography & symbolism**, check the full
photo for each suggested feature and record whether it is carved on the stone or on a separate
object beside it. Test proposed meanings against a period reference [S61 @2026-11-23],
[S62 @2026-11-23], [S89 @2026-11-23]. If the inscription gives no cemetery, log each
**Location context** candidate with the clue behind it [S61 @2026-11-23], [S62 @2026-11-23].
Use the verified name and dates to look for a matching cemetery register or plot entry. Leave
the location open until corroborated and cite the photo and burial record separately.

To reopen a report for an image uploaded through Scribe AI on the web, go to **My Photos →
Scribe AI**, open the analyzed image and select its insights button [S62 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: export --> Copying a Scribe AI transcription exports the names, relationships and other details of anyone mentioned, including living or possibly living people, from MyHeritage to a local editor. Answer the privacy gate in `SKILL.md` before copying.

Copy a working transcript into a local editor using the whole-transcription or section copy
control. Keep its image locator and mark any corrections after comparing it with the image
[S61 @2026-11-22], [S62 @2026-11-22].

In the MyHeritage app, open **Photos → Scribe AI** from the grid menu to choose an image. For
one already in the gallery, open it and use the three-dot menu’s Scribe AI option. Clear the
upload gate before submitting an image from the device. Scroll down and expand the relevant
sections. To recover a saved report, reopen the photo and look for **Scribe AI: View insights**
at the lower left of the photo view [S64 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: link --> The Scribe AI report link can expose the analysis and details about anyone shown or named, including living or possibly living people, to the recipient and anyone with access to the link. Answer the privacy gate in `SKILL.md` before sending it.

When a reviewer needs the same Scribe AI analysis, check what the report link exposes. Use the
link control under the report and send the source locator with the link so the reviewer can
identify the record [S62 @2026-11-22].

For Swedish court books (*domböcker*), use ArkivDigital’s **Machine-Transcribed Text**
(*Maskinell texttolkning*) to search the text of volumes listed as covered [S36 @2026-11-20],
[S37 @2026-11-20], [S38 @2026-11-20]. Filter by court, volume type and date. Start with one
Swedish search term per query because a multiword query requires the terms on the same image
[S38 @2026-11-20]. Open each hit and cite the court, volume and page or image. If the volume is
outside coverage or repeated queries miss, browse the volume by date.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A query sent through the connected assistant sends the names, places and other identifiers in the query to its provider and Riksarkivet. If the query identifies anyone living or possibly living, answer the privacy gate in `SKILL.md` first.

If the user already has the Riksarkivet beta connected, ask it to search the archive inventories
and available machine-transcribed documents, including some from the 1600s. Give a historical
surname, locality and record type. Narrow promising leads with a follow-up that names the court,
series or period. Open the linked original and confirm its archival reference and wording. Check
collection coverage and use the ordinary catalogue or browse the volumes when the assistant
finds nothing [S83 @2026-11-22], [S84 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: publish --> A BillionGraves contribution sends images and names or other details of anyone shown or mentioned, including living relatives, to BillionGraves for use in its public database. Answer the privacy gate in `SKILL.md` before contributing.

For a BillionGraves contribution, use the desktop Dashboard’s upload section and select
the source type for a headstone photo, obituary, death certificate or funeral program.
Review Cemetery Intelligence’s extracted fields against the image [S36 @2026-11-20],
[S39 @2026-11-20]. For headstone photos taken in the app, check whether the account offers
automatic transcription. The app can release photos into the public transcription queue
even if you choose self-transcription [S40 @2026-11-20]. Use a local reader for material
you need to keep private.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A page sent to the PERO OCR demonstration app can disclose living people’s details in the page image and transcription corrections to Brno University of Technology. Answer the privacy gate in `SKILL.md` first.

Try the PERO OCR demonstration app on a sample of historical Latin-script print. Its
documented handwriting scope is mainly Czech [S41 @2026-11-20], [S42 @2026-11-20]. For
Russian or Ukrainian Cyrillic handwriting, choose a reader with a model for the script and
check the sample’s letters and names against the scan before running more pages.

## What to never trust or delegate (verify, or don't)

Each of these is a documented failure, not a hypothetical.

- **Record existence or retrieval by a bare LLM.** With no verified browsing it invents both the record and its citation — "AI assistants are not search engines," and they inconsistently open even a public link. Supply the record, then verify the output against it. (DNAeXplained)
- **Transcription and translation.** Verify names, dates, places, numbers and legal descriptions against the image, then check how each verified field was translated [B1], [S6].
- **Cultural, religious and naming interpretation.** Compare each relationship word with the document’s language and form, including the distinction between Spanish *madrina* (godmother) and *madre* (mother) [B6]. In a ketubah, a reported misreading dropped a name element and assigned the wrong father [B42]. Keep both scripts and ask a reader familiar with the document to check the relationship before entering it.
- **Period and foreign kin or status terms given their modern sense.** Write the literal term next to the gloss, and leave ambiguous readings open. Dutch *nicht*/*neef* can mean niece/nephew or cousin ([also](https://www.youtube.com/watch?v=b_JtDaDF6y4)). In a land-lottery draw, an 'orphan' may only have lost a father. In older English, 'Dutch' can mean German-speaking, and 'fl.' marks an active period, not a lifespan. Check an AI gloss against a dictionary from the record's own period. For Spanish, [Ryskamp](https://www.youtube.com/watch?v=_YP7JKXjthk) points to the RAE's historical-dictionary collection (NTLLE); other languages need their own period sources. None of these terms settles a relationship or origin by itself. ([GeneaVlogger](https://www.youtube.com/watch?v=R2fzEjKl2QI), [Thomsen](https://www.youtube.com/watch?v=C2_9AVcodcg), [Louden](https://www.youtube.com/watch?v=5_kZB9XyA8c), [Genealogy Gems](https://www.youtube.com/watch?v=Pbo5Gm5qSx8))
- **Status or trade words next to a name.** Look up the term in a regional glossary. In two reported church-book readings, *Insten* described a labourer on an estate and *Schmieds* identified the father as a smith; treating either as a personal name changed who appeared in the family [B78], [S34]. Enter the term as status or occupation and repeat the name search without it.
- **Parentage and chronology.** Trace each relationship to the wording of the record and compare the event dates. A hint reviewer reported that the assistant rejected a child born shortly after the father died, overlooking conception before death [B19]. Leave a proposed relationship open until evidence identifies the parents [B38].
- **Same-name disambiguation.** AI conflates two people sharing a name — you catch it via an impossible chronology, and professionals separate them by land boundaries, witnesses, and occupations. Anchoring the assistant to a person's unique ID reduces but does not eliminate this. (Legacy Tree; Genealogy Gems)
- **AI narrative that reads the INDEX, not the image.** Ancestry AI Stories draw on indexed fields and can re-use OLD index errors already corrected elsewhere, producing generic narrative (a Genealogy TV / FamilySearch critique of a fast-evolving generative feature). Open the underlying image. (Genealogy TV; FamilySearch)
- **A record HINT before its facts are verified against the actual record.** Confirm the suggested dates, places, and relationships match the record — and open the image, not the indexed summary — before attaching. Even "highly accurate" hints are "not perfect." (FamilySearch)
- **Extractions that change the record's event or date type.** Keep the type of event and date the entry actually records. A parish burial date is not a death date. 'Received into the congregation' may follow an earlier baptism somewhere else. A baptism 'of necessity' does not show that the child died. A delayed certificate's filing date is not the birth date. An annual report's title year may differ from the period it covers, and an 'on this date' newspaper item carries a later date. Keep qualifiers such as 'Mary late X' (an earlier surname). Search for the missing event record rather than inferring it. Motivated by [Tanner](https://www.youtube.com/watch?v=xOWgEolt7-g), [Brown](https://www.youtube.com/watch?v=_ij26t85WY8), [Ryskamp](https://www.youtube.com/watch?v=_YP7JKXjthk), [Lisson](https://www.youtube.com/watch?v=LHxFLXvGnx4), [Melick](https://www.youtube.com/watch?v=5dVcyQRtbTo) and [GeneaVlogger](https://www.youtube.com/watch?v=-CxvuPelZ4I). These are single examples, not rules for every register.
- **A rank's seniority date taken as the promotion date.** In compiled summaries of Russian imperial civil-service files, one promotion can carry two dates: the date of the promotion and a stated seniority (*старшинство*) date, which can be years earlier. Put each in its own field with the literal wording. Do not put the seniority date on a timeline as the event, and do not use it to place the person in a post at that time. Verify the dates in the service list if available. The cited Perm summaries give promotion and seniority separately but do not show the original lists or how seniority was calculated [B79].
- **Claims to have read a source.** Verify access and match any reported error or quotation to the original passage. One assistant supplied proofreading corrections for a page it had not retrieved [B43].
- **Colorized, restored, or generated images as evidence.** See the image section below — these are derived artifacts, not documentation. (James Tanner; Genealogy TV; Aimee Cross)
- **Citation style.** Gather the source fields and consult the cited style guide for details such as page abbreviations before applying the format [B31].
- **An AI summary or abstract that omits or mislabels fields.** A fluent platform summary of a deed or mortgage can name the parties but leave out their residences, the consideration, the land description and the witnesses. It also won't link other deeds on the same page or for the same parcel. Take those fields from the image or transcript yourself. A small consideration is only a lead toward kinship. Also, don't let an abstract call a list's dollar figures wealth or tax, or treat a signer's mark as proof of illiteracy, until the document explains them (for amounts, also check the governing statute). A reported list recorded jury mileage payments [B51]. Read the heading, statute and payment unit before interpreting a dollar figure; compare the other signatures and check whether the form provided only a space for a mark [S35].
- **Technical drawings requested as generated images.** "Generate an image" of a metes-and-bounds plat yields artistic pixels — accurate output needs a code path plus a human who understands deed mapping. (Family Locket)
- **Final evidentiary judgment / GPS compliance.** AI drafts proof arguments; humans rule — even FamilySearch's own stance is to leave conflicting-record judgments to people. (FamilySearch; Legacy Tree)

In Georgia's 1827 land lottery, an entry for a man's "orphans" does not by itself show that he
had died. The act of 9 June 1825 let the wives and children of men absent from the state for
three years draw as though they were widows and orphans [S3], [S4], [S5]. Before searching for
the father's death or probate before 1827, check the act's categories and look for evidence
that he had left Georgia.

On a MyHeritage **Names & Stories** result from OldNews.com, use the AI-generated summary
and extracted fields to locate the article. Find the separate article-text snippet when
present, and check names and relationships on the full scanned page before citing the
article [S43 @2026-11-20], [S44 @2026-11-20], [S45 @2026-11-20].

Check the user’s account for MyHeritage Omni or OldNews Pro access to the full page on
OldNews.com [S46 @2026-11-20], [S47 @2026-11-20]. If access stops at the index, use the
newspaper title, issue date and place to find the page in another archive.

For an indexed newspaper date, read the notice and the issue date before filing it [S65]. If the
notice gives only a relative day such as “last Thursday,” record the wording and the issue date
and label any calendar day you calculate. Check whether the item was reprinted or carries its
own dateline before choosing the reference date. If the notice gives only an age, keep the age
and allow for whether the birthday had passed when estimating a birth year [S65], [S66].

When a Names & Stories result supplies full OCR, use it to find the rest of the passage around
the snippet. Treat both as machine text and transcribe wording from the scanned page
[S67 @2026-11-22], [S68 @2026-11-22], [S69 @2026-11-22]. On a MyHeritage **Marriages from
Newspapers** entry, use **View full newspaper page** to check the story in context and recover
details omitted from the extracted fields [S70 @2026-11-22].

When an OCR search misses, check whether the host carries the exact newspaper issue and repeat
the same name and place query on a second host. If the second search finds the item, use its
issue and page to check the first host’s copy. Log a search miss when the first host has the
page. In a reported comparison, one host retrieved an article that other hosts carrying the same
issue failed to return [S71]. Differences in machine text can affect retrieval [S72].

For a MyHeritage **United States Consolidated Federal Censuses** hit, open **See variations from
sources** and follow the links to the individual census records. Check each household and the
identifying details on that year’s image before accepting the proposed link across years
[S73 @2026-11-22].

If a name is missing from MyHeritage’s initial 1950 census AI index, search the underlying
schedules by enumeration district. MyHeritage filtered suspect machine readings out of that
index [S74]. Use the address and enumeration district maps or descriptions to choose which
district images to inspect [S75].

**Privacy gate:** <!-- privacy-gate: publish --> A name suggestion sends the corrected name and its association with the newspaper item to MyHeritage and can make it searchable by other users. Answer the privacy gate in `SKILL.md` first if the suggestion identifies anyone living or possibly living.

For a misread name in a MyHeritage newspaper result, verify the name on the scanned page. If the
result offers a correction control, submit an alternative name only after clearing the gate
above. The original indexed name and the searchable member contribution can coexist. Cite the
issue and page for your reading [S65 @2026-11-22], [S85 @2026-11-22].

## Prompt-craft that practitioners found works (the reusable core)

1. **Feed a COMPLETE source folder, not isolated questions.** Hand over the whole transcribed folder and ask for working *artifacts* — research log, plan, timeline, corrected family group sheet, proof statements — not one-off Q&A. (Denyse Allen)
2. **Use a fixed instruction skeleton.** *Role / Goal / Text / Task / Format* for records tasks, or *Task + Context + Desired-output + Known-facts*. Specificity drives quality. (Family Locket; Genealogy TV)
3. **Seed known names, places, and period up front.** Supplying the ancestor's known name, residence, and dates improves name recognition and lets you catch errors. **Start with a document whose facts you already know as a calibration baseline** — if the model misreads a record you *can* check, you know how much to distrust it on one you can't. (Genealogy TV; Family Locket)
4. **Give explicit transcription instructions.** "Identify this as a [deed/newspaper], transcribe exactly, preserve line breaks and original spelling, do NOT hallucinate, flag uncertain words." For a hard word, a letter-by-letter reading can show which letters are in doubt, but a same-chat "ignore your previous attempt" re-ask is not a check: settle the word against the image. (Genealogy Gems; Denyse Allen; Family Locket)
5. **The uncertain-name worksheet trick.** Ask the model to leave blank spaces sized for uncertain names, turning the transcription into a printable correction worksheet — names are the worst-predicted tokens because they're least inferable from surrounding text. (Genealogy Gems)
6. **Work in sections.** Process a long probate packet page by page, preserving page identifiers. Once each reading is checked, query the dated extracts across the packet and follow the citations back to the relevant page [B15].
7. **Prefer the developer / grounded surface.** Gemini in **Google AI Studio** transcribes better than the Gemini chat app, whose hidden system prompts inject interfering formatting (watch: AI Studio may default to Nano Banana, an *image* model — switch to a text/reasoning Gemini). Use **NotebookLM** to constrain answers to supplied documents, and prefer source-grounded/web-research modes over ungrounded custom GPTs. (Family Locket; James Tanner)
8. **Instruct it to STOP rather than invent.** Tell the model to say it doesn't know instead of filling gaps, and define domain rules explicitly *before* asking it to apply them. (James Tanner)
9. **Demand a source, citation, and page number for every claim** — plus "what's missing?" and "argue both sides." When summarizing a long report, require page numbers so the evidence stays relocatable. (James Tanner; The Diehl on Genealogy)
10. **For technical output, request CODE or a diagram, not an image.** "Write and run a Python plotting script" for a plat — and explicitly pick the Thinking/reasoning model, because auto-mode picks the fast one. (Family Locket)
11. **Save reusable "skills" / templates the AI checks against each run.** A script, abstract, or citation template keeps repeated prompts from drifting, since the model re-assembles each response from scratch. (Denyse Allen; Genealogy TV)
12. **Use strict, command-style language and skip politeness** — the AI has no emotions, and imperative phrasing keeps you aware it's a tool. (James Tanner)
13. **Privacy gate:** <!-- privacy-gate: export --> A GEDCOM index or obituary extraction can name living relatives; answer the privacy gate in `SKILL.md` before exporting it to a spreadsheet. **Verify large batches in Excel.** Export a big structured extraction (a GEDCOM index, obituary fields) to a spreadsheet and check row counts and filters, because LLMs silently drop or invent data in the *middle* of a large input rather than raising a capacity error. (Genealogy TV — Little & Thompson)
14. **Run two strong models and diff to find the uncertain tokens.** Transcribe or translate the same record with two different models; the diff points straight at the uncertain tokens. It is neither verification nor corroboration: settle each disputed token against the image, and do not feed both models one draft. (Kitty Cooper)

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Sending a probate PDF to an external AI reader discloses names, relationships and estate details about anyone mentioned, including living or possibly living people, to the tool provider. Answer the privacy gate in `SKILL.md` before attaching it.

For a supplied probate PDF, ask for an alphabetical table of names, exact relationship wording
and page locators. Check each stated relationship to the deceased on its cited page [S52].
Record estate roles in a separate column and leave an unstated relationship blank, even if the
person receives a bequest [S53].

**Prepare the scan before transcription.** If scanning from the original, align the page and
start at 300 pixels per inch. Scan at higher resolution if the writing is small or faint
[S29], [S30]. Work on a copy. Rotate a postcard into reading orientation and crop to the
message [S29]. For a complex multi-column page, make one reading crop per column where the
columns can be read separately [S29]. Keep the full page for checking headings and entries
that span columns.

For a chatbot’s census extraction, locate the person’s or household’s row on the original
page and follow it across to the exact column heading for each value [S52], [S54]. If the page
lacks headings, find them on another page of the same schedule before assigning fields [S55].
Record the row and column for each correction.

Settle differences between a model’s transcription and your own using the image. In Family Locket’s comparison, the typed reference had regularised a spelling that the model preserved [S6 @2026-11-12]. When preparing a reference transcript, turn off automatic spelling corrections and retain the original spelling [S7 @2026-11-12].

For a hard hand, compare each line of the HTR draft with its linked line on the image [S8 @2026-11-12]. If a chatbot edits the draft, diff both texts and verify every change on the image, including changes that make an unfamiliar reading look more plausible [S9 @2026-11-12].

### Gate a bulk handwritten-register run

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Register images can name living or possibly living people; answer the privacy gate in `SKILL.md` before sending any control image, crop or batch to an external AI reader.

The following setup comes from a practitioner's report of blind Claude/GPT transcription
over approximately 3,000 frames of 19th–20th-century registers, with 1,500-pixel scans and
letters about 8 pixels high. These are reported observations, not an independently inspected
benchmark; the underlying images, prompts and logs were not inspected here [S15].

1. **Gate each new model, prompt or setting on a small blind control set.** Choose entries
   whose decisive fields the researcher has verified on the image; withhold those expected
   readings from the reader. The name-seeded prompt in item 3 above is an assisted reading,
   not this blind test. Settle disagreements on the image and keep unresolved control readings open.
   A reader that completed its log and rechecked its output still substituted given names and a parent’s religious status in a reported trial [S15].

2. **Test image scale on the blind control.** Compare native strips, enlarged strips and word crops with line context. Score the same decisive fields and record the cost of each setting. Five entries with one run per setting did not establish a best scale [S15]. Retain the crop locators; enlargement adds no source detail.

3. **Test script tips on the same control.** Compare the reading with and without examples of letter shapes, keeping expected answers hidden. An occupation and a place name remained wrong under every tested setting in the reported comparison [S15]. Verify each conclusion-bearing field on the image.

4. **Measure reader workload.** Test short, fresh batches on the intended material. Count image views, calls and tokens per frame, including fixed instructions and accumulated context. The report proposes five frames per reader as a starting point to test [S15].

5. **Check the reader’s configuration and image access.** Inventory the tools, connectors, skills and fixed prompt the reader actually loads. Retain necessary image access and privacy and permission rules. A tested configuration removed the image tool, and the readers correctly refused to transcribe [S15]. Check access on a control frame. Keep answers out of the blind prompt; test separately whether prior context changes the reading.

6. **Join batches and audit coverage.** Allow a neighbouring image to complete a split or misbound entry. Preserve source frame IDs and first and last entry numbers. Compare every frame on disk with the extraction and explain each gap. One reported draft skipped 140 frames, including frames with entries [S15]. Check reading accuracy separately and keep expected answers out of blind batches.

7. **Use the index to find the page.** Two hits for a wife’s family came from the same patronymic misread twice [S15]. Re-read every hit on its image before connecting the families.

**Triage a long series with local HTR.** When the scans have no searchable text, use the
blind control above to check whether a local handwriting reader retrieves known entries.
Keep the recognized text tied to its source page. Search for several independently known
terms likely to occur in the same entry, such as a child’s given name, a parent’s name and the
residence. Use supported spellings and try each term separately. Start with pages matching
more of the distinct terms and keep pages that match only one for follow-up. Terms can match
different entries on a page, so read the complete entry on the image. Record the model version,
layout settings, queries, matching rules and which pages produced text or failed. Log screening separately
from image review. A zero-hit screen leaves the images to be checked before ruling out a
record. Word-spotting evaluations measure missed and false matches separately [S60].

For resource estimates, compare the same frames with the same model, brief, crop scale and number of readers. Measure input tokens including cache reads, uncached input, output, image views, elapsed time and coverage. Include interrupted batches separately. The practitioner’s follow-up compared different frames and changed prompt, batch size and launch method together [S16]. Use its figures to design a local comparison; assess accuracy on a blind control and calculate billed cost from the applicable rates.

### Generate candidates for an uncertain German word

Retain the partial literal reading and visible beginning/ending letters. Compare candidates
at the estimated letter length and one letter shorter/longer, checking each against the image
and document context. For a possible place name, narrow historical-gazetteer candidates by
the independently supported region. Preserve unresolved letters and historical spellings;
modern spellcheck approval, popularity or familiarity does not verify a reading.
[CompGen's German-handwriting worksheet](https://www.compgen.de/2023/04/fuenf-fantastische-technik-tricks-zur-entschluesselung-der-deutschen-handschrift/)
supports this optional sequence, not automatic replacement or current wildcard/menu syntax.

For an uncertain name, place or relationship parse, compare several available complete entries
in the same clerk's hand. Note repeated formula words and their field roles; keep a change of
hand in a separate comparison block. Preserve alternative readings rather than replacing all
similar tokens. The [locality-reading discussion](https://forum.j-roots.info/viewtopic.php?f=4&t=1272)
motivates this contextual check without verifying its proposed place or subject-status readings.

For a doubtful letter in a name, find the same writer's clear forms of that letter on the same page and compare them before accepting or correcting an index reading. If the image is poor, look for an independent scan of the same page on another provider's site and compare the readings, recording which image each came from. Another copy may be clearer, but not always. When asking a helper, supply the whole page or a link to it ([Sorensen](https://www.youtube.com/watch?v=xvqeNOE_dp8)); the same likely applies to a model. The reading stays an interpretation. Motivated by the [maiden-name example](https://www.youtube.com/watch?v=9Vq4-eIqsg0), the [enumerator comparison](https://www.youtube.com/watch?v=EEhzZ94K0ms) and the [ScotlandsPeople census case](https://www.youtube.com/watch?v=bxUHrllbZI4). These are single cases and do not establish whether the copies come from different filmings or scans.

When an older hand uses a long first *s* in *ss*, compare it with the same writer’s clear *ss*. Test both the double-*s* name and a variant indexed with *p* or *f* if the forms resemble those letters [S10], [S11].

To audit a whole transcription of a Russian confession list or revision tale against its images, use the [household-list transcription audit](russian-household-list-transcription-audit.md).

Before guessing, look for other renderings and reading keys:

- the same person's name elsewhere in the probate or court file
- the same family's other entries (a sibling's baptism may give the place in a clearer, later spelling)
- a published transcription of a will or deed of the same type, place and period, as a key to its formulaic wording
- a legible related notice (e.g. the spouse's death notice) for a blurry obituary

Record which document supplied each reading. Keep keys in a separate comparison block, transcribe each entry as written, and label key-assisted readings. A clerk's copy may carry its own error, and a key pulls you toward the words you expect. Boilerplate never supplies the target's names, amounts or boundaries. Agreement is support, not proof. ([Tanner probate](https://www.youtube.com/watch?v=FA2iXKr09Lo), [Brady](https://www.youtube.com/watch?v=OU2cYqgN-lw), [Tanner town records](https://www.youtube.com/watch?v=bhpOk-A5CeA), [Obee](https://www.youtube.com/watch?v=D-eqV-ZS5UY))

### Check candidate words in Spanish

For a doubtful Spanish word, keep the letters you can read and use that partial reading to
generate alternatives. Compare each candidate with the visible letters and use a dictionary such
as the RAE’s to check whether the meaning fits the passage and period [S76], [S77].

Check an apparently ordinary surname against every visible letter: in a reported Spanish-record
reading, the model rendered *Portier* as *Cortés* [S76].

### Check historical Finnish against parallel Swedish

When a modern gloss fails for a nineteenth-century Finnish word, search *Den Lilla Swenska och
Finska Tolken* (Project Gutenberg eBook 63472) for the period spelling and read across to the
paired Swedish entry [S93], [S95]. For a phrase, compare the whole exchange in the bilingual
dialogues [S94], [S95]. Test the suggested sense against the record sentence, retain the Finnish
as written, and cite the glossary section or dialogue used.

### Assemble a whole-letter reading copy

After checking each page against its image, assemble a separate transcript in source-page
order. Retain page labels/links and unresolved or missing-page markers, together with the
images and native page transcripts. Label the combined reading copy as a derivative of those
pages. The [four-page letter example](https://whoareyoumadeof.com/blog/ancestry-ai-image-transcript-feature-how-to-use/)
motivates this portable output; its historical interface and accuracy claims are not required.

The same applies to register entries. Do not hand the model only the indexed page. Also open and supply the following page, because an entry can run across pages, with the parents' names on the continuation. Supply the facing page too: consent for under-age parties may name their parents outside the printed form. Record a page locator for each part. The [marriage-register example](https://www.youtube.com/watch?v=gsbQIuilOYk) motivates this step. Layouts vary by county and register, and its images are not in the transcript.

### Drafting a narrative from verified records

Keep documented fact, tradition, AI-supplied context and conjecture visibly separate:

- First, have the model outline only from the supplied files, with the instruction 'add nothing else'.
- Then ask separately for period context. Mark every AI insertion (for example with an asterisk) and treat it as unverified until it is checked against a cited period source.
- Don't supply dialogue, thoughts, feelings or physical details that no source records; quote the source instead.
- Render a recounted statement as reported speech, not a quotation, and leave unidentified people unnamed.
- Separate a habitual family custom from one documented for that year, and name who told an undocumented story.
- Label theory ('it is believed', 'I envision') in the text or a footnote. If the story needs invention, call it fiction.

Markers only separate the layers; they verify nothing. ([Sorensen](https://www.youtube.com/watch?v=CoxXz-C754c), [theory labelling](https://www.youtube.com/watch?v=YsWgVd8-mUs), [Allen's outline prompts](https://www.youtube.com/watch?v=M3nAWOP9v8Y), [holiday scene](https://www.youtube.com/watch?v=1qeAV90uQNY), [reported speech](https://www.youtube.com/watch?v=TlZ88OEjHqY); these sources do not show how to weigh a family story as evidence.)

**Privacy gate:** <!-- privacy-gate: third-party-tool --> AI Biographer can send the subject’s and named relatives’ biographical details, including details of living or possibly living people, to OpenAI through MyHeritage. MyHeritage saves the result as a family-site media item visible to site members [S90 @2026-11-23], [S91 @2026-11-23]. Answer the privacy gate in `SKILL.md` before generating the biography.

In MyHeritage AI Biographer, choose **Standard** to draft from the tree profile alone. Use
**Enhanced** to look for leads from matching historical records, other family trees and web
material [S89 @2026-11-23], [S90 @2026-11-23]. Follow the biography’s source links, check the
original records for each claim and keep unsourced additions out of the verified narrative
[S92 @2026-11-23].

### Read Latin register entries by their formula

Extract Latin entries by their grammar and layout, not by guesswork:

- *uxor/uxoris* after a mother's name means 'wife (of)', not a surname. Leave a missing maternal surname blank rather than filling it from a godparent's surname.
- Record each name's literal form and a nominative working form, keeping grammatical case and gender distinct: Petri/Petrus differ only in case ending, but a case ending can also mark gender, so Cornelium and Cornelia are not interchangeable. i/j and u/v vary by priest.
- Take a child's sex from the case and gender endings or from the marked *puer*/*puella* column, not from the given name or the index.
- Where a run gives the month and year only once (later entries may say just *eodem die*), read back to that entry and record the date as inherited, or mark it unresolved.
- Preserve *infans* literally until its local meaning is established; it need not mean a baby. Record *vidua* with a named husband as reported widowhood, not as independent proof of his death date.

These are reading aids from [Hutchison](https://www.youtube.com/watch?v=Prg_XRQSdp0), [Stoddard](https://www.youtube.com/watch?v=fCLOCtag5kA) and [Starkey](https://www.youtube.com/watch?v=GCFTz_67DkY). Normalized forms are not proof of identity, and *uxor* is not proof that the husband was still living.

## Worked mini-examples (workflow logic, not clicks)

**Privacy gate:** <!-- privacy-gate: publish --> A correction saved in the correct-and-verify loop
below, or in the whole-page census fix after it, is a live shared edit that other users can find by
search. Before saving a correction that names or links someone who may be living, whether in the
user's family or, on a whole-page fix, in another household on the page, answer the privacy gate in
`SKILL.md`. Under the gate's Data item, say when a marginal note records an acknowledged father or
another parentage fact. Until each such person has given permission, keep the proposed correction in
the user's local notes instead of saving it. A correction that concerns only people known to be dead
can be saved as before.

- **Full-Text Search for ENSLAVED ancestors.** Search slaveholders, plantation names, overseers, and distinctive property — probate/estate files, bills of sale, and deeds of gift (within FamilySearch's U.S. Plantation and Land & Probate collections) name enslaved people by name, age, value, and family ties that traditional indexes omit. Search spelling and HTR variants (and wildcards) — an AI-misread or misspelled name won't exact-match — and re-run every week or two as processing continues. (James Tanner)
- **Unindexed deeds and probate.** Search for a distinctive item of property such as a piano named in a will, a rare surname with a locality, or two parties together. Try exact phrases and spelling variants. Open each resulting record to see how the people or property are connected [B5].
- **Court orders.** Search the county’s order books for parties on both sides. One image group can contain multiple related entries [B35]. Save each image and its reference, check its transcript against the page and enter the dates, parties and action in a chronological table. Test any proposed reconstruction against the orders and verify legal terms in a period legal dictionary [B36].
- **Correct-and-verify loop for AI-INDEXED Latin American records.** In FamilySearch's review tool, inspect EVERY name and event — don't just click Verify; include marginal notes (they record marriages and acknowledged fathers); correct godparents and witnesses (likely relatives) but skip nonessential priests and notaries; fix a gender label where "parent/godparent" signals a non-standardized value (re-click → father/godfather); leave multi-image, unknown-primary, or too-complex records unresolved rather than guessing — and remember a saved change is a live shared edit (on the record right away, searchable within minutes). (Ada Luque Nelson)
- **Recurring AI-indexing error patterns.** In AI-indexed Iberian records, check the image for these errors:
  - Spanish *M* (mujer, female) indexed as male
  - given name and surname run together in one field
  - the church entered as the birthplace
  - a note that exists only in the margin indexed as its own record
  - a 'tail' record with an unknown principal, created when an entry continues onto the next page (a duplicate, not a separate event)

  A reported 1950 census index copied the first household’s surname onto later households on the page [B53]. Before inferring remarriage or another person, compare each household’s image and index. Where editing is allowed, correct the whole page.
- **German death registers.** Transcribe each labelled column separately, including occupation, religion, residence, cause of death, burial, age and officiant. Check regional month forms such as *Jänner* and Latin medical terms against the image and a suitable reference before interpreting them [B41].
- **Foreign-language HTR discipline.** Do a rough MANUAL read and extract the facts FIRST → prompt with language + period + known names + features → transcribe 1–2 paragraphs at a time → review image and transcription side-by-side word-by-word — because you can't verify a language you don't read at all. (Family Locket)
- **Evaluating a record HINT before attaching.** FamilySearch's AI Research Assistant proposes up to ~5 parent/spouse/child home-page hints (logical dedup filters run before AI filters). Open the ACTUAL record — not the indexed summary — confirm the suggested facts match, and check chronology (parent ages, birth timing); check the possible conception window if a birth follows the father’s death [B19]. Well-sourced names get better hints. (FamilySearch; Genealogy Gems)
- **Deed plat from a metes-and-bounds description.** Do NOT say "generate an image" — ask the Thinking model to write and run a Python script that converts bearings/distances to coordinates and plots the polygon and compare its bearings, distances and closure with an independently plotted baseline [B28]. Learn deed mapping yourself so you can tell an accurate plat from a hallucinated one. (Family Locket)
- **Surname variants.** Group documented spellings by record, date, language and locality. Turn recurring changes, such as final vowels or K/C, into search variants. Keep the original spelling beside its citation and test whether the records describe the same person [B25].
- **Conflicting death dates.** Compare the proposed death with later census, land, probate and tax entries in one timeline. For each apparent later appearance, check whether it refers to the same person, an estate or a namesake [B23].

If a FamilySearch Full-Text Search reading shows a vertical bar or an apparent break in the
text, check whether it lines up with a printed margin before using it to split the entry. In one
reported transcription, a ruled margin appeared as a vertical bar [S78].

In a death register, read a marginal correction as its own statement. Record its date, issuing
authority and the wording it corrects. Check whether the original words are physically struck
out: in one published Scribe AI example, the output marked intact register text as crossed out
[S61]. Keep a cause of death open when the correction gives only the circumstances of discovery.
Use the named authority and correction date to look for a court or police file that could
establish the cause [S61].

For a compound occupation on a German gravestone, inspect any dash in the inscription and test
whether the second word supplies the ending of the first. Search the expanded occupations
separately. In a reported case the tool retained the church-painting description and missed the
history-painting component (*Historienmaler*), an occupation supported independently by a period
artist catalogue [S61], [S87].

When using a translated wanted notice to distinguish people, audit each identifying adjective in
two passes. Compare the color and nationality readings with the printed letters, then compare
their translations with the verified words. In one reported notice the color was misread, and
the translation rendered the transcribed *Svensk* as *suomalainen* [S88].

## Image restoration, colorization & generation — protecting evidentiary trust

Treat any AI-altered image as a **derived, non-documentary** artifact and keep it out of the evidence chain:

- **NEVER use an AI-restored, upscaled, or generated face for identification or facial comparison** — generative "restoration"/upscaling can silently alter facial features and change who the person appears to be; a generated "ancestor photo" is fiction, not a likeness. (James Tanner; Genealogy TV; Aimee Cross)
- **Keep the untouched original** as the record of authority; never overwrite it. (James Tanner)
- **Label every modification in human-readable text** and **cite each edit in a layered citation** — visible provenance metadata and "Generated by AI" tags are removable, and no universal tamper-proof standard is settled yet. (Emerging ones — Google's invisible SynthID watermark on Gemini/Nano Banana images, and C2PA content credentials — are being adopted but are not yet universal, so re-check before relying on any of them.) (James Tanner; DNAeXplained)
- **Convert a reconstruction to a pencil drawing or painting** to signal it is interpretive, not photographic. (Denyse Allen; Genealogy TV)
- Keep generated, enhanced and colourised images separate from the original. Colourisation invents an original colour, removing a background can erase a building or an album mount used for dating, and generative restoration can change a face or add anachronisms. Date or identify the photograph from the original and label the derivative when showing it [B2], [B12].

For a family-history scrapbook, work from copies of photos and documents [S56], [S57].
Skip AI enhancements that add, erase or replace details before placing the copies on the page [S56].

Before treating an image taken from MyHeritage as the original photograph, look at its
corners; MyHeritage's help places its marks at the bottom left [S12 @2026-11-12],
[S13 @2026-11-12]. A palette marks a colorized or color-restored photo, a magic wand an
enhanced one, a moving ball an animation and a bandage a repair, and the original is kept
separately [S12 @2026-11-12]. MyHeritage calls an animation a technological simulation, not
authentic [S13 @2026-11-12], [S14 @2026-11-12]. A marked image is a derived artifact; ask for
the original. A cropped or re-saved copy can lose the marks, so their absence does not show
that an image is unaltered.

In a Reimagine album, look for the edit icons on the thumbnails while choosing photos to
inspect. Open the separately stored original before using a marked photo as a source
[S12 @2026-11-21], [S58 @2026-11-21].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Color restoration sends the scan and any details of living or possibly living people pictured in it to MyHeritage for processing. The same gate covers colorizing a photo with Reimagine’s color wheel. Answer the privacy gate in `SKILL.md` first.

For a faded scan originally taken in color, use MyHeritage **Color Restoration**. Reserve
colorization for black-and-white originals. Label the result as color-restored and retain
the unedited scan for evidence [S48 @2026-11-20], [S49 @2026-11-20].

Check the original before using the color wheel in Reimagine. The same control colorizes
a black-and-white original and restores a faded color original. If the original colors are
intact, the result can look unchanged. Compare both versions before labeling the result
[S12 @2026-11-21], [S58 @2026-11-21].

In MyHeritage’s web **My Photos** gallery, open a faded scan originally taken in color and
select **Restore colors** on the color wheel [S80 @2026-11-22]. Use the before-and-after slider
on a restored or enhanced photo to locate details that changed, then read those details on the
unedited scan [S79 @2026-11-22], [S80 @2026-11-22], [S81 @2026-11-22].

Check each building and its position in the unedited scan before mapping a scene: in one
reported Gemini colorization, a recognizable barracks remained while the surrounding streetscape
changed [S82].

When the web restoration settings offer more than one model, open the cogwheel on the processed
photo, choose a model and select **Preview**. Press and hold the photo to compare the preview
with the previous edit. Save or cancel after comparing, and use the unedited scan for a
comparison with the source [S80 @2026-11-22], [S86 @2026-11-22].

**Privacy gate:** <!-- privacy-gate: publish --> Sharing from Reimagine sends the selected photo or comparison, with details of anyone shown, including living or possibly living people, to the chosen service and audience. Answer the privacy gate in `SKILL.md` before sharing.

From the single-photo view in Reimagine, tap the share icon at the top. Choose the original
when sending the source photo. Choose the before-and-after comparison to show the edit and
label which version was AI-processed [S58 @2026-11-21], [S59 @2026-11-21].

In a military portrait, inspect the collar for numbers or insignia. Use an existing
enhanced copy to locate the detail, check the reading on the original, and compare it with
period uniform references. Use the candidate unit to guide a search of service records
[S50], [S51]. Leave digits that appear only in the enhancement unresolved. Exclude facial
resemblance from the identity evidence and record a person’s recognition only as their
attributed claim.

## The pitfalls worth internalizing (the least-obvious, most-LLM-usable part)

For Russian Orthodox metrical books, use the [Reading the page checklist](russian-orthodox-metrical-book-recovery.md#reading-the-page) alongside these checks.

- **Chained tools propagate a single misread** — transcribe→translate→summarize means one bad transcription poisons every downstream output. (Family Locket)
- **Names, dates, and numbers are the high-error zone** — models transcribe narrative well but substitute a familiar name seen earlier; "November"→"December," "township 18"→"182." Domain knowledge (a plat can't be township 182) is what exposes them. (Genealogy Gems; James Tanner)
- **Scribal conventions can create false names.** Clerks broke words at the end of a line with no hyphen and not at a syllable break, so 'Chris' at a line end and 'tian' on the next line can be one name. In the cited Spanish examples, abbreviation marks support candidate expansions ('Franco' with an overline as Francisco, superscript 'Ant' and 'M' as Antonio and María); verify an expansion against the writer's usage or a period reading key. Before recording an odd fragment or surname as a new variant, test whether it joins the next line and whether each piece makes sense alone. Check the image for overlines and superscripts. Keep the line breaks and the abbreviated form, and add the joined reading or expansion as a note. Sometimes the pieces really are two words, and the sources give no fixed rule or complete list. ([Brady](https://www.youtube.com/watch?v=OU2cYqgN-lw), [Italian records](https://www.youtube.com/watch?v=UC1J5HuNYns), [Badal](https://www.youtube.com/watch?v=eb6YqIJ3aK4))
- **Machine translation can translate surnames away.** A surname built from an ordinary word, as many German names meaning mountain or house are, may come out as that noun, and the person seems to vanish from the translation. Before translating, note where each name sits in the original. Afterwards, check those positions and keep the original-language form in any extraction. The [listener-email advice](https://www.youtube.com/watch?v=Ofj5cluPmEQ) gives no worked example and says nothing about how specific tools behave.
- **Old spelling can break machine translation.** If older texts in a language translate into garbage while modern texts translate well, suspect a spelling reform before trusting the output. Convert the text to modern spelling with a documented old-to-new correspondence table, such as one in a period encyclopedia's article on the language. Then translate, keeping the original beside the converted text. Check each substitution. A Latvian forum contributor identified a table in the language article of a 1932 Brockhaus, but did not reproduce it [B80].
- **Some AI summary/narrative features read the INDEX, not the image** — they draw on indexed fields and silently re-use OLD index errors already corrected on the image elsewhere. Always open the image. (Genealogy TV; FamilySearch)
- **Military service and chronology.** Check the unit and dates in service and pension records. One generated Civil War regiment was fictitious, while the documented service belonged to the man’s brother [B42]. Check relatives with similar names before assigning the event.
- **It can't infer beyond supplied evidence and will REVERSE relationships to force a story** — and it can't independently locate a missing record. (Family Locket)
- **Context fatigue degrades long chats and documents** — quality drops and it drops or invents content past the window. Split into fresh chats and reload the current state. (DNAeXplained; Genealogy TV)
- **Names already known to the assistant.** Verify every extracted person and role on the page where the name appears. An estate-file reading reportedly listed a later daughter-in-law as a child and misnamed the widow [B58]. Memory contamination was the author’s hypothesis. Keep previously known names out of a blind reading and measure its results independently.
- **Full-text search is NOT exhaustive** — not every image is indexed or read correctly, and an HTR misread means a misspelled name won't exact-match. Search variants and wildcards, check it alongside internal indexes AND manual page browsing, and re-run every week or two as collections are processed. (Family Locket; James Tanner)
- **Image quality gates everything** — download high-quality images (not low-res screenshots), crop newspaper clippings tightly to stop line-detection chaos, and expect blurry originals to be unreadable. (Family Locket; James Tanner)
- **The model may see a smaller image than the file.** The vendor API (by default) or the agent tool in front of it may downscale an image above a size limit before the model sees it, so the file's byte size or pixel dimensions do not show what the model actually received ([Claude vision docs](https://platform.claude.com/docs/en/build-with-claude/vision), [computer-use screenshot sizing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool), checked 2026-11-02). Record the source's pixel size, what the tool reports showing, and that the effective model input may be unknown; if it is unknown, say so beside the reading. When letters or digits are small, crop the region from the original and read the crop. Keep the crop's binding (source file or ID plus pixel coordinates) and its line context, and check the reading against the full line; the vendor's guidance also warns against cropping away key context just to enlarge text. A reading that changes after re-cropping in a new chat does not show that the crop caused the change. Enlargement adds no detail, and generatively "enhanced" strokes are never evidence of the original. Limits differ by model and change, so do not hard-code pixel thresholds; cite the vendor page with its check date.
- **Formatting can carry meaning the model drops** — some models can't reliably read COLORED text and only sometimes recognize BOLD, and they handle tables and multi-column layouts inconsistently — exactly the shape of ledgers, registers, and census forms. (DNAeXplained; Family Locket)
- **Correct layout before recognizing text on complex pages.** Where the HTR tool supports separate layout recognition, inspect detected text regions and baselines against the image and correct layout errors before running text recognition on tables or multiple columns. [Family Locket's Transkribus tutorial](https://familylocket.com/transkribus-revolutionizing-handwritten-text-analysis-with-ai/) describes this sequence. Then check the recognized text against the image; a corrected layout does not itself verify the transcription.
- **Marks and placement.** Distinguish a dividing line from a cancellation and inspect underlining against the image [B65]. Preserve the layout of side notes and grouped names. For faint traces in a blank field, compare slant and letter direction with the reverse side if available; keep possible show-through unresolved until checked [B66].
- **Bracketed text with a 'do not read' note is a cancellation.** Official registers did not allow erasures. So in Russian-Empire metrical books a clerk put a miswritten letter, word or phrase in brackets and added a note such as *окаймленное не читать* ('the enclosed is not to be read'). Don't transcribe the enclosed text as a second name, a patronymic or an ending. Keep it as a cancelled reading, together with the note. Several participants in the [bracketed-correction discussion](https://forum.j-roots.info/viewtopic.php?f=4&t=4667) call this routine, but what the clerk first meant to write stays a guess.
- **A bilingual entry has two texts, and an overwrite can hide a third.** In a Russian-Empire rabbinate register, transcribe the Hebrew-script half separately from the Russian half. Record each parent's Hebrew name and patronymic beside the Russian form (for example, a Hebrew 'son of …' beside the Russian patronymic form), then compare the two halves. Where a name was written over earlier text, record both the visible reading and the one underneath, and label which is which. A forum reader reported that a Hebrew patronymic agreed with the underlying Russian reading rather than the overwrite [B81]. The image was unavailable. Preserve the disagreement and verify both texts before using either for identity.
- **Identify the document and its form before assigning fields.** Before transcribing or searching, note the language(s), script(s) (printed Fraktur and handwritten Kurrent can share a page), content type and author. A film of the right year may hold burials rather than baptisms, which would explain a 'missing' child. Don't infer confession from language: Latin does not prove Catholic, nor the reverse. Register headings vary by year and printed form. Scandinavian headings are long instructions (does the place column want village, farm, parish or street?), so match a heading translation to the register's year and form, and read it in full rather than reducing it to one word. ([Minert](https://www.youtube.com/watch?v=cc8_6tNN8C4), [Tanner](https://www.youtube.com/watch?v=1CzAygZqg2Q); their example slides and heading tables are not in the transcripts.)
- **Check a browser assistant’s search coverage.** Compare the places, relatives and spellings it actually searched with your research question, including a spouse’s other documented residence. Record outstanding searches before treating the result as complete [B30].
- **Auto-routing may not pick the reasoning model** — select the reasoning/Thinking model yourself for hard tasks. (Family Locket)
- **Open-web tools can't see gated genealogy sites** — Perplexity and AI web search work from the open web and can't reach sign-in-gated accounts; AI also reinforces misinformation posted repeatedly online. (Aimee Cross; DNAeXplained)
- **A block or a blank results page is not an absence.** A block, a timeout, a CAPTCHA, a WAF or geo-block, or a certificate error from a foreign IP is an access limitation, not evidence that the archive or record is closed or absent. A fetched results page that shows only column headers, an empty `{}` or a blank panel may be an unloaded result list, a login wall or a block. Log either case as an interrupted search in the [research log](research-documentation.md), have the user check the loaded rows and the result counter in their own browser, and never record NIL from it. Never bypass an access control: no VPN or proxy, no override of a certificate warning, no CAPTCHA solving by the agent; hand the step to the user's browser. Do not mass-download collections of unclear legal status, and use scans of unclear provenance, such as public cloud folders, only as leads.
- **Ancestry vs FamilySearch full-text is not the same capability** — FamilySearch's Full-Text Search does broad AI handwriting transcription across a growing set of image collections (land, probate, and more); Ancestry's Search Full Text leans more on OCR plus existing indexes, with AI handwriting recognition applied to selected pre-processed collections (e.g. the 1950 U.S. and 1931 Canada censuses) rather than across the board. For its 1921 England & Wales census, Ancestry licensed Findmypast's transcription rather than producing its own. Ancestry's separate image-HTR "Transcribe" beta (World Explorer / World Deluxe tiers; English, Spanish, French, Italian, German and more) still needs manual checking. Check whether the output is a transcription or a translation before using it [B16]. (Genealogy TV; Ancestry; Library and Archives Canada, 1931 census release; WDYTYA, 1921 census on Ancestry)
- **Saving an AI-index correction is a live shared edit** — visible on the record right away, searchable within minutes, and it persists even if you later abandon the record; and don't waste time on highlighting fixes (they don't train the model and can trigger tool errors). (Ada Luque Nelson)

For a disputed handwritten letter, collect several securely read examples from the same hand, including initial, medial and final positions and joined forms. Do not require one invariant shape: a scholarly analysis of the Vindolanda hand documents positional and joining variation in that script. Use the comparison as a reading test on the target page, without transferring its ancient letter shapes to a different language or period [S17](https://genealogytipoftheday.com/index.php/2024/10/15/inconsistent-writing/), [S18](https://genealogytipoftheday.com/index.php/2024/06/12/changing-up-the-handwriting/), [S19](https://romaninscriptionsofbritain.org/tabvindol/vol-I/introduction/ch4-d).

Keep *late* with its subject and the rest of the clause. A reader of a Pennsylvania deed interpreted it as a former surname; treating it as evidence of a death would have changed the relationship [S20], [S21]. Compare the writer’s other entries and record uncertainty if the wording permits more than one reading.

Preserve an unfamiliar status label in the transcript before interpreting it. "Grass widow" has senses that include a separated or divorced woman and a woman whose husband is temporarily away; the phrase alone cannot establish death, divorce or the reason for absence. Check usage in the document's own time and place, then seek the records needed to test the particular interpretation [S22](https://genealogytipoftheday.com/index.php/2025/08/31/varying-terminology/), [S23](https://www.dictionary.com/browse/grass-widow).

Do not let AI fill a sex field from a familiar-looking given name. Names can be shared across sexes and their usage changes. Preserve the record's actual wording or leave the field unknown; compare its stated relationships and other identifiers before connecting the person to a tree. A name-based guess is not a transcription of a recorded sex [S24](https://genealogytipoftheday.com/index.php/2023/01/14/are-you-certain-of-the-gender-2/), [S25](https://blog.myheritage.com/2026/01/unisex-names-are-they-actually-common/).

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Training a Transkribus model can send document images and transcriptions containing living or possibly living people's information to that service; answer the privacy gate in `SKILL.md` before supplying training material. When a public model performs poorly on a recurring hand, consider a custom text-recognition model using accurately corrected image/transcription pairs. Keep independent pages outside training to test the resulting readings against their images. Transkribus guidance checked 2026-11-16 distinguishes training, validation and test data and says that correcting text in the editor alone does not improve the model: a new training job is needed. Do not promise a clean transcript from training or assume an automatic test function is available [S26](https://www.pricegen.com/artificial-intelligence-and-the-future-of-family-history/), [S27](https://help.transkribus.org/training-text-recognition-models), [S28](https://help.transkribus.org/managing-datasets).

## Verification & privacy discipline

- **AI-generated transcriptions and abstractions are derivative artifacts, not independent evidence.** Verify record-derived claims against the original record, and contextual/research claims (terms, history, strategy) against an authoritative cited source, before either is used. AI is *safer* for analyzing, correlating, and summarizing records you already trust than for the initial finding phase; hallucination ranges from full fabrication to a subtle misunderstanding of intent. Use AI to think faster, never to decide. (Aimee Cross; Legacy Tree)
- **Several readings of one image are one documentary chain.** Readings by people, models or OCR do not corroborate each other. Repeating the request until the model agrees with itself verifies nothing. When a confident reading's structure (rows, columns, numbers) disagrees with the image, the reading fails however confident it is; recheck which image was actually opened. A matching file hash confirms the file, not the reading or the viewing channel. For a second reader or model, record whether it saw the earlier transcription, the expected names or neighbouring pages: a hint-aware re-read is not blind. Keep the superseded reading, the correction and its basis, and leave a disputed spot open.
- **Log which AI tools and conversations you used** — cite the AI step the way you cite any research step. (Family Locket)
- **Check where a correction actually landed.** When correcting a transcription or structured extraction that passes between tools, record where the correction was saved and which version downstream work uses. Reopen the downstream copy or export to verify that it carries the correction. Do not assume that editing one derivative updates the upstream transcript or trains its recognizer. The [DES/Transkribus handoff example](https://www.youtube.com/watch?v=6IwX6kZbx4Q) motivates this check; current synchronization behavior is not asserted. (CompGen; verification steps are Kinprove synthesis)
- **Privacy gate:** <!-- privacy-gate: third-party-tool --> Pasting living people's records into an AI chatbot sends their data to a third party; answer the privacy gate in `SKILL.md` first. **Apply the "water-cooler rule" before pasting living people's records into a consumer chatbot** — don't enter anything you wouldn't post publicly, because these tools may train on your uploads. Replacing names with **Person A / Person B** is *pseudonymization, not anonymization* — dates, places, relationships, and occupations can still re-identify someone, so also strip or generalize those indirect identifiers and treat the result as still potentially personal data; never upload private living-person data that fails the water-cooler rule. Use temporary chats, and keep a separate curated cloud account for connected folders. (This is the records-privacy caveat; the DNA recipe carries the separate de-identify/consent discipline for re-identifiable genetic data.) (Genealogy TV — Little & Thompson)

### Ask for a German-record reading review

**Privacy gate:** <!-- privacy-gate: publish --> The record image or link and draft readings may disclose information about living or possibly living people to FamilySearch Community and public readers. Answer the privacy gate in `SKILL.md` before posting.

For a German record, use FamilySearch Community's public **Germany Research** group and
start the discussion title with “Translation Request” [S31 @2026-11-18].

Check the source site's image-sharing terms first [S33]. Post the source image with the
chatbot's transcription and translation, mark both as drafts, and ask the volunteer to
check the readings against the image [S29]. Give the record's year and locality. Include the
full page if permitted so the volunteer can compare the handwriting. If you post a crop,
include a link the volunteer can open to the full page [S32]. If the terms bar reposting the
image, use a permitted, accessible link. Keep the request local if neither route is available.
