from turtle import *
tracer(0)
left(90)
k = 50
for _ in range(12):
	forward(k * 6)
	right(120)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)

done()