def my_decorator(a_function):
    def wraper():
        print('text1')
        a_function()
        print('text2')
    return wraper


def my_decorator2(a_function):
    def wraper():
        print('text16')
        a_function()
        print('text21')
    return wraper


@my_decorator
@my_decorator2
def alone_func():
    print('text3')


@my_decorator
def other_func():
    print('text4')

alone_func()
#print('-' * 50)
#other_func()