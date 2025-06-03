from re import *
for x in range(0, 10 ** 9, 127):
    if fullmatch(r'215\d*414\d', str(x)) and x % 127 == 0:
        print(x, x // 127)