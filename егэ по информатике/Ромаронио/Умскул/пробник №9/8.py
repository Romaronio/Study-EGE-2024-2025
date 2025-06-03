from itertools import *
k = 0
for i in product('0123456', repeat=4):
    if i.count('4') == 1:
        if i[0] in '135':
            k += 1

print(k)
