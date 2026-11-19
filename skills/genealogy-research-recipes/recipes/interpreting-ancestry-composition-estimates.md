---
id: "interpreting-ancestry-composition-estimates"
title: "Interpret an ancestry-composition (ethnicity) estimate"
summary: "Decide what an ethnicity or ancestry-composition estimate, including GEDmatch admixture output, can show about origins and parentage, and what needs matches or records."
kind: "judgment"
scope: {"platforms": ["MyHeritage DNA", "23andMe", "AncestryDNA", "FamilyTreeDNA", "GEDmatch"], "tasks": ["small or trace ethnicity percentages", "expected German ancestry missing from an estimate", "parent, child or sibling estimates that differ", "unexpected Ashkenazi Jewish share", "choosing and reading admixture calculators"]}
privacy: "genetic-third-party"
gates: ["privacy-transfer"]
guardrails: [{"id": "INTERPRETING-ANCESTRY-COMPOSITION-ESTIMATES-01", "text": "An ethnicity estimate is a lead about where DNA resembles reference populations, not proof of any ancestor, origin or relationship."}, {"id": "INTERPRETING-ANCESTRY-COMPOSITION-ESTIMATES-02", "text": "A share of a few percent is a question, not a finding."}, {"id": "INTERPRETING-ANCESTRY-COMPOSITION-ESTIMATES-03", "text": "Do not reject a documented German line because the German-labelled category is low or missing."}, {"id": "INTERPRETING-ANCESTRY-COMPOSITION-ESTIMATES-04", "text": "Never use the size of a percentage difference between relatives as evidence for or against a relationship."}, {"id": "INTERPRETING-ANCESTRY-COMPOSITION-ESTIMATES-05", "text": "Never average calculators, or a calculator and a company estimate, and never choose the calculator whose result fits the expectation."}, {"id": "INTERPRETING-ANCESTRY-COMPOSITION-ESTIMATES-06", "text": "Record it as a parentage lead, not a conclusion, and keep it private."}]
handoff: ["ai-for-dna-research", "dna-match-outreach-staging", "evidence-proof-judgment"]
checked: "2026-11-16"
checked_basis: "read 2026-11-16"
capabilities: {"browse": ["ethnicity-estimate help pages and published method papers", "the tester's own estimate and match list"], "local_script": [], "extensions": [], "data_transfer": ["upload"], "contact": ["contact"]}
router: {"section": "DNA", "group": "Ethnicity, admixture and match outreach", "order": 31}
---

# Interpret an ancestry-composition (ethnicity) estimate

Use this recipe when a user brings an ethnicity or ancestry-composition estimate from a testing company, or admixture output from GEDmatch, and asks what it shows: whether a listed origin is real, why an expected origin is missing, why a parent's or sibling's estimate differs, or whether a result raises a parentage question. An ethnicity estimate is a lead about where DNA resembles reference populations, not proof of any ancestor, origin or relationship. Read it at the level it supports, and take every conclusion about a person, a line or a relationship to records and to shared DNA with matches.

Overlapping steps belong to sibling recipes. For match analysis, shared-cM comparisons and the consent and redaction rules for DNA, use [AI for DNA research](ai-for-dna-research.md). For any message to a match, a parent or a relative about DNA, use [DNA match outreach staging](dna-match-outreach-staging.md). For identity and kinship rulings, use [evidence/proof judgment](evidence-proof-judgment.md).

## Contents

- What goes wrong
- 1\. Record the estimate and read it at the level it supports
- 2\. Treat a small share as unconfirmed
- 3\. Expect German ancestry under neighbouring labels
- 4\. Do not test relationships with percentage differences
- 5\. Treat GEDmatch admixture as another model, not a check
- 6\. Follow up a large share the known parents cannot explain
- Return packet

## What goes wrong

- Accepting a share of a few percent as an established origin. MyHeritage's own help centre says small findings may be noise. [S3]
- Rejecting a documented German line because the German-labelled category is low or missing. German ancestry is often reported under neighbouring regions. [S7], [S8]
- Reading a difference between a parent's and a child's estimates, or between two siblings', as a sign about the relationship. [S3]
- Treating GEDmatch admixture output as a second opinion that confirms or overturns the testing company's estimate. GEDmatch itself says its results could vary from the company's. [S6]
- Dismissing a share of about half in a precisely detected population that the known parents cannot explain, or announcing a parentage conclusion from it. [S5], [S10]

## 1. Record the estimate and read it at the level it supports

Record each estimate as the site shows it: the platform (or the admixture project and calculator), the estimate's date or version, every region with its percentage, and any range or confidence setting displayed. Then read it at the level the method supports.

