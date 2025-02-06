f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Теория\24.14.txt')
s = f.readline()
buff = ''
res_mas = ''
s = s.replace('-', '*')
s = s.split('**')
buff = ''
res_max = ''
for i in s:
	if i[-1:] == '*':
		i = i[:-1]
	if '*0' in i:
		i = i.replace('*0', '*')
	if len(buff) < len(i):
		buff = i
print(len(buff), buff)