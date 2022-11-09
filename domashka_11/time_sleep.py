import time

a = 0

while True:
    a = a + 1
    print(a)
    print('Ждем 5 секунд')
    time.sleep(5)
    if a >= 5:
        break


print('Через 10 секунд закроется')
print(10)
