from collections.abc import Sequence
from typing import Literal, TypeVar


def add(a: int, b: int) -> int:
    return a + b

result: int = add(1, 2)

x: Literal[42, 999] = 42
x = 999
# print(x)

T = TypeVar('T')

def combine(a: T, b: T) -> list[T]:
    return [a, b]

res1 = combine(1, 2)
res2 = combine('my home', 'is Poland')

# Union

# def combine_1(a: int | str, b: int | str) -> int | str:
#     return a + b
#
# r_1 = combine_1(1, 2)
# r_2 = combine_1('my home', 'is Poland')


# TODO launch file using in terminal mypy example.py

# def magic(data: tuple[int, ...]) -> int:
#     return data[0]

def magic(data: Sequence[int, ...]) -> int:
    return data[0]

v = magic((1, 2, 3))
v2 = magic((1, 2))
