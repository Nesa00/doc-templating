from jinja2 import Environment, FileSystemLoader
import markdown
# from weasyprint import HTML, CSS
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

# --- Render Markdown with Jinja2 ---
rendered_md = template.render(**data)

# --- Convert Markdown → HTML ---
html_content = markdown.markdown(rendered_md, extensions=["extra"])



html_file_path = "report.html"
with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(f"""
<html>
<head>
<link rel="stylesheet" href="static/style.css">
</head>
<body>
{html_content}
<script>
print()
</script>
</body>
</html>
""")

print(f"HTML generated: {html_file_path}")
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe" 
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open('file://' + os.path.abspath(html_file_path))


# css_file = os.path.join("static", "style.css")
# css = CSS(filename=css_file)

# # --- Generate PDF ---
# HTML(string=html_content).write_pdf("report.pdf", stylesheets=[css])

# print("PDF generated: report.pdf")
