from selenium import webdriver
from guara.transaction import Application, AbstractTransaction
from guara import it
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from playwright.sync_api import Page, expect
from pages import BasicPage, CheckboxPage
from wrapper import WrapperSelenium


def test_sample_web_page_object(page: Page):
    driver = WrapperSelenium()
    with_name = "douglas"
    with_password = "abc123"
    with_bio = "aaa\\naaa"
    with_country = "Australia"
    with_age = 54
    with_birthdate = "2025-08-28"
    with_email = "foo@email.com"

    basic_page = BasicPage(driver)
    basic_page.goto()
    basic_page.fill_username(with_name)
    basic_page.fill_password(with_password)
    basic_page.fill_email(with_email)
    basic_page.fill_bio(with_bio)
    basic_page.select_country(with_country)
    basic_page.fill_age(with_age)
    basic_page.fill_birthdate(with_birthdate)
    result = basic_page.submit()
    assert result == "Form would be submitted here"

    checkbox_page = CheckboxPage(driver)
    checkbox_page.select_gender()
    checkbox_page.select_interest()
    checkbox_page.select_technology()
