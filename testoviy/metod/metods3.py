class Birds:
    objInstancesCount = 0
    ruClassName = 'Birds'

    def __init__(self, name, id, age):
        self._name = name
        self._id = id
        self._age = age
        Birds.objInstancesCount = Birds.objInstancesCount + 1

        # getter

    @property
    def name(self):
        return self._name

    # setter
    @name.setter
    def name(self, n):
        if (n != "Иван"):
            self._name = n

    # getter
    @property
    def age(self):
        return self._age

    # setter
    @age.setter
    def age(self, age):
        if (age >= 0):
            self._age = age
        else:
            self._age = 0

    # getter
    @property
    def id(self):
        return self._id

    def info(self):
        print("Имя класса: " + self._name)
        print("Идентификационный номер: " + str(self._id))
        print("Возраст: " + str(self._age))

# b = Birds("объект №1 класса " + Birds.ruClassName, 11, 3)
# b.info()
# b2 = Birds("объект №2 класса " + Birds.ruClassName, 10, 4)
# b2.info()
# print("Количество объектов класса " + Birds.ruClassName + ": " + str(Birds.objInstancesCount))