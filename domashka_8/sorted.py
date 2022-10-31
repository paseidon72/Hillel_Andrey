nums = [('Jon', 15), ('Clarc', 7), ('Ban', 15), ('Sara', 15), ('Nik', 3)]
print(sorted(nums)) #сортировка в алфавитном порядке по первому значению
print('-' * 100)
print(sorted(nums, reverse=True)) #сортировка в обратном порядке
print('-' * 100)
print(sorted(nums, key=lambda x: x[1])) #сортировка по второму значению
print('-' * 100)
print(sorted(nums, key=lambda x: (x[1], x[0]))) #сортировка по второму значению и внутри по алфавиту
print('-' * 100)
print(list(map(lambda x: (x[1], x[0]), sorted(nums, key=lambda x: (x[1], x[0]))))) #сортировка
#по второму значению внутри в алфавитном порядке с заменой местами 1е и 2е значение