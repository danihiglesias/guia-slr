# Fase 2c. Extracción de datos y síntesis

La extracción debe ser homogénea: un formulario con los mismos campos para todos los estudios, definido en el protocolo y pilotado con tres o cuatro artículos antes de usarlo en serio. Cada campo debe servir para responder a una pregunta de investigación concreta; si no responde a ninguna, sobra.

## El formulario de extracción

Tiene dos bloques: datos genéricos (identificador único, referencia completa, año, sede y tipo de publicación, país o afiliación, tipo de estudio, contexto, número de participantes) y datos relativos a las preguntas (en el caso práctico de esta guía sobre simuladores hápticos en cirugía: métricas usadas, nivel de experiencia de los residentes, número de participantes). Añade siempre un campo de notas libres, la puntuación de calidad y quién extrajo los datos. Lo más práctico es una hoja de cálculo compartida (Google Sheets, Excel) con una fila por estudio y una columna por campo, o la ficha de extracción de Parsifal.

Para campos categóricos (tipo de contribución, método de evaluación, dominio) define el esquema de clasificación antes de extraer, con valores cerrados. En mapeos sistemáticos Petersen et al. (2008) proponen construir el esquema por *keywording*: leer los resúmenes de los estudios incluidos, anotar conceptos clave y agruparlos en categorías antes de clasificar. Esquemas reutilizables: tipo de investigación de Wieringa et al. (2006) (validación, evaluación, propuesta de solución, filosófico, opinión, experiencia) y tipo de contribución (método, herramienta, modelo, métrica, proceso).

Valida la extracción como el cribado: un segundo revisor extrae una muestra aleatoria y se compara, o *test-retest*. Durante la lectura completa puede descubrirse que un estudio no es relevante; se excluye y se anota el motivo (Phelps & Campbell, 2012).

## Trazabilidad

Debes poder explicar qué pasó con cada artículo en cada fase y con qué criterio se excluyó. Sin esa trazabilidad ni el revisor del artículo ni el director de la tesis pueden confiar en la revisión. La mayor parte de esa información no cabe en el artículo, así que va a un material suplementario: una hoja de cálculo con todos los candidatos y su decisión por fase, las cadenas de búsqueda, el formulario de extracción completo y la lista de control de calidad. Deposítalo en Zenodo u OSF con DOI y cítalo desde el artículo; es lo que piden PRISMA 2020 (ítem 27) y los Empirical Standards.

## Síntesis

La síntesis responde a cada pregunta a partir de los datos extraídos. Conviene seguir cuatro pasos: presentar los datos del proceso de búsqueda y selección (diagrama PRISMA), tabular los datos de los estudios incluidos, representar gráficamente los datos más característicos y esbozar la respuesta a cada pregunta.

| Método | Cuándo | Cómo |
| --- | --- | --- |
| Síntesis descriptiva y tabular | Siempre; base de cualquier mapeo | Tablas de estudios por categoría; recuentos y porcentajes; una tabla por pregunta |
| Síntesis narrativa | SLR con estudios heterogéneos | Agrupar hallazgos por tema o pregunta y describirlos con referencia a los estudios que los sustentan; explicitar contradicciones |
| Síntesis temática o codificación | Estudios cualitativos o mixtos | Codificar fragmentos, agrupar códigos en temas (Cruzes & Dybå, 2011, para ingeniería del software) |
| Meta-análisis | Estudios cuantitativos con la misma variable y diseños comparables | Tamaños del efecto combinados con modelo de efectos aleatorios; heterogeneidad (I²); gráficos de bosque. Evita el *vote counting* |
| Mapeo y visualización | Mapeos sistemáticos | Gráficos de tendencia por año, distribución por sede, *bubble plots* que cruzan dos categorías, diagramas Sankey de fuente a decisión |

## Representar los datos

Las figuras más útiles (Hou et al., 2024, usan varias de ellas sobre 395 estudios: distribución por sede y por año, evolución anual de los tipos de arquitectura de modelo, recuentos de estrategias de datos y de técnicas de *prompting*, y una tabla de tareas de ingeniería del software por actividad):

- **Gráfico de tendencia**: número de estudios por año, opcionalmente por fuente; muestra si el tema crece o decae.
- **Tabla de autores y de sedes** con su número de publicaciones y el índice h de la sede; responde a "quién" y "dónde".
- **Tabla cruzada estudio × categoría** (una X por celda) para cada pregunta; es la forma más compacta de mostrar qué estudio aporta qué.
- **Gráfico de burbujas** (Petersen et al., 2008; Kitchenham et al., 2015): dos tablas bidireccionales que comparten un eje nominal, con el tamaño de la burbuja igual al número de estudios; es la figura característica de un mapeo.
- **Diagrama Sankey** de fuentes a decisión de inclusión (SankeyMATIC) y **gráficos de anillos** por fuente y año para mostrar el proceso.
- **Diagrama de flujo PRISMA 2020** con el número de registros en cada paso.

Usa la misma paleta y el mismo orden de categorías en todas las figuras, y nunca presentes el mismo dato en tabla y gráfico a la vez.

## Errores frecuentes

```{admonition} Errores frecuentes
:class: warning

- Extraer sin formulario y "ordenar" después.
- Columnas que no responden a ninguna pregunta.
- Presentar la síntesis como una lista artículo a artículo (la "lista de la compra" de los Empirical Standards) en lugar de por tema o pregunta.
- Contar votos ("7 estudios a favor, 3 en contra") como si fuera un meta-análisis.
- Gráficos que repiten la tabla sin añadir lectura.
```
