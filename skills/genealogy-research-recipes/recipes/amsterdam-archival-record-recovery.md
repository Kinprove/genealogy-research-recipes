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
router: {"tier": "pointer", "group": "Church and civil registers", "order": 1055}
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

- **Check the role column of every hit.** The name shown can be the father's rather than the child's. In S2's example, a doop hit that looked like a man's 1799 birth was really his son's entry [S2].
- **Search for children through a parent in the pre-1811 baptism index.** The Stadsarchief's guide says these registers give the child's given names and the parents' full names. S1's presenter states that the index carries no surname for the child [S1]. So search by a parent's surname in the father or mother role, one parent at a time, and add the child's given name if you know it. A child's name will not lead you to the parents [S1].
- **Expand spellings on purpose.** Clerks wrote surnames by sound, even for people who could write [S1], [S2]. Use wildcards to cover variants such as IJ/Y, C/K and S/Z. The archive's current search help documents the `*` wildcard (for example R*eboom). In 2019, S2's presenter also used a phonetic option labelled "ongeveer" [S2]. Check whether the current interface still offers it.
- **Search and read the original Dutch pages, not machine-translated ones.** In the presenters' demonstrations, browser translation changed the name Jan Jong to "John Young" [S1] and Dahan to "Rooster" [S6]. Translate only the interface labels, and do that separately.
- **Treat an index-only gap as a lead.** In S1's example, the indexer merged a given name into the surname, which made it look like a double surname. The given name had been taken from the mother's maiden name. Check the image, the person's signature and the parents' entry [S1].

## Fix the locator and the register's own rules

Follow every hit to the image. Record these separately:

- the archive (access) number
- the inventory number and any sub-number
- the image or page

Archive 334 is the archive of the Portuguese-Israelite (Portuguese Jewish) community. Its numbering is the usual model: inventory numbers, then sub-numbers. A collection can be a sub-part of another archive [S2].

Before you interpret entries, read the inleiding (introduction) or PDF inventory for scope. For population registers, read the register's example and instructions pages [S2]. The registers run in periods: 1851–1853, 1853–1863, 1864–1874 and 1874–1893. House numbers in the 1853–1863 register are not modern addresses. They were numbered by neighbourhood (A–ZZ), and the city renumbered them in 1875. Keep the period house number separate from any modern address. Expect community material in Portuguese, Hebrew or other languages, not only Dutch [S2].

## Ondertrouw: a registration, not a wedding

- **Record the intention date as the date of a public announcement of an intended marriage, not as the ceremony.** The announcement was made so that objections could be raised [S2], [S9], [S11]. Find the marriage, ketubah or civil act separately.
- **Check whether the intention was crossed out or rejected.** Read the marginal note. Per the Stadsarchief, these notes can point to a separate register of objections or of refusals of parental consent. Open that register as well. S1's presenter shows the index marking a struck-through intention. In S1's example the intention was stopped because the couple were too closely related. Expect the couple to register again later [S1].
- **Do not count two registrations of one couple as two marriages.** Church (kerk) and city-hall (pui) ondertrouw series both exist. Per S1's presenter, one couple can appear in both the Dutch Reformed church register and the pui register. Treat these as duplicate registrations of one couple [S1].
- **Do not read the series as proof of religion.** Up to June 1795, search both the church and pui series. From 6 June 1795 to 1811 there is only one series [S18]. In the 17th century, Sephardic Jews often used a former Iberian Christian name alongside their Jewish name, so one person can appear under two names in different records [S17], [S18]. Link two names only through an explicit alias statement, such as an ondertrouw entry, a settlement or an estate division, or other documented evidence that they identify the same person. Otherwise keep the link unresolved.
- **Extract every field on the image.** The Stadsarchief lists birthplace, age, marital status, residence and witnesses as standard fields. The presenters' images also show:
  - origin ("van …")
  - any parent the party lived with
  - prior spouse
  - each witness's stated relationship
  - signature or mark, including Hebrew-script signatures [S1], [S2], [S10], [S11]

  Record the clerk's spelling and the party's own signature as two separate attested forms. The signed form can point to the place of origin [S1], [S2].
