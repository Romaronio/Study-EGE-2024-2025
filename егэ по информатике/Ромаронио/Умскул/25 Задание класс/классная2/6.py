from re import *
for x in range(0, 10 ** 8, 193):
    if fullmatch(r'64\d*32\d2', str(x)):
        print(x, x // 193)