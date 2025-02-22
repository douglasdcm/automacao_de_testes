import re
from playwright.sync_api import Page, expect


def test_radion_button(page: Page) -> None:
    page.goto("https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/radio.html")
    yes = page.get_by_role("radio", name="Yes")
    yes.check()
    expect(yes).to_be_checked()
    expect(page.get_by_role("radio", name="No")).not_to_be_checked()
