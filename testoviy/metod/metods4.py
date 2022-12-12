from metods3 import Birds


class Duck(Birds):
    species = "Утка"

    def __init__(self, name, id, age, fly_speed, fly_height):
        super().__init__(name, id, age)
        self.__fly_speed = fly_speed
        self.__fly_height = fly_height

    @property
    def fly_speed(self):
        return self.__fly_speed

    @fly_speed.setter
    def fly_speed(self, fly_speed):
        self.__fly_speed = fly_speed

    @property
    def fly_height(self):
        return self.__fly_height

    @fly_height.setter
    def fly_height(self, fly_height):
        self.__fly_height = fly_height

    def info(self):
        super().info()
        print('*' * 50)
        print("Вид подкласса: " + Duck.species)
        print("Скорость полета: " + str(self.__fly_speed))
        print("Высота полета: " + str(self.__fly_height))
        print("Номер объекта класса " + Birds.ruClassName + ": " + str(Birds.objInstancesCount))

d = Duck('Birds', 22, 2, 110, 5)
d.info()
print('*' * 50)
d2 = Duck('Birds', 25, 3, 115, 6)
d2.info()
