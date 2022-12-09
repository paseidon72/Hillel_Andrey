from functools import wraps


def my_decorator(func):


    @wraps(func)
    def call_func(*args):
        return func(*args)

    return call_func


@my_decorator
def f(x):
    """does some math"""
    return x + x * x

print(f(5))        # 30
print(f.__name__)  # 'f'
print(f.__doc__)   # 'does some math'