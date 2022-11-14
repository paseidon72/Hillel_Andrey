class String(str):

    def __init__(self, first):
        self.first = str(first)

    def __add__(self, other):
        return String(self.first + str(other))

    def __sub__(self, other):
        return String(self.first.replace(str(other), "", 1))


a = String(String('New') - 'w')
print(a)


