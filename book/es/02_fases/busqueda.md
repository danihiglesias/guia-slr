# Fase 2a. Búsqueda: fuentes, cadenas y documentación

La búsqueda debe ser replicable: otro investigador, con tu cadena, tu base de datos y tu fecha, debería obtener (casi) los mismos registros. Solo el 43 % de 311 SLR de ingeniería del software analizadas publican cadenas reutilizables y menos del 5 % reproducen sus resultados ([Li, 2021](https://arxiv.org/pdf/2103.01381)); no seas parte de esa estadística.


```{figure} ../../_static/generated/diagrams/es/search_design_es.svg
:name: fig-search_design-es
:alt: Construcción y comprobación de búsqueda. Expresiones conceptuales: adapta sintaxis, campos y truncamiento a cada plataforma. Elaboración propia, CC BY 4.0.
:width: 100%
:align: center

Construcción y comprobación de búsqueda. Expresiones conceptuales: adapta sintaxis, campos y truncamiento a cada plataforma. Elaboración propia, CC BY 4.0.
```


## Dónde buscar

Elige fuentes por cobertura temática, tipos de estudio y acceso, y justifica la combinación. Consulta una persona experta en búsquedas si es posible. No existe un número universal de bases suficiente. Índices y plataformas se solapan; conserva la procedencia antes de deduplicar {cite:p}`rethlefsen2021`.

| Fuente | Cobertura y uso |
| --- | --- |
| [Scopus](https://www.elsevier.com/products/scopus) | Índice multidisciplinar; revistas y congresos |
| [Web of Science](https://webofscience.zendesk.com/) | Declara las colecciones consultadas |
| [IEEE Xplore](https://ieeexplore.ieee.org/Xplorehelp/) | Ingeniería e informática |
| [ACM Digital Library](https://libraries.acm.org/training-resources/search-tools) | Distingue colección a texto completo e índice bibliográfico |
| [SpringerLink / ScienceDirect](https://link.springer.com/) | Plataformas editoriales; justifica cobertura adicional |
| [ERIC](https://eric.ed.gov/?faq) | Educación; texto libre y tesauro |
| [Google Scholar](https://scholar.google.com/intl/en/scholar/help.html) | Complemento; documenta límites y ordenación |
| [dblp](https://dblp.org/faq/) | Metadatos de informática; sin resúmenes |
| [OpenAlex / Semantic Scholar](https://docs.openalex.org/) | Comprueba cobertura, campos y condiciones de API |

Los límites de exportación, campos y sintaxis cambian. Consulta la documentación oficial al buscar y anota fecha, formato, lotes y total exportado. Recuperar texto completo es distinto de identificar registros.

## Construir la cadena de búsqueda

1. **Deriva los conceptos de PICOC**: normalmente población, intervención y resultado; el contexto rara vez entra en la cadena.
2. **Amplía cada concepto con sinónimos**: términos derivados, variantes ortográficas (*modelling*/*modeling*), acrónimos (HCI), términos en otros idiomas si procede, y descriptores del tesauro de la base (MeSH en MEDLINE, tesauro ERIC, IEEE Thesaurus, ACM CCS).
3. **Une sinónimos con OR y conceptos con AND**; evita NOT salvo para excluir un dominio claramente ajeno, porque elimina registros relevantes que mencionen el término de pasada.
4. **Usa paréntesis** para fijar la precedencia y comillas para frases exactas; el truncamiento (\*) amplía (*analy\** cubre *analysis*, *analyse*, *analytics*).
5. **Prueba la cadena contra un conjunto de control**: 5 a 10 artículos que sabes que deben aparecer. Si falta alguno, revisa los términos.
6. **Adapta la sintaxis a cada base** y guarda la versión exacta.

Ejemplo de Hou et al. (2024), una revisión sistemática sobre el uso de grandes modelos de lenguaje (LLM) en tareas de ingeniería del software, publicada en *ACM Transactions on Software Engineering and Methodology* con todos sus materiales en abierto. La cadena combina dos conceptos, cada uno con una lista larga de sinónimos unida por OR:

```
Concepto 1 (tareas de ingeniería del software):
  "Software Engineering" OR "Software Development" OR Program* OR "Code Generation"
  OR "Code Completion" OR "Code Summarization" OR "Bug Detection" OR "Program Repair"
  OR "Test Generation" OR "Vulnerability Detection" OR ...

Concepto 2 (modelos de lenguaje):
  LLM OR "Large Language Model*" OR "Language Model*" OR LM OR PLM OR Pretrained
  OR "Pre-trained" OR GPT OR ChatGPT OR Codex OR BERT OR CodeBERT OR T5 OR LLaMA OR ...

Cadena final:  (Concepto 1) AND (Concepto 2)
```

La búsqueda se lanzó en siete fuentes (IEEE Xplore, ACM Digital Library, ScienceDirect, Web of Science, SpringerLink, arXiv y dblp), limitada a enero de 2017–enero de 2024, y devolvió más de 218.000 registros, que las fases de cribado redujeron a 395 estudios incluidos. Tres prácticas de esa revisión merecen copiarse: antes de la búsqueda automática hicieron una búsqueda manual en seis sedes de referencia (ICSE, FSE, ASE, ISSTA, TOSEM y TSE) y construyeron con ella un conjunto de control de 51 artículos (*quasi-gold standard*) para validar la cadena; incluyeron arXiv y dblp como fuentes complementarias a las bibliotecas tradicionales; y publicaron las cadenas adaptadas a cada base, las listas de artículos y las decisiones de cribado en un repositorio público, de modo que cualquiera puede replicar la búsqueda.

Las cadenas de cada base deben ser iguales o equivalentes; si no, los resultados no son comparables. El ejemplo de Ferreras-Fernández et al. (2016) muestra una buena práctica adicional: registrar en una tabla cada consulta numerada (#1, #2…), el campo (título, tema), los filtros (años, idiomas) y el número de resultados, y combinarlas al final (#1 OR #2 OR #3 OR #4).

## Snowballing

Las guías de [Wohlin (2014)](https://conf.researchr.org/details/ease-2024/ease-2024-most-influential-paper-award/1/Guidelines-for-snowballing-in-systematic-literature-studies-and-a-replication-in-soft) proponen partir de un conjunto inicial heterogéneo (distintos autores, años y sedes) y revisar las listas de referencias (*backward*) y las citas recibidas (*forward*, con Google Scholar o Scopus) hasta que una iteración no aporte artículos nuevos. Wohlin et al. (2022) muestran que la estrategia híbrida Scopus + *snowballing* encuentra en torno a un 30 % más de artículos relevantes que la búsqueda en bases de datos sola. En el diagrama PRISMA estos artículos van en el brazo "otros métodos".

## Literatura gris

En temas donde la práctica profesional va por delante de la academia (DevOps, LLM en programación, herramientas educativas comerciales), una revisión multivocal añade blogs técnicos, informes y documentación. Garousi et al. (2019) dan criterios para decidir si incluirla y cómo evaluar su calidad (autoría, fecha, metodología, citas). Documenta las búsquedas en Google con fecha, número de páginas revisadas y criterio de parada.

## Qué documentar (PRISMA-S)

Para cada fuente: nombre y plataforma (Scopus vía Elsevier), cadena completa tal como se ejecutó, campos, filtros y límites (años, idioma, tipo de documento), fecha de ejecución, número de registros devueltos y método de deduplicación con el número de duplicados eliminados. Si actualizas la búsqueda antes de enviar el artículo, documenta ambas ejecuciones. Guárdalo todo en el material suplementario (Zenodo u OSF).

## Errores frecuentes

```{admonition} Errores frecuentes
:class: warning

- Una cadena distinta por base sin tabla de equivalencias.
- Reportar "se buscó en Google Scholar" sin fecha, sin número de resultados revisados ni criterio de parada.
- No guardar la exportación original (RIS/BibTeX) de cada base.
- Olvidar las actas de congresos en áreas donde son la sede principal (ingeniería del software, HCI).
- Limitar por fecha o idioma sin justificarlo en el protocolo.
```

## Validación y registro operativo

No todos los componentes de PICOC tienen que convertirse en bloques AND. Añadir resultados o métricas poco descritos en resúmenes puede perder estudios relevantes. Prueba variantes, inspecciona qué añade o elimina cada bloque y conserva el historial. La figura usa dos bloques conceptuales; no es una consulta lista para todas las plataformas.

En cada base, el denominador del control es el número de artículos conocidos que están indexados y cumplen los límites allí. Recuperarlos todos no demuestra exhaustividad. Registra por qué falta cada uno y evita ajustar solo a sus palabras. Publica la consulta íntegra sin «…»: la cadena abreviada de Hou es ilustrativa, no reproducible.

```{figure} ../../_static/generated/diagrams/es/snowballing_es.svg
:name: fig-snowballing-es
:alt: Búsqueda por citas e iteraciones. Las flechas son pasos de descubrimiento, no la dirección de las citas. Ejemplo conceptual independiente del dataset. Elaboración propia, CC BY 4.0.
:width: 100%
:align: center

Búsqueda por citas e iteraciones. Las flechas son pasos de descubrimiento, no la dirección de las citas. Ejemplo conceptual independiente del dataset. Elaboración propia, CC BY 4.0.
```
