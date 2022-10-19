def dickt(string):
    k = {}
    for i in string:
        if i in k:
            k[i] += 1
        else:
            k[i] = 1
    return k


list = [1, 1, 1, 1, 3, 4, 5, 5, 6, 6]
print(dickt(list))
