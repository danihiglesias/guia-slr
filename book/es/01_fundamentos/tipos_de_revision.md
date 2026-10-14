# Tipos de revisión y cuál elegir

La elección depende de dos preguntas: ¿conoces en profundidad el área? y ¿las evidencias son comparables entre sí? Si no conoces el área, haz un mapeo sistemático. Si la conoces y los estudios miden variables comparables, un meta-análisis. Si la conoces pero las evidencias son heterogéneas, una revisión sistemática.

| Tipo | Pregunta típica | Qué produce | Evaluación de calidad | Guía de referencia |
| --- | --- | --- | --- | --- |
| Revisión sistemática (SLR) | ¿Qué se sabe sobre X? ¿Qué soluciones existen y cómo funcionan? | Síntesis en profundidad de las evidencias de una pregunta concreta | Sí, obligatoria | Kitchenham & Charters (2007); PRISMA 2020; SEGRESS |
| Mapeo sistemático (SMS) | ¿Cuánto se ha publicado, quién, dónde y sobre qué subtemas? | Clasificación y recuento de la literatura; mapas, *bubble plots*, tendencias | Normalmente no, o ligera | Petersen et al. (2008, 2015); PRISMA-ScR |
| Meta-análisis | ¿Cuál es el efecto combinado de la intervención X? | Estimación estadística agregada (tamaño del efecto) | Sí, con riesgo de sesgo | Cochrane Handbook; PRISMA 2020 |
| Scoping review | ¿Qué conceptos, tipos de evidencia y lagunas hay en un campo emergente? | Mapa conceptual del área; a menudo precede a una SLR | Opcional | PRISMA-ScR (Tricco et al., 2018); JBI |
| Revisión multivocal (MLR) | ¿Qué dicen la academia **y** la práctica profesional (blogs, informes, vídeos)? | SLR que incorpora literatura gris | Sí, con criterios para fuentes grises | Garousi et al. (2019) |
| Estudio terciario / umbrella review | ¿Qué dicen las revisiones sistemáticas ya publicadas? | Síntesis de revisiones (la unidad es la SLR) | Sí, con AMSTAR 2 o ROBIS | Kitchenham et al. (2009, 2010) |
| Revisión rápida | Igual que una SLR, con menos recursos y plazo corto | Síntesis simplificada; documentar los atajos | Simplificada | Cochrane Rapid Reviews Methods Group |

## SLR frente a mapeo sistemático

La diferencia se puede resumir así: la revisión sistemática detalla el estado de la cuestión y busca resultados que respondan a preguntas abiertas; el mapeo resume a grandes rasgos e identifica el volumen de evidencias, los tipos de investigación y los resultados disponibles. En la práctica el término "revisión sistemática" se usa indistintamente para ambos, y los dos pueden publicarse en revista y servir como capítulo de una tesis o TFM.

La combinación funciona mejor que cualquiera de los dos por separado: un mapeo inicial dice dónde está la masa de la literatura y una SLR posterior profundiza en el subconjunto que responde a tu pregunta. Las preguntas de mapeo son del tipo "¿cuántos estudios se publicaron por año?", "¿quiénes son los autores más activos?", "¿en qué dominios se ha aplicado?" o, en una revisión sobre LLM en ingeniería del software, "¿qué modelos se usan y en qué tareas?" (Hou et al., 2024); las de SLR son del tipo "¿qué soluciones se han usado para X?" y "¿cómo abordan X?".

## Revisión sistemática frente a meta-análisis

Una SLR responde a una pregunta recopilando y resumiendo toda la evidencia empírica con un método explícito; un meta-análisis es el uso de métodos estadísticos para combinar los resultados de estudios similares y obtener estimaciones más precisas. Toda SLR cuantitativa es requisito previo de un meta-análisis, pero no toda SLR lo contiene (Kitchenham & Charters, 2007; Mujica-Sequera, 2022). En ingeniería e informática el meta-análisis es poco frecuente porque los estudios primarios rara vez miden las mismas variables con diseños comparables; cuando lo hagas, evita el *vote counting* (contar cuántos estudios dan positivo), práctica que los [ACM SIGSOFT Empirical Standards](https://github.com/acmsigsoft/EmpiricalStandards/blob/master/docs/standards/SystematicReviews.md) desaconsejan explícitamente.
