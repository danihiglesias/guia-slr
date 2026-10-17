# Caso práctico guiado

El caso que sigue es una SLR de un solo autor sobre métricas para evaluar el desempeño de residentes de cirugía con simuladores hápticos. Es pequeño (menos de 50 candidatos) y por eso ilustra bien las decisiones y las validaciones que hay que planificar cuando no hay equipo.

## 1. Pregunta y PICOC

Pregunta: *En el campo de la cirugía, ¿qué métricas existen para evaluar de forma objetiva el desempeño de un residente utilizando simuladores hápticos?*

| Criterio | Valor | Palabras clave |
| --- | --- | --- |
| Población / Problema | Evaluación objetiva del desempeño; residente | "objective assessment"; performance; resident |
| Intervención | Simulador háptico | "haptic simulator" |
| Comparación | Ninguna | — |
| Resultado | Métricas | metric |
| Contexto | Cirugía | surgery |

## 2. Conjunto de semi-referencia

Antes de buscar, identifica a mano (o preguntando a un experto) un pequeño conjunto de artículos que responden directamente a la pregunta (Zhang, Babar & Tell, 2011, lo llaman *quasi-gold standard*). Servirá para extraer palabras clave de sus títulos y resúmenes y para validar la cadena: un criterio razonable es que la búsqueda automática recupere todos los artículos conocidos pertinentes indexados en cada fuente (el 70 % del ejemplo histórico no es un umbral general) ; analiza cada ausencia y revisa la cadena cuando corresponda.

## 3. Fuentes y restricciones

Cinco o seis fuentes que combinen generales y específicas: Web of Science, Scopus, ScienceDirect, IEEE Xplore y ACM DL (las dos últimas, específicas de informática). Restricciones declaradas: búsqueda en título, resumen y palabras clave; solo inglés; solo artículos de revista o congreso. La limitación reconocida (solo fuentes accesibles desde la Universidad de León) se compensa con búsqueda complementaria y literatura gris.

## 4. Cadena de búsqueda, iterada

```
Cadena base (WoS, 1 resultado):
("objective assessment" AND performance AND resident) AND "haptic simulator" AND metric AND surgery

Cadena ampliada (WoS, 17 resultados):
("objective assessment" AND performance AND resident*) AND ("haptic simulat*" OR "virtual reality") AND metric* AND surg*
```

La primera versión devolvía un solo artículo; truncar (*resident\**, *metric\**, *surg\**) y añadir un sinónimo de la intervención la amplió a 17. Al ampliar entran falsos positivos; al reducir se pierden falsos negativos: el conjunto de semi-referencia es lo que te dice cuándo parar.

## 5. Criterios de selección y fases

Inclusión: en inglés; artículo de revista o congreso; define métricas de evaluación; las métricas evalúan el desempeño de un residente o estudiante de últimos cursos con un simulador háptico o virtual. Exclusión: otro tipo de simulador (realidad aumentada, modelos físicos); métricas sobre otros aspectos (realismo, factor humano, distinción novato/experto).

Con un solo revisor y pocos candidatos se planifican dos fases: (1) eliminar duplicados y revisar título y resumen, excluyendo si se cumple al menos un criterio de exclusión y pasando a la siguiente fase en caso de duda; (2) descargar y revisar el texto completo con los mismos criterios. Validación por *test-retest* sobre una muestra aleatoria; si los resultados difieren, se revisan los criterios.

## 6. Calidad, extracción y síntesis

Lista de control de Dybå & Dingsøyr (2008) con puntuación Sí = 1, Parcialmente = 0,5, No = 0, más dos preguntas específicas (¿se definen las métricas de forma clara? ¿la población son solo estudiantes o residentes?). Extracción en hoja de cálculo con identificador, referencia, métricas (tipo y descripción), nivel de experiencia del residente (ninguna, estudiante de últimos cursos, residente) y número de participantes. Síntesis con tabla de artículos relevantes, gráfico de tendencia por año y gráfico de burbujas que cruza nivel de experiencia y experiencia previa con simuladores (ejes X) contra tipo de métrica (eje Y).

## Cómo lo harías hoy, con lo que añade esta guía

- Registrar el protocolo en OSF antes de lanzar la búsqueda y citar su DOI.
- Documentar la búsqueda con los 16 ítems de PRISMA-S y añadir *snowballing* hacia atrás y hacia delante desde los incluidos.
- Planificar evaluación humana independiente, justificar el muestreo e informar discrepancias antes del consenso.
- Si un LLM propone decisiones, validarlo con un conjunto independiente y declararlo como automatización.
- Generar el diagrama con la app PRISMA 2020 y rellenar el checklist SEGRESS antes de enviar.
- Depositar hoja de cribado, extracción y cadenas en Zenodo.

