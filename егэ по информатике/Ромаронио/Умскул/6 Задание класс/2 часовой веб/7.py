# from turtle import *
# left(90)
# k = 30
# tracer(0)
# screensize(5000, 5000)
# right(90)
# for i in range(3):
# 	right(45)
# 	forward(10 * k)
# 	right(45)
# right(315)
# forward(10 * k)
# for i in range(2):
# 	right(90)
# 	forward(10 * k)
# pu()
# for x in range(-40, 40):
# 	for y in range(-40, 40):
# 		goto(x * k, y * k)
# 		dot(3)
# done()
k = 0
import math
for x in range(-1000, 1000):
	for y in range(-1000, 1000):
		y1 = x + 10 * (2 ** (1/2))
		y2 = -x - 10*(2 ** (1/ 2))
		y3 = x - 10 * (2 ** (1/2))
		y4 = -x 
		if y < y1 and y < y4 and y > y2 and y > y3:
			k += 1
print(k)
