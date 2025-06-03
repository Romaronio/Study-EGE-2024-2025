# Текстовый файл состоит из символов, обозначающих знаки «-», «*» и цифры 0, 7, 8, 9. 
# Определите в прилагаемом файле максимальное количество идущих подряд символов, 
# которые образуют математически правильную последовательность, в которую входят 
# знаки « - » или « * » и натуральные числа без незначащих нулей

# f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24.txt Задание класс\Теория\24.txt.13.txt')
# s = f.readline()
# buff = ''
# res_mas = []
# for i in range(len(s) - 1):
# 	if s[i].isdigit():
# 		buff += s[i]
# 	elif s[i] in '-*' and s[i - 1].isdigit() and s[i + 1] != '0':
# 		buff += s[i]
# 	else:
# 		res_mas.append(buff)
# 		buff = ''
# for n in res_mas:
# 	if len(n) == 41:
# 		print(n)


f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Теория\24.13.txt')
s = f.readline()
s = s.replace('-', '*')
s = s.split('*')
buff = ''
res_mas = ''
for i in s:
	if len(i) != 0 and i[0] != '0' and int(i) != 0:
		buff += i + '*'
	elif len(i) > 0 and i[0] == '0':
		buff = str(int(i))
	else:
		buff = ""
	res_mas = max(buff, res_mas, key=len)
print(len(res_mas))
