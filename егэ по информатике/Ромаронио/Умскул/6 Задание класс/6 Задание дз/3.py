from turtle import *
left(90)
k = 30
tracer(0)
screensize(5000, 5000)
for i in range(2):
	forward(13 * k)
	right(90)
	forward(5 * k)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()
