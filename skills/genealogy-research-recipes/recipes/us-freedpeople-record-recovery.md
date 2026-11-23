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
router: {"section": "Records by country and region", "group": "United States: people, vital and church records", "order": 172}
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

Use the 1870 federal population schedule to anchor a named household after emancipation. When earlier freedom is plausible, search the 1790–1840 federal schedules for the free Black household head. Use other members’ tallies to guide the household search and look for records that name them [S114], [S133].

- **Check before assuming.** Before moving to enslaver-side records, look for the household as free people of color in the 1850 and 1860 population schedules, which name free people of color. The slave schedules, by contrast, list enslaved people mostly by age, sex and color under the slaveholder's name. If the free-household search fails, move to enslaver-side records [S17], [S10]. A free household found in 1850 or 1860 shows freedom at that census date only. Record it with that date, and if the family could have been enslaved earlier, still search for the will, deed, purchase or manumission that freed them [S2]. Make a status table with three values (free, enslaved, unknown), each with its evidence and date. A failed name search sets the status to "unknown", not "enslaved".
- **Date the status evidence.** Compare the date the will was written with the date emancipation took effect locally. A Texas will bequeathing Mariah and her son Bob in April 1864 reached probate in September 1865, after emancipation, without specifying their status at probate [S26]. Enter the bequest at the writing date.
- **Free people of color in court records.** Search available court minutes and registration books for the phrase “free man of color” and related terms. The 1863 court terms for Richmond County, Georgia, are a lead for registrations [S2]. Transcribe abbreviations such as FPC, FMC and FWC literally [S5].
- **Pennsylvania.** Living in Pennsylvania after the 1780 Gradual Abolition Act does not mean a person was free. The act ended slavery gradually, not at once [S21], [S23]:
  - People already enslaved when the act passed stayed enslaved for life, provided their enslavers registered them by 1 November 1780. Unregistered people were freed. Look for the 1780 slave register in the county.
  - Children born afterward to enslaved mothers were held as servants until age 28 (not for a 28-year term counted from some later date).
  - Registering each such child's birth comes from the amending act of 29 March 1788, not the 1780 act. The holder had to deliver the child's name, sex and age as best known, in writing, to the county clerk of the peace within six months of birth. Search county birth returns from 1788 onward. In Chester County these are the "Negro Servant Returns", 1788–1821.
  - Because of the age-28 term, people enslaved for life and term servants can turn up in the same households for decades after 1780.

- **New Jersey "apprentices for life".** On the 1860 New Jersey census, read this term as a person still held under the state's 1846 act, not as a free trade apprentice [S49], [S50]. Those still held were freed by the Thirteenth Amendment in 1865, but a master or mistress could discharge an apprentice earlier by written certificate, so do not assume that someone listed in 1860 stayed in bondage until 1865 [S50]. The official 1860 total was 18, yet a page-by-page study found 64 names connected to slavery in the regular population schedules [S51]. Search the population pages and inspect each entry’s own status wording.

- **Do not infer freedom from a Northern residence.** The 1840 U.S. census still reported enslaved residents in New Hampshire (1), Rhode Island (5), Connecticut (17, not counting 37 Amistad captives), New York (4) and New Jersey (674), so living in one of these states around 1840 does not settle status [S52]. Nor does Vermont's 1777 clause show that a person there was free: abolition there was a process, not a single event, and law and practice differed, so look for a record of that person's status [S49], [S53], [S54].

- **Local registrations in gradual-abolition states.** Search for local records naming enslaved people and children bound to service: The Legal Genealogist reports such records in most Northern states that adopted gradual emancipation [S49]. The Pennsylvania registers described below went to the county Clerk of the Peace, or in Philadelphia to the clerk of the court of record [S55]. Elsewhere, search at the level each state used: the county clerk under New Jersey's 1804 act [S56], the city or town clerk under New York's 1799 act [S57], and the town clerk in Connecticut, so in New York and Connecticut look in town rather than county records [S58].

  Search these Pennsylvania sources:
  - the 1780 county slave registers and the post-1788 birth returns described above;
  - the septennial census returns (Pennsylvania State Archives RG-7, 1779–1863), which include enslaved people in a household [S23]. Only about 11% of the returns survive, and many enumerators listed only people enslaved for life, not the term servants born after 1780. A blank entry therefore does not rule out a term servant;
  - the Pennsylvania Abolition Society's "Manumissions and indentures, ca. 1780–1840", held at the Historical Society of Pennsylvania and available as a seven-reel microfilm set. The series is arranged by name of master or slaveholder, so search under the master's name. It also includes records from several other eastern states, not only Pennsylvania [S22], [S24];
  - county manumission records. The presenter points to an index found by searching "manumissions" at chesco.org and credits it to the Chester County Historical Society [S22], [S24]. chesco.org is actually the site of Chester County Archives and Records Services, the county government's archive. The Historical Society is a separate private organization. The county archive lists slave manumissions among its holdings and posts online indexes to the 1780 Slave Register and the Negro Servant Returns. Confirm which index you are using, and cite the county archive as its custodian.
