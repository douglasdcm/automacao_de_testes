import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_select_dropdown():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        breakpoint()
        select = Select(driver.find_element(By.NAME, "my-select"))
        
        select.select_by_visible_text("Three")
        assert select.first_selected_option.text == "Three"
        
        select.select_by_value("1")
        assert select.first_selected_option.get_attribute("value") == "1"
        
        select.select_by_index(0)
        assert select.first_selected_option.text == "Open this select menu"
        
    except Exception as e:
        pytest.fail(f"O teste falhou devido a uma excecao: {e}")
        
    finally:
        driver.quit()
