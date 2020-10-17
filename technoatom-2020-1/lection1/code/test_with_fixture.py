import random

import pytest


@pytest.fixture()
def random_value():
    print('entering')
    yield random.randint(0, 100)
    print('exiting')


def test(random_value):
    assert random_value > 50
