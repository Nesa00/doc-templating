import os
import webbrowser
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))
template = env.get_template('template.html')

# Data to fill the template
context = {
    'name': 'World',
    'date': datetime.now().strftime('%Y-%m-%d'),
}

# Render HTML
rendered_html = template.render(context)

# Output HTML path
output_html = os.path.join(os.path.dirname(__file__), 'output.html')

# Write the rendered HTML to file
with open(output_html, 'w', encoding='utf-8') as f:
    f.write(rendered_html)

# Open in default web browser
webbrowser.open('file://' + os.path.abspath(output_html))

print(f"HTML page generated and opened in browser: {output_html}")
