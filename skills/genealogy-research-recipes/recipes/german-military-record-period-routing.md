---
id: "german-military-record-period-routing"
title: "Route a German soldier to the military series that survive for his period, army and rank"
summary: "Route a German soldier to the series that survive for his period, army and rank class; recover dated hospital-book episodes when personnel files are missing."
kind: "records"
scope: {"platforms": [], "tasks": ["Route a German soldier to the series that survive for his period, army and rank class; recover dated hospital-book episodes when personnel files are missing."]}
triggers: ["Route a German soldier to the series that survive for his period", "army and rank class", "recover dated hospital-book episodes when personnel files are missing"]
privacy: "none"
gates: []
guardrails: [{"id": "GERMAN-MILITARY-RECORD-PERIOD-ROUTING-01", "text": "a canton, gazette notice or casualty-list line is a lead, never a birthplace, death date or identity."}]
handoff: ["galicia-bukovina-habsburg-record-routing"]
checked: "2026-11-06"
checked_basis: "checked 2026-11-06"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "pointer", "group": "German records", "order": 1079}
---

# Route a German soldier to the military series that survive for his period, army and rank

Use this recipe before you send anyone to look for a German soldier's personnel file. It applies when a church entry, address book, gazette, casualty list, memorial or grave register calls an ancestor a soldier, NCO or officer. First classify the man by period, army and rank class. Then search only the series that survive for that combination. A regimental canton, a gazette notice or a casualty-list line is a lead with limits. None of them is a birthplace, a death date or an identity.

