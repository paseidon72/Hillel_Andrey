import pickle

book1 = input('пишите текст: ')
book2 = input('пишите текст: ')
book3 = input('пишите текст: ')
book4 = input('пишите текст: ')


try:
    with open('text.bin', 'wb') as f:
        pickle.dump(book1, f)
        pickle.dump(book2, f)
except:
    print('Ошибка с файлом')
try:
    with open('text.bin', 'ab') as f:
        pickle.dump(book3, f)
        pickle.dump(book4, f)
except:
    print('Ошибка с файлом')

try:
    with open('text.bin', 'rb') as f:
        b1 = pickle.load(f)
        b2 = pickle.load(f)
        b3 = pickle.load(f)
        b4 = pickle.load(f)
except:
    print('Ошибка с файлом')

print(b1, b2, b3, b4, sep="\n")