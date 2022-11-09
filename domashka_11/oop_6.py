# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.
class Avto:
    color = True
    weight = True

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

class BMV(Avto):
    def say(self):
        print('instruction')

mashin = BMV('passat', 10, 'pejo')
mashin.say()
mashin.move()
mashin.stop()
mashin.birthday()
print('brand', mashin.brand)
print('mark', mashin.mark)
print('color', mashin.color)
print('weight', mashin.weight)
