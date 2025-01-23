alfa = '01234567890abcd'
for x in range(14):
	res = int(f'1{x}563', 14) + int(f'871{x}3', 14)
	if res % 24 == 0:
		print(res // 24)
		break