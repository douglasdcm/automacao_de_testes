import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_interacoes():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        
        campo_texto = driver.find_element(By.ID, "my-text-id")
        campo_texto.clear()
        campo_texto.send_keys("Selenium Webdriver")
        assert campo_texto.get_attribute("value") == "Selenium Webdriver"
        
        campo_texto.clear()
        assert campo_texto.get_attribute("value") == ""
        
        botao_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
        botao_submit.click()
        
    except Exception as e:
        pytest.fail(f"O teste falhou devido a uma excecao: {e}")
        
    finally:
        driver.quit()
