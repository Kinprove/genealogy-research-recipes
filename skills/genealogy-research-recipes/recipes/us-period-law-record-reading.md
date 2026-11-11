---
id: "us-period-law-record-reading"
title: "Read U.S. records under the law and legal language of their own place and date"
summary: "Read a U.S. record's legal words, courts, bonds, and age or inheritance rules under the law of its own place and date, and keep each inference within what that law required."
kind: "records"
scope: {"platforms": [], "tasks": ["Read a U.S. record's legal words, courts, bonds, and age or inheritance rules under the law of its own place and date, and keep each inference within what that law required."]}
triggers: ["A U.S. record uses a legal word or names an old court", "dower, dowry, next friend, adr c t a, voidable, penal sum or mainpernor in a record", "Did the law of that place and date allow this marriage or inheritance"]
privacy: "none"
gates: []
guardrails: [{"id": "US-PERIOD-LAW-RECORD-READING-01", "text": "a legal rule shows what the law provided at that place and date; it is not by itself a fact about a person."}]
handoff: ["court-case-file-recovery", "deed-content-relationship-clues", "evidence-proof-judgment", "missing-marriage-jurisdiction-search", "probate-case-document-inventory"]
checked: "2026-11-08"
checked_basis: "opened 2026-11-08"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "pointer", "group": "Courts, legislatures, prisons and institutions", "order": 1108}
---

# Read U.S. records under the law and legal language of their own place and date

Use this recipe when a U.S. record uses a legal word, names a court or office, or invites an inference from what the law allowed: a young bride, a widow's share, an intestate father's land, a bond, a juror list, a court date. It shows how to find the rule for that place and date, and how far the record can be read under it.

"The author" in this recipe is Judy G. Russell of The Legal Genealogist, whose posts are cited as S1 to S23.

Errors this recipe blocks:

- applying today's law, or one uniform "American rule", to a record from another place and date
- reading a legal word in its ordinary modern sense: a `next friend` as a non-relative, a `Court of Ordinary` as a routine sitting, an `adr c t a` as an intestate estate
- searching for dower and dowry as if they were one record
- turning a legal requirement into a fact about a person: land ownership from jury service, an unlawful marriage from a young bride, a clerk's error from a December 25 court date
- reading a bond's penal sum as money paid, or an enforced bond as proof of theft
- carrying a rule checked for one state into another state, or across a date when the law changed

Link out for the shared steps:

