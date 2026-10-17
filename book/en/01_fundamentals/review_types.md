# Review types and which one to choose

Choose the design according to the objective: classify a field (mapping), clarify concepts and evidence types (scoping), or answer a focused question through critical synthesis (SLR). Meta-analysis is a synthesis technique that may form part of an SLR when studies are sufficiently compatible. The team’s prior knowledge affects preparation, but does not determine the design.

| Type | Typical question | What it produces | Quality appraisal | Reference guideline |
| --- | --- | --- | --- | --- |
| Systematic review (SLR) | What is known about X? What solutions exist and how do they work? | In-depth synthesis of the evidence on a specific question | Yes, mandatory | Kitchenham & Charters (2007); PRISMA 2020; SEGRESS |
| Systematic mapping study (SMS) | How much has been published, by whom, where and on which subtopics? | Classification and count of the literature; maps, *bubble plots*, trends | Usually not, or light | Petersen et al. (2008, 2015); PRISMA-ScR |
| Meta-analysis | What is the combined effect of intervention X? | Aggregated statistical estimate (effect size) | Yes, with risk of bias | Cochrane Handbook; PRISMA 2020 |
| Scoping review | What concepts, types of evidence and gaps exist in an emerging field? | Conceptual map of the area; often precedes an SLR | Optional | PRISMA-ScR (Tricco et al., 2018); JBI |
| Multivocal review (MLR) | What do academia **and** professional practice (blogs, reports, videos) say? | SLR that incorporates grey literature | Yes, with criteria for grey sources | Garousi et al. (2019) |
| Tertiary study / umbrella review | What do already published systematic reviews say? | Synthesis of reviews (the unit is the SLR) | Yes, with AMSTAR 2 or ROBIS | Kitchenham et al. (2009, 2010) |
| Rapid review | Same as an SLR, with fewer resources and a short deadline | Simplified synthesis; document the shortcuts | Simplified | Cochrane Rapid Reviews Methods Group |


```{figure} ../../_static/generated/diagrams/en/review_choice_en.svg
:name: fig-review_choice-en
:alt: Choose by objective. Designs can be combined with justification; meta-analysis is a synthesis technique. Original figure, CC BY 4.0.
:width: 100%
:align: center

Choose by objective. Designs can be combined with justification; meta-analysis is a synthesis technique. Original figure, CC BY 4.0.
```


## SLR versus systematic mapping study

The difference can be summarised as follows: a systematic review details the state of the art and seeks results that answer open questions; a mapping study gives a broad overview and identifies the volume of evidence, the types of research and the available results. In practice the term "systematic review" is used interchangeably for both, and both can be published in a journal and serve as a chapter of a thesis or master's dissertation.

Combining the designs can be useful when this matches the objectives and available resources: an initial mapping study tells you where the bulk of the literature lies, and a subsequent SLR delves into the subset that answers your question. Mapping questions are of the kind "how many studies were published per year?", "who are the most active authors?", "in which domains has it been applied?" or, in a review on LLMs in software engineering, "which models are used and for which tasks?" (Hou et al., 2024); SLR questions are of the kind "what solutions have been used for X?" and "how do they address X?".

## Systematic review versus meta-analysis

An SLR answers a question by collecting and summarising all the empirical evidence with an explicit method; a meta-analysis is the use of statistical methods to combine the results of similar studies and obtain more precise estimates. Meta-analysis may form part of an SLR, but not every SLR contains one (Kitchenham & Charters, 2007; Mujica-Sequera, 2022). In engineering and computer science, meta-analysis is uncommon because primary studies rarely measure the same variables with comparable designs; when you do one, avoid *vote counting* (counting how many studies come out positive), a practice that the [ACM SIGSOFT Empirical Standards](https://github.com/acmsigsoft/EmpiricalStandards/blob/master/docs/standards/SystematicReviews.md) explicitly discourage.
