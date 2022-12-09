# Desc: create a decorator that prints start/end time of function
# выводит время исполнения вашей функции
import numpy as np
def time_it(func):
    def timer(*args):
        start = np.datetime64('now')
        print(start)

        result = func(*args)

        end = np.datetime64('now')
        print(end)
        print(f'{(end - start) / np.timedelta64(1, "s")} secs')

        return result
    return timer

@time_it
def long_function(x):
    for i in range(x):
        _ = i * i + 5

long_function(int(1e6))

"""
Output:
2022-01-24T02:37:15
2.0 secs
2022-01-24T02:39:15
"""