# Dogtail demo script

import dogtail.tc
import re
from dogtail.procedural import *
from dogtail.rawinput import pressKey, keyNameAliases
from dogtail import tree
from dogtail.utils import screenshot
from time import sleep

import sys
import io


TestString = dogtail.tc.TCString()


def test_1_plus_2_is_3():
    # pré-condição para rodar o teste
    try:
        # arrange
        # Start app
        old_stdout = sys.stdout  # Memorize the default stdout stream
        sys.stdout = buffer = io.StringIO()
        app_name = "gnome-calculator"
        run(app_name)
        focus.application(app_name)

        # act
        click("1")
        click("+")
        click("2")
        # No 'dump' existem vários botões "=". Para achar o correto é preciso
        # navegar pela árvore. Optei por usar o "enter"
        # click("=")
        pressKey(keyNameAliases.get("enter"))
        sleep(3)
        screenshot()

        # assert
        app = tree.root.application(app_name)
        # uso a função dump para pegar os valores printados no painel do aplicativo
        app.dump()

        what_was_dumped = (
            buffer.getvalue()
        )  # Return a str containing the entire contents of the buffer.

        # achata a árvove numa linha única
        what_was_dumped = re.sub(r"\n\s+", "", what_was_dumped)

        assert "[label | 3][label | =][panel | ][label | 1+2]" in what_was_dumped
    except Exception:
        raise
    finally:
        sys.stdout = old_stdout  # Put the old stream back in place
        click("Close")
