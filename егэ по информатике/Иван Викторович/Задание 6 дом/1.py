from turtle import *
tracer(0)
left(90)
right(45)
k = 30
for _ in range(9):
	forward(k * 9)
	right(90)
pu()
for x in range(-40, 80):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()