- **Other gradual-abolition states.** In other Northern states that abolished slavery gradually, a person born before the act's cutoff date was not freed by the act. Connecticut's 1784 act, for example, covered only people born after 1 March 1784 and did not free their parents [S27].
  - For a person born on or before the cutoff, look for separate evidence of manumission and check the later 1848 abolition act [S27].
  - Check an estimated census age against the town birth record. The Woodstock entry placed Gin’s birth ten months before the cutoff, and an 1845 will described her as having passed to the heirs [S27].
  - Do not assume that "servant" in these states' wills means hired help: a "servant" left to the testator's heirs can be a person held as property [S27]. A support duty split among heirs is not proof on its own, since Connecticut also made former owners' heirs liable for supporting people they had freed. Compare the birth date, the census status columns, the terms of the applicable act and any later evidence of freedom.

  "Held for life" means only that the state's first act did not free the person; a later act could. New York's 1799 act did not free people born before 4 July 1799, and legislation enacted in 1817 freed the remaining enslaved people in 1827 [S57]. Before ruling on a person's status at a date after the first act, look for a later act in that state.

- **A free woman heading an 1850 or 1860 household.** When a free woman of color heads a household with a growing number of children and no husband listed, keep an enslaved husband as one hypothesis. The FamilyTreeDNA guide reports that marriages between free and enslaved people, not uncommon in the Upper South, could not be formalized, and that the free-born children of an enslaved father carried their free mother's maiden name [S59]. Enslaved people could not legally marry [S64], and a child's status followed the mother's: Virginia's 1662 act held children "bond or free only according to the condition of the mother" [S63]. Search the children under the mother's surname as well as under any surname a father used. Widowhood, separation and an unmarried mother fit the same household, so keep the enslaved-husband reading open until a record names him. The same guide reports that such couples often registered in the 1866 cohabitation registers described in §2 [S59].

According to the Just Genealogy livestream excerpt, Dorothy Provine’s register abstracts are a starting point for free-status research in Alexandria County and Washington, DC [S99†]. Search the Alexandria County volume for 1797–1861 and the District of Columbia volumes for 1821–1861. When logging a miss for the District, account for the gap between the volume ending in 1846 and the one beginning in 1855 [S100], [S101].

For Boston, look in the Overseers of the Poor’s almshouse records for entries that describe a person as enslaved or formerly enslaved. Record the status the entry states and leave it open when the entry gives only an admission [S94], [S96].

Search period vocabulary as well as modern subject terms. In North Carolina material, the UNC Greensboro exhibit identifies terms such as absconding, truancy, eloping and running away. Combine the terms actually used by the local records with place and date; do not expect a contemporary heading to use a modern research label. [S73], [S74]

According to Just Genealogy, Paul Heinegg’s *Free African Americans of North Carolina, Virginia, and South Carolina, From the Colonial Period to About 1820*, sixth edition, is a starting point for early free families [S123†]. Use the full-name index in each volume and follow the family entry to the tax, court, church or other record it cites. Check what that record establishes about status and kinship [S130].

According to Lindsay Fulton, the 10 Million Names census map can help compare the distribution of free and enslaved populations [S115† @2026-11-21], [S121 @2026-11-21]. Use it to compare candidate localities. Determine individual status from records about the person.

## 2. Look for a document that names the enslaver

Look for a record that names the enslaver before you guess one from a surname.

- **Find out how freedom came.** Possible routes include [S9]:
  - USCT service, with pension files claimed by widows, children or even parents;
  - self-emancipation;
  - flight to a contraband camp. Camp histories turn up in local history sources; a census will not show them;
  - wartime employment.
