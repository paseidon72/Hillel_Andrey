temp = 0
# def decorator_1(func):
#     print('Running our function')
#     return func
# @decorator_1
# def temperature():
#     return temp
# print(temperature())

def decorator_1(func):
    print('Running our function')
    return func
def temperature():
    return temp
decorator_1(temperature())
