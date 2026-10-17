# Phase 1. Planning: from the idea to the protocol

Planning ends with a written protocol that has been reviewed by someone other than you. Define questions, criteria, sources, search strategy, extraction and critical appraisal before the definitive search. Exploratory searches and pilots can refine the protocol. Later amendments may be necessary: record their date, reason, stage and impact, and distinguish prospective decisions from those informed by results.


```{figure} ../../_static/generated/diagrams/en/traceability_en.svg
:name: fig-traceability-en
:alt: From RQ1 to the conclusion in the fictional exercise. Each decision must be traceable to its source. Original figure, CC BY 4.0.
:width: 100%
:align: center

From RQ1 to the conclusion in the fictional exercise. Each decision must be traceable to its source. Original figure, CC BY 4.0.
```


## Step 0. Is this review needed?

Ask yourself two questions (Kitchenham & Charters, 2007). First: is it necessary? Search Google Scholar, Scopus and Web of Science for "systematic review", "literature review", "mapping study", "survey" and "state of the art" together with your topic. If a recent SLR already exists, repeating it only makes sense if it is clearly biased or outdated because new studies have appeared (Petticrew & Roberts, 2005); otherwise, rethink the topic or turn your work into an update. Second: do you have the resources? An SLR takes months; you need time, access to the databases (through your university library), at least a second reviewer and a clear idea of who will use the results and how.

Before going any further, settle four things: scope, timeline, expected benefits and where you intend to publish, because the venue determines the length and the checklist you will have to comply with.

## Step 1. Research questions

The question is the heart of the protocol: the title, the objectives, the search string and the extraction form all derive from it. It must be clear and specific, and answering it must require an explanation (never a yes or no). Check its suitability with the FINER acronym:

| Criterion | Question to ask yourself |
| --- | --- |
| **F**easible | Do I have the resources, access and time to answer it? |
| **I**nteresting | Is it genuinely interesting to me and to my community? |
| **N**ovel | Does it confirm, refute or extend previous findings? |
| **E**thical | Could answering it harm anyone? |
| **R**elevant | Does it contribute anything to scientific knowledge or to practice? |

Mapping questions categorise ("how many studies per year?", "which venues?", "which domains?", "what type of contribution: framework, tool, method?"). SLR questions go deeper ("what solutions have been proposed for X?", "how were they evaluated?", "what limitations do they report?"). It is advisable to number them (MQ1… for mapping, RQ1… for the SLR) and to make each column of the extraction form answer one of them.

## Step 2. Defining the scope with PICOC

PICOC (Petticrew & Roberts, 2005; Kitchenham & Charters, 2007) structures the question and, along the way, provides the search terms:

| Element | Question | Example (Hou et al., 2024) |
| --- | --- | --- |
| **P**opulation | Who or what? | Primary studies that apply an LLM to a software engineering task (code generation, program repair, testing, vulnerability detection…) |
| **I**ntervention | What? How? | Large language models (GPT, Codex, CodeBERT, LLaMA…) and the techniques used to adapt them: *prompting*, fine-tuning, context retrieval |
| **C**omparison | Compared with what? | Across model architectures, data strategies and optimisation techniques; there is no control group |
| **O**utcomes | What is to be achieved or improved? | Which models are used, how data are prepared, how performance is optimised and evaluated, and in which tasks they work best |
| **C**ontext | In which organisation and circumstances? | Academic research in software engineering, including arXiv preprints, from 2017 to January 2024 |

In computer science the "population" is usually a type of system, technique or role (developers, programming students), and the comparison often does not exist; make this explicit. For qualitative reviews you can use SPIDER (*Sample, Phenomenon of Interest, Design, Evaluation, Research type*).

## Step 3. Writing the protocol

A minimal protocol has eight elements: questions and objectives, inclusion criteria, exclusion criteria, databases and search engines, search terms, search and extraction procedure (iterated in stages), quality assessment and synthesis of results. Also add: the number of reviewers and how you will resolve disagreements, the extraction form, the synthesis plan, the timeline and the dissemination strategy. PRISMA-P (17 items) serves as a checklist; the template at the end of this guide follows it.

Ask your supervisor or a colleague to review the protocol before you carry it out. Kitchenham & Charters list this as an activity of its own within planning ("evaluating the protocol"), and it is the cheapest moment to fix a poorly framed question.

## Step 4. Registering or publishing the protocol

Registering the protocol before execution improves transparency and allows comparison of planned and completed methods; it does not guarantee absence of bias. PRISMA 2020 asks authors to report registration and protocol access, or state that neither exists. Public deposit and prospective registration are not equivalent. Options:

- [PROSPERO](https://www.crd.york.ac.uk/prospero/) (University of York, free): only accepts reviews with outcomes relevant to human health; it is not suitable for most SLRs in computer science or education, and it excludes scoping reviews. Relaunched in March 2025 with automatic publication after the authors' approval.
- [OSF Registries](https://help.osf.io/hc/en-us/articles/360019738794-Select-a-Registration-Template) (free, with DOI, any discipline): the most widely used option outside health; it offers a "Generalized Systematic Review" template suitable for SLRs, scoping reviews and meta-analyses.
- [INPLASY](https://inplasy.com/) (check current fees and conditions) and [Research Registry](https://www.researchregistry.com/) (paid): accept any field.
- Open deposit in [Zenodo](https://zenodo.org/), Figshare or arXiv: common practice in software engineering, with a persistent identifier and date, although without review; Zenodo and Figshare support DOIs, whereas arXiv supplies an arXiv identifier.

Only 31.5% of the 537 secondary studies in software engineering published between 2013 and 2023 share their artefacts (protocol, searches, data), and barely 12% do so in a permanent repository ([Huotala, Kuutila & Mäntylä, 2025](https://arxiv.org/html/2504.12646v2)). Doing it properly sets you apart.

## Team and timeline

An SLR is not a one-person job: PRISMA 2020 asks you to state how many reviewers screened and whether they did so independently, and the Empirical Standards consider it desirable to have two analysts with a measure of agreement. For a PhD student, the usual arrangement is for the supervisor or a colleague to act as second reviewer, at least on a sample. As for timing, allow 4 to 9 months for a complete SLR in an area with several hundred candidates; the most underestimated phase is full-text reading and extraction.

## Common mistakes in this phase

```{admonition} Common mistakes in this phase
:class: warning

- Starting to search without a protocol and "reconstructing" it afterwards.
- Questions so broad that the answer fits in a narrative review ("what is known about AI in education?").
- Not checking whether an SLR on the topic already exists.
- Changing the inclusion criteria midway without documenting or justifying it.
- Not deciding from the outset in which venue the review will be published and which checklist it requires.
```
