print('x y z w')
for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				f = ((w <= z) == (x <= (not(y)))) and (x or z)
				print(x, y, z, w, '--', int(f))	 


# x y z w
# 0 0 1 0 -- 1
# 0 0 1 1 -- 1 p
# 0 1 1 0 -- 1 p
# 1 0 0 0 -- 1 p	
# 1 0 1 0 -- 1
# 1 0 1 1 -- 1
# 1 1 1 0 -- 0 p