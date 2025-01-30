from turtle import *
left(90)
tracer(0)
k = 30
screensize(-5000, 5000)
for i in range(6):
	forward(3 * k)
	right(300)
pu()
forward(3 * k)
right(270)
forward(2 * k)
right(90)
pd()
for i in range(2):
	forward(3 * k)
	right(270)
	forward(4 * k)
	right(270)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		setpos(x * k, y * k)
		dot(3)
done()