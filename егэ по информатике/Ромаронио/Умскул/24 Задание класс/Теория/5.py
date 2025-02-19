f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Теория\24.5.txt')
s = f.readline()
s = s.replace('FJN', '*')
s = s.replace('JFN', '*')
for i in range(1, 100):
	if '*' * i in s:
		print(i)

