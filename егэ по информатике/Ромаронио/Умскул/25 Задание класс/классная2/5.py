from re import *
for x in range(0, 10 ** 8, 123):
    if fullmatch('154[0-9]8[0-9]', str(x)):
        print(x, x // 123)