- **USCT testimony and questionnaires.** Look for questions naming former enslavers, including who held the soldier at enlistment. Record the answer, speaker, document type when known and file locator. The surviving question in one demonstration did not identify the form [S14]. Keep same-surname enslavers separate until another record identifies the person.
- **Later records of the children.** Look for family biographical forms in a child’s World War I Gold Star file. Extract any named former enslaver, occupation, county of enslavement and postwar destination [S28]. Attribute the account to its informant and test those leads in earlier records.
- **A woman's maiden name.** Identify the men in her life first: husband, father and brothers. Then search the Civil War pension file of any of them who served, or of another member of her community, and the Freedmen's Bureau marriage records [S29]. These can give her maiden name.
- **Freedmen's Bureau field-office records.** The Bureau operated from 1865 to 1872, and its records are in National Archives Record Group 105 [S1]. Field-office records include rations and labor contracts [S17]. Check who signed the contract and copy any stated relationship: a mother’s signed identification of her children can distinguish them from other people in the same 1870 household [S11]. Search the field office covering the person's home, and also the office in the nearest larger town, because people sometimes travelled there to file [S20].
- **Locate the Bureau series.** The field-office publications are M1900–M1913, one for each state or district, with Florida in M1869 [S43], [S104], [S105]. The Washington headquarters marriage records for 1861–1869 are M1875 [S103]. Use the collection for the relevant office [S44]. Check which pages the Smithsonian project transcribed before relying on its text search [S46].

  FamilySearch offers Alabama’s M1900 field-office images for browsing [S45 @2026-11-19].

**Browse Bureau correspondence by office and date.** According to Shelley Viola Murphy, follow a name search with a browse of the letters for other people in the community [S106†]. Use the office’s roll list to define the series and dates, then log the image range you read. Check the registers of letters received for correspondents, places of origin and entry numbers that lead to the letters [S107].

**Relatives separated by sale.** Start with the “Letters Sent” at the office where the applicant sought help, and check transportation requests and endorsements as well. Extract the requester’s account of kinship, the relatives’ names and the reported destination. Use the destination to find the receiving office’s correspondence or a reply, and log the request separately from any evidence of reunion [S107], [S108].

**Complaints and hearings.** For disputes over pay or reports of violence, check the office’s complaint register, letters received and proceedings or docket of the Freedmen’s Court, where they survive. Record the parties, locations and allegations from the complaint, then look for a separate disposition. Check the roll description for dockets filed within another series. The Charlottesville register of complaints, M1913 roll 67, also contains a court docket [S107], [S109].

**Ration applications and registers.** Read both the application and the issue register. Record the applicant, any named household members and their ages, and the place or landowner if given [S107]. Include white relief recipients in an office search when the series covers them. At Selma, Alabama, check both recipient categories in the ration register for freedpeople and destitute white people, M1900 roll 31, volume 182 [S104]. Keep the register’s labels as recorded and test each person’s earlier status separately.

**Military claims for U.S. Colored Troops.** In RG 105, look for bounty, back pay or pension claims and claimant registers. Copy the company, regiment, claimant and any stated relationship, then compare with the compiled service record in RG 94 and the pension file. If the claim continued after the Bureau closed, check the Freedmen’s Branch field-office records, M2029, 1872–1878 [S107], [S110].

- **Cover the Bureau before calling a search negative.** The home town may have had no field office, and one agent could cover several counties. Find the offices near the home on a map, or on the Mapping the Freedmen's Bureau site, and search each one whose district may have included the home [S30]. Field offices are not the whole Bureau: also search the Headquarters, state Assistant Commissioner and state Superintendent of Education records [S30]. Transcription coverage differs by office. Where a series is not transcribed, browse its images, including the agent's "Letters Sent" [S30]. Record each office and series in the coverage log.
- **Cite the Bureau item.** Record the collection, office, series, NARA publication and roll, page and letter number, together with the range searched. If a finding aid omits roll numbers, match the item’s title and position to NARA’s descriptive pamphlet. The Smithsonian’s Tennessee finding aid preserved the NARA sequence while omitting its roll numbers [S30].
- **Freedman's Bank registers.** The Freedman's Savings and Trust Company opened about 37 branches in 17 states and the District of Columbia. The surviving signature registers of only 29 branches, 1865–1874, are NARA M816 [S39], 27 rolls in Record Group 101 [S47]. What each branch asked varied, but entries can name parents, brothers and sisters, spouse and children, and sometimes a former owner [S39]. The NARA indexes (M817) lack many account numbers, sometimes give numbers that differ from the registers, and leave out some depositors who appear in the registers, so read the register images themselves [S39]. A miss counts only for a surviving branch near the person, within its years. Record which branches you read.

  FamilySearch provides a name index and images of the surviving branch registers [S48 @2026-11-19].

