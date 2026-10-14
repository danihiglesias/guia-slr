# Guided case study

The following case is a single-author SLR on metrics for assessing the performance of surgical residents using haptic simulators. It is small (fewer than 50 candidates) and therefore illustrates well the decisions and validations that need to be planned when there is no team.

## 1. Question and PICOC

Question: *In the field of surgery, what metrics exist to objectively assess a resident's performance using haptic simulators?*

| Criterion | Value | Keywords |
| --- | --- | --- |
| Population / Problem | Objective performance assessment; resident | "objective assessment"; performance; resident |
| Intervention | Haptic simulator | "haptic simulator" |
| Comparison | None | — |
| Outcome | Metrics | metric |
| Context | Surgery | surgery |

## 2. Quasi-gold standard set

Before searching, identify by hand (or by asking an expert) a small set of papers that directly answer the question (Zhang, Babar & Tell, 2011, call it the *quasi-gold standard*). It will be used to extract keywords from their titles and abstracts and to validate the search string: a reasonable criterion is that the automated search should retrieve **at least 70%** of those papers; if not, the string is revised.

## 3. Sources and restrictions

Five or six sources combining general and specific ones: Web of Science, Scopus, ScienceDirect, IEEE Xplore and ACM DL (the last two specific to computing). Declared restrictions: search in title, abstract and keywords; English only; journal or conference papers only. The acknowledged limitation (only sources accessible from the University of León) is compensated for with complementary searching and grey literature.

## 4. Search string, iterated

```
Base string (WoS, 1 result):
("objective assessment" AND performance AND resident) AND "haptic simulator" AND metric AND surgery

Extended string (WoS, 17 results):
("objective assessment" AND performance AND resident*) AND ("haptic simulat*" OR "virtual reality") AND metric* AND surg*
```

The first version returned a single paper; truncating (*resident\**, *metric\**, *surg\**) and adding a synonym for the intervention extended it to 17. Broadening brings in false positives; narrowing loses relevant papers (false negatives): the quasi-gold standard set is what tells you when to stop.

## 5. Selection criteria and phases

Inclusion: in English; journal or conference paper; defines assessment metrics; the metrics assess the performance of a resident or final-year student using a haptic or virtual simulator. Exclusion: another type of simulator (augmented reality, physical models); metrics on other aspects (realism, human factors, novice/expert discrimination).

With a single reviewer and few candidates, two phases are planned: (1) remove duplicates and review title and abstract, excluding if at least one exclusion criterion is met and moving on to the next phase in case of doubt; (2) download and review the full text with the same criteria. Validation by *test-retest* on a random sample; if the results differ, the criteria are revised.

## 6. Quality, extraction and synthesis

Dybå & Dingsøyr (2008) checklist scored Yes = 1, Partially = 0.5, No = 0, plus two specific questions (are the metrics clearly defined? is the population only students or residents?). Extraction in a spreadsheet with identifier, reference, metrics (type and description), resident's level of experience (none, final-year student, resident) and number of participants. Synthesis with a table of relevant papers, a trend chart by year and a bubble plot crossing level of experience and prior experience with simulators (X axes) against type of metric (Y axis).

## How you would do it today, with what this guide adds

- Register the protocol on OSF before launching the search and cite its DOI.
- Document the search with the 16 PRISMA-S items and add backward and forward *snowballing* from the included studies.
- Recruit a second reviewer for a 20% sample and report kappa, in addition to the *test-retest*.
- If an LLM is used as a second reviewer, validate it on that same sample and declare it.
- Generate the diagram with the PRISMA 2020 app and complete the SEGRESS checklist before submitting.
- Deposit the screening sheet, extraction sheet and search strings on Zenodo.

## The mistakes we see most often in PhD students

```{admonition} The mistakes we see most often in PhD students
:class: warning

1. Starting with the search string instead of the question.
2. Choosing a topic for which a recent SLR already exists and neither citing it nor justifying the new one.
3. Using only Google Scholar or only one database.
4. Not keeping the original exports or the search date, and being unable to reconstruct the PRISMA diagram.
5. Screening alone, without any validation, and not mentioning it as a limitation.
6. Confusing a mapping study with an SLR, so that the title promises what the method does not deliver.
7. Synthesising paper by paper instead of by question.
8. Submitting to a journal that no longer accepts reviews or whose format does not allow the necessary length.
9. Using AI to screen or extract without validating or declaring it.
10. Taking so long that the search becomes outdated; if more than 12 months pass, rerun the search before submitting.
```
