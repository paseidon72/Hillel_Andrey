import random
random_value = random.randint(0, 10)
print("komp zagdal chislo ot 0 do 10 est tolko 3 popytke chtoby ugadat chislo")
for i in range(1, 4):
    choice = int(input("Start pishi chislo: "))
    if choice > random_value:
        print("perebor")
    elif choice < random_value:
        print("malovato")
    else:
        print(f"Super {i} popitky i ty ugadal")
        break

    print(f"Ostalos eshe {3 - i} popitky")
else:
    print(f"Vse 3 popitky ischerpany. Chislo compa bilo {random_value}")

