import pytest
from selenium import webdriver

def test_javascript():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://douglasdcm.github.io/aulas/")
        driver.execute_script("window.scrollTo(0, 500)")
        
        scroll_position = driver.execute_script("return window.pageYOffset;")
        assert scroll_position == 500
        
    except Exception as e:
        pytest.fail(f"O teste falhou devido a uma excecao: {e}")
        
    finally:
        driver.quit()
