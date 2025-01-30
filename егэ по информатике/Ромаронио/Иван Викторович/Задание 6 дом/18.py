# from turtle import *
# tracer(0)
# left(90)
# k = 20
# x = 6
# screensize(5000, 5000)
# forward(5 * k)
# while x:
# 	forward(x * k)
# 	right(90)
# 	forward(3 * k)	
# 	right(90)
# 	forward(x * k)
# 	left(90)
# 	forward(k)
# 	left(90)
# 	x -= 1
# back(5 * k)
# pu()
# for x in range(-40, 40):
# 	for y in range(-40, 40):
# 		goto(x * k, y * k)
# 		dot(3)
# done()
s1, s2 = 0, 0
for x in range(1, 1000000): 
	s1 += 16 + (x * 2)
	if s1 - 4  > 5500000:
		print(x - 1)
		break
		