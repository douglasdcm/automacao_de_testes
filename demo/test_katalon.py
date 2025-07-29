# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.set_window_size(1200, 700)
        driver.get("https://www.williams-sonoma.com/")
        driver.refresh()
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.LINK_TEXT, "Cookware")
        ).perform()
        driver.find_element(By.LINK_TEXT, "Cookware Sets").click()
        self.assertEqual(
            "Cookware Sets",
            driver.find_element(
                By.XPATH, "//div[@id='subcat-page']/div[9]/section/div[5]/div/h1"
            ).text,
        )
        Wait = WebDriverWait(driver, 10)
        Wait.until(EC.element_to_be_clickable((By.XPATH, "//h1[text()='Cookware Sets']")))

        ActionChains(self.driver).scroll_to_element(
            self.driver.find_element(
                By.XPATH,
                "//h1[text()='Cookware Sets']",
            )
        ).perform()

        ActionChains(self.driver).move_to_element(
            self.driver.find_element(
                By.XPATH,
                "//div[@data-component='Shop-SubCategoryTemplate']/child::div/child::div[1]",
            )
        ).perform()
        driver.find_element(By.XPATH, "//a[text()='Add to Cart']").click()
        Wait = WebDriverWait(driver, 10)
        Wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//article[@id='itemSelection']/form/fieldset/button")
            )
        )
        ActionChains(self.driver).scroll_to_element(
            self.driver.find_element(
                By.XPATH, "//article[@id='itemSelection']/form/fieldset/button"
            )
        ).perform()
        driver.find_element(By.XPATH, "//article[@id='itemSelection']/form/fieldset/button").click()
        driver.find_element(By.XPATH, "//a[text()='View Cart & Checkout']").click()
        driver.find_element(By.XPATH, "//form[@id='cartForm']/div[2]/div").click()
        self.assertEqual(
            "Shopping Cart",
            driver.find_element(By.XPATH, "//form[@id='cartForm']/div[2]/div/h1").text,
        )
        driver.find_element(By.ID, "updates[0].quantity").click()
        self.assertEqual(
            "1",
            driver.find_element(By.ID, "updates[0].quantity").get_attribute("value"),
        )
        driver.find_element(By.LINK_TEXT, "Williams Sonoma").click()

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
