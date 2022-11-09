class Dog:
    def __init__(self, name, number_of_foot, tail):
        self.__name = name
        self._number_of_foot = number_of_foot
        self.tail = tail


dog_1 = Dog('Dob', 4, 24)
print(dog_1.tail)
print(dog_1._number_of_foot)
print(dog_1._Dog__name)
