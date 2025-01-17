from examples.linux_desktop.screens import calculator, setup

from guara.transaction import Application
from guara import it


class TestLinuxCalculator:
    def setup_method(self, method):
        self._calculator = Application(None)
        self._calculator.at(
            setup.OpenApp,
        )

    def teardown_method(self, method):
        self._calculator.at(setup.CloseApp)

    def test_local_page(self):
        self._calculator.at(calculator.Add, a=1, b=2).asserts(
            it.Contains, "[label | 3][label | =][panel | ][label | 1+2]"
        )
