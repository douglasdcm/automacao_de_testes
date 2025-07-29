# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Home:
    def __setattr__(self, driver):
        self._driver = driver

    def search(self, text):
        self._driver.find_element(By.ID, "search-field").click()
        self._driver.find_element(By.ID, "search-field").clear()
        self._driver.find_element(By.ID, "search-field").send_keys(text)
        self._driver.find_element(By.ID, "search-field").send_keys(Keys.ENTER)


class CookWareSets:
    pass


class Checkout:
    pass


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        URL = "https://www.williams-sonoma.com/"

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        width = 1200
        height = 700

        driver = self.driver
        driver.set_window_size(width, height)
        driver.get(URL)
        driver.refresh()

    def test_app_dynamics_job(self):
        expected = "All-Clad D5® Stainless-Steel 10-Piece Cookware Set"
        home = Home()

        home.search(self.driver, expected)
        self.select_1st_item(self.driver)
        self.add_to_cart(self.driver)
        self.view_cart(self.driver)
        self.assertEqual(
            expected,
            self.get_my_item(self.driver, expected),
        )
        self.clear_quantity(self.driver)

    def clear_quantity(self, driver):
        driver.find_element(By.ID, "updates[0].quantity").click()
        driver.find_element(By.ID, "updates[0].quantity").clear()
        driver.find_element(By.ID, "updates[0].quantity").send_keys("0")
        driver.find_element(By.XPATH, "//button[text()='Update']").click()

    def get_my_item(self, driver, expected):
        return driver.find_element(By.LINK_TEXT, expected).text

    def view_cart(self, driver):
        VIEW_CART = "//a[text()='View Cart & Checkout']"
        driver.find_element(By.XPATH, VIEW_CART).click()

    def add_to_cart(self, driver):
        ActionChains(driver).scroll_to_element(
            driver.find_element(
                By.XPATH,
                "//article[@id='itemSelection']/form/fieldset/button[1]",
            )
        ).perform()

        driver.find_element(
            By.XPATH, "//article[@id='itemSelection']/form/fieldset/button[1]"
        ).click()

    def select_1st_item(self, driver):
        ActionChains(driver).scroll_to_element(
            driver.find_element(
                By.XPATH,
                "//h1[text()='Cookware Sets']",
            )
        ).perform()

        # move mouse first item
        ActionChains(driver).move_to_element(
            driver.find_element(
                By.XPATH,
                "//div[@data-component='Shop-SubCategoryTemplate']/child::div/child::div[1]",
            )
        ).perform()

        # click add to cart
        driver.find_element(
            By.XPATH,
            "//div[@data-component='Shop-SubCategoryTemplate']/child::div/child::div[1]//a[text()='Add to Cart']",
        ).click()

    def access_coockware_sets(self, driver):
        ActionChains(driver).move_to_element(
            driver.find_element(By.LINK_TEXT, "Cookware")
        ).perform()
        driver.find_element(By.LINK_TEXT, "Cookware Sets").click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h1[text()='Cookware Sets']"))
        )

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