- **Information Wanted ads.** Search Last Seen: Finding Family After Slavery (informationwanted.org). It collects newspaper ads, mostly 1865–1922, placed by formerly enslaved people looking for relatives separated by sale [S40]. Search the places and both the relatives’ and former enslavers’ names. Record each ad as the advertiser's own account, with the newspaper and issue date.

  Last Seen’s advanced search provides keyword and location searches. Enter an enslaver’s name as a keyword because the form has no dedicated enslaver field [S41 @2026-11-19].

- **Enslaved.org.** It links person-level data from many contributed datasets and projects [S42]. Follow each hit to its contributing dataset and that dataset's original source, and cite those, not the hub.
- **Postwar labor contracts.** Record the employer and other workers in labor or sharecropping agreements. If the employer shares a freedperson’s surname, trace that employer’s land and family records in the county [S31]. The employment relationship gives a candidate to investigate. Seek an earlier record identifying an enslaving relationship.
- **Apprenticeship records.** Inspect county court minutes and bonds in the years after a child first appears in another household. A Tennessee bond dated 2 March 1874 named the mother and her current husband for a child living with the future master in 1870 [S32]. Record the census observation and legal placement separately, with the boy’s age and the wording of the bond.
- **Southern Claims Commission files.** Search by county, not by surname. Read the testimony in allowed claims and also in disallowed and barred claims (NARA M1407). Look for digitized copies in the Ancestry and Fold3 catalogues. Formerly enslaved witnesses in someone else's claim may name their owner [S20].
- **Fugitive Slave Act cases (post-1850).** The 1850 act used federal commissioners and U.S. marshals to return fugitives, so it created federal paperwork: a petition, an ownership affidavit and witness testimony. Search under the claimant slaveholder's name [S8].

Read the Bureau labor contract for wording that explicitly identifies a former enslaver, such as “former slave of,” and copy the statement with its locator. Keep a named employer as a candidate while the prior relationship is unverified. Clause 12 of Penick’s 1865 contract allowed replacement hires under the same terms, so being covered by the agreement establishes the employment link alone [S112].

- **Cohabitation registers of 1866.** Search the registers made when Virginia and North Carolina legalized the unions of formerly enslaved couples in 1866 [S64], [S65]. Virginia's registers of colored persons cohabiting together as husband and wife on 27 February 1866 usually name former enslavers, residences and birthplaces, and a separate register lists children whose parents had ceased to cohabit [S64]. North Carolina's cohabitation bonds, filed with the county register of deeds under the March 1866 act, typically give the man's and the woman's names and ages and how long they had been married; some counties add the enslaver or the number of children [S65]. The FamilyTreeDNA guide uses these records to find a wife's maiden surname, and treats couples who registered on the same day as possibly related or enslaved in the same household [S60]. A RootsTech 2025 session description also pairs them with probate, Freedmen's Bureau records and DNA for the years before 1870 [S61].

**Bureau marriage records.** Record the date of ceremony or registration and the earlier start or stated duration of cohabitation in separate fields. Read the whole certificate or register entry, including remarks, for children of the current union and any previous unions of either spouse. Copy any details stated about former spouses, why a union ended and which children survived. Assign children or child counts to a union only where the entry identifies it [S103], [S107], [S113].

In Virginia cohabitation registers with separate last-owner columns, copy the name and locality for each spouse independently. If the federal marriage entry gives only the couple, check the locality’s cohabitation register as well as the Bureau field-office series. Search Goochland’s 1866 Register of Marriages in M1913, roll 89, volume 236, under the initial of the husband’s surname [S109], [S111].

- **Virginia death registers, 1853–1865.** Read the county or city register’s date, place and enslaver columns for a death before emancipation [S68]. Where the place describes a plantation, trace the named enslaver in tax and land records to locate it [S62]. Check which years survive. Even a surviving register can omit a death, so a missing entry cannot establish that the person was still alive [S62].

  The Library of Virginia reports no statewide index to the 1853–1896 death registers, only indexes that some county clerks made, so look for a county index or read the register [S68 @2026-11-12].

