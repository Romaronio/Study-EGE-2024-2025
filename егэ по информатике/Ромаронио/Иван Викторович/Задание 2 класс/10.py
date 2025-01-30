print('x y z w F')
for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				print(x, y, z, w, int((x == (z <= y)) and (not w)))