import pytest

from example_5 import divide


def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0


def test_divide_numbers_negative():
    assert divide(10, 2) != 15.0


def test_divide_with_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_divide_floats():
    assert divide(1, 3) == pytest.approx(0.3333333, rel=1e-6)
