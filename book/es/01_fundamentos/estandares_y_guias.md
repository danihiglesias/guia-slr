# Estándares y guías que debes conocer

Para una SLR en informática hoy necesitas tres cosas: una guía de **proceso** (Kitchenham & Charters para SLR; Petersen para mapeos), una guía de **reporte** (PRISMA 2020 o su adaptación SEGRESS) y, si publicas en una sede ACM/IEEE, el **estándar empírico** de SIGSOFT. Los marcos SALSA y PSALSAR sirven para comprobar que el diseño cubre las cuatro dimensiones (sistemática, completa, explícita, reproducible).

| Guía | Año | Para qué sirve | Dónde |
| --- | --- | --- | --- |
| Kitchenham & Charters, EBSE-2007-01 | 2007 | Proceso completo de una SLR en ingeniería del software: planificación, conducción y reporte | [Informe técnico](https://legacyfileshare.elsevier.com/promis_misc/525444systematicreviewsguide.pdf) |
| Kitchenham, Budgen & Brereton, *Evidence-Based Software Engineering and Systematic Reviews* | 2015 | Libro que sustituye a los informes de 2004 y 2007; incluye estudios primarios, síntesis y traslación de conocimiento | [Routledge](https://www.routledge.com/Evidence-Based-Software-Engineering-and-Systematic-Reviews/Kitchenham-Budgen-Brereton/p/book/9781482228656) |
| Petersen et al., EASE | 2008 | Proceso del mapeo sistemático: preguntas, búsqueda, cribado, *keywording* de resúmenes, extracción y mapa | [PDF](https://www.cse.chalmers.se/~feldt/publications/petersen_ease08_sysmap_studies_in_se.pdf) |
| Petersen, Vakkalanka & Kuzniarz, IST | 2015 | Actualización de las guías de mapeo tras analizar cómo se aplicaban; concluye que las guías de 2008 "no bastan por sí solas" | [EBSE](https://ebse.webspace.durham.ac.uk/?p=466) |
| Wohlin, EASE | 2014 | *Snowballing* hacia atrás y hacia delante como estrategia de búsqueda; premio al artículo más influyente EASE 2024 | [EASE 2024 award](https://conf.researchr.org/details/ease-2024/ease-2024-most-influential-paper-award/1/Guidelines-for-snowballing-in-systematic-literature-studies-and-a-replication-in-soft) |
| Garousi, Felderer & Mäntylä, IST | 2019 | Literatura gris y revisiones multivocales (MLR) | [arXiv](https://arxiv.org/abs/1707.02553v4) |
| PRISMA 2020 (Page et al., BMJ) | 2021 | Lista de 27 ítems para **reportar** una revisión y diagrama de flujo; no evalúa la calidad de la revisión | [prisma-statement.org](https://www.prisma-statement.org/prisma-2020-checklist) |
| SEGRESS (Kitchenham, Madeyski & Budgen, IEEE TSE) | 2023 | Adaptación de PRISMA 2020 a los estudios secundarios de ingeniería del software: SLR, mapeos, terciarios, cualitativos | [Checklist](https://ebse.webspace.durham.ac.uk/reporting/) |
| ACM SIGSOFT Empirical Standards (Ralph et al.) | 2020–2021 | Lo que un revisor de ICSE/FSE/EMSE esperará ver en una revisión sistemática | [Estándar Systematic Reviews](https://github.com/acmsigsoft/EmpiricalStandards/blob/master/docs/standards/SystematicReviews.md) |

## PRISMA 2020 en detalle

PRISMA (*Preferred Reporting Items for Systematic Reviews and Meta-Analyses*) nació en 2009 y se actualizó en 2021 ([Page et al., BMJ 2021;372:n71](https://www.bmj.com/content/372/bmj.n71)). Su objetivo es que el informe de la revisión sea completo y transparente; sirve también para evaluar críticamente revisiones publicadas, pero **no** es un instrumento de calidad metodológica. Consta de un checklist de 27 ítems en siete secciones, un checklist de 12 ítems para el resumen y un diagrama de flujo.

Qué cambió respecto a 2009 y conviene tener presente:

- El ítem de búsqueda exige las estrategias completas de **todas** las bases de datos, registros y webs consultadas, no solo una de ejemplo.
- Hay que indicar cuántos revisores cribaron cada registro, si trabajaron de forma independiente y qué herramientas de automatización se usaron.
- La síntesis se desglosa en seis subítems de métodos y cuatro de resultados.
- Se añaden ítems sobre certeza de la evidencia, conflictos de interés y disponibilidad de datos, código y materiales.
- El diagrama de flujo tiene dos brazos: bases de datos y registros, y "otros métodos" (búsqueda por citas, webs, organizaciones), que se añade solo si se usaron. Hay [cuatro plantillas oficiales](https://www.prisma-statement.org/prisma-2020-flow-diagram) y una [aplicación web gratuita](https://estech.shinyapps.io/prisma_flowdiagram/) (Haddaway et al., 2022) que genera el diagrama en PDF, PNG o SVG.

Existe una [traducción oficial al español de la declaración](https://www.prisma-statement.org/s/PRISMA-2020-Spanish.pdf) (Rev Esp Cardiol 2021;74(9):790–799), y la web de PRISMA enlaza también el [checklist y el diagrama en español](https://www.prisma-statement.org/translations).

## Extensiones de PRISMA útiles en informática

- **PRISMA-S** ([Rethlefsen et al., 2021](https://systematicreviewsjournal.biomedcentral.com/articles/10.1186/s13643-020-01542-z)): 16 ítems para documentar la búsqueda (nombre de cada base, cadena completa, límites, filtros, fechas, revisión por pares de la estrategia, total de registros y deduplicación). Es la mejor lista de control para la sección de búsqueda de cualquier SLR.
- **PRISMA-ScR** ([Tricco et al., 2018](https://www.prisma-statement.org/scoping)): 20 ítems esenciales para scoping reviews; SEGRESS la recomienda también para mapeos.
- **PRISMA-P** ([Moher et al., 2015](https://www.prisma-statement.org/protocols)): 17 ítems para redactar el protocolo.

## SEGRESS: PRISMA adaptado a la ingeniería del software

[SEGRESS](https://madeyski.e-informatyka.pl/segress-software-engineering-guidelines-for-reporting-secondary-studies/) (IEEE TSE 49(3), 2023) toma los 27 ítems de PRISMA 2020, los combina con PRISMA-S, PRISMA-P y PRISMA-ScR, e indica para cada ítem a qué tipo de estudio secundario aplica (SLR cuantitativa, mapeo, terciario, cualitativo, mixto). Sustituye "evaluación de calidad" por "riesgo de sesgo" y "amenazas a la validez" por "limitaciones". Si vas a publicar en IST, JSS o TSE, es el checklist que debes seguir.

## ACM SIGSOFT Empirical Standards

El [estándar para revisiones sistemáticas](https://github.com/acmsigsoft/EmpiricalStandards/blob/master/docs/standards/SystematicReviews.md) lista atributos **esenciales** (tipo de revisión identificado; búsqueda replicable paso a paso con los términos; criterios de selección claros; extracción y síntesis detalladas; esquema de codificación; cadena de evidencia; conclusiones útiles para profesionales) y **deseables** (protocolo, búsquedas y dataset como material suplementario; *snowballing* y preprints para mitigar sesgo; evaluación de calidad definida a priori; dos analistas con medida de acuerdo; diagrama PRISMA; meta-análisis sin *vote counting*). Nombra dos antipatrones: la "lista de la compra" de artículos sin síntesis y usar la sede de publicación como sustituto de la calidad.

## SALSA y PSALSAR

Grant & Booth (2009) proponen el marco SALSA (*Search, AppraisaL, Synthesis, Analysis*) para comprobar si un método de revisión cumple las cuatro dimensiones. Mengist et al. (2020) lo amplian a PSALSAR añadiendo el **protocolo** al principio y el **reporte** (con PRISMA) al final, en seis pasos: Protocol, Search, Appraisal, Synthesis, Analysis, Report. Es un buen esqueleto para la sección de metodología de tu artículo.