- **Continent first.** 23andMe's published method assigns each short stretch of DNA to the most specific population it can call with confidence. When it cannot tell, for example, Scandinavia from the British Isles, it falls back to a broader region, and a stretch it cannot place at all stays unassigned. Its cross-validation found precision above 97% and recall above 92% for continents at the lower threshold, with wider variation among finer populations. [S5]
- **Regions are not countries.** MyHeritage describes the boundaries between ethnicity groups as blurry and not confined by modern political borders, so a result may point to a neighbouring group with shared ancestry. [S3] Russell, comparing five companies, finds the numbers strong at the continental level and still problematic at the regional or country level. [S7]
- **Precision differs by population.** At the lower threshold, 23andMe's Ashkenazi Jewish population reached 99.3% precision and 98.6% recall; its Central & West Europe population reached 79.7% and 81.3%. These figures were measured on reference individuals of unmixed ancestry. [S5]

If a percentage estimate omits an expected place, check whether the testing company's reference panel covers the population you are investigating. A gap in reference coverage can explain the omission, according to Ancestry's documentation [S14] and the submitted extract from the Family Tree Magazine episode [S13†]. Keep the ancestry question open and test the line with records or matches.

Use the places highlighted in a DNA community or location report to choose localities for a historical record search, as the Family Tree Magazine search-result extract recommends [S11†]. Read the community timeline as group history [S12]. Establish when each ancestor lived there and for how long from records.

## 2. Treat a small share as unconfirmed

The MyHeritage post behind this rule says a reported origin can be trusted even at 2%. [S1] That is not followed. MyHeritage's help centre says small percentages may be noise rather than an ancestral signal and may not indicate a meaningful heritage connection [S3], and its 2017 announcement of the ethnicity analysis warned of false positives, especially at very low percentages [S4].

A share of a few percent is a question, not a finding. Do not add an origin, a migration story or a search for an unknown ancestor on its strength alone. Keep it in the estimate table as unconfirmed until records, or matches with documented ancestry from that place, support it.

## 3. Expect German ancestry under neighbouring labels

Do not reject a documented German line because the German-labelled category is low or missing. Family Locket's guide to German DNA research says neighbouring ethnicities are common on German results and that ethnicity is less reliable for German ancestors. [S8] Judy Russell's father's family was German, traced there for about 400 years, and she expected about half western and eastern European, mostly German, ancestry. MyHeritage estimated her at 66.9% Scandinavian, AncestryDNA at 14%, FamilyTreeDNA at 11% and 23andMe at 5.4%; she accepts her East European and Balkan shares as coming from a grandfather born in the former East Germany. [S7] In 23andMe's cross-validation, Central & West Europe had the lowest precision of its European populations, and its recall fell to 64.4% at the stricter threshold. [S5]

Read the German-labelled share together with the neighbouring and broad north-west and central European shares as one block. Test the German line with matches whose ancestors come from documented German places, and with records [S8], not with the label. Do not open a new Scandinavian, French or East European line on the strength of a neighbouring label alone.

The community source for this section, Kitty Cooper in a Family Tree Magazine interview, is reported as saying that German ancestry may appear under other European labels and that an unexpected label is no cause for alarm. The interview's transcript and audio were not available to this review, so this attribution is not independently verified. [S2†]

## 4. Do not test relationships with percentage differences

