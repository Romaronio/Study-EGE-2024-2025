import string
alfa = '01234567890' + string.ascii_lowercase[:13]
for x in range(19):
	res = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
	if res % 18 == 0:
		print(res // 18)

import string
alfa = '01234567890' + string.ascii_lowercase[:13]
for x in range(23):
	res = int(f'7{x}38596', 23) + int(f'14{x}36', 23) + int(f'61{x}7', 23)
	if res % 22 == 0:
		print(res // 22)
		break