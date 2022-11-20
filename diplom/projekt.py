import openpyxl
import datetime as DT

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
    date2 = input("Введите дату смерти (dd-mm-yyyy)\n")
    death = DT.datetime.strptime(date2, '%d-%m-%Y').date()
    if birthday > death:
        birthday, death = death, birthday

    age = death.year - birthday.year
    # print('Вы ввели данные человека')
    # print('Фамилия:', lastname)
    # print('Имя', name)
    # print('Отчество', surname)
    # print('Пол', sex)
    # print('Полных лет', age)
    # print('Родился', birthday)
    # print('Умер', death)
    answer = input('Для завершения введите слово: (выход/exit)')
    if answer.upper() in ('ВЫХОД', 'EXIT'):
        break






