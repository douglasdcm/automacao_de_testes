# Como criar Transações

# Sumário

1. Introdução  
1.1 Objetivo  
1.2 Escopo  
2. Localização na Estrutura do Projeto  
3. Conceito de Page Transactions Pattern  
4. Passo a Passo para Criar uma Transaction  
4.1 Criar o arquivo da Transaction  
4.2 Definir a classe e herança  
4.3 Implementar o método do  
4.4 Utilizar Pages dentro da Transaction  
4.5 Retorno de resultados  
5. Estrutura Recomendada de uma Transaction  
6. Exemplo Completo  
7. Boas Práticas  
8. Anti-Patterns  
9. Integração com Testes (Spec)  
10. Checklist de Validação  
11. Referências e Links Úteis  

# 1. Introdução

## 1.1 Objetivo

Este documento descreve o processo padronizado para criação de classes utilizando o padrão Page Transactions no framework de automação baseado em Python, Selenium, Pytest e Guará.

## 1.2 Escopo

Aplica-se a todas as implementações de fluxo de negócio nos testes automatizados, sendo obrigatório para equipes que contribuem com o projeto.

# 2. Localização na Estrutura do Projeto

As Transactions devem ser criadas no diretório:

```
tests/transactions/
```

Exemplo de arquivos existentes:

```
login_transaction.py
add_to_cart_transaction.py
checkout_transaction.py
finish_order_transaction.py
```

# 3. Conceito de Page Transactions Pattern

O padrão Page Transactions define uma camada intermediária responsável por:

- Orquestrar fluxos de negócio
- Reutilizar múltiplas Pages
- Encapsular regras de execução
- Permitir alta reutilização entre testes

Fluxo arquitetural:

```
Test (Spec) → Transaction → Page
```

# 4. Passo a Passo para Criar uma Transaction

## 4.1 Criar o arquivo da Transaction

Criar um novo arquivo seguindo a convenção:

```
\*\_transaction.py
```

Exemplo:

```
login_transaction.py
````

## 4.2 Definir a classe e herança

Todas as Transactions devem:

- Herdar de AbstractTransaction
- Seguir convenção de nomenclatura

Exemplo:

```python
from guara.transaction import AbstractTransaction

class LoginTransaction(AbstractTransaction):
    pass
````

## 4.3 Implementar o método `do`

O método `do` é obrigatório e define o fluxo principal.

Características:

* Define os passos da execução
* Recebe parâmetros necessários
* Pode chamar múltiplas Pages

Exemplo:

```python
def do(self, url, user, password):
    self._driver.get(url)
```

## 4.4 Utilizar Pages dentro da Transaction

Importar e utilizar as Pages necessárias:

```python
from tests.pages.login_page import LoginPage
```

Instanciar Page:

```python
page = LoginPage(self._driver)
```

Executar ações:

```python
page.login(user, password)
```

## 4.5 Retorno de resultados

A Transaction deve retornar dados relevantes para validação no teste.

Exemplo:

```python
return self._driver.current_url
```

# 5. Estrutura Recomendada de uma Transaction

Modelo padrão:

```python
from guara.transaction import AbstractTransaction
from tests.pages.nome_page import NomePage

class NomeTransaction(AbstractTransaction):

    def do(self, parametros):
        page = NomePage(self._driver)

        page.acao()

        return resultado
```

# 6. Exemplo Completo

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

# 7. Boas Práticas

* Centralizar fluxos reutilizáveis
* Utilizar múltiplas Pages quando necessário
* Retornar informações relevantes para validação
* Manter métodos organizados e legíveis
* Evitar duplicação de fluxo
* Nomear claramente a Transaction

# 8. Anti-Patterns

Não implementar:

## Assertions dentro da Transaction

```python
# ERRADO
assert "inventory" in self._driver.current_url
```

## Lógica de validação

Validações devem ser feitas no Test.

## Acesso direto no Test sem Transaction

```python
# ERRADO
page.login()
```

## Duplicação de fluxo

Fluxos repetidos devem ser extraídos para uma Transaction.

# 9. Integração com Testes (Spec)

As Transactions devem ser utilizadas dentro dos testes.

Exemplo com Guará:

```python
from guara.application import Application
from guara import it

from tests.transactions.login_transaction import LoginTransaction

def test_login(driver):

    app = Application(driver)

    app.given(
        LoginTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(it.Contains, "inventory")
```

# 10. Checklist de Validação

Antes de criar ou aprovar uma Transaction:

* A classe herda de AbstractTransaction
* Método do está implementado
* Não há assertions
* Fluxo está reutilizável
* Não há lógica de validação
* Utiliza Page Objects corretamente
* Nome segue padrão \*\_transaction.py

# 11. Referências e Links Úteis

* Guará Framework Tutorial: <https://guara.readthedocs.io/en/latest/TUTORIAL_TESTING.html>
