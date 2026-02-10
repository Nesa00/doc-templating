from jinja2 import Environment, FileSystemLoader
import markdown
from weasyprint import HTML, CSS
import webbrowser
import os
import json

# --- Load JSON data ---
with open("data/report_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# --- Setup template environment ---
env = Environment(loader=FileSystemLoader("templates"))

# Load template
template = env.get_template("report.md")

rendered_md = template.render(**data)

html_content = markdown.markdown(rendered_md, extensions=["extra"])

css_file = os.path.join("static", "style.css")
css = CSS(filename=css_file)

# --- Generate PDF ---
HTML(string=html_content).write_pdf("report.pdf", stylesheets=[css])

print("PDF generated: report.pdf")

