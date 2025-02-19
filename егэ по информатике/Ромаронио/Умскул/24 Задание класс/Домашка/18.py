from re import *
f = open(r'24.18.txt')
s = f.readline()
result = findall('[1234567890+*-/())]+', s)
print(len(max(result, key=len)))