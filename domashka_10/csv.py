import json5
import _csv


with open('task_1.json5') as f:
    output_data = json5.load(f)
    print(output_data)


name_file = ['id', 'firstname', 'age', 'phone']
file_1 = ['123456', 'name', 22, +380501234567]
file_2 = ['789654', 'name1', 25, +380507654321]
file_3 = ['321465', 'name2', 30, +380509876543]
file_4 = ['135802', 'name3', 32, +380503456789]
file_5 = ['133456', 'name4', 38, +380501357937]


with open('task_2._csv', 'w') as f:
    writer = _csv.writer(f)
    for item in (name_file, file_1, file_2, file_3, file_4, file_5):
        writer.writerow(item)



