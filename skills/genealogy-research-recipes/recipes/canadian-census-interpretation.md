---
id: "canadian-census-interpretation"
title: "Interpret a historical Canadian census entry as a de jure listing"
summary: "Read a historical Canadian census line as a de jure listing, and browse by geography when a name search misses."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "CANADIAN-CENSUS-INTERPRETATION-01", "text": "For any census from 1871 onward, write on the observation that the enumeration was de jure. People were listed where they were supposed to belong, as reported by an informant, not where they physically were at a cutoff time."}]
handoff: []
checked: "2026-11-07"
checked_basis: "opened 2026-11-07"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Canada, Latin America, Asia and Oceania", "order": 183}
---

# Interpret a historical Canadian census entry as a de jure listing

Use this recipe when a historical Canadian census line is about to be used as evidence of where someone lived, whether they were alive, who was in the household, or their marital status. Also use it when a name search of a Canadian census, such as 1931, misses a household and you have to browse the images by geography. The default mistake is to read a Canadian listing the way you would read a "present on census night" listing. For year-specific U.S. counting rules, double enumeration and district carry-over, use [U.S. census workflows](us-census-practical-workflows.md). For stated statuses and merge conflicts in general, use [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- Record the enumeration basis before reading the line
- Apply the de jure consequences decisively
- Check form wording and timing for that year
- Browse by title-card geography when the name search misses
- Return an annotated observation

## Record the enumeration basis before reading the line

For a pre-Confederation search in present-day Québec, select the census by year and historical jurisdiction [S29 @2026-11-20]. In LAC's pre-Confederation guide, open Lower Canada for 1825 or 1831, Canada East for 1842, or the Québec returns under *Census of 1851* or *Census of 1861* [S30 @2026-11-20]. Check the surviving sub-districts before treating a miss as evidence of absence [S30 @2026-11-20].

For 1842 Canada West, read the head’s name separately from the numerical household columns. LAC lists a named head of each family, followed by counts by age, sex and other categories [S19]. Do not assign unnamed household counts to particular spouses or children. Check the surviving district pages and their headings before calling a household absent; a statistical total is not a nominal return [S20].

For any census from 1871 onward, write on the observation that the enumeration was de jure. People were listed where they were supposed to belong, as reported by an informant, not where they physically were at a cutoff time. Both presenters stress this as the critical difference from de facto systems, and Ep. 203 contrasts it with the English census [S1], [S2]. The 1852 census (1851 series) is the exception. It mixed de facto and de jure counting and included visitors. Do not apply the presence, absence or duplicate consequences below to 1852 without first checking that year's rules, and read a listed visitor there as someone physically present at that household. Name the informant if the record does. Otherwise mark the informant as unknown.

Before reading an 1871-or-later entry as a home, check whether the instructions placed it where the person was found. In 1931, families or persons in temporary residence, such as summer residents, were entered on the regular schedule with an asterisk in the left margin, and an Absentee Family Card credited them to their fixed home. Read an asterisked entry as the place the person was found, not a reported home. Treat an ordinary household entry as a reported legal residence and nothing more. Do not conclude any of the following from it:

- **Physical presence.** Record the address as the household's report of residence. A spouse seeking work elsewhere could still be listed at home [S1], [S2]. Look for a local record placing that person at the address on the date in question.
- **Being in Canada.** Living abroad did not necessarily prevent enumeration at a Canadian home address [S1]. Check the destination as well.
- **Survival on census day.** A household that had lost contact could report a relative who had already died [S1], [S2]. Compare the death record with the census entry.

When a household reports a long-absent spouse, trace the last documented contact and search for the spouse's own records elsewhere. Obee describes an absence of up to 25 years [S2]. Check the instructions for the particular return before applying any time limit.

## Apply the de jure consequences decisively

- **Duplicate enumeration.** Search both the family home and the work destination. In Obee's illustration a wife in Nova Scotia could report her husband while he gave his own details in Alberta [S2]. Compare age, occupation and family connections across the two lines before deciding whether they describe one person.
- **An earlier death certificate.** Compare the deceased's identifiers with the census household. In his own family Obee initially set aside a death certificate because a later return still listed the relative [S2]. Keep the conflict visible while checking who could have reported each event.
- **A missing name.** Check whether the return sought usual residents or visitors. A usual resident could be omitted, and an overnight visitor could be recorded at home [S3], [S4]. The 1852 census included visitors. In 1931, instructions §§61–62 put temporary residents on the regular schedule with an asterisk. Check for that mark before using an entry to infer residence.

## Check form wording and timing for that year

- **Marital status.** Read the permitted responses on the form and in the instructions. Obee recalls returns with no “divorced” option and gives no years [S2]. If the form offered no such response, look for a divorce as well as a death before interpreting “widowed.”
- **Bilingual headings.** Transcribe both headings for the column in question. Obee found variations across several years when translating the French headings [S2]. Where two readings change what the answer means, record each reading and check the enumerator instructions for that year.
- **Reference date.** Calculate age at the date the schedule specifies. Library and Archives Canada gives 2 April 1871 [S6], 4 April 1881 [S21], 31 March 1901 [S23], 1 June 1921 [S25] and 1 June 1931 [S11]. For 1901 the retrospective *Canada Year Book* says 1 April [S8], but the schedule specifies 31 March for household membership and age [S23]. For 1891, enumeration began on 6 April [S22], and the population was counted as of 5 April [S7], [S8]. For 1911 use 1 June. LAC lists 11 June as the start, but its age column explicitly uses 1 June [S24], the date also given by the *Year Book* [S8]. The prairie censuses began on 24 June 1906 [S26], 1 June 1916 [S27] and 1 June 1926 [S28].
- **Birth dates.** The 1901 return asks for each person's month, day and year of birth [S23]. The return for 1911 asks for month and year [S24]. Compare the reported birth date with the age column.
- **Instructions.** Look for the enumerator instructions for the year and the notices in newspapers published before enumeration. Obee found contemporary notices explaining how to report residents [S2].
- **Remote and northern districts:** if the entry comes from a northern or remote district that enumerators reached rarely, flag the observation with a possible timing gap and check the printed census reports for that district. Obee says such areas might get one visit a year. Information there could be taken about two months before or after the official date, so a person interviewed in person might have died by census day [S1]. Take the population and age reference date from that year's instructions. For 1931 it is 1 June 1931, and a late visit does not admit a child born after that date.

- **1931 radio column:** read column 10, "Has this family a radio?", as one answer for the family, not for a person. The 1931 instructions (§100, as transcribed by the Canadian Century Research Infrastructure project) had the enumerator write yes or no opposite the name of the head of the family "irrespective of the ownership of the instrument" [S15]. LAC notes that 1931 was the first census to ask it [S11]. Record the answer once, for the family. Do not copy it to other members, and do not read a yes as the head having bought or owned the set. Kathryn Lake Hogan (transcript excerpts, not independently verified) reads a yes as a hint of the family's prosperity [S10†]; log it as household context only, never as evidence of income.

## Browse by title-card geography when the name search misses

Since 1 June 2023 the 1931 images have been public, and at launch they could only be browsed. The presenter's workflow comes from that period [S5]. LAC's announcement confirms a free searchable **1931** index in Census Search, made with Ancestry and FamilySearch. [S9] Search it first; check another provider's actual collection coverage before treating it as an independent search. Use the browse below when the index misses a household you have good reason to expect. A missed name search does not show the household is absent. For index and search-scope failures on a platform, use [Ancestry search recovery](ancestry-record-search-recovery.md).

1. **Earlier census location.** From the nearest earlier census, record:
   - enumeration sub-district number
   - municipality
   - township, range and meridian
   - street address, if the household was in town

   For the 1926 Prairie census, also record the neighbours. In the Regina search, Harry Cook's household was at 520 Osler Street, township 17, municipality of Sherwood [S5].
2. **City directory.** Check a directory for the target year. The 1931 Regina directory placed Harry and Martha at the same address [S5]. See the [city-directory recipe](city-directory-observation-workflow.md) for edition dates.
3. **Check what the old number now covers.** The Cooks' 1926 sub-district was 8. In 1931 the title card for 8 matched neither Sherwood nor township 17 [S5]. Discard that number as a location lead and continue through the neighbouring sub-districts.
4. **Step through title cards.** The first image of each sub-district is a title card showing township and municipality [S5]. First check the sub-districts on either side of the old number, since the area may not have shifted far. Then, if there is still no match, open every sub-district in order from number 1, which is how the presenter worked, and look for a township-plus-municipality match [S5]. That key fits Prairie records with numbered townships, as in the presenter's Regina example. Elsewhere, match the locality, ward, parish or street address that the title card and schedule actually give. Log every card you check, including partial matches (right township but wrong municipality, or the reverse), and keep going [S5].
5. **Plausibility screens.** For a promising sub-district, the presenter:
   - looked at image 2, the first page of residents, and compared the neighbourhood's make-up with the earlier census's neighbours
   - checked the township column against the recorded number
   - measured distances between the known street and the street names on the pages
   [S5]

   These screens only decide where to keep looking. A neighbourhood that matches by ancestry or a nearby street does not identify anyone.
6. **Locate and cite.** Record the year, district, sub-district and image of the household. For the Cooks, the 1931 title card for sub-district 11 matched both township 17 and Sherwood. Image 18 contained the household on Osler Street [S5]. Read the entry under the residence rules above.

Where no directory covers the place or year, take the ancestor's address from the 1935 federal voters list and work back to 1931, as Kathryn Lake Hogan suggests (transcript excerpts, not independently verified) [S10†]. Its entries give name, address and occupation and list a household's voters together [S18]. The lists run by electoral district within each province, then by polling station number and address; only some rural districts are alphabetical [S16], [S17]. Read the 1935 address as a lead to test in 1931, not as a 1931 residence: the list is four years later and names only people eligible to vote [S16]. Carry the street or township into the finding-aid lookup below, not the 1935 district or poll number, because the 1931 returns are organized by districts that closely follow the 1924 electoral map [S11].

LAC holds the federal voters lists from 1935 on, and the 1935 lists are indexed by name and digitized on Ancestry, a subscription service that many public libraries offer free [S16 @2026-11-16].

**Look up the 1931 sub-district in LAC's finding aids.** Hogan (transcript excerpts, not independently verified) points to census statistics for western districts whose names do not match the place the family lived [S10†]. Do not take the district from a table of census divisions: the divisions used to publish results sometimes differ from the districts used to collect the returns [S12]. No 1931 sub-district maps are known to survive, so work from the written descriptions [S13].

- **Cities.** For a street in Halifax, Saint John, Quebec, Montréal, Toronto, Hamilton, London, Winnipeg, Edmonton, Calgary or Vancouver, use LAC's street index for that city and only its entries marked 31 [S13].
- **Elsewhere.** Keyword-search the province's finding aid, which transcribes the Dominion Bureau of Statistics sub-district descriptions [S13]. On the Prairies, search both the village or town name and the township, range and meridian. In the Saskatchewan aid's first pages (partial read), a township's description often excludes a village that has its own sub-district, so the family's land and the nearby village can fall in different sub-districts [S14]. Open every sub-district a search returns; LAC's own example, "Birtle", returns sub-districts 24, 25 and 63 of Marquette [S13].
- **Images.** The Saskatchewan aid (partial read: pages 1–2 checked) gives each sub-district's district number and name, microfilm reel and first and last image numbers [S14]. Go to that range and confirm the title card.
- **Unnamed places.** If the aid does not name the place, find the 1924 federal riding it lay in, because 1931 districts nearly always match those ridings [S11], [S12]. Then read that district's descriptions in the aid.

- **Combined sub-districts.** Some small sub-districts were combined by the enumerators. LAC's search takes only the first number of a combined pair; for sub-districts 43 and 44 of District 114, enter 43 [S11 @2026-11-16].

Use the earlier number when the finding aids leave the household unplaced, then step through title cards. LAC says 1931 sub-district names or boundaries are not those of 1921, particularly in large cities [S11]. Hogan's guess (transcript excerpts, not independently verified) that 1921 and 1926 districts partly carried over to 1931 is not a rule [S10†]; use an earlier sub-district description only to help read the 1931 descriptions [S13].

## Return an annotated observation

For each census line, return:

- the literal entry and locator
- the enumeration basis (de jure for 1871 onward; mixed for 1852)
- the entry type: an ordinary household entry or an asterisked temporary-resident entry
- the informant (named or unknown)
- the form's option limits for any interpreted field, plus both heading wordings where they differ
- any remote-district timing caveat
- a possible-duplicate check against other provinces or households
- for an ordinary household entry, a plain statement that the line does not establish presence, survival on census day or residence in Canada

For a browse, also return:

- the name searches tried and where
- the address sources used (directory, 1935 voters list), with their dates
- the finding-aid or street-index searches and the sub-districts they returned
- the log of title cards checked
- partial matches
- the screens applied
- the final sub-district/image citation

If no title card matched, report the sub-districts covered. Do not report the household as absent.
