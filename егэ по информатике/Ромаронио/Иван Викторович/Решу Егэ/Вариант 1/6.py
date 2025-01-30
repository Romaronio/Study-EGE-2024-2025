from turtle import *
tracer(0)
left(90)
k = 10
forward(100 * k)
right(90)
forward(100 * k)
right(30)
pd()
for w in range(10):
	forward(25 * k)
	right(90)
pu()
for x in range(40, 40):
	for y in range(40, 40):
			goto(x * k, y * k)
			dot(3)
done()