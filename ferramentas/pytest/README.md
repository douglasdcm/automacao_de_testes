# Configuração inicial
- Crie e ative um ambiente virtual
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Caso queira sair do ambiente virtual
```
deactivate
```
# Passo a passo para instalação com exemplos
 - https://docs.pytest.org/en/stable/getting-started.html

# Execução e report
```
python -m pytest
============================================================ test session starts =============================================================
platform linux -- Python 3.11.3, pytest-8.2.2, pluggy-1.5.0
rootdir: /home/douglas/repo/automacao_de_testes
collected 2 items                                                                                                                            

ferramentas/pytest/test_sample.py F                                                                                                    [ 50%]
ferramentas/selenium/test_selenium.py .                                                                                                [100%]

================================================================== FAILURES ==================================================================
________________________________________________________________ test_answer _________________________________________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

ferramentas/pytest/test_sample.py:7: AssertionError
========================================================== short test summary info ===========================================================
FAILED ferramentas/pytest/test_sample.py::test_answer - assert 4 == 5
======================================================== 1 failed, 1 passed in 9.32s =========================================================
```