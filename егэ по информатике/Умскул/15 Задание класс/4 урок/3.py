p = list(range(13, 34))
q = list(range(22, 45))
a = []
for x in range(1, 100):
	if (((x in p) and (x in q)) <= (x in a)) == 0:
		a.append(x)
print(a, 33 - 22)