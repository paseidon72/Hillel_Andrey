def area(d, h):
    return 0.5 * d * h


area2 = lambda d, h: 0.5 * d * h
print(area(4, 5))
print(area2(4, 5))


def test(number):
    return str(number) if number == 1 else str(number) + 's'


test2 = lambda number: str(number) if number == 1 else str(number) + 's'


print(test(1))
print(test2(1))
print(test(10))
print(test2(10))

number = int(input('Пиши число: '))
if number % 2 == 0:
    print('четное')
else:
    print('не четное')

number = lambda number: int(number) if number % 2 == 0 else number % 2 != 0
print('1четное')
print('2не четное')
