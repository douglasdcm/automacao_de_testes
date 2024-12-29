from typing import Any, NoReturn
from selenium.webdriver.remote.webdriver import WebDriver


class AbstractTransaction:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def do(self, **kwargs) -> Any | NoReturn:
        raise NotImplementedError


class Application:
    def __init__(self, driver):
        self._driver = driver

    def perform(self, transaction: AbstractTransaction, **kwargs):
        return transaction(self._driver).do(**kwargs)
