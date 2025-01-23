w = 2
from turtle import *
tracer(0)
left(90)
k = 10
for _ in range(2):
	forward(10 * k)
	right(90)
	forward(4 * k)
	right(90)
pu()
forward(3 * k)
right(90)
forward(6 * k)
left(90)
pd()
for _ in range(2):
	forward(8 * k)
	right(90)
	forward(6 * k)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(2)
done()
