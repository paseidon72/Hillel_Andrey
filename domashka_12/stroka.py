class String(str):

    def __init__(self, first):
        self.first = str(first) #перевод в строковое значение

    def __add__(self, other):
        return String(self.first + str(other)) #складываем две строки

    def __sub__(self, other):
        return String(self.first.replace(str(other), "", 1)) #находит в первой строке вторую и меняет ее на '' ,
        # т.е просто вырезает. цифра 1 говорит, что вырезает только первую найденную комбинацию


a = String(String('New') - 'w') #передаем String('New') в self, 'w' в first
print(a)


