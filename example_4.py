def divide(a, b):
    return a / b


if divide(10, 2) == 5.0:
    print('OK')
else:
    raise AssertionError('STH is wrong')


if divide(10, 2) != 15.0:
    print('OK')
else:
    raise AssertionError('STH is wrong')

try:
    divide(10, 0)
    raise AssertionError('STH is wrong')
except ZeroDivisionError:
    print('OK')
