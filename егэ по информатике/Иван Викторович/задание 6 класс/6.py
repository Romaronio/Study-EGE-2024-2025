from turtle import *
tracer(0)
left(90)
k = 5
for i in range(2):
	forward(k * 10)
	right(90)
	forward(k * 20)
	right(90)
pu()
back(k * 15)
right(90)
back(k * 10)
left(90)
pd()
for n in range(2):
	forward(k * 20)
	right(90)
	forward(k * 40)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(2)
done()