# Configuração inicial
- Crie e ative um ambiente virtual
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
# Execução dos testes
```
cd ferramentas/behave_gherkin/
behave
```
Saída
```
Feature: Fight or flight # features/ninja.feature:1
  In order to increase the ninja survival rate,
  As a ninja commander
  I want my ninjas to decide whether to take on an
  opponent based on their skill levels
  Scenario: Weaker opponent                      # features/ninja.feature:7
    Given the ninja has a third level black-belt # features/steps/ninja.py:4 0.000s
    When attacked by a samurai                   # features/steps/ninja.py:11 0.000s
    Then the ninja should engage the opponent    # features/steps/ninja.py:18 0.000s

  Scenario: Stronger opponent                    # features/ninja.feature:12
    Given the ninja has a third level black-belt # features/steps/ninja.py:4 0.000s
    When attacked by Chuck Norris                # features/steps/ninja.py:23 0.000s
    Then the ninja should run for his life       # features/steps/ninja.py:30 0.000s

1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.001s

```
# Referências
- [Tutorial](https://behave.readthedocs.io/en/latest/tutorial/)