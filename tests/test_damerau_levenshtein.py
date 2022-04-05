from stringcompare import DamerauLevenshtein
from stringcompare.distance.dameraulevenshtein import (
    DamerauLevenshtein as PyDamerauLevenshtein,
)
import string
import random

random.seed(1)


def random_string(n):
    return "".join(random.choices(string.ascii_uppercase, k=n))


def test_DamerauLevenshtein_FF():
    cmp = DamerauLevenshtein(normalize=False, similarity=False)

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

    assert cmp.compare("jellyfish", "smellyfihs") == 3


def test_DamerauLevenshtein_FT():
    cmp = DamerauLevenshtein(normalize=False, similarity=True)

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

    assert cmp.compare("jellyfish", "smellyfihs") == 8


def test_DamerauLevenshtein_TF():
    cmp = DamerauLevenshtein(normalize=True, similarity=False)

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


def test_DamerauLevenshtein_TT():
    cmp = DamerauLevenshtein(normalize=True, similarity=True)

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


def test_DamerauLevenshtein_dmat_size():
    cmp = DamerauLevenshtein(normalize=False, similarity=False, dmat_size=10)

    assert cmp.compare("", "") == 0
    assert cmp.compare(" ", "") == 1
    assert cmp.compare("1234", "1") == 3


def test_PyDamerauLevenshtein_FF():
    cmp = PyDamerauLevenshtein(normalize=False, similarity=False)

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


def test_PyDamerauLevenshtein_FT():
    cmp = PyDamerauLevenshtein(normalize=False, similarity=True)

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


def test_PyDamerauLevenshtein_TF():
    cmp = PyDamerauLevenshtein(normalize=True, similarity=False)

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


def test_PyDamerauLevenshtein_TT():
    cmp = PyDamerauLevenshtein(normalize=True, similarity=True)

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


def test_PyDamerauLevenshtein_dmat_size():
    cmp = PyDamerauLevenshtein(normalize=False, similarity=False, dmat_size=10)

    assert cmp.compare("", "") == 0
    assert cmp.compare(" ", "") == 1
    assert cmp.compare("1234", "1") == 3


def test_pycpp():
    cmp = DamerauLevenshtein(normalize=False, similarity=False, dmat_size=20)
    pycmp = PyDamerauLevenshtein(normalize=False, similarity=False, dmat_size=20)

    for i in range(20):
        for j in range(20):
            a = random_string(i)
            b = random_string(j)
            assert cmp(a, b) == pycmp(a, b)
