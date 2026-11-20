---
id: "dna-match-outreach-staging"
title: "Stage and draft outreach to a DNA match or untested relative"
summary: "Stage and draft outreach to a DNA match, a match's account manager or an untested relative."
kind: "judgment"
scope: {"platforms": [], "tasks": []}
privacy: "genetic-third-party"
gates: ["privacy-transfer"]
guardrails: [{"id": "DNA-MATCH-OUTREACH-STAGING-01", "text": "If consent is missing or unclear, stop at the contact plan and a draft for the tester to review. Do not choose recipients yourself."}, {"id": "OUT-01", "text": "The letter must not state the conclusion."}, {"id": "OUT-02", "text": "If consent is missing or unclear, stop at the contact plan and a draft for the tester to review."}]
handoff: []
checked: null
checked_basis: null
capabilities: {"browse": [], "local_script": [], "extensions": [], "data_transfer": ["export", "publish"], "contact": ["contact"]}
router: {"section": "DNA", "group": "Ethnicity, admixture and match outreach", "order": 34}
---

# Stage and draft outreach to a DNA match or untested relative

Use this recipe before you draft or send any message to a DNA match, a match's account manager, or a relative you want to test. It covers four things: who is allowed to make contact, the order in which to approach relatives by closeness, what a first message must name, and how to log replies and silence.

It does not cover the following, which have their own recipes:

