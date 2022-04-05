from stringcompare import Hamming
from stringcompare.distance.hamming import (
    Hamming as PyHamming,
)
import string
import random

random.seed(1)


def random_string(n):
    return "".join(random.choices(string.ascii_uppercase, k=n))

def test_Hamming_FF():
    cmp = Hamming(normalize=False, similarity=False)

    assert cmp("", "") == 0
    assert cmp("! +-2/.", "") == 7

    assert cmp.compare("", "") == 0

    assert cmp.compare(" ", "") == 1
    assert cmp.compare("!", "") == 1
    assert cmp.compare("ab", "") == 2
    assert cmp.compare("! +-2/.", "") == 7

    assert cmp.compare("", " ") == 1
    assert cmp.compare("", "!") == 1
    assert cmp.compare("", "ab") == 2
    assert cmp.compare("", "! +-2/.") == 7

    assert cmp.compare("1", "1234") == 3
    assert cmp.compare("4", "1234") == 4

    assert cmp.compare("1234", "1") == 3
    assert cmp.compare("1234", "4") == 4

    assert cmp.compare("jellyfish", "smellyfihs") == 8


def test_Hamming_FT():
    cmp = Hamming(normalize=False, similarity=True)

    assert cmp.compare("", "") == 1

    assert cmp.compare(" ", "") == 0
    assert cmp.compare("!", "") == 0
    assert cmp.compare("ab", "") == 0
    assert cmp.compare("! +-2/.", "") == 0

    assert cmp.compare("", " ") == 0
    assert cmp.compare("", "!") == 0
    assert cmp.compare("", "ab") == 0
    assert cmp.compare("", "! +-2/.") == 0

    assert cmp.compare("1", "1234") == 1
    assert cmp.compare("4", "1234") == 0

    assert cmp.compare("1234", "1") == 1
    assert cmp.compare("1234", "4") == 0

    assert cmp.compare("jellyfish", "smellyfihs") == 2


def test_Hamming_TF():
    cmp = Hamming(normalize=True, similarity=False)

    assert cmp.compare("", "") == 0

    assert cmp.compare(" ", "") == 1
    assert cmp.compare("!", "") == 1
    assert cmp.compare("ab", "") == 1
    assert cmp.compare("! +-2/.", "") == 1

    assert cmp.compare("", " ") == 1
    assert cmp.compare("", "!") == 1
    assert cmp.compare("", "ab") == 1
    assert cmp.compare("", "! +-2/.") == 1

    assert cmp.compare("1", "1234") == 3 / 4
    assert cmp.compare("4", "1234") == 1

    assert cmp.compare("1234", "1") == 3 / 4
    assert cmp.compare("1234", "4") == 1


def test_Hamming_TT():
    cmp = Hamming(normalize=True, similarity=True)

    assert cmp.compare("", "") == 1

    assert cmp.compare(" ", "") == 0
    assert cmp.compare("!", "") == 0
    assert cmp.compare("ab", "") == 0
    assert cmp.compare("! +-2/.", "") == 0

    assert cmp.compare("", " ") == 0
    assert cmp.compare("", "!") == 0
    assert cmp.compare("", "ab") == 0
    assert cmp.compare("", "! +-2/.") == 0

    assert cmp.compare("1", "1234") == 1 / 4
    assert cmp.compare("4", "1234") == 0

    assert cmp.compare("1234", "1") == 1 / 4
    assert cmp.compare("1234", "4") == 0


def test_PyHamming_FF():
    cmp = PyHamming(normalize=False, similarity=False)

    assert cmp("", "") == 0
    assert cmp("! +-2/.", "") == 7

    assert cmp.compare("", "") == 0

    assert cmp.compare(" ", "") == 1
    assert cmp.compare("!", "") == 1
    assert cmp.compare("ab", "") == 2
    assert cmp.compare("! +-2/.", "") == 7

    assert cmp.compare("", " ") == 1
    assert cmp.compare("", "!") == 1
    assert cmp.compare("", "ab") == 2
    assert cmp.compare("", "! +-2/.") == 7

    assert cmp.compare("1", "1234") == 3
    assert cmp.compare("4", "1234") == 4

    assert cmp.compare("1234", "1") == 3
    assert cmp.compare("1234", "4") == 4

    assert cmp.compare("jellyfish", "smellyfihs") == 8


def test_PyHamming_FT():
    cmp = PyHamming(normalize=False, similarity=True)

    assert cmp.compare("", "") == 1

    assert cmp.compare(" ", "") == 0
    assert cmp.compare("!", "") == 0
    assert cmp.compare("ab", "") == 0
    assert cmp.compare("! +-2/.", "") == 0

    assert cmp.compare("", " ") == 0
    assert cmp.compare("", "!") == 0
    assert cmp.compare("", "ab") == 0
    assert cmp.compare("", "! +-2/.") == 0

    assert cmp.compare("1", "1234") == 1
    assert cmp.compare("4", "1234") == 0

    assert cmp.compare("1234", "1") == 1
    assert cmp.compare("1234", "4") == 0

    assert cmp.compare("jellyfish", "smellyfihs") == 2


def test_PyHamming_TF():
    cmp = PyHamming(normalize=True, similarity=False)

    assert cmp.compare("", "") == 0

    assert cmp.compare(" ", "") == 1
    assert cmp.compare("!", "") == 1
    assert cmp.compare("ab", "") == 1
    assert cmp.compare("! +-2/.", "") == 1

    assert cmp.compare("", " ") == 1
    assert cmp.compare("", "!") == 1
    assert cmp.compare("", "ab") == 1
    assert cmp.compare("", "! +-2/.") == 1

    assert cmp.compare("1", "1234") == 3 / 4
    assert cmp.compare("4", "1234") == 1

    assert cmp.compare("1234", "1") == 3 / 4
    assert cmp.compare("1234", "4") == 1


def test_PyHamming_TT():
    cmp = PyHamming(normalize=True, similarity=True)

    assert cmp.compare("", "") == 1

    assert cmp.compare(" ", "") == 0
    assert cmp.compare("!", "") == 0
    assert cmp.compare("ab", "") == 0
    assert cmp.compare("! +-2/.", "") == 0

    assert cmp.compare("", " ") == 0
    assert cmp.compare("", "!") == 0
    assert cmp.compare("", "ab") == 0
    assert cmp.compare("", "! +-2/.") == 0

    assert cmp.compare("1", "1234") == 1 / 4
    assert cmp.compare("4", "1234") == 0

    assert cmp.compare("1234", "1") == 1 / 4
    assert cmp.compare("1234", "4") == 0


def test_pycpp():
    cmp = Hamming(normalize=False, similarity=False)
    pycmp = PyHamming(normalize=False, similarity=False)

    for i in range(20):
        for j in range(20):
            a = random_string(i)
            b = random_string(j)
            assert cmp(a, b) == pycmp(a, b)
