from re import *

f = open('24.16.txt')
s = f.readline()
is_ok = findall('(?:LDR)+(?:LD?)?', s)
print(len(max(is_ok, key=len)))
