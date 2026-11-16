---
id: "maiden-name-recovery"
title: "Recover a woman's maiden name behind her married name"
summary: "Find a woman's birth surname when records give her husband's, through marriage, children's, census, newspaper, probate and U.S. Social Security records and Italian, Chinese and Japanese naming customs."
kind: "records"
scope: {"platforms": [], "tasks": ["bride married as a widow under an earlier husband's surname", "mother-in-law or brother-in-law in a census household", "Chinese woman recorded as Shee", "GRO birth index mother's maiden name", "SS-5 or NUMIDENT copy for a deceased woman"]}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "MAIDEN-NAME-RECOVERY-01", "text": "A bride's surname on a marriage record is the name she used at that marriage."}, {"id": "MAIDEN-NAME-RECOVERY-02", "text": "Search her Italian civil records under her maiden name, never only under her husband's surname."}, {"id": "MAIDEN-NAME-RECOVERY-03", "text": "Read a name such as Leung Shee as a woman surnamed Leung, not as a given name."}, {"id": "MAIDEN-NAME-RECOVERY-04", "text": "Do not treat a miss as evidence that she never applied."}, {"id": "MAIDEN-NAME-RECOVERY-05", "text": "keep the request an unsent draft on the user's device until every item is answered"}]
handoff: ["evidence-proof-judgment", "newspapers-com-search-recovery", "usa-immigration-search-recovery", "japanese-koseki-honseki-recovery"]
checked: "2026-11-16"
checked_basis: "read 2026-11-16"
capabilities: {"browse": ["civil-registration indexes, census images, newspapers, probate and land records, Social Security indexes"], "local_script": [], "extensions": [], "data_transfer": ["request"], "contact": []}
router: {"section": "Research method", "group": "Search coverage and name searches", "order": 9}
---

# Recover a woman's maiden name behind her married name

Use this recipe when a woman appears in records only under a husband's surname, as "Mrs." with his name, or as someone's wife, mother or widow, and you need her birth surname to reach her parents. Check first which surname her country's record-keepers used. Then work through the records that had to name her birth family: her marriages, her children's registrations, her household, newspaper notices, probate and land records and, in the United States, Social Security applications [S1]. Every surname you recover is a candidate until independent records agree; take identity and kinship rulings to [evidence/proof judgment](evidence-proof-judgment.md).

