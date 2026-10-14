# Fase 2b. Selección de estudios y evaluación de la calidad

La selección convierte cientos o miles de registros en las decenas de estudios primarios que responderán a tus preguntas. Se hace en fases, con criterios fijados en el protocolo y, siempre que sea posible, con más de un revisor.

## Criterios de inclusión y exclusión

Se definen a partir de las preguntas de investigación, más unos criterios genéricos (idioma, fecha, tipo de documento, revisión por pares). Deben ser claros e inequívocos, y cualquier cambio posterior hay que justificarlo y documentarlo; nunca se modifican a la vista de los hallazgos, porque eso introduce sesgo. Los criterios de inclusión se encadenan con AND y los de exclusión con OR: basta un criterio de exclusión para descartar.

Ejemplo (Hou et al., 2024, revisión sobre LLM en ingeniería del software): IC1 el artículo declara que usa un LLM **y** IC2 el estudio aborda una tarea de ingeniería del software **y** IC3 el texto completo es accesible. Criterios de exclusión: EC1 artículos cortos (menos de 8 páginas) **o** EC2 duplicados o versiones distintas del mismo estudio de los mismos autores **o** EC3 libros, tesis, monografías, *keynotes*, paneles o sedes sin revisión por pares completa **o** EC4 demostraciones de herramientas y editoriales **o** EC5 artículos de taller o simposio doctoral **o** EC6 literatura gris (informes técnicos) **o** EC7 no escrito en inglés **o** EC8 menciona LLM sin describir la técnica empleada **o** EC9 usa métodos de ingeniería del software para mejorar los LLM en lugar de LLM para tareas de ingeniería del software. Obsérvese que los tres últimos no son genéricos sino específicos del tema: son los que de verdad separan el estudio relevante del que solo roza el tema. Con esos criterios, más de 218.000 registros se redujeron a 810 tras cribar título y resumen, a 594 tras el texto completo y a 382 tras la evaluación de calidad; el *snowballing* añadió 13, para un total de 395.

Criterios genéricos habituales: fecha (justificada: la aparición de una tecnología, una revisión previa), idioma, tipo de publicación (se suelen excluir editoriales, resúmenes extendidos, pósteres y capítulos sin revisión), población o contexto (nivel educativo, tipo de organización), diseño del estudio (solo empíricos, solo con evaluación) y acceso al texto completo. Cuando un mismo estudio tiene varias publicaciones (congreso y versión extendida en revista), quédate con la más completa e indícalo.

## Las fases de cribado

1. **Ejecutar las consultas** y exportar los registros de cada base (RIS o BibTeX), anotando la fecha.
2. **Eliminar duplicados** con el gestor bibliográfico o una herramienta específica; guarda el número eliminado.
3. **Cribar por título y resumen** aplicando los criterios. En caso de duda, pasa el artículo a la siguiente fase; aquí es mejor ser inclusivo.
4. **Cribar a texto completo**, registrando el motivo de exclusión de cada artículo descartado (PRISMA exige listarlos con sus razones).
5. **Añadir los artículos del *snowballing*** y repetir el cribado sobre ellos hasta que no aparezcan nuevos.

El número de fases depende del volumen de candidatos y del número de revisores. Un cribado típico en informática reduce 2.500 registros a 1.700 tras duplicados, a unos 50 tras título y resumen, y a unos 13 tras texto completo; planifica el tiempo en consecuencia. Antes de cribar en serio, calibra: los revisores cribarán de forma independiente una muestra de 50 a 100 registros, compararan sus decisiones y afinarán la interpretación de los criterios.

## Acuerdo entre revisores

Con un solo revisor el proceso puede considerarse sesgado. Las soluciones, de más a menos robusta:

- Dos revisores independientes en todas las fases, con un tercero para resolver desacuerdos.
- Dos revisores sobre una muestra aleatoria (por ejemplo, el 20 %) y un revisor para el resto, si el acuerdo en la muestra es alto.
- *Test-retest* (Kitchenham et al., 2015): el mismo revisor vuelve a cribar una muestra aleatoria pasado un tiempo y comprueba si obtiene los mismos resultados.

