# Navegação
driver.get("https://example.com")   # Abre URL
driver.back()                       # Volta
driver.forward()                    # Avança
driver.refresh()                    # Atualiza página

# Localização de elementos
from selenium.webdriver.common.by import By
driver.find_element(By.ID, "id")
driver.find_element(By.NAME, "name")
driver.find_element(By.CLASS_NAME, "class")
driver.find_element(By.CSS_SELECTOR, "css")
driver.find_element(By.XPATH, "//xpath")

# Interações
element.click()                     # Clicar
element.send_keys("texto")          # Digitar
element.clear()                     # Limpar campo

# Informaçõe de elementos
element.text                       # Texto visível
element.get_attribute("value")     # Valor de atributo
element.is_displayed()             # Está visível?
element.is_enabled()               # Está habilitado?
element.is_selected()              # Está selecionado?

# Select (dropdown)
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.ID, "dropdown"))
select.select_by_visible_text("Option")   # Seleciona pelo texto
select.select_by_value("1")               # Seleciona pelo value
select.select_by_index(0)                 # Seleciona pelo índice

#ActionChains (ações avançadas)
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.move_to_element(element).perform()      # Hover (mouse over)
actions.click(element).perform()                # Clique
actions.double_click(element).perform()         # Duplo clique
actions.context_click(element).perform()        # Clique direito
actions.drag_and_drop(source, target).perform() # Drag and drop

# Esperas (waits)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located(locator))
wait.until(EC.element_to_be_clickable(locator))
wait.until(EC.url_contains("home"))

# Alertas
driver.switch_to.alert.text                    # Pega texto do alerta
driver.switch_to.alert.accept()                # Aceita o alerta
driver.switch_to.dismiss()                     # Descarta o alerta
driver.switch_to.send_keys("Selenium")         # Envia texto para o prompt

# Janelas / Abas
driver.current_window_handle       # Aba atual
driver.window_handles              # Todas as abas
driver.switch_to.window(handle)    # Trocar aba

# Frames
driver.switch_to.frame("frame")    # Entrar no frame
driver.switch_to.default_content() # Voltar ao conteúdo principal

# Javascript
driver.execute_script("window.scrollTo(0, 500)")

# Encerramento
driver.close()                     # Fecha aba atual
driver.quit()                      # Fecha navegador
