f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Теория\24.9.txt')
s = f.readline()
buff = s[0]
numbers = []
s = s.replace('*', '')
s = s.replace('-', '')
mas = [i for i in range(len(s) - 2)]
for i in mas:
		if int(s[i]) + int(s[i + 1]) >= 10:
			buff += s[i + 1]
		else:
			numbers.append(buff)
			buff = s[i + 1]
print(len(max(numbers, key=len)))