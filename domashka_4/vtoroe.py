
n = int(input())
summa = 0
for i in range(n+1):
    if i % 3 == 0:
        continue
    summa += i**3
print(summa)

i = 1
rs = 0
while i <= n:
    if i % 3 == 0:
        continue
    rs = rs + i**3
    i += 1
print(rs)


