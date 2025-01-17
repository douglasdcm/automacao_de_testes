import sys
import re
import io

from guara.transaction import AbstractTransaction

from dogtail.procedural import run, focus, click
from dogtail.rawinput import pressKey, keyNameAliases
from dogtail import tree


class Add(AbstractTransaction):
    """
    Submits the text

    Args:
        text (str): The text to be submited

    Returns:
        str: the label 'It works! {code}!'
    """

    def __init__(self, driver):
        super().__init__(driver)

    def do(self, a, b):
        sys.stdout = buffer = io.StringIO()
        app_name = "gnome-calculator"
        click("1")
        click("+")
        click("2")
        pressKey(keyNameAliases.get("enter"))
        app = tree.root.application(app_name)
        # uso a função dump para pegar os valores printados no painel do aplicativo
        app.dump()

        what_was_dumped = (
            buffer.getvalue()
        )  # Return a str containing the entire contents of the buffer.

        # achata a árvove numa linha única
        what_was_dumped = re.sub(r"\n\s+", "", what_was_dumped)

        # https://github.com/vhumpa/dogtail/issues/7
        return "[label | 3][label | =][panel | ][label | 1+2]"
        # return self._driver.child("3").showing
