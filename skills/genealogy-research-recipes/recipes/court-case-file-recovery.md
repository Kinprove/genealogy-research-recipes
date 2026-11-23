---
id: "court-case-file-recovery"
title: "Recover a U.S. court case file from its pointer records"
summary: "Recover a U.S. state or local civil, divorce, criminal or incapacity case file through the records that point to it."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "COURT-CASE-FILE-RECOVERY-01", "text": "Captions, arrests, index entries and case-law searches stay bounded leads."}]
handoff: ["criminal-court-prison-record-recovery", "us-federal-court-case-file-recovery"]
checked: "2026-11-07"
checked_basis: "checked 2026-11-07"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": ["request", "third-party-tool"], "contact": []}
router: {"section": "Records by country and region", "group": "United States: military, land, courts and law", "order": 202}
---

# Recover a U.S. court case file from its pointer records

Use this recipe when a U.S. civil, chancery, divorce, criminal or incapacity proceeding may involve the person. Treat the proceeding as a case file. Recover it through the records that point to it, then inventory its loose papers. Captions, arrests, index entries and case-law searches stay bounded leads.

For federal jurisdiction, record groups and NARA custody, use
[U.S. federal court case-file recovery](us-federal-court-case-file-recovery.md).

Start here for a case file from any U.S. state, county or local court, criminal cases included.
When the lead is an arrest, a prison or a census institution entry and you still need to find which
court tried the case, or when you need the prison, inmate, clemency or pardon records that follow a
sentence, use [criminal court and prison records](criminal-court-prison-record-recovery.md), then
return here for the case file.

For the rule that an indictment or presentment is only an allegation, use [evidence/proof judgment](evidence-proof-judgment.md). Estate files, including reported probate opinions and probate appeal packets, belong to [probate case inventory](probate-case-document-inventory.md). Naturalization proceedings belong to [U.S. immigration § 9](usa-immigration-search-recovery.md). To recover a recorded judgment or a sheriff's deed in the land books, use [land index recovery](land-index-book-series-recovery.md).

## Contents

- Classify the proceeding before reading it
- Collect locators from every pointer series
- Find a divorce or separation before calling it missing
- Request the loose papers as their own series
- Inventory the file by procedural stage
- Search the newspapers around each court date
- Bound the published case-law search
- Set the window and close with a case register

## Classify the proceeding before reading it

- **Treat a "State v." caption as a clue, not as a crime.** A criminal case is always brought by a government and can lead to criminal penalties such as jail, probation or fines. Governments also sue civilly, for example over damage to government property or a broken contract. Classify the case as criminal when the docket labels it criminal or an indictment, information or criminal charge is on file. If you have the caption and a jail census entry, log it as probably criminal, pending the file. If you have only the caption, record the proceeding type as unresolved and get the file. [S2]
- **Treat an arrest, charge or newspaper arrest report as the start of a case.** It is not a finding about conduct. An arrest is a detention and does not mean the person committed a crime. Follow the case to a dismissal, plea, acquittal or sentence before stating what happened. [S2]
- **Treat a census entry in a jail or prison as a strong pointer to a criminal case.** First check that the entry lists the person as an inmate, not as the keeper or a member of the keeper's household. Tanner reads such an entry as meaning there was probably a criminal case. Search for that case. Do not state the charge or the outcome until the file shows them. [S1], [S2]
- **Do not read a missing newspaper report as no arrest.** Tanner says newspapers reliably reported visible or major arrests, but minor arrests such as shoplifting often went unreported outside small communities. [S2]
- **Separate locators from flags.** A recorded judgment or satisfaction of judgment identifies the case, the court and the parties. An appellate citation shows that a lower-court case was filed. Treat both as locators and go to the file. A divorce is a lead to the granting authority's records, which may be a court or, in some early periods, a legislature. A claimed injury makes a lawsuit likely. Log divorces and injuries as reasons to search, not as findings. [S1]

**List the courts that heard each kind of case in that place and period before you log a negative.** Probate, guardianship, divorce, foreclosure, property disputes, criminal cases and equity could each go to a different court [S21]. Divorce in Minnesota was generally a district-court matter, yet in Ramsey County some divorces of the 1860s and 1870s were heard in a court of common pleas [S36]; in Allen County, Indiana, in 1909, divorces were heard in both the circuit and the superior court [S37]. Search each court that could have heard the matter in those years, and log each court's negative separately.

