from itertools import *
k = 0
for i in product('345678', repeat=7):
    if i.count('5') == 2:
        print(i)
        k += 1

print(k)
