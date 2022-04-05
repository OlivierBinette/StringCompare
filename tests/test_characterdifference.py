from stringcompare import CharacterDifference
from stringcompare.distance.characterdifference import (
    CharacterDifference as PyCharacterDifference,
)
import string
import random

random.seed(1)


def random_string(n):
    return "".join(random.choices(string.ascii_uppercase, k=n))

def test_CharacterDifference_FF():
    cmp = CharacterDifference(normalize=False, similarity=False)

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


def test_CharacterDifference_FT():
    cmp = CharacterDifference(normalize=False, similarity=True)

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


def test_CharacterDifference_TF():
    cmp = CharacterDifference(normalize=True, similarity=False)

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


def test_CharacterDifference_TT():
    cmp = CharacterDifference(normalize=True, similarity=True)

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


def test_CharacterDifference_dmat_size():
    cmp = CharacterDifference(normalize=False, similarity=False)

    assert cmp.compare("", "") == 0
    assert cmp.compare(" ", "") == 1
    assert cmp.compare("1234", "1") == 3


def test_PyCharacterDifference_FF():
    cmp = PyCharacterDifference(normalize=False, similarity=False)

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


def test_PyCharacterDifference_FT():
    cmp = PyCharacterDifference(normalize=False, similarity=True)

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


def test_PyCharacterDifference_TF():
    cmp = PyCharacterDifference(normalize=True, similarity=False)

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


def test_PyCharacterDifference_TT():
    cmp = PyCharacterDifference(normalize=True, similarity=True)

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


def test_PyCharacterDifference_dmat_size():
    cmp = PyCharacterDifference(normalize=False, similarity=False)

    assert cmp.compare("", "") == 0
    assert cmp.compare(" ", "") == 1
    assert cmp.compare("1234", "1") == 3


def test_pycpp():
    cmp = CharacterDifference(normalize=False, similarity=False)
    pycmp = PyCharacterDifference(normalize=False, similarity=False)

    for i in range(20):
        for j in range(20):
            a = random_string(i)
            b = random_string(j)
            assert cmp(a, b) == pycmp(a, b)
