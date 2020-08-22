from __future__ import absolute_import

import sys
from argparse import ArgumentParser

from brewtils import Plugin

from .client import ComplexClient

__version__ = "3.0.0.dev0"


def main():
    parser = ArgumentParser()
    parser.add_argument("instance_name")
    parser.add_argument("host")
    parser.add_argument("port")

    # Use parse_known_args to work with brewtils CLI arguments
    parsed, _ = parser.parse_known_args(sys.argv[1:])
    config = vars(parsed)

    plugin = Plugin(
        name="complex",
        version=__version__,
        description="Plugin that shows all the cool things Beergarden can do",
        max_instances=2,
        instance_name=config["instance_name"],
    )
    plugin.client = ComplexClient(config["host"], config["port"])
    plugin.run()


if __name__ == "__main__":
    main()
