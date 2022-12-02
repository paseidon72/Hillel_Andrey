class Dog:
    number_of_foot = 4
    viviparous = True
    tail = True
    name = None

    def __init__(self, name, number_of_foot=4, tail=True):
        self.name = name
        self.number_of_foot = number_of_foot
        self.tail = tail

    def say(self):
        print('Woof, woof')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'step {item}')


dog_1 = Dog('Bob', 3)
dog_1.say()
dog_1.go()
print(dog_1.number_of_foot)

dog_1.go()

print('-' * 50)

dog_2 = Dog('Rem')
print(dog_2.number_of_foot)
dog_2.go()