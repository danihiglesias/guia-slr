# What is a systematic literature review

An SLR is a secondary study that identifies, evaluates and interprets all available evidence on a specific research question, following an explicit, unbiased and (to some extent) repeatable method (Kitchenham & Charters, 2007). Unlike original research, the unit of analysis is not people or systems but previous papers: the reviewer poses a question, collects data in the form of studies, analyses them and draws a conclusion.

Its goal is to state what is known about a topic, what has been investigated and what remains unresolved. Its decisive advantage over other reviews is that another researcher can replicate it and check whether they reach the same conclusion (Sáenz, 2001).

## The four dimensions (Codina, 2015)

- **Systematic**: it is neither arbitrary nor subjective; it examines the best available scientific output using the best sources.
- **Comprehensive**: it uses information systems that give access to the bulk of high-quality international output and neither discards nor includes anything without explicit criteria.
- **Explicit**: it publishes the sources, the search criteria and the selection and exclusion criteria.
- **Reproducible**: being systematic and explicit, others can follow the steps and verify the results.

## Origins and communities

SLRs originated in Medicine. The Cochrane Collaboration, founded in 1993, publishes its reviews in the *Cochrane Database of Systematic Reviews*, which in 2025 has an impact factor of 11.1 and brings together more than 154,000 members and supporters in some 210 countries ([Cochrane](https://cochranelibrary.com/cdsr/about-cdsr/impact), [membership dashboard](https://resources.cochrane.org/reports-and-data/membership-dashboard)). The Campbell Collaboration is its sister organisation in the Social Sciences (Petticrew & Roberts, 2005).

In Software Engineering, the *Evidence-Based Software Engineering* (EBSE) community adapted the method from 2004 onwards, with the guidelines by Kitchenham (2004) and Kitchenham & Charters (2007), which remain the reference cited in most computer science SLRs. Since then the field has added its own guidelines for mapping studies (Petersen et al., 2008, 2015), *snowballing* (Wohlin, 2014), grey literature (Garousi et al., 2019) and reporting (SEGRESS, 2023). The standards section goes through them one by one.

## Narrative review versus systematic review

| Feature | Narrative review | Systematic review |
| --- | --- | --- |
| Research question | Broad, unstructured | Structured, clear and specific |
| Literature search | Neither detailed nor systematic; high likelihood of bias | Detailed, systematic and explicit |
| Paper selection | No criteria; not reproducible | Explicit criteria applied uniformly to all papers |
| Quality appraisal | None | Critical appraisal of the methodological quality of each study |
| Synthesis | Subjective, qualitative summary | Based on study quality; often quantified |
| Interpretation | Sometimes evidence-based, often opinion-based | Generally evidence-based |

Adapted from Martín Rodero (2014).

## Systematic or systematized?

The protocol established in the Health Sciences uses statistical methods on quantitative studies (*systematic review*). When it is transferred to fields that do not use statistical analysis, Grant & Booth (2009) and Codina (2015) propose speaking of a *systematized* review (*systematized review*). In practice, the prevailing usage, also in computer science and education, remains *systematic review*; what matters is that the method meets the four dimensions above, not the label.

## Advantages and cost

A well-defined methodology reduces reviewer bias (although it does not protect against publication bias in the primary studies), shows whether a phenomenon is robust across different contexts and, with quantitative studies, allows data to be combined in a meta-analysis that detects effects small studies cannot see. The price is effort: an SLR demands much more time than a traditional review, and it is worth knowing this before you start.
