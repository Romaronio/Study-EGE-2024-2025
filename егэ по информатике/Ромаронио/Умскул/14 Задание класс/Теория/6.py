import string
alfa = '1234567890' + string.ascii_uppercase[:9]
for x in alfa:
	if (int(f'11A{x}3', 19) + int(f'12{x}345', 19)) % 14 == 0:
		print(x, (int(f'11A{x}3', 19) + int(f'12{x}345', 19)) // 14)
		break
