from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from wrappers.base_wrapper import BaseWrapper
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from datetime import datetime, timedelta


class SeleniumWrapper(BaseWrapper):
    def __init__(self):
        options = Options()
        # options.add_argument("--headless")
        self._driver = Chrome(options=options)
        self._current_tab = None

    def get_raw_driver(self):
        """Returns the Selenium Webdriver in case you need it for specific code"""
        return self._driver

    def execute(self, driver_command, params):
        self._driver.execute(driver_command, params)

    def does_element_exist(self, locator):
        return len(self._driver.find_elements(By.ID, locator)) > 0

    def is_element_visible(self, locator):
        return self._driver.find_element(By.ID, locator).is_displayed()

    def is_element_overlapped(self, locator):
        result = False
        if self.does_element_exist(locator):
            try:
                self.click(locator)
            except ElementClickInterceptedException:
                result = True
        return result

    def get_children_of_by_xpath(self, parent, children_locator):
        if isinstance(parent, str):
            element = self._driver.find_element(By.XPATH, parent)
        else:
            element = parent
        return element.find_elements(By.XPATH, children_locator)

    def hover_over_by_class_name(self, locator):
        element = self._driver.find_element(By.CLASS_NAME, locator)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()
        return element.text

    def switch_to_frame(self, locator):
        self._driver.switch_to.frame(self._driver.find_element(By.ID, locator))

    def switch_to_default_content(self):
        self._driver.switch_to.default_content()

    def click(self, locator):
        element = self._driver.find_element(By.ID, locator)
        element.click()

    # If you are bothered about the number of variations of the 'click' method, you
    # still can use other strategies, like receiving the 'locator type' and the 'locator value'
    # or try all locators until you find one that works (it is necessary to handle the exceptions)
    # Be creative!
    def click_by_xpath(self, locator):
        element = self._driver.find_element(By.XPATH, locator)
        element.click()

    def click_by_css(self, locator):
        element = self._driver.find_element(By.CSS_SELECTOR, locator)
        element.click()

    def click_action(self, locator):
        """Performs the click using the ActionChains class"""
        clickable = self._driver.find_element(By.ID, locator)
        self._click_action(clickable)

    def click_action_xpath(self, locator):
        """Performs the click using the ActionChains class"""
        clickable = self._driver.find_element(By.XPATH, locator)
        self._click_action(clickable)

    def click_by_text(self, object_type, text):
        """Performs the click"""
        try:
            element = self._driver.find_element(By.XPATH, f"//{object_type}[text() = '{text}']")
        except Exception:
            element = self._driver.find_element(By.XPATH, f'//{object_type}[text() = "{text}"]')
        element.click()

    def click_action_by_css(self, locator):
        """Performs the click using the ActionChains class"""
        clickable = self._driver.find_element(By.CSS_SELECTOR, locator)
        self._click_action(clickable)

    def _click_action(self, clickable):
        (
            ActionChains(self._driver)
            .move_to_element(clickable)
            .pause(0.5)
            .click_and_hold()
            .pause(0.5)
            .perform()
        )

    def wait_for_text_custom(self, locator, text, timeout=10):
        current_datetime = datetime.now()
        time_to_add = timedelta(seconds=timeout)
        new_datetime = current_datetime + time_to_add
        while datetime.now() < new_datetime:
            element_text = self._driver.find_element(By.ID, locator).text
            if text in element_text:
                return
            sleep(0.1)
        raise TimeoutError()

    def wait_element_be_clicable(self, locator):
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.ID, locator)))

    def wait_element_be_clicable_by_xpath(self, locator):
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, locator)))

    def wait_for_text(self, locator, text, timeout=10):
        wait = WebDriverWait(self._driver, timeout)
        wait.until(expected_conditions.text_to_be_present_in_element((By.ID, locator), text))

    def wait_for_text_by_css(self, locator, text, timeout=10):
        wait = WebDriverWait(self._driver, timeout)
        wait.until(
            expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, locator), text)
        )

    def wait_for_text_by_xpath(self, locator, text, timeout=10):
        wait = WebDriverWait(self._driver, timeout)
        wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, locator), text))

    def get_number_of_rows(self, locator):
        table = self._driver.find_element(By.ID, locator)
        return len(table.find_elements(By.TAG_NAME, "tr")) - 1  # Exclude header row

    def send_text(self, locator, text, clear=True):
        element = self._driver.find_element(By.ID, locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def send_text_by_css(self, locator, text, clear=True):
        element = self._driver.find_element(By.CSS_SELECTOR, locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def send_text_by_name(self, locator, text, clear=True):
        element = self._driver.find_element(By.NAME, locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def send_text_action(self, locator, text, clear=True):
        """Sends a text using the ActionChains class"""
        element = self._driver.find_element(By.ID, locator)
        if clear:
            element.clear()
        (
            ActionChains(self._driver)
            .move_to_element(element)
            .pause(0.5)
            .click_and_hold()
            .pause(0.5)
            .send_keys(text)
            .perform()
        )

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

    def get_text_by_xpath(self, locator):
        text = self._driver.find_element(By.XPATH, locator).text
        if not text:
            text = self._driver.find_element(By.XPATH, locator).get_attribute("value")
        return text

    def get_text_by_class_name(self, locator):
        return self._driver.find_element(By.CLASS_NAME, locator).text

    def get_text_by_css(self, locator):
        return self._driver.find_element(By.CSS_SELECTOR, locator).text

    def maximaize_window(self):
        self._driver.maximize_window()

    def goto(self, url):
        self._driver.get(url)

    def store_original_tab(self):
        self._current_tab = self._driver.current_window_handle

    def restore_original_tab(self):
        if self._current_tab:
            self._driver.switch_to.window(self._current_tab)
        else:
            raise Exception("No tab stored to restore.")

    def close_current_tab(self):
        handles = self._driver.window_handles
        self._go_to_last_window(handles)
        self._driver.close()

    def _go_to_last_window(self, handles):
        self._driver.switch_to.window(handles[len(handles) - 1])

    def dismiss_alert(self):
        alert = self._driver.switch_to.alert
        alert.dismiss()

    def accept_alert(self):
        alert = self._driver.switch_to.alert
        alert.accept()

    def get_text_from_alert(self):
        alert = self._driver.switch_to.alert
        return alert.text

    def send_text_to_alert(self, text):
        alert = self._driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def quit(self):
        self._driver.quit()
