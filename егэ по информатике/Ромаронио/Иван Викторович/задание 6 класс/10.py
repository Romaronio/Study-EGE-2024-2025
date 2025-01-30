from turtle import *
tracer(0)
left(90)
k = 10
screensize(5000, 5000)
for i in range(2):
	forward(k * 22)
	right(90)
	forward(k * 6)
	right(90)
pu()
forward(k * 1)
right(90)
forward(k * 5)
left(90)
pd()
for n in range(2):
	forward(k * 53)
	right(90)
	forward(k * 75)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()	