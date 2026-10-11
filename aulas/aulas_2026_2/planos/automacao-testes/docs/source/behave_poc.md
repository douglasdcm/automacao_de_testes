# Behave PoC

## Objetivo
Validar uso de BDD com Behave reutilizando Pages.

## Estratégia
- Não usar Transactions
- Steps chamam diretamente Pages

## Execução
pytest -k behave

## Estrutura
tests/features/

## Limitações
- Duplication de lógica (temporária)
- Não substitui specs ainda