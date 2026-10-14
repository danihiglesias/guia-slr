# Phase 2a. Search: sources, strings and documentation

The search must be replicable: another researcher, with your string, your database and your date, should obtain (almost) the same records. Only 43% of 311 analysed software engineering SLRs publish reusable strings, and fewer than 5% reproduce their results ([Li, 2021](https://arxiv.org/pdf/2103.01381)); do not become part of that statistic.

## Where to search

Do not limit yourself to the largest databases; combine at least one multidisciplinary index (Scopus or Web of Science) with the digital libraries of your field, and add *snowballing*. Google Scholar is useful for the preliminary search and for *forward snowballing*, but not as a primary source.

| Source | Coverage | Export limits and replicability | For whom |
| --- | --- | --- | --- |
| [Scopus](https://www.elsevier.support/scopus/answer/what%20content-is%20indexed-in-scopus) | More than 83 M records since 1823; 25,000 active journals; 10.5 M conference papers | Up to 20,000 records in CSV (citations only) or 2,000 in RIS; stable syntax (TITLE-ABS-KEY) | Everyone; the best first choice in computer science and education |
| [Web of Science](https://library-guides.ucl.ac.uk/web-of-science/exporting) | Core of JCR journals; fewer proceedings than Scopus | 1,000 records per export (ranges); minimum truncation of 3 characters; TS= field | Everyone; necessary if the venue values JCR |
| [IEEE Xplore](https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore/search-results-page) | IEEE journals and conferences | Maximum of 6 wildcards; export limited to about 2,000 records in CSV; some patterns return errors | Computer science, engineering, educational technology (TLT, FIE, EDUCON) |
| [ACM Digital Library](https://libraries.acm.org/training-resources/search-tools) | ACM full text plus the *Guide to Computing Literature* | No proximity operators; no official bulk export; it is advisable to restrict to "ACM Full-Text" to avoid duplicates | Computer science, HCI, computing education (SIGCSE, ITiCSE) |
| [SpringerLink](https://support.springernature.com/en/support/solutions/articles/6000134488-download-export-a-list-of-search-results-in-springerlink) | Journals, books and LNCS | CSV of up to 1,000 results with an account; field search in title only | Computer science (LNCS), education |
| ScienceDirect | Elsevier journals (IST, JSS, C&E) | Maximum of 8 Boolean operators per field and 500 characters; no wildcards | If Scopus is not enough for full text |
| [ERIC](https://eric.ed.gov/?faq) | About 1.5 M education records since 1966 | API and download; its own thesaurus | Education and educational technology |
| [Google Scholar](https://aarontay.substack.com/p/why-exactly-is-google-scholar-bad-for) | Everything, including grey literature | Maximum of 1,000 results, 256-character queries, no API or bulk export, opaque ranking and non-reproducible results | Only for preliminary searches, *snowballing* and grey literature; Gusenbauer & Haddaway (2020) consider it unsuitable as a primary source |
| [dblp](https://dagstuhl.de/dblp) | More than 6.5 M computer science publications; CC0 data with API | Metadata only, no abstracts | Verifying venues and authors in computer science |
| [OpenAlex](https://help.openalex.org/data/works/) / [Semantic Scholar](https://www.semanticscholar.org/about) / [Lens.org](https://researchguides.library.syr.edu/lensguide/use) | Open indexes of 200 to 320 M records with a free API | OpenAlex: around 40% without an abstract and 64% without references; Lens exports 50,000 records with a free account | Open, API-reproducible complement; useful for automated *snowballing* |

## Building the search string

1. **Derive the concepts from PICOC**: usually population, intervention and outcome; context rarely goes into the string.
2. **Expand each concept with synonyms**: derived terms, spelling variants (*modelling*/*modeling*), acronyms (HCI), terms in other languages where appropriate, and descriptors from the database thesaurus (MeSH in MEDLINE, ERIC thesaurus, IEEE Thesaurus, ACM CCS).
3. **Join synonyms with OR and concepts with AND**; avoid NOT except to exclude a clearly unrelated domain, because it removes relevant records that mention the term in passing.
4. **Use parentheses** to set precedence and quotation marks for exact phrases; truncation (\*) broadens the search (*analy\** covers *analysis*, *analyse*, *analytics*).
5. **Test the string against a control set**: 5 to 10 papers that you know must appear. If any is missing, revise the terms.
6. **Adapt the syntax to each database** and save the exact version.

Example from Hou et al. (2024), a systematic review on the use of large language models (LLMs) in software engineering tasks, published in *ACM Transactions on Software Engineering and Methodology* with all its materials openly available. The string combines two concepts, each with a long list of synonyms joined by OR:

```
Concept 1 (software engineering tasks):
  "Software Engineering" OR "Software Development" OR Program* OR "Code Generation"
  OR "Code Completion" OR "Code Summarization" OR "Bug Detection" OR "Program Repair"
  OR "Test Generation" OR "Vulnerability Detection" OR ...

Concept 2 (language models):
  LLM OR "Large Language Model*" OR "Language Model*" OR LM OR PLM OR Pretrained
  OR "Pre-trained" OR GPT OR ChatGPT OR Codex OR BERT OR CodeBERT OR T5 OR LLaMA OR ...

Final string:  (Concept 1) AND (Concept 2)
```

The search was run on seven sources (IEEE Xplore, ACM Digital Library, ScienceDirect, Web of Science, SpringerLink, arXiv and dblp), limited to January 2017–January 2024, and returned more than 218,000 records, which the screening phases reduced to 395 included studies. Three practices from that review are worth copying: before the automated search, they performed a manual search in six reference venues (ICSE, FSE, ASE, ISSTA, TOSEM and TSE) and used it to build a control set of 51 papers (*quasi-gold standard*) to validate the string; they included arXiv and dblp as sources complementary to the traditional libraries; and they published the strings adapted to each database, the lists of papers and the screening decisions in a public repository, so that anyone can replicate the search.

The strings for each database must be identical or equivalent; otherwise, the results are not comparable. The example by Ferreras-Fernández et al. (2016) shows an additional good practice: recording in a table each numbered query (#1, #2…), the field (title, topic), the filters (years, languages) and the number of results, and combining them at the end (#1 OR #2 OR #3 OR #4).

## Snowballing

The guidelines by [Wohlin (2014)](https://conf.researchr.org/details/ease-2024/ease-2024-most-influential-paper-award/1/Guidelines-for-snowballing-in-systematic-literature-studies-and-a-replication-in-soft) propose starting from a heterogeneous initial set (different authors, years and venues) and reviewing the reference lists (*backward*) and the citations received (*forward*, with Google Scholar or Scopus) until an iteration yields no new papers. Wohlin et al. (2022) show that the hybrid Scopus + *snowballing* strategy finds around 30% more relevant papers than database searching alone. In the PRISMA diagram these papers go in the "other methods" arm.

## Grey literature

In topics where professional practice is ahead of academia (DevOps, LLMs in programming, commercial educational tools), a multivocal review adds technical blogs, reports and documentation. Garousi et al. (2019) provide criteria for deciding whether to include it and how to assess its quality (authorship, date, methodology, citations). Document Google searches with the date, the number of pages reviewed and the stopping criterion.

## What to document (PRISMA-S)

For each source: name and platform (Scopus via Elsevier), the full string exactly as executed, fields, filters and limits (years, language, document type), date of execution, number of records returned and deduplication method with the number of duplicates removed. If you update the search before submitting the paper, document both runs. Store everything in the supplementary material (Zenodo or OSF).

## Common mistakes

```{admonition} Common mistakes
:class: warning

- A different string for each database without a table of equivalences.
- Reporting "Google Scholar was searched" without a date, without the number of results reviewed or a stopping criterion.
- Not keeping the original export (RIS/BibTeX) from each database.
- Forgetting conference proceedings in fields where they are the main venue (software engineering, HCI).
- Limiting by date or language without justifying it in the protocol.
```
