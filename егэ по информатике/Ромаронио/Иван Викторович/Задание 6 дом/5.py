from turtle import *
tracer(0)
left(90)
k = 20
for _ in range(3):
	forward(7 * k)
	right(90)
forward(10 * k)
for _ in range(3):
	left(90)
	forward(6 * k)

pu()
for x in range(-40, 20):
	for y in range(-40, 20):
		goto(x * k, y * k)
		dot(3)
done()