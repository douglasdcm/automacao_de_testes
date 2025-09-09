from time import sleep
from wrappers.base_wrapper import BaseWrapper
from caqui.by import By
from caqui import synchronous
from caqui.easy.options import ChromeOptionsBuilder
from caqui.easy.capabilities import ChromeCapabilitiesBuilder, TimeoutsBuilder
from datetime import datetime, timedelta


class TimeoutError(Exception):
    pass


class CaquiWrapper(BaseWrapper):
    def __init__(self, server_url):
        options = ChromeOptionsBuilder().to_dict()
        timeout = TimeoutsBuilder().implicit(30).to_dict()
        capabilities = (
            ChromeCapabilitiesBuilder()
            .accept_insecure_certs(True)
            .timeouts(timeout)
            .add_options(options)
        ).to_dict()
        session = synchronous.get_session(server_url, capabilities)
        self._connection = (server_url, session)
        self._current_tab = None
        self._TIMEOUT = 30
        self._SLEEP = 0.5

    def goto(self, url):
        synchronous.go_to_page(*(self._connection), url)

    # There are lots of code duplication in the 'wait' functions. Refactor it
    def wait_for_text(self, locator, text):
        current_datetime = datetime.now()
        time_to_add = timedelta(seconds=self._TIMEOUT)
        new_datetime = current_datetime + time_to_add
        while datetime.now() < new_datetime:
            element = synchronous.find_element(*(self._connection), By.ID, locator)
            element_text = synchronous.get_text(*(self._connection), element)
            if text in element_text:
                return
            sleep(self._SLEEP)
        raise TimeoutError()

    def wait_for_text_presence(self, locator):
        current_datetime = datetime.now()
        time_to_add = timedelta(seconds=self._TIMEOUT)
        new_datetime = current_datetime + time_to_add
        while datetime.now() < new_datetime:
            element = synchronous.find_element(*(self._connection), By.ID, locator)
            element_text = synchronous.get_text(*(self._connection), element)
            if element_text:
                return
            sleep(self._SLEEP)
        raise TimeoutError()

    def wait_for_text_presence_css(self, locator):
        current_datetime = datetime.now()
        time_to_add = timedelta(seconds=self._TIMEOUT)
        new_datetime = current_datetime + time_to_add
        while datetime.now() < new_datetime:
            element = synchronous.find_element(*(self._connection), By.CSS_SELECTOR, locator)
            element_text = synchronous.get_text(*(self._connection), element)
            if element_text:
                return
            sleep(self._SLEEP)
        raise TimeoutError()

    def wait_for_element_presence(self, locator):
        current_datetime = datetime.now()
        time_to_add = timedelta(seconds=self._TIMEOUT)
        new_datetime = current_datetime + time_to_add
        while datetime.now() < new_datetime:
            elements = synchronous.find_elements(*(self._connection), By.ID, locator)
            if elements:
                return
            sleep(self._SLEEP)
        raise TimeoutError()

    def wait_for_element_presence_by_css(self, locator):
        current_datetime = datetime.now()
        time_to_add = timedelta(seconds=self._TIMEOUT)
        new_datetime = current_datetime + time_to_add
        while datetime.now() < new_datetime:
            elements = synchronous.find_elements(*(self._connection), By.CSS_SELECTOR, locator)
            if elements:
                return
            sleep(self._SLEEP)
        raise TimeoutError()

    def get_text(self, locator):
        self.wait_for_element_presence(locator)
        element = synchronous.find_element(*(self._connection), By.ID, locator)
        self.wait_for_text_presence(locator)
        return synchronous.get_text(*(self._connection), element)

    def get_text_by_css(self, locator):
        self.wait_for_element_presence_by_css(locator)
        element = synchronous.find_element(*(self._connection), By.CSS_SELECTOR, locator)
        self.wait_for_text_presence_css(locator)
        return synchronous.get_text(*(self._connection), element)

    def get_number_of_rows(self, locator):
        table = synchronous.find_element(*(self._connection), By.ID, locator)
        return (
            len(synchronous.find_children_elements(*(self._connection), table, By.TAG_NAME, "tr"))
            - 1
        )  # Exclude header row

    def get_dialog_text(self):
        return synchronous.get_alert_text(*(self._connection))

    def hover_over_by_class_name(self, locator):
        element = synchronous.find_element(*(self._connection), By.CLASS_NAME, locator)
        synchronous.actions_move_to_element(*(self._connection), element)
        return synchronous.get_text(*(self._connection), element)

    def dismiss_alert(self):
        synchronous.dismiss_alert(*(self._connection))

    def click(self, locator):
        element = synchronous.find_element(*(self._connection), By.ID, locator)
        synchronous.click(*(self._connection), element)

    def store_original_tab(self):
        self._current_tab = synchronous.get_window_handles(*(self._connection))[0]

    def close_current_tab(self):
        tab = synchronous.get_window_handles(*(self._connection))[-1]
        synchronous.switch_to_window(*(self._connection), tab)
        synchronous.close_window(*(self._connection))

    def restore_original_tab(self):
        synchronous.switch_to_window(*(self._connection), self._current_tab)

    def send_text_to_alert(self, text):
        synchronous.send_alert_text(*(self._connection), text)

    def send_text(self, locator, text, clear=True):
        element = synchronous.find_element(*(self._connection), By.ID, locator)
        if clear:
            synchronous.clear_element(*(self._connection), element)
        synchronous.send_keys(*(self._connection), element, str(text))

    def select(self, locator, value):
        parent_element = synchronous.find_element(*(self._connection), By.ID, locator)
        synchronous.click(*(self._connection), parent_element)
        element = synchronous.find_child_element(
            *(self._connection), parent_element, By.XPATH, f"//option[. = '{value}']"
        )
        synchronous.click(*(self._connection), element)

    def switch_to_frame(self, locator):
        frame = synchronous.find_element(*(self._connection), By.ID, locator)
        synchronous.switch_to_frame(*(self._connection), frame)

    def quit(self):
        synchronous.close_window(*(self._connection))
        synchronous.close_session(*(self._connection))
