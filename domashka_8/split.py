

while True:
    print('-' * 50)
    input1 = input("Введите ваше секретное число ")
    input1 = input1.replace(',', '.')
    s = []
    for t in input1.split():
        try:
            s.append(int(t))
        except ValueError:
            pass
        try:
            s.append(float(t))
        except ValueError:
            pass
    input1 = s
#    check_user_input(input1)
    print(input1)
    print(type(input1))
    print('-' * 50)
    answer = input('Чтобы выйти пишите слово (выход/exit/quit/e/q):')
    if answer.upper() in ('ВЫХОД', 'EXIT', 'QUIT', 'E', 'Q'):
        break
