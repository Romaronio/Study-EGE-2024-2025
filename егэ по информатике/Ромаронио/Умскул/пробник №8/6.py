from turtle import *
tracer(0)
left(90)
screensize(5000, 5000)
k = 10

for i in range(1):
    fd(11 * k)
    right(90)
    fd(32 * k)
    right(90)

fd(4 * k)
right(90)
fd(10 * k)

for i in range(2):
    right(90)
    fd(2 * k)

left(90)
fd(1 * k)
left(90)
fd(20 * k)

for i in range(2):
    left(90)
    fd(12 * k)

right(90)
fd(7 * k)
right(90)
fd(34 * k)
right(90)
fd(9 * k)
right(90)
fd(18 * k)
pu()

for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3)
done()