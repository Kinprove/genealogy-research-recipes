---
id: "deed-content-relationship-clues"
title: "Read deed content as dated relationship, probate, migration and parcel hypotheses"
summary: "Read a retrieved deed's type, consideration, estate terms, parties, court-bond security recitals and parcel for dated clues to heirship, probate, migration or land identity."
kind: "records"
scope: {"platforms": [], "tasks": []}
privacy: "none"
gates: []
guardrails: [{"id": "DEED-CONTENT-RELATIONSHIP-CLUES-01", "text": "Every clue here is a dated hypothesis with a stated corroboration need. None is a kinship finding."}]
handoff: []
checked: null
checked_basis: null
capabilities: {"browse": ["record catalogues and original images"], "local_script": [], "extensions": [], "data_transfer": [], "contact": []}
router: {"tier": "pointer", "group": "Censuses, tax, land and property", "order": 1100}
---

# Read deed content as dated relationship, probate, migration and parcel hypotheses

Use this recipe once a deed has been retrieved and you need to read its type, consideration, estate terms, party descriptions and parcel description for clues about heirship, probate, migration or land identity. Every clue here is a dated hypothesis with a stated corroboration need. None is a kinship finding.

Overlapping steps live in sibling recipes:

- Retrieving the instrument, comparing the party roster and recording a wife's release paragraph: [land-record recovery](land-index-book-series-recovery.md).
- Following a fiduciary's deed into the court file: [probate case inventory](probate-case-document-inventory.md).
- Reading deed fields from the image rather than from an AI reading: [AI for documentary records](ai-for-documentary-records.md).
- Heir lists, residence-versus-birthplace and every proof ruling: [evidence/proof judgment](evidence-proof-judgment.md).
- Documentary roles and associates: [FamilySearch workflows §11](familysearch-practical-record-workflows.md).

## Contents

- Errors to block
- 1\. Classify the instrument and its jurisdiction first
- 2\. Test the consideration against the local going rate
- 3\. Keep the inheritance trail open when probate is missing or landless
- 4\. Read party descriptions literally
- 5\. Decide parcel identity before linking deeds
- 6\. Pair migration deeds only after excluding namesakes
- 7\. Return a per-instrument clue register

## Errors to block

Do not do any of the following:

- Read a nominal price, a quitclaim, a dower or spouse release, or a shared surname as proof of kinship.
- Stop the inheritance trail because no probate was found.
- Read "of [place]" as a birthplace.
- Join two deeds or a sale and a later purchase on party name and date alone.
- Merge near-identical surnames, or two transactions with the same grantor and the same date.
- Ignore the instrument type and the estate wording.

## 1. Classify the instrument and its jurisdiction first

Before you read anything for family meaning, label each instrument with its type as written. Possible types are a warranty deed, special warranty, quitclaim, disclaimer deed, dower or widow's release, executor's or administrator's deed, or a conveyance that reserves a life estate or creates joint or survivorship tenancy. Copy the operative wording beside the label.

Type limits what the deed can show:

- **Warranty deed.** Guarantees the title against defects [S7].
- **Special warranty deed.** Warrants only against defects that arose while the grantor owned the land. It makes no promise about earlier owners [S7].
- **Quitclaim.** Passes whatever interest the grantor had and does not warrant that the grantor owned anything [S7]. So it does not certify the grantor's share or relationship. A quitclaim tells you the grantor may have had some claim. It does not tell you what the claim was or where it came from.
- **Disclaimer deed.** The signer states that he or she claims no interest in the property. It is used where community property applies. The presenter explains that in Arizona spouses automatically obtained half ownership of real property, so title work sought a disclaimer deed from a spouse not otherwise provided for in the deed [S7]. A disclaimer by a spouse identifies a spouse on that date. It says nothing about parentage.
- **Dower or widow's release.** S2 describes it as the wife's release of her dower interest when her husband sold the land, or the widow's interest after his death [S2].
- **Jurisdiction check.** Before you interpret a spouse's joinder, disclaimer or release, find out from an authoritative legal-history source whether a community-property or dower regime applied in that jurisdiction on the instrument date. There are nine community-property states today, including Texas, Arizona, New Mexico and California. Utah is not one [S7]. That list describes present law. Do not apply it to an older instrument without a dated legal source for that jurisdiction.

