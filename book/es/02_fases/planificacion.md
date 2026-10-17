# Fase 1. Planificación: de la idea al protocolo

La planificación termina con un protocolo escrito y revisado por alguien que no sea tú. Define preguntas, criterios, fuentes, estrategia de búsqueda, extracción y evaluación crítica antes de la búsqueda definitiva. Las búsquedas exploratorias y los pilotajes permiten afinar el protocolo. Un cambio posterior puede ser necesario: registra fecha, motivo, fase y efecto, y distingue decisiones previas de decisiones informadas por los resultados.


```{figure} ../../_static/generated/diagrams/es/traceability_es.svg
:name: fig-traceability-es
:alt: De RQ1 a la conclusión en el ejercicio ficticio. Cada decisión debe rastrearse hasta su origen. Elaboración propia, CC BY 4.0.
:width: 100%
:align: center

De RQ1 a la conclusión en el ejercicio ficticio. Cada decisión debe rastrearse hasta su origen. Elaboración propia, CC BY 4.0.
```


## Paso 0. ¿Hace falta esta revisión?

Hazte dos preguntas (Kitchenham & Charters, 2007). Primera: ¿es necesaria? Busca en Google Scholar, Scopus y Web of Science con "systematic review", "literature review", "mapping study", "survey" y "state of the art" junto a tu tema. Si ya existe una SLR reciente, solo tiene sentido repetirla si está claramente sesgada o anticuada porque han aparecido estudios nuevos (Petticrew & Roberts, 2005); si no, replantea el tema o conviértela en una actualización. Segunda: ¿tienes los recursos? Una SLR cuesta meses; necesitas tiempo, acceso a las bases de datos (la biblioteca de tu universidad), al menos un segundo revisor y una idea clara de quién va a usar los resultados y cómo.

Antes de seguir fija cuatro cosas: alcance, tiempos, beneficios previstos y dónde piensas publicar, porque la sede condiciona la extensión y el checklist que tendrás que cumplir.

## Paso 1. Preguntas de investigación

La pregunta es el corazón del protocolo: de ella se derivan el título, los objetivos, la cadena de búsqueda y la ficha de extracción. Debe ser clara y específica, y su respuesta debe exigir explicación (nunca un sí o no). Comprueba su pertinencia con el acrónimo FINER:

| Criterio | Pregunta que debes hacerte |
| --- | --- |
| **F**actible | ¿Tengo recursos, acceso y tiempo para responderla? |
| **I**nteresante | ¿Me interesa de verdad a mí y a mi comunidad? |
| **N**ovedosa | ¿Confirma, refuta o amplía hallazgos previos? |
| **É**tica | ¿Responderla puede dañar a alguien? |
| **R**elevante | ¿Aporta algo al conocimiento científico o a la práctica? |

Las preguntas de un mapeo categorizan ("¿cuántos estudios por año?", "¿qué sedes?", "¿qué dominios?", "¿qué tipo de contribución: framework, herramienta, método?"). Las de una SLR profundizan ("¿qué soluciones se han propuesto para X?", "¿cómo se evaluaron?", "¿qué limitaciones reportan?"). Conviene numerarlas (MQ1… para mapeo, RQ1… para SLR) y que cada columna de la ficha de extracción responda a una de ellas.

## Paso 2. Delimitar el ámbito con PICOC

PICOC (Petticrew & Roberts, 2005; Kitchenham & Charters, 2007) estructura la pregunta y, de paso, da los términos de búsqueda:

| Elemento | Pregunta | Ejemplo (Hou et al., 2024) |
| --- | --- | --- |
| **P**opulation | ¿Quién o qué? | Estudios primarios que aplican un LLM a una tarea de ingeniería del software (generación de código, reparación de programas, pruebas, detección de vulnerabilidades…) |
| **I**ntervention | ¿Qué? ¿Cómo? | Grandes modelos de lenguaje (GPT, Codex, CodeBERT, LLaMA…) y las técnicas para adaptarlos: *prompting*, ajuste fino, recuperación de contexto |
| **C**omparison | ¿Con qué se compara? | Entre arquitecturas de modelo, estrategias de datos y técnicas de optimización; no hay grupo de control |
| **O**utcomes | ¿Qué se quiere conseguir o mejorar? | Qué modelos se usan, cómo se preparan los datos, cómo se optimiza y evalúa el rendimiento y en qué tareas funcionan mejor |
| **C**ontext | ¿En qué organización y circunstancias? | Investigación académica en ingeniería del software, incluidos preprints de arXiv, de 2017 a enero de 2024 |