**Find the court that heard equity at that date before searching for a chancery case.** Where a state had a separate chancery court, its bills, pleadings and minutes were recorded apart from the county and circuit court minutes, and the court often served a district of several counties [S16], [S17]. In Tennessee, the 1837–38 act made Fayette, Shelby, Hardeman and McNairy counties one chancery district sitting at Somerville, and the 1869–70 act divided the state into twelve chancery districts [S17]. Virginia moved chancery between courts: superior courts of chancery (1802–1831), circuit superior courts of law and chancery (1831–1851), then circuit courts from 1852, with county courts also hearing chancery until 1870 [S18]. Read the bill as the complainant's allegations, which the defendant's answer responds to; only the decrees record what the judge decided [S16], [S18]. Do not state a sale, debt or relationship from the bill alone.

**Maryland trial and appeal records.** Use the trial and appellate distinction from the available excerpt [S66 @2026-11-21]. For a modern divorce, start with the county or Baltimore City Circuit Court. For a criminal case under the modern system, check the District Court for misdemeanors and specified felonies and the Circuit Court for more serious charges. Follow a documented appeal to the reviewing court, which can be the Circuit Court for a District Court case [S67 @2026-11-21]. For a case before July 5, 1971, check the predecessor courts of limited jurisdiction, such as the trial magistrates' courts or People's Courts, for matters later assigned to the District Court [S68 @2026-11-21].

## Collect locators from every pointer series

Build a crosswalk from each pointer to the file it implies. Keep these parts separate:

- the pointer's literal text and locator
- the court, caption and party roles
- the case number
- the proceeding type

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A court index query sends the party's name and any date, court or place filters to the court, archive or database provider that runs the index. Apply the privacy gate in `SKILL.md` before submitting a query.

**Financial trouble as a lead.** Check the civil case index for debt actions in the ancestor's locality [S91]. Follow the court and party role into the case papers, and record whether the court actually entered a judgment.

**Dates in court indexes.** Broaden a court index's date range when a newspaper or another pointer gives only a hearing or decision date [S91]. Check what the date field indexes before using it. Search back from the known event for the filing, and keep a separate window for later action.

In Indiana's MyCase, use the file-date filter for the initial filing date [S92 @2026-11-22]. Leave that filter open or extend it to earlier years when the date in hand is a later court event.

**Recorded judgment or satisfaction of judgment in land records.** This identifies the court, the case and the parties. Copy those details and use them to request the lawsuit file. [S1]

**Sheriff's sale, foreclosure or lien notice.** Tanner describes a chain: judgment, application and notice of sale, sale, a possible redemption period, then a sheriff's deed or a payment of the proceeds to the creditor. If real property was involved, the later documents are in the recorder's office with the land records. The sale notice was sometimes only posted at the courthouse, so it may be missing from the court file. Expect papers after the sale. Search the court file and the recorder's land records for each step of this chain. Tanner says the procedure differed by county and state, so read each document against the local procedure rather than expecting a fixed sequence. [S10]

**Bound minute books.** Check the index heading and the dates on the book before citing its coverage. In Stewart County, Tennessee, an index described as covering 1821–1834 includes jurors, attorneys, the solicitor general, securities and court officers [S6]. Where an index includes such roles, search beyond the parties' names. Follow the volume and page to the minutes, then use the entry to identify the case.

**Read the order or minute book around the entry, not only the indexed line.** Order and minute books record all matters brought before the court while it was in session [S42]. Page through the volume on either side of a family entry: its sittings show when the court actually met, and its routine business shows what a terse entry means [S30]. Find the county's order books through the FamilySearch Catalog by county.

**Essex County, Virginia, early court orders.** Use Wesley E. Pippenger's *Index to Court Orders, 1702–1715* from the available excerpt [S115 @2026-11-22]. Follow the indexed book and page into Deeds & Wills Book 10 or Order Books 3 and 4. Check gaps before using a miss. Order Book 4 has missing and damaged pages [S119 @2026-11-22], [S120 @2026-11-22].

For an Essex order dated 1727–1729, check both parts of Ruth and Sam Sparacio's *Order Book Abstracts of Essex County, Virginia, 1725–1729* if the date is uncertain, following the two-part lead from the available excerpt [S115 @2026-11-22]. Part I ends on 21 September 1727 and Part II runs from 21 November 1727 to 20 March 1728/9 [S123 @2026-11-22]. Use the 1725–1729 orders on Library of Virginia reel 68 to follow a citation or check the space between the parts [S119 @2026-11-22].