- **Lease and release.** When a lease for a nominal sum and a release of the same tract pass between the same parties, read the pair as one sale, not as a rental and a separate cancellation, and take the price from the release, not the nominal lease sum [S11], [S12]. The lease comes first and may predate the release by a day, a week or even a year, so search up to a year earlier from a release and up to a year later from a lease [S11]. The Legal Genealogist reports the form in colonial America more widely, often in the Northern Neck and older Virginia counties; outside Virginia, confirm the pairing from the local deeds [S13].

- **Wife's examination in a lease and release.** Look for a wife's private examination and dower relinquishment on the release, not on the lease. In a 1751 Albemarle County, Virginia, pair the wife signed both documents but was examined privately only on the release, the document that passed the title [S43]. In a 1753 Frederick County pair the husband alone acknowledged the lease, and both acknowledged the release, the wife being privately examined [S44]. Do not record a missing examination on the lease as a failure to relinquish dower.

- **Dower set off to a widow.** Read a record setting off dower as a life estate in part of her husband's lands, generally one-third, not as an inherited ownership share she could keep and pass on [S14], [S15]. At common law, do not list the widow as her husband's heir [S16]. Statutes could differ, so check the law for the place and date: Illinois's 1845 statute endowed a widow with a third of the lands of which her husband was seized of an estate of inheritance during the marriage [S17], and the same guide reports that a widow whose husband left no child took one-half of the real estate and all the personal estate outright, and kept her dower [S17].

- **"Moiety."** Expect one-half when a deed conveys a moiety, since Black's defines it as "the half of anything," and read "demidietas" or "dimidietas" as half or moiety [S18], [S19], [S20]. Read any stated fraction before assuming, because modern Cornell Wex also records a sense of any set of roughly equal parts [S21]. The Legal Genealogist reads an 1848 North Carolina "two-thirds moiety" as two of three equal shares, so do not dismiss such a phrase as a scribal error on sight [S22].

- **Release deed.** When a deed-book entry is on a printed release form, read the body for what was released before you file it as a paid-off mortgage. A deed of release usually releases mortgaged property [S28], [S41], but a release can give up any right or claim against the person released [S42]. In one 1882 Adams County, Illinois, release the grantor freed the grantee from an agreement to pay his siblings for land their parents had transferred to him [S41]. Record the obligation as written. One owed to siblings or heirs is a family-settlement lead to test against the parents' deed and any probate.

- **Hawaiian deeds.** Do not read a Hawaiian conveyance as an arm's-length sale with no family content. The 1846-1900 deed records of Hawaii's Registrar of Conveyances may give the names of relatives or heirs and dates of death [S38]. Price Genealogy reports that many deeds state a relationship between buyer and seller and how the seller got the land, including inheritance from a named relative; that the books also hold leases, mortgages and adoptions; and that deeds between Hawaiians are usually in ʻŌlelo Hawaiʻi and those involving corporations mostly in English [S37]. In one case, a sale of an undivided interest in two Royal Patents made as one of the patentee's grandchildren, and an earlier lease of the same interest by several heirs, led to a probate and an obituary that named the siblings and parents [S37]. Search the index for "heir of", note each Royal Patent (R.P.) and Land Commission Award (LCA) number to find the Kuleana land petition, and search a one-name person in both the given-name and the surname field [S37]. Search names with and without a leading Ka or Ke, which was sometimes dropped, as in Kawaiahao and Waiahao or Kamoiliili and Moiliili [S37], [S39]. Do not read makua kāne as proof of fatherhood: it also means an uncle or a male cousin of a parent's generation, and a land-terms dictionary adds a mother's husband [S40]. For an AI reading or translation, use [AI for documentary records](ai-for-documentary-records.md).

## 2. Test the consideration against the local going rate

