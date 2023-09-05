import os
import sys

from jinja2 import Environment, FileSystemLoader
from prompt_toolkit.shortcuts import input_dialog

from FastGen.utils import BASE


def get_project_data():
    project = input_dialog(
        title='Configure project',
        text='Enter project name:',
        cancel_text='Abort', ok_text='Create',
    ).run()

    if not project:
        sys.exit('Project not created')
    return project


# Define paths
template_dir = os.path.join(BASE, 'templates')
# Current working directory
output_dir = os.getcwd()
# Initialize Jinja2 environment
prj_env = Environment(loader=FileSystemLoader(os.path.join(template_dir, 'project')))
