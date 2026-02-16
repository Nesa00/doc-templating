import os
from templating import Generator
from templating.utils import load_data

# Generator().pdf_gen()
# Generator().html_gen()

# print(os.getcwd())

data = load_data("templates/data.json", "templates/paths.json")
print(data)


# gen = Generator(auto_open=True, browser="default", templates_folder=f"{os.getcwd()}\\templates")
# gen = Generator(auto_open=True, browser="default", templates_folder=f"letter")
gen = Generator(auto_open=True, browser="chrome",templates_folder="templates", data=data)
# gen = Generator(auto_open=True, browser="chrome",templates_folder="cv-template")
# gen = Generator(auto_open=True, browser="chrome",templates_folder="cv-template")


# gen.pdf_gen() # bug no image 
# gen.html_gen()
gen.pdf()

# from jinja2 import Environment, FileSystemLoader
# from jinja_markdown import MarkdownExtension

# # 1. Setup Environment to find your parent files (like base.html)
# env = Environment(loader=FileSystemLoader('templates'))
# env.add_extension(MarkdownExtension)

# # 2. Your template stored in a variable
# # This "virtual" file extends a "physical" file
# # core_template_string = """
# # {% extends "base.html" %}

# # {% block content %}
# #     {% markdown %}
# #     # Hello {{ name }}!
# #     This page was rendered from a **static string variable**.
    
# #     * Process: String -> Markdown -> HTML
# #     * Status: Success
# #     {% endmarkdown %}
# # {% endblock %}
# # """
# core_template_string = """
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>Document</title>
#     <link rel="stylesheet" href="templates/style.css">
# </head>
# <body>
# {% markdown %}
# # Report for Alice
# **Date:** 2026-02-09
# ### Summary
# All systems operational. No major issues found.
# ## Details
# - Checked system logs
# - Reviewed performance metrics
# - Validated backups
# ---
# ## Image
# ![Report Image](templates/img.png)
# {% endmarkdown %}
# *Generated automatically.*
#      <script>
#         print()
#     </script>
# </body>
# </html>
# """

# # 3. Render the string
# template = env.from_string(core_template_string)
# output = template.render(name="Developer")

# print(output)
