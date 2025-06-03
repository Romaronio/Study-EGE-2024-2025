# from string import *
# f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24.txt Задание класс\Домашка\24.txt.11.txt')
# s = f.read()
# s = s.split()
# res_mas = []
# Bukv = set()
# non = []
# nonalfa = 'EFGHIJKLMNOPQRSTUVWXYZ'
# alfa = '123456789ABCD'
# def BukvaInStroka(Chislo):
# 	for i in Chislo:
# 		if i in nonalfa:
# 			break
# 	else:
# 		return Chislo
# for i in s:
# 	Bukv.add(BukvaInStroka(i))
# Bukv.remove(None)
# def Sis():
# 	for i in Bukv:
# 		if alfa[-1] in i:
# 			res_mas.append(int(i, 14))
# 		if alfa[-2] in i and not(alfa[-1]) in i:
# 			res_mas.append(int(i, 13))
# 		if alfa[-2] in i and not(alfa[-1]) in i:
# 			res_mas.append(int(i, 12))
# 		if alfa[-2] in i and not(alfa[-1]) in i:
# 			res_mas.append(int(i, 11))
# 		if alfa[-2] in i and not(alfa[-1]) in i:
# 			res_mas.append(int(i, 13))
# 		if alfa[-2] in i and not(alfa[-1]) in i:
# 			res_mas.append(int(i, 13))
# 		if alfa[-2] in i and not(alfa[-1]) in i:
# 			res_mas.append(int(i, 13))
# 		if alfa[-2] in i and not(alfa[-1]) in i:
# 			res_mas.append(int(i, 13))
# 		if alfa[-2] in i and not(alfa[-1]) in i:
# 			res_mas.append(int(i, 13))
# 	return res_mas
# print(Sis())



import string
def check(a, b):
    for i in range(len(a)):
        if not (a[i] in b):
            return False
    return True
f = open(r'C:\Users\spiri\Desktop\подготовка\егэ по информатике\Ромаронио\Умскул\24 Задание класс\Домашка\24.11.txt')
d = {}
cc = [str(i) for i in range(1, 10)] + list(string.ascii_uppercase)
d = d.fromkeys(cc, 0)
o = 2
for i in cc:
    d[i] = o
    o += 1
a = []
cnt = 0
for x in f:
    x = x[:-1]
    if x[0] != '0' and check(list(set(x)), [str(i) for i in range(0, 10)] + ['A', 'B', 'C', 'D']) \
    and sorted(x)[-1] != '0' and int(x, d[sorted(x)[-1]]) % 15 == 0: 
        cnt += 1
        print(x)
print(cnt)