Read the expense clauses in a sharecropping agreement alongside the promised fraction. Record which costs come out before division when the agreement specifies deductions, and leave the actual payout open until an accounting or receipt shows it [S89], [S92]. Check what labor the agreement assigns to each household member, including domestic work, even when only one person is named as the farmer [S89], [S92], [S93].

- **Crop liens and chattel mortgages.** After 1865, search the county's recorded crop liens, chattel mortgages and trust deeds for a freedman who farmed as a sharecropper or tenant. A lien can place him on a named landlord's farm in a given year [S71]. In Tennessee, look in books titled Deeds of Trust or Trust Deeds; elsewhere the books are often titled Crop Liens [S71]. The FamilyTreeDNA guide reports that farmers who signed one lien together shared the risk and were typically a parent and an adult son or son-in-law, or siblings and brothers-in-law [S59]. Record a co-signer as a candidate relative until a record states the relationship.

  The same guide reports that most of FamilySearch's crop liens and chattel mortgages are not indexed but can be reached through Full Text Search [S59 @2026-11-12].

Search American Ancestors’ 10 Million Names databases for people enslaved in what became the United States. Include the collections about free and freed people and their communities when tracing a person across emancipation [S94 @2026-11-18], [S95 @2026-11-18].

According to Lindsay Fulton, the flagship pages are a way to identify relevant collections and check whether they can be searched [S115† @2026-11-21]. Open 10 Million Names’ Five Flagships page, choose the theme that fits the question and check its Completed and Upcoming database lists before logging search coverage [S116 @2026-11-21], [S117 @2026-11-21], [S118 @2026-11-21]. For freedom suits, Underground Railroad testimony and mariners, start with Journeys to Liberation. For New Bedford, check the coastal-town biographical entries and the offshore whaling crew and voyage lists [S117 @2026-11-21].

Use the project search for broad coverage and open the individual database when the ancestor’s historical place points to a specific collection [S119 @2026-11-21]. According to Lindsay Fulton, a given-name search is useful for records of enslavement [S115† @2026-11-21]. When the form permits it, leave the surname blank and narrow by the known historical place.

For a promising 10 Million Names hit, check the collection description for a named contributor. Use the contributor’s own site for the historical context and related records. For example, the project credits the Newport Historical Society for its Newport database, and the society describes the primary sources it used [S94 @2026-11-18], [S97 @2026-11-18], [S98 @2026-11-18].

For someone who escaped enslavement, search contemporary newspaper reward advertisements placed by enslavers, including issues from before 1850. Use terms such as “ran away” and “reward” with the person’s name or the place [S87], [S88].

A flight advertisement records an enslaver seeking someone; it does not establish where that person went. Include southern towns, wilderness refuges and Native communities among routes to test rather than assuming every escape went north. Surviving reports often reflect discovery or suppression, so an undiscovered refuge can leave little official documentation; preserve the destination as unknown unless evidence identifies it. [S75], [S76], [S77]

For Confederate forced labour, inspect the RG 109 Confederate Quartermaster and Corps of Engineer payrolls through the National Archives catalogue and its available indexes. Extract the labourer, enslaver, occupation, work period and payee as separate roles. NARA describes postwar arrangement and indexing, so do not label the entire series unindexed or mistake a later compilation date for the labour date. Some payrolls include free Black or white employees; determine each person’s status from the entry rather than the series title. [S78], [S79]

## 3. Generate and eliminate candidate enslavers

- **Collect candidates.** Draw them from the 1870 household (older generations living there), neighbors, shared given names between Black and white families, slave schedules and county slaveholder lists [S10], [S13]. Include the children’s middle names when generating surname leads, then test each candidate in ownership records [S18].
- **Locate the voter before selecting counties.** Check the 1867 registration or oath book when one survives. Washington McGriff’s recorded birthplace and later tax records pointed to Thomas County, but his 1867 voter oath was in Decatur County, Georgia, election district 8, no. 37, p. 318 [S33]. Include both counties in the candidate search.
- **Rank by schedule entries.** For a surname shared by several owners, compare each owner's 1850/1860 slave-schedule entries. Look for an enslaved person of the expected age and sex, and investigate the owners with a fit first [S18]. An owner with no fitting entry moves down the ranking but is not excluded: schedule ages may be estimates, so keep the mismatch unresolved unless independent evidence excludes that owner. Record the mismatch and its year in the candidate register.
- **Keep the surname as a set of hypotheses.** Possible explanations:
  - the last enslaver;
  - an earlier, first, favorite or longest enslaver [S25];
  - a parent's or grandparent's enslaver [S25];
  - a surname the person carried from owner to owner [S25];
  - no connection at all.

  Compare the surname with earlier holders as well as the last one. In a Liberty County example the adopted surname led back to an earlier enslaver [S12].

