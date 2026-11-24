---
id: "ydna-mtdna-interpretation"
title: "Interpreting Y-DNA and mtDNA — what a haplogroup or STR/sequence match can (and can't) establish"
summary: "Read a haplogroup, Y-STR or mtDNA match for what it can and cannot show about a relationship in genealogical time."
kind: "judgment"
scope: {"platforms": [], "tasks": ["\"what does my haplogroup / Y-STR match / mtDNA match mean\", \"how many generations back is genetic distance N\", \"does this haplogroup contradiction prove a non-paternity event\", differing Y labels, measured versus inferred SNP results, choosing a tester to split an unresolved SNP block, TMRCA disagreement with a dated pedigree, or a pair matching on both autosomal DNA and Y-DNA/mtDNA through potentially different ancestral lines."]}
privacy: "genetic-third-party"
gates: ["privacy-transfer"]
guardrails: [{"id": "YDNA-MTDNA-INTERPRETATION-01", "text": "**you do not compute or assign haplogroups, TMRCAs, or NPE verdicts from your own reasoning.** Every such value is a *hypothesis to route to the right tool or corroborate* — never a fact to state."}, {"id": "Y-01", "text": "A GD is *stochastic*, not a clock (below)."}, {"id": "Y-02", "text": "**you do not compute or assign haplogroups, TMRCAs, or NPE verdicts from your own reasoning.**"}]
handoff: ["ai-for-dna-research", "dna-match-outreach-staging"]
checked: "2026-07-18"
checked_basis: "accessed 2026-07-18"
capabilities: {"browse": [], "local_script": [], "extensions": [], "data_transfer": ["third-party-tool", "upload"], "contact": ["contact"]}
router: {"section": "DNA", "group": "DNA reasoning", "order": 29}
---

# Recipe: Interpreting Y-DNA and mtDNA — what a haplogroup or STR/sequence match can (and can't) establish

## Contents

- Goal
- The mental model (get this right or everything downstream breaks)
- Rules of thumb — the resolution → timeframe map (interpretive ceilings, not a tutorial)
- What to trust vs never fabricate (the four failure modes)
- When Y haplogroups differ: compare calls, then choose the next tester
- Prompt-craft (how to keep an assistant honest here)
- Pitfalls worth internalizing (least-obvious, most-LLM-usable)
- Keep an ancient-sample catalogue query separate from ancestry inference
- Evaluate lineage evidence for historical remains
- Inventory lineage and test coverage before choosing another tester
- Build a maternal pedigree and locality worklist
- Combining tests: establish which ancestral path each supports

## Goal

Given a Y-DNA or mtDNA result — a **haplogroup assignment**, a **Y-STR genetic-distance match**, or an **mtDNA sequence match** — state what it can genuinely establish about a *genealogical-timeframe* relationship (roughly the last ~500 years, the paper-trail era), and refuse the four places where confident interpretation crosses into fabrication.

## The mental model (get this right or everything downstream breaks)

A haplogroup locates a lineage on the tree used to assign it. Genetic distance counts differences under a particular test’s scoring rules. To investigate a relationship, identify the measured result, the dated tree or report, and the documented line of descent.

Check an AI-supplied haplogroup against the tester’s actual report and an ancient comparison against the study that sequenced the sample. A chatbot reportedly assigned both a tester and Anzick-1 to A2ex [N16]; the original Anzick-1 study identified his mtDNA as D4h3a [N146].

So: **you do not compute or assign haplogroups, TMRCAs, or NPE verdicts from your own reasoning.** Every such value is a *hypothesis to route to the right tool or corroborate* — never a fact to state. Route haplogroup/tree questions to **FTDNA Discover** (the free, authoritative Y-DNA tree + Mitotree reference), genetic-distance timing to the **FTDNA TiP report / Match Time Tree**, and treat their output as a **range with a confidence band**, never a point.

## Rules of thumb — the resolution → timeframe map (interpretive ceilings, not a tutorial)

What each test level can *bound*, and where confidence collapses:

