import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_janelas_abas():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://douglasdcm.github.io/aulas/")
        aba_original = driver.current_window_handle
        assert aba_original is not None
        
        botao_nova_aba = driver.find_element(By.XPATH, "//button[text()='Open New Tab']")
        botao_nova_aba.click()
        
        todas_abas = driver.window_handles
        assert len(todas_abas) > 1
        
        for aba in todas_abas:
            if aba != aba_original:
                driver.switch_to.window(aba)
                break
                
        assert driver.current_window_handle != aba_original
        
        driver.switch_to.window(aba_original)
        assert driver.current_window_handle == aba_original
        
    except Exception as e:
        pytest.fail(f"O teste falhou devido a uma excecao: {e}")
        
    finally:
        driver.quit()
