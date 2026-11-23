---
id: "amsterdam-archival-record-recovery"
title: "Recover and read an Amsterdam City Archives register entry"
summary: "Follow an Amsterdam City Archives index hit, tree claim or burial card back to its own register entry."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "AMSTERDAM-ARCHIVAL-RECORD-RECOVERY-01", "text": "Read the entry by its register type, not by the index label."}]
handoff: ["dutch-civil-church-record-recovery"]
checked: "2026-11-04"
checked_basis: "opened 2026-11-04"
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"section": "Records by country and region", "group": "Western and Northern Europe", "order": 139}
---

# Recover and read an Amsterdam City Archives register entry

Use this recipe when you need to follow something back to the entry in its own register. That something can be an Amsterdam City Archives (Stadsarchief) index hit, a failed name search, a tree claim, a Beth Haim burial card or a population-register line. Each register type has its own meaning. Typical cases are an ondertrouw (marriage-intention) entry, a population-register (bevolkingsregister) line, a doop entry, a burial card and an entry in a community inventory. Read the entry by its register type, not by the index label.

For the general rule that an intention or banns entry is not a marriage, use [evidence/proof judgment](evidence-proof-judgment.md). For machine-translation pitfalls in general, use [AI for documentary records](ai-for-documentary-records.md). Other neighbouring recipes:

- cemetery packets: [burial evidence packet](burial-evidence-packet.md)
- Hebrew-script spelling recovery: [name searches across scripts and OCR](corpus-seeded-name-search.md)
- browsing film images: [FamilySearch workflows](familysearch-practical-record-workflows.md)
- patronymic-to-surname hypotheses: [Jewish conditional hypotheses](jewish-genealogy-conditional-hypotheses.md)

## Contents

- Read the index hit before trusting it
- Fix the locator and the register's own rules
- Ondertrouw: a registration, not a wedding
- Population register: a running household ledger
- Civil-period follow-ups
- Portuguese-Jewish material before and after 1811
- Close with a register-entry packet

## Read the index hit before trusting it

- **Check who the index hit names.** A 1799 Portuguese-Jewish birth entry returned for Jacob Nunes Vaz names him as the newborn’s father [S2]. Record the indexed person’s role before assigning the birth.
- **Search for children through a parent in the pre-1811 baptism index.** The register typically gives the child’s given names and the parents’ full names. Search the father and mother separately by surname, then narrow the results by the child’s given name [S1], [S21], [S26].
- **Search variant spellings.** Try IJ/Y, C/K or S/Z and keep the original readings. The archive’s search help uses `me*er` to retrieve forms including Meijer and Meter [S1], [S2], [S25].
- **Copy names from the Dutch page before translating interface labels.** A browser translated Jan Jong as “John Young” in one demonstration [S1], [S6].
- **Check a double surname against the image, the signature and the parents’ entry.** One indexer joined a given name taken from the mother’s maiden name to the child’s surname [S1]. Search the two readings separately.

## Fix the locator and the register's own rules

Follow every hit to the image. Record these separately:

- the archive (access) number
- the inventory number and any sub-number
- the image or page

Archive 334 is the archive of the Portuguese-Israelite (Portuguese Jewish) community. Its numbering is the usual model: inventory numbers, then sub-numbers. A collection can be a sub-part of another archive [S2].

Before you interpret entries, read the inleiding (introduction) or PDF inventory for scope. For population registers, read the register's example and instructions pages [S2]. The registers run in periods: 1851–1853, 1853–1863, 1864–1874 and 1874–1893. House numbers in the 1853–1863 register are not modern addresses. They were numbered by neighbourhood (A–ZZ), and the city renumbered them in 1875. Keep the period house number separate from any modern address. Expect community material in Portuguese, Hebrew or other languages, not only Dutch [S2].

## Ondertrouw: a registration, not a wedding

- **Record the ondertrouw date as registration of the intention.** The banns followed over three Sundays, allowing objections. Look separately for the ceremony in the appropriate marriage register or ketubah [S2], [S9], [S22], [S26].
- **Read the margin of a struck-through intention.** Follow a reference to an objection or a refusal of parental consent. *Niet gecompareerd* means the couple did not appear to sign. Check for a later application in Amsterdam or elsewhere before drawing a conclusion about the marriage [S1], [S22].
- **Compare repeated hits by date, series, image and signatures.** The index can include both the clerk’s spelling and a signature, a cancelled application and a fresh one, or a mixed couple registered in both church (*kerk*) and town-hall (*pui*) series [S1], [S22].
- **Do not read the series as proof of religion.** Up to June 1795, search both the church and pui series. From 6 June 1795 to 1811 there is only one series [S18]. In the 17th century, Sephardic Jews often used a former Iberian Christian name alongside their Jewish name, so one person can appear under two names in different records [S17], [S18]. Link two names only through an explicit alias statement, such as an ondertrouw entry, a settlement or an estate division, or other documented evidence that they identify the same person. Otherwise keep the link unresolved.
- **Extract every field on the image.** The Stadsarchief lists birthplace, age, marital status, residence and witnesses [S22]. Also look for
  - origin ("van …")
  - any parent the party lived with
  - prior spouse
  - each witness's stated relationship
  - signature or mark, including Hebrew-script signatures [S1], [S2], [S10], [S11]

  Record the clerk's spelling and the party's own signature as two separate attested forms. The signed form can point to the place of origin [S1], [S2].
