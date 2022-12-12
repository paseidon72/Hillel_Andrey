#выполняет условные проверки параметров функции перед выполнением самой функции.
def check_not_None(func):
    def check(x):
        if x is not None:
            return func(x)
        else:
            return 'is None'
    return check

@check_not_None
def f1(x):
    return x**1

@check_not_None
def f2(x):
    return x**2

@check_not_None
def f3(x):
    return x**3

print(f1(4))      # 4
print(f2(None))   # 'is None'
print(f3(4))      # 64