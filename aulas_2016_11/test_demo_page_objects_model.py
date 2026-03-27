from page_objects import PageObject, PageElement
from selenium import webdriver


class ButtonPage(PageObject):
    go_home_button = PageElement(id_="home")
    get_position = PageElement(id_="position")


class EditPage(PageObject):
    email_field = PageElement(id_="email")


def test_demo_pom():
    BASE_PAGE = "https://manojkumar4636.github.io/Selenium_Practice_Hub/"
    driver = webdriver.Chrome()

    button_page = ButtonPage(driver)
    button_page.get(f"{BASE_PAGE}/pages/Button.html")
    button_page.get_position.click()
    button_page.go_home_button.click()

    edit_page = EditPage(driver)
    email = "any@any.com"
    edit_page.get(f"{BASE_PAGE}/pages/Edit.html")
    edit_page.email_field.send_keys(email)
    assert edit_page.email_field.get_attribute("value") == email
