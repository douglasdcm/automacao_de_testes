import random
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sample_page():
    file_path = pathlib.Path(__file__).parent.resolve()
    driver = webdriver.Chrome()

    driver.get(f"file:///{file_path}/sample.html")

    title = driver.title
    # assert title == "Web form"
    assert title == "Sample page"

    driver.implicitly_wait(0.5)

    # text_box = driver.find_element(by=By.NAME, value="input")
    text_box = driver.find_element(by=By.ID, value="input")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text = ["cheese", "selenium", "test", "bla", "foo"]
    text_box.send_keys(text[random.randrange(len(text))])
    from_input = text_box.get_attribute("value")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="result")
    value = message.text
    # assert value == "It workls! Selenium!"
    assert value == f"It works! {from_input}!"

    driver.quit()
