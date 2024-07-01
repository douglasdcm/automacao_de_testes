import pathlib
from selenium import webdriver
from pom import Pom


def test_aaa():
    # arrange
    file_path = pathlib.Path(__file__).parent.resolve()
    driver = webdriver.Chrome()
    pom = Pom(driver)

    # act
    title = pom.access_url(f"file:///{file_path}/sample.html")
    # assert
    assert title == "Sample page"

    # arrange
    text = ["cheese", "selenium", "test", "bla", "foo"]
    # act
    from_input = pom.submit_field(text)
    result = pom.result_text()
    # assert
    assert result == f"It works! {from_input}!"

    # cleanup
    pom.close()
