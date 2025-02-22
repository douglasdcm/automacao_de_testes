from playwright.sync_api import Page, expect


def test_dropdown(page: Page):
    page.goto(
        "https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Dropdown.html"
    )
    expect(page).to_have_title("Interact with Drop downs")

    dropdown = page.locator("#dropdown1")
    dropdown.select_option("Selenium")
    expect(dropdown).to_contain_text("Selenium")
