from turtle import *
tracer(0)
left(90)
k = 20
for i in range(45):
	forward(k * 10)
	right(8)
pu()
for x in range(-40, 20):
	for y in range(-40, 20):
		goto(x * k, y * k)
		dot(3)
done()