# Fase 2b. Selección de estudios y evaluación de la calidad

La selección convierte cientos o miles de registros en las decenas de estudios primarios que responderán a tus preguntas. Se hace en fases, con criterios fijados en el protocolo y, siempre que sea posible, con más de un revisor.


```{figure} ../../_static/generated/diagrams/es/records_reports_studies_es.svg
:name: fig-records_reports_studies-es
:alt: Registros, publicaciones y estudios: ejemplo conceptual independiente del dataset, basado en las definiciones PRISMA 2020. Deduplicar y vincular publicaciones son operaciones distintas. Elaboración propia, CC BY 4.0.
:width: 100%
:align: center

Registros, publicaciones y estudios: ejemplo conceptual independiente del dataset, basado en las definiciones PRISMA 2020. Deduplicar y vincular publicaciones son operaciones distintas. Elaboración propia, CC BY 4.0.
```


## Criterios de inclusión y exclusión

Se definen a partir de las preguntas de investigación, más unos criterios genéricos (idioma, fecha, tipo de documento, revisión por pares). Deben ser claros e inequívocos, y cualquier cambio posterior hay que justificarlo y documentarlo; evita cambios guiados por los hallazgos; si una modificación es necesaria, documenta motivo, momento e impacto. Los criterios de inclusión se encadenan con AND y los de exclusión con OR: basta un criterio de exclusión para descartar.

Ejemplo (Hou et al., 2024, revisión sobre LLM en ingeniería del software): IC1 el artículo declara que usa un LLM **y** IC2 el estudio aborda una tarea de ingeniería del software **y** IC3 el texto completo es accesible. Criterios de exclusión: EC1 artículos cortos (menos de 8 páginas) **o** EC2 duplicados o versiones distintas del mismo estudio de los mismos autores **o** EC3 libros, tesis, monografías, *keynotes*, paneles o sedes sin revisión por pares completa **o** EC4 demostraciones de herramientas y editoriales **o** EC5 artículos de taller o simposio doctoral **o** EC6 literatura gris (informes técnicos) **o** EC7 no escrito en inglés **o** EC8 menciona LLM sin describir la técnica empleada **o** EC9 usa métodos de ingeniería del software para mejorar los LLM en lugar de LLM para tareas de ingeniería del software. Obsérvese que los tres últimos no son genéricos sino específicos del tema: son los que de verdad separan el estudio relevante del que solo roza el tema. Con esos criterios, más de 218.000 registros se redujeron a 810 tras cribar título y resumen, a 594 tras el texto completo y a 382 tras la evaluación de calidad; el *snowballing* añadió 13, para un total de 395.

Criterios genéricos habituales: fecha (justificada: la aparición de una tecnología, una revisión previa), idioma, tipo de publicación (se suelen excluir editoriales, resúmenes extendidos, pósteres y capítulos sin revisión), población o contexto (nivel educativo, tipo de organización), diseño del estudio (solo empíricos, solo con evaluación) y acceso al texto completo. Vincula las publicaciones del mismo estudio: pueden aportar datos complementarios. Define qué fuente usarás para cada resultado y evita contar dos veces participantes o efectos. Un texto no recuperado se registra como tal en PRISMA, diferenciado de una exclusión por elegibilidad.

## Las fases de cribado

1. **Ejecutar las consultas** y exportar los registros de cada base (RIS o BibTeX), anotando la fecha.
2. **Eliminar duplicados** con el gestor bibliográfico o una herramienta específica; guarda el número eliminado.
3. **Cribar por título y resumen** aplicando los criterios. En caso de duda, pasa el artículo a la siguiente fase; aquí es mejor ser inclusivo.
4. **Cribar a texto completo**, registrando el motivo de exclusión de cada artículo descartado (PRISMA exige listarlos con sus razones).
5. **Añadir los artículos del *snowballing*** y repetir el cribado sobre ellos hasta que no aparezcan nuevos.

El número de fases depende del volumen de candidatos y del número de revisores. Las tasas de exclusión varían mucho: estima el esfuerzo mediante un pilotaje de tu propio corpus. Antes de cribar en serio, calibra: los revisores cribarán de forma independiente una muestra de 50 a 100 registros, compararán sus decisiones y afinarán la interpretación de los criterios.

## Acuerdo entre revisores

El cribado independiente por dos personas reduce errores; los desacuerdos se resuelven por consenso o una tercera persona. Si solo puedes duplicar una parte, justifica el tamaño y selección de la muestra, cubre las decisiones difíciles y declara la limitación. **El 20 % es un ejemplo de planificación, no un mínimo validado ni una garantía de ausencia de sesgo.** Amplía o repite la calibración si cambian los criterios o aparecen discrepancias relevantes.

Informa el número de registros evaluados por ambos, la tabla de decisiones antes del consenso, el acuerdo bruto y, si procede, kappa con su incertidumbre. Las etiquetas habituales de kappa son orientativas; dependen de prevalencia y márgenes. Una muestra con casi todo excluido puede mostrar gran acuerdo y aun así ocultar errores en estudios relevantes.

El test-retest permite comprobar consistencia del mismo revisor, pero no sustituye una segunda evaluación independiente. Un LLM es una herramienta automatizada y debe describirse y validarse como tal, aunque aporte una segunda propuesta de decisión.

## Evaluación crítica: calidad, riesgo de sesgo y certeza

Son conceptos relacionados que responden a preguntas diferentes:

