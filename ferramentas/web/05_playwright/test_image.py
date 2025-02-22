from playwright.sync_api import Page, expect


def test_image(page: Page):
    page.goto("https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Image.html")
    expect(page).to_have_title("Interact with Images")

    page.locator("xpath=//label[@for='home']/following-sibling::img").click()
    expect(page).to_have_title("Selenium Playground")
    page.go_back()
