a = 7


def test(x):
    print('x 1:', x)
    x = 66
    print('x 2:', x)


test(a)
print(a)
print('-' * 50)

b = [7, 8]


def test(x=None):
    if x is None:
        x = list(range(1, 5))
    print('x 1:', x)
    x.append(45)
    print('x 2:', x)


test(b)
#print('b:', b)
test()
test()
test()