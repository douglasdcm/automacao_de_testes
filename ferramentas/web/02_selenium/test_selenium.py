import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sample_page():
    file_path = pathlib.Path(__file__).parent.resolve()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0.5)
    driver.get(f"file:///{file_path}/sample.html")
    title = driver.title
    assert title == "Sample page"

    text_box = driver.find_element(by=By.ID, value="input")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    my_text = "my text"
    text_box.send_keys(my_text)
    submit_button.click()

    message = driver.find_element(by=By.ID, value="result")
    value = message.text
    assert value == f"It works! {my_text}!"
    driver.quit()
