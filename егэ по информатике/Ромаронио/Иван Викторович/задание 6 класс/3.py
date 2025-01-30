from turtle import *
tracer(0)
left(90)
k = 30
for _ in range(15):
	forward(k * 3)
	right(40)
pu()
for x in range(-30, 40):
	for y in range(-30, 40):
		goto(x * k, y * k)
		dot(3)

done()