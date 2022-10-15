
import random
random_value = random.randint(0, 10)
print("Компьютер загадал число oот 0 до 10 у тебя 3 попытке угадать его")
for i in range(1, 4):
    choice = int(input("Пиши число: "))
    if choice > random_value:
        print("Перебор")
    elif choice < random_value:
        print("Маловато")
    else:
        print(f"Супер {i} попытки и ты угадал")
        break

    print(f"Еще есть {3 - i} попытки")
else:
    print(f"Все попытки исчерпаны. Число компьтера {random_value}")