- **Treat an assisting relative as a role, not proof of parentage.** An ondertrouw entry names whoever appeared to assist each party, and the relationship it gives can be wrong or can belong to a stand-in [S17]. Before you add a named parent, check for a burial entry showing an earlier death, and for later deeds that name the relationship.
- **Follow a widowed party back to the first marriage.** Age was recorded only at a first marriage. If the intention says a party was widowed, look for the intention of the named previous marriage. Repeat until you reach a first marriage. S1's presenter adds that widowed parties' later intentions usually also lack a birthplace, which the first marriage gives [S1].
- **Link a patronymic to a later surname through family records.** Under the 1811 decree, people who lacked a family name had to adopt one. Search the earlier intention by patronymic and origin, then compare the spouse and relatives with the later records. A groom recorded by patronymic in 1793 later appears with an added surname [S8], [S27].

### Follow a remarriage clearance into orphan-chamber records

Use this branch when a widowed party's intention has an orphan-chamber (*Weeskamer*)
note, or when an earlier household remains incomplete because its first-marriage
ketubah is missing. The two Sephardic Genealogy lectures follow marriage-ban
marginalia into chamber declarations, guardian appointments and later discharges
[S15], [S16]. These are municipal records: do not restrict the search to the
Portuguese-Jewish community's archive 334 or assume the route applies only to Jews.
Check the chamber's actual finding aid, period and surviving series before searching.

1. **Copy the clearance note.** Record the marginal wording, date, locator, widowed party and previous spouse. The formula *hij/sij weeskamer voldaan* points to arrangements for minor children’s inheritance before remarriage. Look for the chamber entry before recording any payment, and for the marriage entry before recording a wedding [S16], [S22], [S23].
2. **Follow the chamber’s own index to the entry.** In archive 5073, consult inventories 835–883 (1509–1840) or 3964–3971 (1468–1656). Depending on the index, look under the children or the deceased parent. Take the leaf number to the volume covering the same period in inventories 772–834. Record the volume, leaf, side and image, and compare the surviving parent, deceased spouse and children with the intention [S23].
3. **Extract each child, including adults who have married.** Record ages as of the declaration date, shares, recipients and stated relationships. One account lists children aged 12 to 22 and identifies a brother-in-law through a married daughter [S15].
4. **Follow the guardians through replacements and discharge.** Search the appointment registers for the named people and period. Record the date, locator, roles and account references for each appointment, replacement and review. Establish deaths, birthdays and kinship from records that give them [S16].
5. **Separate the roster from the estate balance.** The chamber can record a maternal inheritance even when the first-marriage ketubah is missing. Enter the amount and recipient, and leave the original contract terms open [S15]. One declaration named five children while reporting no means to declare [S16].

The chamber's own records are Stadsarchief archive 5073 [S20]. The chamber registered
each orphan's inherited share and held it until the child came of age at 25 [S17], [S19].
If a share was paid out earlier, look for a declaration of majority (*venia aetatis*).
The States of Holland, and sometimes a city, granted it after the minor applied to the
local authority with a baptism or birth certificate, on statements from that authority,
relatives and guardians. Those registers are at the Nationaal Archief, not the
Stadsarchief: States of Holland archive 3.01.04.01, with petitions from 1652 to 1795 at
inventory numbers 2085–2191 (indexed to 1700) and registers of grants at 2192–2193. For
1801–1802, see the Hof van Holland archive 3.03.01.01, inventory number 4883 [S19].

Before treating a chamber miss as evidence, read any surviving will for named guardians, executors and a clause excluding chamber intervention. Record the clause or the status of the will search, and keep the search for children open [S16], [S29].

Copy **uncle** literally when a guardian is described that way. One appointment leaves open whether he was related to the deceased wife or the surviving husband [S16]. Record a family side only when the documents identify it.

Add the linked records to the register-entry packet:

