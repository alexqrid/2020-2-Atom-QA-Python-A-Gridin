import os
import random

import pytest


@pytest.fixture(autouse=True)
def new_file(random_file):
    f = open('my_file', 'w')
    yield
    f.close()
    os.remove('my_file')


@pytest.fixture()
def random_file():
    return str(random.randint(0, 1000))
