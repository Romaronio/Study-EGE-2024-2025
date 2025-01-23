from turtle import *
left(90)
k = 20
tracer(0)
screensize(5000, 5000)
for i in range(3):
	forward(7 * k)
	right(90)
	forward(12 * k)
	right(90)
pu()
forward(4 * k)
right(90)
forward(6 * k)
left(90)
pd()
for i in range(9):
	forward(83 * k)
	right(90)
	forward(77 * k)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()