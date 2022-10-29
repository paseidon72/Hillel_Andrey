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
            print("Введенное значение не является числом")


input1 = input("Ввудите ваше секретное число ")
input1 = input1.replace(',', '.')
check_user_input(input1)

#input2 = input("Enter any number ")
#check_user_input(input2)

#input2 = input("Enter the last number ")
#check_user_input(input2)