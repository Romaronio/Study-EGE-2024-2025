from re import findall

f = open('24.19.txt')
s = f.readline()
result = findall(r'[0-9A-G]+', s)
print(len(max(result, key=len)))