En informática la "población" suele ser un tipo de sistema, técnica o rol (desarrolladores, estudiantes de programación), y la comparación a menudo no existe; déjalo explícito. Para revisiones cualitativas puedes usar SPIDER (*Sample, Phenomenon of Interest, Design, Evaluation, Research type*).

## Paso 3. Escribir el protocolo

Un protocolo mínimo tiene ocho elementos: preguntas y objetivos, criterios de inclusión, criterios de exclusión, bases de datos y motores, términos de búsqueda, procedimiento de búsqueda y extracción (iterado en etapas), evaluación de la calidad y síntesis de resultados. Añade además: número de revisores y cómo resolveréis desacuerdos, la ficha de extracción, el plan de síntesis, el cronograma y la estrategia de difusión. PRISMA-P (17 ítems) sirve como lista de control; la plantilla del final de esta guía la sigue.

Pide a tu director o a un colega que revise el protocolo antes de ejecutarlo. Kitchenham & Charters lo marcan como actividad propia de la planificación ("evaluar el protocolo"), y es el momento más barato para corregir una pregunta mal planteada.

## Paso 4. Registrar o publicar el protocolo

Registrar el protocolo antes de la ejecución mejora la transparencia y permite contrastar el plan con lo realizado; no garantiza por sí solo ausencia de sesgo. PRISMA 2020 pide informar del registro y del acceso al protocolo, o indicar que no existen. Un depósito público y un registro prospectivo no son equivalentes. Opciones:

- [PROSPERO](https://www.crd.york.ac.uk/prospero/) (Universidad de York, gratuito): solo acepta revisiones con resultados relevantes para la salud humana; no sirve para la mayoría de SLR de informática o educación, y excluye scoping reviews. Relanzado en marzo de 2025 con publicación automática tras la aprobación de los autores.
- [OSF Registries](https://help.osf.io/hc/en-us/articles/360019738794-Select-a-Registration-Template) (gratuito, con DOI, cualquier disciplina): la opción más usada fuera de salud; tiene plantilla "Generalized Systematic Review" válida para SLR, scoping y meta-análisis.
- [INPLASY](https://inplasy.com/) (consulta tarifas y condiciones vigentes) y [Research Registry](https://www.researchregistry.com/) (de pago): aceptan cualquier campo.
- Depósito abierto en [Zenodo](https://zenodo.org/), Figshare o arXiv: práctica habitual en ingeniería del software, con identificador persistente y fecha, aunque sin revisión; Zenodo y Figshare permiten DOI, mientras que arXiv proporciona un identificador arXiv.

Solo el 31,5 % de los 537 estudios secundarios de ingeniería del software publicados entre 2013 y 2023 comparten sus artefactos (protocolo, búsquedas, datos), y apenas el 12 % lo hace en un repositorio permanente ([Huotala, Kuutila & Mäntylä, 2025](https://arxiv.org/html/2504.12646v2)). Hacerlo bien te diferencia.

## Equipo y tiempos

Una SLR no es un trabajo de una sola persona: PRISMA 2020 pide indicar cuántos revisores cribaron y si lo hicieron de forma independiente, y los Empirical Standards consideran deseable que haya dos analistas con una medida de acuerdo. Para un doctorando lo habitual es que el director o un compañero haga de segundo revisor, al menos sobre una muestra. En cuanto a tiempos, cuenta con 4 a 9 meses para una SLR completa en un área con varios cientos de candidatos; la fase que más se subestima es la lectura a texto completo y la extracción.

## Errores frecuentes en esta fase

```{admonition} Errores frecuentes en esta fase
:class: warning

- Empezar a buscar sin protocolo y "reconstruirlo" después.
- Preguntas tan amplias que la respuesta cabe en una revisión narrativa ("¿qué se sabe de la IA en educación?").
- No comprobar si ya existe una SLR del tema.
- Cambiar criterios de inclusión a mitad de camino sin documentarlo ni justificarlo.
- No decidir desde el principio en qué sede se publicará y qué checklist exige.
```
