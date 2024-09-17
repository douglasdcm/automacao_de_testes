# Requisitos:
# - Uma função que divide dois números inteiros e retorna o resultado
# - Se o divisor for zero, retorna zero
# - Arredonda o resultado para cima
# - Se qualquer dos números não for inteiro retorna erro

# Testes:
# - 3 divido por 1 e retorna 3
# - 3 dividido por 2 retorna 2
# - 3 dividido por 0 retorna 0
# - 3 dividido por -1 retorna -3
# - 3.5 dividido por 1 retorna erro
# - 3 dividido por 1.5 retorna erro

from src import my_function
import pytest


def test_3_divido_por_1_retorna_3():
    assert my_function(3, 1) == 3


def test_3_dividido_por_2_retorna_2():
    assert my_function(3, 2) == 2


def test_3_dividido_por_0_retorna_0():
    assert my_function(3, 0) == 0


def test_3_dividido_por_menos1_retorna_menos3():
    assert my_function(3, -1) == -3


def test_3ponto5_dividido_por_1_retorna_erro():
    with pytest.raises(Exception):
        assert my_function(3.5, 1)


def test_3_dividido_por_1ponto5_retorna_erro():
    with pytest.raises(Exception):
        assert my_function(3, 1.5)
