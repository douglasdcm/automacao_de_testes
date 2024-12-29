from selenium.webdriver.common.by import By
from page_transaction.transaction import AbstractTransaction


class SubmitText(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)

    def do(self, **kwargs) -> str:
        text_box = self._driver.find_element(by=By.ID, value="input")
        submit_button = self._driver.find_element(by=By.CSS_SELECTOR, value="button")
        text_box.send_keys(kwargs.get("text"))
        submit_button.click()
        return self._driver.find_element(by=By.ID, value="result").text
