import pytest

from hw_14_pytest.human import Human


@pytest.fixture()
def create_human():
    man = Human("Elon Musk", 52, "male")
    return man


@pytest.fixture()
def create_almost_dead_human():
    man = Human("Elon Musk", 99, "male")
    return man


@pytest.fixture()
def create_dead_human():
    man = Human("Elon Musk", 100, "male")
    return man
