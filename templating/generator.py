from templating.__generator import PdfHtmlGenerator
from templating.utils import browser_selection

import logging
from typing import Literal

logger = logging.getLogger(__name__)

class Generator(PdfHtmlGenerator):
    def __init__(
        self,
        auto_open: bool = False,
        browser: Literal["edge", "chrome", "brave", "default"] = "default",
        templates_folder: str = "templates"
    ) -> None:
        super().__init__(templates_folder=templates_folder)
        self.auto_open = auto_open
        self.browser = browser
        logger.debug(
            f"Generator initialized: auto_open={auto_open}, browser={browser}"
        )
        # Load templates and render
        try:
            self.load_standard()
            logger.info("Templates and data loaded")
            
            # self.render_data()
            # logger.info("Template rendered to HTML")
        except Exception as e:
            logger.error(f"Error during initialization: {e}", exc_info=True)
            raise

    def open(self):
        if not self.auto_open:
            logger.debug("auto_open is False, skipping browser open")
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
            
    # def pdf_gen(self):
    # #     try:
    # #         self.pdf_write()
    # #     except ImportError as e:
    # #         logger.error(f"Cannot generate PDF: WeasyPrint not installed", exc_info=True)
    # #         raise
    # #     except (RuntimeError, FileNotFoundError) as e:
    # #         logger.error(f"PDF generation failed: {e}", exc_info=True)
    # #         raise
    # #     except Exception as e:
    # #         logger.exception(f"Unexpected error during PDF generation")
    # #         raise
    
    # # # Only open if everything succeeded
    # #     self.open()
    #     try:
    #         self.pdf_write()
    #         self.open()
    #     except Exception as e:
    #         print(f"Error generating PDF: {e}")

    def html_gen(self):
        try:
            self.html_write()
            self.open()
        except Exception as e:
            print(f"Error generating HTML: {e}")
