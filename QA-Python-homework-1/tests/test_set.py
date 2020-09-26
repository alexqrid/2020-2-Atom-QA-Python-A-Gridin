import pytest


class TestSet:

    @pytest.mark.parametrize("param", [["a", "b", "c", "b", "a", "a"],
                                       [1, 2, 2, 2, 3, 5, 6]
                                       ])
    def test_set_elements_uniqueness(self, param):
        set_a = {"a", "b", "c"}
        set_b = {1, 2, 3, 5, 6}
        assert set_a == set(param) or set_b == set(param)

    def test_asterisk(self, get_set):
        assert set([*get_set]) == set([i for i in get_set])

    def test_union(self, get_set, get_int):
        assert set([*get_set, get_int]) == get_set.union({get_int})

    def test_intersection(self, get_set):
        assert get_set.intersection(get_set) == get_set

    def test_slicing_impossible(self, get_set):
        with pytest.raises(TypeError):
            get_set[0]
