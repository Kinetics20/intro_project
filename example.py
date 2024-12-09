from collections.abc import Sequence
from typing import Literal, TypeVar, Callable

from example_types import DictWholeType


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

# TODO tuple[int, ...] , for tuple with unlimited elements

# def magic(data: tuple[int, ...]) -> int:
#     return data[0]

# TODO Sequence | from collections.abc import Sequence , for any collections match to sequence protocol
# Sequence replaces ellipsis [...]

U = TypeVar('U')
# TODO U = TypeVar('U') , created object U presents any type of data element in collection ( generic typing)

def magic(data: Sequence[U]) -> U:
    return data[0]

v = magic((1, 2, 3))
v2 = magic((1, 2))
v3 = magic((3.1, 2))
v4 = magic(('home', '3'))

# TODO str | int , union , means str or int

countries: dict[str | int, str] = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    444: 'New York',
}

# DictInsideType = dict[str | int, str]
# DictWholeType = dict[str, DictInsideType]

countries_2: DictWholeType = {
    'Europe': {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    444: 'New York',
    },
    'Asia':{
        'China': 'Beijing',
        'Vietnam': 'Hanoi',
    }
}

def my_max(*args: int) -> int:
    return max(args)

x_1 = my_max(1, 2, 3, 4)

# TODO Callable from typing , means what we can do execute , i.e. functions named anonymous and classes with __call_

Z = TypeVar('Z')

def sentence(cb: Callable[[Z], Z], txt: Z) -> Z:
    return cb(txt)

sentence (lambda x: x.upper(), 'ala ma kota')