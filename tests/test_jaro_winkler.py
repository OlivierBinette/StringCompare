import pytest
from stringcompare import JaroWinkler
from stringcompare.distance.jarowinkler import JaroWinkler as PyJaroWinkler


def test_jarowinkler():
    cmp = JaroWinkler(similarity=False)
    assert cmp("", "") == 0
    assert cmp("", "1") == 1
    assert cmp("1", "") == 1
    assert cmp("1", "1") == 0
    assert cmp("1", "2") == 1

    assert cmp("Olivier", "Oilvier") == pytest.approx(0.042857142857142816)


def test_pyjarowinkler():
    cmp = PyJaroWinkler(similarity=False)
    assert cmp("", "") == 0
    assert cmp("", "1") == 1
    assert cmp("1", "") == 1
    assert cmp("1", "1") == 0
    assert cmp("1", "2") == 1

    assert cmp("Olivier", "Oilvier") == pytest.approx(0.042857142857142816)
