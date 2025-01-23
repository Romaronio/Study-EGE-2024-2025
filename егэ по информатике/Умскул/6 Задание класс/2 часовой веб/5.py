from turtle import *
left(90)
k = 20
tracer(0)
screensize(5000, 5000)
for i in range(10):
	forward(22 * k)
	right(90)
	forward(16 * k)
	right(90)
pu()
forward(1 * k)
right(90)
forward(1 * k)
left(90)
pd()
for i in range(9):
	forward(72 * k)
	right(90)
	forward(79 * k)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()