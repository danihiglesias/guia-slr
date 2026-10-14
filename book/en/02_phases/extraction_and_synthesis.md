# Phase 2c. Data extraction and synthesis

Extraction must be consistent: a form with the same fields for all studies, defined in the protocol and piloted on three or four papers before being used in earnest. Each field must serve to answer a specific research question; if it answers none, it is superfluous.

## The extraction form

It has two blocks: generic data (unique identifier, full reference, year, venue and publication type, country or affiliation, study type, context, number of participants) and question-specific data (in this guide's case study on haptic simulators in surgery: metrics used, residents' level of experience, number of participants). Always add a free-text notes field, the quality score and who extracted the data. The most practical option is a shared spreadsheet (Google Sheets, Excel) with one row per study and one column per field, or Parsifal's extraction form.

For categorical fields (contribution type, evaluation method, domain), define the classification scheme before extracting, with closed values. In systematic mapping studies, Petersen et al. (2008) propose building the scheme through *keywording*: reading the abstracts of the included studies, noting key concepts and grouping them into categories before classifying. Reusable schemes: the research type by Wieringa et al. (2006) (validation, evaluation, solution proposal, philosophical, opinion, experience) and contribution type (method, tool, model, metric, process).

Validate the extraction in the same way as the screening: a second reviewer extracts a random sample and the results are compared, or *test-retest*. During full reading you may discover that a study is not relevant; it is excluded and the reason is recorded (Phelps & Campbell, 2012).

## Traceability

You must be able to explain what happened to each paper in each phase and by which criterion it was excluded. Without that traceability, neither the paper's reviewer nor the thesis supervisor can trust the review. Most of that information does not fit in the paper, so it goes into supplementary material: a spreadsheet with all candidates and their decision at each phase, the search strings, the full extraction form and the quality checklist. Deposit it in Zenodo or OSF with a DOI and cite it from the paper; this is what PRISMA 2020 (item 27) and the Empirical Standards require.

## Synthesis

The synthesis answers each question from the extracted data. It is advisable to follow four steps: present the data from the search and selection process (PRISMA diagram), tabulate the data of the included studies, represent the most characteristic data graphically and outline the answer to each question.

| Method | When | How |
| --- | --- | --- |
| Descriptive and tabular synthesis | Always; the basis of any mapping study | Tables of studies by category; counts and percentages; one table per question |
| Narrative synthesis | SLRs with heterogeneous studies | Group findings by theme or question and describe them with reference to the studies that support them; make contradictions explicit |
| Thematic synthesis or coding | Qualitative or mixed-methods studies | Code fragments, group codes into themes (Cruzes & Dybå, 2011, for software engineering) |
| Meta-analysis | Quantitative studies with the same variable and comparable designs | Effect sizes pooled with a random-effects model; heterogeneity (I²); forest plots. Avoid *vote counting* |
| Mapping and visualisation | Systematic mapping studies | Trend charts by year, distribution by venue, *bubble plots* crossing two categories, Sankey diagrams from source to decision |

## Representing the data

The most useful figures (Hou et al., 2024, use several of them on 395 studies: distribution by venue and by year, annual evolution of model architecture types, counts of data strategies and *prompting* techniques, and a table of software engineering tasks by activity):

- **Trend chart**: number of studies per year, optionally by source; it shows whether the topic is growing or declining.
- **Table of authors and venues** with their number of publications and the venue's h-index; it answers "who" and "where".
- **Study × category cross-table** (an X per cell) for each question; it is the most compact way of showing which study contributes what.
- **Bubble plot** (Petersen et al., 2008; Kitchenham et al., 2015): two two-way tables sharing a nominal axis, with bubble size equal to the number of studies; it is the signature figure of a mapping study.
- **Sankey diagram** from sources to inclusion decision (SankeyMATIC) and **donut charts** by source and year to show the process.
- **PRISMA 2020 flow diagram** with the number of records at each step.

Use the same palette and the same category order in all figures, and never present the same data in both a table and a chart.

## Common mistakes

```{admonition} Common mistakes
:class: warning

- Extracting without a form and "sorting it out" afterwards.
- Columns that do not answer any question.
- Presenting the synthesis as a paper-by-paper list (the "shopping list" of the Empirical Standards) instead of by theme or question.
- Counting votes ("7 studies for, 3 against") as if it were a meta-analysis.
- Charts that repeat the table without adding insight.
```
