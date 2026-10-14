# Phase 2b. Study selection and quality assessment

Selection turns hundreds or thousands of records into the dozens of primary studies that will answer your questions. It is done in phases, with criteria fixed in the protocol and, whenever possible, with more than one reviewer.

## Inclusion and exclusion criteria

They are defined from the research questions, plus some generic criteria (language, date, document type, peer review). They must be clear and unambiguous, and any later change must be justified and documented; they are never modified in light of the findings, because that introduces bias. Inclusion criteria are chained with AND and exclusion criteria with OR: a single exclusion criterion is enough to discard a paper.

Example (Hou et al., 2024, review on LLMs in software engineering): IC1 the paper states that it uses an LLM **and** IC2 the study addresses a software engineering task **and** IC3 the full text is accessible. Exclusion criteria: EC1 short papers (fewer than 8 pages) **or** EC2 duplicates or different versions of the same study by the same authors **or** EC3 books, theses, monographs, *keynotes*, panels or venues without full peer review **or** EC4 tool demonstrations and editorials **or** EC5 workshop or doctoral symposium papers **or** EC6 grey literature (technical reports) **or** EC7 not written in English **or** EC8 mentions LLMs without describing the technique used **or** EC9 uses software engineering methods to improve LLMs rather than LLMs for software engineering tasks. Note that the last three are not generic but topic-specific: they are the ones that truly separate the relevant study from the one that merely touches on the topic. With these criteria, more than 218,000 records were reduced to 810 after title and abstract screening, to 594 after full text and to 382 after quality assessment; *snowballing* added 13, for a total of 395.

Common generic criteria: date (justified: the emergence of a technology, a previous review), language, publication type (editorials, extended abstracts, posters and non-reviewed chapters are usually excluded), population or context (educational level, type of organisation), study design (empirical only, with evaluation only) and access to the full text. When the same study has several publications (a conference paper and an extended journal version), keep the most complete one and state so.

## The screening phases

1. **Run the queries** and export the records from each database (RIS or BibTeX), noting the date.
2. **Remove duplicates** with the reference manager or a dedicated tool; record the number removed.
3. **Screen by title and abstract** applying the criteria. When in doubt, pass the paper on to the next phase; here it is better to be inclusive.
4. **Screen the full text**, recording the reason for excluding each discarded paper (PRISMA requires listing them with their reasons).
5. **Add the papers from *snowballing*** and repeat the screening on them until no new ones appear.

The number of phases depends on the volume of candidates and the number of reviewers. A typical screening in computer science reduces 2,500 records to 1,700 after duplicates, to about 50 after title and abstract, and to about 13 after full text; plan your time accordingly. Before screening in earnest, calibrate: the reviewers independently screen a sample of 50 to 100 records, compare their decisions and refine their interpretation of the criteria.

## Inter-reviewer agreement

With a single reviewer the process may be considered biased. The solutions, from most to least robust:

- Two independent reviewers in all phases, with a third to resolve disagreements.
- Two reviewers on a random sample (for example, 20%) and one reviewer for the rest, if agreement on the sample is high.
- *Test-retest* (Kitchenham et al., 2015): the same reviewer re-screens a random sample after some time and checks whether they obtain the same results.

Measure agreement with **Cohen's kappa** (κ) and report it: by convention, κ below 0.40 is poor, between 0.41 and 0.60 moderate, between 0.61 and 0.80 substantial and above 0.80 almost perfect (Landis & Koch, 1977). With highly unbalanced sets (few included versus many excluded) kappa drops even when raw agreement is high; in that case add the percentage agreement or PABAK.

## Quality assessment

The quality of a study is the degree to which its information is truthful, reliable and useful for answering your questions. It is assessed with a checklist of scored closed questions (Yes = 1, Partly = 0.5, No = 0), and it serves three purposes: excluding studies below a threshold that you set in the protocol, weighting each study's contribution to the synthesis, or simply describing the strength of the evidence. In a mapping study it is usually not done, or it is done in a lightweight way.

Useful checklists in computer science and education:

| Instrument | For which type of study | Notes |
| --- | --- | --- |
| [Dybå & Dingsøyr (2008)](https://ntnu.no/wiki/download/attachments/78978214/TorgeirDings%C3%B8yr_EmpiricalStudiesOfAgileSoftwareDevelopment.pdf?api=v2) | Empirical software engineering studies | 11 yes/no criteria: is it research rather than *lessons learned*?, aims, context, design, recruitment, control group, data collection, analysis, reflexivity, findings, value. The most widely used in software engineering |
| Kitchenham & Charters (2007), appendix | Any empirical SE study | Questions by design type (experiment, case study, survey) |
| [CASP](https://casp-uk.net/casp-tools-checklists/) | Qualitative studies, trials, cohorts, reviews | Free; originated in health, adaptable |
| [MMAT 2018](https://www.recercat.cat/handle/2072/354452) | Qualitative, quantitative and mixed-methods studies | Five categories, five criteria each; useful in education |
| [AMSTAR 2](https://amstar.ca/Amstar-2.php) | For appraising systematic reviews (tertiary studies) | 16 items; overall rating of high, moderate, low or critically low |
| [ROBIS](https://www.bristol.ac.uk/population-health-sciences/projects/robis/robis-tool/) | Risk of bias in systematic reviews | Four domains: eligibility, identification and selection, data collection, synthesis |
| Cochrane RoB 2, Jadad, Newcastle-Ottawa, GRADE | Clinical trials and observational studies in health | Rarely applicable outside health |

You can add questions specific to your topic ("are the metrics explicitly defined?", "is the population students only?"). Hou et al. (2024) use ten criteria: three of relevance (is it relevant to software engineering?, does it use LLMs?, is it not a secondary study?) and seven of quality scored from 0 to 3 (prestigious venue, clear motivation, description of the techniques, detail of the experimental setup and data, confirmation of the findings, discussion of contributions and limitations, contribution to the community), and they set in the protocol a threshold of 16.8 out of 21 points for including a study (14.4 out of 18 for preprints, to which the venue criterion does not apply). SEGRESS asks for this phase to be called "risk of bias" and, if you use the score to exclude studies, for the threshold to be declared in the protocol. Validate the assessment in the same way as the screening: a second reviewer or *test-retest* on a sample.

## Common mistakes

```{admonition} Common mistakes
:class: warning

- Being too strict when screening by title and abstract, and losing studies that the abstract describes poorly.
- Not recording the reason for exclusion at the full-text stage.
- Not measuring inter-reviewer agreement, or measuring it and not reporting it.
- Using the publication venue or the number of citations as a substitute for quality.
- Inventing your own quality checklist when a validated one exists.
```
