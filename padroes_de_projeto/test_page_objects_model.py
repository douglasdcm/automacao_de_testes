import pathlib
from selenium import webdriver
from pom import Pom


def test_pom():
    file_path = pathlib.Path(__file__).parent.resolve()
    driver = webdriver.Chrome()
    pom = Pom(driver)

    title = pom.access_url(f"file:///{file_path}/sample.html")
    assert title == "Sample page"

    text = ["cheese", "selenium", "test", "bla", "foo"]
    from_input = pom.submit_field(text)
    result = pom.result_text()
    assert result == f"It works! {from_input}!"

    pom.close()
