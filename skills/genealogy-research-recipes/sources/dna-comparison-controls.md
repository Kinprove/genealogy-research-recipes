## Sources (provenance + dates)

> Original Kinprove synthesis. Third-party passages are not reproduced.

Primary documentation opened and checked 2026-10-18. Public documentation confirms
the described scope; it does not verify a signed-in account or every kit generation.

- **H1:** MyHeritage, [DNA Results And Filtering Your DNA Matches](https://education.myheritage.com/article/dna-results-and-filtering-your-dna-matches/),
  sections on searching and filters. The search can target the match's name or an
  ancestral surname. It does not establish the tested person's identity from a hit.
- **H2:** GEDmatch / Andy Lee, [An overview of DNA comparison matrices in Multiple Kit Analysis](https://www.gedmatch.com/education/an-overview-of-dna-comparison-matrices-in-multiple-kit-analysis/),
  approximately 05:52–06:58. The overlap matrix reports common SNP counts for a kit
  pair; no universal minimum local support is supplied by this citation.
- **H3:** FamilyTreeDNA, [Family Finder Matching 5.0 white paper](https://blog.familytreedna.com/wp-content/uploads/2021/08/Family_Finder_Matching_WhitePaper.pdf),
  2021, printed pp. 5–6, matching workflow. Describes chip-set imputation, no-call
  handling, adjacent-segment joining, cM mapping and filtering. It documents that
  method, not every later algorithm version or the cause of an individual discrepancy.
- **H4:** Genome Reference Consortium, [Human Genome Overview](https://www.ncbi.nlm.nih.gov/grc/human),
  GRCh37 and GRCh38 pseudoautosomal-region tables. Coordinates must be interpreted
  against the input's assembly; the recipe intentionally delegates boundary lookup.
- **H5:** MyHeritage Help, [How do I use the Chromosome Browser for shared DNA segments on the MyHeritage app?](https://www.myheritage.com/help/en/articles/12852203-how-do-i-use-the-chromosome-browser-for-shared-dna-segments-on-the-myheritage-app),
  dated 2026-07-21. Describes the app browser's autosomal scope and separately
  distinguishes unsampled markers. No inference about all raw downloads is made.
- **H6:** FamilyTreeDNA Help, [X-Matches](https://help.familytreedna.com/hc/en-us/articles/9134064538895-X-Matches),
  section “Measuring X matches.” List admission requires autosomal qualification;
  X sharing is separate from overall shared cM in that documented list.
- **P1:** Page et al., [Linkage, Physical Mapping, and DNA Sequence Analysis of Pseudoautosomal Loci on the Human X and Y Chromosomes](https://www.pagelab.wi.mit.edu/_files/ugd/8c39a0_415339fd6f6c47728f70d505ae078a55.pdf),
  *Genomics* 1 (1987), 243–256, DOI 10.1016/0888-7543(87)90051-6; author-hosted full
  paper, abstract and introduction. Demonstrates male X–Y recombination and
  inheritance in the pseudoautosomal region. No contemporary array or match-rate
  claim is taken from this historical study.
- **H7:** Family History Fanatics, [The Debate Continues Over Usefulness of Small cM DNA Matches](https://www.youtube.com/watch?v=ZqK9b2Vt6gQ),
  published 2022-04-27. Used for running known-unrelated pairs at the same lowered
  segment threshold as a negative control; the reported true-segment percentages are not
  adopted.
- **H8:** GeneaVlogger with Cairenn Binder, [The Impact of Ancestry's Ban on Forensic Genealogy | Discussion with Cairenn Binder](https://www.youtube.com/watch?v=3xodviufcG4),
  published 2025-11-22. Used for the practice of recording a degraded kit's call rate and
  checking the SNPs read within a segment before trusting a match; the call-rate figures
  and the unnamed study are not adopted.
- **H9:** Family History Fanatics, [Heirloom DNA For Genealogy Sounds Amazing… Until You See This Problem](https://www.youtube.com/watch?v=lMnm4UjIO60),
  published 2026-04-22. Used for the point that coverage gaps in a sparse heirloom kit can
  split or merge segments, which makes the reported cM unreliable; the presenter's
  illustrative ranges are not adopted.
- **H10:** Lisa Lisson with Mary, [Ask Mary Your DNA Questions!](https://www.youtube.com/watch?v=ecwbM9Lc-Gg),
  published 2021-03-12. Used for recomputing a match total from the segment export at a
  common minimum before comparing vendors.
- **H11:** GeneaVlogger, [Answering Live Genealogy and DNA Test Questions](https://www.youtube.com/watch?v=W278DGiDKq0),
  published 2025-07-12. Used for the point that a low minimum for later segments raises a
  vendor's totals; the charted threshold values are not adopted.
- **H12:** GenArchivist Forum, [The quality is deteriorating - 435k vs 677k snps](https://genarchivist.net/showthread.php?tid=2449),
  first post 2026-03-13; [Y and X SNPs missing in new myHeritage raw data?](https://genarchivist.net/showthread.php?tid=1739),
  first post undated; [MyHeritage upgrades its consumer DNA test to whole-genome sequencing](https://genarchivist.net/showthread.php?tid=1999),
  first post undated; [Additional lines/rsids in 23andMe raw data file](https://genarchivist.net/showthread.php?tid=729),
  first post 2024-04-14. Rights: cited reference, not reproduced. Used for inventorying each
  raw file by download date, header and per-chromosome counts, for comparing two files' SNP sets
  and no-calls directly because the same format label covered different marker sets, and for
  keeping file counts separate from a tool's usable counts; reported vendor policies are not
  adopted.
- **H13:** GenArchivist Forum, [FTDNA is updating Family Finder](https://genarchivist.net/showthread.php?tid=2412),
  first post 2026-02-24. Rights: cited reference, not reproduced. Used for recording the assay
  generation of each file; the reported batch and date cutoffs are not adopted.
- **H14:** МолГен forum, [WGSExtract, FASTQ и разные референсные геномы](https://forum.molgen.org/index.php/topic,14971.0.html),
  first post 2023-09-09. Rights: cited reference, not reproduced. Used for building a
  WGS-derived comparison file in the comparison data's reference build instead of lifting
  coordinates over, and for screening a derived file's summary statistics (no-call share,
  heterozygosity) before treating it as comparison input; the posters' figures and causal
  hypotheses are not adopted.
- **H15:** GenArchivist Forum, [Sampling by Country for YFull and FTDNA](https://genarchivist.net/showthread.php?tid=106),
  first post undated. Rights: cited reference, not reproduced. Used for treating excess
  heterozygosity, sex-chromosome calls inconsistent with known sex, and implausible matches to
  known samples as signs of a bad sequencing-derived file.
- **H16:** GenArchivist Forum, [Dante's hell](https://genarchivist.net/showthread.php?tid=1345),
  first post 2024-12-21. Rights: cited reference, not reproduced. Used for the point that a
  variant-only VCF yields limited chip-format data and that a BAM rebuilt from a VCF adds no
  coverage, so BAM/CRAM is the conversion source.
- **H17:** GenArchivist Forum, [MyHeritage Update June 2024](https://genarchivist.net/showthread.php?tid=939),
  first post 2024-06-27. Rights: cited reference, not reproduced. Used for converting a WGS BAM
  to a chip-format raw file before upload, which makes the uploaded kit a derived input.
- **H18:** МолГен forum, [GEDmatch Genesis](https://forum.molgen.org/index.php/topic,10116.0.html),
  first post 2017-06-22. Rights: cited reference, not reproduced. Used for keeping one match's
  several platform kits as separate rows with their compared-SNP overlap; the poster's causal
  explanation is not adopted.
- **H19:** МолГен forum, [LivingDNA](https://forum.molgen.org/index.php/topic,10423.0.html),
  first post 2017-10-27. Rights: cited reference, not reproduced. Used for recording
  self-conversion and receiving-site imputation per kit when one match's total differs widely
  between services; the chip SNP counts and imputation confidences are not adopted.
- **H20:** GenArchivist Forum, [Timber is deeply, deeply flawed](https://genarchivist.net/showthread.php?tid=137),
  first post undated. Rights: cited reference, not reproduced. Used for comparing another
  vendor's total with Ancestry's unweighted figure rather than its Timber-adjusted total.
- **H21:** GenArchivist Forum, [Multiple AncestryDNA Tests](https://genarchivist.net/showthread.php?tid=905),
  first post 2024-06-17. Rights: cited reference, not reproduced. Used for treating a direct
  comparison in another tool, made when an Ancestry match is missing or reduced, as a separate
  measurement.
- **H22:** Family History Fanatics, [Do Chromosome Segment End Points Matter? | Genetic Genealogy Explained](https://www.youtube.com/watch?v=3vWBeFUBVdg),
  published 2021-02-03. Used for the example of one provider's segment overlapping several
  fragment rows in another report, applied as a one-to-many crosswalk that keeps every fragment;
  the proposed endpoint tolerance and any cause of the provider difference are not adopted.

X reporting table, checked 2026-11-06 (H6 supplies the FamilyTreeDNA row):

- **H23:** 23andMe Customer Care, [DNA Relatives: Detecting Relatives and Predicting Relationships](https://support.23andme.org/hc/en-us/articles/42963245607063-DNA-Relatives-Detecting-Relatives-and-Predicting-Relationships),
  updated 2026-11-05. DNA Relatives compares autosomes and X; the parent-child segment counts
  (a male shares 23 segments with his mother). It does not say whether the percentage includes X.
- **H24:** GEDmatch, [One-to-Many DNA Comparison](https://www.gedmatch.com/applications/one-to-many/),
  undated. The "(X-DNA) Total cM" and "(X-DNA) Largest" columns.
- **H25:** GEDmatch Support, [How to Use GEDmatch DNA Matching Tools (One-to-Many, One-to-One, Segment Search)](https://support.gedmatch.com/portal/en/kb/articles/how-to-use-gedmatch-dna-matching-tools-one-to-many-one-to-one-segment-search),
  undated. The separate One-to-One X DNA comparison tool, which compares only the X chromosome.
- **H26:** AncestryDNA, [Matching White Paper](https://www.ancestrycdn.com/support/us/2025/01/2025matchingwhitepaper.pdf),
  last updated 2025-01-10. Timber windows "on autosomal chromosomes 1 through 22" and phasing
  "across the autosome"; it states no X matching. Roberta Estes, [Understanding X-DNA Inheritance Video](https://dna-explained.com/2026/03/16/understanding-x-dna-inheritance-video/),
  DNAeXplained, 2026-03-16, a secondary source, says FamilyTreeDNA is the only genetic genealogy
  company to include X-DNA matching with autosomal results.
- **H27:** MyHeritage Help, [What type of DNA test is used for DNA Matching?](https://www.myheritage.com/help/en/articles/13130239-what-type-of-dna-test-is-used-for-dna-matching),
  dated 2026-07-21. DNA Matching uses autosomal DNA.
- **H28:** MyHeritage Help, [In the Chromosome browser, is it possible to distinguish between DNA segments which were inherited from the paternal and maternal side?](https://www.myheritage.com/help/en/articles/12852329-in-the-chromosome-browser-is-it-possible-to-distinguish-between-dna-segments-which-were-inherited-from-the-paternal-and-maternal-side),
  dated 2026-07-21. The X chromosome is not shown in the chromosome browser; X support is planned.

## Synthesis boundaries

The exact-test registry, known-positive query check, result-status table, local
coverage requirement and reciprocal-row reconciliation are original methodological
synthesis. The sources establish concrete measurement limitations; none supplies a
universal “good overlap,” sensitivity threshold, relationship ceiling or error rate.
An operational control checks the operation and scope exercised, not all claims
about the tested person. No family data, private kit identifiers or account findings
are part of this recipe.

<!-- provenance-ledger:start -->
```yaml
schema: 1
sources:
  - {"id":"H1","kind":"unknown","urls":["https://education.myheritage.com/article/dna-results-and-filtering-your-dna-matches/"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"720466121514d345cd9a3a3b389b036dde43c26b1ffa40df1ce9ec145b1b1738","claims":["C-8f6c8c186ccf"],"review":"pending"}
  - {"id":"H2","kind":"unknown","urls":["https://www.gedmatch.com/education/an-overview-of-dna-comparison-matrices-in-multiple-kit-analysis/"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"497c0b166dc611949f1116c5c5a8b00caf4bcaa8e11a26f4cd22cf43229a999d","claims":["C-7d4534e420b7"],"review":"pending"}
  - {"id":"H3","kind":"unknown","urls":["https://blog.familytreedna.com/wp-content/uploads/2021/08/Family_Finder_Matching_WhitePaper.pdf"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"cd3c19f0a1de142685665f8146a93633b07e15b649ddf4fa81ccd7dd7490579e","claims":["C-7d4534e420b7","C-1f84740c5c43"],"review":"pending"}
  - {"id":"H4","kind":"unknown","urls":["https://www.ncbi.nlm.nih.gov/grc/human"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"88dd6dbc43b0fc16b054e2f0f61ab1b825d771a588d7733008022de33df664c5","claims":["C-8bf30a429d08"],"review":"pending"}
  - {"id":"H5","kind":"unknown","urls":["https://www.myheritage.com/help/en/articles/12852203-how-do-i-use-the-chromosome-browser-for-shared-dna-segments-on-the-myheritage-app"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"86a2010b22a494a030fac40c5203cc9f02e56bba04471093ef720e3953069138","claims":["C-6097b2a63b9f"],"review":"pending"}
  - {"id":"H6","kind":"unknown","urls":["https://help.familytreedna.com/hc/en-us/articles/9134064538895-X-Matches"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"ae678c8f1f8bef1533ec18add0da61f58eea422fa55369f50356eaf434a3f872","claims":["C-6097b2a63b9f","C-2c7f2b59568d"],"review":"pending"}
  - {"id":"P1","kind":"unknown","urls":["https://www.pagelab.wi.mit.edu/_files/ugd/8c39a0_415339fd6f6c47728f70d505ae078a55.pdf"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"8c44935853874df15e49ce73ce267f2f5794e0331dac5cfe211c356a8700cec2","claims":["C-8bf30a429d08"],"review":"pending"}
  - {"id":"H7","kind":"video","urls":["https://www.youtube.com/watch?v=ZqK9b2Vt6gQ"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"bb8e43faaf8a1e7469c7293336f5ba6209b215685f27d1019d6032aa0a648a52","claims":[],"review":"pending"}
  - {"id":"H8","kind":"video","urls":["https://www.youtube.com/watch?v=3xodviufcG4"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"edbad055ba1394788473b11cf7d4e07c095d64bbed689ea2c6911f175a42ca65","claims":[],"review":"pending"}
  - {"id":"H9","kind":"video","urls":["https://www.youtube.com/watch?v=lMnm4UjIO60"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"83f9f841df2a52d50a3c3736afe8d29b26dc8fb4ac813afd9a927f1868ccb623","claims":[],"review":"pending"}
  - {"id":"H10","kind":"video","urls":["https://www.youtube.com/watch?v=ecwbM9Lc-Gg"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"4632596d65c1e871fd79993a3e73c9c5af7daf4794faee59f4b1249f495e4ce6","claims":[],"review":"pending"}
  - {"id":"H11","kind":"video","urls":["https://www.youtube.com/watch?v=W278DGiDKq0"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"481786dc4d2c6b00a474e79e0c059b7b316074b53075594a7ee961f98ec28dee","claims":[],"review":"pending"}
  - {"id":"H12","kind":"unknown","urls":["https://genarchivist.net/showthread.php?tid=2449","https://genarchivist.net/showthread.php?tid=1739","https://genarchivist.net/showthread.php?tid=1999","https://genarchivist.net/showthread.php?tid=729"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"b2dbcb7cb9cbb24272b240dada82f2caca999bbedb352a7a2d64b6abcdf4b6cc","claims":["C-efcee39ba2ef"],"review":"pending"}
  - {"id":"H13","kind":"unknown","urls":["https://genarchivist.net/showthread.php?tid=2412"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"f35911404c890344499a5bfebd4525189686a4742aab08a3fc855cd537d46743","claims":["C-efcee39ba2ef"],"review":"pending"}
  - {"id":"H14","kind":"unknown","urls":["https://forum.molgen.org/index.php/topic,14971.0.html"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"8dd1f9e0212f4487eb83827dcde821f22bd3f1262782a11eaa8410a3918e1be7","claims":["C-579cd19b1d82"],"review":"pending"}
  - {"id":"H15","kind":"unknown","urls":["https://genarchivist.net/showthread.php?tid=106"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"a26ea55b7b6f486c93fc0c53b8c4ec37b4906420123912732bcdef88fc8ae59c","claims":["C-579cd19b1d82"],"review":"pending"}
  - {"id":"H16","kind":"unknown","urls":["https://genarchivist.net/showthread.php?tid=1345"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"28f5f2c63f5200ac3f10b13a93b7694d5f8c361a400c2732d81058291eebb440","claims":["C-579cd19b1d82"],"review":"pending"}
  - {"id":"H17","kind":"unknown","urls":["https://genarchivist.net/showthread.php?tid=939"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"b51f9a958a95d4e98e59d1af4a4a3375343f254318b1392c95ee02a243ebd074","claims":["C-579cd19b1d82"],"review":"pending"}
  - {"id":"H18","kind":"unknown","urls":["https://forum.molgen.org/index.php/topic,10116.0.html"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"528b43808aeb169755e08389b887fbd840808c5eb31d2848ac8866ec35a57997","claims":["C-5eead37c84b2"],"review":"pending"}
  - {"id":"H19","kind":"unknown","urls":["https://forum.molgen.org/index.php/topic,10423.0.html"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"b7541d23c335890b6c79bba46372d40a7c4946dbb1280448c190a24f029229ee","claims":["C-5eead37c84b2"],"review":"pending"}
  - {"id":"H20","kind":"unknown","urls":["https://genarchivist.net/showthread.php?tid=137"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"51bf7df1ba27aa1337942b959f2938f30b6bfbe6bef10b9185f4e4a361e39ce0","claims":["C-b4f828e894b3"],"review":"pending"}
  - {"id":"H21","kind":"unknown","urls":["https://genarchivist.net/showthread.php?tid=905"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"18fea3a0656f39bdd55bb80cce906334aa40d287d675b5a225e45d86f44cafda","claims":["C-b4f828e894b3"],"review":"pending"}
  - {"id":"H22","kind":"video","urls":["https://www.youtube.com/watch?v=3vWBeFUBVdg"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"127f95766be0e109eb35ec9a1e53c9b1b248ce904816b8e490542da4579ee714","claims":[],"review":"pending"}
  - {"id":"H23","kind":"unknown","urls":["https://support.23andme.org/hc/en-us/articles/42963245607063-DNA-Relatives-Detecting-Relatives-and-Predicting-Relationships"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"f0840f2dd3a6c4e5ca191c5855194b5086cded6380aaa5eb1a65fd2bd296c862","claims":["C-2c7f2b59568d"],"review":"pending"}
  - {"id":"H24","kind":"unknown","urls":["https://www.gedmatch.com/applications/one-to-many/"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"fbb00da30b88752dd81c425accfb8d33d71543ba8c822456096b535b9892e672","claims":["C-2c7f2b59568d"],"review":"pending"}
  - {"id":"H25","kind":"unknown","urls":["https://support.gedmatch.com/portal/en/kb/articles/how-to-use-gedmatch-dna-matching-tools-one-to-many-one-to-one-segment-search"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"dd26a5f732e8ab3552f5d0a7fc16759db0e76018fd4fe4af3fde32c2a6e5ff82","claims":["C-2c7f2b59568d"],"review":"pending"}
  - {"id":"H26","kind":"unknown","urls":["https://www.ancestrycdn.com/support/us/2025/01/2025matchingwhitepaper.pdf","https://dna-explained.com/2026/03/16/understanding-x-dna-inheritance-video/"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"4f40d8dbf15fdbba9eec105716190169c1e407b41d5f1b42b3c087cb81d53bc2","claims":["C-2c7f2b59568d"],"review":"pending"}
  - {"id":"H27","kind":"unknown","urls":["https://www.myheritage.com/help/en/articles/13130239-what-type-of-dna-test-is-used-for-dna-matching"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"ad13d9eff5487fc16f6e6bdadd2bc5ce72cc178113f394392193780ad78ba3e4","claims":["C-2c7f2b59568d"],"review":"pending"}
  - {"id":"H28","kind":"unknown","urls":["https://www.myheritage.com/help/en/articles/12852329-in-the-chromosome-browser-is-it-possible-to-distinguish-between-dna-segments-which-were-inherited-from-the-paternal-and-maternal-side"],"published":null,"retrieved":null,"access":"unknown","rights":null,"basis":null,"entry_sha256":"66dca95fe44e31a14fef7e145e0d07a92439c4a6438f83ac74965251cb0e423f","claims":["C-2c7f2b59568d"],"review":"pending"}
claims:
  - {"id":"C-8f6c8c186ccf","kind":"unclassified","anchor":"A surname search can retrieve an ancestral surname rather than the tested person's\nname. MyHeritage documents both as search targets. Inspect the returned card's own\nperson and kit, and use spelling or script variants as leads rather than identity\nproof. A search miss with unresolved kit identity leaves the control unavailable. [H1]","sources":["H1"],"checked":null,"stated_as":null,"review":"pending"}
  - {"id":"C-4d4432b45f0e","kind":"unclassified","anchor":"When sharing appears only under relaxed settings, add a known negative. Run the same tool\nand lowered minimum segment size on pairs documented as unrelated within the time frame of\ninterest. If those pairs show similar summed small-segment totals, the relaxed total does\nnot distinguish a genealogical connection. Do not turn it into a predicted relationship, or\nassign it to a tree line without records or segments above the usual minimum. The\n[unrelated-pair demonstration](https://www.youtube.com/watch?v=ZqK9b2Vt6gQ) motivates this\ncheck; its pairs are anecdotal, not a measured false-positive rate or a vendor threshold.","sources":[],"checked":null,"stated_as":null,"review":"pending"}
  - {"id":"C-7d4534e420b7","kind":"unclassified","anchor":"Keep the tool, date, exact pair, readiness, chromosome scope, coordinate build and\nexposed reporting/filter settings with the result. Check usable shared markers in\nthe interval being tested. GEDmatch's SNP-overlap matrix describes common marker\ncoverage across the kits; a genome-wide count does not establish local coverage or\nwhole-test equivalence. No-calls are not observations of a matching genotype. The\nFamily Finder 5.0 white paper explicitly distinguishes genotyped/imputed calls and\ndoes not count a no-call as a matched SNP. [H2, H3]","sources":["H2","H3"],"checked":null,"stated_as":null,"review":"pending"}
  - {"id":"C-efcee39ba2ef","kind":"unclassified","anchor":"Inventory each raw file before using it as comparison input. Record its download or generation\ndate, header, any lab batch or results date shown, and per-chromosome counts of rows, calls and\nno-calls, including X, Y and MT. A vendor name, format label or header method tag does not fix\nthe marker set. Downloads of one kit at different times can differ, and assay generations change\nunder one label. Before using one file in place of another, compare the two directly for SNPs in\ncommon and SNPs unique to each. Zero rows for a chromosome make that input unavailable, not a\nnegative result. Keep the file's own counts separate from the usable or slimmed counts a tool\nreports after upload. The [raw-file SNP-count comparison](https://genarchivist.net/showthread.php?tid=2449),\n[re-download header discussion](https://genarchivist.net/showthread.php?tid=1739),\n[method-tag discussion](https://genarchivist.net/showthread.php?tid=1999),\n[added-rsID download comparison](https://genarchivist.net/showthread.php?tid=729) and\n[Family Finder generation discussion](https://genarchivist.net/showthread.php?tid=2412) motivate\nthis. They establish no vendor policy, batch cutoff or effect on matching. [H12, H13]","sources":["H12","H13"],"checked":null,"stated_as":null,"review":"pending"}
  - {"id":"C-8bf30a429d08","kind":"unclassified","anchor":"For X, distinguish raw-data coverage from the service's displayed matching scope.\nThe presence of X-labeled markers does not establish usable coverage of a particular\nnon-PAR interval. Identify PAR using\nthe test's actual build: the Genome Reference Consortium lists different boundaries\nfor GRCh37 and GRCh38. Ordinary no-father-to-son X routing concerns non-PAR; PAR can\nrecombine between X and Y. Check the parent's and child's usable coverage of the\nsame interval before treating an absent parental segment as a contradiction. [H4, P1]","sources":["H4","P1"],"checked":null,"stated_as":null,"review":"pending"}
  - {"id":"C-6097b2a63b9f","kind":"unclassified","anchor":"Two documented examples show why scope matters. MyHeritage's app browser describes\nautosomal chromosomes; its silence does not test an X-only claim. FamilyTreeDNA's\nX-Matches list requires qualifying autosomal sharing, so absence from that list can\noccur despite X sharing. These are documented tool behaviors, checked 2026-10-18;\nrecheck the actual service rather than extending them to every raw-file generation\nor future interface. [H5, H6]","sources":["H5","H6"],"checked":null,"stated_as":null,"review":"pending"}
  - {"id":"C-2c7f2b59568d","kind":"unclassified","anchor":"A service's lack of X reporting does not establish that the raw file lacks usable X\nmarkers; check the file itself before treating X as unavailable. Recheck a row before\nrelying on it. [H6, H23–H28]","sources":["H6","H23","H24","H25","H26","H27","H28"],"checked":null,"stated_as":null,"review":"pending"}
  - {"id":"C-1f84740c5c43","kind":"unclassified","anchor":"A result below a reporting floor need not appear. The smallest match in an old\nexport does not establish the service's current admission rule. Differences in\nmarker coverage, maps, phasing, imputation, joining and filters offer possible\nexplanations for disagreement; the discrepancy alone does not select its cause.\nFamily Finder 5.0 is one documented example of processed output, not an unfiltered\nreference instrument. [H3]","sources":["H3"],"checked":null,"stated_as":null,"review":"pending"}
  - {"id":"C-5eead37c84b2","kind":"unclassified","anchor":"When one match person appears under several kits (different chips, a self-converted file, a\nsequencing extract), keep a separate row for each kit against the same tester. Record its\nplatform, any conversion before upload, any imputation by the receiving site, and the\ncompared-SNP overlap. Do not adopt the highest or first-listed total; record the spread across\nkits as unresolved variation for this pair. A\n[multi-platform kit comparison](https://forum.molgen.org/index.php/topic,10116.0.html) and a\n[converted-upload discrepancy report](https://forum.molgen.org/index.php/topic,10423.0.html)\nmotivate this step. Neither shows which value is correct or establishes the cause. [H18, H19]","sources":["H18","H19"],"checked":null,"stated_as":null,"review":"pending"}
  - {"id":"C-86e5dab0fa1f","kind":"unclassified","anchor":"For degraded, forensic, artifact or heirloom-derived kits, record the reported call rate or\nprocessing status with each result, and treat segment count, endpoints and total cM as\nuncertain readings rather than full-coverage input for relationship prediction; the\n[investigative-genealogy discussion](https://www.youtube.com/watch?v=3xodviufcG4) and the\n[heirloom-kit example](https://www.youtube.com/watch?v=lMnm4UjIO60) motivate this but supply\nno validated call-rate cutoff, SNP-density threshold or error bound.","sources":[],"checked":null,"stated_as":null,"review":"pending"}
  - {"id":"C-579cd19b1d82","kind":"unclassified","anchor":"For a kit derived from whole-genome data, treat the FASTQ or BAM/CRAM as the source and each\nuploaded chip-style file as a separate derived input. Record the alignment build, the extraction\ntemplate and its build, the conversion tool, and which derived file went to which service.\nExtract in the comparison data's build instead of relying on a liftover. A variant-only VCF omits\nreference-matching positions, so a missing position is not a measured reference call, and a BAM\nrebuilt from such a VCF adds no coverage. Before reading matches or an empty list, check the\nsummary statistics: no-call share, autosomal heterozygosity, and X/Y calls against known sex. An\nall-no-call file or implausible heterozygosity marks the derived file as unusable input, whether\nfrom the derivation or the source data; report the control as unavailable. The\n[WGS-extraction discussion](https://forum.molgen.org/index.php/topic,14971.0.html),\n[WGS-to-chip conversion discussion](https://genarchivist.net/showthread.php?tid=1345),\n[conversion-before-upload advice](https://genarchivist.net/showthread.php?tid=939) and\n[sequencing-file quality warning](https://genarchivist.net/showthread.php?tid=106) motivate this.\nThey give no thresholds, liftover error rate or measured loss, and the symptoms do not identify a\ncause. [H14, H15, H16, H17]","sources":["H14","H15","H16","H17"],"checked":null,"stated_as":null,"review":"pending"}
  - {"id":"C-1e9629693608","kind":"unclassified","anchor":"When one provider's row overlaps several rows in another report, retain a one-to-many\ncrosswalk: original row IDs, endpoints, cM and SNP counts for every reported fragment.\nPreserve internal gaps and unresolved splitting/joining after checking the actual tests,\nbuild and reporting scope. Close endpoints or similar summed cM do not justify filling a\ngap, merging rows or declaring equivalent inherited tracts. This applies the\n[fragment-comparison example](https://www.youtube.com/watch?v=3vWBeFUBVdg) without adopting\nits proposed endpoint tolerance or inferring the cause of a provider difference.","sources":[],"checked":null,"stated_as":null,"review":"pending"}
  - {"id":"C-505a419d4917","kind":"unclassified","anchor":"Small-segment inclusion is a second reason, besides reciprocal rows, why one service's total\nmay be much larger. To compare totals from services with different minimum-segment rules,\nrecompute from each match's segment-level export. Drop rows below the chosen common minimum,\nsum what remains, and keep the reported total and the recomputed total as separate labelled\nvalues. Some difference may remain after recomputing; it does not select a cause. The\n[vendor-total explanation](https://www.youtube.com/watch?v=ecwbM9Lc-Gg) and the\n[threshold comparison](https://www.youtube.com/watch?v=W278DGiDKq0) motivate this step; their\nper-vendor thresholds are not verified here and may be out of date.","sources":[],"checked":null,"stated_as":null,"review":"pending"}
  - {"id":"C-b4f828e894b3","kind":"unclassified","anchor":"For Ancestry, keep the Timber-adjusted total and the unweighted total as separate labelled\nvalues. Compare the unweighted amount, segment count and longest segment with another service's\nfigures. A Timber reduction is the vendor's weighting, not a disagreement in measured sharing.\nPosters suspect weighting can also push an expected match below a list threshold. A direct\ncomparison of the same raw files in another tool is then a separate measurement with its own\nthresholds, not a correction. The\n[Timber cross-vendor comparison](https://genarchivist.net/showthread.php?tid=137) and a\n[multiple-test Timber discussion](https://genarchivist.net/showthread.php?tid=905) motivate this.\nEven unweighted figures still differ between vendors, and the threads do not establish when a\nmatch is dropped. [H20, H21]","sources":["H20","H21"],"checked":null,"stated_as":null,"review":"pending"}
```
<!-- provenance-ledger:end -->

## Credits

- Kinprove — original distillation and synthesis — FSL-1.1-MIT (kinprove-original)