- **Reading deed type, consideration and parties:** [deed content clues](deed-content-relationship-clues.md).
- **Inventorying a probate file:** [probate case inventory](probate-case-document-inventory.md).
- **Finding a court file:** [court case file recovery](court-case-file-recovery.md).
- **Searching for a marriage record that is missing:** [missing marriage search](missing-marriage-jurisdiction-search.md).
- **Identity rulings, age thresholds as evidence, and negative findings:** [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- Inputs to gather first
- 1\. Find the rule in force for that place and date
- 2\. Read the word in a dictionary of the period
- 3\. Legal terms that an ordinary reading gets wrong
- 4\. Infer only what the law actually required
- 5\. Check inheritance and widows' rights against the date
- 6\. Read a bond as a promise with named people behind it
- 7\. Read cause-of-death terms by their line on the form
- 8\. Write the reading with its rule

## Inputs to gather first

- the date of the event, and the date of the record if it differs
- the place as it was on that date: county, then colony, territory, state or contested claim
- the record type, and the court or office that made it
- the legal words exactly as written, with abbreviations and Latin kept

## 1. Find the rule in force for that place and date

- **Search in order.** Look in the colonial charter or state constitution, then the statutes in force, then common-law principles such as Blackstone. Silence in the statutes does not mean no rule existed [S22]. This is a research order, not a rule stated for every state. It fits Georgia, where the 1784 adopting act received English law only so far as it did not conflict with the state's constitution and laws [S95].
- **Do not treat Louisiana as all one system.** It received common law only in part: its 1805 act construed named crimes according to English common law [S96], [S97]. Test the question at hand.
- **Fix the governing authority before statehood.** For a record made in the Vermont area, do not apply a later Vermont statute. First work out which competing authority could apply. Statehood took effect on 4 March 1791, and New York recognized Vermont in 1790 [S10], [S77], [S79]. Massachusetts and New Hampshire have no clean end dates: *Vermont v. New Hampshire* reports findings of recognition by New Hampshire in 1777, which New Hampshire contested, and by Massachusetts in 1781 [S77], [S78]. The author says there is no easy answer about whose law applied [S10].
- **Follow a bill through the session's journal, and know what it cannot show.** Check whether the jurisdiction published legislative journals, then search Google Books, HathiTrust and Internet Archive for that session. The author's example is the New Hampshire Senate in 1829 [S11]. Journals record a bill's introduction, committee referral, amendments and votes, but they typically contain no debate, so they may show what happened to a law without explaining why it changed. Not all are online [S101], [S102].
- **Say when you did not find it.** If no rule turns up, write "rule not found for this place and date" and leave the inference open. Do not fall back on a rule from another state or on today's law.

## 2. Read the word in a dictionary of the period

- **Use a dictionary close to the record.** When a term in an older statute is missing from Black's 1891 dictionary, try an older one closer to the statute, such as Tomlins's 1797 revision of Giles Jacob [S12], [S103], [S104].
- **Find abbreviations where the dictionary files them.** In Black's, look among the abbreviation entries at the start of the letter, not under the word the abbreviation accompanies, then look up the expansion. This was checked only for the letter C of the 1891 text [S18], [S105].
- **Use a modern explanation only to understand the definition.** When a period definition rests on further unexplained terms, Wex, the Cornell Legal Information Institute's dictionary, is plainer [S15]. Wex is modern and may not cover an older term, so check that its explanation fits your period [S106].
- **Consider a misprint.** If a statutory word appears in no period dictionary, a printer may have changed it. Hening's printing of Virginia's 1785 inheritance act has `parency` for `parcenary`: intestate land passed to kindred as joint heirs. An 1830 Virginia opinion quotes the act as "in parcenary" [S12], [S38], [S80], [S81].

## 3. Legal terms that an ordinary reading gets wrong

| Term | Read it as | Do not read it as | Limits |
| --- | --- | --- | --- |
| `dower` and `dowry` | Dower is a widow's provision from her husband's lands, assigned in records after his death. A wife's release of it can appear in her husband's conveyance while both are alive [S41]. Dowry is property the wife brought, found in the marriage contract in Civil Law places [S1], [S24] | Two names for one record, or a release in a deed as proof of widowhood | Quebec and New France also had dower (*douaire*), often set in that contract. Louisiana did not recognize dower [S51], [S52], [S53]. The word dowry is also used in common-law places [S1] |
| `widow's thirds` | Dower: usually a life estate in one third of the husband's lands [S5], [S69], [S70] | A share she owned outright | "Usually", not always |
| `Court of Ordinary` | The probate court in Georgia and South Carolina. Search probate holdings under that name [S3], [S26], [S57], [S59] | A routine court session | Georgia renamed it Probate Court in 1974. Georgia's Inferior Court held probate from about 1798 to 1852, with the Court of Ordinary before and after, and bound out orphans [S54], [S55], [S56]. A library note says Charleston County's Probate Court replaced it in 1868 [S58] |
| `next friend` | A competent person acting in the name of a minor, married woman or other person lacking capacity, often a parent or other relative [S15], [S49] | Proof of no kinship, or an appointed guardian | Not every next friend was kin. A court could name one without making that person a guardian [S84] |
| `sui juris` | A person with full civil rights and capacity. Someone not sui juris needed a representative such as a next friend [S15], [S39], [S45] | Latin to skip | |
| `void` and `voidable` | Void has no legal force and nothing can cure it. Voidable can be cured by act or confirmation [S16], [S34] | Synonyms | For underage marriage see step 4 |
| `mainpernor` | A surety distinct from bail: could not surrender the defendant early and answered for his appearance on all charges [S6], [S50] | A synonym for bail | The author infers greater trust and suggests checking for kinship. That is an inference, and no source tests it [S6] |
| `puts himself upon the country`, `ponit se super patriam`, `po. se.` | A tender of issue submitting the case to a jury; in criminal records, the term on a not-guilty plea [S4], [S27], [S28], [S29] | A statement about geography | |
| `adr c t a` | Administrator *cum testamento annexo*: a will existed, but it named no executor, named incapable persons, or the named executors refused to act or had died. Look for the will [S18], [S46], [S47] | Proof the person died intestate | |
| `curator` (Missouri) | Guardian of a ward's estate, as distinct from guardian of the person [S18], [S89] | A vague custodian | The author reads `g & c m h` in one 1876 docket as guardian and curator of minor heirs. No source confirmed that shorthand [S18] |
| `-ix`, `-trix` endings | Spelled out in full (administratrix, executrix, testatrix, creditrix, tutrix, relatrix), a female role-holder, even with an ambiguous given name [S13], [S30], [S31], [S32], [S33], [S40], [S44] | Something to leave undetermined | The dictionaries define the words; they do not rule out a clerk's error in one record |
| `ultimate facts` | In court cases from the mid-1800s to the 1930s, the bottom-line facts in issue, in the pleadings or a court's findings, as distinct from evidentiary facts [S2], [S25], [S90], [S91] | Emphasis meaning "the true facts" | The author quotes that courts found the distinction hard to apply consistently [S2] |
| `indenture` (a form of deed) | Any reciprocal sealed agreement between two or more parties [S8], [S37], [S42], [S41] | Only servitude, apprenticeship or land | The author's example is an 1857 Vermont prenuptial agreement [S8]. A 1760 Boston premarital agreement is also styled an indenture [S107] |

## 4. Infer only what the law actually required

- **A young bride is not proof of an unlawful marriage.** Find the statute in force at the exact time and place. Where the common-law rule applied, a male at fourteen and a female at twelve could consent to marry, and a marriage below those ages was inchoate and voidable, not simply impossible [S14], [S48]. Do not assume which rule applied. The Ohio Supreme Court said in 1851 that the common-law rule prevailed in some states while others set the matter by statute, and Ohio's own ages were eighteen and fourteen [S83].
- **Silence before the age of consent did not settle an underage marriage.** At common law the right to disagree arose on reaching that age, and assent or continuing together afterward confirmed the marriage [S48]. Authority varied: the same Ohio decision treated such a marriage as void absent confirmation after age [S83].
- **Test a young mother against every age record, as the author does.** Subtract the governing minimum age from the child's birth date to get her latest qualifying birth date. Compare it with the birth range from each census, obituary and tombstone. In the author's Alabama example the records were inconsistent and the result was only that she may have been old enough [S14]. Failing the test does not show the marriage was void: in Alabama a marriage below the legal age was voidable, standing unless set aside [S108].
- **A juror list shows eligibility under that year's act.** On a 1748 Virginia county-court juror list, first identify the jury. Under the 1705 act a county-court trial jury needed a visible estate, real or personal, of 50 pounds sterling, not land ownership. A county grand jury was summoned from freeholders, and a jury trying a crime or title to land needed a freeholder with a visible estate of 100 pounds sterling [S99]. These are legal requirements, not proof of what a man held. One published reading infers that he did not keep a tavern or own a mill [S23]. Do not adopt that inference: the exclusion is in the October 1748 act, covers only county grand jury summonses, and took effect after 10 June 1751 [S98], [S99].
- **A December 25 court date is not an error by itself.** Check when that jurisdiction made Christmas a legal holiday. The 1870 federal act reached only the federal workforce in the District of Columbia, and states adopted the holiday at different dates [S19], [S92], [S93]. No source documented a particular court sitting that day, so treat this as a reason not to correct the date, not as proof that court sat.
- **Marriage into the Cherokee Nation did not end U.S. citizenship.** For a U.S.-citizen woman adopted into the Cherokee Nation in Indian Territory by intermarriage, search Cherokee court records for her civil suits with tribal members. Do not read later naturalization papers as proof she had lost citizenship. The decision rests on Cherokee treaties and does not establish this for recognized tribes generally [S7], [S71].

## 5. Check inheritance and widows' rights against the date

- **North Carolina land.** Before the April 1784 act, an intestate father's land passed to the oldest son. Do not apply that rule after it. The act gave land to all sons equally, and to daughters only if there were no sons [S5], [S67]. One secondary source says daughters shared with sons from 1795 [S68].
- **Virginia land passing by intestacy.** Check the death date against 1 January 1787. Earlier, the oldest son took the land, with daughters taking together only when there were no sons. From that date sons and daughters inherited jointly, with no preference by age or sex among children. The act kept a male preference among lineal ancestors [S12], [S80], [S82].
- **Illinois dower not assigned within a month of the husband's death.** Look in that county's circuit court chancery records for a petition for assignment of dower (Revised Statutes of 1845, ch. 34, sections 18-19). Check the text in force for your date. The author reports one 1880 bill alleging underage heirs, improvements and taxes paid [S20], [S94].
- **Broad powers in an Alabama will.** When a will gives a spouse everything with full power to sell and convey in fee simple, look for limiting words such as "during her life" and a gift over at death. If present, she may dispose of the property while living, and the remainder takes only what she did not dispose of. Without a limited remainder she took an absolute fee. This is confirmed for Alabama under the Code sections quoted in *Hood v. Bramlett* (1894); check other states [S21], [S100].
- **Look for a premarital agreement.** For propertied people entering a second or later marriage, one may set out what the widow receives instead of dower [S8], [S107], [S109]. Bouvier (1856) recognizes a jointure made before marriage in satisfaction of dower [S43]. For Jewish families, the ketubah is the marriage contract [S8], [S110]. The author does not say where such agreements were usually recorded; the example was a donated document.
- **Look beyond estates in a Georgia Court of Ordinary.** FamilySearch county pages list twelve months' support, poor school funds, free persons of color, apprenticeship indentures, lunacy, Confederate pension rolls and estray sales, each for particular counties and years [S3], [S60], [S61], [S62], [S63], [S64], [S65], [S66]. Confirm the series for your county.

## 6. Read a bond as a promise with named people behind it

- **The penal sum was promised, not paid.** When an official bond names a penal sum and sureties, read the sum as a secured promise to pay on default, not money deposited or spent by the officer or sureties. The author says "in most cases", at least until corporate sureties became the norm [S9], [S35], [S36].
- **A surety is a lead.** On probate, court, marriage and bastardy bonds, treat a named surety as a lead to a relative or close associate of the principal, and research that relationship [S72], [S73], [S74]. A surety was not necessarily related. The author treats sureties on official bonds the same way [S9]; no independent source was found for that.
- **An enforced bond is a claim of breach, not a finding of theft.** Read enforcement of an official bond as a claimed breach of official duty, as a 1912 Wisconsin case required. A shortage or failure to pay over does not by itself show theft or bribery. Sureties could also answer for a shortage found after the officer's death, as in an Arkansas case [S75], [S76].

## 7. Read cause-of-death terms by their line on the form

These readings come from a 2003 standard form and from current county and federal guidance. Check the form used in your certificate's year.

- **Part I runs backward in time.** On the standard certification, read the first line of Part I as the direct cause and the lowest completed line of Part I as the underlying cause the certifier entered. The lowest line is not always the selected underlying cause: the NCHS manual has further selection rules [S17], [S87], [S86].
- **An earlier injury or illness counts as underlying only through an unbroken sequence** to death, with no intervening cause [S17], [S85].
- **`Proximate` is not the nearest cause in time.** Read `proximate` and `underlying` as the same thing, as Harris County's medical examiner glossary does: the disease or injury that started the chain to death. Read `immediate` as the final event in the sequence, closest to death [S17], [S85], [S88]. The author also treats `ultimate` and `proximal` as equivalents; no independent source was found for those two.

## 8. Write the reading with its rule

For each legal reading you rely on, keep one row:

| Field | What to write |
| --- | --- |
| Words as written | The term or abbreviation, unchanged |
| Place and date | The jurisdiction on the event date |
| Rule and source | Statute, case or dictionary, with edition and year |
| Source level | Primary text read, secondary summary, or rule not found |
| What it supports | What the law required or allowed |
| What it does not show | What the person actually did, owned or was |

A rule shows what was required or allowed. It does not show what happened in one family. Use the row as a dated hypothesis and take identity and kinship rulings to [evidence/proof judgment](evidence-proof-judgment.md).
