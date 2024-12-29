from datetime import datetime
from page_transaction.transaction import AbstractTransaction
from selenium.webdriver.common.by import By


class OpenApp(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)

    def do(self, **kwargs):
        self._driver.set_window_size(1094, 765)
        self._driver.get("https://vagaspramim.onrender.com/")
        self._driver.implicitly_wait(0.5)
        return self._driver.find_element(By.CSS_SELECTOR, ".navbar-text").click()


class CloseApp(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)

    def do(self, **kwargs):
        self._driver.get_screenshot_as_file(f"/tmp/test{datetime.now()}.png")
        self._driver.quit()
