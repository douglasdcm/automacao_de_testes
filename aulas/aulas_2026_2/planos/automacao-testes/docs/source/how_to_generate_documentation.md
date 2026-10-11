# Como gerar documentação

# Sumário

1. Introdução  
1.1 Objetivo  
1.2 Escopo  
2. Visão Geral do Sphinx  
3. Requisitos para Uso do Sphinx  
4. Instalação e Setup do Ambiente  
4.1 Instalação das dependências  
4.2 Inicialização do Sphinx  
5. Estrutura da Documentação  
6. Configuração do Projeto  
6.1 Ajuste do arquivo conf.py  
6.2 Integração com código Python  
7. Criação de Conteúdo de Documentação  
7.1 Organização dos arquivos .rst  
7.2 Integração com Markdown (opcional)  
8. Geração da Documentação  
8.1 Build HTML  
8.2 Outros formatos  
9. Visualização da Documentação  
9.1 Abrir localmente  
9.2 Servir via HTTP  
10. Boas Práticas  
11. Troubleshooting  
12. Referências e Links Úteis  

# 1. Introdução

## 1.1 Objetivo

Este documento descreve o processo padronizado para geração de documentação técnica utilizando Sphinx no projeto de automação WEB UI baseado no Sauce Demo.

## 1.2 Escopo

Aplica-se à geração e manutenção de documentação técnica do framework de testes, incluindo Pages, Transactions, Testes e padrões arquiteturais.

# 2. Visão Geral do Sphinx

Sphinx é uma ferramenta de documentação que permite:

- Gerar documentação HTML automaticamente
- Integrar código Python com documentação
- Manter documentação versionada
- Facilitar onboarding de novos desenvolvedores

# 3. Requisitos para Uso do Sphinx

| Requisito | Versão recomendada |
|----------|-------------------|
| Python | 3.11+ |
| Sphinx | 7.x |
| pip | atualizado |

# 4. Instalação e Setup do Ambiente

## 4.1 Instalação das dependências

Instalar Sphinx:

```bash
pip install sphinx
````

Instalar suporte a Markdown:

```bash
pip install myst-parser
```

Atualizar requirements.txt:

```txt
sphinx
myst-parser
```

## 4.2 Inicialização do Sphinx

Executar no diretório raiz do projeto:

```bash
sphinx-quickstart docs
```

Respostas recomendadas:

* Separate source and build directories: yes
* Project name: Automação Testes Sauce Demo
* Author: equipe QA
* Use extensions: aceitar padrão

Estrutura gerada:

```
docs/
  source/
  build/
  Makefile
```

# 5. Estrutura da Documentação

Recomendação de organização:

```
docs/source/
├── index.rst
├── architecture.md
├── patterns.md
├── how_to_create_test.md
├── how_to_create_page.md
├── how_to_create_transaction.md
├── troubleshooting.md
```

# 6. Configuração do Projeto

## 6.1 Ajuste do arquivo conf.py

Arquivo:

```
docs/source/conf.py
```

Adicionar suporte a Markdown:

```python
extensions = [
    'myst_parser'
]
```

Adicionar path do projeto:

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
```

## 6.2 Integração com código Python

Permite documentar automaticamente:

* classes
* métodos
* modules

Adicionar:

```python
extensions.append('sphinx.ext.autodoc')
```

# 7. Criação de Conteúdo de Documentação

## 7.1 Organização dos arquivos .rst

Arquivo principal:

```
index.rst
```

Exemplo:

```rst
Documentação do Projeto
=======================

.. toctree::
   :maxdepth: 2

   architecture
   patterns
   how_to_create_test
   how_to_create_page
   how_to_create_transaction
   troubleshooting
```

## 7.2 Integração com Markdown

Renomear arquivos `.md` corretamente e referenciar no toctree:

```rst
.. toctree::
   :maxdepth: 2

   how_to_create_test.md
```

# 8. Geração da Documentação

## 8.1 Build HTML

Executar dentro da pasta `docs`:

```bash
make html
```

Ou:

```bash
sphinx-build -b html source build
```

Resultado:

```
docs/build/index.html
```

## 8.2 Outros formatos

* PDF (com LaTeX)
* EPUB
* JSON

Exemplo:

```bash
sphinx-build -b latex source build
```

# 9. Visualização da Documentação

## 9.1 Abrir localmente

Executar fora da pasta `docs`:

```bash
xdg-open docs/build/index.html
```
ou
```bash
<browser name> docs/build/index.html
```

Ou abrir manualmente no navegador.

## 9.2 Servir via HTTP

```bash
cd docs/build
python -m http.server 8000
```

Acessar:

```
http://localhost:8000
```

# 10. Boas Práticas

* Centralizar documentação em um único diretório
* Manter versionamento junto ao código
* Atualizar documentação a cada alteração relevante
* Usar nomenclatura consistente
* Evitar duplicação de conteúdo
* Documentar fluxos (Transactions) e não apenas código

# 11. Troubleshooting

## Build falha

Verificar:

* extensão instalada
* erros no conf.py
* caminhos incorretos

## Markdown não renderiza

Validar:

```python
'myst_parser'
```

## Documentos não aparecem

Verificar:

* inclusão no toctree
* caminho correto

## ImportError no autodoc

Garantir:

```python
sys.path.insert(0, os.path.abspath('../../'))
```

# 12. Referências e Links Úteis

* Documentação Sphinx: <https://www.sphinx-doc.org>
* MyST Parser: <https://myst-parser.readthedocs.io>

