from turtle import *
left(90)
k = 20
tracer(0)
screensize(5000, 5000)
for i in range(9):
	forward(5 * k)
	right(90)
	forward(4 * k)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()
