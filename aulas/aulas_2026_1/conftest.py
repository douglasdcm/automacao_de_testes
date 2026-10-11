import pytest


def close():
    print("Closing the application")


@pytest.fixture(autouse=True)
def init():
    print("Initialize")
    yield
    close()
