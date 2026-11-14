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

### X-upload route, duplicate-upload and artifact-depositor sources

- **H29:** Roberta Estes, DNAeXplained, [X Chromosome Master Class](https://dna-explained.com/2023/03/28/x-chromosome-master-class/), published 2023-03-28, read 2026-11-12. Used for: Ancestry and MyHeritage gave no X-DNA results but included the X in their raw files, which could be uploaded to services that match on X. Its suggestion of FamilyTreeDNA as a destination is not used.
- **H30:** GEDmatch Support, [How to Upload DNA Files to GEDmatch (All Testing Companies)](https://support.gedmatch.com/portal/en/kb/articles/how-to-upload-dna-files-to-gedmatch-all-testing-companies), read 2026-11-12. Used for: accepted AncestryDNA and MyHeritage raw files, and its note that MyHeritage changed its raw-data download from 31 December 2025. It does not say whether the changed MyHeritage files still carry X.
- **H31:** GEDmatch Support, [How to Use GEDmatch DNA Matching Tools (One-to-Many, One-to-One, Segment Search)](https://support.gedmatch.com/portal/en/kb/articles/how-to-use-gedmatch-dna-matching-tools-one-to-many-one-to-one-segment-search), read 2026-11-12. Used for: the One-to-One X tool, which compares only the X chromosome.
- **H32:** Roberta Estes, DNAeXplained, [DNA: In Search Of…Your Grandparents](https://dna-explained.com/2023/04/07/dna-in-search-ofyour-grandparents/), published 2023-04-07, read 2026-11-12. Used for: the author's two cases: a tester's own later upload mistaken for a parent, and one match's uploads from two companies mistaken for two sisters.
- **H33:** GEDmatch Support, [Duplicate Kit Issues and How to Resolve Them](https://support.gedmatch.com/portal/en/kb/articles/duplicate-kit-issues-and-how-to-resolve-them), read 2026-11-12. Used for: identical uploads flagged as duplicates, and one person's kits from different companies allowed.
- **H34:** Blaine Bettinger, The Genetic Genealogist, [Testing Artifacts to Obtain DNA Evidence for Genealogical Research](https://thegeneticgenealogist.com/2018/11/19/testing-artifacts-obtain-dna-evidence-genealogical-research/), published 2018-11-19, read 2026-11-12. Used for: a child or the postmaster may have licked the envelope or stamp, or a sponge may have moistened it.
- **H35:** Roberta Estes, DNAeXplained, [Preserving Items for Future DNA Testing – Teeth, Stamps, Envelopes, Hats, Hair and More](https://dna-explained.com/2022/02/25/preserving-items-for-future-dna-testing-teeth-stamps-envelopes-hats-hair-and-more/), published 2022-02-25, read 2026-11-12. Used for: the risk that DNA from a stamp or envelope is another person's or contamination. Its statement that some adhesives contain animal DNA was not confirmed by another source and is not used.

### Low-pass whole-genome and genetic-map sources

- **H36:** Erica Edvi, MyHeritage Blog, [MyHeritage Upgrades Its DNA Tests to Whole Genome Sequencing](https://blog.myheritage.com/2025/10/myheritage-upgrades-its-dna-tests-to-whole-genome-sequencing/), published 2025-10-17, read 2026-11-14. Used for: low-pass sequencing with 2x coverage, each position read twice on average, combined with imputation. Its accuracy claims are not used.
- **H37:** MyHeritage Help, [What is Whole Genome Sequencing (WGS) that MyHeritage now uses for its DNA tests?](https://www.myheritage.com/help/en/articles/12852568-what-is-whole-genome-sequencing-wgs-that-myheritage-now-uses-for-its-dna-tests), dated 2026-07-21, read 2026-11-14. Used for: the low-pass approach with 2x coverage.
- **H38:** MyHeritage Help, [What does the Whole Genome Sequencing (WGS) upgrade mean for my DNA results?](https://www.myheritage.com/help/en/articles/12852457-what-does-the-whole-genome-sequencing-wgs-upgrade-mean-for-my-dna-results), shown as updated about three weeks before reading, read 2026-11-14. Used for: all new samples processed with WGS from January 2026, the raw file's header showing whether a kit was, and the CRAM download for WGS kits.
- **H39:** Louis Kessler, Behold Blog, [MyHeritage DNA Tests are ALL going to be WGS](https://www.beholdgenealogy.com/blog/?p=3926), published 2025-10-14, read 2026-11-14. Used for: the author's expectation that at 2x coverage half the heterozygous sites would not show both alleles. His statement that at least 10x coverage is needed is not used.
- **H40:** Louis Kessler, Behold Blog, [My MyHeritage WGS DNA Results](https://www.beholdgenealogy.com/blog/?p=3930), published 2026-01-04, read 2026-11-14. Used for: the read-count distribution at a mean of 2, two reads seeing the same allele half the time, a WGS-generated raw file with no no-calls, its 99.25% agreement with the author's chip file at 584,174 shared SNPs, and his guess that imputation explains it. A single tester's comparison.
- **H41:** David Wragg, Wengang Zhang, Sarah Peterson et al., Genetics Selection Evolution, [A cautionary tale of low-pass sequencing and imputation with respect to haplotype accuracy](https://pmc.ncbi.nlm.nih.gov/articles/PMC10785484/), published 2024-01-12, read 2026-11-14. Used for: low sequencing depth reducing the reads that span both alleles of a heterozygous genotype. A study of dogs.
- **H42:** Louis Kessler, Behold Blog, [Converting Base Pairs to Centimorgans](https://www.beholdgenealogy.com/blog/?p=3879), published 2022-06-12, read 2026-11-14. Used for: the author's comparison of FamilyTreeDNA, GEDmatch, 23andMe and MyHeritage segment cM with a HapMap-based map. His 2015 chromosome totals are not used.
- **H43:** Jonny Perl, DNA Painter blog, [cM estimator: Estimating cMs for a segment of DNA](https://dnapainter.com/blog/cm-estimator-estimating-cms-for-a-segment-of-dna/), published 2020-11-12, read 2026-11-14. Used for: HapMap-based estimates aligning closely with MyHeritage's and 23andMe's cM, and GEDmatch's figures differing.

## Synthesis boundaries

The self-match test by identity state (a self-match or identical twin fully identical almost
throughout, a parent half-identical) is Kinprove synthesis from the definitions of half- and
fully identical sharing; H32 and H33 supply the cases and the GEDmatch duplicate rule. The
`unconfirmed` depositor status and the close-relative comparison are Kinprove synthesis.

The exact-test registry, known-positive query check, result-status table, local
coverage requirement and reciprocal-row reconciliation are original methodological
synthesis. The sources establish concrete measurement limitations; none supplies a
universal “good overlap,” sensitivity threshold, relationship ceiling or error rate.
An operational control checks the operation and scope exercised, not all claims
about the tested person. No family data, private kit identifiers or account findings
are part of this recipe.

## Credits

- Kinprove — original distillation and synthesis — FSL-1.1-MIT (kinprove-original)
- Roberta Estes, DNAeXplained blog, posts cited as H29, H32 and H35 — Third-party blog; no explicit licence; paraphrase with attribution (adapted)
- GEDmatch Support, help articles cited as H30, H31 and H33 — Vendor documentation; paraphrased factual support with attribution (adapted)
- Blaine Bettinger, The Genetic Genealogist blog, post cited as H34 — Third-party blog; no explicit licence; paraphrase with attribution (adapted)
- Louis Kessler, Behold Blog, posts cited as H39, H40 and H42 — Third-party blog; no explicit licence; paraphrase with attribution (adapted)
