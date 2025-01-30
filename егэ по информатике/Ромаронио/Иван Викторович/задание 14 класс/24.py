for x in range(9, -1, -1):
	f1 = 1 * int(f'123{x}4') ** 2 + 3
	f2 = 1 * int(f'12{x}43') ** 2 + 2 
	if((f1 + f2) % 50) == 0:
		print((f1 + f2) // 50)