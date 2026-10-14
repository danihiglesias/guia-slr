# Review types and which one to choose

The choice depends on two questions: do you know the area in depth? And is the evidence comparable? If you do not know the area, conduct a systematic mapping study. If you know it and the studies measure comparable variables, a meta-analysis. If you know it but the evidence is heterogeneous, a systematic review.

| Type | Typical question | What it produces | Quality appraisal | Reference guideline |
| --- | --- | --- | --- | --- |
| Systematic review (SLR) | What is known about X? What solutions exist and how do they work? | In-depth synthesis of the evidence on a specific question | Yes, mandatory | Kitchenham & Charters (2007); PRISMA 2020; SEGRESS |
| Systematic mapping study (SMS) | How much has been published, by whom, where and on which subtopics? | Classification and count of the literature; maps, *bubble plots*, trends | Usually not, or light | Petersen et al. (2008, 2015); PRISMA-ScR |
| Meta-analysis | What is the combined effect of intervention X? | Aggregated statistical estimate (effect size) | Yes, with risk of bias | Cochrane Handbook; PRISMA 2020 |
| Scoping review | What concepts, types of evidence and gaps exist in an emerging field? | Conceptual map of the area; often precedes an SLR | Optional | PRISMA-ScR (Tricco et al., 2018); JBI |
| Multivocal review (MLR) | What do academia **and** professional practice (blogs, reports, videos) say? | SLR that incorporates grey literature | Yes, with criteria for grey sources | Garousi et al. (2019) |
| Tertiary study / umbrella review | What do already published systematic reviews say? | Synthesis of reviews (the unit is the SLR) | Yes, with AMSTAR 2 or ROBIS | Kitchenham et al. (2009, 2010) |
| Rapid review | Same as an SLR, with fewer resources and a short deadline | Simplified synthesis; document the shortcuts | Simplified | Cochrane Rapid Reviews Methods Group |

## SLR versus systematic mapping study

The difference can be summarised as follows: a systematic review details the state of the art and seeks results that answer open questions; a mapping study gives a broad overview and identifies the volume of evidence, the types of research and the available results. In practice the term "systematic review" is used interchangeably for both, and both can be published in a journal and serve as a chapter of a thesis or master's dissertation.

The combination works better than either one on its own: an initial mapping study tells you where the bulk of the literature lies, and a subsequent SLR delves into the subset that answers your question. Mapping questions are of the kind "how many studies were published per year?", "who are the most active authors?", "in which domains has it been applied?" or, in a review on LLMs in software engineering, "which models are used and for which tasks?" (Hou et al., 2024); SLR questions are of the kind "what solutions have been used for X?" and "how do they address X?".

## Systematic review versus meta-analysis

An SLR answers a question by collecting and summarising all the empirical evidence with an explicit method; a meta-analysis is the use of statistical methods to combine the results of similar studies and obtain more precise estimates. Every quantitative SLR is a prerequisite for a meta-analysis, but not every SLR contains one (Kitchenham & Charters, 2007; Mujica-Sequera, 2022). In engineering and computer science, meta-analysis is uncommon because primary studies rarely measure the same variables with comparable designs; when you do one, avoid *vote counting* (counting how many studies come out positive), a practice that the [ACM SIGSOFT Empirical Standards](https://github.com/acmsigsoft/EmpiricalStandards/blob/master/docs/standards/SystematicReviews.md) explicitly discourage.
