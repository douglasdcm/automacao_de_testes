# Arquitetura do Framework de Testes

Este documento descreve a arquitetura adotada no framework de automação de testes, com foco em escalabilidade, reutilização e separação de responsabilidades.

A arquitetura segue o padrão:

Test (Spec) → Transaction → Page

---

## 1. Visão Geral do Fluxo

O fluxo de execução de um teste deve seguir a ordem:

1. Test (Spec) inicia o cenário
2. Transaction executa o fluxo de negócio
3. Page realiza interações com a interface

Representação:

Test → Transaction → Page → UI (Sistema)

---

## 2. Responsabilidades por Camada

### 2.1 Test (Spec)

#### Objetivo
Validar o comportamento do sistema

#### Responsabilidades
- Definir o cenário de teste
- Orquestrar execution usando Transactions
- Realizar assertions
- Utilizar fixtures (driver, dados, etc)

#### Regras
- Não conter lógica de negócio
- Não acessar Page diretamente
- Ser simples e legível

#### Exemplo conceitual

```python
from guara.application import Application
from guara import it

from tests.transactions.login_transaction import LoginTransaction
from tests.fixtures.driver import driver

def test_checkout(driver):

    app = Application(driver)

    app.given(
        LoginTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")
```

***

### 2.2 Transaction

#### Objetivo

Implementar fluxos de negócio reutilizáveis

#### Responsabilidades

* Coordenar múltiplas ações
* Encapsular regras de negócio
* Interagir com uma ou mais Pages
* Retornar resultados relevantes para validação

#### Regras

* Pode conter lógica condicional
* Pode chamar várias Pages
* Não deve conter assertions
* Deve ser reutilizável

#### Exemplo conceitual

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

***

### 2.3 Page Object

#### Objetivo

Encapsular interação com elementos da interface

#### Responsabilidades

* Definir localizadores
* Executar ações na UI
* Isolar mudanças do front-end

#### Regras

* Não conter lógica de negócio
* Não conter validações de teste
* Não conter regras de fluxo

#### Exemplo conceitual

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
```

***

## 3. Regras de Dependência

As camadas devem respeitar a seguinte hierarquia:

* Test depende de Transaction
* Transaction depende de Page
* Page depende apenas do WebDriver

Proibido:

* Test acessar Page diretamente
* Page depender de Transaction
* Transaction depender de Test

***

## 4. Benefícios da Arquitetura

* Separação clara de responsabilidades
* Alta reutilização de código
* Facilidade de manutenção
* Escalabilidade para múltiplas equipes
* Redução de duplicação

***

## 5. Boas práticas obrigatórias

* Cada teste deve validar apenas um comportamento
* Fluxos devem sempre ser encapsulados em Transactions
* Pages devem ser genéricas e reutilizáveis
* Dados devem ser externos ao código

***

## 6. Erros comuns (evitar)

* Lógica de fluxo dentro do Test
* Assertions dentro de Page
* Dados hardcoded
* Repetição de fluxo entre testes

***

## 7. Conclusão

A arquitetura Test → Transaction → Page deve ser seguida rigorosamente para garantir padronização, escalabilidade e qualidade no projeto.

Qualquer desvio deste padrão deve ser revisado antes da aprovação do código.

