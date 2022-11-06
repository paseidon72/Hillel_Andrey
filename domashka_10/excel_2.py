import json5
import openpyxl




with open('test.json5') as file:
    data = json5.load(file)

book = openpyxl.Workbook()
sheet = book.active

sheet['A1'] = 'ID'
sheet['B1'] = 'TITLE'
sheet['C1'] = 'YEAR'
sheet['D1'] = 'GENRES'
sheet['E1'] = 'DIRECTOR'
sheet['F1'] = 'ACTORS'

row = 2
for movie in data['movies']:
    sheet[row][0].value = movie['id']
    sheet[row][1].value = movie['title']
    sheet[row][2].value = movie['year']
    sheet[row][3].value = ' '.join(movie['genres'])
    sheet[row][4].value = movie['director']
    sheet[row][5].value = movie['actors']

book.save('tab.xlsx')
book.create_sheet()
