import yaml
from jinja2 import Environment, FileSystemLoader

# Load data from YAML file
with open('content.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')  # Assuming your template is named 'template.html'

# Render the template with data from YAML
output = template.render(data)

# Write the rendered HTML to a file
with open('output.html', 'w') as file:
    file.write(output)

print("Template converted successfully!")
