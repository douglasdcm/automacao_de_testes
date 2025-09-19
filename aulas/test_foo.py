import pytest
from wrappers.selenium_wrapper import SeleniumWrapper
from wrappers.playwright_wrapper import PlaywrightWrapper
from playwright.sync_api import Page


def hard_wait_deleteme(time):
    from time import sleep

    sleep(time)


@pytest.fixture
def handle_browser():
    driver = SeleniumWrapper()
    # driver = PlaywrightWrapper(page)
    yield driver
    driver.quit()


def test_visibility(handle_browser: SeleniumWrapper):
    driver = handle_browser
    driver.goto("http://uitestingplayground.com/visibility")
    assert driver.is_element_visible("transparentButton") is True
    assert driver.is_element_visible("removedButton") is True
    assert driver.is_element_visible("invisibleButton") is True
    assert driver.is_element_visible("zeroWidthButton") is True
    assert driver.is_element_visible("notdisplayedButton") is True
    assert driver.is_element_visible("overlappedButton") is True
    assert driver.is_element_visible("transparentButton") is True
    assert driver.is_element_visible("offscreenButton") is True
    driver.click_by_text("button", "Hide")
    assert driver.is_element_visible("transparentButton") is False
    assert driver.does_element_exist("removedButton") is False
    assert driver.is_element_visible("invisibleButton") is False
    assert driver.is_element_visible("zeroWidthButton") is False
    assert driver.is_element_visible("notdisplayedButton") is False
    assert driver.is_element_overlapped("overlappedButton") is True
    assert driver.is_element_visible("transparentButton") is False
    assert driver.is_element_visible("offscreenButton") is False


def test_progress_bar(handle_browser: SeleniumWrapper):
    driver = handle_browser
    driver.goto("http://uitestingplayground.com/progressbar")
    driver.click_by_text("button", "Start")
    driver.wait_for_text_custom("progressBar", "75%", 30)


def test_verify_text(handle_browser: SeleniumWrapper):
    driver = handle_browser
    driver.goto("http://uitestingplayground.com/verifytext")
    driver.wait_for_text_by_css(".bg-primary > span:nth-child(1)", "Welcome")
    assert "Welcome" in driver.get_text_by_css(".bg-primary > span:nth-child(1)")


def test_scrollbar(handle_browser: SeleniumWrapper):
    driver = handle_browser
    driver.goto("http://uitestingplayground.com/scrollbars")
    driver.click_by_text("button", "Hiding Button")


def test_text_input(handle_browser: SeleniumWrapper):
    driver = handle_browser
    driver.goto("http://uitestingplayground.com/textinput")
    text = "foo"
    driver.send_text("newButtonName", text)
    driver.click_by_text("button", "Button That Should Change it's Name Based on Input Value")
    assert driver.get_text("updatingButton") == text


def test_click(handle_browser: SeleniumWrapper):
    driver = handle_browser
    driver.goto("http://uitestingplayground.com/click")
    driver.click_by_text("button", "Button That Ignores DOM Click Event")
    driver.click_by_text("button", "Button That Ignores DOM Click Event")


def test_client_side_delay(handle_browser: SeleniumWrapper):
    driver = handle_browser
    driver.goto("http://uitestingplayground.com/clientdelay")
    driver.click_by_text("button", "Button Triggering Client Side Logic")
    driver.wait_for_text_by_xpath(
        "//div[@id='content']/p", "Data calculated on the client side.", 20
    )
    assert (
        driver.get_text_by_xpath("//div[@id='content']/p") == "Data calculated on the client side."
    )


def test_ajax_data(handle_browser: SeleniumWrapper):
    driver = handle_browser
    driver.goto("http://uitestingplayground.com/ajax")
    driver.click_by_text("button", "Button Triggering AJAX Request")
    driver.wait_for_text_by_xpath(
        "//div[@id='content']/p", "Data loaded with AJAX get request.", 20
    )
    assert (
        driver.get_text_by_xpath("//div[@id='content']/p") == "Data loaded with AJAX get request."
    )


def test_class_load_delay(handle_browser: SeleniumWrapper):
    driver = handle_browser
    driver.goto("http://uitestingplayground.com/loaddelay")
    driver.click_by_text("button", "Button Appearing After Delay")


def test_class_hidden_layer(handle_browser: SeleniumWrapper):
    driver = handle_browser
    driver.goto("http://uitestingplayground.com/hiddenlayers")
    driver.click("greenButton")
    driver.click("blueButton")


def test_class_attribute(handle_browser: SeleniumWrapper):
    driver = handle_browser
    driver.goto("http://uitestingplayground.com/classattr")
    LOCATOR = "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"
    driver.click_by_xpath(LOCATOR)
    assert driver.get_text_from_alert() == "Primary button pressed"
    driver.accept_alert()


def test_dynamic_button(handle_browser: SeleniumWrapper):
    driver = handle_browser
    driver.goto("http://uitestingplayground.com/dynamicid")
    button_text = "Button with Dynamic ID"
    driver.click_by_text("button", button_text)
