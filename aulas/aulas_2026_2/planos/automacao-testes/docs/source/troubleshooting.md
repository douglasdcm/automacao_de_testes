# Troubleshooting

# Sumário

1. Introdução  
1.1 Objetivo  
1.2 Escopo  
2. Abordagem Geral de Troubleshooting  
3. Passo a Passo para Depuração de Testes Automatizados  
3.1 Identificar o erro  
3.2 Reproduzir o problema  
3.3 Isolar a causa  
3.4 Validar hipóteses  
3.5 Corrigir e validar  
4. Depuração com print  
4.1 Quando utilizar  
4.2 Exemplos práticos  
5. Depuração com breakpoint()  
5.1 Como utilizar  
5.2 Execução interativa  
5.3 Exemplos práticos  
6. Arquivos relevantes para investigação  
7. Ferramentas úteis para depuração  
8. Boas práticas de depuração  
9. Checklist de investigação  
10. Referências e Links Úteis  

# 1. Introdução

## 1.1 Objetivo

Este documento define um processo padronizado para identificação, análise e correção de falhas em testes automatizados utilizando Python, Selenium, Pytest e o framework Guará.

## 1.2 Escopo

Aplica-se a depuração de:

- Testes falhando
- Problemas de execução
- Erros em Transactions ou Pages
- Problemas com dados de teste
- Falhas de configuração

# 2. Abordagem Geral de Troubleshooting

A depuração deve seguir uma abordagem estruturada:

1. Identificar o erro
2. Reproduzir o problema
3. Isolar a causa
4. Validar hipóteses
5. Corrigir
6. Confirmar a solução

# 3. Passo a Passo para Depuração de Testes Automatizados

## 3.1 Identificar o erro

Executar os testes e analisar o output:

```bash
pytest -v
````

Avaliar:

* Mensagem de erro
* Stack trace
* Arquivo e linha da falha

## 3.2 Reproduzir o problema

Executar apenas o teste com erro:

```bash
pytest tests/specs/test_login.py -v
```

Garantir que o erro é reproduzível.

## 3.3 Isolar a causa

Verificar em qual camada o erro ocorre:

* Test (Spec)
* Transaction
* Page
* Dados
* Configuração

## 3.4 Validar hipóteses

Checar:

* Localizadores inválidos
* Dados incorretos
* Timeout de elementos
* Problemas de carregamento da página

## 3.5 Corrigir e validar

Após ajustar:

```bash
pytest -v
```

Confirmar que o erro não ocorre mais.

# 4. Depuração com print

## 4.1 Quando utilizar

* Verificar valores de variáveis
* Confirmar execução de passos
* Inspecionar dados de entrada

## 4.2 Exemplos práticos

No Test:

```python
def test_login(driver, login_data):
    print(login_data)
```

Na Transaction:

```python
def do(self, url, user, password):
    print("URL:", url)
    print("User:", user)
```

Na Page:

```python
def login(self, user, password):
    print("Preenchendo usuário:", user)
```

# 5. Depuração com breakpoint()

## 5.1 Como utilizar

Inserir no ponto desejado:

```python
breakpoint()
```

## 5.2 Execução interativa

Executar o teste normalmente:

```bash
pytest -v
```

O Python entrará em modo interativo.

Comandos úteis:

| Comando    | Descrição          |
| ---------- | ------------------ |
| n          | Próxima linha      |
| s          | Entrar na função   |
| c          | Continuar execução |
| p variável | Exibir valor       |
| q          | Sair               |

## 5.3 Exemplos práticos

```python
def do(self, url, user, password):
    breakpoint()
    self._driver.get(url)
```

Analisar:

```python
p url
p user
```

# 6. Arquivos relevantes para investigação

Os seguintes arquivos são fontes importantes de diagnóstico:

| Arquivo                                | Responsabilidade              |
| -------------------------------------- | ----------------------------- |
| tests/config/settings.py               | Configuração geral do projeto |
| tests/fixtures/driver.py               | Inicialização do WebDriver    |
| tests/fixtures/data\_fixture.py        | Dados de teste                |
| tests/data/data\_loader.py             | Carregamento de dados         |
| tests/docs/patterns.md                 | Padrões do framework          |
| tests/docs/architecture.md             | Arquitetura do framework      |
| tests/assertions/custom\_assertions.py | Regras de validação           |
| tests/pages/base\_page.py              | Métodos base de interação     |
| pytest.ini                             | Configuração do Pytest        |

# 7. Ferramentas úteis para depuração

## Pytest verbose

```bash
pytest -v
```

## Execução de teste específico

```bash
pytest caminho/do/teste.py
```

## Execução com logs detalhados

```bash
pytest -s
```

## VSCode Debugger

* Usar breakpoints visuais
* Executar modo debug
* Inspecionar variáveis

## Logs do Selenium

Verificar console do navegador e erros de DOM.

## DevTools (Browser)

* Inspecionar elementos
* Validar seletores
* Verificar tempo de carregamento

# 8. Boas práticas de depuração

* Sempre isolar o problema antes de corrigir
* Evitar alterações sem entender a causa
* Validar localizadores no DevTools
* Usar logs de forma controlada
* Remover prints após correção
* Utilizar breakpoint apenas durante análise
* Garantir que testes são determinísticos

# 9. Checklist de investigação

* O erro é reproduzível?
* O localizador está correto?
* O elemento está disponível no momento da interação?
* Os dados estão corretos?
* A Transaction está funcionando isoladamente?
* Existe timeout ou sincronização incorreta?
* O driver foi inicializado corretamente?
* A URL está correta?
* Existe dependência entre testes?

# 10. Referências e Links Úteis

* Selenium WebDriver Documentation: <https://www.selenium.dev/documentation/>
* Pytest Documentation: <https://docs.pytest.org>
* Python Debugging: <https://docs.python.org/3/library/pdb.html>
* Guará Framework: <https://guara.readthedocs.io/en/latest/>
* Chrome DevTools: <https://developer.chrome.com/docs/devtools/>

