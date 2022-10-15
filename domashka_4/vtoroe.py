
namber = int(input())
summa = 0
for i in range(namber+1):
    if i % 3 == 0:
        continue
    summa += i**3
print(summa)


i = 0
rs = 0
while i < namber:
    i += 1
    if i % 3 == 0:
        continue
    rs += i ** 3
print(rs)


