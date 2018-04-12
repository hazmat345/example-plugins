from __future__ import absolute_import

import sys

from brewtils import load_config
from brewtils.plugin import RemotePlugin
from .client import EchoClient

__version__ = '1.0.0.dev0'


def main():
    plugin = RemotePlugin(EchoClient(), name='echo', version=__version__,
                          **load_config())
    plugin.run()


if __name__ == '__main__':
    main()