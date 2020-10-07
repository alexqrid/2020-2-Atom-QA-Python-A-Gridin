import random
import string


def random_int(a=1, b=26):
    return random.randint(a, b)


def random_string():
    return "".join(random.choices(string.ascii_letters,
                                  k=random.randint(1, 26)))
