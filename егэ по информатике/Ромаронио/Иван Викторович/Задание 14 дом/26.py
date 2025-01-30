# def f(a, n):
# 	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
# for p in range(7, 50):
# 	for x in range(p):
# 		for y in range(p):
# 			if f([3, 4], p) * f([5, 6], p) == f([x, y, 2], p):
# 				print(f([x, y], p))

def f(a, n):
	return(sum(a[::-1][i] * n ** i for i in range(len(a))))
for p in range(7, 50):
	for x in range(p):
		for y in range(p):
			if f([3, 4], p) * f([5, 6], p) == f([x, y, 2], p):
				print(f([y, x], p))