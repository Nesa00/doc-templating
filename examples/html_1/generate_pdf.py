import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from datetime import datetime

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

# Output PDF path
output_pdf = os.path.join(os.path.dirname(__file__), 'output.pdf')

# Generate PDF
HTML(string=rendered_html).write_pdf(output_pdf)

print(f"PDF generated: {output_pdf}")