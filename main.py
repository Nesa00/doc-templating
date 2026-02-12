from templating import Generator

# Generator().pdf_gen()
# Generator().html_gen()

# print(os.getcwd())


# gen = Generator(auto_open=True, browser="brave", templates_folder=f"{os.getcwd()}\\templates")
gen = Generator(auto_open=True, browser="brave",templates_folder="test")


# gen.pdf_gen() # bug no image 
gen.html_gen()



