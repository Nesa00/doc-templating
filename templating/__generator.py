from jinja2 import Environment, FileSystemLoader, Template
import markdown
from weasyprint import HTML, CSS
from typing import Literal
import webbrowser
import os
import json
from templating.__constants import paths, html_base

class pdf_html_generator:
    def __init__(self,
                 templates_folder:str = r"templates", 
                 data_file:str = r"data.json", 
                 md_template:str = r"report.md", 
                 css_style:str = r"style.css",
                 html_file:str = r"base.html",
                 output_pdf:str = r"output.pdf",
                 output_html:str = r"output.html"):
        self.templates_folder = templates_folder
        self.data_file = os.path.join(templates_folder,data_file)
        self.md_template = md_template
        self.css_style = os.path.join(templates_folder,css_style)
        self.output_pdf = output_pdf
        self.output_html = output_html
    
    def load_standard(self):
        with open(self.data_file, "r", encoding="utf-8") as f:
            self.data = json.load(f)
        self.env = Environment(loader=FileSystemLoader(self.templates_folder))
        self.template = self.env.get_template(self.md_template)
        self.css = CSS(filename=self.css_style)

    def render(self):
        rendered_md = self.template.render(**self.data)
        self.html_content = markdown.markdown(rendered_md, extensions=["extra"])
    
    def pdf_write(self):
        HTML(string=self.html_content).write_pdf(self.output_pdf, stylesheets=[self.css])
        self.output = self.output_pdf

    def html_write(self):
        template:Template = Template(html_base)
        output_html_data = template.render(html_content=self.html_content, style_path = self.css_style)
        with open(self.output_html, "w", encoding="utf-8") as f:
            f.write(output_html_data)
        self.output = self.output_html
        
    def open(self, browser: Literal["edge", "chrome", "brave"] = "brave"):
        webbrowser.register(browser, None, webbrowser.BackgroundBrowser(paths[browser]))
        webbrowser.get(browser).open('file://' + os.path.abspath(self.output))
