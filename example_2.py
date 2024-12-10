# tuple packing
from collections import OrderedDict

x = 1, 2, 3, 4, 5
print(type(x), x)

# ways how to create tuple:

t = (1, 2)
t_1 = (1,)
t_2: tuple[int, ...] = tuple()
t_3 = 1, 2, 3 # tuple packing

def magic():
    return 1, 2, 3, 4

# tuple unpacking

a, b, c = (1, 2, 3)

t5 = (1, 2, 3, 4, 5, 6, 7, 9)

a1, b1, *rest = t5

*rest_1, a2, b2 = t5

a3, *rest_2, b3, c3 = t5

print(rest, rest_1, rest_2)

x2: int = 0
y2: int = 1

# left side tuple unpacking = right side tuple packing
# TODO ---- L - tuple unpacking | R - tuple packing
# TODO tuple unpacking works with every variable that has !! Sequence protocol !!

x2, y2 = y2, x2

t_6 = (1, 2, [1, 2])

# TODO set must include hashable elements if tuple includes any kind of non hashable ,
#  we can't create set on the base that tuple , set can takes iterable and create itself ,
#  means __iter__ that returns object serves __iter__ and __next__



# x_6 = {1, 2, t_6}

x_7: set = {1, 2, 3} | {1, 4, 5}
print(x_7)

# TODO from python 3.6+ default dict is ordered

y_7 = dict(q=1, z=2)
y_8 = dict([(1, 2), (3, 4), (5, 6)])
print(y_7, y_8, sep='\n')

x_8 = OrderedDict([(1, 2), (3, 4), (5, 6)])
print(y_8.get(999, 42))

class Magic:
    def __hash__(self):
        return 42

    def __eq__(self, other):
        return True

    # def __str__(self):
    #     return "yolo"
    #
    # __repr__ = __str__


def magic_fn():
    ...


x_10 = {
    1: 0,
    False: 1,
    True: 2,
    0: 3,
    "ala": 4,
    "": 5,
    "": 6,
    (1,): 7,
    (1, 2): 8,
    None: 9,
    Magic: 10,
    Magic(): 11,
    magic_fn: 12,
    Magic(): 13
}

print(x_10)
#
# print(x[0.0000000000000])
# print(x[0])
# print(x[False])

print(x_10[Magic()])