Record the stated consideration literally. Compare it with land values for comparable acreage in the same county and period, using a source you cite. A price far below that rate, a token sum, or a transfer in return for the grantor's lifetime care can point to a family relationship. It can also explain why no probate exists [S1]. Record this as a hypothesis together with the record that would test it, such as a later heir list, the grantee's identity, or a care agreement.

Do not compute the "going rate" from memory. If you have no comparable values, write "not compared". The presenter's remark that most of his own ancestors avoided probate this way is his own experience, not a base rate [S1].

Do not infer the price paid, or kinship, from a $1 or $10 recital alone in a 20th-century or modern deed or deed index. Deeds commonly recite a nominal sum, often with "other good and valuable consideration", so that the actual price stays out of the public record [S46]. One presenter read a $1 entry in a 1939 Belmont County, Ohio, deed index this way, and reports the same figure in newspaper notices of sales [S45]. Unless the deed states the sum as the actual consideration, record it as a nominal recital and the going-rate comparison as "not compared". A nominal recital alone does not separate a full-price sale from a family transfer, so test kinship on the parties, not on the sum.

## 3. Keep the inheritance trail open when probate is missing or landless

There are four routes.

- **Quitclaims among heirs.** When a parent's estate has no will or probate file, search the deed indexes for that parent's land. Look for quitclaims between heirs, or from heirs to a third party. Record each grantor as a possible heir to identify. A married daughter may appear under her married surname [S3]. Being a participant is not the same as being a child. Use [heir lists are not child lists](evidence-proof-judgment.md).
- **Pre-death deed series.** When a probate holds little or no land, search the decedent's grantor index for the period before death. Look for a same-day series of nominal-price deeds of small, apportioned parcels in one area to several grantees. One presenter used such a series as indirect evidence that the grantees were heirs [S4]. Record each grantee as a possible heir. Record the pattern as indirect evidence that still needs correlation. Do not adopt the presenter's tax motive.
- **Fiduciary deeds.** An executor's or administrator's deed in the chain of title means there was a probate. Use the deed date to go straight to the court record [S2]. Then hand the search to the probate inventory recipe.
- **Life estate or survivorship.** Use this route when a child holds the land after a parent's death and there is no deed or probate at the death. Look back for an earlier deed from the parent that reserved a life estate. Under a life estate the property passes to the remainderman when the life tenant dies. Also look for a joint tenancy with right of survivorship, which passes the property automatically to the surviving tenant or tenants [S7]. Record the conveyance date and the end of the life tenancy as separate events. Do not treat the death as the date title passed. The presenter says that US jurisdictions usually require some evidence of the transfer at the death [S7]. Search the chain of title after the death for it, such as a later conveyance by the remainderman or a recital of the life tenant's death. Do not assume nothing was recorded.

- **Heirs' deeds after the widow's death.** When a man died owning land and his widow outlived him, search for his heirs' conveyances after her death as well as after his. What she held as dower went back into his estate for his heirs. The estate should then have been reopened, but often the only record of the division is in the deed books, sometimes only in deeds for the separate pieces sold out of the family years later [S48]. Such a deed may not mention the widow or her death [S47].

- **A widow's will over a life estate.** If a widow's will appears to dispose of the farm, read her husband's will or deed for a life estate before you treat her will as proof that she owned it. A life tenant cannot leave the property by will, because her interest ends at her death, though she can transfer her own interest while she lives [S52]. In one reported family case, a husband left his farm to his wife for life with the remainder to their children, and her will leaving "her property" to one son was denied probate because she lacked title to the farm [S51]. Record her will as an attempted disposition, not as evidence that the named child inherited, and search for the remaindermen's later conveyances.

- **Land in another county or state.** When the owner died holding land outside the county where the estate was probated, search the land county's deed indexes for decades after the death. Titles were usually settled soon after a death, but a later title search could find a defect: in one example, a mid-1940s Nebraska land record dealing with a title left unsettled at an 1890s death in Illinois named the owner, his estate and his Illinois will [S49]. A guide to Pennsylvania land records gives the same advice, to check the indexes many years after the person died or left the area, because deeds there could be recorded years or decades after the transaction [S50].

## 4. Read party descriptions literally

