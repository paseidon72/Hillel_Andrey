import datetime
import csv
import json

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
            else:
                break

        while True:
            print("Чтобы пропустить - нажмите 'Enter'")
            date_of_death = input("Введите дату смерти в формате:'dd.mm.yyyy', 'dd/mm/yyyy', 'dd mm yyyy', 'd-m-yyyy'")

            for item in date_of_death:
                if item not in ("-. 1234567890"):
                    print('Неверный ввод')
                    break
            else:
                break
        while True:
            gender = input("введите пол: мужчина - 'm', женщина - 'f' ")
            if gender not in ('mf') and len(gender) > 1:
                print('Неверный ввод')
                continue
            else:
                break


        return DB(name, date_of_birth, gender, surname, otchestvo, date_of_death)



    def __init__(self, name, date_of_birth, gender, surname="", otchestvo="", date_of_death="000"):

        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.surname = surname
        self.otchestvo = otchestvo
        self.date_of_death = date_of_death
        DB.TOTAL_OBJECTS += 1
        input_person = []


        @property
        def fool_age():

            def split_data(data):
                if " " in data:
                    return (data.split())
                elif "." in data:
                    return (data.split("."))
                elif "/" in data:
                    return (data.split("/"))
                elif "-" in data:
                    return (data.split("-"))

            if self.date_of_death:
                day_b, month_b, year_b = split_data(self.date_of_birth)
                day_d, month_d, year_d = split_data(self.date_of_death)
                birthday = datetime.date(int(year_b), int(month_b), int(day_b))
                print(birthday)
                death = datetime.date(int(year_d), int(month_d), int(day_d))
                print(death)
                self.age = int(death.strftime("%Y")) - int(birthday.strftime("%Y"))
                print(self.age)
                return self.age
            else:
                day_b, month_b, year_b = split_data(self.date_of_birth)
                birthday = datetime.date(int(year_b), int(month_b), int(day_b))
                print(birthday)
                today = datetime.date.today()
                print(today)
                self.age = int(today.strftime("%Y")) - int(birthday.strftime("%Y"))
                print(self.age)
                return self.age

        # @property  # геттер
        # def ful_name():  # метод теперь будет использовать текущие имя и фамилию
        #     return str(self.name + self.surname + self.otchestvo)

        # @property
        # def other_data():
        #     return f"{self.gender} {self.date_of_birth} {self.date_of_death}"

        data_dict = {f'{self.name} {self.surname} {self.otchestvo}': [self.gender, self.date_of_birth,
                                                                      self.date_of_death]}
        data_dict.update(data_dict)
        input_person.append(data_dict)
        print(input_person)


        # Записать в файл в формате json
        with open("diploma.json", "a", encoding="utf-8") as f:  # открыли файл на запись в формате json
            json.dump(input_person, f, indent=4)  #


#        name_of_line = ['name', 'date_of_birth', 'gender', 'surname', 'otchestvo', 'date_of_death']
        line = [self.name, self.date_of_birth, self.gender, self.surname, self.otchestvo, self.date_of_death]

        if DB.TOTAL_OBJECTS <= 1:



            # with open("diploma.csv", "w", encoding="utf-8", newline='') as f1:
            #     file_writer = csv.writer(f1)
            #     file_writer.writerow(name_of_line)
            #     file_writer.writerow(line)



#        else:
            with open("diploma.csv", "a", encoding="utf-8", newline='') as f1:
                file_writer = csv.writer(f1)
                file_writer.writerow(line)
    # @property
    # def fool_age(self):
    #
    #     def split_data(data):
    #         if " " in data:
    #             return (data.split())
    #         elif "." in data:
    #             return (data.split("."))
    #         elif "/" in data:
    #             return (data.split("/"))
    #         elif "-" in data:
    #             return (data.split("-"))
    #
    #     if self.date_of_death:
    #         day_b, month_b, year_b = split_data(self.date_of_birth)
    #         day_d, month_d, year_d = split_data(self.date_of_death)
    #         birthday = datetime.date(int(year_b), int(month_b), int(day_b))
    #         print(birthday)
    #         death = datetime.date(int(year_d), int(month_d), int(day_d))
    #         print(death)
    #         self.age = int(death.strftime("%Y")) - int(birthday.strftime("%Y"))
    #         print(self.age)
    #         return self.age
    #     else:
    #         day_b, month_b, year_b = split_data(self.date_of_birth)
    #         birthday = datetime.date(int(year_b), int(month_b), int(day_b))
    #         print(birthday)
    #         today = datetime.date.today()
    #         print(today)
    #         self.age = int(today.strftime("%Y")) - int(birthday.strftime("%Y"))
    #         print(self.age)
    #         return self.age
    #
    # @property  # геттер
    # def ful_name(self):  # метод теперь будет использовать текущие имя и фамилию
    #     return f"{self.name} {self.surname} {self.otchestvo}"
    #
    # @property
    # def other_data(self):
    #     return f"{self.gender} {self.date_of_birth} {self.date_of_death}"







    def find(self):
        # # Распечатать файл в пайтоне из json
        # with open("task_01.json", "r") as f:  # открыли файл
        #     output_data = json.load(f)  # прочитали и сохранили из файла f в переменную output_data
        #
        # print("output_data:\n", output_data)  # распечатать с новой строки
        # while True:
        #     find = input("Поиск ")
        #
        #     if find == '' or not find.isalpha():
        #         print('Неверный ввод')
        #         continue
        #     else:
        #
        #         for key in input_person.items():

        # dict.keys()
        # с
        # помощью
        # цикла
        # for берешь нужный
        #
        # _dict = {
        #     'Name': 'noname',
        #     'Age': '100',
        #     'IQ': '0'
        # }
        #
        # for key in _dict.keys():
        #     if key == 'IQ':
        #         print(_dict.get(key))
        ...


    def get_from_file(self):  # взять загрузить из excel-евского файла
        ...

    def get_intu_file(self):
        ...

    def export_in_json(self):
        ...