from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from guara.transaction import AbstractTransaction, Application  # Corrected import


# Define Transactions
class NavigateToHomePage(AbstractTransaction):
    def do(self, **kwargs):
        self._driver.get("https://www.williams-sonoma.com/")
        self._driver.refresh()


class HoverOverCookware(AbstractTransaction):
    def do(self, **kwargs):
        cookware_link = self._driver.find_element(By.LINK_TEXT, "Cookware")
        ActionChains(self._driver).move_to_element(cookware_link).perform()


class ClickCookwareSets(AbstractTransaction):
    def do(self, **kwargs):
        self._driver.find_element(By.LINK_TEXT, "Cookware Sets").click()
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h1[text()='Cookware Sets']"))
        )
        return "Cookware Sets"


class ScrollToCookwareSets(AbstractTransaction):
    def do(self, **kwargs):
        cookware_sets_header = self._driver.find_element(By.XPATH, "//h1[text()='Cookware Sets']")
        ActionChains(self._driver).scroll_to_element(cookware_sets_header).perform()


class HoverOverFirstProduct(AbstractTransaction):
    def do(self, **kwargs):
        first_product = self._driver.find_element(
            By.XPATH, "//div[@data-component='Shop-SubCategoryTemplate']/child::div/child::div[1]"
        )
        ActionChains(self._driver).move_to_element(first_product).perform()


class AddToCart(AbstractTransaction):
    def do(self, **kwargs):
        self._driver.find_element(By.XPATH, "//a[text()='Add to Cart']").click()
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//article[@id='itemSelection']/form/fieldset/button")
            )
        )


class ScrollToCheckoutButton(AbstractTransaction):
    def do(self, **kwargs):
        checkout_button = self._driver.find_element(
            By.XPATH, "//article[@id='itemSelection']/form/fieldset/button"
        )
        ActionChains(self._driver).scroll_to_element(checkout_button).perform()


class ClickCheckoutButton(AbstractTransaction):
    def do(self, **kwargs):
        self._driver.find_element(
            By.XPATH, "//article[@id='itemSelection']/form/fieldset/button"
        ).click()


class ViewCartAndCheckout(AbstractTransaction):
    def do(self, **kwargs):
        self._driver.find_element(By.XPATH, "//a[text()='View Cart & Checkout']").click()


class VerifyShoppingCart(AbstractTransaction):
    def do(self, **kwargs):
        cart_header = self._driver.find_element(By.XPATH, "//form[@id='cartForm']/div[2]/div/h1")
        return cart_header.text


class VerifyQuantity(AbstractTransaction):
    def do(self, **kwargs):
        quantity_field = self._driver.find_element(By.ID, "updates[0].quantity")
        quantity_field.click()
        return quantity_field.get_attribute("value")


class NavigateToHome(AbstractTransaction):
    def do(self, **kwargs):
        self._driver.find_element(By.LINK_TEXT, "Williams Sonoma").click()


# Main Script
if __name__ == "__main__":
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.set_window_size(1200, 700)

    # Initialize Application
    app = Application(driver)

    # Perform actions using the Page Transactions pattern
    app.at(NavigateToHomePage)
    app.at(HoverOverCookware)
    app.at(ClickCookwareSets)
    app.at(ScrollToCookwareSets)
    app.at(HoverOverFirstProduct)
    app.at(AddToCart)
    app.at(ScrollToCheckoutButton)
    app.at(ClickCheckoutButton)
    app.at(ViewCartAndCheckout)
    cart_header = app.at(VerifyShoppingCart)
    quantity = app.at(VerifyQuantity)
    app.at(NavigateToHome)

    # Assertions
    assert cart_header == "Shopping Cart", f"Expected 'Shopping Cart', but got '{cart_header}'"
    assert quantity == "1", f"Expected '1', but got '{quantity}'"

    # Close the driver
    driver.quit()
