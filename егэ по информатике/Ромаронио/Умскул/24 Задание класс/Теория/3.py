f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Теория\24.3.txt')
s = f.readline()
a = s.split('O')
maximum = 0
for i in range(len(a) - 1):
	if len(a[i] + a[i + 1]) > maximum:
		maximum = len(a[i] + a[i + 1])
print(maximum + 1)