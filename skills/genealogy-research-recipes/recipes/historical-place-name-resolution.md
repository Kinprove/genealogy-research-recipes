# Resolve a historical place name to dated, same-named candidates

Use this recipe when a place named in a record, family letter, Bible or published biography can't be found, or when it matches a well-known place. Typical wrong defaults are Reno meaning Nevada, Aberdeen meaning Scotland, or Edison meaning today's Edison, Washington. The recipe lists every same-named feature in feature-level, period-dated gazetteers, keeps the name exactly as written, and lets other dated evidence about the person choose among the candidates.

Not covered here:

- The general geographic reality check: [evidence/proof judgment § Geographic reality check](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md).
- Russian-Empire locality handoff: [emigrant-origin recovery § 5](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/russian-empire-emigrant-origin-recovery.md).
- FamilySearch place-tool jurisdiction: [FamilySearch workflows § 1](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/familysearch-practical-record-workflows.md).
- AI candidate generation for an unclear German word: [AI for documentary records](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/ai-for-documentary-records.md).
- JewishGen town geography: [JewishGen search](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/jewishgen-search-family-reconstruction.md).

**The failure this prevents:** taking the best-known or first match, treating a historical name as the modern place with the same name, calling a name that can't be found an error, or treating a sound-alike or a gazetteer hit with coordinates as proof of where someone lived. A gazetteer hit gives you a candidate. It does not establish residence.

## 1. Record the literal form and how it reached the page

- Copy the place exactly as written. Record who wrote it, when, in what source, and from whose speech. Do not modernise or correct it in the working record.
- Ask whether the writer could have misheard someone speaking another language or with a strong accent. In the presenter's Irish case, a US-born daughter wrote down her Irish-speaking father's birthplace from his speech. Her spelling matched no Irish gazetteer entry. Years later the place was resolved as Mulvin, a townland in Ardstraw civil parish, County Tyrone, the parish where his father was reportedly born [S1], [S2], [S3]. Also consider an English listener's spelling of a Spanish name (Slough for Salado) [S4] and an English phonetic spelling of a German one [S12].
- Treat every compiled extract as normalised until you have checked the cited film or image. Minert's German-immigrant church-record compilations deliberately "correct" place spellings to gazetteer forms and assign places to 1871–1918 German Empire borders. Go back to the cited film or image for the literal spelling, and keep the literal and identified forms in separate columns. His team reports that about 30% of place names in the church records were misspelled, and up to 75% for one pastor [S23].
- Write down associated places from the same document or family records, such as a parent's parish, a stated district, or other places named in a letter. These limit where you search for sound-alikes [S1], [S15].

## 2. List every same-named feature, not just towns

- Search a gazetteer that covers features as well as settlements. For US names, use the Board on Geographic Names (BGN) domestic names / GNIS. For foreign names, use the BGN foreign-names gazetteers. These list populated places plus lakes, hills, valleys and other natural features, each with a feature class and coordinates [S4], [S6], [S11]. GNIS also keeps features that no longer exist and names no longer in use, flagged as "historical", so a vanished place can still turn up. In Jensen's example, a German "town" that couldn't be found was a small lake. Its coordinates led to a detailed map and to the surrounding parishes, where the ancestor was found [S11].
- GNIS no longer holds every feature type. Since 2021 USGS has removed many man-made feature classes from GNIS, including cemeteries, churches, post offices, schools, mines, buildings, dams and parks. A church, cemetery or post-office name that an older presentation found there may no longer come up. A GNIS miss on one of those classes tells you nothing. Go to dated maps and gazetteers (§3).
- Search at every level before choosing a match: the county if it is known, then the state or country, then nationally or across countries. Common names repeat. Examples:
  - Pig Hollow, which the presenter's search found in five states [S4].
  - Pumpkin Hollow, in many states; the presenter's GNIS search showed about 50 [S5].
  - Many Pumpkin Centers [S6].
  - Little Poor Valley, which the presenter's search returned in both Scott County, Virginia and Hawkins County, Tennessee [S8]. Poor Valley itself crosses those two counties.
  - Several Deer Lakes in Michigan [S10].
  - Aberdeen, which names several places outside Scotland, including Aberdeen, Washington. The presenter counts about 15 in former British territory [S22].
