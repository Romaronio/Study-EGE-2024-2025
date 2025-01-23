summ = 0
for n in range(2, 11):
	x = 1988
	flag = True
	prev = -1
	while x:
		if (x % n) == prev:
			flag == False
		prev = x % n
		x//= n
	if flag: summ += n
print(summ)


