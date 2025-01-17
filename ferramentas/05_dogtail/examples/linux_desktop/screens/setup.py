import dogtail.tc
import sys
import io
import re
import pytest
from dogtail.procedural import run, focus, click
from dogtail.rawinput import pressKey, keyNameAliases
from dogtail import tree
from dogtail.utils import screenshot
from guara.transaction import AbstractTransaction


class OpenApp(AbstractTransaction):
    """
    Opens the App
    """

    def __init__(self, driver):
        super().__init__(driver)

    def do(self):
        old_stdout = sys.stdout  # Memorize the default stdout stream
        app_name = "gnome-calculator"
        run(app_name)
        focus.application(app_name)


class CloseApp(AbstractTransaction):
    """
    Closes the App
    """

    def __init__(self, driver):
        super().__init__(driver)

    def do(self):
        # sys.stdout = old_stdout  # Put the old stream back in place
        screenshot()
        click("Close")
