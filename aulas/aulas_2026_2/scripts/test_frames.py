import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_frames():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://douglasdcm.github.io/aulas/")
        iframe_element = driver.find_element(By.TAG_NAME, "iframe")
        
        driver.find_element(By.ID, "load-iframe-btn").click()
        driver.switch_to.frame(iframe_element)
        assert driver.find_element(By.CSS_SELECTOR, "h3").text == "IFrame Content Loaded"
        
        corpo_iframe = driver.find_element(By.TAG_NAME, "body")
        assert corpo_iframe.is_displayed()
        
        driver.switch_to.default_content()
        
        titulo_principal = driver.find_element(By.TAG_NAME, "h1")
        assert titulo_principal.text == "Selenium Test Automation Training Page"
        
    except Exception as e:
        pytest.fail(f"O teste falhou devido a uma excecao: {e}")
        
    finally:
        driver.quit()