- **Backbone haplogroup (e.g. R-M269) / a 23andMe or third-party estimate** → resolves **millennia**, not generations: a high-level assignment's MRCA sits **thousands of years back** (R-M269 formed about 6,450 years ago; a 23andMe-level estimate points ~2,000–5,000 years back). Genealogically **inert**: it cannot place a paper-trail-era ancestor, and it is *not* an ethnicity (R1b is common in Europe but not all Europeans are R1b, nor all R1b European). Y and mtDNA haplogroups together capture a *shrinking* slice of ancestry (½ of the grandparents, ¼ of the great-grandparents, ⅛ …), never "your heritage." (Family History Fanatics, 2026-05 [N12 @2026-11-08]; GeneaVlogger, 2026-04 [N3 @2026-11-08]; DNAeXplained, 2026-04 [N11 @2026-11-08])
- **Y-STR panels — Y-37 and Y-111 today** → give **matches + a genetic distance (GD)**, mapped by the TiP report to a **time range that widens at lower marker counts** [N104 @2026-11-08]. A GD is *stochastic*, not a clock (below). FTDNA stopped selling Y-25 and Y-67 as *new* tests in January 2020 [N96 @2026-11-08]. Its help now says it no longer offers the 12-, 25- or 67-marker levels [N97 @2026-11-08], and its upgrade price list shows no upgrade to Y-67 [N98 @2026-11-08]. Legacy Y-67 kits can still be upgraded [N98 @2026-11-08], and FTDNA's TiP help still shows estimates for every Y-STR matching level from Y-12 to Y-111, Y-67 included [N104 @2026-11-08].
- **Terminal SNP via Big Y-700** (~23 million Y positions, per DNAeXplained; tests STRs *and* SNPs — SNPs define the branch, and Big Y matches men who carry the same SNPs) → refines the branch, generally into a **genealogical timeframe**; Match Time Tree dates it. It is the test that can separate a recent surname connection from a deep coincidence. (DNAeXplained, 2026-04 [N11 @2026-11-08]; FTDNA, 2026-05 [N6 @2026-11-08]; Rowe-Schurwanz, 2024-08-20 [N26 @2026-11-08])
- **mtDNA HVR1/HVR2** → a match here has low resolution and tends to point to a more distant maternal ancestor, often **thousands of years back**; on its own it cannot support a recent or geographic conclusion. **Full sequence (all 16,569 positions)** is the refined test — but even a full-sequence match is **still not proof of a genealogical-timeframe or geographic relationship** (where matches live today does not place the shared ancestor [N15 @2026-11-08]; fewer testers [N3 @2026-11-08]). (GeneaVlogger, 2025-09 [N15 @2026-11-08]; DNAeXplained, 2026-04 [N11 @2026-11-08])
- **STR vs SNP**: SNPs are stable, long-term branch definers; **STRs mutate faster**, and a marker value can step up or down (a 15 becoming a 14 or a 16), so STR closeness is *weaker* evidence than a shared SNP. (Rowe-Schurwanz, 2024-08-20 [N26 @2026-11-08]; FTDNA, 2026-05 [N6 @2026-11-08])
- **Privacy gate:** <!-- privacy-gate: third-party-tool --> Entering a tester's or relative's STR values into a subclade predictor sends living people's genetic data to an outside tool; answer the privacy gate in `SKILL.md` first.
- **An STR-based subclade prediction nominates a branch; it does not assign one.** Record the predictor, or the SNP-tested project set whose STR signatures were used, along with the markers, values, tree version and date. Test it against the STRs of a documented same-line relative whose branch was measured by Big Y or sequencing, and compare a second predictor ([predictor comparison](https://genarchivist.net/showthread.php?tid=1806) [N47 @2026-11-08]). A tester who fits no signature stays unresolved ([signature example](https://genarchivist.net/showthread.php?tid=558), partially read [N48 @2026-11-08]); STR instability (see STR vs SNP above) is one reason a signature may mislead. Report the result as predicted until a SNP test confirms it. Agreement at one level does not validate deeper calls, and neither source establishes any tool's accuracy.

## What to trust vs never fabricate (the four failure modes)

### 1 — NEVER emit a Y-STR genetic-distance → generations/TMRCA point estimate

Do **not** say "GD 2 at Y-67 ≈ 5 generations" or "GD 5 at Y-111 means exactly five markers differ." **GD is a score under the comparison's marker rules.** FamilyTreeDNA describes step-wise scoring for most STRs: a difference at one marker can contribute more than one step. Multi-copy STRs use different rules; in its DYS464 example, extra copies can leave GD at zero. Neither GD nor a count of differing markers reconstructs how many mutation events occurred. Back mutations and parallel mutations obscure that history. (Rowe-Schurwanz, 2024-08-20; STR mutation behavior above)

Before interpreting GD, retain the tested panel, the level compared, the reported score and the marker values when available. Compare the shared panel, not one tester's Y-111 results against another's Y-37 label. Apply the reporting laboratory's rules for single-copy markers, multi-copy markers and null/deletion results; an unresolved result is not an allele value of zero. If only the aggregate GD is available, the differing loci and mutation history remain unknown. Do not invent them by subtracting GD from the panel size. (Rowe-Schurwanz, 2024-08-20; comparison synthesis)

For Y-STRs, use the TiP report for the shared panel and genetic distance [N104]. For Big Y results, consult the Match Time Tree [N4]. Record the range, its confidence level and any separately labelled central estimate. In one TiP demonstration the range was 1500–1850 and the documented ancestor was born in 1798 [N4]. The report cannot supply an exact birth year.

**Privacy gate:** <!-- privacy-gate: upload --> Entering a tester's legacy Y-STR marker values
into an outside database or import route moves that tester's genetic data; answer the privacy
gate in `SKILL.md` first.

For an authorized legacy paper result, retain the report and its tester, laboratory, assay
and panel beside any manual reconstruction. Check each available marker label and value
against that source before using an offered entry/import route; leave unreadable or unmapped
fields unresolved. Date and attribute the reconstruction: it represents the old assay, not a
new test or independent confirmation. The [paper-result recovery example](https://familylocket.com/recreating-a-y-dna-surname-project-at-mitoydna-org/)
does not supply a current import format or a cross-laboratory conversion.

For several kits, retain the full STR table and make a separate working view of comparable
marker columns with observed differences. Carry kit/locus labels, panel coverage and unresolved
or multicopy calls; a missing call is not an observed equality or zero allele. Use that view
to nominate a locus or source discrepancy for checking. The [difference-view example](https://www.yourdnaguide.com/ydgblog/ydna-for-genealogy)
supplies the filtering action; the view does not root a tree, count mutation events or identify
a father or MRCA.

Before computing GD across sources, label each STR value's origin and convention. It may be a laboratory panel value (with date), a value extracted from sequencing data, a copied database or certificate entry, or a typical value filled in for a missing marker. Laboratories can number the same marker differently ([cross-database entry discussion](https://forum.molgen.org/index.php/topic,3315.0.html); [laboratory-panel discussion](https://forum.molgen.org/index.php/topic,15097.0.html)). One laboratory announced renumbering that would make earlier certificates disagree with its website ([nomenclature announcement](https://forum.molgen.org/index.php/topic,125.0.html)). Convert a value only where the laboratory or target tool documents the rule, and keep original and converted values side by side. If an extracted value and a panel value disagree, keep both and mark the marker unresolved ([extraction comparison](https://forum.molgen.org/index.php/topic,10934.0.html)). Compare only markers both sides report. For a manual comparison, sort multi-copy values in ascending order without replacing the laboratory's rules ([multi-copy display case](https://genarchivist.net/showthread.php?tid=2477)). A numbering offset, an imputed value or a display-order difference is never a mutation or a GD step.

- **Trust / route:** the TiP report or Match Time Tree, quoted **as a range that widens at lower marker counts**. Recommend upgrading Y-37→Y-111→Big Y-700 to *narrow* it.
- **Never:** a self-computed point estimate, or treating the vendor's midpoint as the relationship.

A Big Y-700 tester already has the Y-111 panel. FamilyTreeDNA's Big Y-700 includes the 111 STRs of the Y-111 test and provides the STR matches, plus at least 589 more STRs (FamilyTreeDNA Help Center, edited 2024-05-21 [N138 @2026-11-14]). Its product page lists Big Y-700 as including everything in Y-37 and Y-111 [N139 @2026-11-14], and a 2024 introduction calls it two tests in one (My Family Pattern [N137 @2026-11-14]). Do not advise a Big Y-700 tester to order Y-37 or Y-111, and do not look for his Y-111 matches anywhere but his own STR match list.

#### When TMRCA conflicts with a dated pedigree

**Investigate a disagreement with the pedigree.** FamilyTreeDNA’s original 95% interval missed John Stewart’s documented birth year, and the estimate changed when the model was revised [N29]. Check the model version, branch-specific rate and sequence coverage before inferring a pedigree error. A fixed number of years per SNP cannot reproduce this estimate.

Record the dated tree node or tester pair, interval and confidence level, estimator, report date and available model/version information. Check that the estimate and documentary date refer to the same proposed ancestor, and inspect the descent paths. For a Big Y or SNP-tree estimate, inspect informative SNP calls and relevant sequence coverage. For an STR/TiP estimate, recheck the shared panel, marker values, laboratory GD scoring and retained report inputs described above. Compare an updated estimate with the retained earlier report. If disagreement persists, seek qualified review of the dating and pedigree evidence. Do not tune a mutation rate to fit the preferred ancestor or silently discard either result. This procedure combines the dating example with the STR and SNP comparison checks in this recipe.

Record both dates for each node, with the tree and version: *formed* dates the branch’s split from its parent and *TMRCA* dates the common ancestor of its sampled members [N32], [N35]. Match the node, event and units before comparing a provider’s estimate with a paper [N33], [N34]. If the displayed estimates appear out of order, inspect their intervals and definitions and retain the discrepancy [N36]. The branch’s formation date cannot date the tester’s nearest match or establish where the branch arose.

### 2 — NEVER read an exact match at low resolution as "recent"

An exact Y-37 or HVR1/HVR2 match establishes agreement only over the markers compared. Check the common higher-resolution test and its reporting threshold before calling the relationship recent [N14], [N26]. In a Schultz surname project, reported Y-37 matches disappeared at Y-67 and Y-111 [N9]. That change describes what the panels could distinguish.

- **Trust:** Keep the relationship unresolved at low resolution. Compare full mitochondrial sequences when available and document each direct-maternal pedigree. A match distribution spanning Romania and Hungary cannot locate the common maternal ancestor [N15].
- **Never:** "you match exactly, so you're closely related," or an mtDNA HVR/region match as evidence of a specific place or recent maternal ancestor.

An exact Y-111 match is not resolved either. In a 2022 case, two exact Y-111 matches came with FamilyTreeDNA's estimate of a 98% chance of a connection within five generations, yet the Big Y Time Tree put the men's shared ancestor at an average birth year of 1643 (95% range 1462–1775); the author took this to rule out the two pedigree hypotheses resting on those matches (The DNA Geek, 2022-11-10 [N109 @2026-11-12]). FamilyTreeDNA replaced that STR estimate in 2023 because it often placed the common ancestor too recently, and now builds its ranges from Big Y branch ages (FamilyTreeDNA, 2023-02-16 [N110 @2026-11-12]). When both lines have Big Y results, take the range for their shared node on the Time Tree. Otherwise keep an exact Y-111 match unresolved, and recommend Big Y-700 before using it to choose between pedigree hypotheses.

Do not turn a full-sequence mtDNA GD0 or GD1 into centuries with a mutation rate. The lower bound is zero. The upper bound depends on the youngest branch containing both sequences, judged against all available sequences of that subclade ([common-ancestor discussion](https://forum.molgen.org/index.php/topic,2742.0.html); [full-sequence example](https://forum.molgen.org/index.php/topic,2548.0.html)). Several exact matches in one region on a widespread ancestral type with no private mutations may be independent lines, not one founder line. Record each match's own test level and compared regions beside its label. An HVR-level match shown to a full-sequence tester may never have tested the coding region. A project table of HVR values cannot show that a coding mutation is absent ([match-list discussion](https://forum.molgen.org/index.php/topic,936.0.html)). Count matches separately at each level. A subclade missing among HVR1-only matches tells you nothing ([match-count example](https://genarchivist.net/showthread.php?tid=1141)). The rates and year figures in these threads are forum estimates from one database; do not reuse them, and no frequency threshold is given.

**Keep competing fathers from the same paternal line in the worklist.** Y-STRs can help investigate the paternal line, but men on that line can share the same STR profile [N152] [N153]. If the observed profile fits both candidates, for example two brothers, keep both and seek records or autosomal evidence that can distinguish them [N153].

If the purchased Y-STR level shows no matches, view the match list at a lower comparison level
before concluding that no paternal-line relatives have tested. Record which level produced each
match. A different-surname match seen only at a lower level remains unresolved as recent or ancient.
Check its actual panel coverage and available higher-level results, and compare the documented
places of origin of both surnames as a lead [N30]. Check the paternal pedigrees before assigning a date or relationship.

If someone is absent from a match list, record the service, test and shared panel before interpreting the miss. A Big Y branch member may appear in the Block Tree while absent from a match list [N60]. Check whether the other person tested Big Y or only STRs [N61] and which service holds the result [N53], [N62]. A pair can disappear at one STR level and reappear at another [N63]. Read the lab’s thresholds and record the actual GD for each level [N26]. In a public STR database distinguish individual testers, study samples and modal haplotypes before counting hits [N54]. A modal value represents a group summary.

Apply the same bounded negative to mtDNA match lists. FamilyTreeDNA's Coding Region tab lists full-sequence matches within three differences, and its HVR1 and HVR1+HVR2 tabs list exact matches only; a match who took only the older HVR1 test is seen on the HVR1 tab, not on the full-sequence list [N105 @2026-11-12]. Coding Region matches also share your Legacy (PhyloTree) haplogroup (FamilyTreeDNA, 2025-02-25 [N108 @2026-11-12]). When a documented maternal relative or a descendant of the target ancestor is missing, look on the HVR tabs for testers who never upgraded (Estes, DNAeXplained, 2022-05-08 [N92 @2026-11-12]), and read any match found there under the low-resolution rule above. Then look in mtDNA Discover. Haplogroup members four or more differences away are not on the Matches page; comparing the Discover Time Tree, which shows everyone in the haplogroup, with your Match Time Tree, which shows only your matches, finds them (Estes, DNAeXplained, 2025-09-02 [N107 @2026-11-12] and 2025-10-22 [N106 @2026-11-12]). Such a member's country entry is a location lead, not a match.

### 3 — NEVER treat mtDNA genetic distance as a clean, linear closeness ranking

A mtDNA **genetic distance (GD)** count is not the even measuring stick it looks like. FTDNA's full-sequence matching allows **up to 3 differences** (heteroplasmy included) but **completely excludes the poly-C insertion positions 309 and 315** from the GD count (a 309.1C/315.1C difference never registers). Haplogroup trees use **separate** exclusion lists: some fast-mutating positions are left out of tree building because they are too unstable to define a branch, but they **still count toward GD**. The two published tree lists differ. PhyloTree Build 17 excludes 309.1C, 315.1C, the AC indels at 515–522, 16182C, 16183C, 16193.1C and 16519. FTDNA's Mitotree list (its mtDNA Discover™ Scientific Details help) excludes positions including 16182, 16183, 16193.XC and indels between 513 and 522, but not 16519. Do not confuse the GD list with the tree lists: only 309/315 are GD-*excluded*; 16519, 16182, 16183 and 16193.1C remain counted in the match's GD number. (FamilyTreeDNA Help Center, "mtDNA Matches Introduction" and "Using the mtDNA Discover Scientific Details Page"; PhyloTree Build 17; Estes, DNAeXplained, 2016-06-29)

Inspect which positions contribute to genetic distance before prioritizing a maternal match. A GD1 or GD2 match with differences at unstable positions can merit follow-up alongside a GD0 match [N21]. GD0 means agreement at the positions counted under the laboratory’s rules. A difference at an excluded insertion such as 309 or 315 can therefore coexist with GD0. Compare the pedigrees and positions before ranking the relationships.

- **Trust:** treat GD as a **starting filter, not a ranking** — before calling one match "closer" than another, name which specific positions produced each count: a difference on a *stable* position weighs heavily, a difference on a fast-mutating position (16519, etc.) weighs lightly and doesn't rule out a close relationship, and an *excluded* position (309/315) can hide a real difference behind an apparently exact GD0.
- **Never:** rank matches by raw GD alone ("GD0 beats GD1"), and never list 16519, 16189, or 16193 as GD-*excluded* — a haplogroup tree list may leave some of them out, but they still count toward the GD number; only 309/315 are excluded.

Keep haplotype cluster, haplogroup, genetic distance and documented maternal descent in separate fields. A cluster can help prioritize matches, and its signature can include fast-mutating or personal markers [N50], [N118]. In one account, two testers reportedly sharing an early-1800s maternal ancestor lay on opposite sides of a cluster despite GD0 [N49]. Check out-of-cluster matches against the documented line as well.

Check for a heteroplasmy before reading a one-position difference, or a haplotype-cluster split, between documented close maternal kin as evidence against the relationship. FamilyTreeDNA reports a heteroplasmy only when more than 20% of the mitochondria tested show the second base, and writes it with a letter other than A, C, G or T [N111 @2026-11-12]. A relative just below that threshold is reported without it, so sisters can differ at that position and fall into different haplotype clusters (Estes, DNAeXplained, 2025-09-02 [N107 @2026-11-12] and 2025-02-25 [N112 @2026-11-12]). If one result shows such a letter at the differing position and the other result's base is one of the bases that letter stands for (R is A or G), the difference is not evidence that the lines differ.

### 4 — NEVER assert a non-paternity event (NPE) from a haplogroup contradiction or absent surname-matches

A haplogroup/terminal-SNP that **contradicts** the documented paternal line, or an **absence of surname-matching Y-testers**, is a **FLAG that needs corroboration — never PROOF of an NPE.** *(This is the Y/mt-specific instantiation of flag-vs-proof; it is not the general proof-standard lesson.)* Competing explanations that produce the identical signal:

- **Check who actually Y-tested.** In one account the researcher had autosomal matches to Goldberg cousins but no Y result from those cousins [N7]. An untested direct-paternal line gives no Y comparison. A private variant may acquire a named branch when another tester shares it [N11].
- **Check the call and the tree version.** A sequencing or read-interpretation error, or a newly defined downstream branch, can produce different reported labels [N24].
- **Check how the surname passed.** Test alternatives such as maternal transmission of the surname, a stepfamily, two men with the same name, or a shared paternal ancestor who lived before hereditary surnames. A reported Woodall project found discordant paternal lines among presumed relatives without resolving where or how the pedigrees diverged [N18].
- **Privacy gate:** <!-- privacy-gate: contact --> Asking another son of the same father, or other documented male-line relatives, to take a Y-DNA test approaches living people about a paternity question; answer the privacy gate in `SKILL.md` before contacting them.
- **A laboratory sample mix-up, or a documented name change.** Before reading a surprising Y result as an event, consider a replicate on a separate kit or a test of another son of the same father ([N64]). Record both kits and their results. Agreement shows only that the result reproduces for that sample source. Disagreement between two kits from the same man points to sample handling; between brothers it leaves both handling and paternity open. Also search for a record that would explain a surname change, such as a child registered under a stepfather's surname after the mother remarried, or a clerical misentry that was later kept ([N65]). Keep legitimacy and biological paternity in separate fields. A man named in a baptism, or a husband who married the mother shortly before a birth, is a documentary attribution, not genetic confirmation. The rates quoted in the surname-change thread are not used, and neither thread shows which pathway applies to a given line.
- **A break in the matches' line, not yours.** When many Y matches share a different surname, the event may sit in their common ancestor: a misattributed or unknown parentage there put that surname on a paternal line shared with yours. To locate a break, target-test documented male-line relatives who descend from your proposed paternal ancestors at different generational depths; the pattern of matches brackets the generation or points to another explanation. A non-match with one cousin leaves the break on either man's path below their shared ancestor, so test another descendant of that ancestor before assigning it to your line. [N86]

Base rate cuts **both** ways: a commonly-cited **~5% per generation** misattributed-paternity estimate (a rule-of-thumb; formal studies usually land lower, ~1–2%) means a *deep* paper trail almost certainly contains a break **somewhere** — so a contradiction is *plausible* — but that same statistic **cannot tell you which generation**, so it never localizes the event. (Legacy Tree, 2026-01)

**Privacy gate:** <!-- privacy-gate: contact --> Asking a known male relative or additional direct-line descendants to test, or a man of the surname with no documented link to your subject, approaches living people about a possible parentage break; answer the privacy gate in `SKILL.md` before contacting them.

- **Stronger corroboration (upgrades a flag toward a finding):** (a) a **known male relative who Y-tested and does *not* match you** — a genuine red flag; (b) the non-surname match also being a **close autosomal (Family Finder) match** ⇒ recent connection, investigate; (c) **Big Y** to date *when* the branch/surname split occurred; (d) testing additional documented direct-line descendants to confirm or eliminate. (Your DNA Guide, 2025-10; GeneaVlogger, 2026-05)
- **Never:** "your haplogroup doesn't match your surname line, so there was an NPE," or "no one with your surname matches, therefore NPE."

**When no Y match carries the expected surname, check the comparison group and the autosomal evidence.** For an uncommon surname, recruit a man of that surname whose family comes from your subject's county if no documented relative is available [N133]. Two local families may be unrelated. A mismatch with that man leaves the relationship open until records connect his branch to the expected family. Prefer a tester from a second documented branch of the subject’s own paternal line [N135]. Next group the subject’s autosomal matches and investigate unexplained clusters using the [WATO workflow](unknown-parentage-wato.md) [N134]. Autosomal evidence becomes less informative for a break further back. Compare the Y results with records at each proposed generation [N136].

#### Test a clan or dynastic pedigree against the Y-SNP tree

When a medieval pedigree joins several surnames to one paternal ancestor, compare testers on documented branches of each family. Check whether their measured SNPs place them under the proposed dynasty SNP and whether their branching order and date intervals fit the pedigree [N113 @2026-11-12], [N114 @2026-11-12]. In the published Mayo O’Malley comparison the testers were placed under DF105, upstream of the proposed A259 dynasty branch [N114 @2026-11-12]. A broad shared label cannot establish the narrower attachment. Check the calls and test coverage, including whether A259 was actually tested, before excluding it. A discordance can flag a pedigree error or a break on either line. Compatible dates alone cannot identify a named historical ancestor.

A surname missing from the expected branch does not make the pedigree false. Its original signature may be absent because the surname died out, no bearer has tested, a DNA switch uncoupled the name from the signature, a family adopted a more powerful lord's surname (surname gravity), the Irish form was lost in 16th–19th-century anglicization, or testers have not made their results public on project pages (Gleeson and DePew, FamilyTreeDNA blog, 2024-05-24 [N113 @2026-11-12]).

**Check which branch the Genghis Khan claim refers to.** The MyHeritage blog suggests comparing branches within C-M217 [N143]. Compare the tester's deepest measured SNPs with the specific branch cited for the claimed descent. The C2*-Star Cluster (C-F3796) is downstream of C-M217, and its estimated common ancestor predates Genghis Khan (Wei et al., 2018 [N144]). Use regional distributions to describe the sampled branches. Leave the named ancestor unresolved even if the comparison reaches the Star Cluster or the branch sampled in Golden Horde burials. Require independent evidence tying the reference branch to Genghis Khan before using it to evaluate a pedigree to him (Hawks, 2026 [N145]).

## When Y haplogroups differ: compare calls, then choose the next tester

**Resolve what differs before calling it a paternal-line contradiction.** Work from each tester's documented male-line descent and actual results, using this comparison sequence.

1. **Trace the path between the reported assignments.** Record the test type, results, tree and date. One relative’s broad assignment can contain the other’s downstream branch [N23]. A father and son can have different terminal labels even after the same test if the son carries a newly arisen variant found in his descendants [N22]. Inspect the connected branches and calls before treating the labels as a conflict.
2. **Build a per-SNP table before excluding a branch.** For each informative variant, retain the report's positive, negative, no-call or untested state and distinguish **measured** from **presumed from the tree**. A tree-inferred negative is not an independent measurement confirming that placement. An omitted row is initially unknown: FamilyTreeDNA's documented haplotree view can omit downstream Big Y negatives that are available in the detailed results. Inspect those results before treating the omission as untested or negative. No-call means no resolved result, not an ancestral allele. Preserve coverage/quality information and reconcile variant identifiers and coordinates before comparing. (Rowe-Schurwanz, 2024-07-02; 2024-09-05)
3. **State the remaining conflict at the right level.** Compatible placements do not by themselves establish the specific relationship; reliable incompatible lineage-defining calls require sample, calling and pedigree checks. A single newly acquired downstream variant is not equivalent to belonging to an incompatible paternal lineage. Route a disputed call for qualified review or suitable confirmation; do not turn a display discrepancy into a localized NPE. (Estes, 2024-05-02; comparison synthesis)

The output is **tester → documented path → test/tree → SNP → reported state → measured or inferred → unresolved check**. Keep the source report so a later tree update does not overwrite what was observed.

**Weigh each call before it places, excludes or links.** Some markers listed as a branch's equivalents also read derived outside it, so require a reliable equivalent or a downstream variant. An ancestral read at a false-negative-prone SNP is a weak exclusion. Ancestral calls at sibling subclades leave the last one likely, not proven ([equivalent caution](https://genarchivist.net/showthread.php?tid=1590); [sibling-elimination discussion](https://genarchivist.net/showthread.php?tid=86)). For each negative used to split a block or set a basal node, record its read count and quality, and inspect the reads ([read list](https://genarchivist.net/showthread.php?tid=1497); [low-quality negative](https://forum.molgen.org/index.php/topic,10534.0.html)). Convert coordinates to each file's build before reading a state, and resolve SNP names by position ([build example](https://genarchivist.net/showthread.php?tid=2491); [naming exchange](https://genarchivist.net/showthread.php?tid=318); [position comparison](https://genarchivist.net/showthread.php?tid=275)). A variant shared with an incompatible haplogroup, or any single shared mutation, may be a recurrence, not a link ([shared-mutation explanation](https://genarchivist.net/showthread.php?tid=1161); [incompatible-haplogroup recurrence](https://forum.molgen.org/index.php/topic,10534.0.html)). Take unreliable markers from the tree, not from memory. No source gives a read-count threshold; the mapping-quality ≥30 filter in the build example is one replier's choice, not a standard.

### Choose a tester who can split the unresolved SNP block

**Name the question before recruiting.** Several equivalent SNPs share a block because the available results have not resolved their order. They are distinct variants, not interchangeable names for one mutation. Do not distribute them among successive named ancestors from their display order. (Rowe-Schurwanz, 2024-07-02)

**Privacy gate:** <!-- privacy-gate: contact --> Recruiting a male-line cousin as a tester means contacting a living person about Y-DNA testing; answer the privacy gate in `SKILL.md` first.

- **Naming shared variants and ordering them are different gains.** A close patrilineal relative may establish that private variants are shared, allowing placement on the tree while leaving them together in one block. To resolve an older split, seek a documented male-line descendant through another son of the relevant ancestor; the useful result would separate shared upstream variants from downstream ones. Choose an assay that can resolve the relevant sites. Such a cousin creates an opportunity for a split, not a guarantee. (Rowe-Schurwanz, 2023-11-22; selection synthesis)
- **Read a proposed split against the calls.** Positive results for some block variants and reliable ancestral results for others can support subdivision. No-calls cannot supply the negative half. Even a supported split does not by itself identify the named man in whom each mutation arose. (Rowe-Schurwanz, 2023-11-22; 2024-09-05)
- **An unchanged label is not a failed experiment.** Inspect the variant evidence. It may add shared variants without resolving their order, or leave the placement unchanged. FamilyTreeDNA describes tree refinement as evidence-driven aggregate analysis; do not promise every kit an individual manual review followed by a changed haplogroup on a fixed schedule. (Rowe-Schurwanz, 2023-11-22)

**Bracket a SNP before naming the man in whom it arose.** Positive descendants of one man can share a variant inherited from further up his line [N114 @2026-11-12]. The University of Strathclyde’s criteria require positive descendants through at least two of his sons and a measured negative through at least one brother [N116 @2026-11-12]. Compare the pedigrees and that SNP’s actual calls. One positive brother’s branch and one negative brother’s branch can narrow the search [N115 @2026-11-12], but carriers all descending through one son leave later generations possible. A no-call supplies no negative evidence.

### Keep predeceased sons in the tester worklist

Before closing a candidate Y-DNA branch because an obituary names no surviving son, compare
the notice with the documented child roster. Check whether a son who died earlier left sons,
and trace the relevant male-line descendants with evidence for each parent-child link. For a
living descendant, record only name, parents and place in the family; do not look up current
contact details, and stage any contact through
[DNA match outreach staging](dna-match-outreach-staging.md). A predeceased son could leave a continuing male line even when the obituary lists no surviving son [N85]. Keep branches without documentary follow-up unresolved.

## Prompt-craft (how to keep an assistant honest here)

1. **Assign nothing; route it.** For any haplogroup/tree question, output "check FTDNA Discover / Mitotree" — do **not** name a haplogroup or its meaning from memory. (The Anzick failure is precisely a from-memory assignment.)
2. **Separate GD from loci, events and time.** State the compared panel and scoring rules; never infer the number of differing markers or historical mutations from GD alone. For "how many generations?", use the report's resolution-dependent range, not an invented conversion or a single date.
3. **Name the resolution ceiling before interpreting a match.** First establish the Y-STR level (Y-37, Y-111, or legacy Y-67) vs Big Y-700, or mtDNA HVR vs full-sequence — the same match means different things per level; interpreting without the level invites the exact-match-is-recent fabrication.
4. **Name the positions before ranking mtDNA matches by GD.** Don't call a GD0 "closer" than a GD1/GD2 without checking which positions produced each count — a GD1/GD2 whose differences sit on unstable/fast-mutating positions can be as relevant as a GD0, whose own apparent exactness can just as easily hide a real difference at an *excluded* position (309/315) that never entered the count. Never state 16519 (or 16189/16193) as GD-excluded — a haplogroup tree list may leave some of them out, but they still count toward GD; only 309/315 are excluded.
5. **Force the alternative-explanations list before any NPE language.** If a contradiction/absence appears, enumerate untested-descendants, sequencing error, same-name, wrong-generation, pre-surname — *then* ask what corroboration exists. Use "flag / needs corroboration," never "proves."
6. **Separate the STR-surname question from the SNP-branch question.** Surname clustering (STR projects) answers "who might share a recent paternal line"; terminal SNP / Big Y answers "how recent." Don't let one stand in for the other.
7. **For differing Y labels or a proposed branch split, request the per-SNP table above.** Separate measured calls from tree inferences; state whether the next tester could name a shared variant, resolve its order, or only check a recent transmission.
8. **For a date conflict, retain both accounts.** Request the dated node/pair, interval, report version and documentary descent; distinguish incompatible variant evidence from a disagreement with a dating model.
9. **For a match across test types, name the path each result supports.** Do not attach the autosomal connection to the Y/mt line solely because the same pair matches on both tests.
10. **Every output is a hypothesis to verify** against the actual vendor tools, autosomal DNA, and documents — the shared spine with `ai-for-dna-research.md`.

## Pitfalls worth internalizing (least-obvious, most-LLM-usable)

- **Verify a proposed haplogroup.** Confirm it in the tester’s report and the dated tree before using it to identify or date a shared branch [N16].
- **Date surname adoption locally.** Compare the estimated paternal ancestor’s interval with historical records of surname use in that place. A hereditary surname may have been adopted after the paternal lines separated, as surname use varied by place [N4]. In the Netherlands, the 1811 decree required people who lacked a family name to adopt and register one. Check the local registers of surname adoption for the family [N148].
- **Check what an autosomal chip actually measured.** Its Y or mtDNA calls may support only an upstream branch. Compare the chip’s covered positions with a dedicated test before interpreting a difference in resolution [N15], [N23].
- **A chip-derived Y terminal shows where the chip's SNPs stop.** Record the vendor and chip version, or mark it inferred or unknown. Sort each downstream branch marker into tested-negative or absent from that version, searching equivalent names too. Only a tested-negative excludes a subclade. A SNP discovered after the chip was designed will not be on it under that name, though an equivalent at a probed position may still be callable ([N73]; [N71]; [N74]). Look up the raw call for each assigning SNP, and check any assigning SNP that recurs on another branch. A positive that conflicts with a positive on a sibling branch is a probable bad probe ([N76]). Two predictions from one file conflict only if neither is upstream of the other ([N77]). A second classifier on the same file checks consistency, not correctness ([N75]). Never fill in a subclade from an AI guess; a downstream share among upgraded testers is a population estimate, not this tester's result. The community SNP lists remain unverified.
- **Date the tree and inspect its coverage.** New testers can change branch assignments, age estimates and the inferred geography of sparsely represented paternal lines. Record the tree, date and sample behind a migration map [N11].
- **A label string is not a clade.** Keep each haplogroup label with the tree or tool that assigned it, its version or date, its input, and the point where assignment stopped. Do not silently replace a vendor label with a deeper third-party one ([N40]; [N41]). Long-form and longhand names are renumbered between releases. A proposed name can also coincide with a vendor name for a different clade. So compare defining variants, and anchor on the source's SNP-named label ([N37]; [N38]; [N39]). Keep a generated or unsourced name-to-SNP mapping unresolved. A shallower label in a second database may only mean it lacks another carrier of the downstream variant. Check the first provider's SNP results before calling it a conflict, and do not promise an update ([N42]). None of these sources validates an assignment.
- **Branch flags, country counts and frequency maps are tester tallies.** Run these checks before reading them as origin or frequency. Count documented close kin, such as a father and son or brothers, once, and record the relationship evidence ([N43]). Assume the same sequence may appear in several public trees. Keep entries of unknown provenance flagged, so a combined count is an upper bound ([N44]). Note which communities test heavily, and compare at subclade level ([N45]). Many testers stopped at an upstream SNP, so downstream shares rest partly on unresolved kits ([N46]). State a count as observed in that database on that date. Do not correct it yourself or swap in an unsourced published frequency. No source measures the bias.
- **A branch's size is not its age or founder status.** Do not read a large branch, or a lineage's large share of one community's Y results, as evidence that the lineage entered that community early or is old. Size depends on how many male-line descendants survived and how many of them have tested; a thin sibling branch may be under-sampled, not extinct. Take a branch's age from the tree's dated estimate, labelled as a formed age or a TMRCA (see the formed-versus-TMRCA rule above) [N89].
- **Origins reported by matches are a location lead, not an origin finding.** For a
  paternal-origin question (England vs Ireland, England vs Germany), tabulate the earliest known
  ancestor and place reported by each Y match or nearby Block Tree non-match. Label each entry as
  self-reported and note its test level and branch. A pattern can show the question is worth
  asking, but it does not answer it, verify those trees, or date a migration. The pattern depends
  on who has tested. Use the place pattern to select candidate records and verify the reported origins on the direct paternal lines [N30], [N31].
- **A notable-connection report is a haplogroup comparison, not a pedigree.** Before any documentary search for a link to a famous person, read the report's estimate of when the shared direct-line ancestor lived; most such ancestors lived thousands of years ago. Attempt documentary proof only when that ancestor falls inside the region's paper-trail era, because proof needs a record for every generation on both direct lines and DNA does not supply them. Record how the notable's haplogroup was obtained: tested directly, deduced from tested descendants, or inferred from living collateral relatives (more common than descendant testing). Any label not tested directly also rests on the documented kinship between those testers and the notable. [N87]
- **A match to a named lineage's project tests descent, not group membership.** When a same-surname tester compares with a chiefly family's Y-DNA project, such as a Scottish clan chief's line, a match is a clue that the tester descends from that family's male line. Before calling it a match to that family, apply the resolution and surname-cluster rules above, and compare the estimated common ancestor's date with when that surname was adopted in the region (see the surname-timing pitfall above). Do not report a match as membership in the clan or other group that bore the name, and do not read a mismatch as excluding that membership. Membership is a separate documentary question for the records of the specific ancestors. [N88]
- **mtDNA is a weak genealogical instrument by design** — slow mutation, fewer testers, wide match ranges. Great for *eliminating* a direct-maternal-line hypothesis, poor for *pinning* a relationship.
- **An mtDNA label is only as deep as the positions behind it.** Record the tool, the tree build and the regions sequenced. For each candidate, record the matched, extra and untested or no-call defining positions. HVR-only data support at most the shared parent of tied sibling subclades, so keep a deeper label provisional until coding-region calls support it ([N78]; [N79]; [N57]; [N54]; [N80]). Check the base each mutation requires against the observed base, reading '!' by the tree's convention ([N81]). Read a label's parent from the tree path, not from its letters, and after an update check whether the branch was renamed or actually moved ([N49]). When labels or providers disagree, tabulate each node's defining mutations and their stability instead of adopting either label ([N82]; [N41]). None of these sources measures accuracy. Route the current label to Mitotree.

**One FamilyTreeDNA mtDNA page can show labels from two trees.** On the Matches page, the 'mtDNA Haplogroup' column is the PhyloTree Build 17 assignment, now called the Legacy haplotree, and the 'Mitotree Haplogroup' column is the Mitotree one [N117 @2026-11-12] (Estes, DNAeXplained, 2025-04-14 [N118 @2026-11-12]). The results page likewise shows a Legacy badge beside a Mitotree badge marked Beta (2025-09-02 [N107 @2026-11-12]). Record which column or badge each label came from, and compare labels only within one tree: a match's Legacy label set against another tester's Mitotree label is not a conflict. Coding Region matches all share your Legacy haplogroup, yet a match related within a genealogical timeframe can carry a different Mitotree haplogroup, so a different Mitotree label alone does not make a match distant (FamilyTreeDNA, 2025-02-25 [N108 @2026-11-12]).

**Keep historical mtDNA type names with their assay.** Preserve the Finnish label *tyyppi 1* as printed [N158]. Before comparing it with a modern haplogroup, use the original study’s restriction-fragment definitions (study abstract, partially read [N160]). Leave the correspondence unresolved without a documented mapping.

**Use the branch shown on MyHeritage’s Y-DNA Migration Map.** Record the broad haplogroup assigned from the kit’s existing Y markers [N154 @2026-11-22] [N155 @2026-11-22]. Follow the timeline below the map through the ancestral branching points and use the parent and sibling branches to place the result [N154 @2026-11-22] [N155 @2026-11-22]. Treat the route as an estimate for that branch. Use the higher-resolution comparison above when the question requires distinguishing more recent branches.

**Check the endpoint of an mtDNA migration map against the reported result.** In August 2023 one tester with H1n2 reported a FamilyTreeDNA map for H [N156 @2026-11-22]. Check the label and endpoint in the user’s own report. FamilyTreeDNA’s guide to its major-haplogroup maps describes approximate directions [N157 @2026-11-22]. If a map stops at a parent branch, limit the route to that branch and leave the downstream route unresolved.

**Read the denominator beside a Discover country flag or percentage.** A tester’s flag reflects the reported maternal ancestor’s country. A globe marks missing location information [N119 @2026-11-12], [N112 @2026-11-12]. Check the entry against the documented maternal pedigree because it may repeat a family story [N121 @2026-11-12]. Country Frequency also includes academic and research samples [N120 @2026-11-12]. In the published Mauritania example, one entry out of ten gave 10% [N107 @2026-11-12]. Record the counts, the denominator and the report date before interpreting a dark patch on the map.

**Read MyHeritage Y-DNA Country Frequency by reported paternal origin.** Record the country, the number of sampled testers in the branch and the percentage among all sampled testers reporting that country [N154 @2026-11-22] [N155 @2026-11-22]. A large count can come from a large country sample. Use the within-country percentage for comparisons of the sampled groups.

**Compare the same mtDNA subclade across samples.** For each country, divide its count in the subclade by that country’s sample total. For geographic concentration within the subclade, divide the same count by the subclade’s sample total across countries [N158] [N120]. Repeat the comparison for the parent branch. Before comparing a database percentage with a published estimate, check the branch definitions, origins and sample selection in both sources [N158] [N159]. Check whether a project supplied a disproportionate share if sample provenance is available [N158]. Leave the source of any skew unresolved where provenance is missing.

## Keep an ancient-sample catalogue query separate from ancestry inference

For a supplied ancient-sample catalogue, retain its source and date/version alongside the
tester's externally reported haplogroup and assay/test level. Search the exact supplied
label and record the query and returned specimen IDs. If a downstream Y label is absent,
use an actually supplied or inspected tree to record each upstream label tried; do not
invent the hierarchy. An unavailable tree or unknown test resolution stays unresolved.
The [dated British Isles catalogue example](https://dna-explained.com/2022/02/01/dna-from-459-ancient-british-isles-burials-reveals-relationships-does-yours-match/)
supplies this search step.

Keep each specimen's reported sex, burial/location, dated interval and original or
reanalysed haplogroup labels with their source references, as available. Record a linked
tree's observed placement separately, or mark it unavailable. A no-hit concerns only the
catalogue and labels searched; its coverage is not established by that result. A returned
specimen is a catalogue lead, not the tester's closest ancient relative, direct ancestor,
birthplace or migration route. No sequence comparison or relationship estimate follows
from the label lookup.

**Read an ancient sample's tree placement as a floor.** When Discover or a Time Tree shows an ancient sample on the same Y branch as today's testers, the sample is at least on that branch: recovery may be incomplete and no-calls unreported, so it may carry downstream SNPs the testers lack (Estes, DNAeXplained, 2022-10-04 [N122 @2026-11-12]). Low coverage and post-mortem damage often make ancient placements overconservative or wrong (Martiniano et al., 2022, partially read [N123 @2026-11-12]). Do not infer that the sample shares the tester's downstream branch, or that it has no further SNPs. Ancient mtDNA placements carry the same limit (Estes, DNAeXplained, 2025-05-08 [N121 @2026-11-12]).

**Check a proposed Indigenous American direct-maternal connection at the measured subclade.** Relevant founder branches occur within A, B, C, D and X, which also contain lineages elsewhere (Tamm et al., partially read [N124 @2026-11-12]; [N125 @2026-11-12]). Compare the full-sequence path with the specific founder branch [N107 @2026-11-12]. The Ancient Connections report identifies the shared node and its estimated age [N126 @2026-11-12]. In the published comparison, Radegonde Lambert’s inferred X2b4g and Kennewick Man’s X2a share the older X2 node [N121 @2026-11-12]. Limit the inference to the tested maternal line.

Kennewick Man’s sequenced mitochondrial genome lies at the root of X2a [N147]. A match at the older X2 node cannot establish descent from an X2a founder.

**Recheck mtDNA Ancient Connections after an update even if the assigned haplogroup stays the same.** In April 2025 a FamilyTreeDNA tester reported new connections under the same label [N161 @2026-11-22]. Check the user’s own Discover report and record newly displayed samples with the report date. FamilyTreeDNA describes adding connections as new evidence becomes available [N108 @2026-11-22]. Use the shared maternal branch and estimated ancestor’s date to place the connection in time [N126 @2026-11-22].

## Evaluate lineage evidence for historical remains

**Trace a maternal comparison through a sister who shared the proposed individual's biological mother.** Document the descent through daughters at every intermediate generation [N149], [N150], [N151]. The final comparison relative may be a son or a daughter [N150], [N151]. Compare available mtDNA results over the regions both results cover [N150].

**Weigh a Y-DNA mismatch alongside the other identification evidence.** Recheck both paternal paths from their proposed common ancestor for a pedigree error or misattributed paternity [N149], [N150]. Keep the identification under consideration when the maternal comparison, burial context, skeletal findings, dating or historical records still support it [N150]. The Richard III study identified the remains despite a Y-DNA mismatch with distant paternal-line relatives [N150].

## Inventory lineage and test coverage before choosing another tester

Keep separate Y-DNA and mtDNA lineage rows. For each documented line, record its nearest
represented person, ordered upstream ancestors, sources and unresolved links, then attach
the existing tester and actual test type/level. Several ancestors in the same line need
not become separate testing targets. Keep a tree-page navigation bookmark in its own
field: the person used to open the next pedigree page may belong to a different lineage.
The [lineage worksheet example](https://dna-explained.com/2025/02/23/lineages-versus-ancestors-how-to-find-and-leverage-yours/)
supplies this organizational step.

State the unanswered question beside each row and whether the available assay can address
it; retain an unknown assay or insufficient resolution as unresolved. A missing result
can become a search for an eligible descendant, including through another child of an
upstream ancestor. Verify the required descent path before proposing that person as a
tester. The register organizes coverage and next questions; it does not establish a DNA
relationship or authorize contacting, testing or sharing another person's data.

**Privacy gate:** <!-- privacy-gate: contact --> Asking a tester, his family or a male-line relative to supply a sample or take a test, or descendants of other men of the surname to test, contacts living people about genetic testing; answer the privacy gate in `SKILL.md` first.

Before planning a Big Y-700 upgrade of an early Y-DNA kit, confirm that it can run. Early kits can be blocked because the tester has died, cannot be reached or will not reply, or because the last stored vial was used or failed (Estes, DNAeXplained, 2026-01-03 [N115 @2026-11-12]). FamilyTreeDNA says the number of stored samples varies, a sample may already have failed, and customer service can say whether any remain, but it cannot judge a sample's viability before testing [N130 @2026-11-12]. Record such a kit as upgrade-blocked, with the reason, not as not yet upgraded. Then route the row to a brother, son or nephew on the same documented line after checking his descent, or, while the tester is alive, ask for extra swabs and vials to be sent and stored for future upgrades (Estes [N115 @2026-11-12]; FamilyTreeDNA, 2023-08-28 [N129 @2026-11-12]).

**Privacy gate:** <!-- privacy-gate: third-party-tool --> Loading a GEDCOM into DNA Painter places living relatives' names and family links in an outside web tool; answer the privacy gate in `SKILL.md` first.

To list candidate testers for a line from a GEDCOM, load it into DNA Painter's What Are the Odds? tool, choose the ancestral couple, and import only the Y-DNA-line descendants of the man or only the mtDNA-line descendants of the woman; then scan the chart for living candidates (Perl, DNA Painter blog, 2021-05-28 [N127 @2026-11-12]). The tool still offers 'Just Male/Y-DNA line descendants of' and 'Just mtDNA line descendants of', and its import can replace living people's names with initials [N128 @2026-11-12]. The chart holds only what the GEDCOM holds: verify each descent before proposing a tester, as above.

Before recruiting a new tester, search for results already published. Where a WikiTree DNA
Tests entry or another source gives a FamilyTreeDNA kit number, run a web search for
`"KITNUMBER" site:familytreedna.com`. Without a kit number, search the earliest known
ancestor's name the same way. For a maternal line, also search each documented daughter's
name: mtDNA testers seldom appear in surname projects, so a hit usually comes from a
haplogroup or geographic project that lists a woman as earliest known ancestor. A public
project page shows a kit number and earliest known ancestor only when the member opted in,
entered an ancestor, and the administrator enabled public display. A hit or a miss reflects
those settings and search indexing, not whether a tester exists. Record the project URL,
retrieval date and displayed row as project-display data. Verify the descent path from the
listed ancestor before counting that kit as coverage for the row. (Estes, DNAeXplained,
2026-10-23)

**Use local same-surname men to build a tester worklist.** If an ancestor’s parents are unknown, identify the men of his surname in the same locality and census, and recruit a documented, unbroken male-line descendant of each for a Y-37 test [N133]. Compare results across the branches. Higher-resolution testing is informative when the other relevant lines also test [N140]. Use shared SNPs to narrow the documented lines to investigate. A close Y-37 distance alone cannot place the common ancestor.

## Build a maternal pedigree and locality worklist

**Prioritize a maternal branch by its estimated shared ancestor’s date.** Read the shared node and age estimate in the FamilyTreeDNA mtDNA Discover Time Tree, keeping any displayed interval [N108 @2026-11-22]. Compare the estimate with the local paper trail before working through a group’s pedigrees. A tester reported a group of about 90 people with a shared ancestor dated to 1050 BCE [N162 @2026-11-22]. Check the shared node in the user’s own report. Give documentary follow-up to branches whose date and measured results fit the question, regardless of group size [N108 @2026-11-22] [N161 @2026-11-22].

**Build the group’s locality worklist from dated events.** For historical earliest maternal ancestors reported by group members, compare birth, residence and death places on the available public Geni profiles [N162]. Retain each place with its event type, date and profile source. Check the candidate profiles and maternal links against records and leave ambiguous identities unresolved [N162]. Use the documented places to choose records to search and keep the group’s place spread separate from the origin of its shared maternal ancestor.

**Privacy gate:** <!-- privacy-gate: contact --> A question to an mtDNA match or its kit manager
contacts a living person about their maternal line; answer the privacy gate in `SKILL.md`
first.

For each selected mtDNA match, place the reported earliest maternal ancestor beside the
direct-maternal pedigree actually inspected, with sources and unresolved links. Keep the
ancestral location distinct from the residence the match displays, and do not guess a
tester's name or email (Living people, in `SKILL.md`); leave the ancestral country unknown
without maternal-line evidence. Turn missing links or locations into a
specific record search or proposed manager question. A separately documented all-maternal
branch can help distinguish the maternal hypotheses; the match does not identify a mother.
Check the match’s reported earliest maternal ancestor against the tree and the records for each link. Extend the worklist through separately documented daughters when that could distinguish the proposed mothers [N92], [N21].

**Privacy gate:** <!-- privacy-gate: contact --> Asking a direct-female-line descendant of each daughter to take an mtDNA test contacts living people about a parentage question; answer the privacy gate in `SKILL.md` first.

When children credited to one mother may have had different mothers, for example because the father married more than once, recruit a full-sequence tester descended through all females from each daughter; the last tester may be a man (Estes, DNAeXplained, 2024-04-09, partially read [N131 @2026-11-12]). Where possible, confirm each woman's signature with more than one documented descendant, so that one wrong pedigree cannot pass for a different mother. Small differences can arise in descendant lines. Widely separated, well-supported haplogroups in independently documented daughter lines argue against a shared mother (Estes, 2025-09-02 [N107 @2026-11-12]). Matching lines are only consistent with one mother: two wives who were sisters, or cousins through their own mothers, carry the same mtDNA, so the documents must still separate them (Russell, The Legal Genealogist, 2012-07-08 [N132 @2026-11-12]). To see how far apart two different labels are, use Discover's Compare Haplogroups tool, which shows how long ago the two lines are related (FamilyTreeDNA, 2025-02-25 [N108 @2026-11-12]). Verify the underlying assignments and pedigrees before excluding a proposed mother.

## Combining tests: establish which ancestral path each supports

**A pair matching on autosomal DNA and Y-DNA or mtDNA does not automatically have one shared connection explaining both.** The autosomal relationship can be recent on one branch while the direct paternal or maternal connection is much older on another. This matters especially when several paths connect the families. (Rowe-Schurwanz, 2026-04-09; 2026-04-24)

For each result, record **test and observation → eligible inheritance path → proposed ancestor → unresolved attribution**. Trace the relevant direct paternal or maternal descent for both testers; separately retain every documented autosomal path. Use tested relatives and segment/transmission evidence to investigate which path explains the autosomal sharing, following [the multiple-path workflow](ai-for-dna-research.md#untangle-multiple-paths-without-discarding-the-useful-evidence). A documented cousin relationship does not assign every segment. Until the connection is resolved, do not count the two test types as two confirmations of the named ancestor. This is an application of the sources' separate-line warning, not a combined probability model.

**Fictional example:** two documented paternal cousins also have matching full mtDNA results. The mtDNA match leaves a separate maternal-line question; it does not turn their known paternal relationship into a maternal one. Conversely, absent detectable autosomal sharing does not by itself exclude a sufficiently distant direct-line relationship. (Inheritance illustration; autosomal limitation: Rowe-Schurwanz, 2026-04-24)

- **Privacy gate:** <!-- privacy-gate: contact --> Asking known descendants of candidate families to take a Y-DNA or mtDNA test, or male-line descendants of an unplaced cluster's ancestor or of your own line to take Big Y-700, contacts living people about a parentage question; answer the privacy gate in `SKILL.md` first.
- **Hypothesis-test by targeted testing.** To confirm/eliminate an unknown direct-line ancestor, test **known direct-line descendants of candidate families** (paternal → Y; maternal → mtDNA) — a purpose-built corroboration, not a database-luck wait. (Legacy Tree, 2026-06)
- **FTDNA is the only major consumer testing company with Y-DNA and mtDNA *match lists*** (23andMe gives high-level haplogroups, no matching). YFull, an analysis service for uploaded sequencing files rather than a test, reports Y-STR matches (BAM uploads), Y-SNP matches and mtDNA matches. YSEQ's free match-finder tool searches public YSEQ projects and Y-STRs you enter. (YFull FAQ and order page; YSEQ tools page; checked 2026-11-06.) The **Million Mito Project** sharpened mtDNA dating enough to place some subclade MRCAs in a genealogical window (e.g. K1a9b1 ~early 1600s) — so *some* mtDNA questions are now tractable, but only at full-sequence and only with corroboration. (GeneaVlogger, 2026-04)

**Use Y evidence to select a generation for an unplaced autosomal cluster.** When the proposed link follows the direct paternal line, recruit male-line descendants of the cluster's ancestor and of documented branches of your own line for Big Y-700. Shared variants can define a new branch, and the service estimates the common ancestor’s date for the testers on it [N142]. A worked project’s estimated dates shifted as branches were added [N141]. Record the dated node and interval after each addition. Use the interval to choose records to inspect and identify the proposed man through documentary evidence.
