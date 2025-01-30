p = list(range(11, 29))
q = list(range(21, 43))
a = list(range(1, 100))
for x in range(1, 100):
	if (((x in p) <= (x in q)) <= (not(x in a))) == 0:
		a.remove(x)
print(a, 21 - 11)