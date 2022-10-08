ponchik = 'пончик'
pirojok = 'пирожок'

s_file = open('pechat.txt', 'w')
menu = print('!Покупай %(pir)s, выбирай %(pon)s?' %
             {'pir': pirojok.upper(), 'pon': ponchik.capitalize()}, sep='<<>>', file=s_file)


super_menu = print('!Покупай {1}, выбирай {0}?'
                   .format(ponchik.capitalize(), pirojok.upper()), sep='<<>>', file=s_file)


mega_menu = print(F'!Покупай {pirojok.upper()}, выбирай {ponchik.capitalize()}?',
                  sep='<<>>', end='', file=s_file)
s_file.close()
