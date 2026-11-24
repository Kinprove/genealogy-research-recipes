---
id: "descendancy-gap-worklist"
title: "Build a ranked descendancy gap worklist"
summary: "Turn \"research the descendants\" into a ranked list of gaps tied to the records each lifespan crosses."
kind: "judgment"
scope: {"platforms": [], "tasks": []}
privacy: "living-person"
gates: ["privacy-transfer"]
guardrails: [{"id": "DESCENDANCY-GAP-WORKLIST-01", "text": "An empty field leaves the event unresolved in this tree. It does not mean the event never happened."}]
handoff: ["gedcom-research-export"]
checked: "2026-11-06"
checked_basis: "opened 2026-11-06"
capabilities: {"browse": [], "local_script": [], "extensions": [], "data_transfer": ["export"], "contact": ["contact"]}
router: {"section": "Research method", "group": "Family trees and research planning", "order": 16}
---

# Build a ranked descendancy gap worklist

Use this recipe when you are researching downward from an ancestor who is already verified, and you have a collaborative tree or descendancy view to work from. "Research the descendants" is too open to act on. Turn it into a ranked list of specific gaps. Tie each gap to the records the person's lifespan crosses, and sweep one generation at a time. An empty field leaves the event unresolved in this tree. It does not mean the event never happened. For the household-by-census grid, use [research documentation § Compare one family across named censuses](research-documentation.md). For finding a missing household, use [U.S. census practical workflows](us-census-practical-workflows.md). For identity and conflation rulings, use [evidence/proof judgment](evidence-proof-judgment.md).

## Do not read a blank as a finding

Turn an empty spouse, death or children field into an open research question. An adult with no recorded marriage may have a spouse or children missing from this tree. Add the marriage or household search to the worklist [S1]. Describe a person as never married or childless only when a source supports it or the search satisfies the negative-evidence gate in the closing section. Cite the evidence for that conclusion.