Mide el acuerdo con la **kappa de Cohen** (κ) e infórmalo: por convención, κ por debajo de 0,40 es escaso, entre 0,41 y 0,60 moderado, entre 0,61 y 0,80 sustancial y por encima de 0,80 casi perfecto (Landis & Koch, 1977). Con conjuntos muy desbalanceados (pocos incluidos frente a muchos excluidos) la kappa baja aunque el acuerdo bruto sea alto; en ese caso añade el porcentaje de acuerdo o la PABAK.

## Evaluación de la calidad

La calidad de un estudio es el grado en que su información es veraz, fiable y útil para responder a tus preguntas. Se evalúa con una lista de control de preguntas cerradas puntuadas (Sí = 1, Parcialmente = 0,5, No = 0), y sirve para tres cosas: excluir estudios por debajo de un umbral que fijas en el protocolo, ponderar el peso de cada estudio en la síntesis, o simplemente describir la solidez de la evidencia. En un mapeo normalmente no se hace, o se hace de forma ligera.

Listas de control útiles en informática y educación:

| Instrumento | Para qué tipo de estudio | Notas |
| --- | --- | --- |
| [Dybå & Dingsøyr (2008)](https://ntnu.no/wiki/download/attachments/78978214/TorgeirDings%C3%B8yr_EmpiricalStudiesOfAgileSoftwareDevelopment.pdf?api=v2) | Estudios empíricos de ingeniería del software | 11 criterios sí/no: ¿es investigación y no *lessons learned*?, objetivos, contexto, diseño, reclutamiento, grupo de control, recogida de datos, análisis, reflexividad, hallazgos, valor. La más usada en ingeniería del software |
| Kitchenham & Charters (2007), apéndice | Cualquier estudio empírico de SE | Preguntas por tipo de diseño (experimento, caso, encuesta) |
| [CASP](https://casp-uk.net/casp-tools-checklists/) | Cualitativos, ensayos, cohortes, revisiones | Gratuitas; origen en salud, adaptables |
| [MMAT 2018](https://www.recercat.cat/handle/2072/354452) | Estudios cualitativos, cuantitativos y mixtos | Cinco categorías, cinco criterios cada una; útil en educación |
| [AMSTAR 2](https://amstar.ca/Amstar-2.php) | Para evaluar revisiones sistemáticas (estudios terciarios) | 16 ítems; valoración global alta, moderada, baja o críticamente baja |
| [ROBIS](https://www.bristol.ac.uk/population-health-sciences/projects/robis/robis-tool/) | Riesgo de sesgo de revisiones sistemáticas | Cuatro dominios: elegibilidad, identificación y selección, recogida de datos, síntesis |
| Cochrane RoB 2, Jadad, Newcastle-Ottawa, GRADE | Ensayos clínicos y estudios observacionales en salud | Raramente aplicables fuera de salud |

Puedes añadir preguntas específicas de tu tema ("¿se definen las métricas de forma explícita?", "¿la población son solo estudiantes?"). Hou et al. (2024) usan diez criterios: tres de pertinencia (¿es relevante para ingeniería del software?, ¿usa LLM?, ¿no es un estudio secundario?) y siete de calidad puntuados de 0 a 3 (sede de prestigio, motivación clara, descripción de las técnicas, detalle del montaje experimental y los datos, confirmación de los hallazgos, discusión de contribuciones y limitaciones, aportación a la comunidad), y fijan en el protocolo un umbral de 16,8 sobre 21 puntos para incluir el estudio (14,4 sobre 18 para preprints, a los que no se aplica el criterio de sede). SEGRESS pide llamar a esta fase "riesgo de sesgo" y, si usas la puntuación para excluir, declarar el umbral en el protocolo. Valida la evaluación igual que el cribado: segundo revisor o *test-retest* sobre una muestra.

## Errores frecuentes

```{admonition} Errores frecuentes
:class: warning

- Cribar por título y resumen siendo demasiado estricto, y perder estudios que el resumen describe mal.
- No anotar el motivo de exclusión a texto completo.
- No medir el acuerdo entre revisores, o medirlo y no informarlo.
- Usar la sede de publicación o el número de citas como sustituto de la calidad.
- Inventar una lista de calidad propia cuando existe una validada.
```
