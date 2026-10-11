import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_actionchains_acoes_avancadas():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    actions = ActionChains(driver)
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        
        input_texto = driver.find_element(By.ID, "my-text-id")
        botao_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
        checkbox = driver.find_element(By.ID, "my-check-2")
        range_slider = driver.find_element(By.NAME, "my-range")
        
        actions.move_to_element(input_texto).perform()
        assert input_texto.is_displayed()
        
        actions.click(checkbox).perform()
        assert checkbox.is_selected()
        
        actions.double_click(input_texto).perform()
        assert input_texto.is_displayed()
        
        actions.context_click(botao_submit).perform()
        assert botao_submit.is_displayed()
        
        actions.drag_and_drop(range_slider, input_texto).perform()
        assert range_slider.is_displayed()
        
    except Exception as e:
        pytest.fail(f"O teste falhou devido a uma excecao: {e}")
        
    finally:
        driver.quit()
