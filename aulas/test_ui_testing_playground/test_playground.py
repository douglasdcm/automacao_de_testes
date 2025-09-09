# Attention: No assertion was put in the tests, just sleeps for manual verification
# Try to assert the expected behavior by yourself (extra exercise)

from test_ui_testing_playground.utils import hard_sleep
from wrappers.selenium_wrapper import SeleniumWrapper
from selenium.webdriver.common.by import By
from pytest import fixture, mark


@fixture
def with_driver():
    driver = SeleniumWrapper()
    yield driver
    driver.quit()


def test_dynamic_id(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/dynamicid"
    with_driver.goto(URL)
    with_driver.click_by_xpath("*//section/div/button")
    hard_sleep()


def test_class_attribute(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/classattr"
    with_driver.goto(URL)
    with_driver.click_by_xpath(
        "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"
    )
    # simplified xpath
    # with_driver.click_by_xpath("//button[contains(@class,'btn-primary')]")
    with_driver.dismiss_alert()
    hard_sleep()


def test_hidden_layers(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/hiddenlayers"
    with_driver.goto(URL)
    if with_driver.does_element_exist("blueButton") is False:
        with_driver.click("greenButton")

    # If the blue button does not exist, then click
    if with_driver.does_element_exist("blueButton") is False:
        with_driver.click("greenButton")
    hard_sleep()


def test_load_delay(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/loaddelay"
    with_driver.goto(URL)
    XPATH = "//button[contains(@class,'btn-primary')]"
    with_driver.wait_element_be_clicable_by_xpath(XPATH)
    with_driver.click_by_xpath(XPATH)
    hard_sleep()


def test_load_delay(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/loaddelay"
    with_driver.goto(URL)
    XPATH = "//button[contains(@class,'btn-primary')]"
    with_driver.wait_element_be_clicable_by_xpath(XPATH)
    with_driver.click_by_xpath(XPATH)
    hard_sleep()


def test_ajax(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/ajax"
    with_driver.goto(URL)
    with_driver.click("ajaxButton")
    with_driver.wait_for_text_by_css("#content > p", "Data loaded with AJAX get request.", 20)
    hard_sleep()


def test_client_side_delay(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/clientdelay"
    with_driver.goto(URL)
    with_driver.click("ajaxButton")
    with_driver.wait_for_text_by_css("#content > p", "Data calculated on the client side.", 20)
    hard_sleep()


def test_click_action(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/click"
    with_driver.goto(URL)
    with_driver.click("badButton")
    hard_sleep()


def test_text_input_action(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/textinput"
    with_driver.goto(URL)
    with_driver.send_text_action("newButtonName", "New Button Name")
    with_driver.click("updatingButton")
    hard_sleep()


def test_scroll_bars(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/scrollbars"
    with_driver.goto(URL)
    # Selenium scrolls to element automatically
    with_driver.click("hidingButton")
    hard_sleep()


def test_dynamic_table(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/dynamictable"
    with_driver.goto(URL)

    # Using Selenium Webdriver as this code is very specify and
    # can not be reused
    raw_driver = with_driver.get_raw_driver()
    table = raw_driver.find_element(By.XPATH, "//section//div[@role = 'table']")
    rows = table.find_elements(By.XPATH, "//div[@role = 'row']")

    header = rows[0]
    # each header is a string with all values like "Name Memory Disk CPU Network"
    header_split = header.text.split(" ")
    column_index = 1
    # find the index were the CPU is
    for h in header_split:
        if h.lower() == "cpu":
            break
        column_index += 1

    result = None
    for row in rows[1:]:
        # remove units before split
        row = row.text.replace(" MB/s", "").replace(" Mbps", "").replace(" MB", "")
        row_split = row.split(" ")
        if row_split[0].lower() == "chrome":
            result = row_split[column_index - 1]

    with_driver.wait_for_text_by_css("p.bg-warning", f"Chrome CPU: {result}")


def test_verify_text(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/verifytext"
    with_driver.goto(URL)
    with_driver.wait_for_text_by_css("div.bg-primary > span", "Welcome UserName!")


def test_progress_bar(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/progressbar"
    with_driver.goto(URL)
    with_driver.click("startButton")
    with_driver.wait_for_text("progressBar", "75%", timeout=60)
    with_driver.click("stopButton")
    hard_sleep()


def test_visibility(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/visibility"
    with_driver.goto(URL)
    assert with_driver.is_element_visible("removedButton") is True
    assert with_driver.is_element_visible("zeroWidthButton") is True
    assert with_driver.is_element_visible("overlappedButton") is True
    assert with_driver.is_element_visible("transparentButton") is True
    assert with_driver.is_element_visible("invisibleButton") is True
    assert with_driver.is_element_visible("notdisplayedButton") is True
    assert with_driver.is_element_visible("offscreenButton") is True
    with_driver.click("hideButton")
    assert with_driver.does_element_exist("removedButton") is False
    assert with_driver.is_element_visible("zeroWidthButton") is False
    assert with_driver.is_element_overlapped("overlappedButton") is True
    assert with_driver.is_element_visible("transparentButton") is False
    assert with_driver.is_element_visible("invisibleButton") is False
    assert with_driver.is_element_visible("notdisplayedButton") is False
    assert with_driver.is_element_visible("offscreenButton") is False


def test_sample_app(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/sampleapp"
    with_driver.goto(URL)
    with_driver.send_text_by_name("UserName", "admin")
    with_driver.send_text_by_name("Password", "pwd")
    with_driver.click("login")
    with_driver.wait_for_text("loginstatus", "Welcome, admin!")


def test_mouse_over(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/mouseover"
    with_driver.goto(URL)
    # CSS selector hard-coded. Fix it!
    with_driver.click_by_css("div:nth-child(7) > a")
    with_driver.click_by_css("div:nth-child(7) > a")
    with_driver.wait_for_text_by_css("div:nth-child(8) > p", "The link above clicked 2 times.")
    with_driver.click_by_css("div:nth-child(9) > a")
    with_driver.click_by_css("div:nth-child(9) > a")
    with_driver.wait_for_text_by_css("div:nth-child(10) > p", "The link above clicked 2 times.")


@mark.skip(reason="Exercise for students")
def test_non_breaking_space(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/nbsp"
    with_driver.goto(URL)
    with_driver.click_by_xpath("//button[text()='My Button']")


def test_overlapped_element(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/overlapped"
    with_driver.goto(URL)
    with_driver.send_text("id", "123")
    try:
        # Go to an element after the "name" textbox to show it
        with_driver.click("subject")
    except Exception:
        pass
    with_driver.send_text("name", "my name")
    hard_sleep()


def test_shadow_dom(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/shadowdom"
    with_driver.goto(URL)
    # Using Selenium Webdriver as it is a very specific scenario
    raw_driver = with_driver.get_raw_driver()
    shadow_host = raw_driver.find_element(By.CSS_SELECTOR, "guid-generator")
    shadow_root = shadow_host.shadow_root
    shadow_content = shadow_root.find_element(By.ID, "buttonGenerate")
    shadow_content.click()
    shadow_content = shadow_root.find_element(By.ID, "buttonCopy")
    shadow_content.click()
    shadow_content = shadow_root.find_element(By.ID, "editField").get_attribute("value")
    assert shadow_content != ""


@mark.skip(reason="Exercise for students")
def test_alerts(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/alerts"
    with_driver.goto(URL)


@mark.skip(reason="Exercise for students")
def test_send_file(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/upload"
    with_driver.goto(URL)


@mark.skip(reason="Exercise for students")
def test_animated_button(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/animation"
    with_driver.goto(URL)


@mark.skip(reason="Exercise for students")
def test_disabled_input(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/disabledinput"
    with_driver.goto(URL)


@mark.skip(reason="Exercise for students")
def test_auto_wait(with_driver: SeleniumWrapper):
    URL = "http://uitestingplayground.com/autowait"
    with_driver.goto(URL)