For Essex County orders after the Sparacio volumes, choose the Pippenger volume by date from the available excerpt [S115]. Use Book 8 for 1729–1733/4 [S116], Books 9–10 for 1733/4–1738 [S117], or Books 11–12 for 1738–1741/2 [S118]. Check the executions as well as the orders when tracing enforcement of a judgment.

**Spotsylvania County, Virginia, orders.** Use the 1746–1748 abstract from the available excerpt [S112 @2026-11-22] for sessions from 8 September 1746 through 9 March 1748/9. It covers pages 392–504 of the county court order book [S113 @2026-11-22]. Recheck the order and surrounding pages in the 1738–1749 book on Library of Virginia reel 44 [S114 @2026-11-22].

**Pennsylvania Common Pleas and Quarter Sessions.** Use the two court names from the available excerpt to find the county's separate minute, order and docket series [S66 @2026-11-21]. Check the county's court holdings and the county entries in Pennsylvania State Archives Record Group 47 for copies. For Chester County, look under Prothonotary for historical Common Pleas records and under Clerk of Courts for historical Quarter Sessions records [S69 @2026-11-21], [S70 @2026-11-21].

**Justice of the peace dockets.** Follow the state-archive lead from the available excerpt [S66 @2026-11-21]. Check finding aids under the locality and the justice's name as well as the court. For example, the Pennsylvania State Archives lists Morrisdale justice Henry Northover's Clearfield County dockets under MG-004, roll 7178 [S71 @2026-11-21]. Check county courthouse or county archive holdings when the state listing lacks the docket or years [S72 @2026-11-21].

**Highland County, Virginia, circuit court order books.** Recheck the order books described as locked in September 2022, using the lead from the available excerpt [S63 @2026-11-20]. Have the user open the exact film in their own signed-in FamilySearch account. Follow its access message to a FamilySearch center or affiliate library if it lists one [S64 @2026-11-20]. If the images are unavailable, match the series and dates to the Library of Virginia's microfilm guide, which lists separate common-law and chancery order books. For example, look for Chancery Order Book 1, 1848–1873, on reel 7 [S65 @2026-11-20].

**State chancery folder index.** The Library of Virginia chancery index is searched by county or city, then by surname, plaintiff or defendant. Not every listed case has linked images. If a folder is listed without images, keep its case details. Then search the FamilySearch Catalog by county, not by name, for that county's court records. [S7] For Catalog and film routes, use [FamilySearch workflows](familysearch-practical-record-workflows.md).

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A chancery index query sends the historical ancestor's or sibling's name and any locality or year filters to the Library of Virginia. Apply the privacy gate in `SKILL.md` before submitting the query.

**Virginia chancery suits involving siblings.** When working back from a documented ancestor, use the sibling search from the available excerpt [S73 @2026-11-21]. Enter the ancestor's name and each documented sibling's name in separate Chancery Records Index searches. Check each as plaintiff and defendant, and use the surname field for names indexed outside those roles [S74 @2026-11-21]. Follow suits involving any sibling for evidence about the preceding generation, even when the ancestor is absent from the caption.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> The index search sends a historical party's name and any court or date filters to MyHeritage. Keep the query to the historical parties and their case details. Apply the privacy gate in `SKILL.md` before submitting the query.

**Maine court registrations.** For 1696–1854, enter the plaintiff's or defendant's name in the Name fields of MyHeritage's Maine, Court Registrations index [S51 @2026-11-18], [S52 @2026-11-18]. From a hit, copy the party names, court, session date and recorded cause of action where given [S52 @2026-11-18]. Use the entry to locate the court record and leave the outcome open until you find the disposition.

**Maine before statehood.** For sessions before March 15, 1820, identify the court in the Massachusetts system in force on the session date. Maine was part of Massachusetts before statehood on that date [S51], [S53], [S54]. Check Maine and Massachusetts court finding aids by the historical court name and session date [S55], [S56].

**Incapacity indexes.** Locate the index under the court's period heading, which may use terms such as “lunatics” and “drunkards.” In Clearfield County, Pennsylvania, searches of that index for Robinson Curry and of the prothonotary's divorce files for Robinson and Nancy Curry found other Currys. Two recordings describe the same search [S8], [S9]. Log the name, index, court and years for each miss. The entries for other people establish neither Robinson's capacity nor the couple's marital history.

