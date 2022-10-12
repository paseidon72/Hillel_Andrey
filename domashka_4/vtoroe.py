
n = int(input())
summa = 0
for i in range(n+1):
    summa += i**3
print(summa)

i = 1
rs = 0
while(i <= n):
    rs = rs + i**3
    i = i + 1
print(rs)
