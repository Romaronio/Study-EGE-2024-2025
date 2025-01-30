x = 4 ** 2016 + 2 ** 2018 - 8 ** 600 + 6
b = bin(x)[2:]
s = b.count('1')
print(s)