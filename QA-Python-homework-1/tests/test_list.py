import pytest


class TestList:

    def test_index_range(self, get_list):
        with pytest.raises(IndexError):
            get_list[len(get_list)]

    def test_list_concat(self, get_list, get_string):
        l1 = get_list
        l2 = [*l1, get_string]

        assert [*l1, *l2] == l1 + l2

    @pytest.mark.parametrize("i", list(range(5)))
    def test_extends(self, get_list, i):
        assert [i].extend(get_list) == get_list.insert(0, i)

    @pytest.mark.parametrize("param", [[1, 2, 3, 4, 5], ["a", "b", "c", "d"]])
    def test_reverse_sort(self, param):
        assert param[::-1] == sorted(param, reverse=True)

    def test_pop(self, get_list):
        a = get_list
        a_len, last = len(a), a[-1]
        s = a.pop()
        assert len(a) == a_len - 1 and s == last
