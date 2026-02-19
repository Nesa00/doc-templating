[![Run Tests (Windows)](https://github.com/Nesa00/doc-templating/actions/workflows/tests.yml/badge.svg)](https://github.com/Nesa00/doc-templating/actions/workflows/tests.yml)

[![jinja2](https://img.shields.io/badge/jinja2-latest-green)](https://jinja.palletsprojects.com/)
[![jinja-markdown](https://img.shields.io/badge/jinja--markdown-latest-green)](https://github.com/jpsca/jinja_markdown)
[![WeasyPrint](https://img.shields.io/badge/WeasyPrint-latest-green)](https://weasyprint.org/)

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
- **WeasyPrint** (for HTML to PDF) - May require GTK libraries on Windows - [Installation guide](docs/html-error.md)

## Installation

...
