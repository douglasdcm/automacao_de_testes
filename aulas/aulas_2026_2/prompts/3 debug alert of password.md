Atue como um Engenheiro de QA Sênior e Especialista em Depuração de Código. Analise o erro descrito abaixo e forneça um diagnóstico detalhado.

### 1. CONTEXTO DO ERRO
*   **Linguagem/Framework:** Python 3.11+, Selenium Webdriver, Pytest, Page Objects, Page Transactions (Guará Python Framework)
*   **Tecnologias/Bibliotecas envolvidas:** Linux Ubuntu, VSCode, GitHub, Git, Google Chrome (Version 149.0.7827.155 (Official Build) (64-bit))
*   **Ambiente:** Local, Sauce Demo (https://www.saucedemo.com)

### 2. O PROBLEMA
*   **O que deveria acontecer:** Quando executo um script Selenium para fazer o checkout de um produto a compra deveria ser concluída sem alertas ou prompts.
*   **O que está acontecendo:** Quando executo um script Selenium para fazer o checkout de um produto um alerta é exibido com a mensagem descrita abaixo.

### 3. ARTEFATOS (LOGS E CÓDIGO)
*   **Mensagem de Erro / Stack Trace:**
    ```
    Change your password

    The password you just used was found in a data breach. Google Password Manager recommends changing your password now.
    ```
*   **Trecho de Código Relevante:**
    ```
    driver.find_element(By.ID, "first-name").send_keys("Douglas")
    driver.find_element(By.ID, "last-name").send_keys("Teste")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()
    ```

### 4. O QUE VOCÊ DEVE FORNECER:
1. **Causa Raiz:** Explique de forma simples por que o erro acontece.
2. **Correção do Código:** Forneça o trecho de código corrigido com comentários explicativos.
3. **Estratégia de Teste:** Sugira um caso de teste (unitário ou de integração) para garantir que este erro não volte a acontecer (Regression Testing).
4. **Boas Práticas:** Uma dica rápida para evitar esse tipo de falha no futuro.
