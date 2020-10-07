import pytest


class TestString:

    def test_modification_impossible(self, get_string):
        a = get_string
        with pytest.raises(TypeError):
            a[0] = "b"

    def test_concat_with_plus(self, get_string):
        s1 = get_string
        s2 = get_string
        assert s1 + s2 == "".join([s1, s2])

    @pytest.mark.parametrize("s,i", [("a", 2), ("b", 3), ("c", 4)])
    def test_multiply_equals_to_repeats(self, s, i):
        tmp = ""

        for j in range(i):
            tmp += s
        assert s * i == tmp

    def test_reversed_and_slice_equals(self, get_string):
        tmp = ""
        for i in reversed(get_string):
            tmp += i
        assert tmp == get_string[::-1]

    def test_lower(self, get_string):
        assert get_string.lower().islower()
