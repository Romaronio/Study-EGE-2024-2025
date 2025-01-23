for x in range(10):
	k = int(f'4c{x}4', 15) + int(f'{x}62A', 13)
	if k % 121 == 0:
		print(k // 121)
		break

