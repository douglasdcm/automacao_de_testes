# Como gerar logs amigáveis

# Sumário

1. Introdução  
1.1 Objetivo  
1.2 Escopo  
2. Visão Geral do Allure Report  
3. Requisitos e Setup do Ambiente  
3.1 Instalação de dependências Python  
3.2 Instalação do Allure CLI  
3.3 Configuração do projeto  
4. Geração de Logs com Allure  
4.1 Execução dos testes com geração de resultados  
4.2 Geração do relatório  
4.3 Abertura do relatório  
5. Navegação nos Logs do Allure  
5.1 Dashboard  
5.2 Seção de testes  
5.3 Histórico de execução  
5.4 Anexos e evidências  
6. Estrutura dos Logs do Allure  
6.1 Test Suites  
6.2 Passos (Steps)  
6.3 Fixtures  
6.4 Anexos (Attachments)  
6.5 Status dos testes  
7. Integração com o Framework Atual  
8. Boas práticas para geração de logs  
9. Checklist de validação  
10. Referências e Links Úteis  

# 1. Introdução

## 1.1 Objetivo

Este documento descreve o processo padronizado para geração de logs amigáveis utilizando Allure Report em testes automatizados com Python, Pytest, Selenium e Guará.

## 1.2 Escopo

Aplica-se à execução, análise e visualização de resultados de testes automatizados no projeto Sauce Demo.

# 2. Visão Geral do Allure Report

O Allure Report é uma ferramenta de visualização que permite:

- Analisar execuções de testes de forma amigável
- Identificar falhas rapidamente
- Visualizar histórico de execuções
- Inspecionar evidências e logs detalhados

# 3. Requisitos e Setup do Ambiente

## 3.1 Instalação de dependências Python

Adicionar dependência ao projeto:

```bash
pip install allure-pytest
````

Atualizar o arquivo requirements.txt:

```txt
allure-pytest
```

## 3.2 Instalação do Allure CLI

Linux Ubuntu:

```bash
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

Verificar instalação:

```bash
allure --version
```

## 3.3 Configuração do projeto

Certificar que o pytest.ini contém configurações básicas:

```ini
[pytest]
addopts = -v
```

Opcionalmente criar diretório padrão:

```
allure-results/
```

# 4. Geração de Logs com Allure

## 4.1 Execução dos testes com geração de resultados

Executar os testes com flag do Allure:

```bash
python -m pytest --alluredir=allure-results
```

Isso irá gerar arquivos de resultado no diretório:

```
allure-results/
```

## 4.2 Geração do relatório

Gerar o relatório HTML:

```bash
allure generate allure-results -o allure-report
```

## 4.3 Abertura do relatório

Abrir o relatório:

```bash
allure open allure-report
```

# 5. Navegação nos Logs do Allure

## 5.1 Dashboard

Apresenta:

* Total de testes
* Taxa de sucesso
* Testes falhos
* Tempo de execução

## 5.2 Seção de testes

Permite visualizar:

* Lista de testes executados
* Status de cada teste
* Detalhes da execução

## 5.3 Histórico de execução

Mostra:

* Execuções anteriores
* Tendência de falhas
* Estabilidade dos testes

## 5.4 Anexos e evidências

Permite visualizar:

* Prints de tela
* Logs adicionais
* Respostas capturadas

# 6. Estrutura dos Logs do Allure

## 6.1 Test Suites

Agrupamento dos testes por categoria:

* smoke
* regression
* e2e

## 6.2 Passos (Steps)

Representam ações executadas durante o teste.

Exemplo:

* Login
* Adicionar produto
* Finalizar compra

## 6.3 Fixtures

Mostram execução de:

* setup
* teardown
* criação do driver

## 6.4 Anexos (Attachments)

Incluem:

* screenshots
* mensagens de erro
* informações de ambiente

## 6.5 Status dos testes

| Status  | Descrição                   |
| ------- | --------------------------- |
| Passed  | Teste executado com sucesso |
| Failed  | Teste falhou                |
| Skipped | Teste ignorado              |
| Broken  | Erro de execução            |

# 7. Integração com o Framework Atual

Adicionar logs dentro de Transactions ou testes:

```python
import allure

@allure.step("Executando login com usuário")
def login(self, user, password):
    self.page.login(user, password)
```

Adicionar anexos:

```python
allure.attach(
    driver.get_screenshot_as_png(),
    name="screenshot",
    attachment_type=allure.attachment_type.PNG
)
```

# 8. Boas práticas para geração de logs

* Inserir steps claros e descritivos
* Anexar evidências relevantes
* Nomear testes corretamente
* Evitar logs excessivos
* Garantir consistência entre testes
* Utilizar screenshots em falhas

# 9. Checklist de validação

* Allure está instalado corretamente?
* Testes estão gerando arquivos em allure-results?
* Relatório está sendo gerado sem erro?
* Passos estão visíveis no relatório?
* Screenshots estão sendo anexados?
* Logs estão legíveis e organizados?

# 10. Referências e Links Úteis

* Documentação oficial Allure: <https://allurereport.org/docs/>

