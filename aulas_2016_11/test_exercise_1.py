import utils
import time
import pytest
from selenium import webdriver


@pytest.fixture
def open():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_wait_2(open):
    utils.goto(open, "https://douglasdcm.github.io/aulas/")
    utils.click(open, "ajax-btn")
    utils.wait_for_text(open, "ajax-content", "AJAX content loaded at")


def test_handle_alerts(open):
    utils.goto(open, "https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Alert.html")
    utils.click_by_text(open, "button", "Alert Box")
    utils.dismiss_alert(open)


def test_checkbox(open):
    utils.goto(open, "https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/checkbox.html")
    utils.click_by_xpath(open, '//*[@id="contentblock"]/section/div[1]/div[2]/input')


def test_radio_button(open):
    utils.goto(open, "https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/radio.html")
    utils.click(open, "yes")
    # actual = utils.get_text(open, 'dropdown1')
    # assert actual == "Appium"


def test_dropdown(open):
    utils.goto(open, "https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Dropdown.html")
    utils.select(open, "dropdown1", "Appium")
    # actual = utils.get_text(open, 'dropdown1')
    # assert actual == "Appium"


def test_link(open):
    utils.goto(open, "https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Link.html")
    utils.click_by_text(open, "a", "Go to Home Page")
    assert utils.get_title(open) == "Selenium Playground"


def test_button(open):
    utils.goto(open, "https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Button.html")
    utils.click(open, "home")
    # time.sleep(10)
    assert utils.get_title(open) == "Selenium Playground"


def test_edit(open):
    utils.goto(open, "https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Edit.html")
    utils.send_text_by_xpath(
        open, '//*[@id="contentblock"]/section/div[4]/div/div/input', "aulas", clear=True
    )
    actual = utils.get_text_by_xpath(open, '//*[@id="contentblock"]/section/div[4]/div/div/input')
    assert actual == "aulas"
