import os
from datetime import datetime

# Read Markdown template
with open('template.md', 'r', encoding='utf-8') as f:
    template = f.read()

# Data to fill the template
context = {
    'name': 'World',
    'date': datetime.now().strftime('%Y-%m-%d'),
}

# Simple string replacement for placeholders
filled = template.replace('{{ name }}', context['name']).replace('{{ date }}', context['date'])

# Write filled template to .md file
with open('output.md', 'w', encoding='utf-8') as f:
    f.write(filled)

# Convert to PDF using Pandoc (must be installed and in PATH)
os.system('pandoc output.md -o output.pdf')

print('PDF generated: output.pdf')