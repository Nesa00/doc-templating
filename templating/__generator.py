from jinja2 import Environment, FileSystemLoader, Template
import markdown
# try:
#     from weasyprint import HTML, CSS
# except OSError:
#     HTML = None
#     CSS = None
#     print("pdf_write() will not work because WeasyPrint is not installed or has missing dependencies.")
import os
import json
import logging
from templating.__constants import defaults

logger = logging.getLogger(__name__)

class PdfHtmlGenerator:
    def __init__(self,
                 templates_folder:str = defaults.templates_folder, 
                 data_file:str = defaults.data_file, 
                 md_template:str = defaults.md_template, 
                 css_style:str = defaults.css_style,
                 output_pdf:str = defaults.output_pdf,
                 output_html:str = defaults.output_html):
        
        # Validate templates folder exists
        if not os.path.isdir(templates_folder):
            raise NotADirectoryError(
                f"Templates folder not found: {templates_folder}"
            )
        
        # Validate file names are non-empty strings
        for param_name, param_value in [
            ("data_file", data_file),
            ("md_template", md_template),
            ("css_style", css_style),
        ]:
            if not isinstance(param_value, str) or not param_value:
                raise ValueError(
                    f"{param_name} must be non-empty string, got: {param_value}"
                )
        self.templates_folder = templates_folder
        self.data_file = os.path.join(templates_folder,data_file)
        self.md_template = md_template
        self.css_style = os.path.join(templates_folder,css_style)
        self.output_pdf = output_pdf
        self.output_html = output_html

        logger.debug(
            f"PdfHtmlGenerator initialized with templates_folder={templates_folder}"
        )
    
    def load_standard(self):
        try:
            # Load JSON data
            with open(self.data_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
            logger.info(f"Loaded data from {self.data_file}")
        except FileNotFoundError as e:
            logger.error(f"Data file not found: {self.data_file}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {self.data_file}: {e}")
            raise
        
        # Initialize Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(self.templates_folder)
        )
        logger.debug(f"Jinja2 environment initialized with {self.templates_folder}")
        
        # Load markdown template
        try:
            self.template = self.env.get_template(self.md_template)
            logger.info(f"Loaded template {self.md_template}")
        except Exception as e:
            logger.error(f"Failed to load template {self.md_template}: {e}")
            raise

    def render(self):
        if not hasattr(self, 'template'):
            raise RuntimeError("Call load_standard() before render()")
        rendered_md = self.template.render(**self.data)
        self.html_content = markdown.markdown(rendered_md, extensions=["extra"])
    
    # def pdf_write(self):
    #     # if HTML is None:
    #     #     raise ImportError("WeasyPrint not available")
    #     # if not hasattr(self, "html_content"):
    #     #     raise RuntimeError("Call render() before writing output.")
        
    #     css = CSS(filename=self.css_style)
    #     HTML(string=self.html_content).write_pdf(self.output_pdf, stylesheets=[css])
    #     self.output_file = self.output_pdf

    def html_write(self):
        template:Template = Template(defaults.html_base)
        output_html_data = template.render(html_content=self.html_content, style_path = self.css_style)
        with open(self.output_html, "w", encoding="utf-8") as f:
            f.write(output_html_data)
        self.output_file = self.output_html
