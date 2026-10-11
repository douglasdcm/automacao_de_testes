# Como criar Pages

# Sumário

1. Introdução  
1.1 Objetivo  
1.2 Escopo  
2. Localização na Estrutura do Projeto  
3. Conceito de Page Objects Model  
4. Passo a Passo para Criar uma Page  
4.1 Criar o arquivo da Page  
4.2 Definir a classe  
4.3 Declarar os localizadores  
4.4 Implementar os métodos de ação  
4.5 Utilizar BasePage  
5. Estrutura Recomendada de uma Page  
6. Exemplo Completo  
7. Boas Práticas  
8. Anti-Patterns  
9. Integração com Transactions  
10. Checklist de Validação   

# 1. Introdução

## 1.1 Objetivo

Este documento descreve o processo padronizado para criação de classes no padrão Page Objects Model no framework de automação baseado em Python, Selenium e Pytest.

## 1.2 Escopo

Aplica-se a todos os desenvolvedores e engenheiros de QA que contribuem com o projeto de automação de testes web UI.

# 2. Localização na Estrutura do Projeto

As Pages devem ser criadas no diretório:

```
tests/pages/
```

Exemplo de arquivos existentes:

```
login_page.py
inventory_page.py
checkout_page.py
cart_page.py
```

# 3. Conceito de Page Objects Model

O padrão Page Objects Model (POM) define uma abstração da interface gráfica onde:

- Cada página da aplicação é representada por uma classe
- Os elementos da interface são definidos como atributos
- As ações são implementadas como métodos
- Não deve existir lógica de negócio nesta camada

# 4. Passo a Passo para criar uma Page

## 4.1 criar o arquivo da Page

Criar um novo arquivo seguindo a convenção:

```
\*\_page.py
```

Exemplo:

```
login_page.py
````

## 4.2 Definir a classe

A classe deve:

- Herdar de BasePage
- Ter nome padronizado

Exemplo:

```python
from .base_page import BasePage

class LoginPage(BasePage):
    pass
````

## 4.3 Declarar os localizadores

Os localizadores devem:

* Ser declarados como constantes da classe
* Utilizar selenium.webdriver.common.by.By
* Seguir padrão maiúsculo

Exemplo:

```python
from selenium.webdriver.common.by import By

USERNAME = (By.ID, "user-name")
PASSWORD = (By.ID, "password")
LOGIN_BTN = (By.ID, "login-button")
```

## 4.4 Implementar os métodos de ação

As Pages devem conter apenas:

* Ações do usuário
* Interações com elementos

Exemplo:

```python
def login(self, user, password):
    self.type(*self.USERNAME, user)
    self.type(*self.PASSWORD, password)
    self.click(*self.LOGIN_BTN)
```

## 4.5 Utilizar BasePage

A BasePage centraliza métodos como:

* click
* type
* wait
* find_element

Nunca utilizar diretamente:

```
driver.find_element
```

Sempre utilizar métodos da BasePage.

# 5. Estrutura Recomendada de uma Page

Modelo padrão:

```python
from selenium.webdriver.common.by import By
from .base_page import BasePage

class NomePage(BasePage):

    # Localizadores
    ELEMENTO_1 = (By.ID, "exemplo")
    ELEMENTO_2 = (By.XPATH, "//input")

    # Ações
    def acao_exemplo(self, valor):
        self.type(*self.ELEMENTO_1, valor)

    def clicar_elemento(self):
        self.click(*self.ELEMENTO_2)
```

# 6. Exemplo Completo

```python
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def login(self, user, password):
        self.type(*self.USERNAME, user)
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)
```

# 7. Boas Práticas

* Nomear classes com clareza (LoginPage, CheckoutPage)
* Centralizar todos os localizadores na classe
* Criar métodos reutilizáveis
* Manter métodos simples e objetivos
* Evitar duplicação de ações
* Utilizar BasePage para abstração

# 8. Anti-Patterns

Não implementar:

## Lógica de negócio

```python
# ERRADO
if usuario_valido:
    self.login()
```

## Assertions

```python
# ERRADO
assert elemento_visivel
```

## Fluxos complexos

Pages não devem conter múltiplas etapas de fluxo.

## Acesso direto ao driver

```python
# ERRADO
self.driver.find_element(...)
```

# 9. Integração com Transactions

As Pages devem ser utilizadas exclusivamente pelas Transactions.

Fluxo correto:

```
Test → Transaction → Page
```

# 10. Checklist de Validação

Antes de criar ou aprovar uma Page:

* A classe herda de BasePage
* Não há lógica de negócio
* Não há assertions
* Os localizadores estão organizados
* Métodos são reutilizáveis
* Não existe acesso direto ao driver
* Nome segue padrão \*\_page.py
