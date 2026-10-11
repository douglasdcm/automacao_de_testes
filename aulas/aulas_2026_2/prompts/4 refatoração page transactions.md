Atue como um Arquiteto de Testes de Software e Engenheiro de QA Sênior. 

Com base no Código (C) e no Problema (P) monte um plano de ação para o Contexto do Projeto (PJ) de modo que eu possa copiar as tarefas em um agente de IA especialidado em testes de software.

**Nota:** O agente de IA não possui acesso ao código fonte. Monte o plano de forma detalhada para que eu possa executar as tarefas manualmente.

### 1. CONTEXTO
*   **Linguagem/Framework:** Python 3.11+, Selenium Webdriver, Pytest, Page Transactions Pattern (Guará Python Framework)
*   **Tecnologias/Bibliotecas envolvidas:** Linux Ubuntu, VSCode, GitHub, Git
*   **Ambiente:** Local

### 2. P
*   **Problema a ser resolvido:** Os primeiros testes funcionam, mas qualquer alteração na interface quebra diversos scripts. Como construir uma automação escalável e de fácil manutenção?	

### 3. PJ
*   **Especificação da tarefa:** Refatoração completa utilizando Page Transactions Pattern (Guará Python Framework), separando páginas, elementos e responsabilidades. Organização da estrutura do framework seguindo boas práticas de arquitetura. Exemplo de Page Transactions Pattern:

** Canonical implementation

This is the simplest implementation to warm up the framework. It uses the OpenApp and CloseApp transactions to open the web page of Google, to assert the title of the page is Google and to close the web application.

```
# test_guara.py

from guara import it
from guara.transaction import Application, AbstractTransaction
from selenium import webdriver


class OpenApp(AbstractTransaction):
    def do(
        self, url: str,
    ) -> str:
        self._driver.get(url)
        return self._driver.title


class CloseApp(AbstractTransaction):
    def do(self) -> None:
        self._driver.quit()


def test_canonical():
    google = Application(webdriver.Chrome())
    google.when(OpenApp, url="http://www.google.com",).asserts(it.IsEqualTo,"Google")
    google.execute(CloseApp)
```

** Basic practical example

This is a basic search of the term “guara” on Google. To follow the steps create the files home.py and test_tutorial.py at the same folder.

```
# home.py

from guara.transaction import AbstractTransaction
from selenium.webdriver.common.by import By


class Search(AbstractTransaction):
    def __init__(self, driver):
        super().__init__(driver)

    def do(self, text):
        # Sends the received text to the textbox in the UI
        self._driver.find_element(By.NAME, "q").send_keys(text)
        
        # Click the button to search
        self._driver.find_element(By.NAME, "btnK").click()
        
        # Waits the next page appears and returns the label of the first tab "All".
        # It will be used by assertions in the next sessions.  
        return self._driver.find_element(
            By.CSS_SELECTOR, ".Ap1Qsc > a:nth-child(1) > div:nth-child(1)"
        ).text
```

```
# test_tutorial.py

import pytest

# Imports the module with the transactions of the Home page
import home

from selenium import webdriver

# Imports the Application to build and run the automation
from guara.application import Application

# Imports the module with the strategies to asset the result
from guara import it

@pytest.fixture
def google():
    # Instantiates the Application to run the automation
    google = Application(webdriver.Chrome())

    # Some interesting things happen here.
    # The framework is used to setup the web application.
    # The method `at` from `app` is the key point here as it
    # receives a transaction (AbstractTransaction) and its `kwargs`.
    # Internally `at` executes the `do` method of the transaction and
    # holds the result in the property `result` which is going to be
    # presented soon.
    # `OpenApp` is a concrete transaction.
    # The `url` is passed to the `at` method by `kwargs`.
    # The result returned by `at` is asserted by `asserts`
    # using the strategy `it.IsEqualTo`.
    google.given(
        OpenApp,
        url="http://www.google.com",
    ).then(it.IsEqualTo, "Google")
    yield google

    # Uses the concrete transaction `CloseApp` to close the web application
    google.execute(CloseApp)


def test_google_search(google: Application):
    # With the `app` received from the fixture the similar things
    # explained previously in the fixture happens.
    # The transaction `home.Search` with the parameter `text`
    # is passed to `at` and the result is asserted by `asserts` with
    # the strategy `it.IsEqualTo`
    google.at(home.Search, text="guara").asserts(it.IsEqualTo, "All")
```

### 4. C
*   **Código fonte / Estrutura de pastas do projeto:**

```
tree -I venv -I __pycache__
.
├── pytest.ini
├── requirements.txt
└── tests
    ├── fixtures
    │   └── driver.py
    ├── __init__.py
    ├── specs
    │   ├── test_checkout.py
    │   └── test_login.py
    └── transactions
        └── login_transaction.py

```
---

```
from selenium.webdriver.common.by import By
from tests.fixtures.driver import driver


def test_compra_produto_com_sucesso(driver):

    # =========================
    # 1. LOGIN
    # =========================
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Validação login
    assert "inventory.html" in driver.current_url

    # =========================
    # 2. ADICIONAR PRODUTO
    # =========================
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # =========================
    # 3. IR PARA CARRINHO
    # =========================
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    assert "cart.html" in driver.current_url

    # =========================
    # 4. INICIAR CHECKOUT
    # =========================
    driver.find_element(By.ID, "checkout").click()


    assert "checkout-step-one.html" in driver.current_url

    # =========================
    # 5. PREENCHER DADOS
    # =========================
    driver.find_element(By.ID, "first-name").send_keys("Douglas")
    driver.find_element(By.ID, "last-name").send_keys("Teste")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()

    assert "checkout-step-two.html" in driver.current_url

    # =========================
    # 6. FINALIZAR COMPRA
    # =========================
    driver.find_element(By.ID, "finish").click()

    # =========================
    # 7. VALIDAÇÃO FINAL
    # =========================
    mensagem = driver.find_element(By.CLASS_NAME, "complete-header")

    assert mensagem.is_displayed()
    assert "Thank you" in mensagem.text
```

### 5. O QUE VOCÊ DEVE FORNECER:
1. **Plano detalhado:** Cada passo de fornecer os detalhes para ser executado manualmente.
2. **Sumário:** Explique em linhas gerais como o plano foi desenvolvido.
3. **Boas práticas:** Sugira melhorias para interações futuras.