- **Wife's or widow's release.** Check the release for her maiden name. List her witnesses as possible relatives to test. The presenter says the release may give the maiden name and may be witnessed by her family [S2]. Witness kinship stays unproven until another record supports it.
- **"Of [place]."** Record it exactly as written, including relative forms such as "of the same place." Treat it as a place tied to the party on the instrument date, usually residence. Do not use it to confirm or overturn a birthplace without a source that states birth [S8].
- **Security for a court bond.** If a deed or deed of trust says it protects a surety on a named court bond, read the recital explaining that purpose, not only the opening parties. Preserve any stated relationship separately from the deed maker, surety, trustee and person bound to appear. Use the supplied names, court, term and dates to queue the corresponding bond or case, then check the cross-reference on the retrieved records. Providing security or acting as surety alone establishes no kinship. [S10]
- **Candidate pool from same-surname parties.** When the parents are unknown, sweep county land records for every party with the surname, starting about 20 years before the target's birth. Then follow each candidate child's own deeds back to their grantors, and note witnesses who recur [S5]. Treat the pool as candidates. Land records seldom name children [S5].
- **Search window.** A deed may not have been recorded until many years after the transaction. The presenter says filing was not required at the time. Search at least 20 years past the ancestor's last known date in the area [S1]. Record the instrument date and the recording date separately, as the land-record recipe requires.

- **Several deeds recorded together.** When a deed was recorded years after it was signed, read the entries recorded at the same time for other deeds to the same grantee. Deeds were entered in the order they reached the recorder, not the order they were signed [S66], [S67]. Some people waited until they had several to record: in 1738 one Middlesex County, Massachusetts, man had four deeds recorded, some signed nearly ten years earlier [S66]. Recording could also wait until the land was sold again, a generation or two later [S67].

- **"Of [place]" against the land's county.** Do not assume a party lived in the county where the tract lies: a deed is recorded in the county of the land, but it often states where each party lived [S28]. When the stated county differs, search that county's census, tax and court records for the party as well. In one Ohio example a buyer of 1815 was "of Knox Co" though his land lay in another county, and the author then found a couple of the right age in a son's Knox County household in the 1820 census [S29]. Name each county as it stood on the instrument date: that land lies in today's Holmes County, which was created only in 1824 [S29], [S30]. When one person's successive patents or deeds change the stated residence from a parent county to a county formed from it, record a boundary change before a move, and search the new county's records for the later years. In an Arkansas example, a patentee first of Izard County was later of Fulton County, created from Izard with effect from 1 January 1843 [S31], [S32].

- **Age of a buyer or lessee.** Do not conclude from a land purchase or lease alone that the party had reached 21, because an infant's contract to purchase land and a lease to an infant were voidable, not void [S23], [S24]. The Legal Genealogist applies this to land deeds where a jurisdiction treats minors' non-necessary contracts as voidable and says land generally was not a necessary [S25].

- **How the seller acquired the land.** Read the land description in a seller's deeds for the source of title, not only for location, because deeds can show who the grantor got the land from and the grantor's relationship to a previous owner [S26]. The Legal Genealogist reports Wilson County, Tennessee, deeds of 1828-1829 where wording such as land formerly owned by, or deeded by, "my father" named a father [S27]. Such a recital does not by itself distinguish among same-named men in the county, so record it as a hypothesis until that is resolved [S27].

- **Proof of a deed your target only witnessed.** The Legal Genealogist reports one Tennessee deed of 1831, proved in 1836-1838, where those proving the handwriting of a witness who had left the state stated their kinship to that witness, and the father and siblings they named were used to eliminate one same-named candidate father [S27]. The author therefore reads such court proofs instead of skipping them as boilerplate [S27]. The elimination rested on the absence of a recorded son, so treat it as a lead and not as proof [S27].

- **Marriage settlement.** Read a marriage settlement, a deed or trust made before a wedding so that the bride keeps her property, for its trustee and witnesses as well as the couple. Such settlements created a separate estate for the wife and could name a trustee to protect it; simple settlements needed none. Where one is named, a relative could serve: in a 1783 settlement filed in Charleston the trustee was the bride's brother-in-law [S34]. In a Clarke County, Georgia, settlement of 1830, the author read the trustee as further indirect evidence that he was the bride's brother, and asked whether a witness was a half-sister under her married name [S33]. List the trustee and each witness as possible kin to test against other records; that deed itself stated no relationship [S33].

