import pathlib
import pytest
from datetime import datetime
from selenium import webdriver
from pom import HomePage


@pytest.fixture
def configure():
    driver = webdriver.Chrome()
    yield driver
    driver.get_screenshot_as_file(f"./test{datetime.now()}.png")
    driver.quit()


def test_pom(configure):
    file_path = pathlib.Path(__file__).parent.resolve()
    driver = configure
    pom = HomePage(driver)

    title = pom.access_page(f"file:///{file_path}/sample.html")
    assert title == "Sample page"

    text = ["cheese", "selenium", "test", "bla", "foo"]
    from_input = pom.submit_text(text)
    result = pom.get_result()
    assert result == f"It works! {from_input}!"
