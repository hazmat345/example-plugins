from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from brewtils import command, system, Plugin, parameter
from brewtils.models import Parameter
from .__version__ import __version__


class Nav:
    href = Parameter(key="href", type="String", optional=False)
    caption = Parameter(key="caption", type="String", optional=False)

    parameters = [href, caption]


@system
class Client:

    def __init__(self):
        self._env = Environment(
            loader=FileSystemLoader('jinja/resources'), autoescape=True
        )

    @parameter(key="nav", model=Nav, multi=True)
    @parameter(key="a_variable", type="String")
    @command(output_type="HTML")
    def do_jinja(self, a_variable=None, nav=None):
        template = self._env.get_template('test_template.j2')

        return template.render(navigation=nav, a_variable=a_variable)

    @parameter(key="nav", model=Nav, multi=True)
    @parameter(key="a_variable", type="String")
    @command(output_type="HTML", output_template="test_template.j2")
    def better_jinja(self, a_variable=None, nav=None):
        return {"navigation": nav, "a_variable": a_variable}


def main():
    plugin = Plugin(
        name="jinja",
        version=__version__,
        description="",
        template_loader=FileSystemLoader("jinja/resources"),
    )
    plugin.client = Client()
    plugin.run()


if __name__ == "__main__":
    main()
