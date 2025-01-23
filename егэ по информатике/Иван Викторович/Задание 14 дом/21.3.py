for x in range(16):
	res = int(f'2{x}84', 16) + int(f'2b3{x}', 16)
	if res % 88 == 0:
		print(res // 88)
		break