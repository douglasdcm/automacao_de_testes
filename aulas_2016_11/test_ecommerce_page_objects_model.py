from page_objects import PageObject, PageElement
import pytest
from selenium import webdriver


class ButtonPage(PageObject):
    go_home_button = PageElement(id_="home")
    get_position = PageElement(id_="position")


class EditPage(PageObject):
    email_field = PageElement(id_="email")


class LoginPage(PageObject):
    username_field = PageElement(id_="user-name")
    password_field = PageElement(id_="password")
    login_button = PageElement(id_="login-button")


class ProductPage(PageObject):
    add_to_cart = PageElement(id_="add-to-cart-sauce-labs-backpack")
    cart_button = PageElement(xpath="//span[@data-test='shopping-cart-badge']")


class YourCartPage(PageObject):
    qtde_field = PageElement(xpath="//div[@data-test='item-quantity']")


@pytest.fixture
def ecommerce():
    driver = webdriver.Chrome()
    yield driver


def test_commerce_pom(ecommerce):
    BASE_PAGE = "https://www.saucedemo.com/"
    driver = ecommerce
    login_page = LoginPage(driver)
    login_page.get(BASE_PAGE)
    login_page.username_field.send_keys("standard_user")
    login_page.password_field.send_keys("secret_sauce")
    login_page.login_button.click()

    product_page = ProductPage(driver)
    product_page.add_to_cart.click()
    assert product_page.cart_button.text == "1"
    product_page.cart_button.click()

    your_cart_page = YourCartPage(driver)
    assert your_cart_page.qtde_field.text == "1"
