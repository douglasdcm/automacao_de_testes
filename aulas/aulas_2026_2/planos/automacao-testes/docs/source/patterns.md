# Test Automation Patterns

Este documento define os padrões obrigatórios para desenvolvimento de testes automatizados no projeto.

# 1. Arquitetura Geral

A automação deve seguir a separação de responsabilidades:

```
Test (Spec) → Transaction → Page Object
````

### Responsabilidades

| Camada | Responsabilidade |
|--------|-----------------|
| Test | Validação e orquestração |
| Transaction | Regras de fluxo de negócio |
| Page | Interação com UI |


# 2. Page Object Pattern

## Objetivo
Encapsular interações com elementos da interface.

## Regras

- Nunca conter lógica de negócio
- Nunca conter validações de teste
- Deve conter apenas:
  - Localizadores
  - Ações
  - Métodos reutilizáveis

## Exemplo

```python
class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def preencher_usuario(self, usuario):
        self.driver.find_element(...).send_keys(usuario)

    def preencher_senha(self, senha):
        self.driver.find_element(...).send_keys(senha)

    def clicar_login(self):
        self.driver.find_element(...).click()
````



# 3. Transaction Pattern

## Objetivo

Centralizar fluxos de negócio reutilizáveis.



## Regras

* Toda lógica de fluxo deve ficar na Transaction
* Pode chamar múltiplas páginas
* Pode conter regras condicionais
* Retornar resultados quando necessário



## Exemplo

```python
from guara.transaction import AbstractTransaction
from tests.pages.login_page import LoginPage

class LoginTransaction(AbstractTransaction):

    def do(self, url, user, password):
        self._driver.get(url)

        page = LoginPage(self._driver)
        page.login(user, password)

        return self._driver.current_url
```



# 4. Test (Spec) Pattern

## Objetivo

Validar comportamento do sistema



## Regras

* Deve ser simples e legível
* Não deve conter lógica complexa
* Usar padrão Page Transactions:



## Exemplo

```python
from guara.application import Application
from selenium import webdriver
from guara import it

from tests.transactions.login_transaction import LoginTransaction
from tests.transactions.add_to_cart_transaction import AddToCartTransaction
from tests.transactions.checkout_transaction import CheckoutTransaction
from tests.transactions.finish_order_transaction import FinishOrderTransaction
from tests.fixtures.driver import driver
def test_checkout(driver):

    app = Application(driver)

    app.given(
        LoginTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")

    app.when(
        AddToCartTransaction
    ).asserts(it.Contains, "cart")

    app.when(
        CheckoutTransaction,
        name="Douglas",
        last="Teste",
        zip_code="12345"
    ).asserts(it.Contains, "checkout-step-two")

    app.when(
        FinishOrderTransaction
    ).asserts(it.Contains, "Thank you")
```

# 5. Naming Conventions (OBRIGATÓRIO)

| Tipo               | Padrão                      |
| ------------------ | --------------------------- |
| Arquivo de teste   | test\_\*.py                 |
| Page Object        | \*\_page.py                 |
| Transaction        | \*\_transaction.py          |
| Dados              | \*\_data.json ou \*.yaml    |
| Classe Page        | NomePaginaPage              |
| Classe Transaction | NomeFluxoTransaction        |
| Testes             | test\_\[ação]\_\[resultado] |


## Exemplos

* test\_login\_sucesso.py
* login\_page.py
* login\_transaction.py
* login\_data.json

# 6. Anti-Patterns (PROIBIDO)

## Lógica dentro do teste

```python
# ERRADO
if usuario_valido:
    fazer_login()
```
## Teste chamando Page diretamente

```python
# ERRADO
page.preencher_usuario("user")
```

Correto:

```python
app.when(
        FinishOrderTransaction
    ).asserts(it.Contains, "Thank you")
```

## Dados hardcoded

```python
# ERRADO
login("admin", "123")
```

Correto:

```python
login_data["admin"]
```

## Duplicação de código

* Nunca repetir fluxo
* Sempre criar Transaction

## Assertions dentro de Page

```python
# ERRADO
assert elemento_visivel
```
