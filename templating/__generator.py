from jinja2 import Environment, FileSystemLoader
from jinja_markdown import MarkdownExtension
import os
import logging

logger = logging.getLogger(__name__)

class PdfHtmlGenerator:
    def __init__(self,
                 templates_folder:str, 
                 template_file:str,
                 output_html:str,
                 data:dict):
        
        # Validate templates folder exists
        if not os.path.isdir(templates_folder):
            raise NotADirectoryError(
                f"Templates folder not found: {templates_folder}"
            )
        
        # # Validate file names are non-empty strings
        for param_name, param_value in [
            ("templates_folder", templates_folder),
            ("template_file", template_file),
            ("output_html", output_html)
        ]:
            if not isinstance(param_value, str) or not param_value:
                raise ValueError(
                    f"{param_name} must be non-empty string, got: {param_value}"
                )
            
        self.templates_folder = templates_folder
        self.data = data
        self.template_file = template_file
        self.output_html = output_html

        logger.debug(
            f"PdfHtmlGenerator initialized with templates_folder={templates_folder}"
        )
    
    def load_standard(self):
        self.env = Environment(
            loader=FileSystemLoader(self.templates_folder)
        )
        logger.debug(f"Jinja2 environment initialized with {self.templates_folder}")
        
        self.env.add_extension(MarkdownExtension)
        try:
            self.base_template = self.env.get_template(self.template_file)
            logger.info(f"Loaded HTML base template {self.template_file}")
        except Exception as e:
            logger.error(f"Failed to load HTML base template {self.template_file}: {e}")
            raise

    def auto_render(self):
        output_html_data = self.base_template.render(**self.data)
        with open(self.output_html, "w", encoding="utf-8") as f:
            f.write(output_html_data)
        self.output_file = self.output_html