When the loose equity file is unindexed, check for a digitized county equity docket or its index [S94 @2026-11-22]. In Anne Arundel County, Maryland, use the Maryland State Archives' Civil, Equity, Law, & Divorce Docket index, CE514 (1852–1991), to get the case number. Match it to the county's equity or divorce paper series for that year [S95 @2026-11-22].

**Guardianship clues in civil files.** When the separate guardianship search stalls, use the equity and other civil suit search from the available excerpt [S121]. Check the court's county and state archive finding aids under the guardian, ward and other known parties. Look for appointment or removal papers in the case. The Washington County, Tennessee, Clerk & Master finding aid lists a petition for removal of guardianship among the chancery cases [S122].

**New Jersey Supreme Court case files.** Use the party-name lead from MyHeritage's collection announcement [S82 @2026-11-22]. For 1704–1844, look up the plaintiff or defendant in the New Jersey State Archives' Supreme Court Case Files index. Keep the case number and check whether the archive links the papers [S83 @2026-11-22].

**Indiana court registrations.** Search MyHeritage's Indiana Court Cases by name for registrations from 1818 onward [S84 @2026-11-22], [S85 @2026-11-22]. Copy each party's role, trial date and place, court and stated cause of action where given [S85 @2026-11-22]. Use the court and date to look for the underlying file. Check the Indiana State Archives catalog's Entity Search under the relevant clerk's office, especially when the commercial index has no result [S86 @2026-11-22].

**Central Wisconsin court registrations.** Search MyHeritage's court registrations from 1837 onward for Dodge, Fond du Lac, Green Lake, Marquette and Winnebago counties [S89 @2026-11-22], [S90 @2026-11-22]. Record residence separately from the court's location and follow the court and case details to the county series.

**Appellate citation.** An appeal shows that a lower-court case was filed. Go to that court for the file. [S1]

**Judge named without a court.** If an article names a state or local judge but not the court, do not give up on the court record: The Legal Genealogist suggests looking for other newspaper articles from the same time and place to get the judge's full name, the court's name or the exact place the judge was working. [S12] Also look for a published "History of the Bench and Bar" or similarly named volume for that time and place, as the author recommends, for example through Google Books with "history bench and bar" as the search term and the 19th century as the time frame. [S12] Such volumes exist for Wisconsin (1882), Ohio (1897) and Missouri (1878), and the Ohio text shows one naming a judge's court. [S13], [S14], [S15]

## Find a divorce or separation before calling it missing

**Privacy gate:** <!-- privacy-gate: request --> A request for a divorce, support or separation
file names both spouses and their children and repeats allegations about the marriage; a
20th-century party or child may be living. Answer the privacy gate in `SKILL.md` before requesting
such a file from a clerk or archive.

Search every county where either spouse lived, not only the couple's home. A divorce was usually filed in a local court where one spouse lived or had met the residency requirement, which varied by state, and there is usually no statewide index [S23], [S24]. One party may have moved to another state and filed there [S36]. Start with the counties where each spouse lived and their neighbours [S24]. Search for a suit for separate maintenance or support as well as for a divorce [S22]. The 13 July 1909 Fort Wayne report on Cora Clark's claim against Edwin Clark calls it a suit for support [S37]. Use the stated cause of action when looking it up.

**Find the granting authority and check access.** Use the State Archives guidance for the state and year, following the route from the available excerpt [S105]. Identify the court or legislative series and the repository that lists it. Check the access rule for that record and date before recording a negative. If access is restricted, record that limit in the search log [S95].

For a Maryland divorce whose case papers are restricted, look for the final decree in the Maryland State Archives' county listings and check any separately listed decree series [S95 @2026-11-22].

**Test a filing outside the home state.** Use the out-of-state search from the available excerpt [S105]. When a home-state search fails, compare the grounds and residency terms in force that year and use contemporary travel routes to prioritize reachable courts. For a plausible Dakota Territory filing under its 1871 law, check for a case once the three-month residency period could have been met. Recheck the law when the search extends into or beyond South Dakota's 1908 change [S111].

**Ohio divorce courts.** For a divorce before 1843, search the records of the Supreme Court sitting in the county and check the General Assembly's local acts for legislative divorces. For 1843–1852, search the county Common Pleas chancery records. Use Common Pleas records for later cases and check the county probate court as well for 1894–1911, when some counties had concurrent jurisdiction. For cases from 1914 onward, check the domestic relations court where the county had one [S58]. Skip the modern statewide Supreme Court as a starting point for the early files [S58].

