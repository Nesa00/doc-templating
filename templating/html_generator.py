from jinja2 import Environment, FileSystemLoader
import markdown
import webbrowser
import os
import json

with open("data/report_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

env = Environment(loader=FileSystemLoader("templates"))

template = env.get_template("report.md")

rendered_md = template.render(**data)

html_content = markdown.markdown(rendered_md, extensions=["extra"])

html_file_path = "report.html"

html_template = env.get_template("base.html")
html_template_final = html_template.render(html_content=html_content)


with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(html_template_final)

print(f"HTML generated: {html_file_path}")
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe" 
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
# webbrowser.get('chrome').open('file://' + os.path.abspath(html_file_path))

webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
webbrowser.get('brave').open('file://' + os.path.abspath(html_file_path))

# webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
# webbrowser.get('edge').open('file://' + os.path.abspath(html_file_path))
