from typing import TypeVar, Protocol

T = TypeVar('T', bound='Addable')


class Addable(Protocol):
    def __add__(self: T, other: T) -> T: ...
    def __radd__(self: T, other: T) -> T: ...


def magic(a: T, b: T) -> T:
    return a + b


class X:
    pass


magic(1, 2)
# magic(1, '2')
# magic(X(), X())
