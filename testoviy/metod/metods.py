# Програма Python для демонстрації статический метод для проверки того, является ли человек взрослым или нет.
# використання методу класу та статичного методу.
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # метод класу для створення об’єкта Person за роком народження.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # статичний метод перевірки того, чи є особа дорослою чи ні.
    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))