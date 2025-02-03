from string import *
f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Домашка\24.9.txt')
s = f.readline()
for i in s:
	if i in 'IJKLMNOPQRSTUVWXYZ':
		s = s.replace(i, ' ')
s = s.split()
print(len(max(s, key=len)))
