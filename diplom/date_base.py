class DataBasa():

    def __int__(self, name, lastname, surname, sex):
        self.name = name
        self.lastname = lastname
        self.surname = surname
        self.sex = sex

    def input_data(self):
        while True:
            name = input('Введите данные человека. Пишите имя: ')
            if not name.isalpha() or name == '':
                print('Неверный ввод')
                continue
            lastname = input('Отлично теперь фамилию: ')
            surname = input('Отчество: ')
            sex = input('Укажите пол: ')

            answer = input('Для завершения введите слово: (выход/exit)\n Для продолжения записи пиши-1: ')
            if answer.upper() in ('ВЫХОД', 'EXIT'):
                break

        return DataBasa(name, lastname, surname, sex)


    def find(self):
        ...


    def get_from_file(self):
        ...


    def get_intu_file(self):
        ...


    def export_in_json(self):
        ...


