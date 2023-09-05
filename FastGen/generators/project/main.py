import os
import sys

from . import get_project_data, output_dir, prj_env
from .renderer.config import ConfigRenderer
from .renderer.gitignore import GitIgnoreRenderer
from .renderer.main_py import MainRenderer
from .renderer.requirements_txt import RequirementsRenderer


class Project:
    def __init__(self, force):
        self.project = get_project_data()
        self.args = {'project': self.project}
        self.project_dir = os.path.join(output_dir, self.project)
        self.generate_project(force)

    def create_file(self, renderer: callable, template: str):
        renderer = renderer(self.project, prj_env, self.args)
        data = renderer.render_template(template)
        output_path = os.path.join(self.project_dir, template[:-3])
        with open(output_path, 'wb') as f:
            f.write(data)

    def generate_project(self, force=False):
        # Create .env file
        if not force:
            if os.path.exists(self.project_dir):
                sys.exit(
                    f'Project "{self.project}" already exists, pass flag -f or --force to override the old project'
                )

        # Generating project dir
        os.makedirs(self.project_dir, exist_ok=True)
        # Config path
        conf_path = os.path.join(self.project_dir, self.project)
        os.makedirs(conf_path, exist_ok=True)

        templates = [
            ('requirements.txt.j2', RequirementsRenderer),
            ('main.py.j2', MainRenderer),
            ('.fastgen.j2', ConfigRenderer),
            ('.gitignore.j2', GitIgnoreRenderer)
        ]

        for template, renderer in templates:
            self.create_file(renderer, template)

        print(f'Project "{self.project}" generated at {self.project_dir}')
