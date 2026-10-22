# Trace an African American ancestor across the 1870 boundary

Use this recipe when an African American family is documented in 1870 or later and the next step is to go back before 1870. It does two jobs. First, it tests whether the family was free or enslaved instead of assuming either. Second, for an enslaved ancestor, it follows a candidate enslaver's personal-property chain. Surname, enslaver, list order and DNA signals stay separate hypotheses until a record names the person.

Overlapping steps live in sibling recipes:

- Changing surnames and family-group comparison across censuses: [census workflows § 9](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/us-census-practical-workflows.md).
- Full Text Search mechanics and associate searches: [AI for documentary records](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/ai-for-documentary-records.md) and [FamilySearch workflows § 11](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/familysearch-practical-record-workflows.md).
- Recovering a whole estate file: [probate case inventory](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/probate-case-document-inventory.md).
- Identity rulings: [evidence/proof judgment](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md).

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
- **Free people of color in court records.** Full Text Search now covers court records, and phrase searches such as "free man of color" return free people of color. One example shown is the court registration of free people of color in Richmond County, Georgia, during the Civil War (for example the 1863 terms) [S2]. Record abbreviations such as FPC, FMC and FWC literally [S5].
- **Pennsylvania.** Living in Pennsylvania after the 1780 Gradual Abolition Act does not mean a person was free. The act ended slavery gradually, not at once [S21], [S23]:
  - People already enslaved when the act passed stayed enslaved for life, provided their enslavers registered them by 1 November 1780. Unregistered people were freed. Look for the 1780 slave register in the county.
  - Children born afterward to enslaved mothers were held as servants until age 28 (not for a 28-year term counted from some later date).
  - Registering each such child's birth comes from the amending act of 29 March 1788, not the 1780 act. The holder had to deliver the child's name, sex and age as best known, in writing, to the county clerk of the peace within six months of birth. Search county birth returns from 1788 onward. In Chester County these are the "Negro Servant Returns", 1788–1821.
  - Because of the age-28 term, people enslaved for life and term servants can turn up in the same households for decades after 1780.

  Search these Pennsylvania sources:
  - the 1780 county slave registers and the post-1788 birth returns described above;
  - the septennial census returns (Pennsylvania State Archives RG-7, 1779–1863), which include enslaved people in a household [S23]. Only about 11% of the returns survive, and many enumerators listed only people enslaved for life, not the term servants born after 1780. A blank entry therefore does not rule out a term servant;
  - the Pennsylvania Abolition Society's "Manumissions and indentures, ca. 1780–1840", held at the Historical Society of Pennsylvania and available as a seven-reel microfilm set. The series is arranged by name of master or slaveholder, so search under the master's name. It also includes records from several other eastern states, not only Pennsylvania [S22], [S24];
  - county manumission records. The presenter points to an index found by searching "manumissions" at chesco.org and credits it to the Chester County Historical Society [S22], [S24]. chesco.org is actually the site of Chester County Archives and Records Services, the county government's archive. The Historical Society is a separate private organization. The county archive lists slave manumissions among its holdings and posts online indexes to the 1780 Slave Register and the Negro Servant Returns. Confirm which index you are using, and cite the county archive as its custodian.

## 2. Look for a document that names the enslaver

Look for a record that names the enslaver before you guess one from a surname.

- **Find out how freedom came.** Possible routes include [S9]:
  - USCT service, with pension files claimed by widows, children or even parents;
  - self-emancipation;
  - flight to a contraband camp. Camp histories turn up in local history sources; a census will not show them;
  - wartime employment.
- **USCT questionnaires.** In the example shown in S14, a soldier's questionnaire asked him to "state the names of all former owners and particularly the name of your owner at the date of your enlistment". The presenter did not identify the form. Expect other USCT pension files to name former owners in testimony too. Record any enslaver named and the locator. With a common surname, matching same-surname slaveholders in the area can produce several candidates [S14].
- **Freedmen's Bureau field-office records.** The Bureau operated from 1865 to 1872, and its records are in National Archives Record Group 105 [S1]. Field-office records include rations and labor contracts [S17]. In one contract, a mother calls the people listed her children, which supplied relationships that the 1870 census lacks [S11]. Search the field office covering the person's home, and also the office in the nearest larger town, because people sometimes travelled there to file [S20].
- **Southern Claims Commission files.** Search by county, not by surname. Read the testimony in allowed claims and also in disallowed and barred claims (NARA M1407). These files are on Ancestry and Fold3. Formerly enslaved witnesses in someone else's claim may name their owner [S20].
- **Fugitive Slave Act cases (post-1850).** The 1850 act used federal commissioners and U.S. marshals to return fugitives, so it created federal paperwork: a petition, an ownership affidavit and witness testimony. Search under the claimant slaveholder's name [S8].

