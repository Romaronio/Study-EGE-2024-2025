f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Теория\24.10.txt')
num = 1
mas_res = {}
for s in f:
	mas_res[len(s)] = num
	num += 1
print(mas_res[40])

# mas1 = [2, 4, 3, 5, 1, 6]
# mas2 = ['s', 'a', 'e', 'd', 'g', 'q']
# obj = {}
# for i in range(len(mas1)):
# 	obj[mas1[i]] = mas2[i]
# 	keys = [k for k in obj]
# print(obj)
# for i, key in enumerate(keys):
# 	print(obj[keys[i]], key)