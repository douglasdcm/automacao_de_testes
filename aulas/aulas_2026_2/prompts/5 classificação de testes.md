Atue como um Arquiteto de Testes de Software e Engenheiro de QA Sênior. 

Com base no Código (C) e no Problema (P) monte um plano de ação para o Contexto do Projeto (PJ) de modo que eu possa copiar as tarefas em um agente de IA especialidado em testes de software.

**Nota:** O agente de IA não possui acesso ao código fonte. Monte o plano de forma detalhada para que eu possa executar as tarefas manualmente.

### 1. CONTEXTO
*   **Linguagem/Framework:** Python 3.11+, Selenium Webdriver, Pytest, Page Transactions Pattern (Guará Python Framework), GitHub Actions, Python Behave
*   **Tecnologias/Bibliotecas envolvidas:** Linux Ubuntu, VSCode, GitHub, Git
*   **Ambiente:** Local

### 2. P
*   **Problema a ser resolvido:** A empresa deseja priorizar alguns testes para serem executados em diferentes momentos do ciclo de vida de desenvolvimento do produto:
- smoke: testes para verificação de integração frequente de código
- regression: testes para validar funcionalidades integradas e entregues
- end-to-end: teste completo focando em jornadas críticas do usuário final

### 3. PJ
*   **Especificação da tarefa:** Classificar os testes (C) nas categorias smoke, regression e e2e.

### 4. C
*   **Código fonte / Estrutura de pastas do projeto:** 

```
# CENÁRIOS

Funcionalidade: Login de usuário
Cenário: Login com sucesso
Cenário: Login com credenciais inválidas
Cenário: Usuário bloqueado

Funcionalidade: Processo de compra
Cenário: Compra de produto com sucesso

Funcionalidade: Carrinho de compras
Cenário: Adicionar item ao carrinho
Cenário: Remover item do carrinho

Funcionalidade: Ordenação de produtos
Cenário: Ordenar produtos por preço crescente
Cenário: Ordenar produtos por nome

Funcionalidade: Continuação de compras
Cenário: Continuar comprando após adicionar item

Funcionalidade: Validação do checkout
Cenário: Checkout sem preencher dados
Cenário: Checkout parcial

Funcionalidade: Logout
Cenário: Logout com sucesso

Funcionalidade: Resetar estado da aplicação
Cenário: Resetar carrinho

Funcionalidade: Carrinho vazio
Cenário: Acessar carrinho sem itens
```

### 5. O QUE VOCÊ DEVE FORNECER:
1. **Plano detalhado:** Cada passo de fornecer os detalhes para ser executado manualmente.
2. **Sumário:** Explique em linhas gerais como o plano foi desenvolvido.
3. **Boas práticas:** Sugira melhorias para interações futuras.

