def test(x, z, y=5):
    print('x:', x)
    print('y:', y)
    print('z:', z)
    return str(x) + str(y) + str(z)


a = test(1, z='dd', y=4)
print(a)

input_list = [1, 2, 3, 4, 5, 6]
a, b, *c = input_list
print('a:', a)
print('b:', b)
print('c:', c)
print('input_list:', input_list)
print('input_list:', *input_list)


def test_2(*args):
    result = ' '
    for item in args:
        result += ' ' + str(item)
    return result


res = test_2(1, 2, 'f')
print('res:', res)


def test_3(**kwargs):
    result = 0
    print('kwargs:', kwargs)
    for item in kwargs:
        result += kwargs[item]
    return result


res_2 = test_3(x=1, y=2, b=8, c=15)
print('res_2:', res_2)

print('-' * 50)


def test_4(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)
    return args, kwargs


a, b = test_4(1, 2, 3, 4, 5, x=8, f=85)
print('a:', a)
print('b:', b)

s = [1, 3, 4, 5, 'dd' 'y']
print('s:', s)
print('len:', len(s))