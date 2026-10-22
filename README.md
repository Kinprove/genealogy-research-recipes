# Genealogy Research Recipes

Fact-checked recipes that keep an AI assistant from the usual genealogy mistakes, for DNA
evidence and for record searches. One [Agent Skill](https://code.claude.com/docs/en/skills),
packaged for Claude, Hermes Agent and OpenClaw, by [Kinprove](https://kinprove.io).
No Kinprove account is needed to read the recipes.

## Install

**Claude Code** — run in a session:

```text
/plugin marketplace add Kinprove/genealogy-research-recipes
/plugin install genealogy-research-recipes@kinprove
```

**Claude.ai and the Claude desktop app** — open **Customize → Plugins → Add → Add marketplace**,
enter `Kinprove/genealogy-research-recipes`, then add `genealogy-research-recipes`.

**Hermes Agent** — install and explicitly enable the native plugin:

```sh
hermes plugins install Kinprove/genealogy-research-recipes --no-enable
hermes plugins enable genealogy-research-recipes
```

After enabling, ask the agent to discover the plugin with `skills_list` and load
`genealogy-research-recipes:genealogy-research-recipes` with `skill_view`. Skill-only
plugins can become available in an open chat; start a new session only if discovery
has not refreshed. A Hermes Gateway restart is not required for this skill bundle.

Agent tool calls (not shell commands):

```python
skills_list(category="plugin")
skill_view(name="genealogy-research-recipes:genealogy-research-recipes")
skill_view(
    name="genealogy-research-recipes:genealogy-research-recipes",
    file_path="recipes/ai-for-dna-research.md",
)
```

Use a relative `file_path` for a recipe, its corresponding `sources/` file, or
another bundled resource. For example, ask: "Load the Kinprove recipes, read
`recipes/xdna-phasing-judgment.md`, and distinguish what my X-DNA evidence can
support from what still needs verification."

Native plugin skills are read-only, namespaced and explicitly loaded; Hermes does
not add them to the automatic system-prompt skill index. Existing skills with the
same bare name remain separate. The plugin needs no Python dependencies, API keys
or Kinprove account and does not configure the optional MCP connector.

Update the installed plugin with:

```sh
hermes plugins update genealogy-research-recipes
```

**OpenClaw** — install the native plugin:

```sh
openclaw plugins install git:github.com/Kinprove/genealogy-research-recipes
```

OpenClaw asks you to confirm the source and the plugin's skills. Restart the Gateway
after installing. The `genealogy-research-recipes` skill then loads like any other
OpenClaw skill, with every recipe file beside it. The plugin registers no tools or
hooks, needs no Node dependencies, API keys or Kinprove account and does not
configure the optional MCP connector.

Update the installed plugin with:

```sh
openclaw plugins update genealogy-research-recipes
```

## Registries and provenance

These are separate distribution surfaces; adding a native adapter does not
register the package in another host's public catalog.

- **Claude:** this repository already supplies its own `kinprove` marketplace in
  [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json). It is not a
  claim of inclusion in a separate Anthropic-curated directory.
- **Hermes:** the [Hermes plugin catalog](https://hermes-agent.nousresearch.com/docs/plugins)
  lists this package at a separately reviewed exact commit. Install by
  `genealogy-research-recipes` and enable it as above, or use the repository install.
  Catalog updates need a new reviewed SHA-pin PR; a source release alone does not
  move the catalog installation to that release.
- **OpenClaw:** [ClawHub](https://clawhub.ai) publication is separate from GitHub
  installation. For a published Kinprove release, use the explicit registry source:

  ```sh
  openclaw plugins install clawhub:@kinprove/genealogy-research-recipes
  ```

  Check the publisher, version and source commit on ClawHub before installing.
  If that release is not available, use the GitHub install above. The OpenClaw
  runtime plugin ID and update target remain `genealogy-research-recipes`.

To make a direct Hermes repository install reproducible, add
`--ref <full-commit-sha>` to the install command. Public catalog inclusion does not
mean a package is maintained by the host or has received a full security audit.

The native adapters expose bundled instructions, not automatic access to your
DNA accounts or records. They do not make service calls, install an MCP server,
store credentials, send telemetry, or start background jobs. Individual recipes
can describe optional services and commands; executing those still requires the
host's appropriate tools, permissions and any service-specific credentials.

## Publishing to ClawHub (maintainers)

Use a clean checkout of the reviewed commit, with all host manifest versions
synchronized. Publish under the ClawHub `kinprove` owner using an account with
access to that owner. The `@kinprove/` package scope must match it.

```sh
npx --yes clawhub@0.23.3 package validate . --out ../clawhub-validation --json
npx --yes clawhub@0.23.3 package publish . --family code-plugin --owner kinprove --dry-run --json
```

Check that the dry-run reports `code-plugin`, the intended version and the exact
reviewed commit before making a separately authorized live publication. Keep
`--family code-plugin`: Claude manifests coexist in this repository, so automatic
family detection can choose a Claude bundle instead of the native OpenClaw package.
The npm artifact deliberately includes native OpenClaw code and the complete
skill/resources/license tree, not the other hosts' adapters or development files.

A successful dry-run is not a public release. Authenticate securely, publish the
same clean commit with the same flags (without `--dry-run`), and verify its
ClawHub publication/security-check status before announcing availability. Do not
publish to npm merely because this package uses an npm-style scoped name.

## Recipes

- **Evidence:** [evidence, proof and working hypotheses](skills/genealogy-research-recipes/recipes/evidence-proof-judgment.md), [standards audits](skills/genealogy-research-recipes/recipes/genealogy-standards-audit.md), [AI for documents](skills/genealogy-research-recipes/recipes/ai-for-documentary-records.md)
- **DNA reasoning:** [unknown parentage and WATO](skills/genealogy-research-recipes/recipes/unknown-parentage-wato.md), [AI for DNA research](skills/genealogy-research-recipes/recipes/ai-for-dna-research.md), [Y-DNA and mtDNA](skills/genealogy-research-recipes/recipes/ydna-mtdna-interpretation.md), [X-DNA and phasing](skills/genealogy-research-recipes/recipes/xdna-phasing-judgment.md)
- **Measurement and retrieval controls:** [cross-vendor DNA comparisons](skills/genealogy-research-recipes/recipes/dna-comparison-controls.md), [archival images and search coverage](skills/genealogy-research-recipes/recipes/archival-image-coverage-verification.md), [corpus-seeded name searches](skills/genealogy-research-recipes/recipes/corpus-seeded-name-search.md)
- **Record sites:** [Ancestry](skills/genealogy-research-recipes/recipes/ancestry-record-search-recovery.md), [FamilySearch](skills/genealogy-research-recipes/recipes/familysearch-practical-record-workflows.md), [MyHeritage](skills/genealogy-research-recipes/recipes/myheritage-historical-record-search.md), [Newspapers.com title, issue and notice recovery](skills/genealogy-research-recipes/recipes/newspapers-com-search-recovery.md), [Geni](skills/genealogy-research-recipes/recipes/geni-practical-research-workflows.md), [U.S. census](skills/genealogy-research-recipes/recipes/us-census-practical-workflows.md), [U.S. immigration](skills/genealogy-research-recipes/recipes/usa-immigration-search-recovery.md)
- **DNA sites:** [23andMe](skills/genealogy-research-recipes/recipes/23andme-match-research.md), [AncestryDNA](skills/genealogy-research-recipes/recipes/ancestry-dna-match-investigation.md), [FamilyTreeDNA exports and Group Time Tree](skills/genealogy-research-recipes/recipes/ftdna-practical-dna-workflows.md), [GEDmatch](skills/genealogy-research-recipes/recipes/gedmatch-practical-dna-workflows.md), [MyHeritage DNA](skills/genealogy-research-recipes/recipes/myheritage-dna-match-investigation.md), [DNA Painter](skills/genealogy-research-recipes/recipes/dnapainter-practical-dna-workflows.md)
- **Record recovery:** [burial evidence packets](skills/genealogy-research-recipes/recipes/burial-evidence-packet.md), [city directories](skills/genealogy-research-recipes/recipes/city-directory-observation-workflow.md), [land indexes and book series](skills/genealogy-research-recipes/recipes/land-index-book-series-recovery.md), [probate case inventories](skills/genealogy-research-recipes/recipes/probate-case-document-inventory.md), [U.S. military pension files](skills/genealogy-research-recipes/recipes/us-military-pension-file-recovery.md), [Irish Catholic parish images](skills/genealogy-research-recipes/recipes/irish-catholic-parish-image-recovery.md), [Polish originals](skills/genealogy-research-recipes/recipes/polish-index-original-record-recovery.md)
- **Tree connections:** [RootsMagic reconciliation](skills/genealogy-research-recipes/recipes/rootsmagic-tree-reconciliation-workflow.md), [WikiTree DNA tester links](skills/genealogy-research-recipes/recipes/wikitree-dna-tester-links.md)
- **Jewish and Russian Empire:** [name and registration changes](skills/genealogy-research-recipes/recipes/russian-empire-jewish-identity-attribution.md), [conditional naming, town and DNA clues](skills/genealogy-research-recipes/recipes/jewish-genealogy-conditional-hypotheses.md), [emigrant origins](skills/genealogy-research-recipes/recipes/russian-empire-emigrant-origin-recovery.md), [JewishGen](skills/genealogy-research-recipes/recipes/jewishgen-search-family-reconstruction.md), [Beider given names](skills/genealogy-research-recipes/recipes/beider-given-name-variants.md), [HebrewBooks](skills/genealogy-research-recipes/recipes/hebrewbooks-search-recovery.md)
- **Testimony and record episodes:** [Holocaust testimony and survivor sources](skills/genealogy-research-recipes/recipes/holocaust-testimony-source-interpretation.md), [Russian military and Soviet-repression records](skills/genealogy-research-recipes/recipes/russian-military-repression-record-episodes.md)
- **Ukrainian archives:** [Jewish named-list triage](skills/genealogy-research-recipes/recipes/jewish-archival-list-triage.md), [ELIB archival guides and volume identity](skills/genealogy-research-recipes/recipes/elib-ukrainian-archive-reference-books.md)
- **Church and civil registers:** [U.S. vital-registration coverage](skills/genealogy-research-recipes/recipes/us-vital-registration-coverage.md), [U.S. church-record custody](skills/genealogy-research-recipes/recipes/us-church-record-custody.md), [missing marriages](skills/genealogy-research-recipes/recipes/missing-marriage-jurisdiction-search.md), [early New England town books](skills/genealogy-research-recipes/recipes/early-new-england-town-records.md), [Quaker meetings](skills/genealogy-research-recipes/recipes/quaker-meeting-record-recovery.md), [Catholic parish and diocesan holdings](skills/genealogy-research-recipes/recipes/catholic-parish-diocesan-record-recovery.md), [Catholic cross-notations](skills/genealogy-research-recipes/recipes/catholic-sacramental-cross-notations.md), [Hispanic Catholic registers](skills/genealogy-research-recipes/recipes/hispanic-catholic-register-recovery.md), [French-Canadian registers](skills/genealogy-research-recipes/recipes/french-canadian-register-recovery.md), [French and Belgian civil acts](skills/genealogy-research-recipes/recipes/french-belgian-civil-act-extraction.md), [Dutch civil and church records](skills/genealogy-research-recipes/recipes/dutch-civil-church-record-recovery.md), [Amsterdam City Archives](skills/genealogy-research-recipes/recipes/amsterdam-archival-record-recovery.md), [Swedish parish registers](skills/genealogy-research-recipes/recipes/scandinavian-parish-record-recovery.md), [Scandinavian patronymic and farm names](skills/genealogy-research-recipes/recipes/scandinavian-patronymic-farm-name-record-recovery.md)
- **Irish and British records:** [England and Wales GRO indexes](skills/genealogy-research-recipes/recipes/england-wales-gro-index-recovery.md), [English records beyond the parish register](skills/genealogy-research-recipes/recipes/english-nonregister-record-recovery.md), [UK censuses and the 1939 Register](skills/genealogy-research-recipes/recipes/uk-census-and-1939-register-interpretation.md), [Scottish parish and statutory registers](skills/genealogy-research-recipes/recipes/scottish-parish-statutory-record-recovery.md), [Irish civil registration](skills/genealogy-research-recipes/recipes/irish-civil-registration-jurisdiction-recovery.md), [Irish emigrant origins](skills/genealogy-research-recipes/recipes/irish-emigrant-origin-locality.md), [Irish valuation and tithe lists](skills/genealogy-research-recipes/recipes/irish-land-valuation-occupancy-series.md), [transported convicts](skills/genealogy-research-recipes/recipes/convict-transportation-record-chain.md)
- **German records:** [German register entries](skills/genealogy-research-recipes/recipes/german-register-image-recovery.md), [German emigrant origins](skills/genealogy-research-recipes/recipes/german-emigrant-origin-sources.md), [German local censuses and residential registration](skills/genealogy-research-recipes/recipes/german-local-census-registration-recovery.md), [German military records](skills/genealogy-research-recipes/recipes/german-military-record-period-routing.md), [German official gazettes](skills/genealogy-research-recipes/recipes/german-official-gazette-notice-search.md), [German compensation files](skills/genealogy-research-recipes/recipes/german-compensation-file-recovery.md)
- **Russian Empire and Soviet records:** [Orthodox metrical books](skills/genealogy-research-recipes/recipes/russian-orthodox-metrical-book-recovery.md), [Jewish metrical books and rabbinates](skills/genealogy-research-recipes/recipes/russian-empire-jewish-metrical-book-recovery.md), [revision-list households](skills/genealogy-research-recipes/recipes/russian-revision-list-household-chaining.md), [Muscovite census and settler origins](skills/genealogy-research-recipes/recipes/muscovite-census-settler-origin-recovery.md), [estate registration status](skills/genealogy-research-recipes/recipes/russian-estate-registration-status.md), [volost and town administrations](skills/genealogy-research-recipes/recipes/russian-volost-town-administration-records.md), [Old Believers](skills/genealogy-research-recipes/recipes/old-believer-sectarian-record-recovery.md), [Orthodox clergy](skills/genealogy-research-recipes/recipes/orthodox-clergy-record-recovery.md), [imperial service lists](skills/genealogy-research-recipes/recipes/russian-imperial-service-record-recovery.md), [schools and universities](skills/genealogy-research-recipes/recipes/school-university-record-recovery.md), [Soviet personal files](skills/genealogy-research-recipes/recipes/soviet-personal-file-recovery.md)
- **Censuses, tax, land and property:** [Canadian censuses](skills/genealogy-research-recipes/recipes/canadian-census-interpretation.md), [tax rolls](skills/genealogy-research-recipes/recipes/tax-roll-observation-workflow.md), [deed content](skills/genealogy-research-recipes/recipes/deed-content-relationship-clues.md), [U.S. federal land-entry files](skills/genealogy-research-recipes/recipes/us-federal-land-entry-file-recovery.md), [livestock marks and brands](skills/genealogy-research-recipes/recipes/marks-and-brands-record-recovery.md)
- **Courts, legislatures, prisons and institutions:** [U.S. court case files](skills/genealogy-research-recipes/recipes/court-case-file-recovery.md), [U.S. federal court case files](skills/genealogy-research-recipes/recipes/us-federal-court-case-file-recovery.md), [criminal courts and prisons](skills/genealogy-research-recipes/recipes/criminal-court-prison-record-recovery.md), [state legislative private acts](skills/genealogy-research-recipes/recipes/state-legislative-private-act-petitions.md), [births outside marriage](skills/genealogy-research-recipes/recipes/illegitimacy-record-recovery.md), [asylum and state-hospital patients](skills/genealogy-research-recipes/recipes/institutional-patient-record-recovery.md)
- **U.S. military service:** [routing by service type](skills/genealogy-research-recipes/recipes/us-military-service-type-record-routing.md), [Civil War service episodes](skills/genealogy-research-recipes/recipes/us-civil-war-service-record-episodes.md), [20th-century service reconstruction](skills/genealogy-research-recipes/recipes/us-20th-century-military-service-reconstruction.md)
- **Migration and origins:** [immigrant congregations](skills/genealogy-research-recipes/recipes/immigrant-congregation-origin-records.md), [surname-distribution leads](skills/genealogy-research-recipes/recipes/surname-distribution-locality-leads.md), [African American families across 1870](skills/genealogy-research-recipes/recipes/us-freedpeople-record-recovery.md), [Chinese lineage and jiapu](skills/genealogy-research-recipes/recipes/chinese-lineage-jiapu-records.md), [Japanese koseki and honseki](skills/genealogy-research-recipes/recipes/japanese-koseki-honseki-recovery.md)
- **Places, maps, libraries and manuscripts:** [historical place names](skills/genealogy-research-recipes/recipes/historical-place-name-resolution.md), [historical maps](skills/genealogy-research-recipes/recipes/historical-map-record-recovery.md), [published books](skills/genealogy-research-recipes/recipes/published-book-catalogue-and-full-text-discovery.md), [periodical indexes](skills/genealogy-research-recipes/recipes/periodical-index-search-retrieval.md), [manuscript collections](skills/genealogy-research-recipes/recipes/manuscript-collection-recovery.md), [uncatalogued local holdings](skills/genealogy-research-recipes/recipes/local-repository-uncatalogued-holdings.md)
- **Family papers, photographs and oral history:** [family collection intake and capture](skills/genealogy-research-recipes/recipes/family-collection-intake-and-capture.md), [family photographs](skills/genealogy-research-recipes/recipes/family-photograph-attribution-and-dating.md), [family papers and Bible registers](skills/genealogy-research-recipes/recipes/family-papers-and-bible-register-dating.md), [family interviews and oral tradition](skills/genealogy-research-recipes/recipes/family-interviews-and-oral-tradition.md), [repository photograph collections](skills/genealogy-research-recipes/recipes/repository-photograph-collection-search.md)
- **DNA workflows and research planning:** [admixture run scope](skills/genealogy-research-recipes/recipes/admixture-model-run-scope.md), [DNA match outreach](skills/genealogy-research-recipes/recipes/dna-match-outreach-staging.md), [descendancy gap worklists](skills/genealogy-research-recipes/recipes/descendancy-gap-worklist.md)

Each recipe's sources are in [`sources/`](skills/genealogy-research-recipes/sources/).

## Kinprove MCP (optional)

Add `https://api.kinprove.io/mcp/v1` as an MCP connector so the agent can read your own Kinprove
matches and projects.

## License

[FSL-1.1-MIT](LICENSE), © 2026 Kinprove; each version becomes MIT two years after its release.
Third-party data: [NOTICE](NOTICE).
