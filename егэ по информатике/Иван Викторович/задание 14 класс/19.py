import string
alfa = '01234567890' + string.ascii_lowercase[:13]
for x in range(23):
	res = int(f'7{x}38596', 23) + int(f'14{x}36', 23) + int(f'61{x}7', 23)
	if res % 22 == 0:
		print(res // 22)
		break