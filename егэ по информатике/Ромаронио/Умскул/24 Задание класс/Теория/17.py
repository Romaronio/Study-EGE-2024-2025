import re
f = open('24.17.txt')
s = f.readline()
is_ok = re.findall(r'\d+(?:[-*/+]\d+)*', s)
print(len(max(is_ok, key=len)))