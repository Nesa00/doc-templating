from jinja2 import Environment, FileSystemLoader, Template
import markdown
try:
    from weasyprint import HTML, CSS
    ie = False
except OSError as e:
    ie = True
    print("pdf_write() will not work because WeasyPrint is not installed or has missing dependencies.")
import os
import json
from templating.__constants import defaults

class pdf_html_generator:
    def __init__(self,
                 templates_folder:str = defaults.templates_folder, 
                 data_file:str = defaults.data_file, 
                 md_template:str = defaults.md_template, 
                 css_style:str = defaults.css_style,
                 html_file:str = defaults.html_file,
                 output_pdf:str = defaults.output_pdf,
                 output_html:str = defaults.output_html):
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
        if not ie:
            self.css = CSS(filename=self.css_style)

    def render(self):
        rendered_md = self.template.render(**self.data)
        self.html_content = markdown.markdown(rendered_md, extensions=["extra"])
    
    def pdf_write(self):
        if ie:
            raise ImportError("WeasyPrint is not installed. PDF generation is not available.")
        HTML(string=self.html_content).write_pdf(self.output_pdf, stylesheets=[self.css])
        self.output_file = self.output_pdf

    def html_write(self):
        template:Template = Template(defaults.html_base)
        output_html_data = template.render(html_content=self.html_content, style_path = self.css_style)
        with open(self.output_html, "w", encoding="utf-8") as f:
            f.write(output_html_data)
        self.output_file = self.output_html
