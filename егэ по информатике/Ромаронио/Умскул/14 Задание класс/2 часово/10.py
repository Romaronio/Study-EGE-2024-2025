for x in '1234567890abcde':
	k = int(f'97968{x}15', 15) + int(f'7{x}233', 15)
	if k % 14 == 0:
		print(k // 14)
		break


