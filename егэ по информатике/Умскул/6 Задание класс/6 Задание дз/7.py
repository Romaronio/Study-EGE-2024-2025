from turtle import *
left(90)
k = 20
tracer(0)
screensize(5000, 5000)
for i in range(5):
	forward(10 * k)
	right(144)
	forward(10 * k)
	left(72)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()
