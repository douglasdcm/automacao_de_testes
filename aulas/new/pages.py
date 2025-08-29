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


class BasicPage:
    def __init__(self, driver):
        self._driver = driver

    def goto(self):
        self._driver.goto("https://douglasdcm.github.io/aulas/")
        self._driver.set_window_size(1024, 555)

    def fill_username(self, with_name):
        self._driver.fill("username", with_name)

    def fill_password(self, with_password):
        self._driver.fill("password", with_password)

    def fill_email(self, with_email):
        self._driver.fill("email", with_email)

    def fill_bio(self, with_bio):
        self._driver.fill("bio", with_bio)

    def select_country(self, with_country):
        self._driver.select("country", with_country)

    def fill_age(self, with_age):
        self._driver.fill("age", with_age)

    def fill_birthdate(self, with_birthdate):
        self._driver.fill("birthdate", with_birthdate)

    def submit(self):
        self._driver.click("submit-btn")
        return self._driver.alert_accept()


class CheckboxPage:
    def __init__(self, driver):
        self._driver = driver

    def select_interest(self):
        self._driver.click("interest-tech")

    def select_technology(self):
        self._driver.click("interest-music")

    def select_gender(self):
        self._driver.click("gender-female")


class PushButtons:
    def do(self):
        self._driver.click("prompt-btn")
        self._driver.alert_fill("Douglas")
        return self._driver.alert_accept()


class InteractWtihDynamics:
    def do(self):
        self._driver.click("show-hidden-btn")
        return self._driver.get_text("hidden-element")


class InteractWithDropdowns:
    def do(self):
        self._driver.select("country", "Option 3")
        self._driver.select("multi-select", "Yellow")
        self._driver.select("multi-select", "Green")


class InteractWithTables:
    def do(self):
        self._driver.click("add-row-btn")
        return self._driver.get_text_css_selector(
            "#users-table > tbody > tr:nth-child(4) > td:nth-child(1)"
        )


class InteractWithTooltips:
    def do(self):
        self._driver.click_css_selector(".tooltip")
        return self._driver.get_text_css_selector("body > div:nth-child(8) > div.tooltip > span")


def hard_wait_deleteme():
    from time import sleep

    sleep(10)


class InteractWithFiles:
    def do(self):
        self._driver.fill("file-upload", "/home/douglas/repo/automacao_de_testes/aulas/new/foo.txt")
        self._driver.fill(
            "multi-file-upload", "/home/douglas/repo/automacao_de_testes/aulas/new/foo.txt"
        )
        self._driver.fill(
            "multi-file-upload", "/home/douglas/repo/automacao_de_testes/aulas/new/foo.txt"
        )


class InteractWithIFrames:
    def do(self):
        self._driver.click("load-iframe-btn")
        self._driver.switch_to_frame("sample-iframe")
        return self._driver.get_text_css_selector("h3")
