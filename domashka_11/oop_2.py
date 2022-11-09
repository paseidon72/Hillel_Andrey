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


dog_1 = Dog('Boob', 3)
dog_1.say()
dog_1.go()
print(dog_1.name)
print('-' * 50)
dog_2 = Dog('Reech')
dog_2.say()
dog_2.go()
print(dog_2.name)
