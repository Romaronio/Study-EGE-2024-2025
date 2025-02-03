from string import *
f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Домашка\24.8.txt')
s = f.readline()
alfa = ascii_uppercase
for x in alfa:
	s = s.replace(x, ' ')
s = s.split()
buff = ''
numbers = []
for i in range(len(s) - 1):
	if s[i] in '13579' and s[i + 1] in '13579':
		buff += s[i + 1]
		numbers.append(buff)
	else:
		buff = s[i + 1]
print(max(numbers))
