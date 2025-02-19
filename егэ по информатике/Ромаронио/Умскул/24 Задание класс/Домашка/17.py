from re import *

f = open('24.17.txt')
s = f.readline()
result = findall(r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]+', s)
print(len(max(result, key=len)))