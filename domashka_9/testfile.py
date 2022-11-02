import pickle

book1 = 'первая строка'
book2 = 'вторая строка'
book3 = 'третья строка'
book4 = 'четвертая строка'


try:
    with open('yes.bin', 'wb') as f:
        pickle.dump(book1, f)
        pickle.dump(book2, f)
except:
    print('Ошибка с файлом')
try:
    with open('yes.bin', 'ab') as f:
        pickle.dump(book3, f)
        pickle.dump(book4, f)
except:
    print('Ошибка с файлом')

try:
    with open('yes.bin', 'rb') as f:
        b1 = pickle.load(f)
        b2 = pickle.load(f)
        b3 = pickle.load(f)
        b4 = pickle.load(f)
except:
    print('Ошибка с файлом')

print(b1, b2, b3, b4, sep="\n")
