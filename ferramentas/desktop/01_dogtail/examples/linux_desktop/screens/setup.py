from dogtail.tree import root

from dogtail.procedural import run, focus, click
from dogtail.utils import screenshot
from guara.transaction import AbstractTransaction


class OpenApp(AbstractTransaction):
    """
    Opens the App

    Returns:
        The calculator application
    """

    def __init__(self, driver):
        super().__init__(driver)

    def do(self):
        return self._driver


class CloseApp(AbstractTransaction):
    """
    Closes the App
    """

    def __init__(self, driver):
        super().__init__(driver)

    def do(self):
        screenshot()
        click("Close")
