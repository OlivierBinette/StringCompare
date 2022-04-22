import pytest
from stringcompare import Jaro
from stringcompare.distance.jaro import Jaro as PyJaro


def test_jaro():
    cmp = Jaro(similarity=False)
    assert cmp("", "") == 0
    assert cmp("", "1") == 1
    assert cmp("1", "") == 1
    assert cmp("1", "1") == 0
    assert cmp("1", "2") == 1

    assert cmp("Olivier", "Oilvier") == pytest.approx(0.04761905)


def test_pyjaro():
    cmp = PyJaro(similarity=False)
    assert cmp("", "") == 0
    assert cmp("", "1") == 1
    assert cmp("1", "") == 1
    assert cmp("1", "1") == 0
    assert cmp("1", "2") == 1

    assert cmp("Olivier", "Oilvier") == pytest.approx(0.04761905)
