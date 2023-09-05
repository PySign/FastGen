import getpass
import json

from FastGen.utils import HEADER
from .base import BaseRenderer


class ConfigRenderer(BaseRenderer):
    def get_input(self, key, message, default=None):
        if key not in self.args:
            value = self.prompt(message)
            if default and not value:
                value = default
            self.args[key] = value
            return value
        return self.args.get(key)

    def render_template(self, template_name) -> bytes:
        self.get_input('author', f'Enter author name [str/{getpass.getuser()}(default)]', getpass.getuser())
        self.get_input('version', 'Enter version code [str/V1(default)]', 'V1')

        template = self.env.get_template(template_name)
        rendered_content = template.render({'header': HEADER, **self.args})
        json_data = json.loads(rendered_content)
        final = json.dumps(json_data, indent=2).encode()
        return final
