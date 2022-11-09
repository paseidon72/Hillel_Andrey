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
import time
class Avto(ABC):

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    @abstractmethod
    def move(self):
        ...

    def stop(self):
        print('stop')

    def birthday(self):
        print(f'age', self.age + 1, 'let')


class truck(Avto):
    def __init__(self, brand, age, mark, max_load, color='Red', weight=2500):
        super().__init__(brand, age, mark)
        self.max_load = max_load
        self.color = color
        self.weight = weight

    def move(self):
        print('«attention»', 'move')

    def load(self):
        time.sleep(1)
        print('«load»')
        time.sleep(1)

class car(Avto):
    def __init__(self, brand, age, mark, max_speed, color='Blec', weight=2800):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed
        self.color = color
        self.weight = weight

    def move(self):
        print('move', f'max speed is {self.max_speed} km/ch')

car_1 = car('bmv', 5, 'sport', 500)
car_1.move()
car_1.stop()
car_1.birthday()
print('-' * 50)
print('brand', car_1.brand)
print('mark', car_1.mark)
print('color', car_1.color)
print('weight-kg', car_1.weight)
print('*' *50)
car_2 = car('bmv', 4, 'sport plus', 600)
car_2.move()
car_2.stop()
car_2.birthday()
print('-' * 50)
print('brand', car_2.brand)
print('mark', car_2.mark)
print('color', car_2.color)
print('weight-kg', car_2.weight)
print('*' *50)
truck_1 = truck('bmv', 10, 'sedan', 100)
truck_1.move()
truck_1.stop()
truck_1.birthday()
truck_1.load()
print('-' * 50)
print('brand', truck_1.brand)
print('mark', truck_1.mark)
print('max_load-kg', truck_1.max_load)
print('color', truck_1.color)
print('weight-kg', truck_1.weight)
print('*' *50)
truck_2 = truck('bmv', 15, 'cadet', 1100)
truck_2.move()
truck_2.stop()
truck_2.birthday()
truck_2.load()
print('-' * 50)
print('brand', truck_2.brand)
print('mark', truck_2.mark)
print('max_load-kg', truck_2.max_load)
print('color', truck_2.color)
print('weight-kg', truck_2.weight)
print('*' *50)
