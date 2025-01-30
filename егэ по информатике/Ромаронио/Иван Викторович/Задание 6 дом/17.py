# from turtle import *
# tracer(0)
# left(90)
# k = 20
# x = 4
# screensize(5000, 5000)
# for i in range(3):
# 	forward(3 * x * k)
# 	right(90)
# forward(x * k)
# right(90)
# forward(2 * x * k)
# left(90)
# forward(x * k)
# left(90)
# forward(2 * x * k)
# right(90)
# forward(x * k)
# pu()
# for x in range(-40, 40):
# 	for y in range(-40, 40):
# 		goto(x * k, y * k)
# 		dot(3)
# done()
for x in range(1, 10000):
	s = (x - 1) ** 2 * 7
	s2 = (x - 1) * 6
	if s + s2 > 400000: 
		print(x)
		break