from templating.__generator import PdfHtmlGenerator
from templating.utils import browser_selection
from templating.utils import defaults
import logging
from typing import Literal

logger = logging.getLogger(__name__)

class Generator(PdfHtmlGenerator):
    def __init__(
        self,
        # auto_open: bool = False,
        browser: Literal["edge", "chrome", "brave", "default"] = None,
        templates_folder: str = defaults.templates_folder,
        template_file: str = defaults.base_html,
        output_html:str = defaults.output_html,
        data: dict = None
    ) -> None:
        super().__init__(
            templates_folder=templates_folder,
            template_file=template_file,
            output_html=output_html,
            data=data
        )
        
        self.browser = browser
        try:
            self.load_standard()
            logger.info("Templates loaded")
        except Exception as e:
            logger.error(f"Error during initialization: {e}", exc_info=True)
            raise

    def auto_open(self):
        if not self.browser:
            logger.debug("browser is None, skipping browser open")
            return
        
        if not hasattr(self, 'output_file'):
            logger.warning("No output_file set, cannot open in browser")
            return
        
        try:
            browser_selection(self.output_file, self.browser)
            logger.info(f"Opened {self.output_file} in {self.browser}")
        except Exception as e:
            logger.error(f"Error opening file in browser: {e}", exc_info=True)
            raise

    def pdf(self):
        self.auto_render()
        self.auto_open()

