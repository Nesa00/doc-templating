from templating.__generator import pdf_html_generator
from templating.utils import browser_selection
class Generator(pdf_html_generator):
    def __init__(self, auto_open:bool= False, browser:str = "default"):
        super().__init__()
        self.auto_open = auto_open
        self.browser = browser
        self.load_standard()
        self.render()

    def open(self):
        if self.auto_open:
            browser_selection(self.output_file, self.browser)
            
    def pdf_gen(self):
        try:
            self.pdf_write()
            self.open()
        except Exception as e:
            print(f"Error generating PDF: {e}")

    def html_gen(self):
        try:
            self.html_write()
            self.open()
        except Exception as e:
            print(f"Error generating HTML: {e}")
