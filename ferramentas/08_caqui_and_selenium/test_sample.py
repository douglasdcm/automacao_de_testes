# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait

from caqui import synchronous, by
from caqui.easy.capabilities import CapabilitiesBuilder, TimeoutsBuilder


def test_convert_selenium_to_caqui_1():
    # driver = webdriver.Chrome()
    driver_url = "http://127.0.0.1:9999"
    capabilities = (
        CapabilitiesBuilder()
        .browser_name("chrome")
        .accept_insecure_certs(True)
        .timeouts(TimeoutsBuilder().implicit(0.5).build())
        # .additional_capability(
        #     {"goog:chromeOptions": {"extensions": [], "args": ["--headless"]}}
        # )
    ).build()
    session = synchronous.get_session(driver_url, capabilities)

    # driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    synchronous.get(
        driver_url,
        session,
        "https://www.selenium.dev/selenium/web/web-form.html",
    )

    # title = driver.title
    title = synchronous.get_title(driver_url, session)
    assert title == "Web form"

    # configured in the capabilities
    # driver.implicitly_wait(0.5)

    # text_box = driver.find_element(by=By.NAME, value="my-text")
    text_box = synchronous.find_element(driver_url, session, by.By.NAME, "my-text")

    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    submit_button = synchronous.find_element(
        driver_url, session, by.By.CSS_SELECTOR, "button"
    )

    # text_box.send_keys("Selenium")
    synchronous.send_keys(driver_url, session, text_box, "Selenium")

    # submit_button.click()
    synchronous.click(driver_url, session, submit_button)

    # message = driver.find_element(by=By.ID, value="message")
    message = synchronous.find_element(driver_url, session, by.By.ID, "message")

    # value = message.text
    value = synchronous.get_text(driver_url, session, message)

    assert value == "Received!"

    # driver.quit()
    synchronous.close_session(driver_url, session)
