import os
from jinja2 import Environment, FileSystemLoader
from FastGen.utils import BASE, HEADER

# Define paths
template_dir = os.path.join(BASE, 'templates')

# Current working directory
output_dir = os.getcwd()

# Initialize Jinja2 environment
prj_env = Environment(loader=FileSystemLoader(os.path.join(template_dir, 'project')))
app_env = Environment(loader=FileSystemLoader(os.path.join(template_dir, 'app')))


def generate_project(project_name):
    # Create project directory
    # Create .env file
    # create requirements.txt
    # create .gitignote
    # create .fastgen
    project_dir = os.path.join(output_dir, project_name)
    os.makedirs(project_dir, exist_ok=True)

    # Render and write files
    templates = ['requirements.txt.j2', 'main.py.j2']
    for _template in templates:
        template = prj_env.get_template(_template)
        rendered_content = template.render({'header': HEADER}).encode('utf-8')

        output_path = os.path.join(project_dir, _template[:-3])
        with open(output_path, 'wb') as f:
            f.write(rendered_content)

    print(f'Project "{project_name}" generated at {project_dir}')
