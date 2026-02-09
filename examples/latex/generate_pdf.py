import os
from datetime import datetime

# Read LaTeX template
with open('template.tex', 'r', encoding='utf-8') as f:
    template = f.read()

# Data to fill the template
context = {
    'name': 'World',
    'date': datetime.now().strftime('%Y-%m-%d'),
}

# Simple string replacement for placeholders
filled = template.replace('{{{ name }}}', context['name']).replace('{{{ date }}}', context['date'])

# Write filled template to .tex file
with open('output.tex', 'w', encoding='utf-8') as f:
    f.write(filled)

# Compile to PDF using pdflatex (must be installed and in PATH)
os.system('pdflatex output.tex')

print('PDF generated: output.pdf')