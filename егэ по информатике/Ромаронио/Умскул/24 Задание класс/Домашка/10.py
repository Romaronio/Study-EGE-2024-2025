f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Домашка\24.10.txt')
s = f.readline()
# buff = str(s[0])
# for i in range(0, len(s), -1):
# 	print(sum(int(i) for i in buff))
# 	if sum(int(i) for i in buff) ** len(buff) != int(buff):
# 		buff += s[i]
# 	else:
# 		number.append(buff)
# print(number)

# for i in range(10 ** 5):
# 	if sum(int(m) for m in str(i)) ** len(str(i)) == i:
# 		print(i)

k = s.count('2401')
print(k)