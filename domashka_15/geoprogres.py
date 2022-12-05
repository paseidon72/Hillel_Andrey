def geo_prog(start, a, chislo):
    for item in range(a):
        yield start*chislo**item


y = geo_prog(1, 8, 4)

print("_" * 50)
print(y)

for item in y:
    print(item)

print("_" * 50)