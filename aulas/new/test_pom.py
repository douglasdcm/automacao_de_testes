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


class Home:
    def __init__(self, driver):
        self._driver = driver

    def search(self, value):
        self._driver.find_element(By.NAME, "q").send_keys(value + Keys.RETURN)

    def press(self):
        self._driver.find_element(By.NAME, "btnK").click()


class All:

    def __init__(self, driver):
        self._driver = driver

    def get_first_result(self):
        text = self._driver.find_element(
            By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div[1]/div/div/span/a/h3"
        ).text
        return text


def test_sample_web_page_object(page: Page):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    home = Home(driver)
    home.search("Guara")

    from time import sleep

    sleep(5000)

    all_page = All(driver)
    first_result = all_page.get_first_result()
    assert "Prefeitura Municipal de Guará" in first_result
