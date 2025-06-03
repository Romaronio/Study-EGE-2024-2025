from re import *
for x in range(0, 10 ** 7, 403):
    if fullmatch(r'12\d*\d1\d*5', str(x)):
        print(x, x // 403)