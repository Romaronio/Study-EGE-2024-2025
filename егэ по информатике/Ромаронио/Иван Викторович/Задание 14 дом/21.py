import string
alfa = '01234567890' + string.ascii_lowercase[:13]
for x in alfa:
	res = int(f'98{x}79641', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)
	if res % 18 == 0:
		print(res // 18)
		break