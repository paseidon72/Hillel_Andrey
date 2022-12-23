import datetime as DT
from datetime import date

class Person:
    def __init__(self, date1, date2):
        self.date1 = date1
        self.date2 = date2

    def birthday(self):
        self.date1 = DT.datetime.strptime(self.da1, '%d-%m-%Y').date()
        today = date.today()
        return Person(today.year - self.date1.year)


da1 = Person("Введите дату рождения (dd-mm-yyyy)\n", '')
age = da1
print(Person)

