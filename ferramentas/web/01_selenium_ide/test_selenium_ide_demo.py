# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        self.driver.set_window_size(970, 555)
        self.driver.find_element(By.ID, "my-text-id").click()
        self.driver.find_element(By.ID, "my-text-id").send_keys("test")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.ID, "message").click()
        assert self.driver.find_element(By.ID, "message").text == "Received!"
        self.driver.close()
