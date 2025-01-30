from turtle import *
tracer(0)
left(90)
k = 20
for i in range(2):
	forward(6 * k)
	right(90)
	forward(12 * k)
	right(90)
pu()
forward(1 * k)
right(90) 
forward(3 * k)
left(90)
pd()
for w in range(2):
	forward(77 * k)
	right(90)
	forward(45 * k )
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()