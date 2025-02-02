f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Теория\24.8.txt')
s = f.readline()
buff = ''
res_mas = []
for i in range(len(s) - 1):
	if s[i] in '1234567890' and s[i + 1] in '1234567890':
		buff += s[i+1]
		if int(buff) % 2 == 1:
			res_mas.append(buff)
	else:
		buff = ''
print(max(res_mas, key=len))
