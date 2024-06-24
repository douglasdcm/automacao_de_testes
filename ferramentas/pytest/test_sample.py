# content of test_sample.py
def func(x):
    return x + 1


def test_func_returns_5_when_the_informed_value_is_3():
    assert func(3) == 5
