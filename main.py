import os
from templating import Generator

# Generator().pdf_gen()
# Generator().html_gen()

# print(os.getcwd())


# gen = Generator(auto_open=True, browser="default", templates_folder=f"{os.getcwd()}\\templates")
# gen = Generator(auto_open=True, browser="default", templates_folder=f"letter")
# gen = Generator(auto_open=True, browser="chrome",templates_folder="templates")
gen = Generator(auto_open=True, browser="chrome",templates_folder="cv-template")


# gen.pdf_gen() # bug no image 
gen.html_gen()



