import pathlib
import pytest
from selenium import webdriver
from page_transaction.access import OpenApp, CloseApp
from page_transaction.transaction import Application
from page_transaction import home

FILE_PATH = pathlib.Path(__file__).parent.resolve()


@pytest.fixture
def configure():
    app = Application(webdriver.Chrome())
    app.perform(OpenApp, url=f"file:///{FILE_PATH}/sample.html")
    yield app
    app.perform(CloseApp)


def test_sample_page_transaction(configure):
    app: Application = configure
    expected = "python"
    result = app.perform(home.SubmitText, text=expected)
    assert result == f"It works! {expected}!"
