# IA generativa en una SLR: qué puede hacer y cómo declararlo

La IA generativa ya forma parte del flujo de muchas revisiones, pero la evidencia de 2023 a 2026 es clara: los modelos de lenguaje sirven como **apoyo** (segundo revisor, prefiltro, borrador de extracción), no como sustituto del juicio humano. La postura conjunta de Cochrane, Campbell, JBI y CEE de noviembre de 2025 lo resume: los autores siguen siendo responsables de todo, la IA solo se usa si no compromete el rigor, con supervisión humana, y todo uso que haga o sugiera juicios se declara ([Flemyng et al., 2025](https://www.sei.org/publications/position-statement-on-ai-use-in-evidence-synthesis/)).

## Qué dice la evidencia, fase por fase

| Fase | Qué funciona | Qué no, y evidencia |
| --- | --- | --- |
| Planificación | Afinar preguntas, proponer sinónimos y términos, revisar el protocolo con PRISMA-P | Nada especialmente arriesgado si revisas lo que propone |
| Búsqueda | Generar variantes de cadena y traducirlas entre bases (Polyglot); búsqueda preliminar en Elicit o Undermind | Pedir referencias a un chatbot: [Chelli et al. (2024)](https://www.jmir.org/2024/1/e53164) midieron tasas de referencias inventadas del 28,6 % en GPT-4 y del 39,6 % en GPT-3.5 (91,4 % en Bard), con solo un 16 a 20 % de DOI correctos |
| Cribado por título y resumen | Como apoyo automatizado al cribado con regla "sensible": [Tran et al. (2024)](https://rti.org/publication/sensitivity-specificity-using-gpt-3-5-turbo-models-title-abstract-screening-systematic-reviews-meta) obtienen sensibilidad del 94,6 al 99,8 % perdiendo 0 o 1 de 26 estudios, a costa de una especificidad del 2 al 47 % | Como revisor único: [Guo et al. (2024)](https://www.jmir.org/2024/1/e48996) sobre 24.307 registros obtienen sensibilidad para incluidos de 0,76 (0,59 a 1,0 según revisión). En ingeniería del software, [Felizardo et al. (ESEM 2024)](https://conf.researchr.org/details/esem-2024/esem-2024-technical-track/2/ChatGPT-application-in-Systematic-Literature-Reviews-in-Software-Engineering-an-eval) obtienen un 75 y un 86 % de aciertos con GPT-4 en dos SLR y concluyen que no es aconsejable externalizar la selección; [Thode et al. (IST 2025)](https://www.fortiss.org/ergebnisse/publikationen/details/exploring-the-use-of-llms-for-the-selection-phase-in-systematic-literature-studies) alcanzan un *recall* del 98 al 99 % combinando dos modelos, con una precisión del 27 % |
| Cribado a texto completo | Prometedor con prompts bien diseñados ([Khraisha et al., 2024](https://arxiv.org/abs/2310.17526)) | Dependiente del prompt y de la versión del modelo; resultados no estables |
| Extracción de datos | Borrador de la ficha a partir del PDF (Elicit, Covidence, LLM con el PDF) que un humano verifica campo a campo | Fiabilidad "moderada" tras ajustar por azar (Khraisha et al.); números y tablas se transcriben mal con frecuencia |
| Síntesis y redacción | Resumir tus propias notas, pulir el inglés, proponer estructura | Redactar hallazgos sin haber leído los estudios; inventar citas |

Patrón común de todos los estudios: la sensibilidad alta solo se consigue aceptando muchos falsos positivos, los resultados varían con el prompt y la versión del modelo, y en datasets antiguos hay riesgo de que el modelo haya visto las revisiones durante su entrenamiento ([Dennstädt et al., 2024](https://boris.unibe.ch/197864/1/s13643-024-02575-4.pdf)). Las versiones de modelo cambian cada pocos meses, así que estas cifras caducan; lo que no caduca es la obligación de validar en tu propio conjunto.

## Protocolo de uso responsable

1. Define tareas, modelo, versión, prompts, parámetros y supervisión antes de su uso; documenta los cambios.
2. Construye un conjunto de referencia evaluado por dos personas y resuelto por consenso. Justifica su tamaño y composición: debe incluir suficientes estudios relevantes, casos dudosos y distintos tipos de documento. Separa el ajuste del prompt de la validación final.
3. Informa verdaderos y falsos positivos y negativos, sensibilidad, especificidad, precisión e intervalos de confianza. **Ni 100–200 registros ni una sensibilidad puntual del 95 % garantizan seguridad.** Si solo hay cinco relevantes y se recuperan todos, la evidencia sobre sensibilidad sigue siendo muy imprecisa.
4. Usa el modelo para priorizar o proponer decisiones; un humano verifica las exclusiones y resuelve desacuerdos. Un LLM no cuenta como segundo revisor humano independiente. Audita también el acuerdo humano–IA, que puede compartir errores.
5. Conserva entradas, salidas, versiones, fechas y decisiones finales; verifica cada dato extraído contra su página de origen. Revalida tras cambios importantes del modelo, prompt o corpus.
6. Respeta licencias y condiciones de tratamiento de los documentos; utiliza las opciones institucionales adecuadas. Declara el uso en Métodos, los materiales y el flujo de selección cuando corresponda.

Una regla de parada basada solo en 50–100 irrelevantes consecutivos no demuestra que se haya recuperado toda la evidencia. El protocolo debe justificar el riesgo de omisiones y el procedimiento de comprobación.

## Guías y estándares

- **RAISE** (*Responsible AI use in Evidence Synthesis*, [Cochrane, 2025](https://www.cochrane.org/events/recommendations-and-guidance-responsible-ai-evidence-synthesis)): tres documentos con recomendaciones por rol, cómo evaluar herramientas y cómo seleccionarlas y usarlas; respaldado por más de 30 organizaciones. El [Cochrane AI Methods Group](https://www.cochrane.org/about-us/news/new-ai-methods-group-spearhead-adoption-across-four-leading-evidence-synthesis-organizations) (febrero de 2025) coordina su desarrollo.
- **Guía de reporte de la CEE** ([documento vivo](https://environmentalevidence.org/artificial-intelligence-reporting-guidance/)): para cada sistema de IA, nombre, versión y desarrollador; justificación y estudios de validación; tareas automatizadas; validación propia o motivo para no hacerla; limitaciones; prompts y código como suplemento; financiación y conflictos. Incluye una plantilla de párrafo de Métodos.
- **PRISMA 2020**: los ítems 8 y 9 (selección y extracción) ya piden indicar las herramientas de automatización usadas. La extensión [PRISMA-trAIce](https://ai.jmir.org/2025/1/e80247) (JMIR AI, diciembre de 2025) propone 14 ítems y un diagrama de flujo que separa exclusiones humanas y de IA; es una propuesta sin respaldo formal todavía. No confundir con PRISMA-AI, que es para revisiones de estudios clínicos de IA.
- **Screen4Me** de Cochrane reduce entre el 50 y el 70 % los registros en revisiones de ensayos, pero solo para revisiones Cochrane.

## Qué exigen las editoriales

| Editorial | Política |
| --- | --- |
| [Elsevier](https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals) (IST, JSS, C&E) | Declaración de IA en una sección propia del manuscrito (herramienta, propósito, supervisión); la IA no puede ser autora; la corrección gramatical básica está exenta; la IA usada en el método se describe en Métodos |
| [IEEE](https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/) (TSE, TLT, Access) | Divulgar en los agradecimientos el sistema y las secciones afectadas (texto, figuras, código); IEEE Access además exige citarlo en cada sección con texto generado |
| [ACM](https://www.acm.org/publications/policies/new-acm-policy-on-authorship) (CSUR, TOCE) | La IA no puede ser autora; divulgar el uso generativo, normalmente en agradecimientos; correctores y traducción exentos |
| [Springer Nature](https://link.springer.com/brands/springer/journal-policies) | Semáforo: pulido de lenguaje (verde), uso evaluativo o redacción (ámbar: verificar y declarar), autoría de IA o citas fabricadas (rojo) |

En todas ellas los revisores tienen prohibido subir manuscritos a herramientas públicas. Consulta también el código de integridad y las condiciones de uso de IA de tu universidad; documenta las reglas aplicables en la fecha del trabajo.


Estas políticas son orientativas y cambian: verifica las instrucciones vigentes de la revista al enviar, y registra fuente y fecha. Los porcentajes de validación de la tabla corresponden a los modelos y datasets históricos citados, no al rendimiento actual de cualquier LLM.

## Ejemplo de párrafo de declaración

```
Durante el cribado por título y resumen se utilizó GPT-4o (OpenAI, versión 2026-05, vía API) como segundo revisor, con el prompt reproducido en el material suplementario S3. En una muestra de 200 registros cribados de forma independiente por dos autores, el modelo alcanzó una sensibilidad de 0,97 y una especificidad de 0,61 (κ = 0,48). Los desacuerdos entre el modelo y el primer revisor (n = 143) fueron resueltos por el segundo autor. La IA no intervino en la extracción ni en la síntesis. Para el pulido lingüístico del manuscrito se usó DeepL Write; los autores revisaron y son responsables de todo el contenido.
```

```{figure} ../../_static/generated/diagrams/es/human_ai_es.svg
:name: fig-human_ai-es
:alt: Colaboración humano–IA con decisión humana y auditoría. Una propuesta automatizada no sustituye la revisión humana independiente. Elaboración propia, CC BY 4.0.
:width: 100%
:align: center

Colaboración humano–IA con decisión humana y auditoría. Una propuesta automatizada no sustituye la revisión humana independiente. Elaboración propia, CC BY 4.0.
```
