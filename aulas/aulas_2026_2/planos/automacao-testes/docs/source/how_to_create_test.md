# Como Criar Testes no Framework (Guará + Selenium + Pytest)

Este guia descreve como criar testes automatizados seguindo o padrão oficial do projeto.

---

# 1. Estrutura básica de um teste

Os testes devem ser criados dentro de:

```
tests/specs/
````

Organização recomendada:

- smoke/
- regression/
- e2e/

---

# 2. Padrão obrigatório: Page Transactions

Todos os testes devem seguir o padrão:

Test → Transaction → Page

Referência oficial:
https://guara.readthedocs.io/en/latest/TUTORIAL_TESTING.html

---

## 2.1 Como funciona

- Test define o cenário
- Transaction executa o fluxo
- Page interage com a interface

# 3. Uso de Fixtures

## 3.1 O que são fixtures

Fixtures são responsáveis por fornecer dependências para os testes:

* WebDriver
* Dados de teste
* Configurações

***

## 3.2 Fixture de driver

Já existente em:

```
tests/fixtures/driver.py
```

Uso:

```python
def test_exemplo(driver):
    assert driver is not None
```

***

## 3.3 Fixture de dados

Local:

```
tests/fixtures/data_fixture.py
```

Exemplo:

```python
def test_login(login_data, driver):
    dados = login_data["valid_user"]
```

***

## 3.4 Boas práticas com fixtures

* Nunca instanciar driver manualmente no teste
* Sempre usar fixtures
* Não duplicar setup

***

# 4. Uso de Transactions

## 4.1 O que é uma Transaction

Uma Transaction representa um fluxo de negócio reutilizável.

Exemplos:

* Login
* Checkout
* Adição ao carrinho

***

## 4.2 Onde ficam

```
tests/transactions/
```

## 4.4 Quando criar uma nova Transaction

Criar sempre que:

* Houver mais de 2 passos
* Exista repetição entre testes
* Houver lógica de fluxo
