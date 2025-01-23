import string
alfa = '1234567890' + string.ascii_uppercase[:9]
for x in alfa:
	if (int(f'AB5{x}3', 18) + int(f'EF{x}13', 18)) % 17 == 0:
		print(x, int(f'AB5{x}3', 18) + int(f'EF{x}13', 18) // 17)
		break
