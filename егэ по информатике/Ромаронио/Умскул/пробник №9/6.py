from turtle import *
left(90)
tracer(0)
screensize(5000, 5000)
k = 20

right(90)
for i in range(3):
    right(45)
    fd(15 * k)
    right(45)
right(315)
fd(15 * k)
for i in range(2):
    right(90)
    fd(15 * k)

pu()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3)
done()