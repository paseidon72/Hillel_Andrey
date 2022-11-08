import openpyxl
import json

with open('movies.json') as file:
    data = json.load(file)


book = openpyxl.Workbook()
book.remove(book['Sheet'])
book.create_sheet(title='sinema', index=0)
sheet = book['sinema']

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
    row += 1


book.save("my_book.xlsx")
book.close()

