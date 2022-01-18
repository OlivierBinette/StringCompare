from stringcompare import Levenshtein
from stringcompare.distance.levenshtein import Levenshtein as PyLevenshtein


def test_Levenshtein_FF():
    cmp = Levenshtein(normalize=False, similarity=False)

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

    assert cmp.compare("jellyfish", "smellyfihs") == 4


def test_Levenshtein_FT():
    cmp = Levenshtein(normalize=False, similarity=True)

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

    assert cmp.compare("jellyfish", "smellyfihs") == 7.5


def test_Levenshtein_TF():
    cmp = Levenshtein(normalize=True, similarity=False)

    assert cmp.compare("", "") == 0

    assert cmp.compare(" ", "") == 1
    assert cmp.compare("!", "") == 1
    assert cmp.compare("ab", "") == 1
    assert cmp.compare("! +-2/.", "") == 1

    assert cmp.compare("", " ") == 1
    assert cmp.compare("", "!") == 1
    assert cmp.compare("", "ab") == 1
    assert cmp.compare("", "! +-2/.") == 1

    assert cmp.compare("1", "1234") == 3/4
    assert cmp.compare("4", "1234") == 3/4

    assert cmp.compare("1234", "1") == 3/4
    assert cmp.compare("1234", "4") == 3/4


def test_Levenshtein_TT():
    cmp = Levenshtein(normalize=True, similarity=True)

    assert cmp.compare("", "") == 1

    assert cmp.compare(" ", "") == 0
    assert cmp.compare("!", "") == 0
    assert cmp.compare("ab", "") == 0
    assert cmp.compare("! +-2/.", "") == 0

    assert cmp.compare("", " ") == 0
    assert cmp.compare("", "!") == 0
    assert cmp.compare("", "ab") == 0
    assert cmp.compare("", "! +-2/.") == 0

    assert cmp.compare("1", "1234") == 1/4
    assert cmp.compare("4", "1234") == 1/4

    assert cmp.compare("1234", "1") == 1/4
    assert cmp.compare("1234", "4") == 1/4


def test_Levenshtein_dmat_size():
    cmp = Levenshtein(normalize=False, similarity=False, dmat_size=10)

    assert cmp.compare("", "") == 0
    assert cmp.compare(" ", "") == 1
    assert cmp.compare("1234", "1") == 3


def test_PyLevenshtein_FF():
    cmp = PyLevenshtein(normalize=False, similarity=False)

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


def test_PyLevenshtein_FT():
    cmp = PyLevenshtein(normalize=False, similarity=True)

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


def test_PyLevenshtein_TF():
    cmp = PyLevenshtein(normalize=True, similarity=False)

    assert cmp.compare("", "") == 0

    assert cmp.compare(" ", "") == 1
    assert cmp.compare("!", "") == 1
    assert cmp.compare("ab", "") == 1
    assert cmp.compare("! +-2/.", "") == 1

    assert cmp.compare("", " ") == 1
    assert cmp.compare("", "!") == 1
    assert cmp.compare("", "ab") == 1
    assert cmp.compare("", "! +-2/.") == 1

    assert cmp.compare("1", "1234") == 3/4
    assert cmp.compare("4", "1234") == 3/4

    assert cmp.compare("1234", "1") == 3/4
    assert cmp.compare("1234", "4") == 3/4


def test_PyLevenshtein_TT():
    cmp = PyLevenshtein(normalize=True, similarity=True)

    assert cmp.compare("", "") == 1

    assert cmp.compare(" ", "") == 0
    assert cmp.compare("!", "") == 0
    assert cmp.compare("ab", "") == 0
    assert cmp.compare("! +-2/.", "") == 0

    assert cmp.compare("", " ") == 0
    assert cmp.compare("", "!") == 0
    assert cmp.compare("", "ab") == 0
    assert cmp.compare("", "! +-2/.") == 0

    assert cmp.compare("1", "1234") == 1/4
    assert cmp.compare("4", "1234") == 1/4

    assert cmp.compare("1234", "1") == 1/4
    assert cmp.compare("1234", "4") == 1/4


def test_PyLevenshtein_dmat_size():
    cmp = Levenshtein(normalize=False, similarity=False, dmat_size=10)

    assert cmp.compare("", "") == 0
    assert cmp.compare(" ", "") == 1
    assert cmp.compare("1234", "1") == 3
