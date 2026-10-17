# Guía para elaborar una revisión sistemática de la literatura (SLR) 📚

Libro electrónico con una guía práctica, paso a paso, para planificar, ejecutar y publicar una **revisión sistemática de la literatura (SLR)** o un **mapeo sistemático** en ingeniería e informática. Pensado para doctorandos e investigadores que abordan su primera revisión.

Cubre los estándares vigentes (PRISMA 2020, SEGRESS, Kitchenham, Petersen), las fases de la revisión, un panorama de herramientas y una sección sobre el uso responsable de la IA generativa.

## Contenido

1. **Fundamentos**: qué es una SLR, tipos de revisión, estándares y guías.
2. **Fases**: planificación y protocolo, búsqueda, selección y calidad, extracción y síntesis, redacción y publicación.
3. **Herramientas e IA**: herramientas por fase; IA generativa, evidencia y cómo declararla.
4. **Práctica**: caso práctico guiado y plantillas (protocolo, ficha de extracción, hoja de cribado, checklist, cronograma).
5. **Referencias**.

## Cómo compilar el libro en local

Requisitos: Python 3.12 (y Git). El resto lo instala el script.

```bash
python scripts/setup_env.py --yes      # crea .venv e instala dependencias
python scripts/build_book.py           # genera HTML en book/_build/html/
python scripts/launch_preview.py       # vista previa en http://localhost:8000
```

Para exportar el PDF:

```bash
python scripts/setup_env.py --yes --extras pdf
python scripts/setup_latex.py --yes
python scripts/export_pdf.py --engine auto
```

## Publicación

Cada `push` a `main` lanza el workflow `deploy-book` (GitHub Actions), que genera el PDF, compila el HTML y lo publica en GitHub Pages. En el repositorio debe estar configurado **Settings → Pages → Source: GitHub Actions**.

## Plantilla y licencia

Construido con la [plantilla TeachBook USAL](https://github.com/elloza/teachbook_usal_template) de Álvaro Lozano Murciego y André Filipe Sales Mendes (Jupyter Book / TeachBooks). Contenido bajo licencia [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Figuras y materiales docentes reproducibles

Las 11 figuras por idioma tienen fuentes editables en `diagram_sources/es/` y `diagram_sources/en/`, con imágenes estáticas en `book/_static/generated/diagrams/`. Los datos del ejercicio son ficticios y se identifican como tales.

Con Python 3.12 del entorno `.venv`, instala opcionalmente `requirements-figures.txt` y ejecuta `scripts/generate_teaching_assets.py` para regenerar los datos y los gráficos. Después ejecuta `scripts/render_diagrams.py` para renderizar las fuentes Graphviz. Las imágenes ya están incluidas: compilar o leer el libro no requiere conexión con Kroki.

Las plantillas y ejemplos descargables están en `book/_static/downloads/es/` y `book/_static/downloads/en/`. Los identificadores y nombres de columnas son estables en inglés; los valores de extracción y las figuras están traducidos. Las figuras originales y los datos docentes siguen la licencia CC BY 4.0; el flujo PRISMA está identificado como adaptación.