For using address books to bound a death window, use [city-directory observation workflow](city-directory-observation-workflow.md). For keeping loss, burial and administrative dates as separate episodes, the closest model is [Russian military and repression record episodes](russian-military-repression-record-episodes.md). For any ruling that two entries are or are not the same man, use [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- 1\. Classify the man before choosing a series
- 2\. Old-Prussian army (1714–1806): the Stammrollen are gone, so work from church books and the canton
- 3\. Imperial officers, active or retired: gazette, chronicle, then a death window
- 4\. First World War casualty lists and memorials: check for a namesake, then check the script
- 5\. Wehrmacht: personnel and loss documents first, then unit records
- Output

## 1. Classify the man before choosing a series

Record three things, each with the document that supports it:

- **Period:** Old-Prussian army (1714–1806), Imperial army in peacetime (before 1914, including retired officers), First World War, or Wehrmacht.
- **Rank class:** enlisted or NCO, or officer. The surviving series differ sharply between the two. Do not merge the routes.
- **Army or state:** Prussian, another German state, Austro-Hungarian and so on. Take the regiment's name and number exactly as the entry gives them, for example "Kürassier-Regiment Nr. 10 (Gensdarmes)" [S2].

A retired officer who died before or during the First World War belongs in the Imperial-officer route [S1]. If he could have been alive in August 1914, also open a casualty-list row until service evidence settles whether he was reactivated. If the period or rank class is uncertain, open one row for each possibility. Do not pick one.

**Scope of this recipe.** The routes below cover six combinations:

- Old-Prussian enlisted men and NCOs
- Imperial Prussian officers, active or retired
- First World War casualty-list and memorial entries
- First World War hospital-book episodes where the selected holding confirms coverage
- Wehrmacht soldiers
- Old-Prussian military church books for all ranks

There is no route here for:

- Old-Prussian officers
- Imperial enlisted men in peacetime
- full routes for personnel records of armies other than the Prussian one (for First World War rolls, see the list below)

Do not reuse the Prussian loss findings for those armies. Give each such man a row marked *route not covered here*. Find out which archive holds that state's records before you record any series as destroyed or searched. For Austro-Hungarian service of men from Galicia and Bukovina, see [Route a Galician or Bukovinian record by date, confession and custodian](galicia-bukovina-habsburg-record-routing.md), steps 5 to 8.

**First World War soldier of a non-Prussian army.** Write to the archive that holds that state's army records:

- **Bavaria:** Bayerisches Hauptstaatsarchiv, Abteilung IV Kriegsarchiv, Munich [S9]. Its Kriegsstammrollen (wartime muster rolls) of 1914–1918 are on Ancestry as "Bavaria, Germany, World War I Personnel Rosters, 1914-1918" [S10].
- **Württemberg:** Hauptstaatsarchiv Stuttgart [S9]. The Kriegsstammrollen are filed by unit, for example M 493 for the Landsturm infantry battalions, and some volumes are online [S11].
- **Baden:** Generallandesarchiv Karlsruhe [S9]. The Kriegsstammrollen of 1914–1918 are in 456 C and the Kriegsranglisten in 456 D [S11].
- **Saxony:** Hauptstaatsarchiv Dresden [S9]. Personnel lists of 1914–1918 survive in at least some units' files, so ask for the unit's finding aid [S13].

Most Prussian army files burned at Potsdam in 1945 [S9]. For a Prussian soldier, use the casualty lists and the hospital books (§ 4) instead.

## 2. Old-Prussian army (1714–1806): the Stammrollen are gone, so work from church books and the canton

- **Record the destroyed series first.** The Prussian Heeresarchiv in Potsdam was destroyed in the air raid of 14 April 1945. Treat the regimental Stammrollen (muster rolls), the key to a soldier's origin, as lost with it; a forum participant reported the loss [S2]. Mark them as *destroyed* and do not send a request for them. Expect no career record for an Old-Prussian enlisted man or NCO [S2]. The one exception is stray copies. A forum post transcribes part of a Stammrolle of the Regiment Prinz Heinrich von Preußen (1777/78) and gives the locator Pr. Geh. Staatsarchiv, Rep. 92 B V.1 [S6]. Write "Stammrollen destroyed with the Heeresarchiv; stray copies possible in the Geheimes Staatsarchiv (e.g. Rep. 92 B V.1, as cited)". Do not write "no roll exists anywhere".
- **Search the surviving military church books.** The military church books were not kept in the Heeresarchiv, so they survived. The originals are in the Geheimes Staatsarchiv PK, and filmed copies are on Ancestry within its German Protestant church book collections. Search them there, together with the Berlin church books, in both the database and the scans [S2]. Regiments and garrisons kept their own baptism, marriage and burial books, separate from the civil parish of the same town. A forum post cites the church book of the Regiment des Königs Nr. 18 under the Wehrkreis-Pfarramt Spandau [S6]. The marriage registers of the Regiment Prinz Heinrich von Preußen for 1756–1806 were the basis of an article by Friedrich Bengs in *Familiengeschichtliche Blätter* (1934–36) [S5]. Name the regiment or garrison congregation as the creator of the register.
- **Search the civil parish books as well.** A soldier's marriage can be in a village parish book instead. In the thread's example, the NCO's 1718 marriage was in an ordinary rural parish book on Archion, found through a Brandenburg database search. It named neither his parents nor his place of origin [S2].
- **For a marriage entry, record its type.** The published extract from the regiment's marriage registers lists entries as "banns or marriage consent" (Aufgebot oder Konsenserteilung), with origin and confession as stated [S5]. Record which type the entry is, or record that the publication does not say. A consent date is not a wedding date.
- **Use the canton as a ranked list of places to search, not as a birthplace.** Look up the regiment in Lyncker, *Die altpreußische Armee 1714–1806*:
  - A participant cited volume I, page 169: the canton of Kürassier-Regiment Nr. 10 was the Kreise Halberstadt, Jerichow and Prignitz, which had to supply young men to that regiment [S2]. The page number has not been checked.
  - Independent summaries of the regiment agree on the districts. They specify part of Kreis Jerichow and add the towns of Havelberg, Sandau and Hornburg.
  - List those districts and towns as search areas and rank them by any other clue. The participant's chance find of a baptism of the same rare surname in a Halberstadt Reformed congregation in 1755 raises that district's rank but proves nothing [S2].
  - Two finding aids are worth knowing. A participant pointed to a FamilySearch catalogue item titled *Die altpreußische Armee 1714–1806 und ihre Militärkirchenbücher* [S2]. Wolfgang Eger's *Verzeichnis der Militärkirchenbücher in der Bundesrepublik Deutschland* (Neustadt/Aisch; vol. 1 1993; vol. 2 1996, covering the new federal states and the Roman Catholic church) indexes military church books by holding [S7]. Check the holdings either one lists before you rely on it.
- **Expect a move into civil service, and treat any link to it as a hypothesis.**
  - A participant said it was the rule for discharged soldiers to be taken into state service (as a "Civilbedienter"). He knew of no explicit Berlin lists of such men [S2].
  - A Geheimes Staatsarchiv file records a 1748 house grant to the widow of an armoury clerk (Zeugschreiber) with the same rare surname. It was offered only as a possible identity, because of the rarity of the name and the military link [S2].
  - Keep it as a proposed link until the person-level details agree.

## 3. Imperial officers, active or retired: gazette, chronicle, then a death window

- **Militär-Wochenblatt.** The Militär-Wochenblatt began in 1816. It published promotions, transfers and deaths of active and retired officers. A participant gave its span as 1843–1926, but that is the run of its supplement, the *Beiheft zum Militär-Wochenblatt*, not the paper itself [S1]. Open the half-year volume's table of contents and go to its section "Biographisches", which lists the personnel notices, then turn straight to the page; a participant showed this layout [S1]. The same participant said in 2025 that volumes after 1908 were not online [S1]. Treat that as a dated availability report, not a present cutoff. Verify the actual volume and image access in each catalogue; neither a journal title nor a search hit establishes a complete digitised run. Before you mark a volume *not available online*, check the Deutsche Digitale Bibliothek, the Elbląg library, UB Potsdam and the Internet Archive. Record which volumes you actually opened and where.
- **Regimental chronicle and Ehrentafel.** In the thread, a 1910 regimental chronicle supplied the promotion date, the transfer as company commander and the date he left the army [S1]. The same chronicle also records an earlier campaign (China, 1900/01) from before his time in that regiment [S1]. Check the chronicle of every regiment he served in, not only the last one. The roll of the fallen (Ehrentafel) in a First World War regimental history has limited coverage, so his absence from it only rules out what that roll covers [S1]. The GenWiki page for a regiment can list digitised regimental histories [S1].
- **Reichsanzeiger.** The *Deutscher Reichsanzeiger und Preußischer Staatsanzeiger* (1871–1945, digitised by UB Mannheim) is on the Deutsches Zeitungsportal. In the thread it confirmed the transfer notice [S1]. Cite the issue and date of each notice.
- **Bound the death window.** Use the date he left the army as the earliest bound. Treat the address book as a sighting, not as a bound on the death: in the thread he was listed as "Hauptm. a.D." in 1912 and was missing from both the name section and the street section in 1913 [S1]. Search newspaper death notices from the last listing through the first inspected absence and into the years after it, because a disappearance is not a death ([city-directory workflow](city-directory-observation-workflow.md)). Take a latest bound only from dated death or widowhood evidence. Search the Deutsches Zeitungsportal, where the researcher found the notice in the *Norddeutsche Allgemeine Zeitung* [S1], and the Staatsbibliothek zu Berlin's ZEFYS, which also holds that paper.
- **Read absences narrowly.** If you find no identifiable entry for him in the First World War Verlustlisten (casualty lists), record exactly that. A participant inferred from the miss that he did not die as a reactivated soldier [S1], but a miss does not exclude reactivation or a wartime military death. Settle reactivation from service evidence before you close the casualty-list route. The same participant mentioned roughly quarterly death lists of active and former officers, but did not know whether they continued up to or through the war. Check their coverage before you count a miss [S1].
- **Civil death registers.**
  - A death is registered at the registry office for the place where it happened (§ 28 PStG). A death while travelling or at a spa is therefore registered there, not at the home address. [S14] A participant made the same point [S1].
  - For a fallen soldier, also search the registers of his birthplace and last residence; the same participant said such deaths are often registered there instead [S1].
  - The continuation period for death registers is 30 years (§ 5(5) PStG); after it ends, § 7(3) requires the records to be offered to the responsible public archive under its archival rules. Confirm the actual custodian rather than assuming a transfer is complete. Access during the continuation period follows § 62 PStG; establish which applicant category applies before requesting an entry. The Sonderstandesamt Bad Arolsen death-register continuation period is 80 years. [S14]
  - A widow's later marriage file may not contain the proof of the first husband's death. In the thread it held only the banns, and a participant thought the supporting documents had been handed back [S1].

## 4. First World War casualty lists and memorials: check for a namesake, then check the script

Search the German casualty lists in CompGen's free name index of the *Deutsche Verlustlisten* 1914–1919 at des.genealogy.net. Volunteers entered over 8.5 million entries from the printed lists, recording the name and the birthplace [S16 @2026-11-12]. Search by name. Each result names the list it came from, for example "Preußen 665" or "Bayern 427", and gives a status such as *gefangen* (captured), the list date and a link to the scanned page [S17 @2026-11-12], [S18 @2026-11-12], [S19 @2026-11-12]. It gives the regiment only where the printed list did: from 1916 until the end of the war the lists omitted it [S20 @2026-11-12]. Open the scan before you record the entry.

Expect several entries for one man. A later list can print his name again under *Berichtigung früherer Angaben* (correction of earlier information) with a new status [S18]. The researchers of a study built on this index used machine learning to merge possible repeat entries for the same person, CompGen reports [S15]. Collect every entry under his name and place, and record each list number, date and status as a separate episode before you call him wounded, captured or fallen. Treat the place as a lead to the birth register, not as his birthplace.

- When a casualty list or memorial gives a different given name from the man in the registers, search the local family book (OFB) **and** the register indexes around the stated birth year for any other man of that name before you split or merge the entries [S3]. In the thread:
  - The documented man had given name A and was born in 1893.
  - One list gave a different given name B, born 1893, killed 1916.
  - Another list gave name A, born 1894, from his wife's village, wounded 1915.
  - The village memorial gave the Hungarian form of name B.
  - No other man of name A or name B with that surname appeared around 1893 in the family books or the register indexes [S3].
- Then check whether a misreading of Kurrent (the old German handwriting) explains the difference. A participant explained that in carelessly written Kurrent an "s" can be read as "h", so the abbreviated stem of one given name is read as the stem of another and expanded to the wrong full name [S3]. Memorials can also give names in a different language form.
- A one-year difference in birth year, or a mismatch between birthplace and residence, ranks a candidate lower but never excludes it. Record the wounding and the death as separate episodes ([episode discipline](russian-military-repression-record-episodes.md)).
- Write the result as an inference ("probably the same man; no namesake found in [books searched] for [years]"). The same thread shows family books disagreeing with each other and with the registers on names and dates, so record which ones you checked [S3]. Leave the identity ruling to [evidence/proof judgment](evidence-proof-judgment.md).

### When a First World War personnel file is missing: seek a hospital-book episode

A lost personnel file need not end a service inquiry. The 2022 Bundesarchiv presentation
describes surviving Krankenbuchlager material and *Lazarettbücher* that can document
particular hospital stays [S8]. Select this route for the period and holding actually
confirmed by the custodian; it does not extend the Prussian loss findings to other armies.

The surviving books of the Krankenbuchlager Berlin, which held the hospital books of
Prussian soldiers, are in the Bundesarchiv (Abteilung PA). The depots for the other armies
in Dresden, Stuttgart and Munich were destroyed in the Second World War, but the same Bundesarchiv page
says the Munich books were moved to Berlin in 1964 [S12]. For a Bavarian soldier, ask the
Bundesarchiv whether a hospital book survives before you record the route as destroyed.

1. Give the archive the independently supported name, birth details and any hospital,
   unit or date clues you have. Ask which surviving hospital book or associated finding
   reference could cover that episode, who now holds it and what the current request
   terms require. Preserve the reply and book/entry reference separately from the
   missing personnel-file result.
2. Request the identified entry. The presentation describes collective pages containing
   several patients, with scans sometimes masking other people's entries [S8]. Ask for
   the relevant entry under the custodian's reproduction conditions; a collective page
   is not automatically available in full.
3. Extract the fields actually present: identity or identification-tag detail, incoming
   unit, admission date, hospital, diagnoses, named relatives and discharge or transfer
   destination. Keep a return-to-duty entry and its named unit as a separate dated
   observation. The presentation describes these possible fields, not a standard form
   or a promise that every entry contains them [S8].
4. Use an actual transfer, hospital or unit reference to select the next record to ask
   about. Compare the person across the linked entries before joining the episodes;
   preserve conflicting dates and unresolved names. A relative named in the book is
   a recorded relationship claim to test, not an identity ruling.
5. Return the book/entry locator, inspected extract, dated admission/discharge/transfer
   observations and remaining gaps. A hospital stay establishes only the episode the
   record documents, not continuous service or a complete military history.

## 5. Wehrmacht: personnel and loss documents first, then unit records

- **Request the man's documents from the Bundesarchiv.** The WASt (Deutsche Dienststelle) holdings became part of the Bundesarchiv on 1 January 2019, initially as department PA. Send the request to the Bundesarchiv, addressed to the department its current guidance names for pre-1945 military personnel records. These records give personal details, including unit information. A participant advised asking for them because they may also give the birthplace, division and regiment [S4]. Log this request on its own. It is not the same as a Volksbund query.
- **Keep the Volksbund entry as a separate lead.** In the same thread, the researcher had asked the Volksbund (the German war graves commission) which source its birth data came from. There was no reply after two to three months [S4]. A grave-register birth date is not a birth record, and its source stays unknown until the Volksbund answers.
- **Use the unit to choose unit records.** NARA's captured German records on microfilm are arranged by unit, mainly by division. For example, T315 is Records of German Field Commands: Divisions. Start from the division and work down to the regiment, and look in the regiment's records for daily orders (Tagesbefehle), as a participant advised [S4]. Unit records may not name the man. Record what the unit did, and do not assign the unit's events to him unless his name appears.
- **Find comrades from the same event.** Ancestry's collection "Deutschland, im Kampf gefallene Soldaten, 1939-1948" consists of index cards derived from WASt records. In the thread, a search by regiment, company and date found several men of the same company killed on the same day. The cards gave a place, a grave location (a numbered comrades' grave in a community cemetery) and a cause of death [S7]. Record each card's place wording exactly. In that case the place was a locality on the Soviet (Lithuanian SSR) side of the border, and the civil death certificate gave the place only as reported [S7]. Identify each place name before you put it on a map.
- **Treat a postwar civil document's birthplace as a weak lead.**
  - In the Wehrmacht thread, the birthplace came from a 1949 marriage extract made far from Silesia, where the registrar probably struggled with place names. A participant said a second documentary mention of the birthplace was needed [S4].
  - The candidate places tested gave no baptism or birth entry [S4]. They were an Upper Silesian Josefsdorf, three places named Josefsdorf in West Prussia, and four places named Józefin in present-day Ukraine.
  - List each candidate place you tested and its result.

## Output

1. **Routing table:** one row per period, army and rank-class route. For each series give its status: *destroyed*, *surviving and searched*, *surviving but not online*, *not yet asked*, or *route not covered here*, with the locator or URL used.
2. **Canton list:** the districts and towns from Lyncker with volume and page, ranked, each labelled as a search area.
3. **Notices:** Militär-Wochenblatt year, half-year, page and the digital library used; chronicle title, edition and page; Reichsanzeiger issue and date.
4. **Death window:** earliest bound (leaving the army), the last address-book listing and the first inspected absence, any latest bound with the dated death or widowhood evidence behind it, and the newspapers and registers searched, with each register's place of death and access status.
5. **Casualty-list identity notes:** the namesake search (books, indexes, years), any script or language confusion considered, and the inference as worded.
6. **WWII leads:** Bundesarchiv request log (department addressed and date), Volksbund query and reply status, regiment and division, and NARA unit-record leads (microfilm series and unit). Keep these separate from personal documents.
7. **Hospital episodes:** custodian reply and current request terms, hospital-book and entry references, inspected or restricted reproduction, actual admission/discharge/unit/transfer fields, and unresolved links between episodes.
