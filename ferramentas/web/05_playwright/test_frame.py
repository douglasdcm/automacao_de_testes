import re
from playwright.sync_api import Page, expect


def test_frame(page: Page):
    page.goto("https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/frame.html")
    button = page.get_by_text(
        "<p>iframes are not supported"
    ).first.content_frame.get_by_role("button", name="Click Me")
    button.click()
    expect(
        page.get_by_text(
            "<p>iframes are not supported"
        ).first.content_frame.get_by_role("button", name="Hurray! You Clicked Me.")
    ).to_be_visible()
