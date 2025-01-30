from turtle import *
tracer(0)
left(90)
k = 20
screensize(5000, 5000)
right(180)
forward(2 * k)
right(90)
forward(40 * k)
right(90)
forward(2 * k)
for x in range(4):
	seth(90)
	circle(-5 * k, 180)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()
