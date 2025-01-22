from dogtail.tree import root
from dogtail.procedural import run, focus
from dogtail.rawinput import pressKey, keyNameAliases


def test_calculator_with_dogtail():
    app_name = "gnome-calculator"
    run(app_name)
    focus.application(app_name)
    calculator = root.application("gnome-calculator")

    # Simple calculation.
    calculator.child("2").click()
    calculator.child("+").click()
    calculator.child("1").click()
    pressKey(keyNameAliases.get("enter"))

    # Simple check.
    assert calculator.child("3").showing