- **Do not read "Mulatto" as a sign of an enslaver father.** The 1870 and 1880 enumerator instructions call the word generic: it includes quadroons, octoroons and all persons having "any perceptible trace of African blood" [S66], [S67]. The entry therefore says nothing about how recent the white ancestry was, and the FamilyTreeDNA guide warns that it does not imply the person was the child of an enslaver [S59]. Do not add a candidate enslaver to the register on the strength of the color entry.

Date a slave-schedule association to the census year and leave earlier ownership open. In 1850, the instructions treated the person for whom the enslaved person was found working as the owner. The 1860 instructions called for identifying the actual proprietor and the employer separately when someone returned people owned by others. Extract those roles as written and verify ownership in a separate record [S89], [S90], [S91].

## 4. Follow the personal-property chain, not land

Enslaved people appear in records of the enslaver's personal property: sale notices, business records and probate [S1]. For each candidate in the register, best fits first:

- **Get the full probate file**, not just the will: inventory, appraisals, accountings and distributions [S10], [S2], and the estate sale record. An estate settled without a will can hold the same papers, and its sale record can name the buyers [S34]. An enslaved person sold at the estate sale passed to the buyer, so follow the buyer as well as the heirs. Then retrieve the later wills of heirs, widows and administrators.
- **Retrieve the other property records:** deeds of sale or gift, mortgages and plantation papers [S15], [S16].
- **Search civil suits over a sale.** Search buyer and seller in the court files and inspect the depositions. In a 1715 Suffolk County suit, the buyer identified the boy, his age, the ship and the island from which he had been brought, and the ship’s captain gave separate testimony [S35]. Record which witness supplied each detail.
- **Read the enslaver family's published genealogies and memoirs.** They can name enslaved people whom the early federal censuses only count. Take each name to vital, census and probate records, and treat the writer's guesses about a person's origin or kin as hypotheses [S27].
- **Follow the chain through purchase, marriage and inheritance.** Work backward from the inventory through mortgages, appraisals, sales and wills [S15]. Record each named person, place, date and party before comparing the next transaction.

  A will and appraisal can list similar names in different generations. In the El Destino research, a proposed link from Amy in an 1820 appraisal to Amy in a 1786 will remained a hypothesis [S15].
- **Search every place the enslaver lived.** Trace the candidate's own moves and search bills of sale and probate in every county and state where he lived. Enslaved people could reach him by bequest from a relative in another state, or move to another state with a widow after her husband's death [S18].
- **Full Text Search.** Put the enslaver's name in quotes in the name field. Add the given name and status keywords using the + prefix for required terms, then filter by place. Quoted phrases, + for required terms and place filters are documented tool behavior. The presenter's grouped form +(negro slave), which she says matches either word, comes only from her demonstration [S2]. Test it, and if it fails, run separate +negro and +slave searches. Also try +emancipate [S2].
  - Also search under the plantation, overseer and executor names [S3], [S6].
  - AI transcripts can drop commas between names, so read the original image [S6].
  - Re-run the searches every week or two, because processed coverage keeps growing [S3].

When a purchase names an estate as the seller, pull that estate’s probate file under the decedent’s name. Check its inventory and distributions for the person and any relatives named there. Follow the seller’s file even when a buyer purchased from an in-law’s estate [S84], [S85].

For antebellum estate and private sale records, start at the county level under the candidate enslaver or decedent. Check state and local catalogues for probate, court order and deed books. The National Archives holds federal records, so a miss there leaves the local search open [S114 @2026-11-21], [S85 @2026-11-21].

