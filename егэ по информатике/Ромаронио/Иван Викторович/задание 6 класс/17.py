from turtle import *
tracer(0)
k = 10
x = 4
screensize(5000, 5000)
for _ in range(10):
	goto(xcor() + 3 * k, ycor() + 6 * k)
	goto(xcor() + 7 * k, ycor() - 2 * k)
	goto(xcor() - 10 * k, ycor() - 4 * k)

pu()
for x in range(-100, 40):
	for y in range(-100, 40):
		goto(x * k, y * k)
		dot(3)
done()
