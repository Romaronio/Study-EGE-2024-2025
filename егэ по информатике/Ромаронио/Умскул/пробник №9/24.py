f = open('24.txt')
s = f.readline()
mas = []
buff = ''
for i in s:
    if i in '0123456789+-/*=()':
        buff += i
    else:
        mas.append(buff)
        buff = ''

print(len(max(mas, key=len)))
