import time
from selenium import webdriver
from guara import it
from guara.transaction import Application, AbstractTransaction
from selenium.webdriver.common.by import By


class OpenApp(AbstractTransaction):
    def do(self, url):
        self._driver.get(url)
        return self._driver.title


class CloseApp(AbstractTransaction):
    def do(self):
        self._driver.quit()


def test_google():
    google = Application(webdriver.Chrome())
    google.when(
        OpenApp,
        url="http://www.google.com",
    ).asserts(it.IsEqualTo, "Google")
    google.then(CloseApp)
