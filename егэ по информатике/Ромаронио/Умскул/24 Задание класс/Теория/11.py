f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Теория\24.11.txt')
res_mas = []
for i, s in enumerate(f, start=1):
	try:
		if eval(s):
			res_mas.append([eval(s), i])
	except:
		pass
print(max(res_mas))
print(sorted(res_mas, reverse=True)[:10])





# for s in f:
# 	try:
# 		if eval(s):
# 			for i, x in enumerate(s):
# 				print(i + 1, exec(s))
# 	except:
# 		pass