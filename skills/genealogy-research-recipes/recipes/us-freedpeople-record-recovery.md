---
id: "us-freedpeople-record-recovery"
title: "Trace an African American ancestor across the 1870 boundary"
summary: "Trace an African American family back across the 1870 boundary."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "US-FREEDPEOPLE-RECORD-RECOVERY-01", "text": "Surname, enslaver, list order and DNA signals stay separate hypotheses until a record names the person."}]
handoff: []
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "pointer", "group": "Migration and origins", "order": 1113}
---

# Trace an African American ancestor across the 1870 boundary

Use this recipe when an African American family is documented in 1870 or later and the next step is to go back before 1870. It does two jobs. First, it tests whether the family was free or enslaved instead of assuming either. Second, for an enslaved ancestor, it follows a candidate enslaver's personal-property chain. Surname, enslaver, list order and DNA signals stay separate hypotheses until a record names the person.

Overlapping steps live in sibling recipes:

- Changing surnames and family-group comparison across censuses: [census workflows § 9](us-census-practical-workflows.md).
- Full Text Search mechanics and associate searches: [AI for documentary records](ai-for-documentary-records.md) and [FamilySearch workflows § 11](familysearch-practical-record-workflows.md).
- Recovering a whole estate file: [probate case inventory](probate-case-document-inventory.md).
- Identity rulings: [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- What goes wrong
- 1\. Test free versus enslaved status first
- 2\. Look for a document that names the enslaver
- 3\. Generate and eliminate candidate enslavers
- 4\. Follow the personal-property chain, not land
- 5\. Build a per-document register of named enslaved people
- 6\. Check segregated series before calling a search negative
- 7\. Keep narratives and DNA as separate tests
- Outputs

## What goes wrong

An unaided assistant tends to make these mistakes:

- It assumes every Black ancestor before 1870 was enslaved.
- It treats the freedperson's surname as the name of the last enslaver.
- It searches under the ancestor's own name, or in land indexes, or stops at an indexed will.
- It merges same-name inventory entries into one person.
- It reads list adjacency as proven kinship.
- It cites a WPA narrative from the same county as evidence about the ancestor.
- It calls a single register with no hit a negative search.

Each section below blocks one of these mistakes.

## 1. Test free versus enslaved status first

- **Check before assuming.** Before moving to enslaver-side records, look for the household as free people of color in the 1850 and 1860 population schedules, which name free people of color. The slave schedules, by contrast, list enslaved people mostly by age, sex and color under the slaveholder's name. If the free-household search fails, move to enslaver-side records [S17], [S10]. A free household found in 1850 or 1860 shows freedom at that census date only. Record it with that date, and if the family could have been enslaved earlier, still search for the will, deed, purchase or manumission that freed them [S2]. Make a status table with three values (free, enslaved, unknown), each with its evidence and date. A failed name search sets the status to "unknown", not "enslaved".
- **Date status evidence by when the record was written.** Check each enslaver-side record against the date emancipation was enforced in that place. A will proved after that date can still treat people as property and say nothing of their freedom. In one Texas example, a will dated April 1864 bequeathed two enslaved people. It was probated in September 1865, after General Order No. 3 had enforced emancipation in Texas that June, and the probate records have no language on their status [S26]. Enter such a will in the status table at its writing date, not its probate date.
- **Free people of color in court records.** Full Text Search now covers court records, and phrase searches such as "free man of color" return free people of color. One example shown is the court registration of free people of color in Richmond County, Georgia, during the Civil War (for example the 1863 terms) [S2]. Record abbreviations such as FPC, FMC and FWC literally [S5].
- **Pennsylvania.** Living in Pennsylvania after the 1780 Gradual Abolition Act does not mean a person was free. The act ended slavery gradually, not at once [S21], [S23]:
  - People already enslaved when the act passed stayed enslaved for life, provided their enslavers registered them by 1 November 1780. Unregistered people were freed. Look for the 1780 slave register in the county.
  - Children born afterward to enslaved mothers were held as servants until age 28 (not for a 28-year term counted from some later date).
  - Registering each such child's birth comes from the amending act of 29 March 1788, not the 1780 act. The holder had to deliver the child's name, sex and age as best known, in writing, to the county clerk of the peace within six months of birth. Search county birth returns from 1788 onward. In Chester County these are the "Negro Servant Returns", 1788–1821.
  - Because of the age-28 term, people enslaved for life and term servants can turn up in the same households for decades after 1780.

- **New Jersey "apprentices for life".** On the 1860 New Jersey census, read this term as a person still held under the state's 1846 act, not as a free trade apprentice [S49], [S50]. Those still held were freed by the Thirteenth Amendment in 1865, but a master or mistress could discharge an apprentice earlier by written certificate, so do not assume that someone listed in 1860 stayed in bondage until 1865 [S50]. Official statistics listed 18 enslaved people and there was no separate slave schedule, yet a page-by-page review found 64 names tied to slavery, so read the census pages instead of relying on the official count [S51].

- **Do not infer freedom from a Northern residence.** The 1840 U.S. census still reported enslaved residents in New Hampshire (1), Rhode Island (5), Connecticut (17, not counting 37 Amistad captives), New York (4) and New Jersey (674), so living in one of these states around 1840 does not settle status [S52]. Nor does Vermont's 1777 clause show that a person there was free: abolition there was a process, not a single event, and law and practice differed, so look for a record of that person's status [S49], [S53], [S54].

- **Local registrations in gradual-abolition states.** Search for local records naming enslaved people and children bound to service: The Legal Genealogist reports such records in most Northern states that adopted gradual emancipation [S49]. The Pennsylvania registers described below went to the county Clerk of the Peace, or in Philadelphia to the clerk of the court of record [S55]. Elsewhere, search at the level each state used: the county clerk under New Jersey's 1804 act [S56], the city or town clerk under New York's 1799 act [S57], and the town clerk in Connecticut, so in New York and Connecticut look in town rather than county records [S58].

  Search these Pennsylvania sources:
  - the 1780 county slave registers and the post-1788 birth returns described above;
  - the septennial census returns (Pennsylvania State Archives RG-7, 1779–1863), which include enslaved people in a household [S23]. Only about 11% of the returns survive, and many enumerators listed only people enslaved for life, not the term servants born after 1780. A blank entry therefore does not rule out a term servant;
  - the Pennsylvania Abolition Society's "Manumissions and indentures, ca. 1780–1840", held at the Historical Society of Pennsylvania and available as a seven-reel microfilm set. The series is arranged by name of master or slaveholder, so search under the master's name. It also includes records from several other eastern states, not only Pennsylvania [S22], [S24];
  - county manumission records. The presenter points to an index found by searching "manumissions" at chesco.org and credits it to the Chester County Historical Society [S22], [S24]. chesco.org is actually the site of Chester County Archives and Records Services, the county government's archive. The Historical Society is a separate private organization. The county archive lists slave manumissions among its holdings and posts online indexes to the 1780 Slave Register and the Negro Servant Returns. Confirm which index you are using, and cite the county archive as its custodian.
- **Other gradual-abolition states.** In other Northern states that abolished slavery gradually, a person born before the act's cutoff date was not freed by the act. Connecticut's 1784 act, for example, covered only people born after 1 March 1784 and did not free their parents [S27].
  - Living in Connecticut before 1848 does not prove that a person born before 1 March 1784 was free. Slavery there ended officially only in 1848, when an act freed the last people still enslaved, all born before that date; the S27 author counts about six [S27].
  - Compare the person's birth with the state's cutoff. A census age is an estimate, so confirm the birth from a vital record before ruling on status. In the S27 example, the town birth record put a woman ten months before Connecticut's cutoff, so the act did not free her, and an 1845 family will still describes her as "left by my Father to his heirs" [S27].
  - Do not assume that "servant" in these states' wills means hired help: a "servant" left to the testator's heirs can be a person held as property [S27]. A support duty split among heirs is not proof on its own, since Connecticut also made former owners' heirs liable for supporting people they had freed. Decide with the birth date against the act's cutoff and the census status columns: born before the cutoff, the person was held for life; born after it, for a term until the age the act set.

  "Held for life" means only that the state's first act did not free the person; a later act could. New York's 1799 act did not include people born before 4 July 1799, and legislation enacted in 1817 freed the remaining enslaved people in 1827 [S57]. Before ruling on a person's status after the first act, look for a later act in that state.

- **A free woman heading an 1850 or 1860 household.** When a free woman of color heads a household with a growing number of children and no husband listed, keep an enslaved husband as one hypothesis. The FamilyTreeDNA guide reports that marriages between free and enslaved people, not uncommon in the Upper South, could not be formalized, and that the free-born children of an enslaved father carried their free mother's maiden name [S59]. Enslaved people could not legally marry [S64], and a child's status followed the mother's: Virginia's 1662 act held children "bond or free only according to the condition of the mother" [S63]. Search the children under the mother's surname as well as under any surname a father used. Widowhood, separation and an unmarried mother fit the same household, so keep the enslaved-husband reading open until a record names him. The same guide reports that such couples often registered in the 1866 cohabitation registers described in §2 [S59].

## 2. Look for a document that names the enslaver

Look for a record that names the enslaver before you guess one from a surname.

- **Find out how freedom came.** Possible routes include [S9]:
  - USCT service, with pension files claimed by widows, children or even parents;
  - self-emancipation;
  - flight to a contraband camp. Camp histories turn up in local history sources; a census will not show them;
  - wartime employment.
- **USCT questionnaires.** In the example shown in S14, a soldier's questionnaire asked him to "state the names of all former owners and particularly the name of your owner at the date of your enlistment". The presenter did not identify the form. Expect other USCT pension files to name former owners in testimony too. Record any enslaver named and the locator. With a common surname, matching same-surname slaveholders in the area can produce several candidates [S14].
- **Later records of the children.** Search the children's twentieth-century records before the antebellum ones, because a family-supplied account can name the enslaver. In one Alabama example, a World War I Gold Star file held a biographical form that named the soldier's father's former owner, the father's work for him, the county where he was enslaved and the family's move after the war [S28]. Record such a statement as the family informant's account, with its date, and test it against enslaver-side records.
- **A woman's maiden name.** Identify the men in her life first: husband, father and brothers. Then search the Civil War pension file of any of them who served, or of another member of her community, and the Freedmen's Bureau marriage records [S29]. These can give her maiden name.
- **Freedmen's Bureau field-office records.** The Bureau operated from 1865 to 1872, and its records are in National Archives Record Group 105 [S1]. Field-office records include rations and labor contracts [S17]. In one contract, a mother calls the people listed her children, which supplied relationships that the 1870 census lacks [S11]. Search the field office covering the person's home, and also the office in the nearest larger town, because people sometimes travelled there to file [S20].
- **Where to read the Bureau records.** The field-office records are NARA microfilm publications M1900–M1913, one for each state or district; Florida's are in M1869. The marriage records of the Washington headquarters, 1861–1869, are M1875 [S43]. NARA gives digital access through FamilySearch [S43]. FamilySearch has 32 Bureau collections, and some, such as Alabama's field-office records, have images but no name index, so browse them [S44], [S45]. The Smithsonian Transcription Center, working with the National Museum of African American History and Culture, has transcribed part of the records [S46].
- **Cover the Bureau before calling a search negative.** The home town may have had no field office, and one agent could cover several counties. Find the offices near the home on a map, or on the Mapping the Freedmen's Bureau site, and search each one whose district may have included the home [S30]. Field offices are not the whole Bureau: also search the Headquarters, state Assistant Commissioner and state Superintendent of Education records [S30]. Transcription coverage differs by office. Where a series is not transcribed, browse its images, including the agent's "Letters Sent" [S30]. Record each office and series in the coverage log.
- **Cite a Bureau item to the NARA film.** Record the collection title, the page number and the letter number, the NARA microfilm publication and roll, and what you searched without finding. The S30 author (2025) found a finding aid on another site that listed the same items in NARA's order but left out the roll numbers. If a finding aid lacks roll numbers, match it item by item to NARA's finding aid to recover the roll [S30].
- **Freedman's Bank registers.** The Freedman's Savings and Trust Company opened about 37 branches in 17 states and the District of Columbia. The surviving signature registers of only 29 branches, 1865–1874, are NARA M816 [S39], 27 rolls in Record Group 101 [S47]. What each branch asked varied, but entries can name parents, brothers and sisters, spouse and children, and sometimes a former owner [S39]. FamilySearch has a name index with the register images [S48]. The NARA indexes (M817) lack many account numbers, sometimes give numbers that differ from the registers, and leave out some depositors who appear in the registers, so read the register images themselves [S39]. A miss counts only for a surviving branch near the person, within its years. Record which branches you read.
- **Information Wanted ads.** Search Last Seen: Finding Family After Slavery (informationwanted.org). It collects newspaper ads, mostly 1865–1922, placed by formerly enslaved people looking for relatives separated by sale [S40]. It has a location search but no enslaver field, so run keyword searches on enslaver names as well as relatives' names, and search the places [S41]. Record each ad as the advertiser's own account, with the newspaper and issue date.
- **Enslaved.org.** It links person-level data from many contributed datasets and projects [S42]. Follow each hit to its contributing dataset and that dataset's original source, and cite those, not the hub.
- **Postwar labor contracts.** Add the employer named in a postwar labor or sharecropping agreement to the candidate register, above all when he shares a freedperson's surname. In one Georgia example, an agreement of about 1867 listed a freedman and several other freedpeople with an employer of the freedman's surname. With a local historical society's help, the agreement led the researchers to land owned by the same-surname family that probably enslaved the freedman [S31]. A contract names an employer, not an owner: keep him a candidate until a record names the person as enslaved by him.
- **Apprenticeship records.** A child of color living in a white household in 1870 may later have been bound to that household by the county court. Search the county court minutes for an apprenticeship indenture or bond, including the years after the census. In the S32 example, an 1874 Tennessee bond formalized a placement that the 1870 census already showed. It named the boy's mother and her current husband, gave his age and called him illegitimate [S32].
- **Southern Claims Commission files.** Search by county, not by surname. Read the testimony in allowed claims and also in disallowed and barred claims (NARA M1407). These files are on Ancestry and Fold3. Formerly enslaved witnesses in someone else's claim may name their owner [S20].
- **Fugitive Slave Act cases (post-1850).** The 1850 act used federal commissioners and U.S. marshals to return fugitives, so it created federal paperwork: a petition, an ownership affidavit and witness testimony. Search under the claimant slaveholder's name [S8].

- **Cohabitation registers of 1866.** Search the registers made when Virginia and North Carolina legalized the unions of formerly enslaved couples in 1866 [S64], [S65]. Virginia's registers of colored persons cohabiting together as husband and wife on 27 February 1866 usually name former enslavers, residences and birthplaces, and a separate register lists children whose parents had ceased to cohabit [S64]. North Carolina's cohabitation bonds, filed with the county register of deeds under the March 1866 act, typically give the man's and the woman's names and ages and how long they had been married; some counties add the enslaver or the number of children [S65]. The FamilyTreeDNA guide uses these records to find a wife's maiden surname, and treats couples who registered on the same day as possibly related or enslaved in the same household [S60]. A RootsTech 2025 session description also pairs them with probate, Freedmen's Bureau records and DNA for the years before 1870 [S61].

- **Virginia death registers, 1853–1865.** For an enslaved person who died in Virginia before emancipation, read the county or city death register: from 1853 its headings include the name of the enslaver, if the deceased was enslaved, and the date and place of death [S68]. In Roberta Estes's Washington County example, the place of death was often a plantation's name or location, and the owner named there can be followed through land and tax records [S62]. Estes suspects that not every enslaved person's death was recorded, so a missing entry does not show that the person was alive [S62].

  The Library of Virginia reports no statewide index to the 1853–1896 death registers, only indexes that some county clerks made, so look for a county index or read the register [S68 @2026-11-12].

- **Crop liens and chattel mortgages.** After 1865, search the county's recorded crop liens, chattel mortgages and trust deeds for a freedman who farmed as a sharecropper or tenant. A lien can place him on a named landlord's farm in a given year [S71]. In Tennessee, look in books titled Deeds of Trust or Trust Deeds; elsewhere the books are often titled Crop Liens [S71]. The FamilyTreeDNA guide reports that farmers who signed one lien together shared the risk and were typically a parent and an adult son or son-in-law, or siblings and brothers-in-law [S59]. Record a co-signer as a candidate relative until a record states the relationship.

  The same guide reports that most of FamilySearch's crop liens and chattel mortgages are not indexed but can be reached through Full Text Search [S59 @2026-11-12].

## 3. Generate and eliminate candidate enslavers

- **Collect candidates.** Draw them from the 1870 household (older generations living there), neighbors, shared given names between Black and white families, slave schedules and county slaveholder lists [S10], [S13]. Read the children's middle names too: in one presenter's family, the parents gave their children the names of both former owners as middle names [S18].
- **Place the man in 1867.** Where the state registered voters in 1867, look for him in those registers, two or three years before the 1870 census. In one Georgia example, the Returns of Qualified Voters and Reconstruction Oath Books, 1867–1869, placed a freedman in Decatur County, election district 8, while his recorded birthplace and his later tax records were in Thomas County [S33]. Draw candidates from the 1867 county as well as the county of the later records.
- **Rank by schedule entries.** For a surname shared by several owners, compare each owner's 1850/1860 slave-schedule entries. Look for an enslaved person of the expected age and sex, and investigate the owners with a fit first [S18]. An owner with no fitting entry moves down the ranking but is not excluded: schedule ages may be estimates, so keep the mismatch unresolved unless independent evidence excludes that owner. Record the mismatch and its year in the candidate register.
- **Keep the surname as a set of hypotheses.** Possible explanations:
  - the last enslaver;
  - an earlier, first, favorite or longest enslaver [S25];
  - a parent's or grandparent's enslaver [S25];
  - a surname the person carried from owner to owner [S25];
  - no connection at all.

  The Liberty County presenter estimates that only about 10% of formerly enslaved people there took their last enslaver's name. In the presenter's example, the adopted surname pointed to a much earlier enslaver of the family [S12]. Treat that figure as a local, attributed estimate, not a rule.

- **Do not read "Mulatto" as a sign of an enslaver father.** The 1870 and 1880 enumerator instructions call the word generic: it includes quadroons, octoroons and all persons having "any perceptible trace of African blood" [S66], [S67]. The entry therefore says nothing about how recent the white ancestry was, and the FamilyTreeDNA guide warns that it does not imply the person was the child of an enslaver [S59]. Do not add a candidate enslaver to the register on the strength of the color entry.

## 4. Follow the personal-property chain, not land

Enslaved people appear in records of the enslaver's personal property: sale notices, business records and probate [S1]. For each candidate in the register, best fits first:

- **Get the full probate file**, not just the will: inventory, appraisals, accountings and distributions [S10], [S2], and the estate sale record. An estate settled without a will can hold the same papers, and its sale record can name the buyers [S34]. An enslaved person sold at the estate sale passed to the buyer, so follow the buyer as well as the heirs. Then retrieve the later wills of heirs, widows and administrators.
- **Retrieve the other property records:** deeds of sale or gift, mortgages and plantation papers [S15], [S16].
- **Search civil suits over a sale.** When a buyer and seller disputed the sale of an enslaved person, the court file can hold depositions about that person. In a 1715 Boston suit in the Suffolk County court files, the buyer's deposition gives the boy's name and age, the island he was brought from and the ship, and the ship's captain also testified about him [S35]. Search the court files under the candidate enslaver's name as buyer or seller.
- **Read the enslaver family's published genealogies and memoirs.** They can name enslaved people whom the early federal censuses only count. Take each name to vital, census and probate records, and treat the writer's guesses about a person's origin or kin as hypotheses [S27].
- **Follow the chain back through purchase, marriage and inheritance.** The presenter's El Destino example works back through:
  1. an 1845 estate inventory;
  2. an 1834 mortgage;
  3. an 1820 probate appraisal;
  4. a 1797 purchase;
  5. a 1786 will.

  The presenter labels much of the resulting tree a hypothesis [S15].
- **Search every place the enslaver lived.** Trace the candidate's own moves and search bills of sale and probate in every county and state where he lived. Enslaved people could reach him by bequest from a relative in another state, or move to another state with a widow after her husband's death [S18].
- **Full Text Search.** Put the enslaver's name in quotes in the name field. Add the given name and status keywords using the + prefix for required terms, then filter by place. Quoted phrases, + for required terms and place filters are documented tool behavior. The presenter's grouped form +(negro slave), which she says matches either word, comes only from her demonstration [S2]. Test it, and if it fails, run separate +negro and +slave searches. Also try +emancipate [S2].
  - Also search under the plantation, overseer and executor names [S3], [S6].
  - AI transcripts can drop commas between names, so read the original image [S6].
  - Re-run the searches every week or two, because processed coverage keeps growing [S3].

- **Search heirs' chancery suits.** When an enslaver's heirs disputed who should inherit an enslaved person, look for the suit in the county court of equity (chancery) and, occasionally, on appeal to a state court [S59]. Such a suit can state relationships that the will and the distribution omit. In the FamilyTreeDNA guide's North Carolina Kee example, the heirs disputed a girl born after the will was written, and agreed that she was the daughter of a named woman [S59]. The Library of Virginia's archives blog reports Virginia chancery causes about dividing enslaved people as part of an estate, whose exhibits give names, ages and family relationships [S72]. To find and inventory the file, use [court case file recovery](court-case-file-recovery.md).

## 5. Build a per-document register of named enslaved people

Make one row per person per document with these fields:

- date;
- document and locator;
- holder and recipient;
- literal name and descriptor (age, size, color term);
- alternative readings;
- grouping type.

Rules for reading the register:

- **Same name in one document.** Same-name entries in a single document stay separate people. In the presenter's example, an 1857 inventory listed two men named Elijah. The later accounting gave ages and family relationships, and it separated Elijah, aged 43, from his son Elijah Jr., aged 22 [S2].
- **Names across documents.** Link variants such as Jim/James or Nan/Fanny/Nanny only as candidates [S25]. An exact same-spelling match is a candidate too: several enslaved people in one area could share a name [S36]. A link to the same holder or household [S36], or a repeated distinctive descriptor within the same family or neighborhood [S25], strengthens it.
- **Descriptors across documents.** Record each person's appraised value with the descriptor. Where names and ages are missing, a value that matches contemporary prices for the same kind of person supports a link; values varied with age, health and skills. A different color or ethnic term does not exclude a link, because one person can be described differently in separate records: in the S36 example, a woman called "negro" in a vital record could not be ruled out as the "Indian girl" of an earlier inventory [S36].
- **Unnamed entries.** Record a count-only entry (for example a purchase of eight enslaved people with no names) as its own row with holder, recipient and date. A later document by the same holder that names people can then be tested against it as a candidate link [S36].
- **Grouping type.** Mark each grouping **explicit** (for example "and her three children" [S2], or "Caesar his wife and his children" [S6]) or **order-inferred** [S15]. A woman listed in a mother-like position is a hypothesis unless the record lists family groups [S16]. List order can also reflect appraisal practice, so do not read adjacency as kinship.
- **Bequests of a woman's increase.** Read "her increase" or "all her issue" in a will as a gift of the enslaved woman's children, not as boilerplate: usually those born later, and those already born too when the clause says so. Record the clause as an explicit grouping of the woman and the children it covers, still unnamed, and look for those children in the legatee's later records. Read every bequest clause in full: wills can name enslaved people in the same sentence as bedding, silverware and livestock, and use the livestock term "increase" for enslaved women's children (sale advertisements also use "breeding") [S37].

- **Age words and values.** Use descriptors and appraised values to bracket an age, not to fix one. "Old" and "young", like "big" and "little", may only tell apart two people with the same name, and do not show that they were related [S59], [S69]. Read "boy" and "girl" by that appraiser's own usage, not as children under ten: one 1843 Maryland appraiser counted "boys" as 17 and under [S69]. Prices were highest for healthy young adult men, then for women of childbearing age, and low for young children and for old or infirm people [S70], [S69]. A low value can therefore mean a child or an old person, so compare values only within one document and beside their descriptors.

## 6. Check segregated series before calling a search negative

- **Registers.** Search the separate colored register, the back of the register and the regular or white register. Clerks differed, and entries in a colored register may not state race [S5].
- **Other separated series.** Check Black churches, separate obituary sections, separate cemeteries or sections, segregated military units and prison records [S4].
- **Catholic registers.** Find out whether the diocese kept separate registers by race or one combined register. The S19 guest reports that, among the dioceses she has worked with, Baltimore alone puts enslaved and free Black people in the regular sacramental registers. She says status such as "free black" appears in the margin and entries sometimes name the owner [S19]. Record margin status and owner as separate observations.

Keep a coverage log of every series checked.

## 7. Keep narratives and DNA as separate tests

- **WPA narratives.** The Federal Writers' Project interviews (1936–1938) hold more than 2,300 first-person accounts by former slaves. A narrative from the same birthplace or birth year gives locality context. It is not evidence about the ancestor. Note the narratives' limits: memories more than 60 years old, uneven transcription and reduced candor with white interviewers [S7].
- **Handed-down accounts.** A family's account of an enslaved ancestor may not be a first-person narrative. It can be an oral history handed down over generations [S38]. Record its chain of tellers as [family interviews and oral tradition](family-interviews-and-oral-tradition.md) describes, and treat what it says as a hypothesis to test, not as the ancestor's own testimony.
- **DNA.** DNA matches to descendants of a proposed sibling test one hypothesis [S15]. A Y-DNA surname mismatch is another. Neither proves who the enslaver or the father was. Route them to [Y-DNA interpretation](ydna-mtdna-interpretation.md) and [evidence/proof judgment](evidence-proof-judgment.md).

## Outputs

Return:

- the status-hypothesis table;
- the candidate-enslaver register with the basis for each candidate, any recorded mismatch and any exclusion with its independent evidence;
- the per-document register of named enslaved people;
- the segregated-series coverage log;
- candidate identity links, each with the record that would settle it.

Leave identity and kinship rulings to the researcher.
