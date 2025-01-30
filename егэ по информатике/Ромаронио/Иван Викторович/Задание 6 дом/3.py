from turtle import *
tracer(0)
left(90)
k = 40
for _ in range(11):
	forward(4 * k)
	right(60)
pu()
for x in range(-40, 20):
	for y in range(-40, 20):
		goto(x * k, y * k)
		dot(3)
done()