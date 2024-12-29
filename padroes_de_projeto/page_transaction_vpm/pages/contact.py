from selenium.webdriver.common.by import By
from page_transaction.transaction import AbstractTransaction


class GoTo(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)

    def do(self, **kwargs):
        self._driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(6) img").click()
        self._driver.find_element(By.CSS_SELECTOR, ".container:nth-child(3)").click()
        return self._driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").text
