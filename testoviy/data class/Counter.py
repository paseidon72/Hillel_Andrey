from collections import Counter

a = Counter('superfluous')

Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'f': 1, 'o': 1, 'r': 1, 'p': 1})
print(a)

counter = Counter('superfluous')
print(counter['u'])
print(list(counter.elements()))
print(counter.most_common(2))
counter_one = Counter('superfluous')

Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'f': 1, 'o': 1, 'r': 1, 'p': 1})
print(counter_one)

counter_two = Counter('super')
counter_one.subtract(counter_two)

print(counter_one)
Counter({'u': 2, 'l': 1, 'f': 1, 'o': 1, 's': 1, 'e': 0, 'r': 0, 'p': 0})
