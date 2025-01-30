from turtle import *
tracer(0)
left(90)
k = 20
for _ in range(100):
	forward(k * 10)
	right(80)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(k * x, k * y)
		dot(3)
done()
