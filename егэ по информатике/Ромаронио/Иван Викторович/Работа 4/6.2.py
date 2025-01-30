# from turtle import *
# tracer(0)
# left(90)
# k = 20
# x = 4
# forward((x + 2) * k)
# for _ in range(4):
# 	forward(x * k)
# 	right(90)
# 	forward((x + 2) * k)
# right(90)
# forward(2 * x * k)
# for _ in range(4):
# 	right(90)
# 	forward((3 * x - 1) * k)
# pu()
# for x in range(-40, 40):
# 	for y in range(-40, 40):
# 		goto(x * k, y * k)
# 		dot(3)
# done()

for x in range(1, 100):
	if ((2 * x + 2) ** 2 + (3 * x - 1) ** 2 - (2 * x * (x + 2))) > 2000:
		print(x)
		break