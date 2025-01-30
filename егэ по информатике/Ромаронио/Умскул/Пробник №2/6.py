from turtle import *
left(90)
tracer(0)
k = 20
screensize(5000, 5000)
for i in range(4):
	forward(28 * k)
	right(90)
	forward(26 * k)
	right(90)
pu()
forward(8 * k)
right(90)
forward(7 * k)
left(90)
pd()
for i in range(4):
	forward(67 * k)
	right(90)
	forward(98 * k)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()

19