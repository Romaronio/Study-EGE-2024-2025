p = list(range(31, 49))
q = list(range(37, 57))
a = []
for x in range(1, 100):
	if (((x in p) and (x in q)) <= (x in a)) == 0:
		a.append(x)
print(a)