| Record | Keep beside its own locator |
| --- | --- |
| Marriage intention | Prior spouse, literal clearance note, dated context and unresolved reading |
| Chamber declaration or account | Children and stated ages, maternal-estate wording, amount/share or no-means statement |
| Appointment and later discharge | Named roles, action dates, changes of guardian and referenced accounts |
| Will, if located | Actual appointments or exclusion wording and its inspection status |

Report which links were recovered and which remain unsearched, unavailable or
unresolved. These lectures supply the retrieval sequence and narrated examples;
the underlying chamber entries and missing ketubah have not been inspected here.

## Population register: a running household ledger

- **A crossed-out name means the person left the household, not that they died**, unless the entry says death. Record the departure date and destination beside each person as a separate observation. Keep other family groups on the same sheet apart [S2], [S3], [S6].
- **Read each stay at the same address.** A child appears only during the family’s second stay in a demonstrated register [S1]. Compare the entry and departure dates for each person across both stays.
- **Compare the wife’s birth year with each child’s birth.** One register lists a later wife who was too young to be the mother; the marriage supplements identified the mother [S1]. Seek the civil birth or the couple’s supplements before assigning parentage.
- **Use the household dates to locate civil acts.** Compare each date with the birth, marriage or death entry and retain the discrepancy with both locators [S1].

## Civil-period follow-ups

Civil registration began in Amsterdam in 1811 [S13], [S14]. Do not give 1811 as the national start; for regional start dates use [Dutch civil and church record recovery](dutch-civil-church-record-recovery.md).

- **Browse unindexed civil births from the register date.** Where civil births are not indexed, take the population-register birth date and browse the civil birth images a few days on either side [S1].
- **Check both register sets on a film before reporting "not found".** Per S1's presenter, some films hold two register sets covering the same period, and a birth may appear in only one of them [S1].
- **Retrieve the huwelijksbijlagen (marriage supplements) as well as the marriage act.** They can hold birth extracts, military-service certificates and the parents' death records. Per S1's presenter, they also record the witnesses [S1].

## Portuguese-Jewish material before and after 1811

- **When the name index fails before 1811, browse archive 334.** Do not conclude the person is absent. Browse the community's member registers (births, circumcisions, marriages, deaths) [S3], [S4].
- **Check both arrangements of the birth registers.** In one search, the alphabetical list under the child’s given name supplied the father, while the chronological entry for the same birth gave the mother’s name and patronymic [S4]. Use the first entry’s date to locate and cite the second.
- **Identify the event on the image under a *doop* (baptism) index label.** The index includes Portuguese-Jewish birth registers from 1736. For Hebrew-language Ashkenazi births, use the archive’s separate guide to surviving birth and circumcision registers [S2], [S21], [S24], [S29].
  - Record the register label and the event type separately.
  - Take the birth date from the birth entry.
  - Look for the circumcision in the separate circumcision registers (archive 5001) or in the community's own registers in 334.
  - Copy both Hebrew and Gregorian dates when the register gives them. The 1799 entry also carries the year 5559 [S2].
- **Follow Beth Haim cards back to the underlying records.** Archive 334 inventories 500A–500M are a 1960 card index to the Ouderkerk burial register for about 1700–1850 [S28]. The presenter found entries in the inventories for people missing from the cards [S5].
  - Take the register, folio and number from a card and verify the event and relatives in the referenced burial, marriage or circumcision entry [S5].
  - Rebuild child lists year by year from the birth registers.
  - Search each surname component, birth and married names, and recorded aliases as separate keys. S3's presenter shows the Beth Haim database splitting Sephardic names into first and second family-name fields [S3].
  - Absence from the cards does not show that the person did not die in Amsterdam. Check the inventories and payment entries for burials, and consider a death elsewhere [S5].
- **Date the last appearance in the matzah-baking lists.** Browse successive years in archive 334 under both name orders. If a death elsewhere is suggested, check the death register there. After the Amsterdam list entries ended, a presenter traced a tree’s Livorno lead to a March 1742 entry in its Jewish death register [S7], [S28].
- **Index spellings by writer.** Keep the community’s and the Dutch clerk’s forms as separate search keys and cite the record for each, including variants such as *Barzilay* and *Barzilaij* [S2], [S12].

## Close with a register-entry packet

Return the following:

- **Locator:** archive, inventory and sub-number, image, and the register type with its literal meaning (intention, household ledger line, doop label vs reported birth, compiled card).
- **Extracted fields:** parties, roles, origins, ages, residences, witnesses and relationships, and signatures, with each spelling attributed to its writer.
- **Events kept apart:** intention, marriage, birth, circumcision and burial as distinct events.
- **Dated departures and last appearances.**
- **Gaps:** the registers, parallel series, objection registers, film sets and supplements not inspected.

An entry located this way is evidence to correlate, not an identity ruling.
