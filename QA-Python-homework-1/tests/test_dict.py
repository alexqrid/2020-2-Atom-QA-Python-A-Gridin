import pytest


class TestDict:

    def test_get_key_method(self, get_dict):
        assert not get_dict.get(-1, False)

    def test_keys_uniqueness(self, get_dict):
        with pytest.raises(TypeError):
            get_dict[["abc"]] = 2

    def test_value_update(self, get_dict, get_string):
        key, old_val = list(get_dict.items())[0]
        get_dict[key] = get_string
        assert get_dict[key] != old_val

    @pytest.mark.parametrize("d", [{"a": 1}, {-2: "asd"}])
    def test_update(self, d, get_dict):
        l1 = len(get_dict)
        get_dict.update(d)
        assert len(get_dict) != l1

    def test_clear(self, get_dict):
        get_dict.clear()
        assert len(get_dict) == 0
