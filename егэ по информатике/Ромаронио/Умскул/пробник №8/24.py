f = open('24.txt')
s = f.readline()
res_mas = []
buff = ''
for i in s:
    if i in '0123456789ABCDE':
        buff += i
    else:
        res_mas.append(buff)
        buff = ''
print(max(res_mas, key=len))