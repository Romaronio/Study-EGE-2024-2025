from turtle import *
tracer(0)
left(90)
k = 10
for i in range(4):
	forward(19 * k)
	right(90)
	forward(30 * k)
	right(90)
pu()
forward(2 * k)
right(90)
forward(8 * k)
left(90)
pd()
for w in range(4):
	forward(93 * k)
	right(90)
	forward(97 * k)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()