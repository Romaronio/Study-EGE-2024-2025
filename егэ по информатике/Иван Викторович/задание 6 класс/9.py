from turtle import *
tracer(0)
left(90)
k = 15
for i in range(2):
	forward(k * 6)
	right(90)
	forward(k * 4)
	right(90)
pu()
forward(k * 2)
right(90)
back(k * 4)
left(90)
pd()
for n in range(2):
	forward(k * 5)
	right(90)
	forward(k * 7)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()	