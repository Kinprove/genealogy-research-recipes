# Coverage roadmap

This list records record areas that the catalog does not cover yet, so that new recipes can be
chosen from it rather than one at a time. It came out of
[issue 101](https://github.com/Kinprove/genealogy-research-recipes/issues/101). Rows are in the
demand order proposed there. A row is a plan, not a promise of a release.

Each row names the one mistake a future recipe for that area must prevent. A recipe that ships for
the area should state that mistake as a guardrail.

## How the list was measured

Measured on 2026-11-08 against the 136 recipes on `main`. For each area, the recipe bodies were
searched for its record names and place names (for example "SS-5", "Numident", "SSDI", "Dawes",
"Guion Miller", "WO 363", "CWGC", "Loyalist", "Mennonite", "Huguenot", "orphan train", "Lithuania",
"Latvia", "Estonia"), and every hit was read. A keyword hit is not coverage: an area counts as
covered only where a recipe gives a search route for it.

## Gaps

| # | Area | What the catalog has now | Mistake a recipe must prevent |
| --- | --- | --- | --- |
| 1 | U.S. Social Security records: SS-5 applications, Numident, SSDI | No route; one passing mention of a Social Security entry in [burial evidence](../skills/genealogy-research-recipes/recipes/burial-evidence-packet.md) | Treating a person's absence from the SSDI as proof that the person was not deceased |
| 2 | UK and Commonwealth First and Second World War service records | War-dead burials through CWGC in [burial evidence](../skills/genealogy-research-recipes/recipes/burial-evidence-packet.md); Canadian personnel files in [Canadian record routing](../skills/genealogy-research-recipes/recipes/canadian-provincial-record-routing.md); no route for British service files | Reading a missing or burnt First World War service file as proof that the man did not serve |
| 3 | U.S. Native American rolls: Dawes, Guion Miller and agency census rolls | No route. Canadian First Nations and Métis records are in [Canadian record routing](../skills/genealogy-research-recipes/recipes/canadian-provincial-record-routing.md); Aboriginal agency files are in [Australia and New Zealand routing](../skills/genealogy-research-recipes/recipes/australia-nz-record-routing.md) | Discarding a rejected application, although its file can still hold the family's testimony |
| 4 | Baltic records: Estonia, Latvia, Lithuania | No route; [image coverage verification](../skills/genealogy-research-recipes/recipes/archival-image-coverage-verification.md) names the Estonian and Latvian image portals | Searching by today's country instead of the period state and the family's confession, and reading one portal's miss as a lost record |
| 5 | Canadian immigration records | [Canadian record routing](../skills/genealogy-research-recipes/recipes/canadian-provincial-record-routing.md) covers vital registration, war personnel files, Métis and First Nations records and British Home Children; U.S.–Canada crossings are in [U.S. immigration search](../skills/genealogy-research-recipes/recipes/usa-immigration-search-recovery.md); no route for other arrivals in Canada | Reading one passenger-list miss as proof that the person did not arrive in Canada |
| 6 | Caribbean civil registration under British and Dutch rule | Cuba and Puerto Rico in [Hispanic Catholic registers](../skills/genealogy-research-recipes/recipes/hispanic-catholic-register-recovery.md); the 1813–1834 [British colonial slave registers](../skills/genealogy-research-recipes/recipes/british-colonial-slave-registers.md); an overseas civil-registration reference in [French departmental routing](../skills/genealogy-research-recipes/recipes/french-departmental-record-routing.md) | Routing an event by today's country instead of the authority that ruled the place on the event date |
| 7 | Sephardic records outside Amsterdam, and Ottoman records | Amsterdam's Portuguese-Jewish community archive in [Amsterdam archival records](../skills/genealogy-research-recipes/recipes/amsterdam-archival-record-recovery.md); nothing for Ottoman lands | Inferring Sephardic origin from a surname or naming pattern alone |
| 8 | Huguenot and Latter-day Saint membership records, and Mennonite records outside the Netherlands | Dutch Mennonite registers in [Dutch civil and church records](../skills/genealogy-research-recipes/recipes/dutch-civil-church-record-recovery.md); passing mentions otherwise | Reading a parish-register miss as covering a separate church's own membership and baptism series |
| 9 | Occupational records: railroad, guild and company personnel files | Apprenticeship records in [English records beyond the parish register](../skills/genealogy-research-recipes/recipes/english-nonregister-record-recovery.md) and directory listings in [city directories](../skills/genealogy-research-recipes/recipes/city-directory-observation-workflow.md); no route for personnel files | Calling a personnel file lost before finding the employer's successor or archive |
| 10 | Orphan-train and child-placement records | Adoption proceedings and sealed records in [illegitimacy record recovery](../skills/genealogy-research-recipes/recipes/illegitimacy-record-recovery.md); British Home Children in [Canadian record routing](../skills/genealogy-research-recipes/recipes/canadian-provincial-record-routing.md); a caution on orphanage listings in [evidence/proof judgment](../skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md); no route for orphan-train or placing-out files | Treating a placement as a legal adoption without the court record |

## Covered now

These areas were in issue 101's list and now have recipes:

- Italian civil and parish records, including Antenati:
  [Italian Stato civile and parish records](../skills/genealogy-research-recipes/recipes/italian-stato-civile-parish-record-recovery.md).
- Slovakia, Croatia and the rest of the pre-1920 Kingdom of Hungary:
  [historic Hungary routing](../skills/genealogy-research-recipes/recipes/historic-hungary-record-routing.md).
- Austria and the Czech lands:
  [Austrian confessional register routing](../skills/genealogy-research-recipes/recipes/austrian-confessional-register-routing.md).
- Australian and New Zealand births, marriages, deaths and arrivals:
  [Australia and New Zealand routing](../skills/genealogy-research-recipes/recipes/australia-nz-record-routing.md).
- Brazilian parish and civil registers:
  [Brazilian registers](../skills/genealogy-research-recipes/recipes/brazilian-parish-civil-registry-recovery.md).
- Loyalist claims and confiscated property:
  [U.S. military service routing](../skills/genealogy-research-recipes/recipes/us-military-service-type-record-routing.md), §5.
- Welsh nonconformist chapel registers:
  [English records beyond the parish register](../skills/genealogy-research-recipes/recipes/english-nonregister-record-recovery.md), §5 and §6.

## Updating this list

When a recipe for a row ships, move the row to "Covered now" in the same pull request and link the
recipe. When you find a new gap, add a row with what the catalog has now, measured as above, and the
one mistake its recipe must prevent.
