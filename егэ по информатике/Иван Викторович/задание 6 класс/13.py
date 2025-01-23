# from turtle import *
# tracer(0)
# left(90)
# k = 20
# x = 3
# for _ in range(4):
# 	forward(x * k)
# 	right(90)
# 	forward(x * k)
# 	left(90)
# 	forward(x * k)
# 	right(90)
# pu()
# for x in range(-40, 40):
# 	for y in range(-40, 40):
# 		goto(x * k, y * k)
# 		dot(3)
# done()

for x in range(1, 100):
	if(x-1)**2 * 5 + 4 * (x -1) > 20000:
		print(x)
		break