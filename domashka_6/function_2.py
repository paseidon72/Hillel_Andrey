name = 'Tom'


def say_hi():
#    global name
#    name = 'Jack'
    print('Hello:', name)


def say_bye():
    print('Good bye:', name)


say_hi()
say_bye()


def hello(age: int, name: str = 'Kucusha') -> str:
    '''
    Test primer
    '''
    return 'Hello:' + str(name)


print(hello(34))
print(hello.__annotations__)
print(hello.__doc__)