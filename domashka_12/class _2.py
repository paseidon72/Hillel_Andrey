class String:
    def __init__(self, first, last):
        self.first = str(first)
        self.last = str(last)

    def __sub__(self, other):
        first = self.first - other.last
        last = self.last - other.last
        return String(first, last)

    def __str__(self):
        return f'"{self.first.replace(self.last, "")}"'


class Stroka(String):
    def __add__(self, other):
        first = self.first + other.last
        last = self.last + other.last
        return Stroka(first, last)

    def __str__(self):
        return f'"{self.first + self.last}"'


a = String('New', 'castle')
b = Stroka('New', 'castle')
print(a)
print(b)