A child does not inherit a parent's percentages. [S1] Each child receives a random half of each parent's DNA, so the share from each grandparent can differ from a quarter (MyHeritage's example is 30% and 20%), siblings can carry different proportions from the same ancestors, and a distant line can leave little or no detectable DNA. [S3] A child's share of a region can therefore be larger or smaller than a parent's, or missing. Of five siblings in Russell's family, four were labelled Scandinavian and the fifth got the North and West European label the family expected. [S7]

To see which parental side AncestryDNA assigns a painted segment to, use the tester's existing results. With an Ancestry family history membership, open **DNA → Origins → By parent → View chromosome painter** and switch between the two parent views, labelled **Maternal** and **Paternal** when the sides are named. The colours show estimated regions and can change when the estimate is updated. Read matching colours on two charts as matching region labels and use shared DNA to test relationships. [S17 @2026-11-18]

Keep the numbered labels Parent 1 and Parent 2 until you can identify a side, for example by checking where Ancestry placed a DNA match whose side you already know. [S18 @2026-11-18]

According to the submitted extract [S15†], the presenter suggests switching between the two parent views in the Family Tree Magazine episode's Tree Talk segment on Chromosome Painter [S16].

Never use the size of a percentage difference between relatives as evidence for or against a relationship. Test relationships with shared DNA through [AI for DNA research](ai-for-dna-research.md). The exception is §6: a share that neither known parent could have passed on.

## 5. Treat GEDmatch admixture as another model, not a check

GEDmatch's Admixture (Heritage) tool offers calculators from five projects, many of them with several calculators. GEDmatch says the results could vary from the testing company's estimate and advises choosing the project and calculator that fit your known ancestry; for example, it recommends Eurogenes K36 for mostly European ancestry and Eurogenes Jtest when there is also an Ashkenazi Jewish background. [S6 @2026-11-16]

- Choose the calculator from the documented tree before reading any result, and report the project and calculator with every figure.
- Never average calculators, or a calculator and a company estimate, and never choose the calculator whose result fits the expectation.
- A calculator figure neither confirms nor overturns a company estimate. Where they disagree, take the question to matches and records.

Kitty Cooper, the community source for this section, is reported as calling ancestry composition an inexact science, unlike relative matching. The interview's transcript and audio were not available to this review, so this attribution is not independently verified. [S2†]

**Privacy gate:** <!-- privacy-gate: upload --> The tester's raw DNA file, the genetic data of the tester (the user, a parent or another relative, who may be living), leaves the user's device for GEDmatch, a matching database.

GEDmatch's calculators become available once a kit's upload is complete [S6 @2026-11-16]. If the tester's kit is not already there, uploading a raw DNA file to get another estimate is a data transfer to a matching database. Before it, answer every item of the [privacy gate](../SKILL.md#privacy-gate) in writing, including who can see and match the kit and whether law-enforcement uploads can match it, and get the tester's explicit permission for this upload to this destination. Apply the consent and redaction rules in [AI for DNA research](ai-for-dna-research.md#verification--privacy-discipline). If any answer is unknown, do not upload; read the testing company's estimate instead.

## 6. Follow up a large share the known parents cannot explain

Compare the estimate with what the documented parents could have passed on. A share of about half in a population that neither known parent belongs to, or a share of only about half when both known parents belong to it entirely, is not ordinary inheritance variation (§4). When the population is one the model detects precisely, treat it as a parentage lead. Ashkenazi Jewish ancestry is the clearest case: 99.3% precision and 98.6% recall in 23andMe's cross-validation. [S5]

Published cases show how such a lead resolves. A woman conceived with a donor described as of Jewish extraction was estimated at 49.9% Ashkenazi Jewish, and the donor later appeared among her 23andMe relative matches. [S9] The DNA Geek describes a woman whose parents and four grandparents were all Jewish but whom four companies estimated as only about half Ashkenazi; her legal father's brother shared only 69 cM with her, and the case resolved to a known donor. [S10]

Kitty Cooper, the community source for this section, is reported as describing a half-Jewish result that led to the discovery of a sperm donor. The interview's transcript and audio were not available to this review, so this attribution is not independently verified. [S2†]

- Record it as a parentage lead, not a conclusion, and keep it private. The estimate does not show which parent, which generation or which explanation applies; donor conception, another misattributed parentage and a parent's own unknown origins can all produce it.
- Test it with shared DNA: compare shared cM with known relatives on each side through [AI for DNA research](ai-for-dna-research.md), and take the kinship ruling to [evidence/proof judgment](evidence-proof-judgment.md).
- The finding is sensitive: it concerns unexpected parentage. Do not add it to a shared tree, a match note or a message.

**Privacy gate:** <!-- privacy-gate: contact --> A message from the tester or user leaves for a living parent, relative or DNA match; it concerns a sensitive parentage lead and may carry only that person's own data and the question.

Asking a parent or relative to test or to share results, or messaging a match about this lead, contacts a living person about a sensitive finding. Stage it through [DNA match outreach staging](dna-match-outreach-staging.md) and answer the [privacy gate](../SKILL.md#privacy-gate) in writing first. A first message may show the person only their own data and the question, never another person's sensitive finding.

**Living people.** Do not look up a possible donor's or biological parent's current address, phone number, email, workplace or online accounts. Identify a person only as far as the match evidence and the user's question require, as the [Living people](../SKILL.md#living-people) rule says.

## Return packet

- An estimate table: platform, or project and calculator; the estimate's date or version; each region and percentage; any range or confidence setting shown.
- For each region, the level read (continent, region or country) and a status: supported by records or matches, lead, or unconfirmed small share.
- An expected-versus-reported comparison against the documented parents and tree, with neighbouring-label shares read together (§3).
- Any parentage lead, kept private, with the shared-DNA tests planned and their results.
- The written privacy-gate answers for any upload or contact, or a note that none took place.
- Explicit gaps: no parent tested, calculator not chosen in advance, lead not yet tested with matches.
