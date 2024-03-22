import yaml
from jinja2 import Environment, FileSystemLoader

with open('content.yaml', 'r') as file:
    data = yaml.safe_load(file)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('cv_template.html') 

output = template.render(data)

with open('cv.html', 'w') as file:
    file.write(output)

print("Template converted successfully!")
