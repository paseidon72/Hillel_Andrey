#Дан список состоящий из данных разного типа.
#Вернуть новый список, где при помощи функции map() каждый элемент типа int
# первоначального списка приведён к типу str, элементы всех остальных типов передаются
# в новый список без изменения их типа.
#В качестве входной функции в map() использовать lambda-функцию.

result = map(lambda x: str(x), [1, 2, 'rr', 5, 65, 'tyu'])
print(list(result))

result2 = map(lambda x: str(x) if type(x) == int else x, [1, 2, 'rr', 5, 65, 'tyu'])
print(list(result2))