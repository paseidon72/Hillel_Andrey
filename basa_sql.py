import os
import sqlite3

db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)
cur = connection.cursor()

query_sql = '''
  SELECT *
    FROM invoice_items;
 '''

rows = cur.execute(query_sql).fetchall()

for row in rows:
    print(*row)

city = input('Введите город: ')
state = input('Введите штат: ')
query_sql = '''
  SELECT CustomerId, FirstName, City, State
     FROM customers
 '''
if city == '' and state == '':
    query_sql += ';'
elif city != '' and state != '':
    query_sql += f"WHERE City = '{city}' AND State = '{state}';"
elif city != '':
    query_sql += f"WHERE City = '{city}';"
elif state != '':
    query_sql += f"WHERE State = '{state}';"

print(query_sql)
print('*' * 50)

rows = cur.execute(query_sql).fetchall()

for row in rows:
   print(*row)

query_sql = '''
    SELECT DISTINCT FirstName
      FROM customers;
'''

# С помощью SQL + Python
query_sql = '''
    SELECT FirstName
      FROM customers;
'''
rows = cur.execute(query_sql).fetchall()
unique_first_name = set()

for row in rows:
    unique_first_name.add(row[0])


print(f'all names quantity: {len(rows)}, unique names quantity: {len(unique_first_name)}')
print(*unique_first_name)

connection.close()
