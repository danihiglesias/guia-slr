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

Antes de buscar, identifica a mano (o preguntando a un experto) un pequeño conjunto de artículos que responden directamente a la pregunta (Zhang, Babar & Tell, 2011, lo llaman *quasi-gold standard*). Servirá para extraer palabras clave de sus títulos y resúmenes y para validar la cadena: un criterio razonable es que la búsqueda automática recupere **al menos el 70 %** de esos artículos; si no, se revisa la cadena.

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
- Conseguir un segundo revisor para una muestra del 20 % y reportar la kappa, además del *test-retest*.
- Si se usa un LLM como segundo revisor, validarlo en esa misma muestra y declararlo.
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
10. Tardar tanto que la búsqueda queda desactualizada; si pasan más de 12 meses, repite la búsqueda antes de enviar.
```
