from turtle import *
left(90)
tracer(0)
k = 20
screensize(5000, 5000)
for i in range(2):
	forward(13 * k)
	right(90)
	forward(20 * k)
	right(90)
pu()
forward(8 * k)
right(90)
back(3 * k)
left(90)
pd()
for i in range(2):
	forward(16 * k)
	right(90)
	forward(8 * k)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()

14 * 21
17 * 9
