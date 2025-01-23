from turtle import *
tracer(0)
k = 20
screensize(5000, 5000)
for i in range(11):
	goto(xcor() + 4 * k, ycor() + 4 * k)
	goto(xcor() - 9 * k, ycor() + 1 * k)
	goto(xcor() + 5 * k, ycor() - 5 * k)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()