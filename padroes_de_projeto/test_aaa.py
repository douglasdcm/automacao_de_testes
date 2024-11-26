import pathlib
from selenium import webdriver
from pom import HomePage


def test_aaa():
    # arrange
    file_path = pathlib.Path(__file__).parent.resolve()
    driver = webdriver.Chrome()
    pom = HomePage(driver)

    # act
    title = pom.access_page(f"file:///{file_path}/sample.html")
    # assert
    assert title == "Sample page"

    # arrange
    text = ["cheese", "selenium", "test", "bla", "foo"]
    # act
    from_input = pom.submit_text(text)
    result = pom.get_result()
    # assert
    assert result == f"It works! {from_input}!"

    # cleanup
    pom.close_page()
