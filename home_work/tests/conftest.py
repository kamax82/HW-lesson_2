import pytest


@pytest.fixture()
def fix_for_list():
    return [i for i in range(1, 11)]


@pytest.fixture()
def fix_for_dict():
    return {i: i * 10 for i in range(10)}


@pytest.fixture()
def fix_for_set():
    return set(x * 2 for x in range(10))


@pytest.fixture()
def fix_for_string():
    return 'Classical hello world'
