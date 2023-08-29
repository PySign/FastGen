import os
from jinja2 import Environment, FileSystemLoader

# Define paths
template_dir = os.path.join(os.getcwd(), 'project_templates')
output_dir = os.getcwd()  # Current working directory

# Initialize Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))


def generate_project(project_name):
    # Create project directory
    project_dir = os.path.join(output_dir, project_name)
    os.makedirs(project_dir, exist_ok=True)

    # Render and write files
    templates = ['requirements.txt.j2', 'main.py.j2']
    for template in templates:
        template_path = os.path.join('basic_project', template)
        template = env.get_template(template_path)
        rendered_content = template.render()

        output_path = os.path.join(project_dir, template[:-3])
        with open(output_path, 'w') as f:
            f.write(rendered_content)

    print(f'Project "{project_name}" generated at {project_dir}')
