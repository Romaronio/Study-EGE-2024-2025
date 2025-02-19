f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\9 Задание класс\09.txt')
res_mas = []
def four(s):
	for i in range(0, len(s), 4):
		mas = s[i:i+4]
		res_mas.append(mas)
n = f.read()
s = [int(i) for i in n.split()]
four(s)
k1 = 0
k2 = 0
for m in res_mas:
	if len(set(m)) == 4:
		Nepovtor = set(m)
		if ((max(Nepovtor) + min(Nepovtor)) // 2) in Nepovtor:
			k1 += 1
	else:
		m.sort()
		if m.count(m[0]) == 2:
			if m[0] ** 2 + m[1] ** 2 < m[2] ** 2 + m[3] ** 2:
				k2 += 1
		elif m.count(m[0]) == 3:
			if m[0] ** 2 + m[1] ** 2 + m[2] ** 2 < m[3] ** 2:
				k2 += 1
		elif m.count(m[1]) == 2 and m[1] != m[0]:
			if m[1] ** 2 + m[2] ** 2 < m[0] ** 2 + m[3] ** 2:
				k2 += 1
		elif m.count(m[1]) == 3 and m[1] != m[0]:
			if m[1] ** 2 + m[2] ** 2 + m[3] ** 2 < m[0] ** 2:
				k2 += 1
		elif m.count(m[2]) == 2 and m[2] != m[1]:
			if m[2] ** 2 + m[3] ** 2 < m[0] ** 2 + m[1] ** 2:
				k2 += 1
print(k1 + k2)