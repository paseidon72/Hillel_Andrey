import time

def timeit(f):
    def inner(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        print(f'{end - start} seconds')
        return res
    return inner




@timeit
def my_sum_1(*args, **kwargs):
    return sum(*args, **kwargs)

@timeit
def my_sum_2(*args, **kwargs):
    return sum(*args, **kwargs)

res = print('my_sum_1:', my_sum_1([i for i in range(int(1e5))]))
print('-' * 50)
res = print('my_sum_2:', my_sum_1([i for i in range(int(1e5))]))