from selenium import webdriver
from pom import Pom


def test_sample_page():
    driver = webdriver.Chrome()

    pom = Pom(driver)
    pom.access_url("file:///home/douglas/sample.html")
    text = ["cheese", "selenium", "test", "bla", "foo"]
    from_input = pom.submit_field(text)
    pom.result_text(from_input)
    pom.close()
