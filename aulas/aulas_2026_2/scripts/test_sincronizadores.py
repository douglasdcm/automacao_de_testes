from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_sincronizadores():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    try:
        driver.get("https://douglasdcm.github.io/aulas/")

        button = driver.find_element(By.ID, "ajax-btn")
        button.click()
        
        wait = WebDriverWait(driver, timeout=10)
        wait.until(lambda d: "AJAX content loaded at" in d.find_element(By.ID, "ajax-content").text)
        
    except Exception as e:
        print(f"Erro no teste: {e}")
        raise e
    finally:
        driver.quit()
