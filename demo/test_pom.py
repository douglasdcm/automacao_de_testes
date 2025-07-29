from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.cookware_link = (By.LINK_TEXT, "Cookware")
        self.cookware_sets_link = (By.LINK_TEXT, "Cookware Sets")

    def navigate_to_homepage(self):
        self.driver.get("https://www.williams-sonoma.com/")
        self.driver.refresh()

    def hover_over_cookware(self):
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(*self.cookware_link)
        ).perform()

    def click_cookware_sets(self):
        self.driver.find_element(*self.cookware_sets_link).click()


class CookwareSetsPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = (By.XPATH, "//div[@id='subcat-page']/div[9]/section/div[5]/div/h1")
        self.first_product = (
            By.XPATH,
            "//div[@data-component='Shop-SubCategoryTemplate']/child::div/child::div[1]",
        )
        self.add_to_cart_button = (By.XPATH, "//a[text()='Add to Cart']")
        self.view_cart_button = (By.XPATH, "//article[@id='itemSelection']/form/fieldset/button")

    def verify_page_title(self):
        return self.driver.find_element(*self.page_title).text

    def scroll_to_first_product(self):
        ActionChains(self.driver).scroll_to_element(
            self.driver.find_element(*self.page_title)
        ).perform()

    def hover_over_first_product(self):
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(*self.first_product)
        ).perform()

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def click_view_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.view_cart_button)
        ).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_title = (By.XPATH, "//form[@id='cartForm']/div[2]/div/h1")
        self.quantity_input = (By.ID, "updates[0].quantity")
        self.home_link = (By.LINK_TEXT, "Williams Sonoma")

    def verify_cart_title(self):
        return self.driver.find_element(*self.cart_title).text

    def verify_quantity(self):
        return self.driver.find_element(*self.quantity_input).get_attribute("value")

    def click_home_link(self):
        self.driver.find_element(*self.home_link).click()


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.set_window_size(1200, 700)

        # Initialize Page Objects
        home_page = HomePage(driver)
        cookware_sets_page = CookwareSetsPage(driver)
        cart_page = CartPage(driver)

        # Test Steps
        home_page.navigate_to_homepage()
        home_page.hover_over_cookware()
        home_page.click_cookware_sets()

        self.assertEqual("Cookware Sets", cookware_sets_page.verify_page_title())
        cookware_sets_page.scroll_to_first_product()
        cookware_sets_page.hover_over_first_product()
        cookware_sets_page.click_add_to_cart()
        cookware_sets_page.click_view_cart()

        self.assertEqual("Shopping Cart", cart_page.verify_cart_title())
        self.assertEqual("1", cart_page.verify_quantity())
        cart_page.click_home_link()

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
