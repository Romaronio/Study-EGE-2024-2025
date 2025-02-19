f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Домашка\24.4.txt')
s = f.readline()
s = s.replace('ZXY', 'a').replace('ZYX', 'a')
for i in range(1, 100):
	if 'a' * i in s:
		print(i)