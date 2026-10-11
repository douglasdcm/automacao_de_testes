from playwright.sync_api import Page, expect
from wrappers.base_wrapper import BaseWrapper


class PlaywrightWrapper(BaseWrapper):
    def __init__(self, driver: Page):
        self._driver: Page = driver
        self._browser = self._driver
        self._dialog_message = ""

    def _dialog_handler(self, dialog):
        dialog.accept()
        self._dialog_message = dialog.message

    def _dialog_handler_send_message(self, dialog):
        dialog.send_text_to_alert("This is a prompt")
        dialog.accept()
        self._dialog_message = dialog.message

    def dismiss_alert(self):
        pass

    def store_original_tab(self):
        self._current_tab = self._driver.context.pages[0]

    def close_current_tab(self):
        self._driver.context.pages[-1].close()

    def restore_original_tab(self):
        self._current_tab.bring_to_front()

    def send_text_to_alert(self, text):
        self._driver.once("dialog", self._dialog_handler_send_message)

    def click(self, locator):
        # Register the dialog handler to capture alert messages
        self._driver.once("dialog", self._dialog_handler)
        self._driver.locator(f"id={locator}").click(force=True)

    def send_text(self, locator, text, clear=True):
        if not isinstance(text, str):
            text = str(text)
        element = self._driver.locator(f"id={locator}")
        if element.get_attribute("type") == "file":
            element.set_input_files(text)
        else:
            element.fill(text)

    def select(self, locator, value):
        self._driver.locator(f"id={locator}").select_option(value)

    def goto(self, url):
        self._driver.goto(url=url)

    def get_text(self, locator):
        text = self._driver.locator(f"id={locator}").text_content()
        if not text:
            text = self._driver.locator(f"id={locator}").input_value()
        return text

    def get_text_by_css(self, locator):
        self._driver.locator(locator).wait_for(state="visible")
        return self._driver.locator(locator).text_content()

    def wait_for_text(self, locator, text):
        expect(self._driver.locator(f"id={locator}")).to_contain_text(text)

    def get_dialog_text(self):
        return self._dialog_message

    def get_number_of_rows(self, locator):
        # Getting all rows from all tables, because when getting them by a specific
        # table is not working properly
        return self._driver.locator("tr").count() - 1  # Exclude header row

    def hover_over_by_class_name(self, locator):
        element = self._driver.locator(f".{locator}")
        element.hover()
        return element.text_content()

    def switch_to_frame(self, locator):
        frame = self._driver.frame_locator(f"iframe#{locator}")
        if not frame:
            raise ValueError(f"Frame with locator '{locator}' not found")
        self._driver = frame

    def quit(self):
        self._browser.close()
