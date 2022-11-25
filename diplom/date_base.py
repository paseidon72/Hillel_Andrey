import csv
import datetime as DT
from datetime import date

class DataBasa():

    def __int__(self, name, lastname, surname, sex, birthday, age, death='%d-%m-%Y'):
        self.name = name
        self.lastname = lastname
        self.surname = surname
        self.sex = sex
        self.birthday = birthday
        self.death = death
        self.age = age


    def __str__(self):
        return f'{self.name}{self.lastname}{self.surname}{self.sex}{self.age}{self.birthday}{self.death}'


    def input_data(self):
        while True:
            name = input('Введите данные человека. Пишите имя: ')
            if not name.isalpha() or name == '':
                print('Неверный ввод')
                continue
            lastname = input('Отлично теперь фамилию: ')
            surname = input('Отчество: ')
            sex = input('Укажите пол: ')
            date1 = input("Введите дату рождения (dd-mm-yyyy)\n")
            birthday = DT.datetime.strptime(date1, '%d-%m-%Y').date()
            today = date.today()
            age = today.year - birthday.year

#            title = ['Имя', 'Фамилия', 'Отчество', 'Пол', 'Родился', 'Полных лет']
            tekst = [name, lastname, surname, sex, birthday, age]
            # with open("spisok.csv", "w", encoding="utf-8", newline='') as f:
            #     file_writer = csv.writer(f)
            #     file_writer.writerow(title)
            with open("spisok.csv", "a", encoding="utf-8", newline='') as f:
                file_writer = csv.writer(f)
                file_writer.writerow(tekst)


            answer = input('Для завершения введите слово: (выход/exit)\n Для продолжения записи пиши-1: ')
            if answer.upper() in ('ВЫХОД', 'EXIT'):
                break

        return DataBasa(name, lastname, surname, sex, age, birthday)


    def find(self):
        ...


    def get_from_file(self):
        ...


    def get_intu_file(self):
        ...


    def export_in_json(self):
        ...


