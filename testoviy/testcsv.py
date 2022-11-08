import csv

f = open('my_book.csv')
reader = csv.DictReader(f, delimiter=',', quotechar='"')
for index, row in enumerate(reader):
    if index > 10:
        break
    print(row)