According to Lindsay Fulton, an unnamed estate entry gives a lead to other records of the same holder [S115†]. Search under that holder in personal-property tax lists, deeds and family papers in university special collections. Compare the tax counts and look for names in transactions, account books and other papers tied to the holder [S122], [S92].

- **Search heirs’ chancery suits.** Inspect the pleadings, exhibits and disposition when an inventory or will omits a person, including children born after the will was written. William Kee’s heirs disputed who inherited Tissa but agreed that she was Hannah’s daughter [S59]. Record what the parties agreed on separately from what they contested. Search the county equity court and any state appeal. Virginia chancery exhibits can give names, ages and relationships [S72]. To locate the file, use [court case file recovery](court-case-file-recovery.md).

## 5. Build a per-document register of named enslaved people

Make one row per person per document with these fields:

- date;
- document and locator;
- holder and recipient;
- literal name and descriptor (age, size, color term);
- alternative readings;
- grouping type.

Rules for reading the register:

- **Same name in one document.** Create distinct rows for same-name entries and seek a later accounting that supplies ages or relationships. An 1857 inventory listed two Elijahs whom a later accounting distinguished as father and son, aged 43 and 22 [S2].
- **Names across documents.** Link variants such as Jim/James or Nan/Fanny/Nanny only as candidates [S25]. An exact same-spelling match is a candidate too: several enslaved people in one area could share a name [S36]. A link to the same holder or household [S36], or a repeated distinctive descriptor within the same family or neighborhood [S25], strengthens it.
- **Descriptors across documents.** Record descriptions and appraised values with their dates. Appraisals can vary with age, health and skills. Similar prices provide little identification on their own. A vital entry describing a woman named Pegge as “negro” did not settle whether she was the “Indian girl” in an earlier inventory [S36]. Test the holder, date and household against independent evidence.
- **Unnamed entries.** Record the count, holder, recipient and date on a separate row. A later deed naming Pegge did not establish that she was among eight people recorded without names in the earlier purchase [S36]. Preserve the proposed link as a hypothesis.
- **Grouping type.** Mark a grouping **explicit** when the document states the relationship, even if some members appear only as “her three children” [S2], [S6]. Mark a grouping suggested by sequence **order-inferred** and test it against another record. Appraisal order can put unrelated people together [S15], [S16].
- **Bequests of a woman's increase.** Read "her increase" or "all her issue" in a will as a gift of the enslaved woman's children, not as boilerplate: usually those born later, and those already born too when the clause says so. Record the clause as an explicit grouping of the woman and the children it covers, still unnamed, and look for those children in the legatee's later records. Read every bequest clause in full: wills can name enslaved people in the same sentence as bedding, silverware and livestock, and use the livestock term "increase" for enslaved women's children (sale advertisements also use "breeding") [S37].

- **Age words and values.** Use descriptors and appraised values to bracket an age, not to fix one. "Old" and "young", like "big" and "little", may only tell apart two people with the same name, and do not show that they were related [S59], [S69]. Read "boy" and "girl" by that appraiser's own usage, not as children under ten: one 1843 Maryland appraiser counted "boys" as 17 and under [S69]. Prices were highest for healthy young adult men, then for women of childbearing age, and low for young children and for old or infirm people [S70], [S69]. A low value can therefore mean a child or an old person, so compare values only within one document and beside their descriptors.

In a plantation list with explicit mother–child groups, look for daughters listed elsewhere in the same record as mothers. Record each stated relationship on its own, and keep the link between the two entries tentative until their details agree [S84], [S86].

When an inventory gives ages and sex without names, carry those descriptors and the count into the next search under the same holder. According to Lindsay Fulton, these details can suggest a family group [S115†]. Test the grouping against other records and keep kinship tentative until a record identifies the relationship [S97].

If a pre-emancipation entry names the person and the 1870 census search misses, keep the earlier name and locator in the register. According to Lindsay Fulton, a different name is one possible explanation [S115†]. Search the 1870 census again by given name, approximate age and locality, with the surname open, and leave the link unresolved if the evidence still falls short [S122].

Keep an honorific separate from a relationship. The Natchez Trace history describes aunt and uncle as respectful forms of address for older Black people. A person called Uncle in a narrative is therefore a candidate relative only when other evidence supplies the kinship; copy the wording without manufacturing a parent-sibling connection. [S80], [S81]

