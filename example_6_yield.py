def magic():
    yield 42
    yield 422
    yield 842

for m in magic():
    print(m)

d = magic()
print(next(d))
print(next(d))
print(next(d))


def magic_2():
    counter = 0

    while True:
        yield counter
        counter += 1
        if counter > 5:
            return

e = magic_2()
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
# print(next(e))


for m in magic_2():
    print(e)
