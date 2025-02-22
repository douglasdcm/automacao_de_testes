from playwright.sync_api import Page, expect


def test_button(page: Page):
    page.goto(
        "https://manojkumar4636.github.io/Selenium_Practice_Hub/pages/Button.html"
    )
    expect(page).to_have_title("Interact with Buttons")

    page.get_by_role("button").filter(has_text="Go to Home Page").click()
    expect(page).to_have_title("Selenium Playground")
    page.go_back()

    button_position = (
        page.get_by_role("button").filter(has_text="Get position").bounding_box()
    )
    assert button_position["x"] == 240
    assert button_position["y"] == 304

    button_color = page.get_by_role("button").filter(has_text="What color am I?")
    color = button_color.get_attribute("style")
    assert color == "background-color:lightgreen"

    button_position = (
        page.get_by_role("button").filter(has_text="What is my size?").bounding_box()
    )
    assert button_position["height"] == 20
    assert round(button_position["width"]) == 130
