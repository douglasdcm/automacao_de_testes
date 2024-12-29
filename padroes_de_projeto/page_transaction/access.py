from datetime import datetime
from page_transaction.transaction import AbstractTransaction


class OpenApp(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)

    def do(self, **kwargs):
        self._driver.get(kwargs.get("url"))
        self._driver.implicitly_wait(0.5)
        return self._driver.title


class CloseApp(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)

    def do(self, **kwargs):
        self._driver.get_screenshot_as_file(f"./test{datetime.now()}.png")
        self._driver.quit()