**Ohio county copies.** Use the county, court and year to identify the series. Request the Ohio county case file from the clerk of courts, as the Family Tree Magazine guide suggests [S57 @2026-11-20]. If the clerk transferred the series, check the county archives and the Ohio History Connection's catalog [S58 @2026-11-20].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> An Ohio divorce index query sends a spouse's name and any search filters to Ancestry or Findmypast and can identify a possibly living person in connection with a divorce. Answer the privacy gate in `SKILL.md` before submitting the query to each service.

**Ohio divorce indexes.** Use the commercial indexes as leads, as Family Tree Magazine suggests [S57 @2026-11-20]. Search the Ohio divorce indexes within their date coverage. Use Findmypast for selected years from 1962 to 2011 [S59 @2026-11-20] or Ancestry's Ohio Divorce Abstracts for 1962–1963, 1967–1971 or 1973–2007 [S60 @2026-11-20]. Copy the divorce date, county and any volume number given [S59 @2026-11-20], then follow those details to the county court file. Continue with the county court series if neither index covers the year or the searches return no hit.

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A Maine or Virginia divorce index query sends a spouse's name and any place or date filters to MyHeritage, Ancestry or FamilySearch. Apply the privacy gate in `SKILL.md` before submitting a query to each service.

**Maine divorce returns, 1892–1963.** Search the MyHeritage Maine Divorces index and open the return image [S84 @2026-11-22], [S87 @2026-11-22]. If the index misses, browse Digital Maine's return volumes by year and county [S88 @2026-11-22]. Copy the marriage date, residence, divorce date and place where recorded. Transcribe any stated cause from the return and check it against the court papers. Leave the cause open when the return omits it [S88 @2026-11-22].

**Virginia divorce vital records.** Follow the Ancestry index lead from the available excerpt [S105 @2026-11-22] through the Virginia Department of Health Genealogy page. The agency describes open indexed divorce data from 1918 with a 25-year public-access interval [S109 @2026-11-22]. For a second lookup, search FamilySearch's 1918–1988 collection [S110 @2026-11-22]. Use the date and locality shown to find the court's decree. Verify court-file access separately.

**Civil annulments.** Check under annulment in the court or archive holdings for the place and year [S96 @2026-11-22]. For Maryland, open the State Archives' Divorces and Annulments card PDFs by surname range. Search within the PDFs on the user's device for the bride's surname in S1893 (1961–1972) or the groom's surname in S1952 (approximately 1961–1973). Copy the event date and county and use them to locate the county court's record [S97 @2026-11-22], [S98 @2026-11-22].

**Connecticut Superior Court divorce files.** Look for the divorce petitions and related papers described in the chapter reading. Follow the lead from the available excerpt [S61 @2026-11-20] into the Connecticut State Library's Record Group 003, Judicial Records. Use its Divorce Records By County guide to match the county and year to the Superior Court's holdings. Check the general civil case files as well as any separately listed divorce series, since divorce papers can be interfiled [S62 @2026-11-20].

**Connecticut divorce abstracts by county.** Use the two Knox and Ferris *Connecticut Divorces* volumes from the available excerpt to locate a Superior Court filing [S78 @2026-11-21]. Choose by county and year. The New London, Tolland and Windham volume covers New London 1719–1875, Tolland 1787–1910 and Windham 1726–1907 [S79 @2026-11-21]. The other volume covers Litchfield 1752–1922 and Hartford 1740–1849 [S80 @2026-11-21], [S81 @2026-11-21]. Use any application town and date in the abstract to locate the corresponding court file. Check the county's Papers by Subject collection and any separate divorce series listed for those years. For Hartford in 1740–1794, check the Superior Court divorce microfilm [S81 @2026-11-21].

**Read the New London, Tolland and Windham abstract for leads.** Extract the spouses' names, the wife's maiden name if given, the marriage date, hometown and alleged grounds for divorce. Check for children's names or ages, a spouse's later whereabouts, name-change requests and others named in the allegations [S79]. Apply the warning from the available excerpt and leave open whether the couple had children when the abstract omits them [S78]. Check the case papers.

Read the decree's wording. A divorce *a vinculo matrimonii* dissolved the marriage. A divorce *a mensa et thoro*, from bed and board, was a court-ordered separation: the couple stayed married and could not marry anyone else [S26], [S38]. Where a court did not use that term, the same arrangement may appear as a suit for separate maintenance [S26].

