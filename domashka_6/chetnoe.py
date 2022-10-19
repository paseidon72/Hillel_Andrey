#def chislo(number):
#    if number % 2 == 0:
#        return 'четное'
#    else:
#        return 'не четное'


normal = lambda number: 'четное' if number % 2 == 0 else 'не четное'

red = int(input('Пиши число: '))
print(normal(red))
