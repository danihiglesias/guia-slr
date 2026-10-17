# Templates and checklists

Copy these templates into your own document or spreadsheet and fill them in order. They are aligned with PRISMA-P, PRISMA-S and SEGRESS, so that when you finish you will have almost everything the reporting checklist will ask for.

## Protocol template

```markdown
# Systematic review protocol: <title>
Version: 1.0 · Date: <yyyy-mm-dd> · Registration: <OSF/Zenodo DOI>
Authors and roles: <reviewer 1, reviewer 2, arbiter>

## 1. Rationale
- Previous reviews located (search string and date of that search) and why they are not sufficient
- Whom this review serves and how

## 2. Objectives and questions
- Review type: SLR / mapping / scoping / MLR
- PICOC
- MQ1… / RQ1… (each with the extraction field that answers it)

## 3. Search strategy
- Sources (name, platform, reason)
- Generic search string and adaptation per source
- Restrictions: fields, years, languages, document types (justified)
- Control set (list of papers) and retrieval threshold
- Snowballing: backward / forward, stopping criterion
- Grey literature: sources and stopping criterion

## 4. Eligibility criteria
- Inclusion (IC1…, joined by AND)
- Exclusion (EC1…, joined by OR)

## 5. Selection process
- Phases (duplicates, title/abstract, full text)
- Reviewers per phase, calibration, disagreement resolution, agreement measure
- Tools (reference manager, screening, active learning, AI) and how they are validated

## 6. Quality assessment / risk of bias
- Tool by design, domains, rationales and use in synthesis; justified exclusions and sensitivity analyses

## 7. Data extraction
- Form (fields, allowed values), piloting, validation

## 8. Synthesis
- Method per question (tabular, narrative, thematic, meta-analysis), planned figures

## 9. Reporting and dissemination
- Checklist (PRISMA 2020 / SEGRESS), target venue, supplementary material

## 10. Schedule and resources

## 11. Protocol change log
| Date | Change | Reason |
```

## Extraction form (spreadsheet columns)

| Block | Fields |
| --- | --- |
| Identification | ID (S01…), full citation, DOI, year, venue, type (journal, conference, chapter), country of first affiliation, source it comes from |
| Design | Research type (Wieringa: validation, evaluation, solution proposal, philosophical, opinion, experience), empirical method (experiment, case study, survey, quasi-experiment), context (academic, industrial), participants and number |
| Content | One field per research question, with closed values where possible; contribution type (method, tool, model, metric, process) |
| Quality | Domain judgement, rationale, page and effect on synthesis |
| Management | Extracting reviewer, date, notes, relevant verbatim quotes with page |

## Screening sheet (one row per record)

Record ID, report ID, study ID, source, title, year, report retrieved (yes/no), duplicate (yes/no and of which), phase 1 decision reviewer A, phase 1 decision reviewer B, final phase 1 decision, phase 2 decision, exclusion criterion applied, origin (search / snowballing / grey). Count records, reports and studies separately; link multiple reports of one study. Record retrieval attempts and reasons for unavailable reports too.

## Abridged reporting checklist (PRISMA 2020 + SEGRESS)

- [ ] The title states that it is a systematic review or a mapping study
- [ ] Structured abstract with sources, dates, criteria, number of studies and conclusion
- [ ] Rationale with previous reviews cited
- [ ] Numbered questions and PICOC
- [ ] Protocol registered and linked; deviations explained
- [ ] All sources with full search string, filters and date (PRISMA-S)
- [ ] Explicit inclusion and exclusion criteria
- [ ] Selection process: phases, reviewers, agreement, automation or AI tools
- [ ] PRISMA 2020 flow diagram with numbers at each step
- [ ] List of studies excluded at full text with reason (supplement)
- [ ] Quality or risk-of-bias instrument and results per study
- [ ] Extraction form and extracted data available
- [ ] Synthesis by question, with tables and figures that do not duplicate each other
- [ ] Limitations or threats to validity with mitigations
- [ ] Implications for research and practice
- [ ] Funding, conflicts of interest and AI declaration
- [ ] Materials in a repository with a DOI

## Indicative schedule (PhD SLR, 300 to 1,500 candidates)

| Phase | Typical duration | Deliverable |
| --- | --- | --- |
| Preliminary search and check for existing reviews | 2 weeks | List of previous reviews; decision to proceed |
| Protocol and review by the supervisor | 3 to 4 weeks | Protocol v1.0 registered |
| Search, export and deduplication | 1 to 2 weeks | Zotero library; search table |
| Title and abstract screening (with calibration) | 2 to 4 weeks | Screening sheet; kappa |
| Full text and snowballing | 4 to 6 weeks | List of included and excluded studies with reason |
| Quality and extraction | 4 to 8 weeks | Validated extraction sheet |
| Synthesis and figures | 3 to 4 weeks | Tables and figures per question |
| Writing, checklist and submission | 4 to 6 weeks | Manuscript and supplementary material |

Total: 6 to 9 months part-time. Assess updates against the field’s pace and elapsed time; twelve months is an indicative warning, not a universal threshold.

## Downloadable templates

- {download}`Editable protocol <../../_static/downloads/en/protocol_template.md>`
- {download}`Blank screening log <../../_static/downloads/en/screening_template.csv>`
- {download}`Blank extraction form <../../_static/downloads/en/extraction_template.csv>`
- {download}`Search log <../../_static/downloads/en/search_log_template.csv>`
- {download}`Amendment log <../../_static/downloads/en/amendments_template.csv>`
- {download}`Editable checklist <../../_static/downloads/en/reporting_checklist.md>`
- {download}`All templates and worked example <../../_static/downloads/en/teaching_materials.zip>`