- A name found in only one region narrows the search area. The presenter read Nicollet in an 1855 letter as pointing to the Midwest or Great Lakes, the only North American area where she says the name occurs [S21]. Confirm the distribution in GNIS and BGN, then search that region first.
- For each hit, keep the feature ID, feature class, county, state and listed topographic quadrangle. A GNIS feature ID retrieves that exact entry, and the entry names the topo maps the feature appears on [S6]. If the target is too small to find directly, search the larger place on the same quadrangle. Then look at the names around it in a feature viewer such as GeoNames. Feaster, Arizona was found this way through the Nutrioso quadrangle [S4].
- If you can't read the spelling, don't stop at a failed exact search. In 2018 the presenter said the FamilySearch Catalog needed an exact place spelling [S24]. Instead, browse "places within" the known county or province, or run a fuzzy-spelling gazetteer search limited to the likely country. In the presenter's example, the country filter cut 409 results to 3 [S24]. Any spelling you recover this way is still only a candidate.
- **Use the place list in the record's own unit before guessing sound-alikes.** If the record names a unit (a volost, parish or district), list every settlement in it from records of the same period. Use settlement headings in census and tax lists, register entries, and period lists of populated places. Keep the alias forms ("X, also called Y") and any alternate names given in brackets. Then match the odd reading against that list. A name can be a river or a resident family's surname standing in for the village.
  - In one forum thread, a commissioned extract in modern spelling named a bride's village "Barzino" in the volost. No settlement of that name could be found. A participant proposed building a register of the volost's settlements from the published census books, and the researcher later reported, without saying how, that the village was Berdysheva [S25].
  - In another thread, "Shavy" matched no village. A participant linked it to a 1719 census heading for the village of Sheveleva (Shevelova in 1869) on the Shava rivulet, where the Prytkov family lived. The participant also reported an 1869 Perm list giving it as Shevelova (Prytkova) [S26].
  - In a parish register, check whether each candidate also appears elsewhere under its normal spelling. A candidate that never appears separately fits an odd spelling better than one the clerk wrote normally elsewhere. Compare the uncertain first letter with a place name in the same hand that you can read with certainty. Participants resolved "Rinsen" near Kellinghusen as Rensing this way, and an old-map spelling was offered in support [S27].
  
  **Limit:** each of these is a lead. The Shavy link rests on a shared river name and surname. The register check for Rensing was cursory. The forum posts don't show the images behind the Barzino result. None of these places the person there.

## 3. Date the name before matching it

- Every candidate row needs a gazetteer or map dated close to the record. A modern-only match is not a candidate yet. Place names change in three ways:
  - **Names move.** Edison was the name of the area now called South Tacoma (renamed in 1895). Today's Edison is in Skagit County, in northern Washington [S14].
  - **Names change.** Neuse Crossroads, Wake County, North Carolina was formerly Dunnsville and Neuse. The Roanoke River carried other names on older maps [S17].
  - **Places disappear.** Small, Idaho, on Medicine Lodge Creek, appears on a 1909 Fremont County map but not on Google Maps [S15].