- **Calidad metodológica:** adecuación y transparencia del diseño, ejecución y análisis de un estudio.
- **Riesgo de sesgo:** posibilidad de que sus métodos distorsionen sistemáticamente un resultado.
- **Certeza de la evidencia:** confianza en una conclusión del conjunto de estudios para un resultado concreto. GRADE considera riesgo de sesgo, inconsistencia, imprecisión, indirectitud y sesgo de publicación {cite:p}`grade2023`.

Elige el instrumento según los diseños incluidos y sigue su manual. No todas las herramientas permiten sumar puntos: **MMAT desaconseja una puntuación global**, y AMSTAR 2 utiliza debilidades críticas, no una suma simple {cite:p}`mmat2018,amstar2017`. Conserva cada juicio por dominio, su justificación y la página o fragmento de apoyo.

| Instrumento | Para qué tipo de estudio | Notas |
| --- | --- | --- |
| [Dybå & Dingsøyr (2008)](https://ntnu.no/wiki/download/attachments/78978214/TorgeirDings%C3%B8yr_EmpiricalStudiesOfAgileSoftwareDevelopment.pdf?api=v2) | Estudios empíricos de ingeniería del software | 11 criterios sí/no: ¿es investigación y no *lessons learned*?, objetivos, contexto, diseño, reclutamiento, grupo de control, recogida de datos, análisis, reflexividad, hallazgos, valor. La más usada en ingeniería del software |
| Kitchenham & Charters (2007), apéndice | Cualquier estudio empírico de SE | Preguntas por tipo de diseño (experimento, caso, encuesta) |
| [CASP](https://casp-uk.net/casp-tools-checklists/) | Cualitativos, ensayos, cohortes, revisiones | Gratuitas; origen en salud, adaptables |
| [MMAT 2018](https://www.recercat.cat/handle/2072/354452) | Estudios cualitativos, cuantitativos y mixtos | Cinco categorías, cinco criterios cada una; útil en educación |
| [AMSTAR 2](https://amstar.ca/Amstar-2.php) | Para evaluar revisiones sistemáticas (estudios terciarios) | 16 ítems; valoración global alta, moderada, baja o críticamente baja |
| [ROBIS](https://www.bristol.ac.uk/population-health-sciences/projects/robis/robis-tool/) | Riesgo de sesgo de revisiones sistemáticas | Cuatro dominios: elegibilidad, identificación y selección, recogida de datos, síntesis |

RoB 2 se dirige a resultados de ensayos aleatorizados; GRADE corresponde al conjunto de evidencia por resultado. Ninguno debe aplicarse automáticamente a cualquier estudio de informática.

Los criterios de Hou et al. (2024) ilustran decisiones de una revisión publicada, no un instrumento universal recomendado. En particular, el prestigio de la sede no sustituye la evaluación metodológica. Justifica cualquier adaptación y cualquier exclusión por evaluación crítica de antemano. No conviertas una suma de calidad en pesos estadísticos: en un metaanálisis los pesos dependen del modelo y de la precisión de las estimaciones.

Explica cómo afecta la evaluación a la síntesis: señalar limitaciones, comparar conclusiones al retirar estudios con problemas importantes o moderar la confianza en los hallazgos. En mapeos descriptivos puede omitirse con justificación; si se extraen conclusiones sobre efectividad, la evaluación crítica resulta necesaria.

Dos personas deben contrastar los juicios y resolver discrepancias. El test-retest mide consistencia de una persona y no equivale a una evaluación independiente.

## Errores frecuentes

```{admonition} Errores frecuentes
:class: warning

- Cribar por título y resumen siendo demasiado estricto, y perder estudios que el resumen describe mal.
- No anotar el motivo de exclusión a texto completo.
- No medir el acuerdo entre revisores, o medirlo y no informarlo.
- Usar la sede de publicación o el número de citas como sustituto de la calidad.
- Inventar una lista de calidad propia cuando existe una validada.
```

```{figure} ../../_static/generated/diagrams/es/prisma_example_es.svg
:name: fig-prisma_example-es
:alt: Flujo docente adaptado de PRISMA 2020 (Page et al., 2021), CC BY 4.0. Datos ficticios: 40 − 8 = 32; 32 − 22 = 10; 10 − 1 = 9; 9 − 4 = 5; 5 + 1 = 6. No son resultados de la revisión original.
:width: 100%
:align: center

Flujo docente adaptado de PRISMA 2020 (Page et al., 2021), CC BY 4.0. Datos ficticios: 40 − 8 = 32; 32 − 22 = 10; 10 − 1 = 9; 9 − 4 = 5; 5 + 1 = 6. No son resultados de la revisión original.
```

```{figure} ../../_static/generated/diagrams/es/appraisal_matrix_es.svg
:name: fig-appraisal_matrix-es
:alt: Juicios por dominio del ejercicio ficticio. NI significa no informado, no riesgo bajo. Los dominios son didácticos, no una escala validada, y no se suman. Elaboración propia, CC BY 4.0.
:width: 100%
:align: center

Juicios por dominio del ejercicio ficticio. NI significa no informado, no riesgo bajo. Los dominios son didácticos, no una escala validada, y no se suman. Elaboración propia, CC BY 4.0.
```

Para una revisión real, usa la [plantilla oficial PRISMA 2020](https://www.prisma-statement.org/prisma-2020-flow-diagram) apropiada para revisión nueva o actualizada y las fuentes utilizadas. Este ejemplo es una adaptación docente, no una plantilla oficial sin modificar. Cuenta registros en identificación/cribado, publicaciones en recuperación/elegibilidad y estudios al final {cite:p}`page2021prisma`. Los datos están en el [caso práctico](../04_practica/caso_practico.md).
