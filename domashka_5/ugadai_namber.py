
import random
random_value = random.randint(0, 10)
print("Компьютер загадал число oот 0 до 10 у тебя 3 попытке угадать его")
for i in range(1, 4):
    choice = int(input("Пиши число: "))
    if choice > random_value:
        print(f"Перебор? {choice}")
    elif choice < random_value:
        print(f"Маловато? {choice}")
    else:
        print(f"Супер {i} попытки и ты угадал это число! {random_value}")
        break
        
    print(f"Еще есть {3 - i} попытки")
else:
    print(f"Все попытки исчерпаны. Число компьтера {random_value}")

