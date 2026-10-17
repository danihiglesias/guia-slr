# Generative AI in an SLR: what it can do and how to declare it

Generative AI is already part of the workflow of many reviews, but the evidence from 2023 to 2026 is clear: language models serve as **support** (second reviewer, pre-filter, extraction draft), not as a substitute for human judgement. The joint position statement of Cochrane, Campbell, JBI and CEE of November 2025 sums it up: authors remain responsible for everything, AI is used only if it does not compromise rigour, with human oversight, and any use that makes or suggests judgements is declared ([Flemyng et al., 2025](https://www.sei.org/publications/position-statement-on-ai-use-in-evidence-synthesis/)).

## What the evidence says, phase by phase

| Phase | What works | What does not, and evidence |
| --- | --- | --- |
| Planning | Refining questions, suggesting synonyms and terms, reviewing the protocol against PRISMA-P | Nothing especially risky as long as you check what it proposes |
| Search | Generating search string variants and translating them between databases (Polyglot); preliminary search in Elicit or Undermind | Asking a chatbot for references: [Chelli et al. (2024)](https://www.jmir.org/2024/1/e53164) measured fabricated reference rates of 28.6% for GPT-4 and 39.6% for GPT-3.5 (91.4% for Bard), with only 16 to 20% correct DOIs |
| Title and abstract screening | As automated screening assistance with a "sensitive" rule: [Tran et al. (2024)](https://rti.org/publication/sensitivity-specificity-using-gpt-3-5-turbo-models-title-abstract-screening-systematic-reviews-meta) obtain a sensitivity of 94.6 to 99.8%, missing 0 or 1 of 26 studies, at the cost of a specificity of 2 to 47% | As the sole reviewer: [Guo et al. (2024)](https://www.jmir.org/2024/1/e48996), over 24,307 records, obtain a sensitivity for included studies of 0.76 (0.59 to 1.0 depending on the review). In software engineering, [Felizardo et al. (ESEM 2024)](https://conf.researchr.org/details/esem-2024/esem-2024-technical-track/2/ChatGPT-application-in-Systematic-Literature-Reviews-in-Software-Engineering-an-eval) obtain 75 and 86% accuracy with GPT-4 in two SLRs and conclude that outsourcing selection is not advisable; [Thode et al. (IST 2025)](https://www.fortiss.org/ergebnisse/publikationen/details/exploring-the-use-of-llms-for-the-selection-phase-in-systematic-literature-studies) reach a *recall* of 98 to 99% by combining two models, with a precision of 27% |
| Full-text screening | Promising with well-designed prompts ([Khraisha et al., 2024](https://arxiv.org/abs/2310.17526)) | Dependent on the prompt and the model version; unstable results |
| Data extraction | Draft of the extraction form from the PDF (Elicit, Covidence, an LLM with the PDF) that a human verifies field by field | "Moderate" reliability after adjusting for chance (Khraisha et al.); numbers and tables are frequently transcribed incorrectly |
| Synthesis and writing | Summarising your own notes, polishing the English, proposing a structure | Writing up findings without having read the studies; inventing citations |

A pattern common to all studies: high sensitivity is only achieved by accepting many false positives, results vary with the prompt and the model version, and with older datasets there is a risk that the model has seen the reviews during training ([Dennstädt et al., 2024](https://boris.unibe.ch/197864/1/s13643-024-02575-4.pdf)). Model versions change every few months, so these figures go out of date; what does not go out of date is the obligation to validate on your own dataset.

## Protocol for responsible use

1. Define tasks, model, version, prompts, parameters and oversight before use; document amendments.
2. Build a reference set assessed by two people with consensus resolution. Justify its size and composition: include enough relevant studies, uncertain cases and different document types. Separate prompt tuning from final validation.
3. Report true and false positives and negatives, sensitivity, specificity, precision and confidence intervals. **Neither 100–200 records nor a point sensitivity of 95% guarantees safety.** Recovering all five relevant studies still leaves substantial uncertainty about sensitivity.
4. Use the model to prioritise or propose decisions; a human verifies exclusions and resolves disagreements. An LLM does not count as a second independent human reviewer. Audit human–AI agreement too, since both may share errors.
5. Retain inputs, outputs, versions, dates and final decisions; verify each extracted item against its source page. Revalidate after important changes to the model, prompt or corpus.
6. Respect licences and document processing conditions; use appropriate institutional services. Declare use in Methods, materials and the selection flow where applicable.

Stopping solely after 50–100 consecutive irrelevant records does not demonstrate complete evidence retrieval. The protocol must justify the risk of omissions and the checking procedure.

## Guidelines and standards

- **RAISE** (*Responsible AI use in Evidence Synthesis*, [Cochrane, 2025](https://www.cochrane.org/events/recommendations-and-guidance-responsible-ai-evidence-synthesis)): three documents with recommendations by role, how to evaluate tools and how to select and use them; endorsed by more than 30 organisations. The [Cochrane AI Methods Group](https://www.cochrane.org/about-us/news/new-ai-methods-group-spearhead-adoption-across-four-leading-evidence-synthesis-organizations) (February 2025) coordinates its development.
- **CEE reporting guidance** ([living document](https://environmentalevidence.org/artificial-intelligence-reporting-guidance/)): for each AI system, name, version and developer; rationale and validation studies; automated tasks; own validation or the reason for not performing it; limitations; prompts and code as supplementary material; funding and conflicts of interest. It includes a template paragraph for the Methods section.
- **PRISMA 2020**: items 8 and 9 (selection and extraction) already ask you to state the automation tools used. The [PRISMA-trAIce](https://ai.jmir.org/2025/1/e80247) extension (JMIR AI, December 2025) proposes 14 items and a flow diagram that separates human and AI exclusions; it is a proposal without formal endorsement yet. Not to be confused with PRISMA-AI, which is for reviews of clinical AI studies.
- Cochrane's **Screen4Me** reduces records by 50 to 70% in reviews of trials, but only for Cochrane reviews.

## What publishers require

| Publisher | Policy |
| --- | --- |
| [Elsevier](https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals) (IST, JSS, C&E) | AI declaration in a dedicated section of the manuscript (tool, purpose, oversight); AI cannot be an author; basic grammar correction is exempt; AI used in the method is described in the Methods section |
| [IEEE](https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/) (TSE, TLT, Access) | Disclose in the acknowledgements the system and the affected sections (text, figures, code); IEEE Access additionally requires citing it in each section containing generated text |
| [ACM](https://www.acm.org/publications/policies/new-acm-policy-on-authorship) (CSUR, TOCE) | AI cannot be an author; disclose generative use, usually in the acknowledgements; spelling/grammar checkers and translation are exempt |
| [Springer Nature](https://link.springer.com/brands/springer/journal-policies) | Traffic light: language polishing (green), evaluative use or writing (amber: verify and declare), AI authorship or fabricated citations (red) |

In all of them, reviewers are forbidden from uploading manuscripts to public tools. Also consult your university’s research-integrity and AI policies; document the rules applicable when the work is performed.


These policy summaries are indicative and change: check the journal’s current instructions at submission and log source and date. Validation percentages above refer to the historical models and datasets cited, not current performance of any LLM.

## Example declaration paragraph

```
During title and abstract screening, GPT-4o (OpenAI, version 2026-05, via API) was used as a second reviewer, with the prompt reproduced in supplementary material S3. On a sample of 200 records screened independently by two authors, the model achieved a sensitivity of 0.97 and a specificity of 0.61 (κ = 0.48). Disagreements between the model and the first reviewer (n = 143) were resolved by the second author. AI was not involved in extraction or synthesis. DeepL Write was used for language polishing of the manuscript; the authors reviewed and are responsible for all content.
```

```{figure} ../../_static/generated/diagrams/en/human_ai_en.svg
:name: fig-human_ai-en
:alt: Human–AI collaboration with human decisions and auditing. An automated proposal does not replace independent human review. Original figure, CC BY 4.0.
:width: 100%
:align: center

Human–AI collaboration with human decisions and auditing. An automated proposal does not replace independent human review. Original figure, CC BY 4.0.
```
