from stringcompare import LCSDistance
from stringcompare.distance.lcs import LCSDistance as PyLCSDistance
import string
import random

random.seed(1)


def random_string(n):
    return "".join(random.choices(string.ascii_uppercase, k=n))


def test_LCSDistance_FF():
    cmp = LCSDistance(normalize=False, similarity=False)

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
    assert cmp.compare("4", "1234") == 3

    assert cmp.compare("1234", "1") == 3
    assert cmp.compare("1234", "4") == 3

    assert cmp.compare("jellyfish", "smellyfihs") == 5


def test_LCSDistance_FT():
    cmp = LCSDistance(normalize=False, similarity=True)

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
    assert cmp.compare("4", "1234") == 1

    assert cmp.compare("1234", "1") == 1
    assert cmp.compare("1234", "4") == 1

    assert cmp.compare("jellyfish", "smellyfihs") == 7


def test_LCSDistance_TF():
    cmp = LCSDistance(normalize=True, similarity=False)

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
    assert cmp.compare("4", "1234") == 3 / 4

    assert cmp.compare("1234", "1") == 3 / 4
    assert cmp.compare("1234", "4") == 3 / 4


def test_LCSDistance_TT():
    cmp = LCSDistance(normalize=True, similarity=True)

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
    assert cmp.compare("4", "1234") == 1 / 4

    assert cmp.compare("1234", "1") == 1 / 4
    assert cmp.compare("1234", "4") == 1 / 4


def test_LCSDistance_dmat_size():
    cmp = LCSDistance(normalize=False, similarity=False, dmat_size=10)

    assert cmp.compare("", "") == 0
    assert cmp.compare(" ", "") == 1
    assert cmp.compare("1234", "1") == 3


def test_PyLCSDistance_FF():
    cmp = PyLCSDistance(normalize=False, similarity=False)

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
    assert cmp.compare("4", "1234") == 3

    assert cmp.compare("1234", "1") == 3
    assert cmp.compare("1234", "4") == 3


def test_PyLCSDistance_FT():
    cmp = PyLCSDistance(normalize=False, similarity=True)

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
    assert cmp.compare("4", "1234") == 1

    assert cmp.compare("1234", "1") == 1
    assert cmp.compare("1234", "4") == 1


def test_PyLCSDistance_TF():
    cmp = PyLCSDistance(normalize=True, similarity=False)

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
    assert cmp.compare("4", "1234") == 3 / 4

    assert cmp.compare("1234", "1") == 3 / 4
    assert cmp.compare("1234", "4") == 3 / 4


def test_PyLCSDistance_TT():
    cmp = PyLCSDistance(normalize=True, similarity=True)

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
    assert cmp.compare("4", "1234") == 1 / 4

    assert cmp.compare("1234", "1") == 1 / 4
    assert cmp.compare("1234", "4") == 1 / 4


def test_PyLCSDistance_dmat_size():
    cmp = PyLCSDistance(normalize=False, similarity=False, dmat_size=10)

    assert cmp.compare("", "") == 0
    assert cmp.compare(" ", "") == 1
    assert cmp.compare("1234", "1") == 3


def test_pycpp():
    cmp = LCSDistance(normalize=False, similarity=False, dmat_size=20)
    pycmp = PyLCSDistance(normalize=False, similarity=False, dmat_size=20)

    for i in range(20):
        for j in range(20):
            a = random_string(i)
            b = random_string(j)
            assert cmp(a, b) == pycmp(a, b)