## 3. Generate and eliminate candidate enslavers

- **Collect candidates.** Draw them from the 1870 household (older generations living there), neighbors, shared given names between Black and white families, slave schedules and county slaveholder lists [S10], [S13].
- **Rank by schedule entries.** For a surname shared by several owners, compare each owner's 1850/1860 slave-schedule entries. Look for an enslaved person of the expected age and sex, and investigate the owners with a fit first [S18]. An owner with no fitting entry moves down the ranking but is not excluded: schedule ages may be estimates, so keep the mismatch unresolved unless independent evidence excludes that owner. Record the mismatch and its year in the candidate register.
- **Keep the surname as a set of hypotheses.** Possible explanations:
  - the last enslaver;
  - an earlier, first, favorite or longest enslaver [S25];
  - a parent's or grandparent's enslaver [S25];
  - a surname the person carried from owner to owner [S25];
  - no connection at all.

  The Liberty County presenter estimates that only about 10% of formerly enslaved people there took their last enslaver's name. In the presenter's example, the adopted surname pointed to a much earlier enslaver of the family [S12]. Treat that figure as a local, attributed estimate, not a rule.

## 4. Follow the personal-property chain, not land

Enslaved people appear in records of the enslaver's personal property: sale notices, business records and probate [S1]. For each candidate in the register, best fits first:

- **Get the full probate file**, not just the will: inventory, appraisals, accountings and distributions [S10], [S2]. Then retrieve the later wills of heirs, widows and administrators.
- **Retrieve the other property records:** deeds of sale or gift, mortgages and plantation papers [S15], [S16].
- **Follow the chain back through purchase, marriage and inheritance.** The presenter's El Destino example works back through:
  1. an 1845 estate inventory;
  2. an 1834 mortgage;
  3. an 1820 probate appraisal;
  4. a 1797 purchase;
  5. a 1786 will.

  The presenter labels much of the resulting tree a hypothesis [S15].
- **Full Text Search.** Put the enslaver's name in quotes in the name field. Add the given name and status keywords using the + prefix for required terms, then filter by place. Quoted phrases, + for required terms and place filters are documented tool behavior. The presenter's grouped form +(negro slave), which she says matches either word, comes only from her demonstration [S2]. Test it, and if it fails, run separate +negro and +slave searches. Also try +emancipate [S2].
  - Also search under the plantation, overseer and executor names [S3], [S6].
  - AI transcripts can drop commas between names, so read the original image [S6].
  - Re-run the searches every week or two, because processed coverage keeps growing [S3].

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
- **Name variants across documents.** Link variants such as Jim/James or Nan/Fanny/Nanny only as candidates. A repeated distinctive descriptor within the same family or neighborhood strengthens the case but does not settle it [S25].
- **Grouping type.** Mark each grouping **explicit** (for example "and her three children" [S2], or "Caesar his wife and his children" [S6]) or **order-inferred** [S15]. A woman listed in a mother-like position is a hypothesis unless the record lists family groups [S16]. List order can also reflect appraisal practice, so do not read adjacency as kinship.

## 6. Check segregated series before calling a search negative

- **Registers.** Search the separate colored register, the back of the register and the regular or white register. Clerks differed, and entries in a colored register may not state race [S5].
- **Other separated series.** Check Black churches, separate obituary sections, separate cemeteries or sections, segregated military units and prison records [S4].
- **Catholic registers.** Find out whether the diocese kept separate registers by race or one combined register. The S19 guest reports that, among the dioceses she has worked with, Baltimore alone puts enslaved and free Black people in the regular sacramental registers. She says status such as "free black" appears in the margin and entries sometimes name the owner [S19]. Record margin status and owner as separate observations.

Keep a coverage log of every series checked.

## 7. Keep narratives and DNA as separate tests

- **WPA narratives.** The Federal Writers' Project interviews (1936–1938) hold more than 2,300 first-person accounts by former slaves. A narrative from the same birthplace or birth year gives locality context. It is not evidence about the ancestor. Note the narratives' limits: memories more than 60 years old, uneven transcription and reduced candor with white interviewers [S7].
- **DNA.** DNA matches to descendants of a proposed sibling test one hypothesis [S15]. A Y-DNA surname mismatch is another. Neither proves who the enslaver or the father was. Route them to [Y-DNA interpretation](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/ydna-mtdna-interpretation.md) and [evidence/proof judgment](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md).

## Outputs

Return:

- the status-hypothesis table;
- the candidate-enslaver register with the basis for each candidate, any recorded mismatch and any exclusion with its independent evidence;
- the per-document register of named enslaved people;
- the segregated-series coverage log;
- candidate identity links, each with the record that would settle it.

Leave identity and kinship rulings to the researcher.
