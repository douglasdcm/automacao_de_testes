from selenium import webdriver
import time

def test_navegacao():
    # Inicializa o ChromeDriver automaticamente
    driver = webdriver.Chrome()

    try:
        # 1. Abre a URL inicial
        driver.get("https://example.com")
        time.sleep(2)  # Pausa apenas para você visualizar a ação

        # 2. Navega para uma segunda página (necessário para testar o 'back')
        driver.get("https://google.com")
        time.sleep(2)

        # 3. Volta para a página anterior (example.com)
        driver.back()
        print("Voltou para:", driver.current_url)
        time.sleep(2)

        # 4. Avança novamente (google.com)
        driver.forward()
        print("Avançou para:", driver.current_url)
        time.sleep(2)

        # 5. Atualiza a página atual
        driver.refresh()
        print("Página atualizada!")
        time.sleep(2)

    finally:
        # Fecha o navegador e encerra o processo
        driver.quit()
