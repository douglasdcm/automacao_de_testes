import random
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_sample_page():
    file_path = pathlib.Path(__file__).parent.resolve()
    driver = webdriver.Chrome()
    driver.get(f"file:////{file_path}/sample-exercise_.html")
    generate_code(driver)
    sleep(5)
    code = driver.find_element(By.ID, "my-value")
    input = driver.find_element(By.ID, "input")
    input.clear()
    input.send_keys(code.text)
    test_bnt = driver.find_element(By.NAME, "button")
    test_bnt.click()

    alert = driver.switch_to.alert
    alert.accept()

    result = driver.find_element(By.ID, "result")
    assert result.text == f"It workls! {code.text}!"

    driver.quit()


def generate_code(driver):
    generate = driver.find_element(By.NAME, "generate")
    generate.click()
