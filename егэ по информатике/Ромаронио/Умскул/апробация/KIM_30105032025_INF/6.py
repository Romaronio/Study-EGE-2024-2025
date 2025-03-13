from turtle import *
left(90)
k = 15
tracer(0)
screensize(5000, 5000)
for _ in range(9):
  forward(27 * k)
  right(90)
  forward(30 * k)
  right(90)
pu()
forward(3 * k)
right(90)
forward(6 * k)
left(90)
pd()
for _ in range(9):
  forward(77 * k)
  right(90)
  forward(66 * k)
  right(90)
pu()
for x in range(-40, 40):
  for y in range(-40, 40):
    goto(x * k, y * k)
    dot(3)
done()