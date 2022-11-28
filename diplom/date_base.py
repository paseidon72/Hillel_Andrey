import datetime
import csv
import json
import datetime as DT
from datetime import date

class DB():
    TOTAL_OBJECTS = 0


    def input_data(self):


        while True:
            name = input("Введите имя ")
            if name == '' or not name.isalpha():
                print('Неверный ввод')
                continue
            else:
                break


        while True:
            print("Чтобы пропустить - нажмите 'Enter'")
            surname = input("Введите фамилию ")
            if surname != '' and not surname.isalpha():
                print('Неверный ввод')
                continue
            else:
                break

        while True:
            print("Чтобы пропустить - нажмите 'Enter'")
            otchestvo = input("Введите отчество ")
            if otchestvo != '' and not otchestvo.isalpha():
                print('Неверный ввод')
                continue

            else:
                break

        while True:
            date_of_birth = input("Введите дату рождения в формате:'dd.mm.yyyy', 'dd/mm/yyyy', 'dd mm yyyy', 'd-m-yyyy'")
            if date_of_birth == "":
                print('Неверный ввод')
                continue
            for item in date_of_birth:
                if item not in ("-. 1234567890") :
                    print('Неверный ввод')
                    break
            if date_of_birth == date_of_birth:
                birthday = DT.datetime.strptime(date_of_birth, '%d-%m-%Y').date()
                today = date.today()
                age = today.year - birthday.year
                print('Полных лет', age)
                break

        while True:
            print("Чтобы пропустить - нажмите 'Enter'")
            date_of_death = input("Введите дату смерти в формате:'dd.mm.yyyy', 'dd/mm/yyyy', 'dd mm yyyy', 'd-m-yyyy'")
            if date_of_death == "":
                break
            for item in date_of_death:
                if item not in ("-. 1234567890"):
                    print('Неверный ввод')
                    break
            if date_of_death == date_of_death:
                death = DT.datetime.strptime(date_of_death, '%d-%m-%Y').date()
                if birthday > death:
                    birthday, death = death, birthday

                age = death.year - birthday.year
                print('Полных лет', age)
                break
        while True:
            gender = input("введите пол: мужчина - 'm', женщина - 'f' ")
            if gender not in ('mf') and len(gender) > 1:
                print('Неверный ввод')
                continue
            else:
                break


        return DB(name, date_of_birth, gender, age, surname, otchestvo, date_of_death)



    def __init__(self, name, date_of_birth, gender, age, surname="", otchestvo="", date_of_death="000"):

        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.age = age
        self.surname = surname
        self.otchestvo = otchestvo
        self.date_of_death = date_of_death
        DB.TOTAL_OBJECTS += 1
        input_person = []

        data_dict = {f'{self.name} {self.surname} {self.otchestvo}': [self.gender, self.date_of_birth,
                                                                      self.date_of_death, self.age]}
        data_dict.update(data_dict)
        input_person.append(data_dict)
        print(input_person)

        with open("spisok.json", "a", encoding="utf-8") as f:  # открыли файл на запись в формате json
            json.dump(input_person, f, indent=4)


        line = [self.name, self.date_of_birth, self.gender, self.age, self.surname, self.otchestvo, self.date_of_death]

        if DB.TOTAL_OBJECTS <= 1:
            with open("spisok.csv", "a", encoding="utf-8", newline='') as f1:
                file_writer = csv.writer(f1)
                file_writer.writerow(line)



    def __str__(self):
        return f'{self.name}{self.otchestvo}{self.surname}{self.gender}{self.age}{self.date_of_birth}{self.date_of_death}'




    def find(self):


        while True:
            name1 = input("Введите поисковый запрос ")
            with open("spisok.csv", encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if line.find(name1) != -1:
                        print(name1, ':запись есть')
                        print('строка №', lines.index(line))
                        print('Информация подробно: ', line)
                        break




    def get_from_file(self):
        print('vtoroe')

    def get_intu_file(self):
        print('vtoroe')

    def export_in_json(self):
        print('vtoroe')

