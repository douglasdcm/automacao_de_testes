from playwright.sync_api import Page, expect


def test_edit(page: Page):
    page.goto("https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Edit.html")
    expect(page).to_have_title("Interact with Edit Fields")

    email_text = "email@email.com"
    email = page.locator("id=email")
    email.fill(email_text)
    expect(email).to_have_value(email_text)

    other_text = "other"
    append_text = page.locator("xpath=//input[@type='text' and @value='Append ']")
    append_text.fill(other_text)
    expect(append_text).to_have_value("other")

    default_text = page.locator("xpath=//input[@name='username' and @value='TestLeaf']")
    expect(default_text).to_have_value("TestLeaf")

    clear_text = page.locator("xpath=//input[@name='username' and @value='Clear me!!']")
    clear_text.clear()
    expect(clear_text).to_be_empty()

    disabled = page.locator(
        "xpath=//label[text()='Confirm that edit field is disabled']//following-sibling::input"
    )
    expect(disabled).to_be_disabled()
