from guara.transaction import AbstractTransaction

from wrappers.base_wrapper import BaseWrapper


class OpenApp(AbstractTransaction):
    def __init__(self, driver):
        self._driver: BaseWrapper = driver

    def do(self, **kwargs):
        self._driver.goto(kwargs.get("url"))


class CloseApp(AbstractTransaction):
    def __init__(self, driver):
        self._driver: BaseWrapper = driver

    def do(self, **kwargs):
        self._driver.quit()
