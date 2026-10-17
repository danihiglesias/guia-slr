# Phase 2b. Study selection and quality assessment

Selection turns hundreds or thousands of records into the dozens of primary studies that will answer your questions. It is done in phases, with criteria fixed in the protocol and, whenever possible, with more than one reviewer.


```{figure} ../../_static/generated/diagrams/en/records_reports_studies_en.svg
:name: fig-records_reports_studies-en
:alt: Records, reports and studies: conceptual example independent of the dataset, based on PRISMA 2020 definitions. Deduplication and report linking are different operations. Original figure, CC BY 4.0.
:width: 100%
:align: center

Records, reports and studies: conceptual example independent of the dataset, based on PRISMA 2020 definitions. Deduplication and report linking are different operations. Original figure, CC BY 4.0.
```


## Inclusion and exclusion criteria

They are defined from the research questions, plus some generic criteria (language, date, document type, peer review). They must be clear and unambiguous, and any later change must be justified and documented; avoid result-driven changes; when an amendment is necessary, document its rationale, timing and impact. Inclusion criteria are chained with AND and exclusion criteria with OR: a single exclusion criterion is enough to discard a paper.

Example (Hou et al., 2024, review on LLMs in software engineering): IC1 the paper states that it uses an LLM **and** IC2 the study addresses a software engineering task **and** IC3 the full text is accessible. Exclusion criteria: EC1 short papers (fewer than 8 pages) **or** EC2 duplicates or different versions of the same study by the same authors **or** EC3 books, theses, monographs, *keynotes*, panels or venues without full peer review **or** EC4 tool demonstrations and editorials **or** EC5 workshop or doctoral symposium papers **or** EC6 grey literature (technical reports) **or** EC7 not written in English **or** EC8 mentions LLMs without describing the technique used **or** EC9 uses software engineering methods to improve LLMs rather than LLMs for software engineering tasks. Note that the last three are not generic but topic-specific: they are the ones that truly separate the relevant study from the one that merely touches on the topic. With these criteria, more than 218,000 records were reduced to 810 after title and abstract screening, to 594 after full text and to 382 after quality assessment; *snowballing* added 13, for a total of 395.

Common generic criteria: date (justified: the emergence of a technology, a previous review), language, publication type (editorials, extended abstracts, posters and non-reviewed chapters are usually excluded), population or context (educational level, type of organisation), study design (empirical only, with evaluation only) and access to the full text. Link reports of the same study: they may provide complementary data. Specify the source for each outcome and avoid counting participants or effects twice. Record unavailable reports separately from eligibility exclusions in PRISMA.

## The screening phases

1. **Run the queries** and export the records from each database (RIS or BibTeX), noting the date.
2. **Remove duplicates** with the reference manager or a dedicated tool; record the number removed.
3. **Screen by title and abstract** applying the criteria. When in doubt, pass the paper on to the next phase; here it is better to be inclusive.
4. **Screen the full text**, recording the reason for excluding each discarded paper (PRISMA requires listing them with their reasons).
5. **Add the papers from *snowballing*** and repeat the screening on them until no new ones appear.

The number of phases depends on the volume of candidates and the number of reviewers. Exclusion rates vary widely: estimate workload through a pilot of your own corpus. Before screening in earnest, calibrate: the reviewers independently screen a sample of 50 to 100 records, compare their decisions and refine their interpretation of the criteria.

## Inter-reviewer agreement

Independent screening by two people reduces errors; disagreements are resolved by consensus or a third person. If only part can be duplicated, justify sample size and selection, cover difficult decisions and report the limitation. **Twenty per cent is a planning example, not a validated minimum or a guarantee against bias.** Expand or repeat calibration when criteria change or important disagreements arise.

Report how many records both people assessed, their decision table before consensus, raw agreement and, where appropriate, kappa with its uncertainty. Conventional kappa labels are only indicative and depend on prevalence and margins. A sample dominated by exclusions may show high agreement while hiding mistakes in relevant studies.

Test-retest assesses consistency within one reviewer, but cannot replace independent assessment. An LLM is an automated tool and must be described and validated as such, even when it supplies a second proposed decision.

## Critical appraisal: quality, risk of bias and certainty

These related concepts answer different questions:

- **Methodological quality:** appropriateness and transparency of a study’s design, conduct and analysis.
- **Risk of bias:** the possibility that its methods systematically distort a result.
- **Certainty of evidence:** confidence in a body-of-evidence conclusion for a specific outcome. GRADE considers risk of bias, inconsistency, imprecision, indirectness and publication bias {cite:p}`grade2023`.

