f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Теория\24.4.txt')
s = f.readline()
s = s.replace('U', 'G').replace('A', 'G').replace('S', 'C').replace('T', 'C').replace('R', 'C')
len_max = 0
for i in range(100):
	if 'GC' * i in s:
		print(i)