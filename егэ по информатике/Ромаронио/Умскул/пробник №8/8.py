from itertools import *
k = 0
for i in product('ГГГСССС', repeat=6):
    if i[0] != 'С' and i[-1] != 'Г':
        k += 1
print(k)