from turtle import *
tracer(0)
left(90)
k = 20
for i in range(4):
	for w in range(4):
		for i in range(4):
			forward(k * 3)
			right(120)
		forward(3 * k)
	forward(6 * k)
pu()
for x in range(-40, 20):
	for y in range(-40, 20):
		goto(x * k, y * k)
		dot(3)
done()