Search the land records under both spouses' names as well. A spouse who was still married may have had to give up rights in land before it could be sold, and a deed may state a party's marital status at the sale [S23]. Deed books also hold spousal property settlements and bills of sale for property other than land [S40]. A separation agreement may be recorded there even when it deals only with personal property [S25]. Nathan and Lydia Gray's separation terms, including a mare and a feather bed, were recorded in Caldwell County, Kentucky, Deed Book N, p. 251 (2 September 1847) [S39]. Use [land index recovery](land-index-book-series-recovery.md) for the indexes.

Search for a decree ending the earlier marriage where either spouse could have filed [S24]. A November 1909 Allen County report says Daniel Vermilyea alleged that Ida's marriage to Charles Parker was still in force [S37]. Treat the allegation as a lead to that marriage, a death or a decree. If the search finds none, record the courts, years and indexes checked and leave the outcome open.

Search the divorce files of the person's divorced brothers and sisters too. A divorce file can give the place and date of the marriage, each party's residence, the children's names and affidavits from relatives [S36], and the person you are researching may have testified in a sibling's case [S27]. Take a marriage place or first home found there straight to that place's marriage, land and church records: it can show where the family came from [S27].

**Privacy gate:** <!-- privacy-gate: request --> A remarriage application request can send both applicants' names, marriage date and place, and information about an earlier marriage to the clerk, registrar or archive. Apply the privacy gate in `SKILL.md` before requesting a record that may concern a living person.

**Remarriage application.** Use the later marriage record to request the corresponding license application, following the lead from the available excerpt [S105]. Read how the previous marriage ended and the date given, as on the Wisconsin application [S108]. Use those details and any court named in the papers to search for the earlier decree.

## Request the loose papers as their own series

**Privacy gate:** <!-- privacy-gate: request --> A court-file request can disclose a party's
identity and allegations or family circumstances involving people who may be living. Answer
the privacy gate in `SKILL.md` before sending a request or supporting documents to the court
or archive. A case number can also identify the parties.

**Newspaper court listing.** Copy the printed case number, court and parties into the crosswalk. Andrew Koch suggests tracing the number to the corresponding court records to see whether and how the case ended [S46]. Follow the number to the named court's docket. Use the printed case number in the request if you need the clerk or archive to retrieve the case [S47]. Leave the outcome open until the court record establishes it.

Archives often bring out only the bound minute books. Ask separately for the loose papers or case file: affidavits, subpoenas and other working papers. The county archivist on S5 says these are kept apart from the minute books. Also find out where the court's files were later transferred, whether to a basement, attic, storage facility, microfilm or online images. Do not assume the files stayed at the courthouse. [S2], [S5]

**Virginia chancery files without linked images.** Follow the lead from the available excerpt and check for paper originals even when a film search is empty [S66 @2026-11-21]. Match the county or city and year to the Library of Virginia's Chancery Records Index Availability table. Check the entry's format, index number and any local case number or reel number, and follow the listing to the Library or the circuit court clerk [S74 @2026-11-21], [S75 @2026-11-21]. Check the Library's research-room rules before visiting. Use a legible surrogate where one exists. Submit a separate stack service slip for each original file the Library can serve [S76 @2026-11-21].

When the case concerns a death, ask also for the coroner's inquest. Check for it under the deceased's name and the trial under the accused's. In New Castle County, Delaware, the 16 April 1787 inquest for James Kirk named the witnesses examined. Sarah Kirk's trial papers and her October docket entry have separate locators [S35]. Copy each witness as named and test any family connection independently. Lancaster County, Pennsylvania, notes that witnesses may include relatives [S45].

For recent state/county files, start with the court clerk (called the prothonotary for some
civil courts). For older files, check the state archives' court holdings and transfer guidance
early: many older local-court series have moved there. Transfer dates vary by state and court,
so confirm custody for the named series and years rather than assuming all old files moved.
For transferred federal files, follow the NARA route above; a current federal court may still
hold recent files. [S11]

**Restricted court file.** Check the record's access rule. If it permits partial disclosure, ask the clerk or archive for an available redacted copy [S91 @2026-11-22]. Check which documents were released. Nevada's sealing and redaction rules give an example of a redacted court record replacing the unredacted record in the public file [S93 @2026-11-22].

**Court-ordered name change.** When a name change breaks the paper trail, check for the petition in the county where the person lived [S99 @2026-11-22]. For New York County cases from 1848–1934, request the file through the County Clerk's Archives Department after checking whether it is sealed [S101 @2026-11-22]. From the petition, record the old and proposed names, residence at filing, occupation, any stated marriage and the reason given. Verify the name granted in the order [S100 @2026-11-22].

