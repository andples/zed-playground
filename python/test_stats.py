import pytest

from stats import mean, stdev


def test_mean():
    assert mean([1, 2, 3]) == 2


def test_stdev():
    assert stdev([2, 4, 4, 4, 5, 5, 7, 9]) == 2


def test_empty():
    with pytest.raises(ValueError):
        mean([])
