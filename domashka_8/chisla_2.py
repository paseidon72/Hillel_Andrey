import re
import nums_from_string

input1 = input("Введите ваше секретное число ")
input1 = input1.replace(',', '.')
s = []
for t in input1.split():
    try:
        s.append(int(t))
    except ValueError:
        pass
    try:
        s.append(float(t))
    except ValueError:
        pass
print('s split', s)

s1 = [int(s1) for s1 in str.split(input1) if s1.isdigit()]
print('s1 isdigit', s1)

s2 = nums_from_string.get_nums(input1)
print('s2 nums', s2)

s3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', input1)]
print('s3 regex', s3)