from turtle import *
left(90)
tracer(0)
screensize(5000, 5000)
k = 20

right(10)
for i in range(8):
    fd(1 * k)
    right(3)
    fd(5 * k)
    right(123)
    fd(6 * k)

pu()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3)
done()