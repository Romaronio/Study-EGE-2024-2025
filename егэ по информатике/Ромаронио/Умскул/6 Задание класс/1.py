from turtle import *
left = 90
tracer(0)
k = 20
screensize(5000, 5000)
for _ in range(12):
	right(90)
	forward(125 * k)
	right(90)
	forward(17 * k)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()

