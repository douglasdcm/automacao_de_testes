import pytest
from selenium import webdriver
from guara import it
from guara.transaction import Application, AbstractTransaction
from selenium.webdriver.common.by import By


class OpenApp(AbstractTransaction):
    def do(self, url):
        self._driver.maximize_window()
        self._driver.get(url)
        return self._driver.title


class CloseApp(AbstractTransaction):
    def do(self):
        self._driver.quit()


class Login(AbstractTransaction):
    def do(self):
        user = self._driver.find_element(By.ID, "user-name")
        user.send_keys("standard_user")
        password = self._driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        self._driver.find_element(By.ID, "login-button").click()
        label = self._driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/div"
        )
        return label.text


class AddToCart(AbstractTransaction):
    def do(self):
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        # self._driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
        return self._driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']").text


class ViewCart(AbstractTransaction):
    def do(self):
        self._driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']").click()
        return self._driver.find_element(By.XPATH, "//div[@data-test='item-quantity']").text


@pytest.fixture
def ecommerce():
    ecommence = Application(webdriver.Chrome())
    yield ecommence
    ecommence.then(CloseApp)


def test_ecommerce(ecommerce: Application):
    ecommerce.at(OpenApp, url="https://www.saucedemo.com/")
    ecommerce.when(Login).asserts(it.IsEqualTo, "Swag Labs")
    ecommerce.when(AddToCart).asserts(it.IsEqualTo, "1")
    ecommerce.when(ViewCart).asserts(it.IsEqualTo, "1")
