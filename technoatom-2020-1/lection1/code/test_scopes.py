import random

import pytest


@pytest.fixture(scope='function')
def function_fixture():
    return random.randint(0, 100)


@pytest.fixture(scope='class')
def class_fixture():
    return random.randint(0, 100)


@pytest.fixture(scope='session')
def session_fixture():
    return random.randint(0, 100)


def test1(function_fixture, session_fixture):
    print(f"func fixture:{function_fixture}")
    print(f"session fixture:{session_fixture}")


def test2(function_fixture, session_fixture):
    print(f"func fixture:{function_fixture}")
    print(f"session fixture:{session_fixture}")


def test3(function_fixture, session_fixture):
    print(f"func fixture:{function_fixture}")
    print(f"session fixture:{session_fixture}")


class Test4:

    def test4_1(self, function_fixture, class_fixture, session_fixture):
        print(f"func fixture:{function_fixture}")
        print(f"class fixture:{class_fixture}")
        print(f"session fixture:{session_fixture}")

    def test4_2(self, function_fixture, class_fixture, session_fixture):
        print(f"func fixture:{function_fixture}")
        print(f"class fixture:{class_fixture}")
        print(f"session fixture:{session_fixture}")

    def test4_3(self, function_fixture, class_fixture, session_fixture):
        print(f"func fixture:{function_fixture}")
        print(f"class fixture:{class_fixture}")
        print(f"session fixture:{session_fixture}")