- **Names in the boundary description.** Read every name in a metes-and-bounds description, not only the parties. An adjoining owner named in the calls can be a relative whose connection the deed does not state, such as a married daughter under her husband's surname [S54]. In a 1780 Massachusetts sale, the description named the seller's mother under her new married name without saying she was his mother [S53]. List each named adjoiner as a possible relative to test against other records.

- **Deed witnesses.** Do not assign one witness to the husband's family and one to the wife's, as a guidebook did [S55]. Colonial law asked only that a witness be credible, meaning competent to testify and without an interest in the transaction; Virginia's 1710 act, for example, required deeds for land to be proved by two or more credible witnesses [S56]. Treat each witness as an associate lead. Research first the witnesses who recur on documents the person signed, especially across years and places [S55], [S57].

- **Chain carriers.** Read a name marked CC, CB or SCC on a survey, plat or grant as a chain carrier, who carried the surveyor's measuring chain, not as a witness or a party [S58], [S59]. Do not infer legal age from a plain CC: a Tennessee land glossary reads C.C. as possibly under legal age and S.C.C., a sworn carrier, as having reached it [S82], and a Cumberland County, North Carolina, page gives 14 as the minimum age for male carriers [S83]. Family members commonly carried the chain [S60], [S82]; the man having the survey made very often had relatives carry it, especially brothers-in-law, but carriers could be anyone [S61]. List them as possible kin of the landowner to test.

- **Mortgage lenders.** Go through every mortgage and trust deed in a person's series and identify each lender or note holder. In the early years mortgages and trust deeds were usually made with private individuals, and banks became the usual lenders only as banking grew during the 19th century [S50]. In an 1879 trust deed, a couple borrowing against their farm borrowed from the wife's mother and stepfather, and the instrument did not say so [S62]. In another family, one mortgage in a long series was to the borrower's in-laws and revealed a family conflict the researcher had not known of [S63]. List each private lender as a possible relative to test; the instrument usually states only the debt, the collateral and the terms [S62].

- **Separation recited in a deed.** When a spouse remarried and you find neither the other spouse's death nor a divorce, search the deed records where the couple lived. A deed between husband and wife can divide their property and state that they had separated without a divorce, as one Kentucky deed of the 1860s did [S64]. An 1854 separation agreement recorded in a Crittenden County, Kentucky, deed book released the husband's claim to the property his wife had from her father [S65]. Record the deed date as the date by which the separation is documented, use a separation date only where the deed states one, and do not record the deed as a divorce or a death.

## 5. Decide parcel identity before linking deeds

To test whether two deeds or mortgages concern the same land, compare:

- boundary calls and shape;
- book-and-page citations of earlier deeds;
- acreage or dimensions;
- adjoining owners named.

Record a "part of" relationship when a small earlier lot was absorbed into a larger later tract. Do not record it as identity. Neighbours who do not match point to a different tract even when the date and grantor match. In the presenter's parcel comparison, a deed recited the same original date and grantor as another transaction yet concerned a different lot [S9].

The Legal Genealogist reports, from one 1848 Caldwell County, North Carolina, deed of a two-thirds share of inherited land, that to own the whole tract the buyers would have had to acquire the remaining third separately from the children of a brother who had died [S22]. On that example, do not record a buyer of a fractional share as owner of the whole tract or the named sellers as the only heirs, and search for separate conveyances of the remaining shares [S22].

Keep an in-and-out table of each person's land: every parcel, its acreage, the record by which it came and the record by which it left. The acres acquired should equal the acres disposed of plus any still held at the end of the period you traced, apart from small surveying differences [S68]. A parcel with only an out entry, a parcel with only an in entry that the person no longer held, or acres that do not balance, means a transfer is still missing. Look for it in probate as well as in the deed books, since after the first title ownership passed by deeds and wills [S71], and outside the years you searched [S69]. In one Ontario case, full-text search found a purchase of 21 acres and a sale of 27; a gap like that calls for a search of the grantor and grantee indexes by hand. Full-text search need not find every deed [S70], and its AI transcriptions contain errors [S72].

