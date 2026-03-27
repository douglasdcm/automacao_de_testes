from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def test_waits():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    # Open browser
    driver = webdriver.Chrome(options=options)
    # Set implicit wait
    driver.implicitly_wait(2)
    # Navigate to the web form page
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    # Find the element to reveal hidden text
    revealed = driver.find_element("id", "my-text-id")
    # Wait until the element is displayed
    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda _: revealed.is_displayed())
