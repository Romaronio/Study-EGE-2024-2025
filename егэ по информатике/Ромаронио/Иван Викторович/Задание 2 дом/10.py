print('x y z w')
for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				if not(((w <= y) <= x) or not(z)):
					print(x, y, z, w)
	
