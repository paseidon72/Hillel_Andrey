
name = input('Napishite svoe imya: ')
while True:
    age = input('Napishi svoy vozrast: ')
    if not age.isdigit() or int(age) <= 0:
        print('Oshibka, povtorite vvod')
    elif int(age) >= 100:
        print(name, 'Vi ljete v nashe vremya stolko ne jivut...')
        answer = input('Hotite viyti? (Y/D):')
        if answer.upper() in ('Y', 'D'):
            break
    elif int(age) >= 18:
        print('Chto jelaete', name)
        answer = input('Hotite viyti? (Y/D):')
        if answer.upper() in ('Y', 'D'):
            break
    elif int(age) >= 10:
        print('Kak jizn?', name)
        answer = input('Hotite viyti? (Y/D):')
        if answer.upper() in ('Y', 'D'):
            break
    elif int(age) <10:
        print('Privet shket', name)
        answer = input('Hotite viyti? (Y/D):')
        if answer.upper() in ('Y', 'D'):
            break