Keep a recent branch open when it stops at the edge of a public tree. A tree can withhold living profiles from public view, as FamilySearch's public user trees do [S18 @2026-11-22] [S19 @2026-11-22]. Record where the visible line stops and use only the user's supplied materials for anyone who may be living, under the [Living people rule](../SKILL.md#living-people).

## Flag the three gap patterns

For a paper review, have the user print a descendant chart on their own printer and mark each gap beside the person or couple it belongs to [S17]. Turn each mark into a worklist row with a specific record target.

Go through the whole descendancy view and flag every person who fits one of these patterns [S1], [S2]:

1. **Birth but no death.** The person has a birth date but no death date or age at death. They might have died as an infant, or lived to old age and married more than once. A missing death date also leaves the marriage question open [S1], [S2].
2. **Adult with no spouse.** The person lived long enough to marry, but no spouse is recorded [S1].
3. **Couple with no children or too few.** The couple's lifespans allowed time for children, but none are recorded, or very few are. The presenter says that in the 1800s having children was much more common than having none, and that smaller families of one or two children become more plausible in the late 1800s and early 1900s [S1], [S2]. Apply this rule: if the couple's childbearing years fell in the 1800s, flag zero children and also flag one or two children. If they fell in the late 1800s or early 1900s, flag zero children and rank one or two children lower. These are the presenter's search flags, not a demographic norm or evidence that children must be missing. Check the couple's place, years and record coverage before ranking the gap; do not apply an unsourced regional fertility timetable. Check whether the line was compiled surname-only: someone took the direct ancestor in each generation and never added the other children, second wives or other relationships [S2]. A widow who was young enough to still have children at home may well have remarried, so put that on the list too [S2].

Names repeat often within one family, so keep same-named people apart while you flag [S1].

## Rank by source count before working

Check each flagged person's source count before you start research. Do the people with few or no sources first [S1], [S2]. FamilySearch Family Tree shows the number of attached sources on the person's page (Sources tab and Details page). The descendancy view shows icons for record hints, research suggestions and data problems, and a research suggestion can flag "no sources attached". It does not show the count itself, so open the person page to read it. Lower the rank of well-sourced people unless the gap itself is unsourced. The goal is to add what is missing, not to confirm work someone has already done [S2]. Use relatives who already have sources to decide where to search first [S1].

For each person on the list, record: person ID, gap type, source count, lifespan or birth-to-last-known span, the records that span crosses, and the first targets to check.

When a historical death notice gives a grandchild count, group the known grandchildren by their parents and match them against the heirs named in the probate file. Count each grandchild once. Check whom the notice counts and what role each person has in the probate record before comparing totals [S8, S25]. A probate list may name a surviving child while leaving that child's own children unnamed [S8, S24]. If the notice's total still exceeds the number accounted for, rank branches with incomplete child lists higher and search their birth, baptism or household records. Keep the discrepancy open until you can explain it [S24].

## Tie each gap to the records its span crosses

From each lifespan, list every census taken while the person was alive. Then mark each one as name-level, head-only, or largely lost. The name-level censuses that survive are the first targets [S1]. In the U.S., the censuses from 1790 to 1840 name only heads of household, so anyone else appears only as an unnamed tally in the household where they were counted [S4]. The 1890 population schedule was mostly destroyed after the January 1921 Commerce Department fire. Check the surviving fragments, but expect a gap between 1880 and 1900.

Build a census timeline from the person’s dates and jurisdiction:

- **U.S. lifespan, 1819–1893.** For 1820–1840, search the named head of household and test the other members’ age groups [S4]. By 1840 the person might themselves head a household. For 1850 and 1860, free population schedules name individuals, while slave schedules generally identify enslaved people only by characteristics such as age and sex [S12]. Include 1870 and 1880, and check whether an 1890 population fragment survives for the locality [S1, S12].
- **Birth in 1855.** After locating the family, list the census years the child could have lived through. Start in 1860 in the United States or 1861 in England and Wales [S1]. For each subsequent enumeration, check that the person was still alive and living there. In England and Wales, continue through 1921 if the dates fit. The 1931 returns were destroyed and there was no 1941 census [S5]. For someone alive on 29 September 1939, check the separate 1939 Register [S6].

Work out the list from each person's own dates and jurisdiction. Do not reuse these lists as fixed defaults. The presenter calls people in this period comparatively accessible because these censuses exist, and treats that as a factor in choosing whom to research first [S1]. Rank them accordingly.

If a cousin branch stalls and the child list comes from nineteenth-century census households, add the intervals between enumerations to the worklist. Search birth and baptism records by the parents' names, and check death and burial records for children who could have been born and died between counts [S13, S14]. For a possible U.S. death in the year before the 1850, 1860, 1870 or 1880 census, check that census's mortality schedule too [S15].

When a historical child list comes from family accounts, search the birth or baptism registers under both parents' names for every year of the couple's documented residence, including years the family account assigns to no child [S21, S22]. Use the parish or civil district for each residence and log gaps in register coverage [S23].

Censuses are not the only targets. Lineage-society applications can carry documented descendant lines. For example, Sons of the American Revolution membership applications require the applicant to prove direct descent from a Patriot [S3]. Use the documents an application cites as leads for each generation of the descendant line.

## Sweep one generation at a time

Do not follow whatever branch looks most interesting. Jumping around that way is how siblings get skipped, and the connection you needed may be in a skipped sibling's line [S3]. Instead:

- Within each family, go from the oldest child to the youngest. The presenter says most family software programs place the oldest child on the far left, so the sweep runs left to right [S3]. In a vertical list view such as FamilySearch's descendancy view, use birth order instead.
- Identify every child you can for that family, then move to the next family in the same generation [S3].
- Finish the whole generation before you go down to the next one. Record the order you used so a later session can pick up where you stopped [S3].
- Follow an older child across consecutive censuses. Match the other siblings, their ages and their parents before joining the two households [S3]. If the child has moved or the family composition differs, verify the relationship with a birth, marriage or other independent record.

When a DNA match is estimated to be a third cousin, keep other plausible relationships open [S16]. Test the third-cousin hypothesis by starting with the children of verified great-great-grandparents on plausible lines. At each generation, if the match's path is still missing, recheck every sibling's child list before moving down to the next generation [S13]. Compare details about anyone who may be living using only materials the user supplied, under the [Living people rule](../SKILL.md#living-people).

For the 10 Million Names Patriots of Color study, start the sweep from the patriot's entry in the DAR Patriots of Color database [S9]. According to Lindsay Fulton's interview, the study worked down through all children and grandchildren and stopped at births after 1900 [S10†], [S11]. When following that workflow, include births through 1900 and mark later births as outside the sweep. Compare the resulting lines locally with a grandparent or earlier ancestor the user has already identified.

## Close, open or correct each family

In the final review of each cousin branch, check for omitted divorces and remarriages. For deceased people, check marriage records and use newspaper divorce notices as leads to court records [S13, S14]. Log the documented events and reconcile the child lists across the unions. Record the earlier and later surnames at each documented marriage-related name change and carry both into the branch's search targets [S13, S14]. For anyone who may be living, follow the [Living people rule](../SKILL.md#living-people) and work from materials the user supplied.

If the records leave a couple's child list incomplete, follow each spouse's historical sibling lines to see which branches might have inherited family papers. Check the materials the user already supplied for notes, Bible entries or photo captions that name children. Add each name as a lead to verify in the records [S18, S20]. For a parentage question, use the user's supplied materials to identify whether a newly documented child line offers a possible DNA comparison [S20]. Evaluate that comparison with [unknown-parentage analysis](unknown-parentage-wato.md).

**Privacy gate:** <!-- privacy-gate: contact --> Before contacting the relative, clear the gate for the family-history question and any identifying details sent to that relative. Limit the first message to the question about the deceased household and any necessary details about the recipient.

Ask the relative whether they hold notes, Bible entries or captioned photographs about the historical household [S18, S20]. Use a route permitted by the [Living people rule](../SKILL.md#living-people). Stage the message and log it using the consent and disclosure rules in [DNA match outreach staging](dna-match-outreach-staging.md).

Give every family in the sweep log one status:

- **Open:** gaps remain. Name the next records to check.
- **Closed:** a source states the absence, or the absence passes the negative-evidence gate in [evidence/proof judgment](evidence-proof-judgment.md): the records should have shown the event, record loss, coverage gaps and index errors are ruled out, and every search is logged with its date. State the reason and the source. A "never married/no children" tag then tells collaborators this absence was researched [S3]. A search that found nothing does not close the family by itself: keep it Open and log "searched X on date, no entry".
- **Corrected:** research may show that the people in a family are not actually related to each other, or that the family was made up. If so, stop going down. Go back up the line and correct it until you reach the right ancestors, then continue [S1]. Send merge and separation decisions to the human through [evidence/proof judgment](evidence-proof-judgment.md).

If the question is whether a childless subject has surviving relatives and the siblings' lines are documented as ended, restart the sweep at the subject's verified grandparents. Work down through the subject's aunts and uncles to the first cousins and their descendants. Use historical census records to trace the branches, with family trees as leads [S7], [S8]. For anyone who may be living, follow the [Living people rule](../SKILL.md#living-people) and work from family materials the user supplied.

**Privacy gate:** <!-- privacy-gate: export --> A GEDCOM export of the corrected tree can carry recent descendants who may still be living, so answer the privacy gate in `SKILL.md` before exporting it.

Return three things: the ranked worklist, the sweep log with each family's status, and a list of families flagged for correction. Leave out open-ended "research the descendants" suggestions. For exporting the corrected tree as GEDCOM, see [Export research findings to a GEDCOM file without changing what they prove](gedcom-research-export.md).
