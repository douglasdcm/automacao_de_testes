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
from playwright.sync_api import Page, expect


class Wrapper:

    def __init__(self, driver=None):
        if driver is None:
            raise ValueError("Driver must be provided")
        self._driver = driver

    def goto(self, url):
        raise NotImplementedError()

    def click(self, locator):
        raise NotImplementedError()

    def fill(self, locator, value):
        raise NotImplementedError()

    def set_window_size(self, width, height):
        raise NotImplementedError()

    def select(self, localtor, value):
        raise NotImplementedError()

    def alert_accept(self) -> str:
        raise NotImplementedError()


class WrapperSelenium(Wrapper):
    def __init__(self):
        self._driver = webdriver.Chrome()

    def set_window_size(self, width, height):
        return self._driver.set_window_size(width, height)

    def goto(self, url):
        self._driver.get(url)

    def click(self, locator):
        self._driver.find_element(By.ID, locator).click()

    def fill(self, locator, value):
        self._driver.find_element(By.ID, locator).send_keys(value)

    def select(self, locator, value):
        dropdown = self._driver.find_element(By.ID, locator)
        dropdown.find_element(By.XPATH, f"//option[. = '{value}']").click()

    def alert_accept(self):
        alert = self._driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text


class WrapperPlaywright(Wrapper):

    def __init__(self, driver: Page):
        self._driver: Page = driver
        self._browser = self._driver
        self._dialog_message = ""

    def set_window_size(self, width, height):
        pass

    def goto(self, url):
        self._driver.goto(url=url)

    def fill(self, locator, text, clear=True):
        if not isinstance(text, str):
            text = str(text)
        element = self._driver.locator(f"id={locator}")
        if element.get_attribute("type") == "file":
            element.set_input_files(text)
        else:
            element.fill(text)

    def select(self, locator, value):
        self._driver.locator(f"id={locator}").select_option(value)


class SubtimForm(AbstractTransaction):

    def do(
        self, with_name, with_password, with_email, with_bio, with_country, with_age, with_birthdate
    ):
        self._driver.goto("https://douglasdcm.github.io/aulas/")
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
        pass


class PushButtons(AbstractTransaction):
    def do(self):
        pass


def test_sample_web_page(page: Page):
    app = Application(WrapperPlaywright(page))
    app.when(
        SubtimForm,
        with_name="douglas",
        with_password="abc123",
        with_bio="aaa\\naaa",
        with_country="Australia",
        with_age=54,
        with_birthdate="2025-08-28",
        with_email="foo@email.com",
    ).asserts(it.IsEqualTo, "Form would be submitted here")
    app.when(FillCheckbox)
    app.when(PushButtons)


class Home:
    def __init__(self, driver):
        self._driver = driver

    def search(self, value):
        self._driver.find_element(By.NAME, "q").send_keys(value)

    def press(self):
        self._driver.find_element(By.NAME, "btnK").click()
