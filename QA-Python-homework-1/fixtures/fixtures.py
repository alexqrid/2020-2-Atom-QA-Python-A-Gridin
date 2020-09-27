import pytest
import random
import string
from tools.helpers import random_int, random_string


@pytest.fixture()
def get_int():
    yield random_int(1, 100)


@pytest.fixture()
def get_string():
    yield random_string()


@pytest.fixture()
def get_list():
    yield [random_int(1, 100),
           random_string(),
           random_int(1, 100)]


@pytest.fixture()
def get_set():
    yield {random_int(1, 100),
           random_string(),
           random_int(120, 1000),
           random_string()
           }


@pytest.fixture("class")
def get_dict():
    yield {
        random_int(1, 100): random_string(),
        random_string(): random_int(1, 100),
        random_string(): [
            random_int(1, 100),
            random_string()]
    }
