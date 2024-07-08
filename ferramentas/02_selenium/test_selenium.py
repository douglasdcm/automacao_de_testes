from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_demo():
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    driver.quit()


# source: https://github.com/SeleniumHQ/seleniumhq.github.io/blob/91329809cbfc3b017910f861f5a7751065e62f9b/examples/python/tests/waits/test_waits.py#L36
def test_explicit_waits():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()

    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda d: revealed.is_displayed())

    revealed.send_keys("Displayed")
    assert revealed.get_property("value") == "Displayed"
