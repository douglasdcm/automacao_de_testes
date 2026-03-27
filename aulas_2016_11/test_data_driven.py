import pytest


@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4), (0, 5), (0, 0), (9, 5)])
class TestClass:
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected
