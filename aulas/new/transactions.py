from selenium import webdriver
from guara.transaction import Application, AbstractTransaction
from guara import it
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class NavigateToPage(AbstractTransaction):
    def do(self):
        self._driver.goto("https://douglasdcm.github.io/aulas/")


class SubtimForm(AbstractTransaction):

    def do(
        self, with_name, with_password, with_email, with_bio, with_country, with_age, with_birthdate
    ):
        self._driver.set_window_size(1024, 555)
        self._driver.fill("username", with_name)
        self._driver.fill("password", with_password)
        self._driver.fill("email", with_email)
        self._driver.fill("bio", with_bio)
        self._driver.select("country", with_country)
        self._driver.fill("age", with_age)
        self._driver.fill("birthdate", with_birthdate)
        self._driver.click("submit-btn")
        return self._driver.alert_accept()


class FillCheckbox(AbstractTransaction):
    def do(self):
        self._driver.click("interest-tech")
        self._driver.click("interest-music")
        self._driver.click("gender-female")


class PushButtons(AbstractTransaction):
    def do(self):
        self._driver.click("prompt-btn")
        self._driver.alert_fill("Douglas")
        return self._driver.alert_accept()


class InteractWtihDynamics(AbstractTransaction):
    def do(self):
        self._driver.click("show-hidden-btn")
        return self._driver.get_text("hidden-element")


class InteractWithDropdowns(AbstractTransaction):
    def do(self):
        self._driver.select("country", "Option 3")
        self._driver.select("multi-select", "Yellow")
        self._driver.select("multi-select", "Green")


class InteractWithTables(AbstractTransaction):
    def do(self):
        self._driver.click("add-row-btn")
        return self._driver.get_text_css_selector(
            "#users-table > tbody > tr:nth-child(4) > td:nth-child(1)"
        )


class InteractWithTooltips(AbstractTransaction):
    def do(self):
        self._driver.click_css_selector(".tooltip")
        return self._driver.get_text_css_selector("body > div:nth-child(8) > div.tooltip > span")


def hard_wait_deleteme():
    from time import sleep

    sleep(10)


class InteractWithFiles(AbstractTransaction):
    def do(self):
        self._driver.fill("file-upload", "/home/douglas/repo/automacao_de_testes/aulas/new/foo.txt")
        self._driver.fill(
            "multi-file-upload", "/home/douglas/repo/automacao_de_testes/aulas/new/foo.txt"
        )
        self._driver.fill(
            "multi-file-upload", "/home/douglas/repo/automacao_de_testes/aulas/new/foo.txt"
        )


class InteractWithIFrames(AbstractTransaction):
    def do(self):
        self._driver.click("load-iframe-btn")
        self._driver.switch_to_frame("sample-iframe")
        return self._driver.get_text_css_selector("h3")
