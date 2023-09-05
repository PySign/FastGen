from FastGen.utils import HEADER
from .base import BaseRenderer


class GitIgnoreRenderer(BaseRenderer):
    def render_template(self, template_name) -> bytes:
        template = self.env.get_template(template_name)
        rendered_content = template.render({'header': HEADER, **self.args})
        final = rendered_content.encode()
        return final
