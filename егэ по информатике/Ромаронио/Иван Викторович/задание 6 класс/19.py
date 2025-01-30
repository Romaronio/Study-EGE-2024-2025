from turtle import *
tracer(0)
k = 30
x = 4
screensize(5000, 5000)
for _ in range(10):
	goto(xcor() + 3 * k, ycor() + 2 * k)
	goto(xcor() - 2 * k, ycor() + 3 * k)
	goto(xcor() - 3 * k, ycor() - 2 * k)
	goto(xcor() + 2 * k, ycor() - 3 * k)

pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(2)
done()
