import string
digits26 = string.digits + string.ascii_lowercase
for x in digits26[:26]:
	flag = 1
	for y in digits26[:26]:
		s = int(f'13{y}{x}5', 26) + int(f'24{y}13', 26)
		if s % 8 != 0:
			flag = 0
			break
	if flag:
		y = 2
		s = int(f'13{y}{x}5', 26) + int(f'24{y}13', 26)
		print(x, s // 8)

			