import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_localizacao_de_elementos():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html ")
        
        elemento_id = driver.find_element(By.ID, "my-text-id")
        assert elemento_id.is_displayed()
        
        elemento_name = driver.find_element(By.NAME, "my-password")
        assert elemento_name.is_displayed()
        
        elemento_class = driver.find_element(By.CLASS_NAME, "form-control")
        assert elemento_class.is_displayed()
        
        elemento_css = driver.find_element(By.CSS_SELECTOR, "textarea[name='my-textarea']")
        assert elemento_css.is_displayed()
        
        elemento_xpath = driver.find_element(By.XPATH, "//button[@type='submit']")
        assert elemento_xpath.is_displayed()
        
    except Exception as e:
        pytest.fail(f"O teste falhou devido a uma excecao: {e}")
        
    finally:
        driver.quit()
