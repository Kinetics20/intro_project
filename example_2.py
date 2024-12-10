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
print(rest, rest_1)