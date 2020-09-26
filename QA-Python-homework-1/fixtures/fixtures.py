import pytest
import random
import string


@pytest.fixture()
def get_int():
    yield random.randint(1, 100)


@pytest.fixture()
def get_string():
    yield "".join(random.choices(string.ascii_letters,
                                 k=random.randint(1, 26)))


@pytest.fixture()
def get_list():
    yield [random.randint(1, 100),
           "".join(random.choices(string.ascii_letters,
                                  k=random.randint(1, 26))),
           random.randint(1, 100)]


@pytest.fixture()
def get_set():
    yield {random.randint(1, 100),
           "".join(random.choices(string.ascii_letters,
                                  k=random.randint(1, 26))),
           random.randint(120, 1000),
           "".join(random.choices(string.ascii_letters,
                                  k=random.randint(1, 26)))
           }


@pytest.fixture("class")
def get_dict():
    count = random.randint(1, 26)
    s = random.choices(string.ascii_letters, k=count)
    random.shuffle(s)
    yield {
        random.randint(1, 100): "".join(
            random.choices(string.ascii_letters,
                           k=random.randint(1, 26))),
        "".join(random.choices(string.ascii_letters,
                               k=random.randint(1, 26))): random.randint(1,
                                                                         100),
        "".join(random.choices(string.ascii_letters,
                               k=random.randint(1, 26))): [
            random.randint(1, 100),
            s[:random.randint(1, count)]]
    }
