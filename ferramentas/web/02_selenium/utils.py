from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from datetime import datetime, timedelta


def get_raw_driver(driver):
    """Returns the Selenium Webdriver in case you need it for specific code"""
    return driver

def execute(driver, driver_command, params):
    driver.execute(driver_command, params)

def does_element_exist(driver, locator):
    return len(driver.find_elements(By.ID, locator)) > 0

def is_element_visible(driver, locator):
    return driver.find_element(By.ID, locator).is_displayed()

def is_element_overlapped(driver, locator):
    result = False
    if does_element_exist(locator):
        try:
            click(locator)
        except ElementClickInterceptedException:
            result = True
    return result

def get_children_of_by_xpath(driver, parent, children_locator):
    if isinstance(parent, str):
        element = driver.find_element(By.XPATH, parent)
    else:
        element = parent
    return element.find_elements(By.XPATH, children_locator)

def hover_over_by_class_name(driver, locator):
    element = driver.find_element(By.CLASS_NAME, locator)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    return element.text

def switch_to_frame(driver, locator):
    driver.switch_to.frame(driver.find_element(By.ID, locator))

def switch_to_default_content(driver):
    driver.switch_to.default_content()

def click(driver, locator):
    element = driver.find_element(By.ID, locator)
    element.click()

# If you are bothered about the number of variations of the 'click' method, you
# still can use other strategies, like receiving the 'locator type' and the 'locator value'
# or try all locators until you find one that works (it is necessary to handle the exceptions)
# Be creative!
def click_by_xpath(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    element.click()

def click_by_css(driver, locator):
    element = driver.find_element(By.CSS_SELECTOR, locator)
    element.click()

def click_action(driver, locator):
    """Performs the click using the ActionChains class"""
    clickable = driver.find_element(By.ID, locator)
    _click_action(clickable)

def click_action_xpath(driver, locator):
    """Performs the click using the ActionChains class"""
    clickable = driver.find_element(By.XPATH, locator)
    _click_action(clickable)

def click_by_text(driver, object_type, text):
    """Performs the click"""
    try:
        element = driver.find_element(By.XPATH, f"//{object_type}[text() = '{text}']")
    except Exception:
        element = driver.find_element(By.XPATH, f'//{object_type}[text() = "{text}"]')
    element.click()

def click_action_by_css(driver, locator):
    """Performs the click using the ActionChains class"""
    clickable = driver.find_element(By.CSS_SELECTOR, locator)
    _click_action(clickable)

def _click_action(driver, clickable):
    (
        ActionChains(driver)
        .move_to_element(clickable)
        .pause(0.5)
        .click_and_hold()
        .pause(0.5)
        .perform()
    )

def wait_for_text_custom(driver, locator, text, timeout=10):
    current_datetime = datetime.now()
    time_to_add = timedelta(seconds=timeout)
    new_datetime = current_datetime + time_to_add
    while datetime.now() < new_datetime:
        element_text = driver.find_element(By.ID, locator).text
        if text in element_text:
            return
        sleep(0.1)
    raise TimeoutError()

def wait_element_be_clicable(driver, locator):
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.element_to_be_clickable((By.ID, locator)))

def wait_element_be_clicable_by_xpath(driver, locator):
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, locator)))

def wait_for_text(driver, locator, text, timeout=10):
    wait = WebDriverWait(driver, timeout)
    wait.until(expected_conditions.text_to_be_present_in_element((By.ID, locator), text))

def wait_for_text_by_css(driver, locator, text, timeout=10):
    wait = WebDriverWait(driver, timeout)
    wait.until(
        expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, locator), text)
    )

def wait_for_text_by_xpath(driver, locator, text, timeout=10):
    wait = WebDriverWait(driver, timeout)
    wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, locator), text))

def get_number_of_rows(driver, locator):
    table = driver.find_element(By.ID, locator)
    return len(table.find_elements(By.TAG_NAME, "tr")) - 1  # Exclude header row

def send_text(driver, locator, text, clear=True):
    element = driver.find_element(By.ID, locator)
    if clear:
        element.clear()
    element.send_keys(text)

def send_text_by_css(driver, locator, text, clear=True):
    element = driver.find_element(By.CSS_SELECTOR, locator)
    if clear:
        element.clear()
    element.send_keys(text)

def send_text_by_name(driver, locator, text, clear=True):
    element = driver.find_element(By.NAME, locator)
    if clear:
        element.clear()
    element.send_keys(text)

def send_text_action(driver, locator, text, clear=True):
    """Sends a text using the ActionChains class"""
    element = driver.find_element(By.ID, locator)
    if clear:
        element.clear()
    (
        ActionChains(driver)
        .move_to_element(element)
        .pause(0.5)
        .click_and_hold()
        .pause(0.5)
        .send_keys(text)
        .perform()
    )

def select(driver, locator, option):
    dropdown = driver.find_element(By.ID, locator)
    dropdown.find_element(By.XPATH, f"//option[. = '{option}']").click()

def get_dialog_text(driver):
    return driver.switch_to.alert.text

def get_text(driver, locator):
    text = driver.find_element(By.ID, locator).text
    if not text:
        text = driver.find_element(By.ID, locator).get_attribute("value")
    return text

def get_text_by_xpath(driver, locator):
    text = driver.find_element(By.XPATH, locator).text
    if not text:
        text = driver.find_element(By.XPATH, locator).get_attribute("value")
    return text

def get_text_by_class_name(driver, locator):
    return driver.find_element(By.CLASS_NAME, locator).text

def get_text_by_css(driver, locator):
    return driver.find_element(By.CSS_SELECTOR, locator).text

def maximaize_window(driver):
    driver.maximize_window()

def goto(driver, url):
    driver.get(url)

def return_current_tab(driver):
    return driver.current_window_handle

def go_to_window(driver, window):
    driver.switch_to.window(window)

def close_current_tab(driver):
    handles = driver.window_handles
    _go_to_last_window(handles)
    driver.close()

def _go_to_last_window(driver, handles):
    driver.switch_to.window(handles[len(handles) - 1])

def dismiss_alert(driver):
    alert = driver.switch_to.alert
    alert.dismiss()

def accept_alert(driver):
    alert = driver.switch_to.alert
    alert.accept()

def get_text_from_alert(driver):
    alert = driver.switch_to.alert
    return alert.text

def send_text_to_alert(driver, text):
    alert = driver.switch_to.alert
    alert.send_keys(text)
    alert.accept()

def quit(driver):
    driver.quit()
