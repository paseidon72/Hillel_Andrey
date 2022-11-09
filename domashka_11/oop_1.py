class Dog:
    number_of_foot = 4
    viviparous = True
    tail = True
    name = None

    def say(self):
        print('Woof, woof')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'step {item}')


dog_1 = Dog()
dog_1.say()
print(dog_1.number_of_foot)
dog_1.go()
print('-' * 50)
dog_2 = Dog()
dog_2.say()
dog_2.number_of_foot = 3
dog_2.go()
