import random
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_generate():
    file_path = pathlib.Path(__file__).parent.resolve()
    driver = webdriver.Chrome()
    driver.get(f"file:////{file_path}/my.html")
    title = driver.title
    assert title == "Sample page"

    button_generate = driver.find_element(by=By.NAME, value="generate")
    button_generate.click()
    code_generated_element = driver.find_element(by=By.ID, value="my-value")
    wait = WebDriverWait(driver, timeout=10)
    wait.until(lambda d: code_generated_element.is_displayed())
    code_generated = code_generated_element.text
    assert code_generated is not ""

    text_field = driver.find_element(by=By.ID, value="input")
    text_field.clear()
    text_field.send_keys(code_generated)
    button_test = driver.find_element(by=By.NAME, value="button")
    button_test.click()
    alert = driver.switch_to.alert
    alert.accept()
    result = driver.find_element(by=By.ID, value="result")
    assert result.text == f"It workls! {code_generated}!"
