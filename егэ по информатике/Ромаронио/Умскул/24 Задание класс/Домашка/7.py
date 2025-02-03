# import string
# f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Домашка\24.7.txt')
# s = f.readline()
# buff = ''
# numbers = []
# for i in range(len(s) - 1):
# 	if s[i] in '1234567890' and s[i + 1] in '1234567890':
# 		buff += s[i + 1]
# 		numbers.append(buff)
# 	else:
# 		buff = s[i + 1]
# res_mas = []
# for n in numbers:
# 	if len(n) == 6:
# 		if n[0] != '0':
# 			res_mas.append(int(n))
# print(min(res_mas))
# if len(numbers) == 6:
# 	print(min(numbers))
f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Домашка\24.7.txt')
s = f.readline()
for x in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
    s = s.replace(x, ' ')
a = s.split(' ')
min_str = 999999
for i in range(len(a)):
    if len(a[i]) == 6 and a[i][0] != '0':
        min_str = min(min_str, int(a[i]))
print(min_str)