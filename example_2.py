# tuple packing

x = 1, 2, 3, 4, 5
print(type(x), x)

# ways how to create tuple:

t = (1, 2)
t_1 = (1,)
t_2 = tuple()
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

x = 0
y = 1

# left side tuple unpacking = right side tuple packing
# TODO ---- L - tuple unpacking | R - tuple packing
x, y = y, x
