import yaml
from jinja2 import Environment, FileSystemLoader

with open('base.yaml', 'r') as file:
    data = yaml.safe_load(file)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

output = template.render(data)

with open('index.html', 'w') as file:
    file.write(output)

print("Template converted successfully!")
