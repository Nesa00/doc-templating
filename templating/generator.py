from templating.__generator import pdf_html_generator

class Generator(pdf_html_generator):
    # def __init__(self, screen, config, callbacks):
    #     super().__init__(screen, config)
    def __init__(self,auto_open=False):
        super().__init__()
        self.auto_open = auto_open
        self.load_standard()
        self.render()
    
    def pdf_gen(self):
        self.pdf_write()
        if self.auto_open:
            self.open()

    def html_gen(self):
        self.html_write()
        if self.auto_open:
            self.open()