- Selecting and investigating matches on one site: [MyHeritage steps 2–7](myheritage-dna-match-investigation.md#2-build-a-shortlist-without-losing-matches-behind-an-old-filter) and the [23andMe match worksheet](23andme-match-research.md).
- The ethics of unknown-parentage cases: [unknown parentage / WATO](unknown-parentage-wato.md).
- Consent before an AI processes or names a match: [AI for DNA research](ai-for-dna-research.md).
- Whether a placement is proven: [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- Common assistant failures this recipe prevents
- 1\. Clear the consent gate first
- 2\. Stage the approach by relationship closeness
- 3\. Write a first message the recipient can check
- 4\. Inviting an untested relative to test
- 5\. Log every attempt; record silence as silence
- Output

## Common assistant failures this recipe prevents

- Drafting or sending contact on its own initiative, or for a helper, without the tester's consent.
- Writing a message to a possible parent or half-sibling that announces the relationship ("you are my father").
- Sending a vague invitation to "learn more about the family" that never names the kit, site, cM or segment.
- Treating the account holder as the tester.
- Treating no reply as a refusal.

## 1. Clear the consent gate first

- If the user is helping someone else (a client, relative or adoptee), do not draft a message for sending until the tester has explicitly agreed to all of the following, and record each answer:
  - who makes the first contact (the helper or the tester);
  - which matches the helper may contact;
  - what may be disclosed: the case question, the adoptee's or NPE status, names, birth details and tree links.
- Require a written informed-consent agreement. It must state that the helper does not discuss the case with others, and does not contact matches, without the tester's permission. The reason: that contact may be the only one the tester ever gets with that person [S1]. Treat a first message as final: you cannot revise it later.
- If consent is missing or unclear, stop at the contact plan and a draft for the tester to review. Do not choose recipients yourself.

## 2. Stage the approach by relationship closeness

**Privacy gate:** <!-- privacy-gate: contact --> Every message in this step goes to a living person and can disclose the tester's case; clear step 1 and answer the privacy gate in `SKILL.md` before any of them is sent.

Rank every planned recipient by how close the relationship is and how sensitive the case is. Then apply these tiers:

- **Distant cousins (second cousin or further, where the match is not itself evidence of the parentage question).**
  - With the tester's permission, a helper may write in the helper's own name.
  - Ask for something factual and limited, such as sharing a locked or missing tree ("I'm helping someone; could you please share your tree with us?").
  - Source: Eberle's practice in client cases [S4].
- **Possible birth parent, half-sibling or another immediate relative implicated in the question.**
  - The tester sends the message, not the helper. The helper only supports, for example by drafting the message and keeping the log. [S4]
  - Use a contact route the tester already has, the testing site's messaging, or a relative who agrees to pass the message on. Do not search for the recipient's address, phone number, email or online accounts (Living people, in `SKILL.md`).
  - Use a fill-in template that sets out facts only:
    - the sender is an adoptee (or describe the situation);
    - the sender has DNA tested and has these matches;
    - the sender was born in this place in this year;
    - if known and permitted, the birth mother's name.
  - Then ask for help. The letter must not state the conclusion. Leave the recipient to work it out and decide whether and how to reply. [S4]
  - Eberle credits this kind of model letter to a template a genetic genealogist published in 2017, and points to The DNA Geek blog [S4]. Leah Larkin published the template as *Letter to a Birth Parent* in 2017 [S22]. Read the published template before using it. Do not reconstruct it from memory.
- **First cousins, aunts, uncles and anyone in between.** Put them in the sensitive tier unless the tester decides otherwise. A close relative's reply can itself reveal the parentage answer.
- **A close relative does not reply.** Stop sending follow-ups. With the tester's permission, use Jones's alternative [S3]. Write instead to a second cousin on the same line. Ask only for a place, date or family connection. Keep the close match's identity and the parentage question private.
- **A previously responsive match goes quiet.** A participant reported that a 570 cM match initially discussed the connection and then stopped replying. Record the last exchange and any contact preference. If the person asked for no further contact, stop there. If the tester chooses to write again, Bardige recommended the following approach [S8]. Wait at least a year, then send a new sensitive-tier message, not a reminder.

Contacting a more distant relative is still contact. It needs the same consent and disclosure limits as step 1.

When two close matches point to the same paternal family, ask a relative you can already reach which brothers were in that family [S17]. Keep the question to family structure and use the replies to build a candidate list. Agreement on a surname does not identify the father.

## 3. Write a first message the recipient can check

**Privacy gate:** <!-- privacy-gate: contact, publish --> The message names kits, shared DNA and possibly a tree with living relatives in it; answer the privacy gate in `SKILL.md` before sending it or the tree link. The same gate covers historical record excerpts sent to the match that could identify living descendants.

Address the message so that it works whether the recipient is the tester or someone managing the kit. Rossi manages several kits and warns against assuming that the reader is the matching tester, or that you are matching their own kit [S5]. Include:

1. Who you are, whose kit you are writing about (your own or one you manage), and what the research is for.
2. The exact kit pair: your managed kit's name, and their kit name or username.
3. The site where the two kits match. Testers may have uploaded to several sites [S5].
4. Shared cM and the longest segment, copied from that site's display for that pair [S5]. If a value is not displayed, leave it out. Never estimate it.
5. One hypothesis, if you have one, such as a surname or town you saw in their tree [S5]. Label it as a hypothesis and keep it to a single sentence.
6. A link to your online tree, if one exists. Do not write out the whole tree [S5].
7. One specific question.

Keep it short. The aim is that the recipient does not have to move from website to website to find the match, and has enough to form their own hypothesis [S5]. Some testers care only about ethnicity results and may have no genealogical information [S5], so make the question answerable without genealogical knowledge.

Check the match's linked tree for signs that someone other than the tester runs the kit, sometimes the family's genealogist [S9]. If so, write to that person. In the sensitive tier, the tester decides first whether that person may be contacted (step 1).

Do not make the one question a request for access to the recipient's test results. Ask for that only after they have replied. Legacy Tree lists results access among useful requests to a genetic cousin [S6]. This governs what a message asks; a site's own connection or sharing request, such as 23andMe's, follows that site's recipe.

Ask a question the recipient can answer from their records. Milgrom reports that questions to Iberian matches about Jewish lineage drew no replies. After she asked whether their family records reached the 1400s or 1500s, some matches could answer [S10]. Ask about a person, place or period without assigning an ancestry to the recipient. Milgrom sent short versions in English and Spanish; choose languages the recipient is likely to use [S10].

For the most sensitive tier, step 2 limits what you may say, and those limits override this list. Leave out any kit or cM detail that would itself tell the recipient how they are related to the tester.

If records point to a possible connection through enslavement, offer the match the relevant historical records in place of the checklist question and say explicitly that you expect no reply or information in return [S15] [S16]. Leave ancestry estimates out of the outreach decision. Send cleared excerpts if the match accepts the offer.

### After a match replies

**Privacy gate:** <!-- privacy-gate: contact, publish --> A photo can show living people and would reach the match and the relative who sees it. A birth surname sent to the match may reveal a living person's name change or adoption. Answer the privacy gate in `SKILL.md` before either disclosure, including any onward sharing of the photo.

Ask the match whether an older relative who may have known the person would be willing to look at the photograph. After clearing the photo for both recipients, share it through the match and ask who the relative recognizes without suggesting an identity [S18] [S19]. Log any recognition as that relative's attributed claim. Never use facial resemblance as identity evidence.

When following up on an unexpected match, share a birth surname of the tester's parent if the parent later used another surname and the disclosure is cleared. Ask whether the match recognizes the birth surname from their family's papers [S20]. Treat a mention as a lead to check before assigning a relationship.

## 4. Inviting an untested relative to test

- **Privacy gate:** <!-- privacy-gate: contact, publish --> The invitation, and any tree snapshot or family photos sent with it, reach a living person and may show other living relatives; answer the privacy gate in `SKILL.md` first.
- **Channel and identity.** Reach the relative through a route the tester already has, or through a relative who knows them and agrees to pass the message on. Do not search for their email address, phone number or social-media accounts. Write from an identity the recipient can look up and confirm is real; when the route is email or social media, the presenter prefers social media for that reason. Do not cold call or send unsolicited postal letters: strangers' contact raises scam worries, and the recipient has to trust that you are real before you can persuade them to test [S2].
- **Say what the test would resolve.** Name the specific question, such as which ancestor or which brick wall, and why the answer is good for the recipient. "If you can DNA test, we can learn so much more about the family" is the vague form the presenter criticises [S2].
- **Help them recognise the connection.** Offer a tree snapshot, or photos of relatives you share or of their own family. Second cousins of a grandparent may still know people you know. [S2] The presenter warns to be careful with attachments [S2]. Since the barrier at this point is scam suspicion, put the snapshot in the message body or send a tree link rather than an unsolicited file.
- **Privacy.** If asked, describe the privacy risks plainly. Do not sugarcoat them or lie [S2]. Do not assert any company's current privacy terms unless you have checked them.
- **Kits.** If the user is supplying kits, say up front that the recipient will not pay. The presenter treats a prepaid kit as removing a major barrier [S2].

For a line from France, recruit testers among descendants of emigrants, such as Québécois or Acadian families, and expect few testers living in France [S11]. French law permits genetic examination of a person for medical or scientific-research purposes and for anti-doping, not for genealogy, and fines a person who requests one outside the legal conditions €3,750 (articles in force when checked on 2026-11-12) [S12], [S13]. Some people in France test anyway: a French law firm cited an estimate of three million in July 2026 [S14]. Do not read a lack of France-resident matches as evidence against a French origin.

**Privacy gate:** <!-- privacy-gate: contact, publish --> A group invitation reaches the tester. Joining or posting may disclose the tester's identity, an unknown-parentage search or information about living relatives to the service and group members. Answer the privacy gate in `SKILL.md` for those destinations before inviting the tester or posting.

If shared matches point to a common ancestral line and a private descendants' group already exists, offer the tester an invitation and let them decide whether to join [S21]. With permission for that audience, ask the group for family-branch information and for volunteers to test. Keep candidate parents' names and individual DNA results out of the group post.

## 5. Log every attempt; record silence as silence

For each message, log the date, recipient, kit, site, channel, sender (tester or helper), the disclosure tier used, and the reply status.

**Privacy gate:** <!-- privacy-gate: export, publish --> Screenshots of match entries and trees name living testers: keep them on the user's device and delete them with the case files, as the privacy gate's Retention item says. Posting about the case online publishes it; answer the privacy gate in `SKILL.md` first.

Before the first message to any match, and before posting about the case online, save dated screenshots of the match entry (kit names, shared cM, longest segment) and of any tree linked to the match. Keep them with the log. Matches may later make their profiles private or remove their trees [S7].

Record a missing reply as **no response as of [date]**, never as “refused” or “declined”. Jones describes a parentage search that narrowed to six brothers. More than a year after contact, the family had not replied [S3]. Leave the reason for the silence and the identity of the father unresolved. A contact log establishes only what was sent, received or expressly declined.

Record a reply such as "no, I don't recognise those names" as **does not recognise**, never as "no connection". Bardige notes that this is the usual answer to a list of surnames and towns. It means only that the names are not in the recipient's documented tree, so it does not count against the hypothesis [S8].

## Output

Return:

- the recorded consent terms;
- a contact plan: recipients ordered by tier, who sends each message, and what each may disclose;
- one draft per tier, filled only with values actually observed;
- the attempt log;
- any open consent or disclosure question for the tester to decide.
