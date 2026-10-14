# Fase 2a. Búsqueda: fuentes, cadenas y documentación

La búsqueda debe ser replicable: otro investigador, con tu cadena, tu base de datos y tu fecha, debería obtener (casi) los mismos registros. Solo el 43 % de 311 SLR de ingeniería del software analizadas publican cadenas reutilizables y menos del 5 % reproducen sus resultados ([Li, 2021](https://arxiv.org/pdf/2103.01381)); no seas parte de esa estadística.

## Dónde buscar

No te limites a las bases más grandes; combina al menos un índice multidisciplinar (Scopus o Web of Science) con las bibliotecas digitales de tu área, y añade *snowballing*. Google Scholar sirve para la búsqueda preliminar y para el *forward snowballing*, pero no como fuente principal.

| Fuente | Cobertura | Límites de exportación y replicabilidad | Para quién |
| --- | --- | --- | --- |
| [Scopus](https://www.elsevier.support/scopus/answer/what%20content-is%20indexed-in-scopus) | Más de 83 M de registros desde 1823; 25.000 revistas activas; 10,5 M de ponencias | Hasta 20.000 registros en CSV (solo citas) o 2.000 en RIS; sintaxis estable (TITLE-ABS-KEY) | Todos; la mejor primera opción en informática y educación |
| [Web of Science](https://library-guides.ucl.ac.uk/web-of-science/exporting) | Núcleo de revistas JCR; menos actas que Scopus | 1.000 registros por exportación (rangos); truncamiento mínimo 3 caracteres; campo TS= | Todos; necesario si la sede valora JCR |
| [IEEE Xplore](https://ieeexplore.ieee.org/Xplorehelp/searching-ieee-xplore/search-results-page) | Revistas y congresos IEEE | Máximo 6 comodines; exportación limitada a unos 2.000 registros en CSV; algunos patrones dan error | Informática, ingeniería, tecnología educativa (TLT, FIE, EDUCON) |
| [ACM Digital Library](https://libraries.acm.org/training-resources/search-tools) | Texto completo ACM más la *Guide to Computing Literature* | Sin operadores de proximidad; sin exportación masiva oficial; conviene restringir a "ACM Full-Text" para evitar duplicados | Informática, HCI, educación en computación (SIGCSE, ITiCSE) |
| [SpringerLink](https://support.springernature.com/en/support/solutions/articles/6000134488-download-export-a-list-of-search-results-in-springerlink) | Revistas, libros y LNCS | CSV de hasta 1.000 resultados con cuenta; búsqueda por campo solo en título | Informática (LNCS), educación |
| ScienceDirect | Revistas Elsevier (IST, JSS, C&E) | Máximo 8 operadores booleanos por campo y 500 caracteres; sin comodines | Si Scopus no basta para texto completo |
| [ERIC](https://eric.ed.gov/?faq) | Unos 1,5 M de registros de educación desde 1966 | API y descarga; tesauro propio | Educación y tecnología educativa |
| [Google Scholar](https://aarontay.substack.com/p/why-exactly-is-google-scholar-bad-for) | Todo, incluida literatura gris | Máximo 1.000 resultados, consultas de 256 caracteres, sin API ni exportación masiva, ranking opaco y resultados no reproducibles | Solo preliminar, *snowballing* y literatura gris; Gusenbauer & Haddaway (2020) lo consideran inadecuado como fuente principal |
| [dblp](https://dagstuhl.de/dblp) | Más de 6,5 M de publicaciones de informática; datos CC0 con API | Solo metadatos, sin resúmenes | Verificar sedes y autores en informática |
| [OpenAlex](https://help.openalex.org/data/works/) / [Semantic Scholar](https://www.semanticscholar.org/about) / [Lens.org](https://researchguides.library.syr.edu/lensguide/use) | Índices abiertos de 200 a 320 M de registros con API gratuita | OpenAlex: en torno al 40 % sin resumen y 64 % sin referencias; Lens exporta 50.000 registros con cuenta gratuita | Complemento abierto y reproducible por API; útil para *snowballing* automatizado |

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