Choose the tool for the included designs and follow its manual. Not every tool permits summing scores: **MMAT discourages an overall score**, and AMSTAR 2 uses critical weaknesses rather than a simple total {cite:p}`mmat2018,amstar2017`. Retain each domain judgement, its rationale and the supporting page or passage.

| Instrument | For which type of study | Notes |
| --- | --- | --- |
| [Dybå & Dingsøyr (2008)](https://ntnu.no/wiki/download/attachments/78978214/TorgeirDings%C3%B8yr_EmpiricalStudiesOfAgileSoftwareDevelopment.pdf?api=v2) | Empirical software engineering studies | 11 yes/no criteria: is it research rather than *lessons learned*?, aims, context, design, recruitment, control group, data collection, analysis, reflexivity, findings, value. The most widely used in software engineering |
| Kitchenham & Charters (2007), appendix | Any empirical SE study | Questions by design type (experiment, case study, survey) |
| [CASP](https://casp-uk.net/casp-tools-checklists/) | Qualitative studies, trials, cohorts, reviews | Free; originated in health, adaptable |
| [MMAT 2018](https://www.recercat.cat/handle/2072/354452) | Qualitative, quantitative and mixed-methods studies | Five categories, five criteria each; useful in education |
| [AMSTAR 2](https://amstar.ca/Amstar-2.php) | For appraising systematic reviews (tertiary studies) | 16 items; overall rating of high, moderate, low or critically low |
| [ROBIS](https://www.bristol.ac.uk/population-health-sciences/projects/robis/robis-tool/) | Risk of bias in systematic reviews | Four domains: eligibility, identification and selection, data collection, synthesis |

RoB 2 targets results from randomised trials; GRADE addresses a body of evidence by outcome. Neither should automatically be applied to every computing study.

The criteria used by Hou et al. (2024) illustrate decisions in a published review, rather than a universally recommended instrument. In particular, venue prestige cannot replace methodological appraisal. Prespecify and justify any adaptation or appraisal-based exclusion. Do not turn a quality total into statistical weights: meta-analysis weights depend on the model and the precision of estimates.

Explain how appraisal informs synthesis: identify limitations, compare conclusions after removing studies with major concerns, or moderate confidence in findings. Appraisal may be omitted with justification in descriptive mapping; conclusions about effectiveness require critical assessment.

Two people should compare judgements and resolve disagreements. Test-retest assesses one person’s consistency and is not equivalent to independent appraisal.

## Common mistakes

```{admonition} Common mistakes
:class: warning

- Being too strict when screening by title and abstract, and losing studies that the abstract describes poorly.
- Not recording the reason for exclusion at the full-text stage.
- Not measuring inter-reviewer agreement, or measuring it and not reporting it.
- Using the publication venue or the number of citations as a substitute for quality.
- Inventing your own quality checklist when a validated one exists.
```

```{figure} ../../_static/generated/diagrams/en/prisma_example_en.svg
:name: fig-prisma_example-en
:alt: Teaching flow adapted from PRISMA 2020 (Page et al., 2021), CC BY 4.0. Fictional data: 40 − 8 = 32; 32 − 22 = 10; 10 − 1 = 9; 9 − 4 = 5; 5 + 1 = 6. These are not original review results.
:width: 100%
:align: center

Teaching flow adapted from PRISMA 2020 (Page et al., 2021), CC BY 4.0. Fictional data: 40 − 8 = 32; 32 − 22 = 10; 10 − 1 = 9; 9 − 4 = 5; 5 + 1 = 6. These are not original review results.
```

```{figure} ../../_static/generated/diagrams/en/appraisal_matrix_en.svg
:name: fig-appraisal_matrix-en
:alt: Domain judgements in the fictional exercise. NR means not reported, not low risk. These teaching domains are not a validated scale and must not be summed. Original figure, CC BY 4.0.
:width: 100%
:align: center

Domain judgements in the fictional exercise. NR means not reported, not low risk. These teaching domains are not a validated scale and must not be summed. Original figure, CC BY 4.0.
```

For an actual review, use the [official PRISMA 2020 template](https://www.prisma-statement.org/prisma-2020-flow-diagram) for the review type and sources used. This is a teaching adaptation, not an unchanged official template. Count records during identification/screening, reports during retrieval/eligibility and studies at the end {cite:p}`page2021prisma`. Data are in the [case study](../04_practice/case_study.md).
