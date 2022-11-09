# Создать 2 класса truck и car, которые являются наследниками класса auto из
# предыдущего домашнего  задания.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит надпись «attention»,
# его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение обязательного атрибума max_speed.
# Создать по 2 объекта для каждого из классов truck и car, проверить все их методы и атрибуты.
from abc import ABC, abstractmethod

class Avto(ABC):

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        print(f'age', self.age + 1, 'let')

class truck(Avto):
    def __init__(self, brand, age, mark, max_load):
        super().__init__(self, brand, age, mark)
        self.max_load = max_load

    def move(self):
        print('«attention»', 'move')

class car(Avto):
    def __init__(self, brand, age, mark, max_speed):
        super().__init__(self, brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        print('move')
