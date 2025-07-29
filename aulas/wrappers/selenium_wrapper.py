from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from wrappers.base_wrapper import BaseWrapper


class SeleniumWrapper(BaseWrapper):
    def __init__(self):
        options = Options()
        # options.add_argument("--headless")
        self._driver = Chrome(options=options)

    def click(self, locator):
        element = self._driver.find_element(By.ID, locator)
        element.click()

    def send_text(self, locator, text):
        element = self._driver.find_element(By.ID, locator)
        element.clear()
        element.send_keys(text)

    def select(self, locator, option):
        dropdown = self._driver.find_element(By.ID, locator)
        dropdown.find_element(By.XPATH, f"//option[. = '{option}']").click()

    def get_dialog_text(self):
        return self._driver.switch_to.alert.text

    def get_text(self, locator):
        text = self._driver.find_element(By.ID, locator).text
        if not text:
            text = self._driver.find_element(By.ID, locator).get_attribute("value")
        return text

    def get_text_by_class_name(self, locator):
        return self._driver.find_element(By.CLASS_NAME, locator).text

    def goto(self, url):
        self._driver.get(url)

    def quit(self):
        self._driver.quit()
