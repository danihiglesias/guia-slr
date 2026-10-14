# Standards and guidelines you should know

For an SLR in computer science today you need three things: a **process** guideline (Kitchenham & Charters for SLRs; Petersen for mapping studies), a **reporting** guideline (PRISMA 2020 or its SEGRESS adaptation) and, if you publish at an ACM/IEEE venue, the SIGSOFT **empirical standard**. The SALSA and PSALSAR frameworks help check that the design covers the four dimensions (systematic, comprehensive, explicit, reproducible).

| Guideline | Year | What it is for | Where |
| --- | --- | --- | --- |
| Kitchenham & Charters, EBSE-2007-01 | 2007 | Complete process of an SLR in software engineering: planning, conducting and reporting | [Technical report](https://legacyfileshare.elsevier.com/promis_misc/525444systematicreviewsguide.pdf) |
| Kitchenham, Budgen & Brereton, *Evidence-Based Software Engineering and Systematic Reviews* | 2015 | Book that supersedes the 2004 and 2007 reports; covers primary studies, synthesis and knowledge translation | [Routledge](https://www.routledge.com/Evidence-Based-Software-Engineering-and-Systematic-Reviews/Kitchenham-Budgen-Brereton/p/book/9781482228656) |
| Petersen et al., EASE | 2008 | Systematic mapping process: questions, search, screening, *keywording* of abstracts, extraction and map | [PDF](https://www.cse.chalmers.se/~feldt/publications/petersen_ease08_sysmap_studies_in_se.pdf) |
| Petersen, Vakkalanka & Kuzniarz, IST | 2015 | Update of the mapping guidelines after analysing how they were applied; concludes that the 2008 guidelines "are not sufficient on their own" | [EBSE](https://ebse.webspace.durham.ac.uk/?p=466) |
| Wohlin, EASE | 2014 | Backward and forward *snowballing* as a search strategy; EASE 2024 most influential paper award | [EASE 2024 award](https://conf.researchr.org/details/ease-2024/ease-2024-most-influential-paper-award/1/Guidelines-for-snowballing-in-systematic-literature-studies-and-a-replication-in-soft) |
| Garousi, Felderer & Mäntylä, IST | 2019 | Grey literature and multivocal reviews (MLR) | [arXiv](https://arxiv.org/abs/1707.02553v4) |
| PRISMA 2020 (Page et al., BMJ) | 2021 | 27-item checklist for **reporting** a review and flow diagram; does not assess the quality of the review | [prisma-statement.org](https://www.prisma-statement.org/prisma-2020-checklist) |
| SEGRESS (Kitchenham, Madeyski & Budgen, IEEE TSE) | 2023 | Adaptation of PRISMA 2020 to software engineering secondary studies: SLRs, mapping studies, tertiary, qualitative | [Checklist](https://ebse.webspace.durham.ac.uk/reporting/) |
| ACM SIGSOFT Empirical Standards (Ralph et al.) | 2020–2021 | What an ICSE/FSE/EMSE reviewer will expect to see in a systematic review | [Systematic Reviews standard](https://github.com/acmsigsoft/EmpiricalStandards/blob/master/docs/standards/SystematicReviews.md) |

## PRISMA 2020 in detail

PRISMA (*Preferred Reporting Items for Systematic Reviews and Meta-Analyses*) was created in 2009 and updated in 2021 ([Page et al., BMJ 2021;372:n71](https://www.bmj.com/content/372/bmj.n71)). Its aim is for the review report to be complete and transparent; it can also be used to critically appraise published reviews, but it is **not** a methodological quality instrument. It consists of a 27-item checklist in seven sections, a 12-item checklist for the abstract and a flow diagram.

What changed with respect to 2009 and is worth bearing in mind:

- The search item requires the full strategies for **all** databases, registers and websites consulted, not just one example.
- You must state how many reviewers screened each record, whether they worked independently and which automation tools were used.
- The synthesis is broken down into six methods sub-items and four results sub-items.
- Items are added on certainty of evidence, conflicts of interest and availability of data, code and materials.
- The flow diagram has two arms: databases and registers, and "other methods" (citation searching, websites, organisations), which is added only if they were used. There are [four official templates](https://www.prisma-statement.org/prisma-2020-flow-diagram) and a [free web application](https://estech.shinyapps.io/prisma_flowdiagram/) (Haddaway et al., 2022) that generates the diagram in PDF, PNG or SVG.

There is an [official Spanish translation of the statement](https://www.prisma-statement.org/s/PRISMA-2020-Spanish.pdf) (Rev Esp Cardiol 2021;74(9):790–799), although not of the checklist.

## PRISMA extensions useful in computer science

- **PRISMA-S** ([Rethlefsen et al., 2021](https://systematicreviewsjournal.biomedcentral.com/articles/10.1186/s13643-020-01542-z)): 16 items for documenting the search (name of each database, full string, limits, filters, dates, peer review of the strategy, total records and deduplication). It is the best checklist for the search section of any SLR.
- **PRISMA-ScR** ([Tricco et al., 2018](https://www.prisma-statement.org/scoping)): 20 essential items for scoping reviews; SEGRESS also recommends it for mapping studies.
- **PRISMA-P** ([Moher et al., 2015](https://www.prisma-statement.org/protocols)): 17 items for writing the protocol.

## SEGRESS: PRISMA adapted to software engineering

[SEGRESS](https://madeyski.e-informatyka.pl/segress-software-engineering-guidelines-for-reporting-secondary-studies/) (IEEE TSE 49(3), 2023) takes the 27 items of PRISMA 2020, combines them with PRISMA-S, PRISMA-P and PRISMA-ScR, and indicates for each item which type of secondary study it applies to (quantitative SLR, mapping study, tertiary, qualitative, mixed). It replaces "quality assessment" with "risk of bias" and "threats to validity" with "limitations". If you are going to publish in IST, JSS or TSE, this is the checklist you should follow.

## ACM SIGSOFT Empirical Standards

The [standard for systematic reviews](https://github.com/acmsigsoft/EmpiricalStandards/blob/master/docs/standards/SystematicReviews.md) lists **essential** attributes (review type identified; step-by-step replicable search with the terms; clear selection criteria; detailed extraction and synthesis; coding scheme; chain of evidence; conclusions useful to practitioners) and **desirable** ones (protocol, searches and dataset as supplementary material; *snowballing* and preprints to mitigate bias; quality assessment defined a priori; two analysts with an agreement measure; PRISMA diagram; meta-analysis without *vote counting*). It names two antipatterns: the "shopping list" of papers without synthesis, and using the publication venue as a proxy for quality.

## SALSA and PSALSAR

Grant & Booth (2009) propose the SALSA framework (*Search, AppraisaL, Synthesis, Analysis*) to check whether a review method meets the four dimensions. Mengist et al. (2020) extend it to PSALSAR by adding the **protocol** at the beginning and **reporting** (with PRISMA) at the end, in six steps: Protocol, Search, Appraisal, Synthesis, Analysis, Report. It is a good skeleton for the methodology section of your paper.
