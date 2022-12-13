from metods3 import Birds


class GalaBacklane(Birds):
    species = "Галапагосский баклан"

    def __init__(self, name, id, age, population):
        super().__init__(name, id, age)
        self.__population = population

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        self.__population = population

    def info(self):
        super().info()
        print('*' * 50)
        print("Вид подкласса: " + GalaBacklane.species)
        print("Количество особей: " + str(self.__population))
        print("Номер объекта класса " + Birds.ruClassName + ": " + str(Birds.objInstancesCount))

g = GalaBacklane("Birds", 22, 2, 60)
g.info()