- **Treat an assisting relative as a role, not proof of parentage.** An ondertrouw entry names whoever appeared to assist each party, and the relationship it gives can be wrong or can belong to a stand-in [S17]. Before you add a named parent, check for a burial entry showing an earlier death, and for later deeds that name the relationship.
- **Follow a widowed party back to the first marriage.** Age was recorded only at a first marriage. If the intention says a party was widowed, look for the intention of the named previous marriage. Repeat until you reach a first marriage. S1's presenter adds that widowed parties' later intentions usually also lack a birthplace, which the first marriage gives [S1].
- **Link pre-1811 Ashkenazi patronymics to later surnames.** Ashkenazi parties usually appear under patronymics until surnames were adopted under Napoleonic rule in 1811. Treat the link between a patronymic form and the later surname as a hypothesis. Do not search only under the later surname. S8's example is a 1793 intention whose groom later carries an added surname [S8].

### Follow a remarriage clearance into orphan-chamber records

Use this branch when a widowed party's intention has an orphan-chamber (*Weeskamer*)
note, or when an earlier household remains incomplete because its first-marriage
ketubah is missing. The two Sephardic Genealogy lectures follow marriage-ban
marginalia into chamber declarations, guardian appointments and later discharges
[S15], [S16]. These are municipal records: do not restrict the search to the
Portuguese-Jewish community's archive 334 or assume the route applies only to Jews.
Check the chamber's actual finding aid, period and surviving series before searching.

1. **Preserve the starting note.** Copy the complete marginal wording or abbreviation,
   its date if supplied, the intention's locator, the widowed party and the named
   previous spouse. Keep an uncertain reading unresolved. In S16, the presenter reads
   the note as satisfaction of the orphan chamber; that is a lead to the chamber's
   record, not a statement that the wedding took place or that money was paid.
2. **Find and check the chamber entry.** Use the supported names, dated remarriage
   context and any explicit reference to search the relevant chamber register or
   index. Preserve its own archive, inventory, folio and image locator. Compare the
   surviving parent, deceased spouse and children actually named before linking it
   to the intention. A clearance note need not contain a complete chamber locator;
   an unlocated entry remains an open target rather than a reconstructed account.
3. **Extract the earlier household from the account or declaration.** Record each
   child separately, with the age as stated and the date of that statement. Copy
   maternal-estate wording, amounts or shares and named recipients exactly. Retain
   adult or married children and any stated spouse or sibling relationship; the
   relevant roster need not consist only of minors in the parent's later household.
   S15 reports children aged 12 to 22 and a brother-in-law connected to an already
   married daughter. That supplies an extraction target, not verified people for
   another tree or a complete list of every child.
4. **Follow appointments beyond the first entry.** Locate the separately described
   guardian-appointment register for the supported people and period. Copy each
   appointment, replacement, account reference and discharge with its own date and
   locator. Use later entries to test the earlier roster: S16 follows replacement
   guardians and a later review of their administration. Keep guardian, child,
   reviewer and estate representative as separate roles; a replacement or discharge
   does not by itself establish a death, exact birthday or new family relationship.
5. **Reconcile the money without inventing the missing ketubah.** A chamber statement
   that the children received their mother's inheritance can recover a dated estate
   observation even when the first-marriage contract is unavailable. It does not
   recover that contract's terms or establish where the money originated. S15's
   suggested connection to an earlier marriage provision remains a hypothesis.
   S16 also shows a declaration naming five children while reporting no means to
   declare. Keep a named child roster separate from a positive cash balance.

The chamber's own records are Stadsarchief archive 5073 [S20]. The chamber registered
each orphan's inherited share and held it until the child came of age at 25 [S17], [S19].
If a share was paid out earlier, look for a declaration of majority (*venia aetatis*).
The States of Holland, and sometimes a city, granted it after the minor applied to the
local authority with a baptism or birth certificate, on statements from that authority,
relatives and guardians. Those registers are at the Nationaal Archief, not the
Stadsarchief: States of Holland archive 3.01.04.01, with petitions from 1652 to 1795 at
inventory numbers 2085–2191 (indexed to 1700) and registers of grants at 2192–2193. For
1801–1802, see the Hof van Holland archive 3.03.01.01, inventory number 4883 [S19].

Before using a chamber miss, check any located will for the executors, guardians
and chamber-exclusion wording it actually contains. S16 describes wills that
excluded chamber intervention; this is a reason to inspect the will, not a
universal legal rule or an explanation for every absent entry. Record whether a
will was inspected, unavailable or not yet located. Neither a chamber miss nor a
declaration reporting no means establishes that there were no children.

