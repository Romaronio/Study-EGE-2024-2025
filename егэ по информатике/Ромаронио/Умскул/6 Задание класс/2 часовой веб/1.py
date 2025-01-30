from turtle import *
left(90)
k = 20
tracer(0)
pd()
screensize(5000, 5000)
for i in range(2):
	forward(10 * k)
	right(90)
	forward(18 * k)
	right(90)
pu()
forward(5 * k)
right(90)
forward(7 * k)
left(90)
pd()
for i in range(2):
	forward(10 * k)
	right(90)
	forward(7 * k)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()