- **Date the name to when the document was written, not only to the event.** A later certificate, questionnaire or database may record a birthplace under the name in force when it was written rather than the name at the event. Before choosing which registers to search, establish which of the two the document uses. If it is the later name, translate it back to the name in use at the event. In one forum thread, a Soviet certificate gave the birthplace as the village of Kalinino. Its pre-1915 name was Yugo-Knaufsky zavod, and the researcher found a matching birth date and given name in that settlement's register, under a different surname. The researcher asked whether the match was reliable and later reported that this version was not confirmed. The rename was the useful step; the match was not [S29]. The reverse also applies: search indexes built from later forms under the later name as well. A participant found only four Leningrad-born prisoners in a database of Gulag camp prisoners and inferred that it recorded birthplaces as Leningrad, not Petersburg or Petrograd [S30]. Search every such index under both forms.
- Read period gazetteer entries for location relative to other places, civil registration office, post office and railway. Check name-change supplements too. For the German Empire, the standard gazetteer is Meyers Orts- und Verkehrs-Lexikon (1912 edition). The presenter also has an 80-page German name-change volume issued within three years of one Meyers edition, and he reports a Ukrainian village with six names in the 20th century [S13]. An 1860s Irish gazetteer from the Internet Archive matched Coast Guard station names that no modern map showed [S16].
- Record whether each name on a dated map is a town, a creek or an area. On the 1909 map, Medicine Lodge was a creek and a ranching area, not a town [S15].

## 4. Convert phonetic and translated forms back to the source language

- Map each syllable and regional term into the source language, for example Middle→Mittel and Lower Franconia→Unterfranken. Check the national gazetteer first (Meyers), then the alphabetical list in the regional (state-level) gazetteer, in this case Bavaria's [S12].
- Accept a candidate only when the gazetteer's district fits the district given in the source. In the presenter's example, only one Bavarian entry matched the converted syllables, and the district the gazetteer listed for it corrected the phonetic district name in the biography [S12].
- If only the end of a name is legible, use a reverse-alphabetical place index such as Minert's German place-name indexes [S23].
- For Irish names, use logainm.ie, the bilingual Placenames Database of Ireland, which gives county, barony, civil parish and townland. Check the candidate at every level [S2].

## 5. Look below the settlement level, and resolve nicknames

- **Scottish farm towns.** A Scottish residence name in a register or family letter may be a farm town: a cluster of farm buildings within a parish or estate, not a town. Find it on 1:25,000 Ordnance Survey or National Library of Scotland maps. Use 1:25,000 rather than 1:50,000, because the smaller farm-town names appear only at the larger scale. NLS has a side-by-side viewer for comparing an old map with modern imagery [S18], [S19]. Use the recorded farm or estate to keep same-surname households in one parish apart rather than merging them [S18].
- **Parish boundaries.** Parishes can change county. Cairnie lay across the Aberdeenshire–Banffshire line until 1891, when the Boundary Commissioners transferred its Banffshire part to the Banffshire parish of Keith. After that, Cairnie was wholly in Aberdeenshire. (The presenter described this change the other way round [S19].) Treat the nearest parish only as a candidate repository until you confirm its jurisdiction at the event date.
- **Nicknames.** Before calling a name nonexistent, check whether it is a local nickname:
  - Fogieloan (Foggieloan) is the old and local name for Aberchirder [S19].
  - In a published biography, Wrangle Town turned out, from county historical journals, to be the nickname for a five-road crossroads with taverns. The subject's 1929 death certificate gave the official place [S20].
  - Soap Hill, a name later dropped from maps, was explained by local memory [S20].
  
  Search county historical journals, local histories, and local societies or their social-media groups [S20], [S17].
- **Oral explanations are leads, not proof.** Record them as leads that need documents to back them up. The presenter herself planned to check the Soap Hill account against legislative records [S20]. Record the official place from another record separately from the nickname.
- **Wherever they were at the time.** An informal name can mean only where the family happened to be at the time [S10]. If no settlement of that name fits, do not force a match to a settlement, and do not adopt the informal reading as the answer either. Add "informal/locational" as one candidate row and test it against dated residence evidence.

## 6. Plot candidates against dated jurisdictions

