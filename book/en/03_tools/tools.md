# Tools

There is no single best tool; there is a reasonable combination for each phase. For a PhD student with a zero budget, the following works well: Zotero to manage references and remove duplicates, Parsifal or Rayyan for team screening, a shared spreadsheet for extraction, ASReview if the volume exceeds 2,000 records, and the PRISMA 2020 app for the flow diagram. The [Systematic Review Toolbox](http://systematicreviewtools.com/) maintains a catalogue searchable by phase, discipline and cost. Prices and versions checked in October 2026; they change frequently.

## Managing the whole review

| Tool | Phases covered | Cost | Notes |
| --- | --- | --- | --- |
| [Parsifal](https://parsif.al/) | Protocol (objectives, PICOC, questions, search string, sources, criteria), BibTeX import, duplicates, selection, quality, extraction, report | Free, open source (MIT) | Designed for software engineering SLRs following Kitchenham; the most cited in that field. Still operational but with minimal development (latest version 2.2.1, maintenance only); imports only one format and does not integrate with reference managers |
| [Rayyan](https://www.rayyan.ai/pricing) | Deduplication, blind screening with several reviewers, labels, AI ranking | Free (3 active reviews, 2 reviewers); plans from 4.99 USD/month | The most widely used for team screening; ranking requires 50 prior decisions and never decides for you |
| [Covidence](https://www.covidence.org/pricing/) | Screening, full text, extraction, quality, PRISMA | 339 USD/year per review; 500-record trial; institutional licences | Standard in health sciences; relevance sorting and LLM-based extraction suggestions that must be verified |
| [CADIMA](https://www.cadima.info/) | Protocol, search, screening with kappa, extraction, quality, PRISMA | Free (Julius Kühn-Institut) | Very complete and free; less agile interface |
| [PICO Portal](https://picoportal.org/) | AI screening, duplicates, full text, extraction, PRISMA, export to EndNote/Zotero | Paid, with a free single-project version | Compared with Parsifal: assigns roles and integrates with reference managers, but does not assess quality |
| [DistillerSR](https://info.distillersr.com/pricing/student-pricing) | The whole workflow with audit trail | From 19.95 USD/month (student) | Geared towards regulated reviews |
| [EPPI-Reviewer](https://eppi.ioe.ac.uk/cms/er4/About/Fees) | The whole workflow, classifiers | £10/month per user; free for Cochrane and Campbell | Strong in social sciences and education |
| [JBI SUMARI](https://jbi-global.atlassian.net/wiki/spaces/SKB/pages/3345151/Basics+of+JBI+SUMARI) | Protocol to synthesis, including qualitative | 130 USD/year | JBI methodology |
| [Nested Knowledge](https://nested-knowledge.com/) | Search, assisted screening, extraction, synthesis with dashboards | Paid, free trial | Designed for living reviews |
| [Buhos](https://buhos.org/) | Full workflow, web and desktop | Free, open source | Less well known; check whether it is maintained |

## Screening assisted by active learning

[ASReview LAB](https://asreview.nl/) (Utrecht University; version 3.0.8 of June 2026, Apache 2.0, Python 3.10 or later) ranks the pending records according to the decisions you make and retrains the model with each decision. In the original validation ([van de Schoot et al., Nature Machine Intelligence, 2021](https://www.nature.com/articles/s42256-020-00287-7)) screening between 8 and 33% of the records was enough to find 95% of the relevant ones, including a software engineering dataset (8,911 records on fault prediction). [Ferdinands et al. (2023)](https://systematicreviewsjournal.biomedcentral.com/articles/10.1186/s13643-023-02257-7) report work savings between 64 and 92% depending on the dataset, with high variability. Its simulation mode lets you estimate those savings on your own data. Alternatives: [Abstrackr](https://abstrackr.com/) (free; median savings of 35% with 0 to 3 studies missed per review in Gates et al., 2020), [Colandr](https://colandrapp.com/) (free, new version 2.0 in 2026) and [SWIFT-Review](https://www.sciome.com/swift-review/) (free, desktop).

Rule of use: active learning decides the reading **order**, never inclusion; set a stopping criterion in the protocol (for example, 50 or 100 consecutive irrelevant records) and report it.

## Reference managers and deduplication

- [Zotero 7](https://www.zotero.org/blog/zotero-7/) (free, open source; 300 MB of free storage): imports RIS and BibTeX from all databases, [detects duplicates](https://www.zotero.org/support/duplicate_detection) by title, DOI and ISBN together with year and author, and exports to Parsifal, Rayyan or ASReview. It is the recommended option.
- Mendeley (free, Elsevier) and EndNote (paid) are alternatives; EndNote has good deduplication but costs 275 USD (150 for students).
- [Deduplicator](https://pmc.ncbi.nlm.nih.gov/articles/PMC11081115) from the TERA suite (formerly SR-Accelerator, Bond University; free): accepts RIS and XML, groups possible duplicates into four confidence levels and lets you exclude records already screened when updating a review. The same suite offers Polyglot Search to translate a search string between databases and Word Frequency Analyser to find terms.

## Assisted search and discovery

These tools are useful for the preliminary search, for *snowballing* and for building the control set, not as a primary source: their coverage and ranking are not reproducible.

| Tool | What it does | Cost |
| --- | --- | --- |
| [Semantic Scholar](https://www.semanticscholar.org/about) | Open index of more than 200 M papers with a free API; the basis for many of the tools below | Free |
| [Connected Papers](https://www.connectedpapers.com/) | Graph of similar papers based on co-citation and bibliographic coupling | 5 graphs/month free |
| [ResearchRabbit](https://www.researchrabbit.ai/pricing) | Collections and recommendations based on seed papers | Free; RR+ 10 USD/month |
| [Litmaps](https://www.litmaps.com/pricing) | Citation maps with a timeline | Limited free tier; Pro 10 USD/month |
| [Elicit](https://elicit.com/pricing) | Natural-language search over more than 125 M papers and extraction of data from PDFs into tables | Free (10 extractions/month); Plus 12 USD; Pro 49 USD |
| [Scite](https://scite.ai/pricing.md) | Classifies citations as supporting, contrasting or mentioning | 20 USD/month |
| [Undermind](https://www.casrai.org/guides/undermind-ai) | Multi-step search agent over Semantic Scholar | Free; Pro 16 USD/month |
| [Consensus](https://consensus.app/), [SciSpace](https://scispace.com/) | Search with synthesised answers | Free with limits |
| [NotebookLM](https://support.google.com/notebooklm/answer/16213268) | Questions about the PDFs you upload (up to 50 sources per notebook in the free plan) | Free |

## Visualisation and bibliometrics for mapping studies

- [VOSviewer](https://www.vosviewer.com/download) 1.6.21 (June 2026; free, Java): co-authorship, co-citation and term co-occurrence networks from Scopus, WoS or OpenAlex exports.
- [bibliometrix](https://cran.r-project.org/web/packages/bibliometrix/) 5.2.1 (R, GPL-3) with its biblioshiny interface: complete bibliometric analysis without programming.
- [CiteSpace](https://citespace.podia.com/) 7.0.2: paid (65 USD/year).
- [SCImago Graphica](https://www.graphica.app/): charts, maps and networks in the browser, without uploading data to any server.
- For *bubble plots*, trend charts and Sankey diagrams, Excel or Google Sheets, R (ggplot2, ggBubbles) or Python (matplotlib, plotly) are enough; [SankeyMATIC](https://sankeymatic.com/) generates the Sankey diagram in the browser.
- [PRISMA 2020 app](https://estech.shinyapps.io/prisma_flowdiagram/) for the flow diagram, with export to PDF, PNG and SVG.
