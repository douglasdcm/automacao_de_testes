import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_informacoes_de_elementos():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        titulo = driver.find_element(By.CSS_SELECTOR, "h1.display-6")
        assert titulo.text == "Web form"
        
        campo_texto = driver.find_element(By.ID, "my-text-id")
        campo_texto.send_keys("Automação")
        assert campo_texto.get_attribute("value") == "Automação"
        
        botao_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
        assert botao_submit.is_displayed()
        
        campo_desabilitado = driver.find_element(By.NAME, "my-disabled")
        assert not campo_desabilitado.is_enabled()
        
        checkbox_selecionado = driver.find_element(By.ID, "my-check-1")
        assert checkbox_selecionado.is_selected()
        
    except Exception as e:
        pytest.fail(f"O teste falhou devido a uma excecao: {e}")
        
    finally:
        driver.quit()
