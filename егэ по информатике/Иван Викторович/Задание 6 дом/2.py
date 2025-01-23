from turtle import *
tracer(0)
left(90)
k = 20
right(45)
for _ in range(7):
	forward(5 * k)
	right(45)
	forward(10 * k)
	right(135)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()