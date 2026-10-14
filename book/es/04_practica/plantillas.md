# Plantillas y listas de control

Copia estas plantillas a tu propio documento o hoja de cálculo y rellénalas en orden. Están alineadas con PRISMA-P, PRISMA-S y SEGRESS, de modo que al terminar tengas casi todo lo que el checklist de reporte te pedirá.

## Plantilla de protocolo

```markdown
# Protocolo de revisión sistemática: <título>
Versión: 1.0 · Fecha: <aaaa-mm-dd> · Registro: <DOI de OSF/Zenodo>
Autores y roles: <revisor 1, revisor 2, árbitro>

## 1. Justificación
- Revisiones previas localizadas (cadena y fecha de esa búsqueda) y por qué no bastan
- A quién sirve esta revisión y cómo

## 2. Objetivos y preguntas
- Tipo de revisión: SLR / mapeo / scoping / MLR
- PICOC
- MQ1… / RQ1… (cada una con el campo de extracción que la responde)

## 3. Estrategia de búsqueda
- Fuentes (nombre, plataforma, motivo)
- Cadena genérica y adaptación por fuente
- Restricciones: campos, años, idiomas, tipos de documento (justificadas)
- Conjunto de control (lista de artículos) y umbral de recuperación
- Snowballing: hacia atrás / hacia delante, criterio de parada
- Literatura gris: fuentes y criterio de parada

## 4. Criterios de elegibilidad
- Inclusión (IC1…, unidos por AND)
- Exclusión (EC1…, unidos por OR)

## 5. Proceso de selección
- Fases (duplicados, título/resumen, texto completo)
- Revisores por fase, calibración, resolución de desacuerdos, medida de acuerdo
- Herramientas (gestor, cribado, aprendizaje activo, IA) y cómo se validan

## 6. Evaluación de la calidad / riesgo de sesgo
- Instrumento, puntuación, umbral y uso (excluir / ponderar / describir)

## 7. Extracción de datos
- Formulario (campos, valores permitidos), pilotaje, validación

## 8. Síntesis
- Método por pregunta (tabular, narrativa, temática, meta-análisis), figuras previstas

## 9. Reporte y difusión
- Checklist (PRISMA 2020 / SEGRESS), sede prevista, material suplementario

## 10. Cronograma y recursos

## 11. Registro de cambios al protocolo
| Fecha | Cambio | Motivo |
```

## Ficha de extracción (columnas de la hoja de cálculo)

| Bloque | Campos |
| --- | --- |
| Identificación | ID (S01…), cita completa, DOI, año, sede, tipo (revista, congreso, capítulo), país de la primera afiliación, fuente de la que procede |
| Diseño | Tipo de investigación (Wieringa: validación, evaluación, propuesta, filosófico, opinión, experiencia), método empírico (experimento, caso, encuesta, cuasi-experimento), contexto (académico, industrial), participantes y número |
| Contenido | Un campo por pregunta de investigación, con valores cerrados cuando sea posible; tipo de contribución (método, herramienta, modelo, métrica, proceso) |
| Calidad | Puntuación por criterio y total |
| Gestión | Revisor que extrae, fecha, notas, citas textuales relevantes con página |

## Hoja de cribado (una fila por registro)

ID, fuente, título, año, duplicado (sí/no y de cuál), decisión fase 1 revisor A, decisión fase 1 revisor B, decisión final fase 1, decisión fase 2, criterio de exclusión aplicado, origen (búsqueda / snowballing / gris). Con estas columnas el diagrama PRISMA se calcula con filtros.

## Checklist de reporte abreviado (PRISMA 2020 + SEGRESS)

- [ ] El título dice que es una revisión sistemática o un mapeo
- [ ] Resumen estructurado con fuentes, fechas, criterios, número de estudios y conclusión
- [ ] Justificación con las revisiones previas citadas
- [ ] Preguntas numeradas y PICOC
- [ ] Protocolo registrado y enlazado; desviaciones explicadas
- [ ] Todas las fuentes con cadena completa, filtros y fecha (PRISMA-S)
- [ ] Criterios de inclusión y exclusión explícitos
- [ ] Proceso de selección: fases, revisores, acuerdo, herramientas de automatización o IA
- [ ] Diagrama de flujo PRISMA 2020 con números en cada paso
- [ ] Lista de estudios excluidos a texto completo con motivo (suplemento)
- [ ] Instrumento de calidad o riesgo de sesgo y resultados por estudio
- [ ] Formulario de extracción y datos extraídos disponibles
- [ ] Síntesis por pregunta, con tablas y figuras que no se duplican
- [ ] Limitaciones o amenazas a la validez con mitigaciones
- [ ] Implicaciones para investigación y práctica
- [ ] Financiación, conflictos de interés y declaración de IA
- [ ] Materiales en repositorio con DOI

## Cronograma orientativo (SLR de doctorado, 300 a 1.500 candidatos)

| Fase | Duración típica | Entregable |
| --- | --- | --- |
| Búsqueda preliminar y comprobación de revisiones existentes | 2 semanas | Lista de revisiones previas; decisión de seguir |
| Protocolo y revisión por el director | 3 a 4 semanas | Protocolo v1.0 registrado |
| Búsqueda, exportación y deduplicación | 1 a 2 semanas | Biblioteca Zotero; tabla de búsquedas |
| Cribado título y resumen (con calibración) | 2 a 4 semanas | Hoja de cribado; kappa |
| Texto completo y snowballing | 4 a 6 semanas | Lista de incluidos y excluidos con motivo |
| Calidad y extracción | 4 a 8 semanas | Hoja de extracción validada |
| Síntesis y figuras | 3 a 4 semanas | Tablas y figuras por pregunta |
| Redacción, checklist y envío | 4 a 6 semanas | Manuscrito y material suplementario |

Total: 6 a 9 meses a tiempo parcial. Si la búsqueda tiene más de 12 meses al enviar, repite la búsqueda y actualiza el diagrama.
