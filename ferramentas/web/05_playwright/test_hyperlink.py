from playwright.sync_api import Page, expect


def test_hyperlink(page: Page):
    page.goto("https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Link.html")
    expect(page).to_have_title("Interact with HyperLinks")

    page.locator("xpath=//section/div[1]//a[text()='Go to Home Page']").click()
    expect(page).to_have_title("Selenium Playground")
    page.go_back()

    # //section//div[@class='row'][1]//a[text()='Go to Home Page'][1]
