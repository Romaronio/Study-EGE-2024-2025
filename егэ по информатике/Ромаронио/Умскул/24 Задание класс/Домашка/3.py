f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Домашка\24.3.txt')
s = f.readline()
# buff = ''
# res_mas = []
s = s.replace('M', 'C').replace('K', 'C').replace('E', 'G').replace('I', 'G').replace('O', 'G')
# for i in range(len(s) - 1):
# 	if s[i] + s[i + 1] == 'GC':
# 		buff = buff + 'GC'
# 		res_mas.append(buff)
# 	else:
# 		buff = ''
# print(max(res_mas, key=len))
for i in range(len(s) - 1):
	if 'GC' * i in s:
		print(i)