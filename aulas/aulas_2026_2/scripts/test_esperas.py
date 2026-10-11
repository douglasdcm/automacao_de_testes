import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_esperas():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        
        locator_id = (By.ID, "my-text-id")
        elemento_visivel = wait.until(EC.visibility_of_element_located(locator_id))
        assert elemento_visivel.is_displayed()
        
        locator_xpath = (By.XPATH, "//button[@type='submit']")
        elemento_clicavel = wait.until(EC.element_to_be_clickable(locator_xpath))
        assert elemento_clicavel.is_enabled()
        
        elemento_clicavel.click()
        
        assert wait.until(EC.url_contains("submitted-form"))
        
    except Exception as e:
        pytest.fail(f"O teste falhou devido a uma excecao: {e}")
        
    finally:
        driver.quit()
