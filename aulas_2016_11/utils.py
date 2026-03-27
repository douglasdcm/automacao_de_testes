from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from datetime import datetime, timedelta


def get_raw_driver(driver):
    """Return the underlying Selenium WebDriver instance."""
    return driver


def get_title(driver):
    """Return the current page title."""
    return driver.title


def execute(driver, driver_command, params):
    """
    Execute a custom WebDriver command.

    Args:
        driver: Selenium WebDriver instance.
        driver_command (str): The command to execute.
        params (dict): Parameters to send with the command.
    """
    driver.execute(driver_command, params)


def does_element_exist(driver, locator):
    """
    Check whether an element exists in the DOM by ID.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Element ID.

    Returns:
        bool: True if the element exists, False otherwise.
    """
    return len(driver.find_elements(By.ID, locator)) > 0


def is_element_visible(driver, locator):
    """
    Check whether an element is visible on the page.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Element ID.

    Returns:
        bool: True if the element is displayed.
    """
    return driver.find_element(By.ID, locator).is_displayed()


def is_element_overlapped(driver, locator):
    """
    Determine if an element is overlapped by another element.

    Attempts to click the element and checks if the click is intercepted.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Element ID.

    Returns:
        bool: True if the element is overlapped.
    """
    result = False
    if does_element_exist(locator):
        try:
            click(locator)
        except ElementClickInterceptedException:
            result = True
    return result


def get_children_of_by_xpath(driver, parent, children_locator):
    """
    Return child elements of a parent element using XPath.

    Args:
        driver: Selenium WebDriver instance.
        parent (str | WebElement): Parent XPath or WebElement.
        children_locator (str): XPath for child elements.

    Returns:
        list[WebElement]: List of found child elements.
    """
    if isinstance(parent, str):
        element = driver.find_element(By.XPATH, parent)
    else:
        element = parent
    return element.find_elements(By.XPATH, children_locator)


def hover_over_by_class_name(driver, locator):
    """
    Hover the mouse over an element located by class name.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Class name of the element.

    Returns:
        str: Text of the hovered element.
    """
    element = driver.find_element(By.CLASS_NAME, locator)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    return element.text


def switch_to_frame(driver, locator):
    """
    Switch the driver context to an iframe by ID.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Frame ID.
    """
    driver.switch_to.frame(driver.find_element(By.ID, locator))


def switch_to_default_content(driver):
    """Switch context back to the main document."""
    driver.switch_to.default_content()


def click(driver, locator):
    """
    Click an element located by ID.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Element ID.
    """
    element = driver.find_element(By.ID, locator)
    element.click()


# If you are bothered about the number of variations of the 'click' method, you
# still can use other strategies, like receiving the 'locator type' and the 'locator value'
# or try all locators until you find one that works (it is necessary to handle the exceptions)
# Be creative!
def click_by_xpath(driver, locator):
    """
    Click an element located by XPath.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): XPath locator.
    """
    element = driver.find_element(By.XPATH, locator)
    element.click()


def click_by_css(driver, locator):
    """
    Click an element located by CSS selector.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): CSS selector.
    """
    element = driver.find_element(By.CSS_SELECTOR, locator)
    element.click()


def click_action(driver, locator):
    """
    Click an element using ActionChains.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Element ID.
    """
    clickable = driver.find_element(By.ID, locator)
    _click_action(driver, clickable)


def click_action_xpath(driver, locator):
    """
    Click an element using ActionChains with an XPath locator.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): XPath locator.
    """
    clickable = driver.find_element(By.XPATH, locator)
    _click_action(driver, clickable)


def click_by_text(driver, object_type, text):
    """
    Click an element by matching its exact text.

    Args:
        driver: Selenium WebDriver instance.
        object_type (str): HTML tag (e.g., 'button', 'a').
        text (str): Exact text to match.
    """
    try:
        element = driver.find_element(By.XPATH, f"//{object_type}[text() = '{text}']")
    except Exception:
        element = driver.find_element(By.XPATH, f'//{object_type}[text() = "{text}"]')
    element.click()


def click_action_by_css(driver, locator):
    """
    Click an element using ActionChains with a CSS selector.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): CSS selector.
    """
    clickable = driver.find_element(By.CSS_SELECTOR, locator)
    _click_action(driver, clickable)


def _click_action(driver, clickable):
    """
    Perform a click using ActionChains.

    Args:
        driver: Selenium WebDriver instance.
        clickable (WebElement): Element to click.
    """
    (
        ActionChains(driver)
        .move_to_element(clickable)
        .pause(0.5)
        .click_and_hold()
        .pause(0.5)
        .perform()
    )


def wait_for_text_custom(driver, locator, text, timeout=10):
    """
    Wait until specific text appears in an element.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Element ID.
        text (str): Text to wait for.
        timeout (int): Maximum wait time in seconds.

    Raises:
        TimeoutError: If text does not appear within the timeout.
    """
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
    """
    Wait until an element located by ID becomes clickable.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Element ID.
    """
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.element_to_be_clickable((By.ID, locator)))


def wait_element_be_clicable_by_xpath(driver, locator):
    """
    Wait until an element located by XPath becomes clickable.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): XPath locator.
    """
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, locator)))


