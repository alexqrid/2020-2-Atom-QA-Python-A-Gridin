def test():
    errors = []
    for i in range(0, 10):
        try:
            assert i % 2 == 0
        except AssertionError:
            errors.append(f'{i} is not even')

    assert not errors
