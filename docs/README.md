# doc-templating

A Python-based document generation tool that converts HTML and Markdown templates into formatted PDFs with CSS styling and structure support.

## Features

- **Multi-format support**: Convert HTML and Markdown documents to PDF
- **Template rendering**: Use Jinja2 templating for dynamic content
- **CSS styling**: Apply custom styling to your generated documents
- **Flexible structure**: Mix HTML and Markdown for document composition
- **Easy integration**: Simple Python API for document generation

## Requirements

This tool requires external dependencies depending on which conversion method you use:

- **Python 3.7+**
- **Pandoc** (for Markdown to PDF conversion) - [Installation guide](https://pandoc.org/installing.html)
- **LaTeX/pdflatex** (for advanced PDF generation) - [MiKTeX](https://miktex.org/download) or [TeX Live](https://www.tug.org/texlive/acquire-netinstall.html)
- **WeasyPrint** (for HTML to PDF) - May require GTK libraries on Windows - [Installation guide](docs/html-error.md)

## Installation

...
