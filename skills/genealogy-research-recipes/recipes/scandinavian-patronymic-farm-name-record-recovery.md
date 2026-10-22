# Recover a Scandinavian emigrant's home-parish entries under patronymic, farm and soldier names

Use this when a Danish, Norwegian, Swedish or Icelandic emigrant is known from destination records and you need to find that person in the home parish. The main way this goes wrong is searching the American surname in home-country indexes, finding nothing or attaching the wrong same-named person. The name in the parish register is usually not the American surname. Same-named parishioners are common, so separate them by birth date, parents, spouse, farm and vaccination entries, never by name alone.

Covered elsewhere and not repeated here: [same-name elimination](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md), [searching through an associate (§9)](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/ancestry-record-search-recovery.md), classifying name tokens (the catalogue's recipe on name searches across scripts and OCR), [native spellings and holdings audits (§2)](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/familysearch-practical-record-workflows.md).

## Fix the identity anchors before touching home-country indexes

From destination records (census, church, naturalization, obituary, passenger list), extract and keep separate:

- the exact birth date
- the town of birth or last residence, and the parish it belonged to
- the father's given name, if any record states it
- co-travellers such as siblings, a future spouse or neighbours

Start with destination records, identify the parish, and then search that parish [S2]. An approximate age is not an anchor. The exact birth date is. Swedish church books, including the household examination books, record the exact birth date, often in its own column, so the date works almost like an identifier for telling same-named people apart [S5].

Do not search the American surname backwards as if it were hereditary. Everett's example: a family known as Jensens in America cannot simply be looked for as Jensens in Denmark [S2].

## Build the expected name forms and log them as a register

Create one row for each form you expect or observe. Record the literal form, the record it appears in, and its type: patronymic, matronymic, farm/house, soldier byname or adopted.

- **Patronymic.** Built from the father's given name plus -son/-sen or -dotter/-datter. It changes every generation [S1], [S5]. Build spelling variants as well. Brady shows one man recorded as Persson, Pierson, Pettersson and similar forms across Swedish and U.S. records [S1]. Swedish given names also vary, for example Per, Petter, Peder and Pär for Peter [S1].
- **Matronymic.** An illegitimate Swedish child may carry a surname based on the mother's name [S3]. A female-based surname is a lead to an illegitimate birth, not an error. Check the baptism entry for it before you look for a father.
- **Farm or house name.** Clerks added these to tell parishioners apart. A farm name may stay with a family for generations or for only one [S6]. Castillo reports that the farm name changed when a person moved to another farm, and that she has seen a son-in-law who married into a family of daughters take his father-in-law's name or the farm's name [S3]. A change of farm name is therefore not a change of person.
- **Soldier byname.** The army assigned these because so many men had the same name, and soldiers may appear under either the patronymic or the soldier name. Some men kept the byname afterwards. Brady's example is Johan Magnus Anderson from Kalmar province, who was John Falk in the U.S. and Johan Magnus Anderson in Swedish records [S1]. In S5, the guest's family surname came from a great-great-uncle's army byname, which an emigrant brother adopted instead of the patronymic. Search military records by unit and by the soldier name, not only by the civil name, starting with the local muster [S8].
- **Adopted American name.** This may come from none of the forms above. Everett's Walter Slangerup was christened Waldemar … Martinson after his father. After emigrating he took the name of Slangerup, a town northwest of Copenhagen that his great-grandfather came from [S2]. Treat the American surname as one observed form, not as the search key.

In your tree, enter the name exactly as it appears in the christening (the first record) as the primary form. Log every farm, soldier or American name as an alternate with its source [S6].

## Search the forms, then browse to the known date

Search the parish indexes under each patronymic and farm form in the register. If all of them fail, do not conclude the person is absent. Browse the parish register to the known birth date and recognize the entry from its context. Everett found Slangerup this way after no index search could reach him [S2].

Write down the parish, register volume and date range you browsed. If you get no hit, report that bounded range, not "not born there."

## Pivot through co-travellers when the passenger search fails

If you cannot find the emigrant on a passenger list:

1. Open the manifest of a known co-traveller, such as a future spouse or a sibling. In S5, the guest found his great-grandfather next to his future wife, listed under a father-derived "-son" form instead of the American surname.
2. Scan the nearby pages, not only the family group, for people with the same farm name and a matching patronymic. In S7, a probable brother was listed on the parents' page of a Norway Heritage transcription, outside the family group, under the same farm name; the family's daughter appeared a page or two later. Those transcriptions mainly cover 1825–1873/75. The site search is currently down, so browse by ship and year.
3. Treat any such person as a candidate only. Confirm through:
   - the home-parish baptism, which should name the expected parents and parish
   - the minister's record of people moving out (in Norwegian church books, the *utflyttede* section), with an entry dated before sailing [S7]

S7 found both records for its candidate. The moving-in and moving-out registers (*innflyttede* / *utflyttede* in Norway) also let you follow a person between parishes [S2], [S9].

## Discriminate same-named candidates with a comparison table

Same-named people are common in a parish. Families with the same parents' names and the same children's names are also common, so a careless search attaches other families' children [S1], [S4]. Build one row per candidate with these columns:

- exact birth date
- father's name, and mother's name where recorded
- spouse
- farm or house of residence, taken from house censuses and farm records [S4]
- smallpox vaccination date and place, from baptism, confirmation or marriage entries [S2]
- the locator for each entry

Vaccination became compulsory in Norway from 1810 and in Sweden from 1816. Denmark's decree of 3 April 1810 required a vaccination certificate for school, confirmation and marriage. In Danish confirmation and marriage entries after 1810, expect the vaccination note and use it. Everett shows it in a Norwegian marriage entry of 1843 and in confirmation entries, and uses the vaccination date and place to decide whether two records are the same person [S2]. In other places and periods, check whether the column exists before you count a blank against a candidate.

Tanner warns that a Norwegian line with no source at the house-census or farm level is very likely wrong in its places, its names or both [S4]. Treat such an inherited tree as unverified until you have tied it to farm-level records, such as the censuses and church records on Digitalarkivet.

A candidate matches only when several of these discriminators agree. Leave any column you could not fill blank, and send the merge-or-separate decision to [evidence/proof judgment](https://github.com/Kinprove/genealogy-research-recipes/blob/8b235c47acf62b78cd5a1ccf85f4eb974b2f966a/skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md).

## Rebuild siblings and marriages from the named parents

- **Sibling sets.** Build these from the parents named in each baptism, not from a shared surname. Around a parish's change to fixed surnames, older children may carry the father's patronymic while younger ones carry a fixed surname [S6]. Brady says adult siblings in Sweden chose their own fixed surnames, so two brothers can have different surnames [S1].
- **Transition dates.** The laws differ by country, and people widely ignored them, so read the actual parish entries:
  - Denmark: a decree in 1828 and a ministerial circular in 1856.
  - Sweden: Brady places voluntary fixed surnames around the 1880s [S1], and Castillo dates the first changes to about 1860 [S3]. The names act of 5 December 1901 then required anyone without a fixed surname to take the masculine form of the father's surname.
  - Norway: the first Name Act came on 9 February 1923.
  - Iceland never abandoned patronymics [S9].

  Lisson's guest's "mid-1800s, each country its own year" [S6] fits Denmark only. Do not apply it to Swedish or Norwegian parishes. Tanner's "after about 1830, varying by country" [S9] is a rough orientation, not a rule.
- **Marriages.** Under traditional patronymic practice, wives keep their own patronymic or maiden name, so a wife whose surname differs from her husband's is not a mistake [S5]. Norway's 1923 Name Act required a wife to take her husband's surname, so for later Norwegian records also log her married-name form. A census household can list a man and several women, none of them with his surname, and nothing shows which woman is his wife. Prove the marriage in the parish register [S9].

## Close with an origin packet

Return:

- the name-form register
- the candidate comparison table, with the discriminators used for each candidate
- the baptism entry with its parish, volume, page or date, and image locator, or the bounded browse range with no hit
- the sibling and marriage reconstruction, citing the parents named in each entry
- any unresolved alternate identities, kept visible

A co-traveller row, a shared farm name or an indexed baptism hint is still a candidate until the parish entries agree.
