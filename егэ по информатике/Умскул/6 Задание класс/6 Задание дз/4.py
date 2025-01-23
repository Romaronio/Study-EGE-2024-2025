from turtle import *
left(90)
k = 30
tracer(0)
screensize(5000, 5000)
right(45)
forward(4 * k)
for i in range(10):
	right(45)
	forward(7 * k)
	right(135)
	forward(4 * k)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()