Keep an unspecified **uncle** unspecified. In S16, the presenter cannot determine
whether the named uncle belongs to the deceased wife's family or the surviving
husband's. Preserve the literal relationship and the person to whom it refers,
where stated; leave the family side open. Appointment as guardian does not resolve it.

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
- **Open every residence entry for the household**, including repeated stays at the same address. In S1's example, a child appeared only at the second stay [S1].
- **Check the mother's birth year against the children's births before assigning children to her.** In S1's example, the listed wife was a later wife, born too late to be the mother. The marriage supplements settled who the mother was [S1].
- **Treat population-register dates as clues.** S1's presenter reports finding many errors in them [S1].

## Civil-period follow-ups

Civil registration began in Amsterdam in 1811 [S13], [S14]. Do not give 1811 as the national start; for regional start dates use [Dutch civil and church record recovery](dutch-civil-church-record-recovery.md).

- **Browse unindexed civil births from the register date.** Where civil births are not indexed, take the population-register birth date and browse the civil birth images a few days on either side [S1].
- **Check both register sets on a film before reporting "not found".** Per S1's presenter, some films hold two register sets covering the same period, and a birth may appear in only one of them [S1].
- **Retrieve the huwelijksbijlagen (marriage supplements) as well as the marriage act.** They can hold birth extracts, military-service certificates and the parents' death records. Per S1's presenter, they also record the witnesses [S1].

## Portuguese-Jewish material before and after 1811

- **When the name index fails before 1811, browse archive 334.** Do not conclude the person is absent. Browse the community's member registers (births, circumcisions, marriages, deaths) [S3], [S4].
- **Find the mother in a second birth register.** S4's presenter worked from a birth register in 334 arranged alphabetically by given name, which named only the father. A parallel chronological register for the same date gave the mother's name and patronymic. Record both entries [S4].
- **A "doop" (baptism) label on a Jewish entry is not a baptism, and it is not a circumcision record either.** Jews were not baptised. The Stadsarchief's guide to the pre-1811 baptism index includes the Portuguese-Israelite community's birth registrations but not the Hebrew-language Ashkenazi (Hoogduits) birth registers. In 1811 the Portuguese Jews handed in birth registrations for boys and girls going back to 1736. S2's 1799 Nunes Vaz hit reads as such a birth entry [S2].
  - Record the register label and the event type separately.
  - Read the date as a reported birth.
  - Look for the circumcision in the separate circumcision registers (archive 5001) or in the community's own registers in 334.
  - Portuguese-Jewish registers carry both Gregorian and Hebrew years (S2's example shows 5559 beside 1799). Use both when browsing [S2].
- **Treat Beth Haim burial cards as a later compilation that contains errors.** The cards were compiled from community records, and index cards survive as inventory 500A–500M in 334. S5's presenter adds that some people found in the inventories are missing from the cards [S5].
  - Follow each card's register/folio/number reference to the underlying circumcision, marriage or burial entry. S5 demonstrates this [S5].
  - Rebuild child lists year by year from the birth registers.
  - Search each surname component, birth and married names, and recorded aliases as separate keys. S3's presenter shows the Beth Haim database splitting Sephardic names into first and second family-name fields [S3].
  - Absence from the cards does not show that the person did not die in Amsterdam. Check the inventories and payment entries for burials, and consider a death elsewhere [S5].
- **Use dated administrative lists for a last appearance, not a death date.** The 334 finding aid has a matsebet (matzah bakery) section. S7 reads the community's lists of people admitted to matzah baking year by year, matching reversed name orders [S7]. A last appearance there is not a death date. S7's presenter then checked a tree's death-place claim against a death register at the proposed place [S7].
- **Keep the community's surname spelling and the Dutch clerk's spelling as separate attested forms.** S12's example is Barzilay vs Barzilaij. Do not normalize to the civil form [S2], [S12].

## Close with a register-entry packet

Return the following:

- **Locator:** archive, inventory and sub-number, image, and the register type with its literal meaning (intention, household ledger line, doop label vs reported birth, compiled card).
- **Extracted fields:** parties, roles, origins, ages, residences, witnesses and relationships, and signatures, with each spelling attributed to its writer.
- **Events kept apart:** intention, marriage, birth, circumcision and burial as distinct events.
- **Dated departures and last appearances.**
- **Gaps:** the registers, parallel series, objection registers, film sets and supplements not inspected.

An entry located this way is evidence to correlate, not an identity ruling.
