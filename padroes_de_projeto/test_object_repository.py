import random
import pathlib
import pytest
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver


class ObjectRepository:
    @staticmethod
    def set(driver):
        ObjectRepository._driver = driver

    class HomePage:
        @staticmethod
        def access_page(url):
            ObjectRepository._driver.get(url)
            ObjectRepository._driver.implicitly_wait(0.5)

        def get_title_page():
            return ObjectRepository._driver.title

        def submit_text(text):
            text_box = ObjectRepository._driver.find_element(by=By.ID, value="input")
            submit_button = ObjectRepository._driver.find_element(
                by=By.CSS_SELECTOR, value="button"
            )
            text_box.send_keys(text)
            submit_button.click()

        def get_result():
            return ObjectRepository._driver.find_element(by=By.ID, value="result").text

    class OtherPage:
        def do():
            ObjectRepository._driver


FILE_PATH = pathlib.Path(__file__).parent.resolve()


@pytest.fixture
def configure():
    driver = webdriver.Chrome()
    yield driver
    driver.get_screenshot_as_file(f"./test{datetime.now()}.png")
    driver.quit()


def test_sample_object_repository(configure):
    driver = configure
    r = ObjectRepository
    r.set(driver)
    expected = "python"

    r.HomePage.access_page(f"file:///{FILE_PATH}/sample.html")
    assert r.HomePage.get_title_page() == "Sample page"

    r.HomePage.submit_text(expected)
    result = r.HomePage.get_result()

    assert result == f"It works! {expected}!"

    r.OtherPage.do()