Keep near-identical surnames (Wilmer/Wimmer in that example) as separate parties until other evidence joins them [S9]. Where a citing deed's date disagrees with the cited deed's own body, acknowledgment and cover note, keep both readings. A proposed misreading (13th/30th in the example) is a hypothesis to check on the image [S9]. That analysis was AI-assisted: Claude compared her own transcriptions, and she said she still needed to double-check the details [S9]. Verify every call and citation on the images yourself.

To place a metes-and-bounds tract on a modern map, do not work from one description. Collect the calls from every grant, survey and deed for the man's tracts, and from each neighbour's grant or survey that names him as a corner, such as the side of a river, a mountain, ridge, valley, creek, spring, road or adjoining owner, then look for the one area where they all fit [S35]. Anchor the assembled plats to a fixed feature such as a river or county line before you overlay a modern map [S36]. Report the result as an approximate location until the original drawn surveys are checked: in the Virginia example the author had only transcribed surveys and listed the county surveyor's books as the next search [S35].

Convert French and Spanish units with the value for the grant's place, not one standard. Arpents appear in formerly French parts of the United States and varas in formerly Spanish ones [S77]. The arpent is both a length of about 192 feet and an area; as an area it is officially 0.84628 acre in Louisiana, Mississippi, Alabama and Florida and 0.8507 acre in Arkansas and Missouri [S78]. The vara varied by time and place [S79]; in Texas surveys it was about 33⅓ inches [S80]. Do not treat an arpent as an acre or a vara as a yard.

In colonial Virginia, landowners were to walk and renew their lines with their neighbours every four years, in precincts the parish vestry defined, and each owner had to attend only to the boundaries of his own tracts [S75]. So do not read a neighbour's absence from one tract's processioning as evidence that the tracts did not adjoin. In a 1755 Augusta County list, one owner attended the processioning of two neighbours who did not attend his; Elizabeth Shown Mills reads this as a line shared with each, settled at their walks, which left them no reason to walk his other lines [S73]. Processioners usually went from farm to farm along the roads, so names next to each other on a list were neighbours and often kin [S74]. To rebuild the route, use the road orders in the county court order books: the Virginia Transportation Research Council has published extracts for several counties, among them Augusta County for 1745-1769 [S74], [S76].

## 6. Pair migration deeds only after excluding namesakes

A sale in the origin county and a purchase in the destination county by the same name supports a proposed move [S6]. The same applies when someone buys and later sells the same acreage, which can suggest departure [S1]. Before you link them, rule out two different people with the same name. Use the parcel, spouse, witnesses and other people in each locality [S6]. Check that the county and state boundaries for each date are correct [S1].

For a family that moved, get every deed in the county they left in which they were grantors, including deeds made or recorded after they seem to have gone, because a sale there could be completed after the move [S81]. Read each for the grantor's stated residence, and note where and before which official the acknowledgment was taken: the sale may name the new county, and the acknowledgment places the grantor where that official could act on that date [S81], [S28]. A clerk could wait for an acknowledgment from a grantor in another county before recording, so recording could follow by days or weeks [S28]. Treat a place found this way as a destination lead, and pair it with a purchase there only after excluding namesakes.

## 7. Return a per-instrument clue register

For each instrument, record:

- locator and instrument type as written;
- consideration, and your comparison with the going rate or "not compared";
- estate or reservation terms;
- each party's role and "of" place, verbatim;
- every other person named, with role: adjoiner, witness, chain carrier, trustee, lender or acknowledging official;
- parcel comparison: calls, cited book and page, acreage, neighbours, part-of links.

Then list each clue as a hypothesis. Name the record that would corroborate it: the probate case, an heir list, the wife's identity, or the migration pair. Name the same-name alternative it must survive. Hand every proof ruling to [evidence/proof judgment](evidence-proof-judgment.md).
