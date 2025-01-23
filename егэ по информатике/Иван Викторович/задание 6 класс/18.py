from turtle import *
tracer(0)
k = 10
x = 4
screensize(5000, 5000)
for _ in range(10):
	goto(xcor() + 6 * k, ycor() + 15 * k)
	goto(xcor() - 5 * k, ycor() - 5 * k)
	goto(2 * k, 2 * k)
	goto(xcor() - 1 * k, ycor() - 10 * k)

pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(2)
done()