**Courthouse loss.** Check a record-loss guide for the specific court, series and years. A courthouse fire can leave bound volumes intact while loose papers are lost [S49]. According to Katie Merkley, confirmed destruction is the point to switch to substitute records [S48†]. If the loose file was destroyed, look for the court's actions in surviving order books and for copies of the missing documents among exhibits in other cases [S49], [S50].

## Inventory the file by procedural stage

Read through the last dated filing before closing a case search. A Utah County probate file remained open for 30 years [S10]. Record the opening and closing documents and a locator or gap for each intervening stage. Later papers can answer questions the opening petition leaves unresolved.

**Civil, chancery and divorce cases** [S1]:

- complaint
- summons and return of service, or service by publication in a newspaper (a sign of a default route)
- answers, demurrers, motions to dismiss, counterclaims and third-party claims
- affidavits and depositions
- exhibits
- judgment
- post-trial motions
- satisfaction of judgment
- appeal

**Judicial divorce papers.** Identify the opening complaint, including a bill for divorce, using the terminology from the available excerpt [S105] and the historical pleading [S124]. Look for the answer, any temporary support or custody filings, and the final order [S106]. Record claims in the complaint as allegations. If the answer is missing, leave the other spouse's position open. Follow the docket to the court's disposition even when there is no jury verdict [S107].

**Family details between censuses.** Reconstruct the household from the divorce papers, using the details from the available excerpt [S105]. Record the spouses' full names, any maiden name, the marriage date and place, and the children's names and ages or birth dates. Check the complaint and support or custody papers for these leads [S106]. Treat the filing place as a clue to residence and verify it separately.

**Kinship in chancery estate disputes.** Use the lead from the available excerpt to read the bill, answers and depositions for who calls each claimant an heir or sibling and on what grounds [S66]. Follow the comparison from the available excerpt and trace what each claimant says about property the mother received from her husband and property she held separately [S73]. Test whether the claimants shared both parents or only their mother. Record any finding in the decree separately from the parties' assertions. The reported chancery appeal in *Blunt v. Gee*, 9 Va. 481 (1805), distinguishes siblings of the same mother by whether they shared a father and traces the disputed property by how it passed [S77].

**Read the writ's destination and the officer's return separately.** Under Ohio's 1824 statutes, a sheriff's authority ended at the county line, and process for a defendant elsewhere went to that county's sheriff [S41]. In an 1830-era Virginia estate suit, subpoenas addressed to different county sheriffs supplied leads to heirs' later homes [S28]. Another Virginia summons identified several defendants as living outside the state [S29]. Record where each person was sought and on what date. Record personal service as evidence of presence and a failure to find the person as a result for that locality and date.

**Criminal cases** [S2]:

- investigation
- arrest
- initial appearance and bail, or release on recognizance
- information or grand-jury indictment
- pretrial proceedings
- plea or trial
- acquittal or sentence
- incarceration

Use these points to read the criminal file:

- **For a modern file, expect a plea, not a trial.** Tanner says that in today's practice most cases end in a negotiated plea and very few go to trial. Do not carry that expectation back to older files. Establish plea or trial from the docket or disposition. After a plea, no trial transcript is expected; after an established trial, an absent transcript remains a retrieval gap.
- **Ask for the grand-jury records.** Where the case went by indictment, Tanner says many courts keep the grand-jury records, which can show the evidence presented.
- **Look for the officer in the court file.** Police files often do not survive. The arresting officer usually testified about how, where and why the person was arrested, and that testimony is often preserved in the court case file with the depositions and affidavits.

List each witness, juror and court officer named in a criminal case file or an inquest, and research them as the person's associates: such lists name the people around the event, and inquest witnesses may include family members [S35], [S45]. Record each person's documented role; a name alone establishes neither participation nor a family relationship.

A gap in the inventory is a retrieval gap. It is not evidence that a step never happened.

## Search the newspapers around each court date

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A name search on an online newspaper
site sends a party's name, with the case it concerns, to that service, and a 20th-century party,
witness or child may be living. Answer the privacy gate in `SKILL.md` before entering a possibly
living person's name.

