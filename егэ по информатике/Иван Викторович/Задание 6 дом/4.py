from turtle import *
tracer(0)
left(90)
k = 20
for _ in range(5):
	forward(9 * k)
	right(90)
	forward(3 * k)
	right(90)

pu()
for x in range(-40, 20):
	for y in range(-40, 20):
		goto(x * k, y * k)
		dot(3)
done()