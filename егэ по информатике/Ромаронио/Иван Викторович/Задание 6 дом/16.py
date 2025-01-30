# from turtle import *
# tracer(0)
# left(90)
# k = 10
# x =10
# screensize(5000, 5000)
# for i in range(2):
# 	forward(3 * x * k)
# 	right(90)
# 	forward(x * k)
# 	right(90)
# 	for m in range(2):
# 		forward(x * k)
# 		left(90)
# 	for n in range(2):
# 		forward(x * k)
# 		right(90)
# pu()
# for x in range(-40, 40):
# 	for y in range(-40, 40):
# 		goto(x * k, y * k)
# 		dot(3)
# done()
for x in range(1, 1000):
	s = x ** 2 * 7
	if s > 200000:
		print(x)
		break