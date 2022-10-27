#Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
import time


from datetime import datetime
start_time = datetime.now()


def my_decorator(a_function):
    def wraper():
        print('text1')
        a_function()
        print('text2')
    return wraper



@my_decorator
def alone_func():
    print(list(range(1, 10, 2)))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))


start_time = datetime.now()


def my_decorator2(a_function):
    def wraper():
        print('text16')
        a_function()
        print('text21')
    return wraper
@my_decorator2
def other_func():
    line = "=" * 40
    print(line)


alone_func()
print('-' * 50)
other_func()
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))