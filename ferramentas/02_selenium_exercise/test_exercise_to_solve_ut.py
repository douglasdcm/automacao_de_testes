import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ChromeOptions
import unittest


class TestStringMethods(unittest.TestCase):
    def test_sample_page(self):
        file_path = pathlib.Path(__file__).parent.resolve()

        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)

        driver.get(f"file:////{file_path}/sample-exercise_.html")
        self.generate_code(driver)
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

    def generate_code(self, driver):
        generate = driver.find_element(By.NAME, "generate")
        generate.click()


if __name__ == "__main__":
    unittest.main()