## Los errores que más vemos en doctorandos

```{admonition} Los errores que más vemos en doctorandos
:class: warning

1. Empezar por la cadena de búsqueda en lugar de por la pregunta.
2. Elegir un tema para el que ya existe una SLR reciente y no citarla ni justificar la nueva.
3. Usar solo Google Scholar o solo una base.
4. No guardar las exportaciones originales ni la fecha de búsqueda y no poder reconstruir el diagrama PRISMA.
5. Cribar solo, sin ninguna validación, y no mencionarlo como limitación.
6. Confundir mapeo con SLR y que el título prometa lo que el método no entrega.
7. Sintetizar artículo a artículo en lugar de por pregunta.
8. Enviar a una revista que ya no acepta revisiones o cuyo formato no admite la extensión necesaria.
9. Usar IA para cribar o extraer sin validarla ni declararla.
10. Tardar tanto que la búsqueda queda desactualizada; evalúa la actualización según la velocidad del campo y la fecha de envío.
```

## Ejercicio completo reproducible: datos ficticios

Este ejercicio complementa el caso histórico. **Registros, estudios S01–S06, participantes, fragmentos, páginas y juicios son inventados para docencia. No representan resultados científicos ni reconstruyen la revisión original.**

**Protocolo:** RQ1 pregunta qué métricas se registran por población. Se incluyen residentes o estudiantes de últimos cursos, simulador háptico/virtual y al menos una métrica de desempeño. EC1: población distinta; EC2: sin métrica. Los revisores ficticios A/B aplican los mismos criterios; su acuerdo no estima el esperable en una revisión real. Los tres dominios de evaluación son ilustrativos, sin puntuación total. No se usa IA.

**Selección:** Scopus aporta 24 registros e IEEE Xplore 16. Se eliminan ocho duplicados, se criban 32 y se excluyen 22. Se buscan diez publicaciones: una no se recupera y nueve se evalúan. Se excluyen dos por EC1 y dos por EC2. Se incluyen cinco publicaciones de bases y una adicional por citas: seis publicaciones y seis estudios. La rama por citas contiene una publicación buscada, recuperada y elegible. R28 no se recupera: en una revisión real deben registrarse intentos de acceso/contacto; no se etiqueta como exclusión por contenido.

| Estudio | Población | Participantes | Métricas (página ficticia 2) |
| --- | --- | --- | --- |
| S01 | Residente | 24 | Tiempo; errores |
| S02 | Residente | 18 | Tiempo |
| S03 | Estudiante | 30 | Errores; fuerza |
| S04 | Estudiante | 16 | Tiempo; fuerza |
| S05 | Residente | 22 | Errores |
| S06 | Estudiante | 20 | Tiempo; errores; fuerza |

**Respuesta a RQ1:** tiempo y errores aparecen en cuatro estudios cada uno; fuerza, en tres. Los tres estudios de estudiantes registran fuerza; dos registran tiempo y dos errores. Entre residentes, dos registran tiempo y dos errores. Son frecuencias de registro, no comparaciones de eficacia. Una ejecución rápida puede incluir errores: no se demuestra superioridad de una métrica ni se suman participantes como una muestra común.

**Evaluación e interpretación:** S02 no informa sobre datos ausentes; S04 no informa sobre validez de la medida; S05 describe insuficientemente el contexto. Las demás celdas documentan el criterio. «No informado» exige cautela, no demuestra métodos incorrectos. Conserva estas limitaciones al agrupar tiempo como eficiencia temporal y errores/fuerza como seguridad de ejecución.

**Descargas:** {download}`Cribado completo <../../_static/downloads/es/screening_example.csv>` · {download}`Extracción <../../_static/downloads/es/extraction_example.csv>` · {download}`Diccionario <../../_static/downloads/es/codebook.csv>` · {download}`Recuentos <../../_static/downloads/es/flow_counts.json>` · {download}`Paquete completo <../../_static/downloads/es/teaching_materials.zip>`.

**Reproducción:** instala `requirements-figures.txt` en `.venv` y ejecuta `scripts/generate_teaching_assets.py` desde la raíz del repositorio. Comprueba recuentos y crea gráficos desde la extracción descargable. Después ejecuta `scripts/render_diagrams.py` para las fuentes Graphviz. Las columnas e identificadores conservan nombres en inglés por estabilidad; valores y figuras están traducidos.

**Comprueba tu comprensión:** ¿por qué 11 apariciones de métricas no significan 11 estudios? ¿Por qué R28 no se suma a las cuatro exclusiones? Hay clasificación múltiple y R28 nunca pudo evaluarse.
