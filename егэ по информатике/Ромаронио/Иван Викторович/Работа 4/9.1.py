
for x in range(0, 22):
	s = int(f'18{x}89957', 22) + int(f'80{x}33', 22) + int(f'521{x}6', 22)
	if s % 21 == 0:
		print(s // 21)
		break