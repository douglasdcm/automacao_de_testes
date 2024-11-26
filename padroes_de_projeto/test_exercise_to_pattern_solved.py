import random
import pathlib
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def init():
    driver = webdriver.Chrome()
    driver.implicitly_wait(0.5)
    yield driver
    driver.quit()


def test_sample_page_to_pattern_solved(init):
    text = ["cheese", "selenium", "test", "bla", "foo"]
    text = text[random.randrange(len(text))]

    driver = init
    hp = HomePage
    hp.driver = driver

    hp.go_to()
    title = hp.get_title()
    assert title == "Sample page"

    hp.submit_text(text)

    message = hp.get_message()
    from_input = hp.get_text_from_text_box()
    assert message == f"It works! {from_input}!"


class HomePage:
    driver = None

    @staticmethod
    def __find_text_box():
        return HomePage.driver.find_element(by=By.ID, value="input")

    @staticmethod
    def go_to():
        FILE_PATH = pathlib.Path(__file__).parent.resolve()
        HomePage.driver.get(f"file:///{FILE_PATH}/sample.html")

    @staticmethod
    def get_title():
        return HomePage.driver.title

    @staticmethod
    def submit_text(text):
        text_box = HomePage.__find_text_box()
        submit_button = HomePage.driver.find_element(by=By.CSS_SELECTOR, value="button")
        text_box.send_keys(text)
        submit_button.click()

    @staticmethod
    def get_text_from_text_box():
        return HomePage.__find_text_box().get_attribute("value")

    @staticmethod
    def get_message():
        return HomePage.driver.find_element(by=By.ID, value="result").text