def wait_for_text(driver, locator, text, timeout=10):
    """
    Wait until text appears in an element located by ID.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Element ID.
        text (str): Text to wait for.
        timeout (int): Timeout in seconds.
    """
    wait = WebDriverWait(driver, timeout)
    wait.until(expected_conditions.text_to_be_present_in_element((By.ID, locator), text))


def wait_for_text_by_css(driver, locator, text, timeout=10):
    """
    Wait until text appears in an element located by CSS selector.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): CSS selector.
        text (str): Text to wait for.
        timeout (int): Timeout in seconds.
    """
    wait = WebDriverWait(driver, timeout)
    wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, locator), text))


def wait_for_text_by_xpath(driver, locator, text, timeout=10):
    """
    Wait until text appears in an element located by XPath.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): XPath locator.
        text (str): Text to wait for.
        timeout (int): Timeout in seconds.
    """
    wait = WebDriverWait(driver, timeout)
    wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, locator), text))


def get_number_of_rows(driver, locator):
    """
    Return the number of rows in a table (excluding the header).

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Table ID.

    Returns:
        int: Number of data rows.
    """
    table = driver.find_element(By.ID, locator)
    return len(table.find_elements(By.TAG_NAME, "tr")) - 1


def send_text(driver, locator, text, clear=True):
    """
    Send text to an input element located by ID.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Element ID.
        text (str): Text to send.
        clear (bool): Whether to clear existing text first.
    """
    element = driver.find_element(By.ID, locator)
    if clear:
        element.clear()
    element.send_keys(text)


def send_text_by_css(driver, locator, text, clear=True):
    """Send text to an element located by CSS selector."""
    element = driver.find_element(By.CSS_SELECTOR, locator)
    if clear:
        element.clear()
    element.send_keys(text)


def send_text_by_name(driver, locator, text, clear=True):
    """Send text to an element located by name attribute."""
    element = driver.find_element(By.NAME, locator)
    if clear:
        element.clear()
    element.send_keys(text)


def send_text_by_xpath(driver, locator, text, clear=True):
    """Send text to an element located by XPath."""
    element = driver.find_element(By.XPATH, locator)
    if clear:
        element.clear()
    element.send_keys(text)


def send_text_action(driver, locator, text, clear=True):
    """
    Send text to an element using ActionChains.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Element ID.
        text (str): Text to type.
        clear (bool): Whether to clear the field first.
    """
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
    """
    Select an option from a dropdown by visible text.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Dropdown ID.
        option (str): Visible option text.
    """
    dropdown = driver.find_element(By.ID, locator)
    dropdown.find_element(By.XPATH, f"//option[. = '{option}']").click()


def get_dialog_text(driver):
    """Return the text of the currently displayed alert dialog."""
    return driver.switch_to.alert.text


def get_text(driver, locator):
    """
    Retrieve text from an element by ID.

    Falls back to the 'value' attribute if the element has no text.

    Args:
        driver: Selenium WebDriver instance.
        locator (str): Element ID.

    Returns:
        str: Element text or value.
    """
    text = driver.find_element(By.ID, locator).text
    if not text:
        text = driver.find_element(By.ID, locator).get_attribute("value")
    return text


def get_text_by_xpath(driver, locator):
    """Retrieve text from an element located by XPath."""
    text = driver.find_element(By.XPATH, locator).text
    if not text:
        text = driver.find_element(By.XPATH, locator).get_attribute("value")
    return text


def get_text_by_class_name(driver, locator):
    """Return text from an element located by class name."""
    return driver.find_element(By.CLASS_NAME, locator).text


def get_text_by_css(driver, locator):
    """Return text from an element located by CSS selector."""
    return driver.find_element(By.CSS_SELECTOR, locator).text


def maximaize_window(driver):
    """Maximize the browser window."""
    driver.maximize_window()


def goto(driver, url):
    """
    Navigate the browser to a URL.

    Args:
        driver: Selenium WebDriver instance.
        url (str): Target URL.
    """
    driver.get(url)


def return_current_tab(driver):
    """Return the handle of the current browser tab."""
    return driver.current_window_handle


def go_to_window(driver, window):
    """
    Switch focus to a specific browser window.

    Args:
        driver: Selenium WebDriver instance.
        window (str): Window handle.
    """
    driver.switch_to.window(window)


def close_current_tab(driver):
    """Close the current browser tab."""
    handles = driver.window_handles
    _go_to_last_window(driver, handles)
    driver.close()


def _go_to_last_window(driver, handles):
    """
    Switch to the last window handle in the list.

    Args:
        driver: Selenium WebDriver instance.
        handles (list): List of window handles.
    """
    driver.switch_to.window(handles[len(handles) - 1])


def dismiss_alert(driver):
    """Dismiss the currently displayed alert."""
    alert = driver.switch_to.alert
    alert.dismiss()


def accept_alert(driver):
    """Accept the currently displayed alert."""
    alert = driver.switch_to.alert
    alert.accept()


def get_text_from_alert(driver):
    """Return the text of the active alert."""
    alert = driver.switch_to.alert
    return alert.text


def send_text_to_alert(driver, text):
    """
    Send text to a prompt alert and accept it.

    Args:
        driver: Selenium WebDriver instance.
        text (str): Text to send to the alert prompt.
    """
    alert = driver.switch_to.alert
    alert.send_keys(text)
    alert.accept()


def quit(driver):
    """Close the browser and end the WebDriver session."""
    driver.quit()
