import pytest


@pytest.mark.parametrize('i', list(range(10)))
def test_even(i):
    """
    :param i: range of integers
    Parametrized test which checks that number if even.
    """

    assert i % 2 == 0
