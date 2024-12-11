from example_5 import divide


def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0


def test_divide_numbers_negative():
    assert divide(10, 2) != 15.0


try:
    divide(10, 0)
    raise AssertionError('STH is wrong')
except ZeroDivisionError:
    print('OK')
