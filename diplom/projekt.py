import openpyxl
import datetime as DT
from datetime import date

book = openpyxl.Workbook()
book.remove(book['Sheet'])
book.create_sheet(title='данные', index=0)
sheet = book['данные']

sheet['A1'] = 'Фамилия'
sheet['B1'] = 'Имя'
sheet['C1'] = 'Очество'
sheet['D1'] = 'Пол'
sheet['E1'] = 'Полных лет'
sheet['F1'] = 'Дата рождения'
sheet['G1'] = 'Дата смерти'


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
    print('Полных лет', age)
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
    print('Полных лет', age)
    # print('Родился', birthday)
    # print('Умер', death)
    answer = input('Для завершения введите слово: (выход/exit)')
    if answer.upper() in ('ВЫХОД', 'EXIT'):
        break






