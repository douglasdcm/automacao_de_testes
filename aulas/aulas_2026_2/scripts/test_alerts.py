import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_alertas():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://douglasdcm.github.io/aulas/")
        
        botao_alert = driver.find_element(By.XPATH, "//button[text()='Show Alert']")
        botao_alert.click()
        alerta_simples = driver.switch_to.alert
        assert alerta_simples.text is not None
        alerta_simples.accept()
        
        botao_prompt = driver.find_element(By.XPATH, "//button[text()='Show Prompt']")
        botao_prompt.click()
        alerta_prompt = driver.switch_to.alert
        alerta_prompt.send_keys("Selenium")
        alerta_prompt.accept()
        alerta_prompt = driver.switch_to.alert
        alerta_prompt.accept()

        botao_confirm = driver.find_element(By.XPATH, "//button[text()='Show Confirm']")
        botao_confirm.click()
        alerta_confirm = driver.switch_to.alert
        alerta_confirm.dismiss()
        
    except Exception as e:
        pytest.fail(f"O teste falhou devido a uma excecao: {e}")
        
    finally:
        driver.quit()
