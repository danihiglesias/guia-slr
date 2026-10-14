# Herramientas

No hay una herramienta mejor; hay una combinación razonable por fase. Para un doctorando con presupuesto cero funciona bien: Zotero para gestionar referencias y deduplicar, Parsifal o Rayyan para cribar en equipo, una hoja de cálculo compartida para extraer, ASReview si el volumen supera los 2.000 registros, y la app PRISMA 2020 para el diagrama. El [Systematic Review Toolbox](http://systematicreviewtools.com/) mantiene un catálogo buscable por fase, disciplina y coste. Precios y versiones consultados en octubre de 2026; cambian con frecuencia.

## Gestión de toda la revisión

| Herramienta | Fases que cubre | Coste | Notas |
| --- | --- | --- | --- |
| [Parsifal](https://parsif.al/) | Protocolo (objetivos, PICOC, preguntas, cadena, fuentes, criterios), importación BibTeX, duplicados, selección, calidad, extracción, informe | Gratuita, código abierto (MIT) | Diseñada para SLR de ingeniería del software según Kitchenham; la más citada en ese ámbito. Sigue operativa pero con desarrollo mínimo (última versión 2.2.1, solo mantenimiento); solo importa un formato y no se integra con gestores bibliográficos |
| [Rayyan](https://www.rayyan.ai/pricing) | Deduplicación, cribado a ciegas con varios revisores, etiquetas, ranking por IA | Gratuito (3 revisiones activas, 2 revisores); planes desde 4,99 USD/mes | La más usada para cribar en equipo; el ranking requiere 50 decisiones previas y nunca decide por ti |
| [Covidence](https://www.covidence.org/pricing/) | Cribado, texto completo, extracción, calidad, PRISMA | 339 USD/año por revisión; prueba de 500 registros; licencias institucionales | Estándar en salud; ordenación por relevancia y sugerencias de extracción con LLM que deben verificarse |
| [CADIMA](https://www.cadima.info/) | Protocolo, búsqueda, cribado con kappa, extracción, calidad, PRISMA | Gratuita (Julius Kühn-Institut) | Muy completa y gratuita; interfaz menos ágil |
| [PICO Portal](https://picoportal.org/) | Cribado con IA, duplicados, texto completo, extracción, PRISMA, exportación a EndNote/Zotero | De pago con versión gratuita de un proyecto | Frente a Parsifal: asigna roles y se integra con gestores, pero no evalúa calidad |
| [DistillerSR](https://info.distillersr.com/pricing/student-pricing) | Todo el flujo con auditoría | Desde 19,95 USD/mes (estudiante) | Orientada a revisiones reguladas |
| [EPPI-Reviewer](https://eppi.ioe.ac.uk/cms/er4/About/Fees) | Todo el flujo, clasificadores | 10 £/mes por usuario; gratis para Cochrane y Campbell | Fuerte en ciencias sociales y educación |
| [JBI SUMARI](https://jbi-global.atlassian.net/wiki/spaces/SKB/pages/3345151/Basics+of+JBI+SUMARI) | Protocolo a síntesis, incluida cualitativa | 130 USD/año | Metodología JBI |
| [Nested Knowledge](https://nested-knowledge.com/) | Búsqueda, cribado asistido, extracción, síntesis con paneles | De pago, prueba gratuita | Pensada para revisiones vivas |
| [Buhos](https://buhos.org/) | Flujo completo, web y escritorio | Gratuita, código abierto | Menos conocida; comprueba su mantenimiento |

## Cribado asistido por aprendizaje activo

[ASReview LAB](https://asreview.nl/) (Universidad de Utrecht; versión 3.0.8 de junio de 2026, Apache 2.0, Python 3.10 o superior) ordena los registros pendientes según lo que vas decidiendo y reentrena el modelo con cada decisión. En la validación original ([van de Schoot et al., Nature Machine Intelligence, 2021](https://www.nature.com/articles/s42256-020-00287-7)) bastó cribar entre el 8 y el 33 % de los registros para encontrar el 95 % de los relevantes, incluido un dataset de ingeniería del software (8.911 registros sobre predicción de fallos). [Ferdinands et al. (2023)](https://systematicreviewsjournal.biomedcentral.com/articles/10.1186/s13643-023-02257-7) obtienen ahorros de trabajo entre el 64 y el 92 % según el dataset, con mucha variabilidad. Su modo de simulación permite calcular ese ahorro sobre tus propios datos. Alternativas: [Abstrackr](https://abstrackr.com/) (gratuita; ahorro mediano del 35 % con 0 a 3 estudios perdidos por revisión en Gates et al., 2020), [Colandr](https://colandrapp.com/) (gratuita, nueva versión 2.0 en 2026) y [SWIFT-Review](https://www.sciome.com/swift-review/) (gratuita, escritorio).

Regla de uso: el aprendizaje activo decide el **orden** de lectura, nunca la inclusión; fija un criterio de parada en el protocolo (por ejemplo, 50 o 100 irrelevantes consecutivos) e infórmalo.

## Gestores bibliográficos y deduplicación

- [Zotero 7](https://www.zotero.org/blog/zotero-7/) (gratuito, código abierto; 300 MB de almacenamiento gratis): importa RIS y BibTeX de todas las bases, [detecta duplicados](https://www.zotero.org/support/duplicate_detection) por título, DOI e ISBN con año y autor, y exporta a Parsifal, Rayyan o ASReview. Es la opción recomendada.
- Mendeley (gratuito, Elsevier) y EndNote (de pago) son alternativas; EndNote tiene buena deduplicación pero cuesta 275 USD (150 para estudiantes).
- [Deduplicator](https://pmc.ncbi.nlm.nih.gov/articles/PMC11081115) de la suite TERA (antes SR-Accelerator, Bond University; gratuita): acepta RIS y XML, agrupa posibles duplicados en cuatro niveles de confianza y permite excluir los ya cribados en actualizaciones. La misma suite ofrece Polyglot Search para traducir una cadena entre bases y Word Frequency Analyser para encontrar términos.

## Búsqueda y descubrimiento asistidos

Estas herramientas sirven para la búsqueda preliminar, para el *snowballing* y para construir el conjunto de control, no como fuente principal: su cobertura y su ranking no son reproducibles.

| Herramienta | Qué hace | Coste |
| --- | --- | --- |
| [Semantic Scholar](https://www.semanticscholar.org/about) | Índice abierto de más de 200 M de artículos con API gratuita; base de muchas de las siguientes | Gratuita |
| [Connected Papers](https://www.connectedpapers.com/) | Grafo de artículos similares por cocitación y acoplamiento bibliográfico | 5 grafos/mes gratis |
| [ResearchRabbit](https://www.researchrabbit.ai/pricing) | Colecciones y recomendaciones a partir de artículos semilla | Gratuita; RR+ 10 USD/mes |
| [Litmaps](https://www.litmaps.com/pricing) | Mapas de citas con línea temporal | Gratuita limitada; Pro 10 USD/mes |
| [Elicit](https://elicit.com/pricing) | Búsqueda en lenguaje natural sobre más de 125 M de artículos y extracción de datos de PDF en tablas | Gratuita (10 extracciones/mes); Plus 12 USD; Pro 49 USD |
| [Scite](https://scite.ai/pricing.md) | Clasifica citas en apoyo, contraste o mención | 20 USD/mes |
| [Undermind](https://www.casrai.org/guides/undermind-ai) | Agente de búsqueda multi-paso sobre Semantic Scholar | Gratuita; Pro 16 USD/mes |
| [Consensus](https://consensus.app/), [SciSpace](https://scispace.com/) | Búsqueda con respuestas sintetizadas | Gratuitas con límites |
| [NotebookLM](https://support.google.com/notebooklm/answer/16213268) | Preguntas sobre los PDF que subas (hasta 50 fuentes por cuaderno en el plan gratuito) | Gratuita |

## Visualización y bibliometría para mapeos

- [VOSviewer](https://www.vosviewer.com/download) 1.6.21 (junio de 2026; gratuito, Java): redes de coautoría, cocitación y co-ocurrencia de términos a partir de exportaciones de Scopus, WoS o OpenAlex.
- [bibliometrix](https://cran.r-project.org/web/packages/bibliometrix/) 5.2.1 (R, GPL-3) con su interfaz biblioshiny: análisis bibliométrico completo sin programar.
- [CiteSpace](https://citespace.podia.com/) 7.0.2: de pago (65 USD/año).
- [SCImago Graphica](https://www.graphica.app/): gráficos, mapas y redes en el navegador, sin subir datos a ningún servidor.
- Para *bubble plots*, gráficos de tendencia y Sankey bastan Excel o Google Sheets, R (ggplot2, ggBubbles) o Python (matplotlib, plotly); [SankeyMATIC](https://sankeymatic.com/) genera el Sankey en el navegador.
- [App PRISMA 2020](https://estech.shinyapps.io/prisma_flowdiagram/) para el diagrama de flujo, con exportación a PDF, PNG y SVG.