If she may be living, apply the [Living people rule](../SKILL.md#living-people): stay with the family-history question and the records the user supplies, and do not use people-search or contact-aggregator services to find her or her relatives.

## Contents

- What goes wrong
- 0\. Check the naming custom before searching
- 1\. Read every child's registration
- 2\. Rebuild her marriage chain, latest marriage first
- 3\. Read the household for her relatives
- 4\. Search newspapers under her husband's name
- 5\. Read probate and land records for her as a relative
- 6\. U.S.: read the Social Security application
- Return packet

## What goes wrong

- Reading the bride's surname on a marriage record as her maiden name. A bride's surname on a marriage record is the name she used at that marriage. If she had married before, it is probably a previous husband's surname, not her maiden name. [S7], [S8]
- Searching a woman from Italy or China only under her husband's surname. Italian records refer to women by their maiden name in most documents, and Chinese women traditionally kept their own surname. [S20], [S22]
- Reading "Shee" in an English-language record as a given name. It transliterates 氏, "Ms". [S22]
- Taking a census mother-in-law for the current wife's mother without checking. She can be the mother of an earlier wife. [S12]
- Treating a miss in the Social Security indexes as proof that she never had a number. [S16], [S19]

## 0. Check the naming custom before searching

Decide which surname each record type used before you choose search terms.

**Italy.** Italian records refer to women by their maiden name in most documents, even after marriage [S20]. Search her Italian civil records under her maiden name, never only under her husband's surname. On a passenger list, a married woman might be listed under her maiden name, a custom Family Tree Magazine calls more prevalent in Catholic countries [S21]. Her children should be under their father's surname, so when you know only the husband's surname, find the children on the manifest and read the woman travelling with them [S21]. Many Italians emigrated, so search immigration records for her too [S1]; take the arrival to [U.S. immigration search recovery](usa-immigration-search-recovery.md).

**China.** Chinese women traditionally kept their own surname after marriage, and records often give a wife only that surname [S22], [S1]. Clan genealogies usually record a wife only by surname and rarely include daughters [S23]. Read the surname a husband's genealogy gives his wife as her birth surname, and do not expect her father's genealogy to list her.

In English-language records, "Shee" is the Cantonese transliteration of 氏, "Ms", and can be mistaken for a name [S22]. Read a name such as Leung Shee as a woman surnamed Leung, not as a given name. The National Archives at Riverside describes Leung Shee, also referred to as Mrs. Tom Ah Quin [S24]; search such a woman under both forms.

**Japan.** For a Japanese wife's birth surname [S1], first establish which spouse changed surname. Article 750 of the Civil Code requires a married couple to share one surname, the husband's or the wife's; in 2017, 4.1% of marriages took the wife's [S25]. Nippon.com's timeline dates the same-surname requirement to 1896 and records that in 1876 a wife used her original family name [S25]. Trace her birth family through the family registers with the [koseki recovery recipe](japanese-koseki-honseki-recovery.md).

## 1. Read every child's registration

**Privacy gate:** <!-- privacy-gate: request --> A certificate order sends the child's name, the birth details or index reference you hold and the requester's identity to the registration office, and asks for a record that names the child and the child's parents. A child born within the last hundred years may be living. Before ordering a certificate or copy that names such a child, answer every [privacy gate](../SKILL.md#privacy-gate) item and follow its [Record requests](../SKILL.md#record-requests) rule: order only the record the question needs, send only the identity proof the office asks for, and keep the order an unsent draft on the user's device until every item is answered.

Search the birth registration of every child, not just one [S1]. In England and Wales the birth certificate gives the name and maiden name of the mother [S2]. Record the maiden name each registration gives, child by child, with its locator. Treat a differing name as a conflict to resolve: it can be a previous married name or a different mother.

In England and Wales, use the GRO's own online index before buying certificates. The GRO birth index includes the mother's maiden name from the September quarter of 1911, and the online index shows it where available [S2 @2026-11-16]. That online index covers births from 1837 to 1934 [S3 @2026-11-16] and includes the mother's maiden name before 1911 [S4 @2026-11-16]. Do not read the name's absence from an older printed or transcribed index as its absence from the GRO's online index.

On FamilySearch, search her children's death records with her as their mother: enter the child's name, the place and a year range for the death, add a mother relationship with only her given name, and set the record type to Death. The mother's maiden name may appear on the record [S5 @2026-11-16].

## 2. Rebuild her marriage chain, latest marriage first

**Privacy gate:** <!-- privacy-gate: request --> A marriage-record order sends the couple's names, the marriage date and place and the requester's identity to the office that holds the record, and asks for a record that names the couple and may name their parents and witnesses. A marriage within living memory names people who may be living. Before ordering a marriage certificate or a copy of a license, answer every [privacy gate](../SKILL.md#privacy-gate) item, apply the same [Record requests](../SKILL.md#record-requests) rule, and keep the request an unsent draft until every item is answered.

Search each marriage under the groom's name, the place and the approximate date [S1], [S9]. The name the bride gives is the one she used at the time of that marriage [S7]. In England and Wales the certificate states her condition, such as spinster or widow, and her father's name and surname [S6]. A bride who had married before probably used her previous husband's surname; her father's name is then the lead to her maiden name [S8].

Work backwards. When she married as a widow or divorced woman, search for the earlier marriage under her given name, her birth date and the surname she used at the later one [S1]. Repeat until you reach a marriage at which she had not married before; among her marriage records, that is the one that should give her maiden surname [S8].

Keep one row per marriage: date and place, the surname she used, her condition, her father's name, how and when the marriage ended, and the children born to it [S1]. Do not assign every child in the household to the current wife; children with the family surname can be the husband's from an earlier marriage [S12].

## 3. Read the household for her relatives

Read the household for her relatives [S1]. The 1850 U.S. census was the first decennial census to collect the names of every free person in each household, so before 1850 expect the head of household alone by name [S10]. The 1880 schedule records each person's relationship to the head of the family [S11].

Where relationships are given, a mother-in-law of a male head is his wife's mother or the mother of an earlier wife; in Diane Haddad's case, a first wife's mother stayed in the home after the head remarried [S12]. A brother-in-law or sister-in-law can be the wife's sibling or the spouse of the head's sibling. The mother-in-law may have taken a different surname since the wife's birth [S9]. Record each in-law's surname, age and birthplace as a lead, and test it against the marriage chain (§2).

## 4. Search newspapers under her husband's name

Search engagement and wedding notices with the groom's name, the place and the approximate marriage date [S1], and look for marriage-license items and other articles that name husband and wife together [S14]. Search her obituary and her husband's: a woman's obituary may give her maiden name or name a parent, a brother or an unmarried sister [S9]. A brother or an unmarried sister usually carries her birth surname; a married sister does not. Search her as "Mrs." with her husband's given name or initials, for example `"Mrs. * Smith"` or `Mrs Smith NEAR/5 John` [S13]. Use [newspaper search recovery](newspapers-com-search-recovery.md) for search mechanics.

## 5. Read probate and land records for her as a relative

When household records name her only as a wife, mother or daughter, turn to wills, property and tax records [S1]. Look for her there as a relative, not as a head of household; widows and single women sometimes appear as landholders or guardians in probate and tax rolls [S13]. Probate can name a decedent's in-laws, and wills list many family members [S15]. Read the probate of each candidate father for a daughter with her given name and her husband's name, and the husband's probate and deeds for her as his widow. A hit is a hypothesis for [evidence/proof judgment](evidence-proof-judgment.md), not a conclusion.

## 6. U.S.: read the Social Security application

The SS-5 application asked for the applicant's mother's full maiden name and, at various times, for the applicant's full name at birth, including a married woman's maiden name [S17]. So both her own application and each child's can give her maiden name [S1].

Search the NUMIDENT collection on FamilySearch first. It is free to search, covers deceased people only, and gives parents' names, including the mother's maiden name when available [S16 @2026-11-16]. Search her children's entries as well as her own.

**Privacy gate:** <!-- privacy-gate: request --> An SS-5 copy request sends the applicant's name (hers or a deceased child's), any number you hold, proof of death and the requester's identity to the Social Security Administration, and asks for a record that names the applicant's parents. Before submitting it, answer every [privacy gate](../SKILL.md#privacy-gate) item, follow its [Record requests](../SKILL.md#record-requests) rule, and keep the request an unsent draft on the user's device until every item is answered. Keep the copy that arrives on the user's device.

For a copy of the SS-5 itself, follow the Social Security Administration's process for a deceased person. Its manual directs such requests to its FOIA webpage, releases a deceased person's records when it has acceptable proof of death, such as a copy of a public record of the death, and withholds the parents' first and last names without proof of their deaths; a fee may apply [S18 @2026-11-16]. Send proof of the parents' deaths with the request, or expect their names withheld.

Do not treat a miss as evidence that she never applied. The MyHeritage post notes that only some people applied and that name changes and record errors get in the way [S1]. The NUMIDENT collection covers deceased people only [S16], and the Applications and Claims Index on Ancestry does not include everyone listed in the Social Security Death Index [S19]. Search under each surname in her marriage chain and through her children's entries.

## Return packet

- The naming custom applied for her country and period, and the surname each record type should carry.
- A marriage-chain table: one row per marriage with the surname she used, her condition, her father's name, how the marriage ended and its children.
- A child table: each child's birth and death registrations, the mother's maiden name each gives, and the locator.
- Household relatives: each in-law with census year, relationship, surname, age, birthplace and locator.
- Newspaper, probate and land leads, each with its locator.
- Application records searched, copies requested or still in draft, and any redactions.
- Each candidate maiden surname with the records that support it, and every conflict left open.