- Carry decimal coordinates with their sign. Western-Hemisphere longitudes are negative. If you drop the minus sign, the point lands on the opposite side of the world [S4].
- Plot each candidate against dated county boundaries, for example the Newberry Library's Atlas of Historical County Boundaries (US changes through 2000). List every county that may have created records at the event date [S5], [S7]. Small, Idaho shows why this matters: it was in Fremont County in 1909, but the area is now in Clark County, which was created from Fremont in 1919 [S15].
- If the feature is a valley or area that crosses a boundary, keep both sides as candidate record jurisdictions until the residence is located more precisely. The presenter's Little Poor Valley family lived in Virginia and found wives in Tennessee by travelling along the valley [S8].
- Measure each candidate's distance from the family's documented places. The presenter's GNIS search returned Clove Valley, Dutchess County as a populated place 16 miles from where a son died [S9].

## 7. Narrow candidates only with independent, dated evidence

- Research every candidate rather than picking the one that fits the family story. For each one, check its settlement date, its population around the event date, older gazetteers, and town and county records [S10]. Use ordinary record research (land, probate and so on) to decide which state and county a common name means [S6].
- **Check the owner or unit the record states.** If the record says the person came from a named estate, owner, volost or district, drop any same-named place that lay outside it at the date. In one forum thread, a 1711 census of the Stroganov estates gave the family's origin as a Chernovskaya on those estates. A participant ruled out a same-named Chernovskoye on the Siva, about 250 km from the family's home by the poster's estimate, because it did not belong to the Stroganovs [S25]. **Limit:** that ownership statement is the participant's, and the thread doesn't document it. Check it in a dated estate or administrative list.
- **An unsourced identification is not a candidate.** Don't accept a place identification from a search engine or an AI summary that no printed gazetteer supports until its source is shown. List the same-named places from printed gazetteers for the period, including renamings. Then check the exact birth date in the civil registry office (Standesamt) register that covered each place at the date. In one forum thread, a search engine equated "Josefsdorf" with a hamlet beside the family's later home. A participant found it in no printed gazetteer. He then checked the exact date in two civil registers: the one covering that area (Zembowitz) and the one covering an Upper Silesian Josefsdorf (Domb). The birth was in neither. Participants also listed three West Prussian places named Josefsdorf for the researcher to check, and noted four Volhynian places named Józefin. The thread doesn't report any of those being checked [S28]. **Limit:** a failed check means the birth is not in those two registers. It does not rule the places out, and it does not make the unsourced identification true.
- Look for a set of names that fit together on one dated map. Small, Reno and Medicine Lodge all fit within 1909 Fremont County, Idaho, which ruled out Reno, Nevada [S15].
- Plot dated postings beside the children's birthplaces. A puzzling birthplace made sense once it lined up with the father's Coast Guard assignment [S16].
- Use other dated context in the document. In the 1855 letter, "the gold diggings" led the presenter to consider the Australian goldfields [S21]. Record any inference like that as a stated premise.
- Keep a sound-alike as a hypothesis until it is named in a record where the subject gave the place himself, or in a reliably recorded official record. In the presenter's case, Mulvin, found by a sound-alike search near Ardstraw, was confirmed only when an early church record in special collections showed the man giving it as his birthplace [S1]. In a later retelling, the presenter says a marriage record held only at the Family History Library played that role [S3]. Further weighing belongs in [evidence/proof judgment](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md).

## 8. Return a candidate table

Before you call a name unresolved, complete at least these passes:

1. A feature-level gazetteer (GNIS / BGN), searched at every jurisdiction level.
2. A period gazetteer or map dated close to the record, plus name-change supplements where they exist.
3. A regional (state, county or province) gazetteer or detailed map.
4. Nickname sources: county journals, local histories, and local societies.

Return one row per candidate:

literal form | interpreted form and basis (phonetic / translation / nickname / rename / moved name) | gazetteer or map and edition/date | feature ID and feature type | county/district and jurisdiction at the event date | coordinates (signed decimal) | supporting and conflicting dated evidence | status (candidate / eliminated (reason) / corroborated by a named record)

Then list the record jurisdictions to search for each surviving candidate, including both sides of any boundary. Also list the gazetteer editions and nickname sources you haven't searched yet, and note any feature class that current GNIS no longer holds. "Not found" means not found in the editions named in the table. It does not mean the place never existed or that the record is wrong.
