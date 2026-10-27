# Extract French and Belgian civil acts field by field

Use this when you have the image of a French-language birth, marriage or death act from France or Belgium and need its fields: the act date, the event date, declarants, life-status words, clerk corrections, statements about a parent's death, and children legitimated by the marriage. The output is a field table and a list of acts to retrieve next. It does not rule on identity or proof. For status words read as a statement on one date, see [evidence/proof judgment](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md). For AI transcription limits and keeping a date's type separate from the event, see [AI for documentary records](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/ai-for-documentary-records.md).

Work from the original image. A yearly index or a ten-year table (*table décennale*, available for Belgian civil registers in the FamilySearch catalog) is only a way to find the act. Marriage acts hold leads that an index leaves out. [S1], [S2]

## Check a Paris reconstructed-record branch

If the original Paris civil series is unavailable for the event, [S3] identifies a
separate *état civil reconstitué* and its *fichiers*. Check the actual collection
description and coverage, then use an applicable reconstruction-file name/date lead
to locate the reconstructed act. Searching the ordinary register series does not
search this separately created corpus.

Read and cite that act as a reconstruction. Preserve any stated reconstruction
date and basis separately from the event date; a named parish register, notarial act
or family paper remains an uninspected source until retrieved. Record the
reconstruction ranges actually checked. A miss there does not show that the event
did not occur or that no other reconstruction survives.

## Anchor every act on its own date

1. Record the act's opening date first, as its own field. In birth and death acts this is the date the act was recorded, not the date of the event. [S1]
2. Resolve relative expressions against that act date: *aujourd'hui* (today), *hier* (yesterday), "the Nth of this month", or a late declaration that gives a day and says "N years ago". Store two fields: the act date, and the event date as stated (literal) or as resolved. Never fill only one date field. [S1]
3. In a marriage act, the opening date is the marriage date. The spouses' birth extracts were handed to the officer, who worked out each spouse's age from them. These ages contain errors. Treat the age as derived, and keep any mismatch with the birth act visible instead of correcting it. [S1]
4. Years can be written out as French number words, for example a "four-score-and-eleven" form for 1791. Transcribe the literal words beside the number you read from them. [S2]

## Convert Republican dates with a tool, never by arithmetic

1. Write down the literal Republican date: day, month name and year number. Enter it in a Republican–Gregorian converter and record the Gregorian result next to the literal date, naming the tool. The napoleon.org converter takes a day, a month from a dropdown and a Roman-numeral year (I–XIV), and converts in both directions. Do not work the date out in your head. Example: 17 Floréal year XI = 7 May 1803. The presenter's other example, 10 Thermidor year IX, falls in Thermidor (about 19 July – 17 August); run it through the converter for the exact day. [S2]
2. Many registers are filed by Republican year. To browse them, convert the Gregorian target date into a Republican year first. Later marriage acts can still give a spouse's birth in Republican form, so you will need the converter for acts written after 1805 as well. [S2]
3. Handwritten month names are easy to confuse. The presenter has mixed up Brumaire and Frimaire. Check the month you read against the order of the entries before and after it in the register. If the order does not settle it, keep both readings and convert each. [S2]
4. Which acts can carry Republican dates: the calendar was decreed in October 1793 and applied from day one, 22 September 1792. France returned to the Gregorian calendar on 1 January 1806. In Belgium, annexed in 1795, the Republican calendar was used in the civil registers from 17 June 1796 and became mandatory from 3 April 1798 (Leiestam, Familiekunde Deinze). Use these dates to spot which acts may carry Republican dates. They do not tell you what a particular commune's clerk actually wrote. [S2]

## Apply *je dis* corrections

The presenter explains that a clerk who made a mistake wrote *je dis* ("I say", meaning "or rather"), and that the value after it replaces the value before it. Her example reads like "born on the 5th of March, *je dis* the 8th of April". Extract only the corrected value as the field. Record the replaced value in a note marked "superseded by clerk". Never give both as alternative dates or names. [S1]

## Read status words as limits at the act date

- *veuf / veuve de* (widower / widow of): the named spouse died before the act date. The presenter says a widower clause in a marriage may give the first spouse's death date and place. If it does, add that as a death-act lead. [S1]
- *époux / épouse de* (husband / wife of): the spouse was alive at the act date. Look for their death after it. [S1]
- *défunt / décédé(e)(s)* before a parent: that parent was dead by the act date. Under the Code civil, a deceased parent's death had to be proven to the officer at the marriage, so marriage acts often give the date and place of death. Use the gender and number endings to see which parent the word covers. In the presenter's example the plural *-s* showed that both parents had died. [S1], [S2]
- *présent(e)* parent: the parent was alive and present at the marriage. [S1]

Each of these words limits the date range of an event. None of them is the event's own record. Whether the word is reliable is a question for evidence/proof judgment.

## Classify every statement about a parent's death

For each parent marked as deceased, record the basis of the statement as one of the following:

1. **Dated statement** (a date and usually a commune). Convert the date if it is Republican, then search that commune's death register around that date. [S2]
2. **Undated "died before"** (the presenter shows a word meaning "earlier"). This gives only an upper limit, the act date. The presenter takes it as a sign the officials could not find the death act. Treat that as her inference, not a negative search result. [S2]
3. **Witness attestation**. When a parent's death act could not be produced, the Avis du Conseil d'État of 4 Thermidor XIII allowed a declaration sworn by the four marriage witnesses to be recorded in the marriage act. The legal formula concerns not knowing the place of death or last domicile. In the presenter's example, a mother's death "about 22 years ago" was attested this way because it was not found in that place's registers. Record the approximate date as secondhand testimony from the date of the attestation. The attestation establishes only the declarations the act records. Treat a register search as done only when the act says so, and only for the place and registers it names. It does not prove that no death act exists elsewhere. The presenter says such a record cannot be found. Do not repeat that as a finding. Keep a lower-priority search open in other likely communes and periods. [S2]

## Read a marriage to the end for legitimated children

1. Do not stop after the couple, the parents or the witnesses. After the formula stating that the couple are united in marriage "in the name of the law", look for the couple *ont déclaré … est né d'eux* (have declared … was born of them) a child whom they recognise and legitimate by this marriage. Under Code civil art. 331, a child born before the marriage was legitimated by it if recognised before or in the marriage act. [S1], [S2]
2. For each child, record: sex, the commune where the birth was registered (in a phrase like "inscribed in the civil-status registers of …"), the date given (as written; convert it if Republican), and the name under which the child was registered. The presenter usually sees one such child, sometimes two, and gives an example with five. [S1], [S2]
3. Look for the birth act in that commune on that date under the **mother's surname**, and check its margin for a legitimation note. Then link it to the **father's surname** the child is expected to use in later records. Keep both forms as linked name variants, not as a merge. Whether the man legitimating the child is the biological father is a separate question. [S1], [S2]

## Output

For each act, return a table with these fields:

- commune, register type and image locator
- act date
- event date (literal, converted or resolved, and the converter used)
- declarants, in order
- the status limit for each spouse and parent
- *je dis* corrections (kept value / superseded value)
- the basis of each parental death statement

Then add:

- a follow-up list of death and birth acts to retrieve, each with commune and date range
- the legitimated children, each with both surname forms
- unresolved readings, such as a month name you could not settle
