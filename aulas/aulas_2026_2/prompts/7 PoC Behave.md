Atue como um Arquiteto de Testes de Software e Engenheiro de QA Sênior. 

Com base no Código (C) e no Problema (P) monte um plano de ação para o Contexto do Projeto (PJ) de modo que eu possa copiar as tarefas em um agente de IA especialidado em testes de software.

**Nota:** O agente de IA não possui acesso ao código fonte. Monte o plano de forma detalhada para que eu possa executar as tarefas manualmente.

### 1. CONTEXTO
*   **Linguagem/Framework:** Python 3.11+, Selenium Webdriver, Pytest, Page Transactions Pattern (Guará Python Framework), GitHub Actions, Python Behave
*   **Tecnologias/Bibliotecas envolvidas:** Linux Ubuntu, VSCode, GitHub, Git
*   **Ambiente:** GitHUb Actions

### 2. P
*   **Problema a ser resolvido:** A equipe precisa apresentar uma prova de conceito (PoC) para o uso de Python Behave. Os testes existentes serão usado como base. Como reescrever os testes em BDD sem modificá-los? 	

### 3. PJ
*   **Especificação da tarefa:** Utilização do Python Behave para escrita dos testes. Os testes seguem o padrão Test (spec) -> Transactions -> Page Objects. A ideia é reaproveitar as Pages e substituir as Transactios por cenários escritos em BDD usando Python Behave.

* VOCÊ DEVE:
- Listar os arquivos novos a serem criados incluindo arquivos de documentação
- Detalhar as novas configurações necessárias para fazer o setup do Python Behave
- Detalhar as configuraçõe necessárias para executar os novos testes no GitHub Actions
- Detalhar como o agente deve portar a fixture do Pytest para o ciclo de vida do Behave (before_all, before_scenario, after_scenario)
- Detalhar onde a pasta `features` deve nascer. Dentro de tests/ ou na raiz do projeto? Como ela vai conviver com a pasta specs atual durante a PoC?
- A PoC deve usar o Behave integrar o Behave ao Pytest (pytest-behave) para reaproveitar relatórios e plugins já existentes no pyproject.toml
- Fazer perguntas quando alguma informação estiver faltando para tomar decisão

** NÃOS:
* NÃO modificar o códig existente
* NÃO halucinar quando não tiver certeza de algo. Pergunte antes de inventar soluções.

### 4. C
*   **Código fonte / Estrutura de pastas do projeto:**

```
tree -I venv -I __pycache__
.
├── pyproject.toml
├── pytest.ini
├── README.md
├── requirements.txt
└── tests
    ├── assertions
    │   └── custom_assertions.py
    ├── config
    │   └── settings.py
    ├── data
    │   ├── data_loader.py
    │   ├── dynamic
    │   ├── factories
    │   │   └── user_factory.py
    │   ├── schemas
    │   └── static
    │       └── login_data.json
    ├── docs
    │   ├── architecture.md
    │   ├── data_strategy.md
    │   ├── how_to_create_page.md
    │   ├── how_to_create_test.md
    │   ├── how_to_create_transaction.md
    │   ├── patterns.md
    │   ├── pr_checklist.md
    │   └── troubleshooting.md
    ├── fixtures
    │   ├── data_fixture.py
    │   └── driver.py
    ├── hooks
    ├── __init__.py
    ├── pages
    │   ├── base_page.py
    │   ├── cart_page.py
    │   ├── checkout_page.py
    │   ├── inventory_page.py
    │   └── login_page.py
    ├── specs
    │   ├── e2e
    │   ├── regression
    │   ├── smoke
    │   ├── test_checkout.py
    │   └── test_login.py
    ├── transactions
    │   ├── add_to_cart_transaction.py
    │   ├── checkout_transaction.py
    │   ├── finish_order_transaction.py
    │   └── login_transaction.py
    └── utils

19 directories, 31 files
```

### 5. O QUE VOCÊ DEVE FORNECER:
1. **Plano detalhado:** Cada passo de fornecer os detalhes para ser executado manualmente.
2. **Sumário:** Explique em linhas gerais como o plano foi desenvolvido.
3. **Boas práticas:** Sugira melhorias para interações futuras.

