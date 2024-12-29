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

    @property
    def result(self):
        return self._result

    def at_page(self, transaction: AbstractTransaction, **kwargs):
        self._result = transaction(self._driver).do(**kwargs)
        return self

    def assert_equals(self, content):
        assert self._result == content

    def assert_contains(self, content):
        assert content in self._result
