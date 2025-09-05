from playwright.sync_api import Page, expect
from selenium import webdriver
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


class Wrapper:

    def __init__(self, driver=None):
        if driver is None:
            raise ValueError("Driver must be provided")
        self._driver = driver

    def goto(self, url):
        raise NotImplementedError()

    def click(self, locator):
        raise NotImplementedError()

    def click_css_selector(self, locator):
        raise NotImplementedError()

    def fill(self, locator, value):
        raise NotImplementedError()

    def set_window_size(self, width, height):
        raise NotImplementedError()

    def select(self, localtor, value):
        raise NotImplementedError()

    def alert_fill(self, text: str) -> None:
        raise NotImplementedError()

    def alert_accept(self) -> str:
        raise NotImplementedError()

    def get_text(self, locator) -> str:
        raise NotImplementedError()

    def get_text_css_selector(self, locator) -> str:
        raise NotImplementedError()

    def switch_to_frame(self, locator):
        raise NotImplementedError()

    def wait_for_text(self, locator, text):
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

    def click_by_css_selector(self, locator):
        self._driver.find_element(By.CSS_SELECTOR, locator).click()

    def fill(self, locator, value):
        self._driver.find_element(By.ID, locator).send_keys(value)

    def fill_by_css_selector(self, locator, value):
        self._driver.find_element(By.CSS_SELECTOR, locator).send_keys(value)

    def select(self, locator, value):
        dropdown = self._driver.find_element(By.ID, locator)
        dropdown.find_element(By.XPATH, f"//option[. = '{value}']").click()

    def alert_fill(self, text: str) -> None:
        alert = self._driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def alert_accept(self):
        alert = self._driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def get_text(self, locator) -> str:
        return self._driver.find_element(By.ID, locator).text

    def get_text_css_selector(self, locator) -> str:
        return self._driver.find_element(By.CSS_SELECTOR, locator).text

    def click_css_selector(self, locator):
        self._driver.find_element(By.CSS_SELECTOR, locator).click()

    def switch_to_frame(self, locator):
        self._driver.switch_to.frame(self._driver.find_element(By.ID, locator))

    def wait_for_text(self, locator, text):
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.text_to_be_present_in_element((By.ID, locator), text))

    def finish(self):
        self._driver.quit()


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
