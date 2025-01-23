from turtle import *
left(90)
tracer(0)
k = 30
screensize(5000, 5000)
right(45)
forward(5 * k)
for i in range(7):
	right(45)
	forward(16 * k)
	right(135)
	forward(8 * k)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()
