from turtle import *
tracer(0)
left(90)
k = 20
for i in range(2):
	forward(5 * k)
	right(90)
	forward(6 * k)
	right(90)
pu()
forward(2 * k)
right(90)
back(4 * k)
left(90)
pd()
for w in range(2):
	forward(6 * k)
	right(90)
	forward(9 * k)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()