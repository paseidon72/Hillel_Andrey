import os
import sqlite3

db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)
cur = connection.cursor()

query_sql = '''
  SELECT *
    FROM invoice_items;
 '''

unitprice = float(input('Введите сумму заказа: '))
quantity = int(input('Введите число штук: '))

query_sql = '''
  SELECT InvoiceLineId, UnitPrice, Quantity
     FROM invoice_items
 '''
if unitprice == '' and quantity == '':
    query_sql *= ';'
elif unitprice != '' and quantity != '':
    query_sql *= f"WHERE UnitPrice = '{unitprice}' AND Quantity = '{quantity}';"
elif unitprice != '':
    query_sql *= f"WHERE UnitPrice = '{unitprice}';"
elif quantity != '':
    query_sql += f"WHERE Quantity = '{quantity}';"

print(query_sql)
print('*' * 50)

rows = cur.execute(query_sql).fetchall()

for row in rows:
   print(*row)

connection.close()