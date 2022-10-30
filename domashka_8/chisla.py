#chislo = "1,15"
#chislo = chislo.replace(',', '.')
#print(chislo)

#number1 = input("Enter number and hit enter ")
#print("Printing type of input value")
#print("type of number ", type(number1))


def check_user_input(input):
    try:
        val = int(input)
        if(val > 0):
            print("Вы ввели целое положительное число. = ", val)
        else:
            print("Вы ввели целое отрицательное число. = ", val)
    except ValueError:
        try:
            val = float(input)
            if (val > 0):
                print("Вы ввели дробное положительное число = ", val)
            else:
                print("Вы ввели дробное отрицательное число = ", val)
        except ValueError:
            print("Вы ввели не корректное число = ", input1)


while True:
    print('-' * 50)
    input1 = input("Введите ваше секретное число ")
    input1 = input1.replace(',', '.')
    check_user_input(input1)
    print('-' * 50)
    answer = input('Чтобы выйти пишите слово (выход/exit/quit/e/q):')
    if answer.upper() in ('ВЫХОД', 'EXIT', 'QUIT', 'E', 'Q'):
        break







#input2 = input("Enter any number "
#check_user_input(in

#input2 = input("Enter the last number ")
#check_user_input(input2)