res1 = []
for x in range(9):
	for y in range(9):
		res = int(f'88{x}4{y}', 9) + int(f'7{x}44{y}', 11)
		if res % 61 == 0:
			res1.append((res, res // 61))
print(min(res1))