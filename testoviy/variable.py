#Лістинг 2
a = [1, 2, 3]
b = 5


def func(x, y):
    x.append(4)
    y = y + 1


func(a, b)
print("a=", a) # Вихід a=[1, 2, 3, 4]
print("b=", b) # Вихід b=5

# лістинг 5
def f(x):
    def g(y):
        return y
    return g
a = 5
b = 1
h=f(a)
h(b) # Вихід 1