For North Carolina emancipation research, search county court records and the State Archives’ Records of Enslaved People collection, PC.1629, alongside Quaker meeting papers. Read the collection guide’s provenance notes: it combines originals and copies, and some selected copies have uncertain provenance. Identify the actual document and originating county or collection before treating a finding-aid entry as a complete county search. [S82], [S83]

According to Just Genealogy, *In Full Force and Virtue: North Carolina Emancipation Records, 1713–1860* is a lead for manumission [S123†]. Search Byrd’s index and use both “emancipation” and “manumission” in the underlying record series. Check whether the document records a petition or a grant of freedom before assigning a status or date [S128], [S131].

According to Just Genealogy, Byrd’s *North Carolina General Assembly Sessions Records: Slaves and Free Persons of Color, 1709–1789* is a starting point for colonial and early state legislative activity [S123† @2026-11-21]. Use its entries to identify the session and look for the petition, bill or other session paper in the State Archives’ North Carolina Digital Collections [S128 @2026-11-21], [S129 @2026-11-21].

## 6. Check segregated series before calling a search negative

- **Registers.** Search the separate colored register, the back of the register and the regular or white register. Clerks differed, and entries in a colored register may not state race [S5].
- **Other separated series.** Check Black churches, separate obituary sections, separate cemeteries or sections, segregated military units and prison records [S4].
- **Catholic registers.** Check how the particular parish or diocese organized its sacramental records. Combined Baltimore registers can put a person’s status in the margin and name an enslaver in the entry [S19]. Read the margins and transcribe each observation separately.

Search for both Black and white names in Byrd and Smith’s North Carolina county volumes. According to the Just Genealogy livestream excerpt, names of white people appear in these sources too [S99†]. The Mecklenburg, Gaston and Union volume has a full name index and a table of civil and criminal cases [S102].

According to Just Genealogy, the county compilations include both stand-alone and combined titles [S123†]. Choose the volume for the historical county. Look under combined titles for Burke, Lincoln and Rowan, for Hyde and Beaufort, for Mecklenburg, Gaston and Union, and for Stokes and Yadkin [S124]. Perquimans, Pasquotank, Iredell and McDowell have separate titles [S124]. Check both Chowan volumes [S125], [S126].

According to Just Genealogy, the case tables are a route to civil and criminal proceedings [S123†]. Use the table as well as the name index in both Chowan volumes and Pasquotank. Check the pertinent petitions, actions and miscellaneous sections, and log a miss against the volume and coverage you actually checked [S125], [S126], [S127].

Keep a coverage log of every series checked.

## 7. Keep narratives and DNA as separate tests

- **WPA narratives.** The Federal Writers' Project interviews (1936–1938) hold more than 2,300 first-person accounts by former slaves. A narrative from the same birthplace or birth year gives locality context. It is not evidence about the ancestor. Note the narratives' limits: memories more than 60 years old, uneven transcription and reduced candor with white interviewers [S7].
- **Handed-down accounts.** A family's account of an enslaved ancestor may not be a first-person narrative. It can be an oral history handed down over generations [S38]. Record its chain of tellers as [family interviews and oral tradition](family-interviews-and-oral-tradition.md) describes, and treat what it says as a hypothesis to test, not as the ancestor's own testimony.
- **DNA.** DNA matches to descendants of a proposed sibling test one hypothesis [S15]. A Y-DNA surname mismatch is another. Neither proves who the enslaver or the father was. Route them to [Y-DNA interpretation](ydna-mtdna-interpretation.md) and [evidence/proof judgment](evidence-proof-judgment.md).

According to Lindsay Fulton, the Remembering Slavery flagship points to Fisk and WPA interviews and other oral histories [S115† @2026-11-21]. Use the page to choose a testimony source, and check the completed list before counting the WPA index as searched [S118 @2026-11-21].

For WPA testimony, go directly to the Library of Congress’s *Born in Slavery* collection and browse by interview state [S120 @2026-11-21], [S132 @2026-11-21]. According to Lindsay Fulton, interviews can supply names, relationships, enslavers and places [S115† @2026-11-21]. Extract each detail with its speaker, volume and page.

## Outputs

Return:

- the status-hypothesis table;
- the candidate-enslaver register with the basis for each candidate, any recorded mismatch and any exclusion with its independent evidence;
- the per-document register of named enslaved people;
- the segregated-series coverage log;
- candidate identity links, each with the record that would settle it.

Leave identity and kinship rulings to the researcher.
