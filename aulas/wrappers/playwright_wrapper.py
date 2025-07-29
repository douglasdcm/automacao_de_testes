from playwright.sync_api import Page
from wrappers.base_wrapper import BaseWrapper


class PlaywrightWrapper(BaseWrapper):
    def __init__(self, driver: Page):
        self._driver: Page = driver
        self._dialog_message = ""

    def _dialog_handler(self, dialog):
        dialog.accept()
        self._dialog_message = dialog.message

    def click(self, locator):
        # Register the dialog handler to capture alert messages
        self._driver.once("dialog", self._dialog_handler)
        self._driver.locator(f"id={locator}").click()

    def send_text(self, locator, text):
        if not isinstance(text, str):
            text = str(text)
        self._driver.locator(f"id={locator}").fill(text)

    def select(self, locator, value):
        self._driver.locator(f"id={locator}").select_option(value)

    def goto(self, url):
        self._driver.goto(url=url)

    def get_dialog_text(self):
        return self._dialog_message

    def quit(self):
        self._driver.close()
