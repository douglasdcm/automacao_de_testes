# Sumário

1. Introdução  
1.1 Objetivo do Projeto  
1.2 Escopo  
2. Visão Geral da Arquitetura  
3. Tecnologias Utilizadas  
4. Estrutura do Projeto  
5. Como Executar os Testes  
6. Como Gerar Relatórios  
7. Documentação Técnica do Projeto  
7.1 Arquitetura  
7.2 Padrões de Desenvolvimento  
7.3 Criação de Testes  
7.4 Criação de Pages  
7.5 Criação de Transactions  
7.6 Estratégia de Logs  
7.7 Geração de Documentação  
7.8 Troubleshooting  
7.9 Checklist de PR  
8. Contribuição com o Projeto  
9. Incentivo à Comunidade  
10. Referências e Links Úteis  

# 1. Introdução

## 1.1 Objetivo do Projeto

Este projeto tem como objetivo demonstrar uma arquitetura profissional para automação de testes WEB UI utilizando Selenium, PyTest e o padrão Page Transactions aplicado através do framework Guará.

A solução foi construída com foco em:

- Escalabilidade
- Reutilização de código
- Padronização entre equipes
- Facilidade de manutenção
- Qualidade dos testes automatizados

## 1.2 Escopo

O projeto automatiza fluxos básicos do sistema Sauce Demo, incluindo:

- Login
- Adição de produtos ao carrinho
- Fluxo completo de checkout

# 2. Visão Geral da Arquitetura

A arquitetura segue o padrão:

Test → Transaction → Page

- Test: define o cenário e valida resultados
- Transaction: executa o fluxo de negócio
- Page: interage com a interface

Esse modelo garante isolamento de responsabilidades e alta reutilização.

# 3. Tecnologias Utilizadas

| Tecnologia | Descrição |
|----------|----------|
| Python | Linguagem principal |
| PyTest | Framework de testes |
| Selenium | Automação WEB |
| Guará Framework | Orquestração de testes |
| Page Objects | Abstração da UI |
| Page Transactions | Reutilização de fluxos |
| Allure Report | Geração de relatórios |
| Sphinx | Documentação técnica |

# 4. Estrutura do Projeto

Principais diretórios:

```
tests/
docs/
allure-results/
allure-report/
````

- tests: código de automação
- docs: documentação técnica em Sphinx
- allure-results: resultados de execução
- allure-report: relatório gerado

# 5. Como Executar os Testes

Criar o ambiente virtual:

```
python3.11 -m venv venv
```

Ativar o ambiente virtual:

```bash
source venv/bin/activate
````

Executar testes:

```bash
python -m pytest -v
```

Executar com geração de logs Allure:

```bash
python -m pytest --alluredir=allure-results
```

# 6. Como Gerar Relatórios

Gerar relatório Allure:

```bash
allure generate allure-results -o allure-report
```

Abrir relatório:

```bash
allure open allure-report
```

# 7. Documentação Técnica do Projeto

A documentação completa está disponível na pasta:

```
docs/source/
```

## 7.1 Arquitetura

Descrição da arquitetura do framework, incluindo fluxo entre camadas e responsabilidades.

Arquivo:

```
docs/source/architecture.md
```

## 7.2 Padrões de Desenvolvimento

Define regras obrigatórias como naming conventions, separação de responsabilidades e anti-patterns.

Arquivo:

```
docs/source/patterns.md
```

## 7.3 Criação de Testes

Guia prático para criação de testes utilizando Page Transactions, fixtures e PyTest.

Arquivo:

```
docs/source/how_to_create_test.md
```

## 7.4 Criação de Pages

Explica como implementar classes utilizando Page Objects Model.

Arquivo:

```
docs/source/how_to_create_page.md
```

## 7.5 Criação de Transactions

Guia para construção de fluxos reutilizáveis com o padrão Page Transactions.

Arquivo:

```
docs/source/how_to_create_transaction.md
```

## 7.6 Estratégia de Logs

Explica como gerar logs estruturados e relatórios com Allure.

Arquivo:

```
docs/source/how_to_generate_logs.md
```

## 7.7 Geração de Documentação

Passo a passo para gerar documentação técnica com Sphinx.

Arquivo:

```
docs/source/how_to_generate_documentation.md
```

## 7.8 Troubleshooting

Guia para depuração de erros e identificação de problemas no framework.

Arquivo:

```
docs/source/troubleshooting.md
```

## 7.9 Checklist de PR

Checklist obrigatório para garantir qualidade nas contribuições.

Arquivo:

```
docs/source/pr_checklist.md
```

# 8. Contribuição com o Projeto

Contribuições são bem-vindas e incentivadas.

Para contribuir:

1. Criar uma branch a partir da main
2. Implementar alterações seguindo os padrões definidos
3. Garantir que todos os testes passem
4. Submeter Pull Request

É obrigatório:

* Seguir patterns.md
* Não violar arquitetura definida
* Garantir reuso com Transactions
* Manter testes desacoplados

# 9. Incentivo à Comunidade

Caso este projeto seja útil:

* Marque uma estrela no repositório no GitHub
* Compartilhe com sua equipe
* Contribua com melhorias
* Sugira novas funcionalidades

O crescimento do projeto depende da colaboração da comunidade.

# 10. Referências e Links Úteis

* Documentação Selenium: <https://www.selenium.dev/documentation/>
* Documentação PyTest: <https://docs.pytest.org>
* Allure Report: <https://allurereport.org/docs/>
* Sphinx Documentation: <https://www.sphinx-doc.org>
* Guará Framework: <https://guara.readthedocs.io/en/latest/>
