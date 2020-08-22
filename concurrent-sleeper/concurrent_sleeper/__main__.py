import logging
import time

from brewtils import parameter, system, Plugin

__version__ = "3.0.0.dev0"


@system
class SleeperClient:
    def __init__(self):
        self._logger = logging.getLogger("concurrent-sleeper")

    @parameter(
        key="amount", type="Float", description="Amount of time to sleep (in seconds)"
    )
    def sleep(self, amount):
        self._logger.info("About to sleep for %d seconds" % amount)
        time.sleep(amount)
        self._logger.info("I'm Awake!")


def main():
    plugin = Plugin(
        name="concurrent-sleeper",
        version=__version__,
        description="An efficiently lazy plugin",
        max_concurrent=5,
    )
    plugin.client = SleeperClient()
    plugin.run()


if __name__ == "__main__":
    main()
