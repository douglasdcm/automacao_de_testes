import random
from datetime import datetime
from selenium.webdriver.common.by import By


class Pom:
    def __init__(self, driver) -> None:
        self.__driver = driver

    def access_url(self, url):
        self.__driver.get(url)
        title = self.__driver.title
        self.__driver.implicitly_wait(0.5)
        return title

    def submit_field(self, text):
        text_box = self.__driver.find_element(by=By.ID, value="input")
        submit_button = self.__driver.find_element(by=By.CSS_SELECTOR, value="button")
        text_box.send_keys(text[random.randrange(len(text))])
        from_input = text_box.get_attribute("value")
        submit_button.click()
        return from_input

    def result_text(self):
        return self.__driver.find_element(by=By.ID, value="result").text

    def close(self):
        self.__driver.get_screenshot_as_file(f"./test{datetime.now()}.png")
        self.__driver.quit()
