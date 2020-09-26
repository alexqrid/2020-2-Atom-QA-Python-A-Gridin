import pytest


class TestInt:

    @pytest.mark.parametrize('b', [1, 3])
    def test_division_not_int(self, get_int, b):
        assert isinstance(get_int / b, float)

    def test_zero_division(self, get_int):
        with pytest.raises(ZeroDivisionError):
            assert get_int / 0

    @pytest.mark.parametrize('a,b', [(3, 5), (7, 23), (2, 13)])
    def test_product_greater_than_squares_sum(self, a, b):
        assert a ** 2 + b ** 2 <= a ** 2 * b ** 2

    def test_positive_product_negative_is_negative(self, get_int):
        assert get_int * (-get_int) <= 0

    def test_float_is_not_equal_to_int(self, get_int):
        with pytest.raises(AssertionError):
            assert get_int / get_int != 1
