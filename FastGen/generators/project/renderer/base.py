from abc import ABC, abstractmethod
from typing import final

from jinja2 import Environment
from prompt_toolkit import HTML, prompt
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory


class BaseRenderer(ABC):
    def __init__(self, project, env: Environment, args: dict):
        self.env = env
        self.args = args
        self.project = project

    @final
    def toolbar(self):
        return HTML(f'You are configuring <b><style bg="ansired">{self.project}</style></b> project')

    def prompt(self, message):
        text: str = prompt(
            f'{message}: ', auto_suggest=AutoSuggestFromHistory(),
            bottom_toolbar=self.toolbar, mouse_support=True
        )
        return text

    @abstractmethod
    def render_template(self, template_name) -> bytes:
        ...

    def __call__(self, *args, **kwargs) -> bytes:
        return self.render_template(*args, **kwargs)
