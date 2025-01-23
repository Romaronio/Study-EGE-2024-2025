from turtle import *
tracer(0)
left(90)
k = 10
for i in range(-40, 40):
	right(90)
	forward(k * 100)
pu()
for x in range(-40, 20):
	for y in range(-40, 20):
		goto(x * k, y * k)
		dot(3)
done()