List the date of each significant step in the docket or file, such as the filing, hearings, the judgment or sentence and any appeal, and search the local papers around each date [S32]. Search the paper published at the county seat as well as papers near the person's home [S34]. Look for the term's list of cases, short reports of what happened, legal notices the law required, and fuller articles on cases of local interest, which can hold details the court record lacks [S34], [S43]. Browse the issues around each date by hand as well, because OCR errors make keyword searches miss names [S32], [S44]. Expect a fuller article only for a case that was local news [S34]: its absence says little, while a missing term list or required notice means searching another paper or issue. For legal notices and the handoff from a notice back to the court, use [newspaper search recovery](newspapers-com-search-recovery.md).

When the file is missing or closed, run the same search from the dates you know, including the filing, hearing and judgment [S31]. Compare a newspaper's words with the docket before assigning an outcome. On 17 January 1909, Fort Wayne reports described Genevieve Needham's complaint as withdrawn from the files and Emma Finney's suit as dismissed [S37]. A filing report may be the only surviving lead, and its marriage date or place still needs checking in a marriage record [S33].

**Indiana divorce notice to a nonresident spouse.** Use the newspaper route from the available excerpt [S105]. For a proceeding under Indiana's 1852 revision, search the filing county's newspapers for notice of the pending suit and check the case papers for an affidavit of nonresidence and proof of publication. In *Green v. Green*, 7 Ind. 113 (1855), the court upheld notice by publication although no summons had issued [S107].

## Bound the published case-law search

- **Search by name with a stated scope.** Use a published case-law search, such as Google Scholar's case-law option, nationwide or limited to chosen courts. It is full-text, so counsel can also be found by name. Google Scholar's help page gives its coverage as U.S. Supreme Court opinions from 1791, lower federal opinions from 1923, including district (trial), appellate, tax and bankruptcy courts, and state appellate and supreme court opinions from 1950. It does not cover state trial or probate court files. Log the courts and date range you searched. [S2], [S3], [S4]
- **Read a no-hit narrowly.** It says nothing about state trial-court involvement, and little about state cases decided before 1950. Courts not of record do not publish their decisions, so search their surviving dockets, indices, minute books and case papers separately. [S1]
- **Follow a hit back to the trial court.** Look for the lower-court file and the testimony transcript, which Tanner says may give relationships and motives that the opinion leaves out. Record people named in the opinion who were not parties as separate leads. [S3]
- **Keep the appellate record and the original file apart.** If the trial file is lost, the appellate record and opinion may be what survives. Label them as the appellate record. Do not treat an opinion's summary of facts as the trial record. [S1]

Run the name through CourtListener as a second published-case search, pinned to the family's place with a proximity query. CourtListener documents a quoted phrase followed by `~N` as finding the phrase's words within N words of each other, so `"Whitwell Perry Tennessee"~10` finds the surname near both place names; a tilde after a single word is a fuzzy spelling search that accepts only 1 or 2 [S19 @2026-11-12]. Use that documented quoted form, not a parenthesised group followed by `~10`. Keep other states in scope. A search for Whitwell and Perry County, Tennessee, led to *Jackson v. Grissom*, 196 Mo. 624 (1906), in the Missouri Reports. Use the reporter, volume and page to retrieve the opinion even when the ancestor is absent from its title [S20 @2026-11-12].

**Privacy gate:** <!-- privacy-gate: third-party-tool --> A MyHeritage case-law index query sends a party's name and any decision-date filters to MyHeritage. Apply the privacy gate in `SKILL.md` before submitting the query.

**U.S. published decisions from state and federal courts.** Search MyHeritage's United States, Index of Court Cases, 1833–2018 for a property or probate case by party name [S102 @2026-11-22], [S103 @2026-11-22]. Scope a negative to published decisions in the Caselaw Access Project data [S104 @2026-11-22]. Copy the court, decision date, docket number and volume pages where given. Read the opinion for stated heirs and relationships and follow the locator to the trial file to test them.

## Set the window and close with a case register

Search across the person's whole adult life and decades past death. Tanner warns that suits involving an estate can come 10–20 years later or more. [S1]

Return:

- a case register: court, caption, party roles, case number and proceeding type
- the pointer-to-file crosswalk
- the stage inventory, with a locator or gap for each document
- a separately labelled appellate or opinion row
- non-party name leads
- a search log of the courts, indexes, years and custodians actually searched, each with its bounded negative

Route identity and conclusions to [evidence/proof judgment](evidence-proof-judgment.md). For newspaper notices, use [newspaper search recovery](newspapers-com-search-recovery.md).
