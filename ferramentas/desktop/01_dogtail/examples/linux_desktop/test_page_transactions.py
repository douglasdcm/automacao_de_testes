from dogtail.tree import root
from dogtail.procedural import run, focus

from examples.linux_desktop.screens import calculator, setup

from guara.transaction import Application
from guara import it


class ItShows(it.IAssertion):
    """
    It checks if the value in shown in the calculator

    Args:
        actual (application): The calculator object
        expected (int): the value that should be present in the screen
    """

    def __init__(self):
        super().__init__()

    def asserts(self, actual, expected):
        assert actual.child(str(expected)).showing


class TestLinuxCalculator:

    def setup_method(self, method):
        # Dogtail first runs the app and then gets the application.
        # So the calculator is opened direclty in the fixture.
        # This is an exception when compared against with other drivers like Selenium
        # that first gets the driver and then opens the app
        app_name = "gnome-calculator"
        run(app_name)
        focus.application(app_name)
        driver = root.application("gnome-calculator")

        self._calculator = Application(driver=driver)
        self._calculator.at(
            setup.OpenApp,
        )

    def teardown_method(self, method):
        self._calculator.at(setup.CloseApp)

    def test_local_page(self):
        self._calculator.at(calculator.Add, a=1, b=2).asserts(ItShows, 3)
