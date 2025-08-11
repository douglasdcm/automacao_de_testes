from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from wrappers.base_wrapper import BaseWrapper
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumWrapper(BaseWrapper):
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        self._driver = Chrome(options=options)
        self._current_tab = None

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

    def wait_for_text(self, locator, text):
        wait = WebDriverWait(self._driver, 10)
        wait.until(expected_conditions.text_to_be_present_in_element((By.ID, locator), text))

    def get_number_of_rows(self, locator):
        table = self._driver.find_element(By.ID, locator)
        return len(table.find_elements(By.TAG_NAME, "tr")) - 1  # Exclude header row

    def send_text(self, locator, text, clear=True):
        element = self._driver.find_element(By.ID, locator)
        if clear:
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

    def get_text_by_css(self, locator):
        return self._driver.find_element(By.CSS_SELECTOR, locator).text

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

    def send_text_to_alert(self, text):
        alert = self._driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def quit(self):
        self._driver.quit()
