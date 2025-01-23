# a = []
# for x in range(1, 1000):
# 	for y in range(1, 1000):
# 		a.append([x, y])

# a = [[x, y] for x in range(1, 1000) for y in range(1, 1000)]
# print(a)

# for a in range(1, 1000):
# 	print(list(((y + 7 * x != 36) or (a > x - 2) or (a < y + 27))for x in range(1, 1000) for y in range(1, 1000)))
for a in range(1, 1000):
	if all(((y + 7 * x != 36) or (a > x - 2) or (a < y + 27))for x in range(1, 1000) for y in range(1, 1000)) == True:
		print(a)
		break