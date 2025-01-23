from turtle import *
tracer(0)
left(90)
k = 30
for _ in range(5):
	for i in range(3):
		forward(4 * k)
		left(90)
	forward(2 * k)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()