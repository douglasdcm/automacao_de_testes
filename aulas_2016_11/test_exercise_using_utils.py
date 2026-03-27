import utils
from selenium import webdriver

def test_use_utils():
    driver = webdriver.Chrome()
    utils.goto(driver, "https://douglasdcm.github.io/aulas/")
    utils.send_text_by_css(driver, "#username", "Fulano")
    utils.click(driver, "interest-tech")
    utils.click(driver, "interest-sports")
    utils.click(driver, "gender-female")
    utils.click_by_text(driver, "button", "Simple Button")
    utils.dismiss_alert(driver)
    utils.click_by_text(driver, "button", "Load Content via AJAX")
    utils.wait_for_text(driver, "ajax-content", "AJAX content loaded at")
    utils.select(driver, "simple-dropdown", "Option 2")
    utils.select(driver, "multi-select", "Red")
    utils.select(driver, "multi-select", "Green")
    utils.hover_over_by_class_name(driver, "tooltip")
    utils.wait_for_text_by_css(driver, ".tooltiptext", "This is a tooltip")
